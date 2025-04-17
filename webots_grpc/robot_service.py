import grpc
from controller.robot import Robot

import generated.robot_pb2 as robot_pb2
import generated.robot_pb2_grpc as robot_pb2_grpc


class RobotService(robot_pb2_grpc.RobotServiceServicer):
    def __init__(self, robot: Robot):
        self.robot = robot

    def GetRobotName(self, request, context):
        return robot_pb2.RobotNameResponse(name=self.robot.getName())

    def GetRobotModel(self, request, context):
        return robot_pb2.RobotModelResponse(model=self.robot.getModel())

    def GetCustomData(self, request, context):
        return robot_pb2.CustomDataResponse(data=self.robot.getCustomData())

    def SetCustomData(self, request, context):
        self.robot.setCustomData(request.data)
        return robot_pb2.Empty()

    def GetDeviceList(self, request, context):
        devices = [
            robot_pb2.DeviceResponse(
                name=device.getName(),
                model=device.getModel(),
                node_type=device.getNodeType(),
            )
            for device in self.robot.devices.values()
        ]
        return robot_pb2.DeviceListResponse(devices=devices)

    def GetDevice(self, request, context):
        device = self.robot.getDevice(request.name)
        if device is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Device '{request.name}' not found.")
            return robot_pb2.DeviceResponse()
        return robot_pb2.DeviceResponse(
            name=device.getName(),
            model=device.getModel(),
            node_type=device.getNodeType(),
        )

    def Step(self, request, context):
        """

        ref
        ---
        A controller cannot prevent its own termination.
        When one of the above events happens, the wb_robot_step function returns -1.
        From this point, Webots will not communicate with the controller any more.
        Therefore, new print statements executed by the controller on stdout or stderr
        will no longer appear in the Webots console.
        After one second (real time), if the controller has not terminated by itself,
        Webots will kill it (SIGKILL). That leaves a limited amount of time to the
        controller to save important data, close files, etc. before it is actually killed
          by Webots. Here is an example that shows how to save data before the upcoming termination:
        """
        success = self.robot.step(request.time_step) != -1
        return robot_pb2.StepResponse(success=success)
