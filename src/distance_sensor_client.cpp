
#include "distance_sensor_client.hpp"

DistanceSensorClient::DistanceSensorClient(const std::shared_ptr<grpc::Channel>& channel)
  : stub_(webots::DistanceSensorService::NewStub(channel))
{
}
DistanceSensorClient::~DistanceSensorClient()
{
  // Destructor implementation (if needed)
}

bool
DistanceSensorClient::Enable(const std::string& sensor_name, int sampling_period)
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
DistanceSensorClient::Disable(const std::string& sensor_name)
{
  webots::DistanceSensorRequest request;
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
DistanceSensorClient::GetSamplingPeriod(const std::string& sensor_name)
{
  webots::DistanceSensorRequest request;
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
DistanceSensorClient::GetValue(const std::string& sensor_name)
{
  webots::DistanceSensorRequest request;
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