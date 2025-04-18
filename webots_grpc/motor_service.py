import grpc
from controller.motor import Motor
from controller.robot import Robot
from google.protobuf.empty_pb2 import Empty  # Import Empty for empty responses

import generated.device_pb2 as device_pb2
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

    def _get_motor(self, motor_name, context) -> Motor:
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
                type=motor_pb2.MotorResponse.Type.UNKNOWN,
            )
        wb_mot_type = motor.getType()
        if wb_mot_type == Motor.ROTATIONAL:
            motor_type = motor_pb2.MotorResponse.Type.ROTATIONAL
        elif wb_mot_type == Motor.LINEAR:
            motor_type = motor_pb2.MotorResponse.Type.LINEAR
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
        motor.setPosition(request.position)
        return Empty()

    def SetVelocity(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{request.name}' not found.")
            return Empty()
        motor.setVelocity(request.velocity)
        return Empty()

    def GetVelocity(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetVelocityResponse(velocity=0.0)
        return motor_pb2.GetVelocityResponse(velocity=motor.getVelocity())

    def SetTorque(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Motor '{request.name}' not found.")
            return Empty()
        motor.setTorque(request.torque)
        return Empty()

    def GetTorque(self, request, context):
        motor = self._get_motor(request.name, context)
        if motor is None:
            return motor_pb2.GetTorqueResponse(torque=0.0)
        return motor_pb2.GetTorqueResponse(torque=motor.getTorqueFeedback())

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
