import generated.distance_sensor_pb2 as distance_sensor_pb2
import generated.distance_sensor_pb2_grpc as distance_sensor_pb2_grpc
import generated.sensor_pb2 as sensor_pb2
import grpc
from controller.distance_sensor import DistanceSensor
from controller.robot import Robot
from google.protobuf.empty_pb2 import Empty  # Import Empty for empty responses


class DistanceSensorService(distance_sensor_pb2_grpc.DistanceSensorServiceServicer):
    """
    gRPC service for controlling distance sensors in Webots.
    This service provides methods to enable, disable, and retrieve data from distance sensors.
    """

    def __init__(self, robot: Robot):
        self.robot = robot

    def _get_distance_sensor(self, sensor_name, context) -> DistanceSensor:
        sensor = self.robot.getDevice(sensor_name)
        if not isinstance(sensor, DistanceSensor):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"DistanceSensor '{sensor_name}' not found.")
            return None
        return sensor

    def Enable(self, request, context):
        sensor = self._get_distance_sensor(request.name, context)
        if sensor is None:
            return Empty()
        sensor.enable(request.sampling_period)
        return Empty()

    def Disable(self, request, context):
        sensor = self._get_distance_sensor(request.name, context)
        if sensor is None:
            return Empty()
        sensor.disable()
        return Empty()

    def GetSamplingPeriod(self, request, context):
        sensor = self._get_distance_sensor(request.name, context)
        if sensor is None:
            return sensor_pb2.GetSamplingPeriodResponse(sampling_period=0)
        return sensor_pb2.GetSamplingPeriodResponse(
            sampling_period=sensor.getSamplingPeriod()
        )

    def GetValue(self, request, context):
        sensor = self._get_distance_sensor(request.name, context)
        if sensor is None:
            return sensor_pb2.GetValueResponse(value=0.0)
        return sensor_pb2.GetValueResponse(value=sensor.getValue())
