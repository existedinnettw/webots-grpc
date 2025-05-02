#include "position_sensor_client.hpp"
#include <iostream>

PositionSensorClient::PositionSensorClient(const std::shared_ptr<grpc::Channel>& channel)
  : stub_(webots::PositionSensorService::NewStub(channel))
{
}

PositionSensorClient::~PositionSensorClient()
{
  // Destructor implementation (if needed)
}

bool
PositionSensorClient::Enable(const std::string& sensor_name, int sampling_period)
{
  webots::EnableRequest request;
  request.set_name(sensor_name);
  request.set_sampling_period(sampling_period);

  google::protobuf::Empty response;
  grpc::ClientContext context;

  grpc::Status status = stub_->Enable(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in Enable: " << status.error_message() << std::endl;
    return false;
  }
  return true;
}

bool
PositionSensorClient::Disable(const std::string& sensor_name)
{
  webots::PositionSensorRequest request;
  request.set_name(sensor_name);

  google::protobuf::Empty response;
  grpc::ClientContext context;

  grpc::Status status = stub_->Disable(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in Disable: " << status.error_message() << std::endl;
    return false;
  }
  return true;
}

int
PositionSensorClient::GetSamplingPeriod(const std::string& sensor_name)
{
  webots::PositionSensorRequest request;
  request.set_name(sensor_name);

  webots::GetSamplingPeriodResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetSamplingPeriod(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetSamplingPeriod: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get sampling period");
  }
  return response.sampling_period();
}

double
PositionSensorClient::GetValue(const std::string& sensor_name)
{
  webots::PositionSensorRequest request;
  request.set_name(sensor_name);

  webots::GetValueResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetValue(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetValue: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get value");
  }
  return response.value();
}

webots::GetTypeResponse::Type
PositionSensorClient::GetType(const std::string& sensor_name)
{
  webots::PositionSensorRequest request;
  request.set_name(sensor_name);

  webots::GetTypeResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetType(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetType: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get type");
  }
  return response.type();
}

int
PositionSensorClient::GetBrakeTag(const std::string& sensor_name)
{
  webots::PositionSensorRequest request;
  request.set_name(sensor_name);

  webots::GetBrakeTagResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetBrakeTag(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetBrakeTag: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get brake tag");
  }
  return response.brake_tag();
}

int
PositionSensorClient::GetMotorTag(const std::string& sensor_name)
{
  webots::PositionSensorRequest request;
  request.set_name(sensor_name);

  webots::GetMotorTagResponse response;
  grpc::ClientContext context;

  grpc::Status status = stub_->GetMotorTag(&context, request, &response);
  if (!status.ok()) {
    std::cerr << "Error in GetMotorTag: " << status.error_message() << std::endl;
    throw std::runtime_error("Failed to get motor tag");
  }
  return response.motor_tag();
}
