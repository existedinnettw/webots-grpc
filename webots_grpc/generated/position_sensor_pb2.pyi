import sensor_pb2 as _sensor_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PositionSensorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetTypeResponse(_message.Message):
    __slots__ = ('type',)

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROTATIONAL: _ClassVar[GetTypeResponse.Type]
        LINEAR: _ClassVar[GetTypeResponse.Type]
    ROTATIONAL: GetTypeResponse.Type
    LINEAR: GetTypeResponse.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: GetTypeResponse.Type

    def __init__(self, type: _Optional[_Union[GetTypeResponse.Type, str]]=...) -> None:
        ...

class GetBrakeTagResponse(_message.Message):
    __slots__ = ('brake_tag',)
    BRAKE_TAG_FIELD_NUMBER: _ClassVar[int]
    brake_tag: int

    def __init__(self, brake_tag: _Optional[int]=...) -> None:
        ...

class GetMotorTagResponse(_message.Message):
    __slots__ = ('motor_tag',)
    MOTOR_TAG_FIELD_NUMBER: _ClassVar[int]
    motor_tag: int

    def __init__(self, motor_tag: _Optional[int]=...) -> None:
        ...