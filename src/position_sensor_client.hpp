#pragma once

#include <grpcpp/grpcpp.h>
#include <position_sensor.grpc.pb.h> // services
#include <position_sensor.pb.h>      // messages
#include <string>

/**
 * @ref
 * [webots/include/controller/cpp/webots/PositionSensor.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/PositionSensor.hpp)
 * @see webots/src/controller/cpp/PositionSensor.cpp
 * @see webots/lib/controller/python/controller/position_sensor.py
 * @see [Webots Reference Manual - PositionSensor](https://www.cyberbotics.com/doc/reference/positionsensor)
 */
class PositionSensorClient
{
public:
  PositionSensorClient(const std::shared_ptr<grpc::Channel>& channel);
  ~PositionSensorClient();

  // Enable the position sensor
  bool Enable(const std::string& sensor_name, int sampling_period);

  // Disable the position sensor
  bool Disable(const std::string& sensor_name);

  // Get the sampling period of the position sensor
  int GetSamplingPeriod(const std::string& sensor_name);

  // Get the value of the position sensor
  double GetValue(const std::string& sensor_name);

  // Get the type of the position sensor
  webots::GetTypeResponse::Type GetType(const std::string& sensor_name);

  // Get the brake tag associated with the position sensor
  int GetBrakeTag(const std::string& sensor_name);

  // Get the motor tag associated with the position sensor
  int GetMotorTag(const std::string& sensor_name);

private:
  std::unique_ptr<webots::PositionSensorService::Stub> stub_;
};
