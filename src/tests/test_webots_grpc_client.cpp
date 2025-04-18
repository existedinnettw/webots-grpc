#include "webots-grpc-client.hpp" // Includes RobotClient, MotorClient, and DeviceClient
#include <iostream>
#include <map>
#include <random>
#include <string>
#include <vector>

int
main()
{
  // Initialize RobotClient and MotorClient
  RobotClient robotClient(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));
  MotorClient motorClient(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));

  // Get Robot Name
  try {
    std::string robotName = robotClient.GetRobotName();
    if (!robotName.empty()) {
      std::cout << "Robot Name: " << robotName << std::endl;
    } else {
      std::cerr << "Failed to get Robot Name." << std::endl;
    }
  } catch (const std::exception& e) {
    std::cerr << "Error calling GetRobotName: " << e.what() << std::endl;
  }

  // Get Device List
  std::vector<std::string> deviceList;
  try {
    deviceList = robotClient.GetDeviceList();
    if (!deviceList.empty()) {
      std::cout << "Devices:" << std::endl;
      for (const auto& device : deviceList) {
        std::cout << "  " << device << std::endl;
      }
    } else {
      std::cerr << "Device list is empty." << std::endl;
    }
  } catch (const std::exception& e) {
    std::cerr << "Error calling GetDeviceList: " << e.what() << std::endl;
  }

  // Define motor names
  std::vector<std::string> motorNames = { "base_link_to_link2", "link2_to_link3_1", "link3_1_to_link4_1" };
  std::map<std::string, std::pair<double, double>> motorLimits;

  // Fetch motor details and limits
  for (const auto& motorName : motorNames) {
    try {
      double minPosition = motorClient.GetMinPosition(motorName);
      double maxPosition = motorClient.GetMaxPosition(motorName);
      motorLimits[motorName] = { minPosition, maxPosition };
      std::cout << "Motor: " << motorName << ", Min Position: " << minPosition << ", Max Position: " << maxPosition
                << std::endl;
    } catch (const std::exception& e) {
      std::cerr << "Error fetching motor details for " << motorName << ": " << e.what() << std::endl;
    }
  }

  // Move motors randomly within their min/max range
  std::random_device rd;
  std::mt19937 gen(rd());
  for (int i = 0; i < 100; ++i) {
    for (const auto& [motorName, limits] : motorLimits) {
      std::uniform_real_distribution<> dis(limits.first, limits.second);
      double position = dis(gen);
      try {
        if (motorClient.SetPosition(motorName, position)) {
          // std::cout << "Set motor " << motorName << " to position " << position << std::endl;
        } else {
          std::cerr << "Failed to set position for motor: " << motorName << std::endl;
        }
      } catch (const std::exception& e) {
        std::cerr << "Error setting position for motor " << motorName << ": " << e.what() << std::endl;
      }
    }

    // Step simulation
    try {
      if (!robotClient.Step(32)) {
        std::cerr << "Step failed." << std::endl;
        return 1;
      }
    } catch (const std::exception& e) {
      std::cerr << "Error during Step: " << e.what() << std::endl;
      return 1;
    }
  }

  return 0;
}