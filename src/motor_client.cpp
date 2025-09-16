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

bool
MotorClient::SetVelocity(const std::string& motor_name, double velocity)
{
  webots::SetVelocityRequest request;
  request.set_name(motor_name);
  request.set_velocity(velocity);

  google::protobuf::Empty response; // Use google::protobuf::Empty
  grpc::ClientContext context;

  grpc::Status status = stub_->SetVelocity(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in SetVelocity: " << status.error_message() << std::endl;
    return false;
  }
  return true; // No success field in google::protobuf::Empty
}

double
MotorClient::GetVelocity(const std::string& motor_name)
{
  webots::MotorRequest request; // Use MotorRequest
  request.set_name(motor_name);

  webots::GetVelocityResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetVelocity(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetVelocity: " << status.error_message() << std::endl;
    return false;
  }
  return response.velocity();
}

double
MotorClient::GetMaxVelocity(const std::string& motor_name)
{
  webots::MotorRequest request; // Use MotorRequest
  request.set_name(motor_name);

  webots::GetVelocityResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetMaxVelocity(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetMaxVelocity: " << status.error_message() << std::endl;
    return false;
  }
  return response.velocity();
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

std::string
MotorClient::GetPositionSensor(const std::string& motor_name)
{
  webots::MotorRequest request; // Use MotorRequest
  request.set_name(motor_name);

  webots::GetPositionSensorResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetPositionSensor(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetPositionSensor: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get position sensor");
  }
  return response.position_sensor_name();
}