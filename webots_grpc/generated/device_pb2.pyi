from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DeviceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeviceResponse(_message.Message):
    __slots__ = ('name', 'model', 'node_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    model: str
    node_type: int

    def __init__(self, name: _Optional[str]=..., model: _Optional[str]=..., node_type: _Optional[int]=...) -> None:
        ...

class DeviceModelResponse(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class NodeTypeResponse(_message.Message):
    __slots__ = ('node_type',)
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    node_type: int

    def __init__(self, node_type: _Optional[int]=...) -> None:
        ...

class DeviceTagResponse(_message.Message):
    __slots__ = ('tag',)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: int

    def __init__(self, tag: _Optional[int]=...) -> None:
        ...