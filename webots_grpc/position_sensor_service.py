import generated.position_sensor_pb2 as position_sensor_pb2
import generated.position_sensor_pb2_grpc as position_sensor_pb2_grpc
import generated.sensor_pb2 as sensor_pb2
import grpc
from controller.position_sensor import PositionSensor
from controller.robot import Robot
from google.protobuf.empty_pb2 import Empty  # Import Empty for empty responses


class PositionSensorService(position_sensor_pb2_grpc.PositionSensorServiceServicer):
    """
    gRPC service for controlling position sensors in Webots.
    This service provides methods to enable, disable, and retrieve data from position sensors.
    """

    def __init__(self, robot: Robot):
        self.robot = robot

    def _get_position_sensor(self, sensor_name, context) -> PositionSensor:
        sensor = self.robot.getDevice(sensor_name)
        if not isinstance(sensor, PositionSensor):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"PositionSensor '{sensor_name}' not found.")
            return None
        return sensor

    def Enable(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return Empty()
        sensor.enable(request.sampling_period)
        return Empty()

    def Disable(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return Empty()
        sensor.disable()
        return Empty()

    def GetSamplingPeriod(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return sensor_pb2.GetSamplingPeriodResponse(sampling_period=0)
        return sensor_pb2.GetSamplingPeriodResponse(
            sampling_period=sensor.getSamplingPeriod()
        )

    def GetValue(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return sensor_pb2.GetValueResponse(value=0.0)
        return sensor_pb2.GetValueResponse(value=sensor.getValue())

    def GetType(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return position_sensor_pb2.GetTypeResponse(
                type=position_sensor_pb2.GetTypeResponse.Type.ROTATIONAL
            )
        sensor_type = sensor.getType()
        if sensor_type == PositionSensor.ROTATIONAL:
            return position_sensor_pb2.GetTypeResponse(
                type=position_sensor_pb2.GetTypeResponse.Type.ROTATIONAL
            )
        elif sensor_type == PositionSensor.LINEAR:
            return position_sensor_pb2.GetTypeResponse(
                type=position_sensor_pb2.GetTypeResponse.Type.LINEAR
            )
        return position_sensor_pb2.GetTypeResponse(
            type=position_sensor_pb2.GetTypeResponse.Type.ROTATIONAL
        )

    def GetBrakeTag(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return position_sensor_pb2.GetBrakeTagResponse(brake_tag=-1)
        return position_sensor_pb2.GetBrakeTagResponse(brake_tag=sensor.getBrakeTag())

    def GetMotorTag(self, request, context):
        sensor = self._get_position_sensor(request.name, context)
        if sensor is None:
            return position_sensor_pb2.GetMotorTagResponse(motor_tag=-1)
        return position_sensor_pb2.GetMotorTagResponse(motor_tag=sensor.getMotorTag())
