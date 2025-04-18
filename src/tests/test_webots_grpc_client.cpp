#include "webots-grpc-client.hpp" // Replace with the actual header file for your client
#include <gtest/gtest.h>


#include "webots-grpc-client.hpp"
#include <iostream>

int
main()
{
  RobotClient client;

  std::string robotName = client.GetRobotName();
  if (!robotName.empty()) {
    std::cout << "Robot Name: " << robotName << std::endl;
  }

  std::string robotModel = client.GetRobotModel();
  if (!robotModel.empty()) {
    std::cout << "Robot Model: " << robotModel << std::endl;
  }

  return 0;
}