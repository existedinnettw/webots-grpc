from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EnableRequest(_message.Message):
    __slots__ = ('name', 'sampling_period')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    name: str
    sampling_period: int

    def __init__(self, name: _Optional[str]=..., sampling_period: _Optional[int]=...) -> None:
        ...

class GetSamplingPeriodResponse(_message.Message):
    __slots__ = ('sampling_period',)
    SAMPLING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    sampling_period: int

    def __init__(self, sampling_period: _Optional[int]=...) -> None:
        ...

class GetValueResponse(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float

    def __init__(self, value: _Optional[float]=...) -> None:
        ...