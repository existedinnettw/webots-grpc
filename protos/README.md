# Webots gRPC API

This project provides a gRPC interface for interacting with the Webots Robot Simulation environment. It includes definitions for the Robot, Motor, and Device APIs, allowing users to control and retrieve information from simulated robots and their components.

## Project Structure

```
webots-grpc
├── protos
│   ├── robot.proto      # gRPC service and messages for the Robot API
│   ├── motor.proto      # gRPC service and messages for the Motor API
│   └── device.proto     # gRPC service and messages for the Device API
└── README.md            # Project documentation
```

## Setup Instructions

1. **Install Dependencies**: Ensure you have the necessary dependencies installed, including gRPC and Protocol Buffers.

2. **Generate gRPC Code**: Use the Protocol Buffers compiler (`protoc`) to generate the gRPC code from the `.proto` files. For example:
   ```
   protoc -I=protos --python_out=. --grpc_python_out=. protos/*.proto
   ```

3. **Run the Server**: Implement the server logic to handle the gRPC requests defined in the `.proto` files.

4. **Client Usage**: Create a client to interact with the gRPC server using the generated code.

## Usage Examples

### Robot API

- **Get Robot Name**: Call the `GetRobotName` method to retrieve the name of the robot.
- **Get Device List**: Use `GetDeviceList` to get a list of all devices attached to the robot.

### Motor API

- **Set Motor Position**: Use `SetMotorPosition` to set the desired position of a motor.
- **Get Motor Velocity**: Call `GetMotorVelocity` to retrieve the current velocity of a motor.

### Device API

- **Get Device Information**: Use `GetDeviceInfo` to retrieve details about a specific device.
- **Enable Device**: Call `EnableDevice` to enable a device for interaction.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the Apache License, Version 2.0. See the LICENSE file for more details.