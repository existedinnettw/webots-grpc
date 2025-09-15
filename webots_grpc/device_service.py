import generated.device_pb2 as device_pb2
import generated.device_pb2_grpc as device_pb2_grpc
import grpc
from controller.robot import Robot


class DeviceService(device_pb2_grpc.DeviceServiceServicer):
    def __init__(self, robot: Robot):
        self.robot = robot

    def GetDeviceInfo(self, request, context):
        device = self.robot.getDevice(request.name)
        if device is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Device '{request.name}' not found.")
            return device_pb2.DeviceResponse()
        return device_pb2.DeviceResponse(
            name=device.getName(),
            model=device.getModel(),
            node_type=device.getNodeType(),
        )

    def GetDeviceModel(self, request, context):
        device = self.robot.getDevice(request.name)
        if device is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Device '{request.name}' not found.")
            return device_pb2.DeviceModelResponse(model="")
        return device_pb2.DeviceModelResponse(model=device.getModel())

    def GetNodeType(self, request, context):
        device = self.robot.getDevice(request.name)
        if device is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Device '{request.name}' not found.")
            return device_pb2.NodeTypeResponse(node_type=0)
        return device_pb2.NodeTypeResponse(node_type=device.getNodeType())

    def GetTag(self, request, context):
        device = self.robot.getDevice(request.name)
        if device is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Device '{request.name}' not found.")
            return device_pb2.DeviceTagResponse(tag=0)
        return device_pb2.DeviceTagResponse(tag=device.getTag())
