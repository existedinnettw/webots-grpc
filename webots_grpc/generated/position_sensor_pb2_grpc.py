"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import position_sensor_pb2 as position__sensor__pb2
from . import sensor_pb2 as sensor__pb2
GRPC_GENERATED_VERSION = '1.71.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in position_sensor_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class PositionSensorServiceStub(object):
    """*
    @see webots/include/controller/cpp/webots/PositionSensor.hpp
    @see webots/src/controller/cpp/PositionSensor.cpp
    @see webots/lib/controller/python/controller/position_sensor.py
    @see [Webots Reference Manual - PositionSensor](https://www.cyberbotics.com/doc/reference/positionsensor)

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Enable = channel.unary_unary('/webots.PositionSensorService/Enable', request_serializer=sensor__pb2.EnableRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.Disable = channel.unary_unary('/webots.PositionSensorService/Disable', request_serializer=position__sensor__pb2.PositionSensorRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetSamplingPeriod = channel.unary_unary('/webots.PositionSensorService/GetSamplingPeriod', request_serializer=position__sensor__pb2.PositionSensorRequest.SerializeToString, response_deserializer=sensor__pb2.GetSamplingPeriodResponse.FromString, _registered_method=True)
        self.GetValue = channel.unary_unary('/webots.PositionSensorService/GetValue', request_serializer=position__sensor__pb2.PositionSensorRequest.SerializeToString, response_deserializer=sensor__pb2.GetValueResponse.FromString, _registered_method=True)
        self.GetType = channel.unary_unary('/webots.PositionSensorService/GetType', request_serializer=position__sensor__pb2.PositionSensorRequest.SerializeToString, response_deserializer=position__sensor__pb2.GetTypeResponse.FromString, _registered_method=True)
        self.GetBrakeTag = channel.unary_unary('/webots.PositionSensorService/GetBrakeTag', request_serializer=position__sensor__pb2.PositionSensorRequest.SerializeToString, response_deserializer=position__sensor__pb2.GetBrakeTagResponse.FromString, _registered_method=True)
        self.GetMotorTag = channel.unary_unary('/webots.PositionSensorService/GetMotorTag', request_serializer=position__sensor__pb2.PositionSensorRequest.SerializeToString, response_deserializer=position__sensor__pb2.GetMotorTagResponse.FromString, _registered_method=True)

class PositionSensorServiceServicer(object):
    """*
    @see webots/include/controller/cpp/webots/PositionSensor.hpp
    @see webots/src/controller/cpp/PositionSensor.cpp
    @see webots/lib/controller/python/controller/position_sensor.py
    @see [Webots Reference Manual - PositionSensor](https://www.cyberbotics.com/doc/reference/positionsensor)

    """

    def Enable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSamplingPeriod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBrakeTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMotorTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PositionSensorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Enable': grpc.unary_unary_rpc_method_handler(servicer.Enable, request_deserializer=sensor__pb2.EnableRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'Disable': grpc.unary_unary_rpc_method_handler(servicer.Disable, request_deserializer=position__sensor__pb2.PositionSensorRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetSamplingPeriod': grpc.unary_unary_rpc_method_handler(servicer.GetSamplingPeriod, request_deserializer=position__sensor__pb2.PositionSensorRequest.FromString, response_serializer=sensor__pb2.GetSamplingPeriodResponse.SerializeToString), 'GetValue': grpc.unary_unary_rpc_method_handler(servicer.GetValue, request_deserializer=position__sensor__pb2.PositionSensorRequest.FromString, response_serializer=sensor__pb2.GetValueResponse.SerializeToString), 'GetType': grpc.unary_unary_rpc_method_handler(servicer.GetType, request_deserializer=position__sensor__pb2.PositionSensorRequest.FromString, response_serializer=position__sensor__pb2.GetTypeResponse.SerializeToString), 'GetBrakeTag': grpc.unary_unary_rpc_method_handler(servicer.GetBrakeTag, request_deserializer=position__sensor__pb2.PositionSensorRequest.FromString, response_serializer=position__sensor__pb2.GetBrakeTagResponse.SerializeToString), 'GetMotorTag': grpc.unary_unary_rpc_method_handler(servicer.GetMotorTag, request_deserializer=position__sensor__pb2.PositionSensorRequest.FromString, response_serializer=position__sensor__pb2.GetMotorTagResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('webots.PositionSensorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('webots.PositionSensorService', rpc_method_handlers)

class PositionSensorService(object):
    """*
    @see webots/include/controller/cpp/webots/PositionSensor.hpp
    @see webots/src/controller/cpp/PositionSensor.cpp
    @see webots/lib/controller/python/controller/position_sensor.py
    @see [Webots Reference Manual - PositionSensor](https://www.cyberbotics.com/doc/reference/positionsensor)

    """

    @staticmethod
    def Enable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/Enable', sensor__pb2.EnableRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/Disable', position__sensor__pb2.PositionSensorRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSamplingPeriod(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/GetSamplingPeriod', position__sensor__pb2.PositionSensorRequest.SerializeToString, sensor__pb2.GetSamplingPeriodResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/GetValue', position__sensor__pb2.PositionSensorRequest.SerializeToString, sensor__pb2.GetValueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/GetType', position__sensor__pb2.PositionSensorRequest.SerializeToString, position__sensor__pb2.GetTypeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetBrakeTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/GetBrakeTag', position__sensor__pb2.PositionSensorRequest.SerializeToString, position__sensor__pb2.GetBrakeTagResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMotorTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.PositionSensorService/GetMotorTag', position__sensor__pb2.PositionSensorRequest.SerializeToString, position__sensor__pb2.GetMotorTagResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)