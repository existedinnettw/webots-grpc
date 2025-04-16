# Ensure the generated files are in the PYTHONPATH
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../generated"))

import grpc
import generated.robot_pb2 as robot_pb2
import generated.robot_pb2_grpc as robot_pb2_grpc
import generated.motor_pb2 as motor_pb2
import generated.motor_pb2_grpc as motor_pb2_grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)

import random


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
                robot_pb2.Empty()
            )
            print("Robot Name:", robot_name_response.name)
        except grpc.RpcError as e:
            print(f"Error calling GetRobotName: {e.code()} - {e.details()}")

        # get device from robot
        try:
            get_device_list_response: robot_pb2.DeviceListResponse = (
                robot_stub.GetDeviceList(robot_pb2.Empty())
            )
            # print("Get Device List:", get_device_list_response)
            for device in get_device_list_response.devices:
                print(
                    f"Device Name: {device.name}, Model: {device.model}, Node Type: {device.node_type}"
                )
        except grpc.RpcError as e:
            print(f"Error calling GetDevice: {e.code()} - {e.details()}")

        # webots is designed to known the device name and type beforehand, reflection is not supported(expected)
        # base_link_to_link2, link2_to_link3_1, link3_1_to_link4_1
        motor_x: robot_pb2.DeviceResponse = robot_stub.GetDevice(
            robot_pb2.DeviceRequest(name="base_link_to_link2")
        )
        motor_y: robot_pb2.DeviceResponse = robot_stub.GetDevice(
            robot_pb2.DeviceRequest(name="link2_to_link3_1")
        )
        motor_z: robot_pb2.DeviceResponse = robot_stub.GetDevice(
            robot_pb2.DeviceRequest(name="link3_1_to_link4_1")
        )

        # show max/min position of motor_x, y, z
        # put in min/max in dictionary
        motor_x = {
            "name": motor_x.name,
            "min_position": 0,
            "max_position": 0,
        }
        motor_y = {
            "name": motor_y.name,
            "min_position": 0,
            "max_position": 0,
        }
        motor_z = {
            "name": motor_z.name,
            "min_position": 0,
            "max_position": 0,
        }
        for motor in [motor_x, motor_y, motor_z]:
            try:
                response: motor_pb2.GetMaxPositionResponse = motor_stub.GetMaxPosition(
                    motor_pb2.GetMaxPositionRequest(motor_name=motor["name"])
                )
                motor["max_position"] = response.max_position
                response: motor_pb2.GetMinPositionResponse = motor_stub.GetMinPosition(
                    motor_pb2.GetMinPositionRequest(motor_name=motor["name"])
                )
                motor["min_position"] = response.min_position
                print(
                    f"Motor: {motor['name']}, Min Position: {motor['min_position']}, Max Position: {motor['max_position']}"
                )
            except grpc.RpcError as e:
                print(f"Error calling GetMaxPosition: {e.code()} - {e.details()}")

        # move x, y, z axes randomly within the min/max range
        for i in range(100):
            # Set position for each motor

            for motor in [motor_x, motor_y, motor_z]:
                position = motor["min_position"] + (
                    motor["max_position"] - motor["min_position"]
                ) * random.uniform(0, 1)
                try:
                    response: motor_pb2.SetPositionResponse = motor_stub.SetPosition(
                        motor_pb2.SetPositionRequest(
                            motor_name=motor["name"], position=position
                        )
                    )
                    # print("Set Position:", response.success)
                except grpc.RpcError as e:
                    print(f"Error calling SetPosition: {e.code()} - {e.details()}")
                    sys.exit(1)

            # step
            try:
                response_step: robot_pb2.StepResponse = robot_stub.Step(
                    robot_pb2.StepRequest(time_step=32)
                )
                # print("Step:", response_step.success)
            except grpc.RpcError as e:
                print(f"Error calling Step: {e.code()} - {e.details()}")
                sys.exit(1)


if __name__ == "__main__":
    run()
