"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sensor.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csensor.proto\x12\x06webots"6\n\rEnableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fsampling_period\x18\x02 \x01(\x05"4\n\x19GetSamplingPeriodResponse\x12\x17\n\x0fsampling_period\x18\x01 \x01(\x05"!\n\x10GetValueResponse\x12\r\n\x05value\x18\x01 \x01(\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_ENABLEREQUEST']._serialized_start = 24
    _globals['_ENABLEREQUEST']._serialized_end = 78
    _globals['_GETSAMPLINGPERIODRESPONSE']._serialized_start = 80
    _globals['_GETSAMPLINGPERIODRESPONSE']._serialized_end = 132
    _globals['_GETVALUERESPONSE']._serialized_start = 134
    _globals['_GETVALUERESPONSE']._serialized_end = 167