"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'distance_sensor.proto')
_sym_db = _symbol_database.Default()
from . import sensor_pb2 as sensor__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15distance_sensor.proto\x12\x06webots\x1a\x0csensor.proto\x1a\x1bgoogle/protobuf/empty.proto"%\n\x15DistanceSensorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xae\x02\n\x15DistanceSensorService\x127\n\x06Enable\x12\x15.webots.EnableRequest\x1a\x16.google.protobuf.Empty\x12@\n\x07Disable\x12\x1d.webots.DistanceSensorRequest\x1a\x16.google.protobuf.Empty\x12U\n\x11GetSamplingPeriod\x12\x1d.webots.DistanceSensorRequest\x1a!.webots.GetSamplingPeriodResponse\x12C\n\x08GetValue\x12\x1d.webots.DistanceSensorRequest\x1a\x18.webots.GetValueResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'distance_sensor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DISTANCESENSORREQUEST']._serialized_start = 76
    _globals['_DISTANCESENSORREQUEST']._serialized_end = 113
    _globals['_DISTANCESENSORSERVICE']._serialized_start = 116
    _globals['_DISTANCESENSORSERVICE']._serialized_end = 418