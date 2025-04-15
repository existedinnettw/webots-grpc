import grpc
from concurrent import futures
from controller.device import Device
from controller.robot import Robot
import generated.device_pb2 as device_pb2
import generated.device_pb2_grpc as device_pb2_grpc


class DeviceService(device_pb2_grpc.DeviceServiceServicer):
    def __init__(self, robot):
        self.robot = robot

    def GetDeviceInfo(self, request, context):
        device = self.robot.getDevice(request.device_name)
        if device is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Device '{request.device_name}' not found.")
            return device_pb2.DeviceResponse()
        return device_pb2.DeviceResponse(
            device_info=device_pb2.DeviceInfo(
                name=device.getName(),
                model=device.getModel(),
                node_type=device.getNodeType(),
            )
        )

