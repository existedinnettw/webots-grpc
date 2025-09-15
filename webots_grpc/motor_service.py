import generated.device_pb2 as device_pb2
import generated.motor_pb2 as motor_pb2
import generated.motor_pb2_grpc as motor_pb2_grpc
import grpc
from controller.motor import Motor
from controller.robot import Robot
from google.protobuf.empty_pb2 import Empty  # Import Empty for empty responses


class MotorService(motor_pb2_grpc.MotorServiceServicer):
    """
    gRPC service for controlling motors in Webots.
    It is designed as a wrapper around Webots `controller.motor.Motor`.
    This service provides methods to set and get motor positions, velocities, and torques.
    """

    def __init__(self, robot: Robot):
        self.robot = robot

    from typing import Optional

    def _get_motor(self, motor_name, context) -> Motor | None:
        motor = self.robot.getDevice(motor_name)
        if not isinstance(motor, Motor):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{motor_name}' not found.")
            return None
        # print(f"Retrieved motor: {motor_name}, Type: {type(motor)}")
        return motor

    def GetMotor(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.MotorResponse(
                device=device_pb2.DeviceResponse(name=request.name, model="", node_type=0),
                type=None,
            )
        wb_mot_type = motor.getType()
        if wb_mot_type == Motor.ROTATIONAL:
            motor_type = motor_pb2.MotorResponse.Type.ROTATIONAL
        elif wb_mot_type == Motor.LINEAR:
            motor_type = motor_pb2.MotorResponse.Type.LINEAR
        else:
            motor_type = None
        return motor_pb2.MotorResponse(
            device=device_pb2.DeviceResponse(
                name=request.name, model=motor.getModel(), node_type=motor.getNodeType()
            ),
            type=motor_type,
        )

    def SetPosition(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{request.name}' not found.")
            return Empty()

        # hotfix webots minpoisition not work (maxposition works correctly)
        new_position = max(request.position, motor.getMinPosition())
        motor.setPosition(new_position)

        # motor.setPosition(request.position)
        return Empty()

    def SetVelocity(self, request, context):
        """ """
        motor = self._get_motor(request.name, context)
        if motor is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{request.name}' not found.")
            return Empty()
        # https://cyberbotics.com/doc/reference/motor?tab-language=python#velocity-control
        # motor.setPosition(float("inf"))  # Set position to infinity for velocity control
        # https://cyberbotics.com/doc/reference/motor#field-summary
        # The value should always be positive (the default is 10).
        assert request.velocity >= 0, "Velocity must be non-negative."
        motor.setVelocity(request.velocity)
        return Empty()

    def GetVelocity(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetVelocityResponse(velocity=0.0)
        return motor_pb2.GetVelocityResponse(velocity=motor.getVelocity())

    def GetMaxVelocity(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetVelocityResponse(velocity=0.0)
        return motor_pb2.GetVelocityResponse(velocity=motor.getMaxVelocity())

    def SetTorque(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{request.name}' not found.")
            return Empty()
        motor.setTorque(request.torque)
        return Empty()

    def GetTorqueFeedback(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetTorqueFeedbackResponse(torque=0.0)
        return motor_pb2.GetTorqueFeedbackResponse(torque=motor.getTorqueFeedback())

    def GetMinPosition(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetMinPositionResponse(min_position=0.0)
        return motor_pb2.GetMinPositionResponse(min_position=motor.getMinPosition())

    def GetMaxPosition(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetMaxPositionResponse(max_position=0.0)
        return motor_pb2.GetMaxPositionResponse(max_position=motor.getMaxPosition())

    def SetControlPID(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{request.name}' not found.")
            return Empty()
        motor.setControlPID(request.p, request.i, request.d)
        return Empty()

    def GetTargetPosition(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetTargetPositionResponse(target_position=0.0)
        return motor_pb2.GetTargetPositionResponse(target_position=motor.getTargetPosition())

    def GetPositionSensor(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetPositionSensorResponse(position_sensor_name="")
        position_sensor = motor.getPositionSensor()
        if position_sensor is None:
            return motor_pb2.GetPositionSensorResponse(position_sensor_name="")
        return motor_pb2.GetPositionSensorResponse(position_sensor_name=position_sensor.getName())
