"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import motor_pb2 as motor__pb2
GRPC_GENERATED_VERSION = '1.71.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in motor_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class MotorServiceStub(object):
    """*
    @see [webots/include/controller/cpp/webots/Motor.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/Motor.hpp)
    @see webots/src/controller/cpp/Motor.cpp
    @see webots/lib/controller/python/controller/motor.py
    @see [Webots Reference Manual-Motor](https://www.cyberbotics.com/doc/reference/motor)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMotor = channel.unary_unary('/webots.MotorService/GetMotor', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.MotorResponse.FromString, _registered_method=True)
        self.SetPosition = channel.unary_unary('/webots.MotorService/SetPosition', request_serializer=motor__pb2.SetPositionRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.SetVelocity = channel.unary_unary('/webots.MotorService/SetVelocity', request_serializer=motor__pb2.SetVelocityRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetVelocity = channel.unary_unary('/webots.MotorService/GetVelocity', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetVelocityResponse.FromString, _registered_method=True)
        self.GetMaxVelocity = channel.unary_unary('/webots.MotorService/GetMaxVelocity', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetVelocityResponse.FromString, _registered_method=True)
        self.SetTorque = channel.unary_unary('/webots.MotorService/SetTorque', request_serializer=motor__pb2.SetTorqueRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetTorqueFeedback = channel.unary_unary('/webots.MotorService/GetTorqueFeedback', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetTorqueFeedbackResponse.FromString, _registered_method=True)
        self.GetMinPosition = channel.unary_unary('/webots.MotorService/GetMinPosition', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetMinPositionResponse.FromString, _registered_method=True)
        self.GetMaxPosition = channel.unary_unary('/webots.MotorService/GetMaxPosition', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetMaxPositionResponse.FromString, _registered_method=True)
        self.SetControlPID = channel.unary_unary('/webots.MotorService/SetControlPID', request_serializer=motor__pb2.SetControlPIDRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetTargetPosition = channel.unary_unary('/webots.MotorService/GetTargetPosition', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetTargetPositionResponse.FromString, _registered_method=True)
        self.GetPositionSensor = channel.unary_unary('/webots.MotorService/GetPositionSensor', request_serializer=motor__pb2.MotorRequest.SerializeToString, response_deserializer=motor__pb2.GetPositionSensorResponse.FromString, _registered_method=True)

class MotorServiceServicer(object):
    """*
    @see [webots/include/controller/cpp/webots/Motor.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/Motor.hpp)
    @see webots/src/controller/cpp/Motor.cpp
    @see webots/lib/controller/python/controller/motor.py
    @see [Webots Reference Manual-Motor](https://www.cyberbotics.com/doc/reference/motor)
    """

    def GetMotor(self, request, context):
        """Retrieves motor details by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPosition(self, request, context):
        """Sets the target position of the motor.
        `name`: The name of the motor.
        `position`: The target position in radians (for rotational motors) or meters (for linear motors).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVelocity(self, request, context):
        """Sets the velocity of the motor.
        `name`: The name of the motor.
        `velocity`: The target velocity in radians/second or meters/second.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVelocity(self, request, context):
        """Retrieves the current velocity of the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMaxVelocity(self, request, context):
        """Retrieves the maximum velocity of the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTorque(self, request, context):
        """Sets the torque of the motor.
        `name`: The name of the motor.
        `torque`: The target torque in Nm.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTorqueFeedback(self, request, context):
        """Retrieves the torque feedback of the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMinPosition(self, request, context):
        """Retrieves the minimum position of the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMaxPosition(self, request, context):
        """Retrieves the maximum position of the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetControlPID(self, request, context):
        """Sets the PID control parameters for the motor.
        `name`: The name of the motor.
        `p`: Proportional gain.
        `i`: Integral gain.
        `d`: Derivative gain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTargetPosition(self, request, context):
        """Retrieves the target position of the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPositionSensor(self, request, context):
        """Retrieves the name of the position sensor attached to the motor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MotorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetMotor': grpc.unary_unary_rpc_method_handler(servicer.GetMotor, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.MotorResponse.SerializeToString), 'SetPosition': grpc.unary_unary_rpc_method_handler(servicer.SetPosition, request_deserializer=motor__pb2.SetPositionRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'SetVelocity': grpc.unary_unary_rpc_method_handler(servicer.SetVelocity, request_deserializer=motor__pb2.SetVelocityRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetVelocity': grpc.unary_unary_rpc_method_handler(servicer.GetVelocity, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetVelocityResponse.SerializeToString), 'GetMaxVelocity': grpc.unary_unary_rpc_method_handler(servicer.GetMaxVelocity, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetVelocityResponse.SerializeToString), 'SetTorque': grpc.unary_unary_rpc_method_handler(servicer.SetTorque, request_deserializer=motor__pb2.SetTorqueRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetTorqueFeedback': grpc.unary_unary_rpc_method_handler(servicer.GetTorqueFeedback, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetTorqueFeedbackResponse.SerializeToString), 'GetMinPosition': grpc.unary_unary_rpc_method_handler(servicer.GetMinPosition, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetMinPositionResponse.SerializeToString), 'GetMaxPosition': grpc.unary_unary_rpc_method_handler(servicer.GetMaxPosition, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetMaxPositionResponse.SerializeToString), 'SetControlPID': grpc.unary_unary_rpc_method_handler(servicer.SetControlPID, request_deserializer=motor__pb2.SetControlPIDRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetTargetPosition': grpc.unary_unary_rpc_method_handler(servicer.GetTargetPosition, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetTargetPositionResponse.SerializeToString), 'GetPositionSensor': grpc.unary_unary_rpc_method_handler(servicer.GetPositionSensor, request_deserializer=motor__pb2.MotorRequest.FromString, response_serializer=motor__pb2.GetPositionSensorResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('webots.MotorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('webots.MotorService', rpc_method_handlers)

class MotorService(object):
    """*
    @see [webots/include/controller/cpp/webots/Motor.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/Motor.hpp)
    @see webots/src/controller/cpp/Motor.cpp
    @see webots/lib/controller/python/controller/motor.py
    @see [Webots Reference Manual-Motor](https://www.cyberbotics.com/doc/reference/motor)
    """

    @staticmethod
    def GetMotor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetMotor', motor__pb2.MotorRequest.SerializeToString, motor__pb2.MotorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetPosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/SetPosition', motor__pb2.SetPositionRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetVelocity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/SetVelocity', motor__pb2.SetVelocityRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetVelocity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetVelocity', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetVelocityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMaxVelocity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetMaxVelocity', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetVelocityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetTorque(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/SetTorque', motor__pb2.SetTorqueRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTorqueFeedback(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetTorqueFeedback', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetTorqueFeedbackResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMinPosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetMinPosition', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetMinPositionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMaxPosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetMaxPosition', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetMaxPositionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetControlPID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/SetControlPID', motor__pb2.SetControlPIDRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTargetPosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetTargetPosition', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetTargetPositionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPositionSensor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.MotorService/GetPositionSensor', motor__pb2.MotorRequest.SerializeToString, motor__pb2.GetPositionSensorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)