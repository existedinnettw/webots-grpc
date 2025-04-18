import grpc
from concurrent import futures
from controller.motor import Motor
from controller.robot import Robot
import generated.motor_pb2 as motor_pb2
import generated.motor_pb2_grpc as motor_pb2_grpc


class MotorService(motor_pb2_grpc.MotorServiceServicer):
    """
    gRPC service for controlling motors in Webots.
    It is designed as a wrapper around Webots `controller.motor.Motor`.
    This service provides methods to set and get motor positions, velocities, and torques.
    """

    def __init__(self, robot: Robot):
        self.robot = robot

    def _get_motor(self, motor_name, context):
        motor = self.robot.getDevice(motor_name)
        if not isinstance(motor, Motor):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{motor_name}' not found.")
            return None
        return motor

    def SetPosition(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.SetPositionResponse(success=False)
        motor.setPosition(request.position)
        return motor_pb2.SetPositionResponse(success=True)

    def GetPosition(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetPositionResponse(position=0.0)
        return motor_pb2.GetPositionResponse(position=motor.getTargetPosition())

    def SetVelocity(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.SetVelocityResponse(success=False)
        motor.setVelocity(request.velocity)
        return motor_pb2.SetVelocityResponse(success=True)

    def GetVelocity(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetVelocityResponse(velocity=0.0)
        return motor_pb2.GetVelocityResponse(velocity=motor.getVelocity())

    def SetTorque(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.SetTorqueResponse(success=False)
        motor.setTorque(request.torque)
        return motor_pb2.SetTorqueResponse(success=True)

    def GetTorque(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetTorqueResponse(torque=0.0)
        return motor_pb2.GetTorqueResponse(torque=motor.getTorqueFeedback())

    def GetMinPosition(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetMinPositionResponse(min_position=0.0)
        return motor_pb2.GetMinPositionResponse(min_position=motor.getMinPosition())

    def GetMaxPosition(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetMaxPositionResponse(max_position=0.0)
        return motor_pb2.GetMaxPositionResponse(max_position=motor.getMaxPosition())

    def SetControlPID(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.SetControlPIDResponse(success=False)
        motor.setControlPID(request.p, request.i, request.d)
        return motor_pb2.SetControlPIDResponse(success=True)

    def GetTargetPosition(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetTargetPositionResponse(target_position=0.0)
        return motor_pb2.GetTargetPositionResponse(
            target_position=motor.getTargetPosition()
        )

    def GetPositionSensor(self, request, context):
        motor = self._get_motor(request.motor_name, context)
        if motor is None:
            return motor_pb2.GetPositionSensorResponse(position_sensor_name="")
        position_sensor = motor.getPositionSensor()
        if position_sensor is None:
            return motor_pb2.GetPositionSensorResponse(position_sensor_name="")
        return motor_pb2.GetPositionSensorResponse(
            position_sensor_name=position_sensor.getName()
        )
