import device_pb2 as _device_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RobotNameResponse(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RobotModelResponse(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class CustomDataRequest(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str

    def __init__(self, data: _Optional[str]=...) -> None:
        ...

class CustomDataResponse(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str

    def __init__(self, data: _Optional[str]=...) -> None:
        ...

class DeviceListResponse(_message.Message):
    __slots__ = ('devices',)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.DeviceResponse]

    def __init__(self, devices: _Optional[_Iterable[_Union[_device_pb2.DeviceResponse, _Mapping]]]=...) -> None:
        ...

class GetBasicTimeStepResponse(_message.Message):
    __slots__ = ('basic_time_step',)
    BASIC_TIME_STEP_FIELD_NUMBER: _ClassVar[int]
    basic_time_step: float

    def __init__(self, basic_time_step: _Optional[float]=...) -> None:
        ...

class StepRequest(_message.Message):
    __slots__ = ('time_step',)
    TIME_STEP_FIELD_NUMBER: _ClassVar[int]
    time_step: int

    def __init__(self, time_step: _Optional[int]=...) -> None:
        ...

class StepResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...