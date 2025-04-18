#pragma once

#include <device.grpc.pb.h> // service
#include <device.pb.h>      // message
#include <grpcpp/grpcpp.h>
#include <string>

class DeviceClient
{
public:
  DeviceClient(const std::shared_ptr<grpc::Channel>& channel)
    : stub_(webots::DeviceService::NewStub(channel))
  {
  }

  // Example method to get device model
  std::string GetDeviceModel(const std::string& device_name);

private:
  std::unique_ptr<webots::DeviceService::Stub> stub_;
};