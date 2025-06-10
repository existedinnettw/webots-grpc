#pragma once

#include <distance_sensor.grpc.pb.h> // services
#include <distance_sensor.pb.h>      // messages
#include <grpcpp/grpcpp.h>
#include <memory>
#include <string>

class DistanceSensorClient
{
public:
  DistanceSensorClient(const std::shared_ptr<grpc::Channel>& channel);
  ~DistanceSensorClient();

  // Enable the distance sensor
  bool Enable(const std::string& sensor_name, int sampling_period);

  // Disable the distance sensor
  bool Disable(const std::string& sensor_name);

  // Get the sampling period of the distance sensor
  int GetSamplingPeriod(const std::string& sensor_name);

  // Get the value of the distance sensor
  double GetValue(const std::string& sensor_name);

private:
  std::unique_ptr<webots::DistanceSensorService::Stub> stub_;
};