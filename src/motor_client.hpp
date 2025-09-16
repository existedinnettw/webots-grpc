#pragma once

#include <grpcpp/grpcpp.h>
#include <motor.grpc.pb.h> //services
#include <motor.pb.h>      //messages
#include <string>

/**
 * @ref webots/include/controller/cpp/webots/Motor.hpp
 */
class MotorClient
{
public:
  MotorClient(const std::shared_ptr<grpc::Channel>& channel);
  ~MotorClient();

  // Set motor position
  bool SetPosition(const std::string& motor_name, double position);

  // Set motor velocity
  bool SetVelocity(const std::string& motor_name, double velocity);

  // Get motor velocity
  double GetVelocity(const std::string& motor_name);

  // Get motor maximum velocity
  double GetMaxVelocity(const std::string& motor_name);

  // Get motor minimum position
  double GetMinPosition(const std::string& motor_name);

  // Get motor maximum position
  double GetMaxPosition(const std::string& motor_name);

  /**
   * @brief Get the position sensor name associated with the motor.
   */
  std::string GetPositionSensor(const std::string& motor_name);

private:
  std::unique_ptr<webots::MotorService::Stub> stub_;
};