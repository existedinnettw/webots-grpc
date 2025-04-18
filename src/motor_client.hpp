#pragma once

#include <grpcpp/grpcpp.h>
#include <motor.grpc.pb.h> //services
#include <motor.pb.h>      //messages
#include <string>

class MotorClient
{
public:
  MotorClient(const std::shared_ptr<grpc::Channel>& channel);
  ~MotorClient();

  // Set motor position
  bool SetPosition(const std::string& motor_name, double position);

  // Get motor minimum position
  double GetMinPosition(const std::string& motor_name);

  // Get motor maximum position
  double GetMaxPosition(const std::string& motor_name);

private:
  std::unique_ptr<webots::MotorService::Stub> stub_;
};