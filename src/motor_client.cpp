#include "motor_client.hpp"
#include <iostream>

MotorClient::MotorClient(const std::shared_ptr<grpc::Channel>& channel)
  : stub_(webots::MotorService::NewStub(channel))
{
}

MotorClient::~MotorClient()
{
  // Destructor implementation (if needed)
}

bool
MotorClient::SetPosition(const std::string& motor_name, double position)
{
  webots::SetPositionRequest request;
  request.set_name(motor_name);
  request.set_position(position);

  google::protobuf::Empty response; // Use google::protobuf::Empty
  grpc::ClientContext context;

  grpc::Status status = stub_->SetPosition(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in SetPosition: " << status.error_message() << std::endl;
    return false;
  }
  return true; // No success field in google::protobuf::Empty
}

double
MotorClient::GetMinPosition(const std::string& motor_name)
{
  webots::MotorRequest request; // Use MotorRequest
  request.set_name(motor_name);

  webots::GetMinPositionResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetMinPosition(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetMinPosition: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get minimum position");
  }
  return response.min_position();
}

double
MotorClient::GetMaxPosition(const std::string& motor_name)
{
  webots::MotorRequest request; // Use MotorRequest
  request.set_name(motor_name);

  webots::GetMaxPositionResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetMaxPosition(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetMaxPosition: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get maximum position");
  }
  return response.max_position();
}