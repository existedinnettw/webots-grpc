#include "webots-grpc-client.hpp"

#include <gtest/gtest.h>
#include <iostream>
#include <limits>
#include <memory>
#include <random>
#include <string>
#include <vector>

class WebotsApiTest : public ::testing::Test
{
protected:
  std::shared_ptr<grpc::Channel> channel;
  std::unique_ptr<RobotClient> robot;
  std::unique_ptr<MotorClient> motor;
  std::unique_ptr<PositionSensorClient> position_sensor;
  std::unique_ptr<DistanceSensorClient> distance_sensor;

  void SetUp() override
  {
    channel = grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials());
    robot = std::make_unique<RobotClient>(channel);
    motor = std::make_unique<MotorClient>(channel);
    position_sensor = std::make_unique<PositionSensorClient>(channel);
    distance_sensor = std::make_unique<DistanceSensorClient>(channel);
  }
};

TEST_F(WebotsApiTest, GetRobotName)
{
  std::string name = robot->GetRobotName();
  ASSERT_FALSE(name.empty());
  ASSERT_EQ(name, "robot");
}

TEST_F(WebotsApiTest, GetBasicTimeStep)
{
  int timestep = robot->GetBasicTimeStep();
  ASSERT_GT(timestep, 0);
}

TEST_F(WebotsApiTest, GetDeviceList)
{
  auto devices = robot->GetDeviceList();
  ASSERT_FALSE(devices.empty());
}

TEST_F(WebotsApiTest, MotorApi)
{
  auto devices = robot->GetDeviceList();
  std::vector<std::string> motor_names;
  for (const auto& d : devices) {
    if ((d.find("motor") != std::string::npos || d.find("_to_") != std::string::npos) &&
        d.find("sensor") == std::string::npos) {
      motor_names.push_back(d);
    }
  }
  ASSERT_FALSE(motor_names.empty());
  std::string motor_name = motor_names[0];
  ASSERT_EQ(motor_name, "linear motor");

  auto device_name = robot->GetDevice(motor_name);
  ASSERT_EQ(device_name, motor_name);

  double max_pos = motor->GetMaxPosition(motor_name);
  double min_pos = motor->GetMinPosition(motor_name);
  ASSERT_NEAR(max_pos, 0.2, 1e-6);
  ASSERT_NEAR(min_pos, 0.0, 1e-6);

  std::string pos_sensor_name = motor->GetPositionSensor(motor_name);
  ASSERT_EQ(pos_sensor_name, "linear motor sensor");

  // ASSERT_TRUE(position_sensor->Disable(pos_sensor_name));
  // double value = position_sensor->GetValue(pos_sensor_name);
  // std::cout << std::format("Value of position sensor '{}' after disabling: {}\n", pos_sensor_name, value);
  // EXPECT_FALSE(std::isfinite(value));

  ASSERT_TRUE(position_sensor->Enable(pos_sensor_name, 32));
  ASSERT_TRUE(robot->Step(32));
  ASSERT_TRUE(std::isfinite(position_sensor->GetValue(pos_sensor_name)));

  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_real_distribution<> dis(0, 1);
  double position = min_pos + (max_pos - min_pos) * dis(gen);
  ASSERT_TRUE(motor->SetPosition(motor_name, position));
  ASSERT_TRUE(robot->Step(500));

  double updated_value = position_sensor->GetValue(pos_sensor_name);
  ASSERT_NEAR(updated_value, position, 0.01);
}

TEST_F(WebotsApiTest, MotorSpeedApi)
{
  std::string motor_name = "linear motor";
  std::string pos_sensor_name = "linear motor sensor";

  // Enable position sensor
  ASSERT_TRUE(position_sensor->Enable(pos_sensor_name, 32));

  // Set initial position to 0.1
  ASSERT_TRUE(motor->SetPosition(motor_name, 0.1));
  ASSERT_TRUE(robot->Step(320));
  double max_velocity = motor->GetMaxVelocity(motor_name);
  EXPECT_NEAR(max_velocity, 10.0, 1e-6); // from robot model

  {
    // https://cyberbotics.com/doc/reference/motor?tab-language=python#velocity-control
    ASSERT_TRUE(motor->SetPosition(motor_name, -std::numeric_limits<double>::infinity()));
    ASSERT_TRUE(motor->SetVelocity(motor_name, 0.5));
    double motor_velocity = motor->GetVelocity(motor_name);
    EXPECT_NEAR(motor_velocity, 0.5, 1e-6);
    ASSERT_TRUE(robot->Step(600));
    double value = position_sensor->GetValue(pos_sensor_name);
    ASSERT_NEAR(value, 0.0, 0.05);
  }

  {
    ASSERT_TRUE(motor->SetPosition(motor_name, std::numeric_limits<double>::infinity()));
    ASSERT_TRUE(motor->SetVelocity(motor_name, 0.5));
    ASSERT_TRUE(robot->Step(600));
    double value = position_sensor->GetValue(pos_sensor_name);
    ASSERT_NEAR(value, 0.2, 0.05);
  }
}

TEST_F(WebotsApiTest, DistanceSensorApi)
{
  std::string motor_name = "linear motor";
  std::string pos_sensor_name = "linear motor sensor";
  std::string pos_ds_name = "pos ds";
  std::string neg_ds_name = "neg ds";
  std::string home_ds_name = "home ds";
  int sample_period = 32;

  ASSERT_TRUE(position_sensor->Enable(pos_sensor_name, sample_period));
  ASSERT_TRUE(distance_sensor->Enable(pos_ds_name, sample_period));
  ASSERT_TRUE(distance_sensor->Enable(neg_ds_name, sample_period));
  ASSERT_TRUE(distance_sensor->Enable(home_ds_name, sample_period));

  struct AnsMatRow
  {
    std::function<bool(double)> neg, home, pos;
  };
  std::vector<AnsMatRow> ans_mat = {
    { [](double x) { return x > 3000; }, [](double x) { return x < 1000; }, [](double x) { return x < 1000; } },
    { [](double x) { return x < 1000; }, [](double x) { return x < 1000; }, [](double x) { return x < 1000; } },
    { [](double x) { return x < 1000; }, [](double x) { return x < 1000; }, [](double x) { return x > 3000; } }
  };
  std::vector<double> target_positions = { 0, 0.1, 0.2 - 1e-6 };
  for (size_t i = 0; i < target_positions.size(); ++i) {
    double target_pos = target_positions[i];
    ASSERT_TRUE(motor->SetPosition(motor_name, target_pos));
    ASSERT_TRUE(robot->Step(500));

    double pos_value = position_sensor->GetValue(pos_sensor_name);
    ASSERT_NEAR(pos_value, target_pos, 0.01);

    double neg_val = distance_sensor->GetValue(neg_ds_name);
    double home_val = distance_sensor->GetValue(home_ds_name);
    double pos_val = distance_sensor->GetValue(pos_ds_name);

    EXPECT_TRUE(ans_mat[i].neg(neg_val));
    EXPECT_TRUE(ans_mat[i].home(home_val));
    EXPECT_TRUE(ans_mat[i].pos(pos_val));
  }
}
