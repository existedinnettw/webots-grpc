#include "webots-grpc-client.hpp"

#include <grpcpp/create_channel.h>
#include <grpcpp/grpcpp.h>

#include <iostream>

int
main()
{
  // Create a RobotClient object
  try {
    RobotClient robotClient(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));
    //   MotorClient motorClient(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));
  } catch (const std::exception& e) {
    std::cerr << "Error creating RobotClient(as expected, server not started): " << e.what() << std::endl;
    return 0;
  }
  return 0;
}
