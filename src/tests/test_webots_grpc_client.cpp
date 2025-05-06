#include "position_sensor_client.hpp" // Include PositionSensorClient
#include "webots-grpc-client.hpp"     // Includes RobotClient, MotorClient, and DeviceClient
#include <iostream>
#include <map>
#include <random>
#include <string>
#include <vector>

int
main(int argc, char* argv[])
{
  // Check if the user provided a URL as an argument
  std::string serverAddress = "localhost:50051"; // Default address
  if (argc > 1) {
    serverAddress = argv[1];
  }

  // Initialize RobotClient, MotorClient, and PositionSensorClient
  RobotClient robotClient(grpc::CreateChannel(serverAddress, grpc::InsecureChannelCredentials()));
  MotorClient motorClient(grpc::CreateChannel(serverAddress, grpc::InsecureChannelCredentials()));
  PositionSensorClient positionSensorClient(grpc::CreateChannel(serverAddress, grpc::InsecureChannelCredentials()));

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

  // Get basic time step
  try {
    double basicTimeStep = robotClient.GetBasicTimeStep();
    if (basicTimeStep > 0) {
      std::cout << "Basic Time Step: " << basicTimeStep << std::endl;
    } else {
      std::cerr << "Failed to get Basic Time Step." << std::endl;
    }
  } catch (const std::exception& e) {
    std::cerr << "Error calling GetBasicTimeStep: " << e.what() << std::endl;
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
  std::map<std::string, std::string> positionSensorNames;

  // Fetch motor details and limits
  for (const auto& motorName : motorNames) {
    try {
      double minPosition = motorClient.GetMinPosition(motorName);
      double maxPosition = motorClient.GetMaxPosition(motorName);
      motorLimits[motorName] = { minPosition, maxPosition };
      std::cout << "Motor: " << motorName << ", Min Position: " << minPosition << ", Max Position: " << maxPosition
                << std::endl;

      // Get position sensor name for the motor
      std::string positionSensorName = motorClient.GetPositionSensor(motorName);
      positionSensorNames[motorName] = positionSensorName;
      std::cout << "Motor: " << motorName << ", Position Sensor: " << positionSensorName << std::endl;

      // Enable the position sensor
      if (!positionSensorClient.Enable(positionSensorName, 32)) {
        std::cerr << "Failed to enable position sensor: " << positionSensorName << std::endl;
      }
    } catch (const std::exception& e) {
      std::cerr << "Error fetching motor details or enabling position sensor for " << motorName << ": " << e.what()
                << std::endl;
    }
  }

  // Move motors randomly within their min/max range and read position sensor values
  std::random_device rd;
  std::mt19937 gen(rd());
  for (int i = 0; i < 100; ++i) {
    for (const auto& [motorName, limits] : motorLimits) {
      std::uniform_real_distribution<> dis(limits.first, limits.second);
      double position = dis(gen);
      try {
        if (motorClient.SetPosition(motorName, position)) {
          std::cout << "Set motor " << motorName << " to position " << position << std::endl;
        } else {
          std::cerr << "Failed to set position for motor: " << motorName << std::endl;
        }
      } catch (const std::exception& e) {
        std::cerr << "Error setting position for motor " << motorName << ": " << e.what() << std::endl;
      }

      // Read position sensor value
      try {
        double sensorValue = positionSensorClient.GetValue(positionSensorNames[motorName]);
        std::cout << "Motor: " << motorName << ", Position Sensor Value: " << sensorValue << std::endl;
      } catch (const std::exception& e) {
        std::cerr << "Error reading position sensor for motor " << motorName << ": " << e.what() << std::endl;
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