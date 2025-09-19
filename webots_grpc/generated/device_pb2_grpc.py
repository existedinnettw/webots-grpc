"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from . import device_pb2 as device__pb2
GRPC_GENERATED_VERSION = '1.71.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in device_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class DeviceServiceStub(object):
    """*
    @see webots/include/controller/cpp/webots/Device.hpp
    @see webots/src/controller/cpp/Device.cpp
    @see webots/lib/controller/python/controller/device.py
    @see [Webots Reference Manual - Device](https://www.cyberbotics.com/doc/reference/device)
    @details This service provides access to Webots device properties and functionalities.
    It allows retrieving the model, node type, and tag of a device.
    Note: It is not meaningful to retrieve the model or node type if the device object has already been obtained.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDeviceModel = channel.unary_unary('/webots.DeviceService/GetDeviceModel', request_serializer=device__pb2.DeviceRequest.SerializeToString, response_deserializer=device__pb2.DeviceModelResponse.FromString, _registered_method=True)
        self.GetNodeType = channel.unary_unary('/webots.DeviceService/GetNodeType', request_serializer=device__pb2.DeviceRequest.SerializeToString, response_deserializer=device__pb2.NodeTypeResponse.FromString, _registered_method=True)
        self.GetTag = channel.unary_unary('/webots.DeviceService/GetTag', request_serializer=device__pb2.DeviceRequest.SerializeToString, response_deserializer=device__pb2.DeviceTagResponse.FromString, _registered_method=True)

class DeviceServiceServicer(object):
    """*
    @see webots/include/controller/cpp/webots/Device.hpp
    @see webots/src/controller/cpp/Device.cpp
    @see webots/lib/controller/python/controller/device.py
    @see [Webots Reference Manual - Device](https://www.cyberbotics.com/doc/reference/device)
    @details This service provides access to Webots device properties and functionalities.
    It allows retrieving the model, node type, and tag of a device.
    Note: It is not meaningful to retrieve the model or node type if the device object has already been obtained.

    """

    def GetDeviceModel(self, request, context):
        """*
        Retrieves the model of the device.
        @param DeviceRequest - The request containing the device name.
        @return DeviceModelResponse - The response containing the device model as a string.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodeType(self, request, context):
        """*
        Retrieves the node type of the device.
        @param DeviceRequest - The request containing the device name.
        @return NodeTypeResponse - The response containing the node type as an integer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTag(self, request, context):
        """*
        Retrieves the tag of the device.
        @param DeviceRequest - The request containing the device name.
        @return DeviceTagResponse - The response containing the device tag as an integer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DeviceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetDeviceModel': grpc.unary_unary_rpc_method_handler(servicer.GetDeviceModel, request_deserializer=device__pb2.DeviceRequest.FromString, response_serializer=device__pb2.DeviceModelResponse.SerializeToString), 'GetNodeType': grpc.unary_unary_rpc_method_handler(servicer.GetNodeType, request_deserializer=device__pb2.DeviceRequest.FromString, response_serializer=device__pb2.NodeTypeResponse.SerializeToString), 'GetTag': grpc.unary_unary_rpc_method_handler(servicer.GetTag, request_deserializer=device__pb2.DeviceRequest.FromString, response_serializer=device__pb2.DeviceTagResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('webots.DeviceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('webots.DeviceService', rpc_method_handlers)

class DeviceService(object):
    """*
    @see webots/include/controller/cpp/webots/Device.hpp
    @see webots/src/controller/cpp/Device.cpp
    @see webots/lib/controller/python/controller/device.py
    @see [Webots Reference Manual - Device](https://www.cyberbotics.com/doc/reference/device)
    @details This service provides access to Webots device properties and functionalities.
    It allows retrieving the model, node type, and tag of a device.
    Note: It is not meaningful to retrieve the model or node type if the device object has already been obtained.

    """

    @staticmethod
    def GetDeviceModel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.DeviceService/GetDeviceModel', device__pb2.DeviceRequest.SerializeToString, device__pb2.DeviceModelResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetNodeType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.DeviceService/GetNodeType', device__pb2.DeviceRequest.SerializeToString, device__pb2.NodeTypeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.DeviceService/GetTag', device__pb2.DeviceRequest.SerializeToString, device__pb2.DeviceTagResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)