import os
import sys
import time

# import subprocess
from multiprocessing import Process

# grpcio-tools.protoc python import paths should be relative to a specified root directory #29459
sys.path.append(os.path.join(os.path.dirname(__file__), "../generated"))
from concurrent import futures

import grpc
from controller.robot import Robot
from grpc_reflection.v1alpha import reflection

# Import the generated gRPC modules
import generated.device_pb2 as device_pb2
import generated.device_pb2_grpc as device_pb2_grpc
import generated.distance_sensor_pb2 as distance_sensor_pb2
import generated.distance_sensor_pb2_grpc as distance_sensor_pb2_grpc
import generated.motor_pb2 as motor_pb2
import generated.motor_pb2_grpc as motor_pb2_grpc
import generated.position_sensor_pb2 as position_sensor_pb2
import generated.position_sensor_pb2_grpc as position_sensor_pb2_grpc
import generated.robot_pb2 as robot_pb2
import generated.robot_pb2_grpc as robot_pb2_grpc

# Import the service implementations
from webots_grpc.device_service import DeviceService
from webots_grpc.distance_sensor_service import DistanceSensorService
from webots_grpc.motor_service import MotorService
from webots_grpc.position_sensor_service import PositionSensorService
from webots_grpc.robot_service import RobotService


def serve():
    # Create a single Robot instance
    robot = Robot()

    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register all services with the shared Robot instance
    robot_pb2_grpc.add_RobotServiceServicer_to_server(RobotService(robot), server)
    motor_pb2_grpc.add_MotorServiceServicer_to_server(MotorService(robot), server)
    device_pb2_grpc.add_DeviceServiceServicer_to_server(DeviceService(robot), server)
    position_sensor_pb2_grpc.add_PositionSensorServiceServicer_to_server(
        PositionSensorService(robot), server
    )
    distance_sensor_pb2_grpc.add_DistanceSensorServiceServicer_to_server(
        DistanceSensorService(robot), server
    )

    # Enable reflection
    service_names = (
        robot_pb2.DESCRIPTOR.services_by_name["RobotService"].full_name,
        motor_pb2.DESCRIPTOR.services_by_name["MotorService"].full_name,
        device_pb2.DESCRIPTOR.services_by_name["DeviceService"].full_name,
        position_sensor_pb2.DESCRIPTOR.services_by_name["PositionSensorService"].full_name,
        distance_sensor_pb2.DESCRIPTOR.services_by_name["DistanceSensorService"].full_name,
        reflection.SERVICE_NAME,  # Reflection service
    )
    reflection.enable_server_reflection(service_names, server)

    # Bind the server to a port
    server.add_insecure_port("[::]:50051")

    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()


def watchdog():
    """Parent process that monitors and restarts the gRPC server subprocess."""
    while True:
        print("Starting gRPC server subprocess...")
        p = Process(target=serve)
        p.start()
        result = p.join()

        if result == 0:
            print("gRPC server subprocess exited normally.")
            break
        else:
            print(f"gRPC server subprocess crashed with return code {result}. Restarting...")
            time.sleep(2)  # Optional: Add a delay before restarting


if __name__ == "__main__":
    watchdog()
