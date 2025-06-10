#pragma once

#include <grpcpp/grpcpp.h>
#include <robot.grpc.pb.h>
#include <robot.pb.h> // message
#include <string>
#include <vector>

// webots grpc robot client
class RobotClient
{
public:
  RobotClient(const std::shared_ptr<grpc::Channel>& channel);
  ~RobotClient();

  // Method to get the robot's name
  std::string GetRobotName();

  // Method to get the robot's model
  std::string GetRobotModel();

  // Method to get custom data
  std::string GetCustomData();

  // Method to set custom data
  bool SetCustomData(const std::string& data);

  // Method to get a device by its name
  std::string GetDevice(const std::string& device_name);

  // Method to get the list of devices
  std::vector<std::string> GetDeviceList();

  // Method to perform a simulation step
  bool Step(int32_t time_step);

  // Method to get the basic time step
  double GetBasicTimeStep();

private:
  std::unique_ptr<webots::RobotService::Stub> stub_; // gRPC stub for RobotService
};