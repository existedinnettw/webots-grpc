import device_pb2 as _device_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MotorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MotorResponse(_message.Message):
    __slots__ = ('device', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROTATIONAL: _ClassVar[MotorResponse.Type]
        LINEAR: _ClassVar[MotorResponse.Type]
    ROTATIONAL: MotorResponse.Type
    LINEAR: MotorResponse.Type
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    device: _device_pb2.DeviceResponse
    type: MotorResponse.Type

    def __init__(self, device: _Optional[_Union[_device_pb2.DeviceResponse, _Mapping]]=..., type: _Optional[_Union[MotorResponse.Type, str]]=...) -> None:
        ...

class SetPositionRequest(_message.Message):
    __slots__ = ('name', 'position')
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    position: float

    def __init__(self, name: _Optional[str]=..., position: _Optional[float]=...) -> None:
        ...

class SetVelocityRequest(_message.Message):
    __slots__ = ('name', 'velocity')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    velocity: float

    def __init__(self, name: _Optional[str]=..., velocity: _Optional[float]=...) -> None:
        ...

class GetVelocityResponse(_message.Message):
    __slots__ = ('velocity',)
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    velocity: float

    def __init__(self, velocity: _Optional[float]=...) -> None:
        ...

class SetTorqueRequest(_message.Message):
    __slots__ = ('name', 'torque')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TORQUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    torque: float

    def __init__(self, name: _Optional[str]=..., torque: _Optional[float]=...) -> None:
        ...

class GetTorqueFeedbackResponse(_message.Message):
    __slots__ = ('torque',)
    TORQUE_FIELD_NUMBER: _ClassVar[int]
    torque: float

    def __init__(self, torque: _Optional[float]=...) -> None:
        ...

class GetMinPositionResponse(_message.Message):
    __slots__ = ('min_position',)
    MIN_POSITION_FIELD_NUMBER: _ClassVar[int]
    min_position: float

    def __init__(self, min_position: _Optional[float]=...) -> None:
        ...

class GetMaxPositionResponse(_message.Message):
    __slots__ = ('max_position',)
    MAX_POSITION_FIELD_NUMBER: _ClassVar[int]
    max_position: float

    def __init__(self, max_position: _Optional[float]=...) -> None:
        ...

class SetControlPIDRequest(_message.Message):
    __slots__ = ('name', 'p', 'i', 'd')
    NAME_FIELD_NUMBER: _ClassVar[int]
    P_FIELD_NUMBER: _ClassVar[int]
    I_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    name: str
    p: float
    i: float
    d: float

    def __init__(self, name: _Optional[str]=..., p: _Optional[float]=..., i: _Optional[float]=..., d: _Optional[float]=...) -> None:
        ...

class GetTargetPositionResponse(_message.Message):
    __slots__ = ('target_position',)
    TARGET_POSITION_FIELD_NUMBER: _ClassVar[int]
    target_position: float

    def __init__(self, target_position: _Optional[float]=...) -> None:
        ...

class GetPositionSensorResponse(_message.Message):
    __slots__ = ('position_sensor_name',)
    POSITION_SENSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    position_sensor_name: str

    def __init__(self, position_sensor_name: _Optional[str]=...) -> None:
        ...