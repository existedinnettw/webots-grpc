#include "webots-grpc-client.hpp"
#include <google/protobuf/empty.pb.h> // Include the protobuf Empty message
#include <iostream>

RobotClient::RobotClient(const std::shared_ptr<grpc::Channel>& channel)
  : stub_(webots::RobotService::NewStub(channel))
{
}

RobotClient::~RobotClient()
{
}

std::string
RobotClient::GetRobotName()
{
  google::protobuf::Empty request; // Use google::protobuf::Empty
  webots::RobotNameResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetRobotName(&context, request, &response);

  if (status.ok()) {
    return response.name();
  } else {
    std::cerr << "GetRobotName RPC failed: " << status.error_message() << std::endl;
    return "";
  }
}

std::string
RobotClient::GetRobotModel()
{
  google::protobuf::Empty request; // Use google::protobuf::Empty
  webots::RobotModelResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetRobotModel(&context, request, &response);

  if (status.ok()) {
    return response.model();
  } else {
    std::cerr << "GetRobotModel RPC failed: " << status.error_message() << std::endl;
    return "";
  }
}

std::string
RobotClient::GetCustomData()
{
  google::protobuf::Empty request; // Use google::protobuf::Empty
  webots::CustomDataResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetCustomData(&context, request, &response);

  if (status.ok()) {
    return response.data();
  } else {
    std::cerr << "GetCustomData RPC failed: " << status.error_message() << std::endl;
    return "";
  }
}

bool
RobotClient::SetCustomData(const std::string& data)
{
  webots::CustomDataRequest request;
  request.set_data(data);
  google::protobuf::Empty response; // Use google::protobuf::Empty
  grpc::ClientContext context;

  grpc::Status status = stub_->SetCustomData(&context, request, &response);

  if (status.ok()) {
    return true;
  } else {
    std::cerr << "SetCustomData RPC failed: " << status.error_message() << std::endl;
    return false;
  }
}

std::string
RobotClient::GetDevice(const std::string& device_name)
{
  webots::DeviceRequest request;
  request.set_name(device_name);
  webots::DeviceResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetDevice(&context, request, &response);

  if (status.ok()) {
    return response.name();
  } else {
    std::cerr << "GetDevice RPC failed: " << status.error_message() << std::endl;
    return "";
  }
}

std::vector<std::string>
RobotClient::GetDeviceList()
{
  google::protobuf::Empty request; // Use google::protobuf::Empty
  webots::DeviceListResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetDeviceList(&context, request, &response);

  if (status.ok()) {
    std::vector<std::string> devices;
    for (const auto& device : response.devices()) {
      devices.push_back(device.name());
    }
    return devices;
  } else {
    std::cerr << "GetDeviceList RPC failed: " << status.error_message() << std::endl;
    return {};
  }
}

bool
RobotClient::Step(int32_t time_step)
{
  webots::StepRequest request;
  request.set_time_step(time_step);
  webots::StepResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->Step(&context, request, &response);

  if (status.ok()) {
    return response.success();
  } else {
    std::cerr << "Step RPC failed: " << status.error_message() << std::endl;
    return false;
  }
}

double
RobotClient::GetBasicTimeStep()
{
  google::protobuf::Empty request; // Use google::protobuf::Empty
  webots::GetBasicTimeStepResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetBasicTimeStep(&context, request, &response);

  if (status.ok()) {
    return response.basic_time_step();
  } else {
    std::cerr << "GetBasicTimeStep RPC failed: " << status.error_message() << std::endl;
    return -1.0; // Return an invalid value to indicate failure
  }
}
