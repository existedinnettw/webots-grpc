# Ensure the generated files are in the PYTHONPATH
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../generated"))

import random

import grpc
from google.protobuf import empty_pb2
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)

import generated.device_pb2 as device_pb2
import generated.device_pb2_grpc as device_pb2_grpc
import generated.motor_pb2 as motor_pb2
import generated.motor_pb2_grpc as motor_pb2_grpc
import generated.robot_pb2 as robot_pb2
import generated.robot_pb2_grpc as robot_pb2_grpc


def run():
    # Connect to the gRPC server
    with grpc.insecure_channel("localhost:50051") as channel:
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"found services: {services}")

        # RobotService client
        robot_stub = robot_pb2_grpc.RobotServiceStub(channel)
        motor_stub = motor_pb2_grpc.MotorServiceStub(channel)

        try:
            robot_name_response: robot_pb2.RobotNameResponse = robot_stub.GetRobotName(
                empty_pb2.Empty()
            )
            print("Robot Name:", robot_name_response.name)
        except grpc.RpcError as e:
            print(f"Error calling GetRobotName: {e.code()} - {e.details()}")

        # Get device list from robot
        try:
            get_device_list_response: robot_pb2.DeviceListResponse = robot_stub.GetDeviceList(
                empty_pb2.Empty()
            )
            for device in get_device_list_response.devices:
                print(
                    f"Device Name: {device.name}, Model: {device.model}, Node Type: {device.node_type}"
                )
        except grpc.RpcError as e:
            print(f"Error calling GetDeviceList: {e.code()} - {e.details()}")

        # Webots is designed to know the device name and type beforehand, reflection is not supported (expected)
        motor_names = ["base_link_to_link2", "link2_to_link3_1", "link3_1_to_link4_1"]
        motors = {}

        for motor_name in motor_names:
            try:
                device_response: device_pb2.DeviceResponse = robot_stub.GetDevice(
                    device_pb2.DeviceRequest(name=motor_name)
                )
            except grpc.RpcError as e:
                print(f"Error calling GetDevice for {motor_name}: {e.code()} - {e.details()}")

            try:
                motor_request: motor_pb2.MotorRequest = motor_pb2.MotorRequest(
                    name=device_response.name
                )
                motor_response: motor_pb2.MotorResponse = motor_stub.GetMotor(motor_request)
                print(
                    f"Motor Name: {motor_response.device.name}, Model: {motor_response.device.model}, Node Type: {motor_response.device.node_type}, Type: {motor_response.type}"
                )
                motors[motor_name] = {
                    "motor_request": motor_request,
                    "min_position": 0,
                    "max_position": 0,
                }
            except grpc.RpcError as e:
                print(f"Error calling GetMotor for {motor_name}: {e.code()} - {e.details()}")

        # Fetch min/max positions for each motor
        for motor_name, motor in motors.items():
            try:
                response: motor_pb2.GetMaxPositionResponse = motor_stub.GetMaxPosition(
                    motor["motor_request"]
                )
                motor["max_position"] = response.max_position
                response: motor_pb2.GetMinPositionResponse = motor_stub.GetMinPosition(
                    motor["motor_request"]
                )
                motor["min_position"] = response.min_position
                # print(
                #     f"Motor: {motor['name']}, Min Position: {motor['min_position']}, Max Position: {motor['max_position']}"
                # )
                print(
                    "Motor:{}, Min Position: {}, Max Position: {}".format(
                        motor_name, motor["min_position"], motor["max_position"]
                    )
                )
            except grpc.RpcError as e:
                print(
                    f"Error calling GetMin/MaxPosition for {motor_name}: {e.code()} - {e.details()}"
                )

        # Move motors randomly within their min/max range
        for i in range(100):
            for motor_name, motor in motors.items():
                position = motor["min_position"] + (
                    motor["max_position"] - motor["min_position"]
                ) * random.uniform(0, 1)
                # print(position)
                try:
                    response: motor_pb2.SetPositionResponse = motor_stub.SetPosition(
                        motor_pb2.SetPositionRequest(
                            name=motor["motor_request"].name,
                            position=position,
                        )
                    )
                except grpc.RpcError as e:
                    print(f"Error calling SetPosition for {motor_name}: {e.code()} - {e.details()}")
                    sys.exit(1)

            # Step simulation
            try:
                response_step: robot_pb2.StepResponse = robot_stub.Step(
                    robot_pb2.StepRequest(time_step=32)
                )
                if not response_step.success:
                    print("Step failed")
            except grpc.RpcError as e:
                print(f"Error calling Step: {e.code()} - {e.details()}")
                sys.exit(1)


if __name__ == "__main__":
    run()
