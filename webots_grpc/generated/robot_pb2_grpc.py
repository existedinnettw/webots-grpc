"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from . import device_pb2 as device__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import robot_pb2 as robot__pb2
GRPC_GENERATED_VERSION = '1.71.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in robot_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class RobotServiceStub(object):
    """*
    @see [webots/include/controller/cpp/webots/Robot.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/Robot.hpp)
    @see webots/src/controller/cpp/Robot.cpp
    @see webots/lib/controller/python/controller/robot.py
    @see [Webots Reference Manual - Robot](https://www.cyberbotics.com/doc/reference/robot)
    @details This service provides access to robot-level functionalities, such as retrieving the robot's name, model, custom data, and devices, as well as controlling the simulation step.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRobotName = channel.unary_unary('/webots.RobotService/GetRobotName', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=robot__pb2.RobotNameResponse.FromString, _registered_method=True)
        self.GetRobotModel = channel.unary_unary('/webots.RobotService/GetRobotModel', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=robot__pb2.RobotModelResponse.FromString, _registered_method=True)
        self.GetCustomData = channel.unary_unary('/webots.RobotService/GetCustomData', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=robot__pb2.CustomDataResponse.FromString, _registered_method=True)
        self.SetCustomData = channel.unary_unary('/webots.RobotService/SetCustomData', request_serializer=robot__pb2.CustomDataRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetDevice = channel.unary_unary('/webots.RobotService/GetDevice', request_serializer=device__pb2.DeviceRequest.SerializeToString, response_deserializer=device__pb2.DeviceResponse.FromString, _registered_method=True)
        self.GetDeviceList = channel.unary_unary('/webots.RobotService/GetDeviceList', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=robot__pb2.DeviceListResponse.FromString, _registered_method=True)
        self.GetBasicTimeStep = channel.unary_unary('/webots.RobotService/GetBasicTimeStep', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=robot__pb2.GetBasicTimeStepResponse.FromString, _registered_method=True)
        self.Step = channel.unary_unary('/webots.RobotService/Step', request_serializer=robot__pb2.StepRequest.SerializeToString, response_deserializer=robot__pb2.StepResponse.FromString, _registered_method=True)

class RobotServiceServicer(object):
    """*
    @see [webots/include/controller/cpp/webots/Robot.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/Robot.hpp)
    @see webots/src/controller/cpp/Robot.cpp
    @see webots/lib/controller/python/controller/robot.py
    @see [Webots Reference Manual - Robot](https://www.cyberbotics.com/doc/reference/robot)
    @details This service provides access to robot-level functionalities, such as retrieving the robot's name, model, custom data, and devices, as well as controlling the simulation step.
    """

    def GetRobotName(self, request, context):
        """*
        Retrieves the name of the robot.
        @return RobotNameResponse - The response containing the robot's name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRobotModel(self, request, context):
        """*
        Retrieves the model of the robot.
        @return RobotModelResponse - The response containing the robot's model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomData(self, request, context):
        """*
        Retrieves the custom data associated with the robot.
        @return CustomDataResponse - The response containing the custom data as a string.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCustomData(self, request, context):
        """*
        Sets custom data for the robot.
        @param CustomDataRequest - The request containing the custom data to set.
        @return google.protobuf.Empty - An empty response indicating success.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevice(self, request, context):
        """*
        Retrieves a device by its name.
        @param DeviceRequest - The request containing the device name.
        @return DeviceResponse - The response containing the device information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceList(self, request, context):
        """*
        Retrieves the list of all devices associated with the robot.
        @return DeviceListResponse - The response containing a list of devices.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBasicTimeStep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Step(self, request, context):
        """*
        Advances the simulation by a specified time step.
        @param StepRequest - The request containing the time step in milliseconds.
        @return StepResponse - The response indicating whether the step was successful.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_RobotServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetRobotName': grpc.unary_unary_rpc_method_handler(servicer.GetRobotName, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=robot__pb2.RobotNameResponse.SerializeToString), 'GetRobotModel': grpc.unary_unary_rpc_method_handler(servicer.GetRobotModel, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=robot__pb2.RobotModelResponse.SerializeToString), 'GetCustomData': grpc.unary_unary_rpc_method_handler(servicer.GetCustomData, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=robot__pb2.CustomDataResponse.SerializeToString), 'SetCustomData': grpc.unary_unary_rpc_method_handler(servicer.SetCustomData, request_deserializer=robot__pb2.CustomDataRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetDevice': grpc.unary_unary_rpc_method_handler(servicer.GetDevice, request_deserializer=device__pb2.DeviceRequest.FromString, response_serializer=device__pb2.DeviceResponse.SerializeToString), 'GetDeviceList': grpc.unary_unary_rpc_method_handler(servicer.GetDeviceList, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=robot__pb2.DeviceListResponse.SerializeToString), 'GetBasicTimeStep': grpc.unary_unary_rpc_method_handler(servicer.GetBasicTimeStep, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=robot__pb2.GetBasicTimeStepResponse.SerializeToString), 'Step': grpc.unary_unary_rpc_method_handler(servicer.Step, request_deserializer=robot__pb2.StepRequest.FromString, response_serializer=robot__pb2.StepResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('webots.RobotService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('webots.RobotService', rpc_method_handlers)

class RobotService(object):
    """*
    @see [webots/include/controller/cpp/webots/Robot.hpp](https://github.com/cyberbotics/webots/blob/master/include/controller/cpp/webots/Robot.hpp)
    @see webots/src/controller/cpp/Robot.cpp
    @see webots/lib/controller/python/controller/robot.py
    @see [Webots Reference Manual - Robot](https://www.cyberbotics.com/doc/reference/robot)
    @details This service provides access to robot-level functionalities, such as retrieving the robot's name, model, custom data, and devices, as well as controlling the simulation step.
    """

    @staticmethod
    def GetRobotName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/GetRobotName', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, robot__pb2.RobotNameResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetRobotModel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/GetRobotModel', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, robot__pb2.RobotModelResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCustomData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/GetCustomData', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, robot__pb2.CustomDataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetCustomData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/SetCustomData', robot__pb2.CustomDataRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/GetDevice', device__pb2.DeviceRequest.SerializeToString, device__pb2.DeviceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetDeviceList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/GetDeviceList', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, robot__pb2.DeviceListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetBasicTimeStep(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/GetBasicTimeStep', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, robot__pb2.GetBasicTimeStepResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Step(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/webots.RobotService/Step', robot__pb2.StepRequest.SerializeToString, robot__pb2.StepResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)