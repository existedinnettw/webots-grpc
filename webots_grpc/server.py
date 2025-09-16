import argparse
import functools
import signal
import time
from concurrent import futures

# import subprocess
from multiprocessing import Process

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
import grpc
from controller.robot import Robot

# from google.protobuf.message import Message
from grpc_reflection.v1alpha import reflection

# Import the service implementations
from webots_grpc.device_service import DeviceService
from webots_grpc.distance_sensor_service import DistanceSensorService
from webots_grpc.motor_service import MotorService
from webots_grpc.position_sensor_service import PositionSensorService
from webots_grpc.robot_service import RobotService


class LoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        method = handler_call_details.method
        print(f"[gRPC] Incoming call to method: {method}")

        # TODO: no good way to get args yet.
        # print(f"[gRPC]   args: {request}")

        handler = continuation(handler_call_details)
        # Check if the call is unary-unary, unary-stream, etc.
        if handler is None:
            return None
        return handler


def serve(port=50051, enable_log=False):
    interceptors = []
    if enable_log:
        interceptors.append(LoggingInterceptor())
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)

    robot = Robot()
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
    server.add_insecure_port(f"[::]:{port}")

    print(f"gRPC server is running on port {port}...")
    server.start()

    def signal_handler(signum, frame):
        print(f"Received signal {signum}, shutting down server gracefully...")
        server.stop(grace=5)  # 5 seconds grace period

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    server.wait_for_termination()


def watchdog(func):
    """Parent process that monitors and restarts the gRPC server subprocess."""
    stop_flag = False

    def signal_handler(signum, frame):
        nonlocal stop_flag
        print(f"Received signal '{signal.strsignal(signum)}'...")
        stop_flag = True
        if "p" in locals() and p.is_alive():
            p.terminate()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while not stop_flag:
        print("Starting gRPC server subprocess...")
        p = Process(target=func)
        p.start()
        result = p.join()

        if stop_flag:
            print("Watchdog shutting down.")
            break

        if result == 0:
            print("gRPC server subprocess exited normally.")
            break
        else:
            print(f"gRPC server subprocess crashed with return code {result}. Restarting...")
            time.sleep(0.5)  # Optional: Add a delay before restarting


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Webots gRPC Server")
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=50051,
        help="Port for the gRPC server to listen on (default: 50051)",
    )
    parser.add_argument(
        "-d",
        "--enable-log",
        action="store_true",
        help="Enable logging of incoming gRPC requests",
    )
    args = parser.parse_args()

    configured_serve = functools.partial(serve, port=args.port, enable_log=args.enable_log)

    watchdog(configured_serve)
