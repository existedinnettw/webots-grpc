"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'position_sensor.proto')
_sym_db = _symbol_database.Default()
from . import sensor_pb2 as sensor__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15position_sensor.proto\x12\x06webots\x1a\x0csensor.proto\x1a\x1bgoogle/protobuf/empty.proto"%\n\x15PositionSensorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"a\n\x0fGetTypeResponse\x12*\n\x04type\x18\x01 \x01(\x0e2\x1c.webots.GetTypeResponse.Type""\n\x04Type\x12\x0e\n\nROTATIONAL\x10\x00\x12\n\n\x06LINEAR\x10\x01"(\n\x13GetBrakeTagResponse\x12\x11\n\tbrake_tag\x18\x01 \x01(\x05"(\n\x13GetMotorTagResponse\x12\x11\n\tmotor_tag\x18\x01 \x01(\x052\x87\x04\n\x15PositionSensorService\x127\n\x06Enable\x12\x15.webots.EnableRequest\x1a\x16.google.protobuf.Empty\x12@\n\x07Disable\x12\x1d.webots.PositionSensorRequest\x1a\x16.google.protobuf.Empty\x12U\n\x11GetSamplingPeriod\x12\x1d.webots.PositionSensorRequest\x1a!.webots.GetSamplingPeriodResponse\x12C\n\x08GetValue\x12\x1d.webots.PositionSensorRequest\x1a\x18.webots.GetValueResponse\x12A\n\x07GetType\x12\x1d.webots.PositionSensorRequest\x1a\x17.webots.GetTypeResponse\x12I\n\x0bGetBrakeTag\x12\x1d.webots.PositionSensorRequest\x1a\x1b.webots.GetBrakeTagResponse\x12I\n\x0bGetMotorTag\x12\x1d.webots.PositionSensorRequest\x1a\x1b.webots.GetMotorTagResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'position_sensor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_POSITIONSENSORREQUEST']._serialized_start = 76
    _globals['_POSITIONSENSORREQUEST']._serialized_end = 113
    _globals['_GETTYPERESPONSE']._serialized_start = 115
    _globals['_GETTYPERESPONSE']._serialized_end = 212
    _globals['_GETTYPERESPONSE_TYPE']._serialized_start = 178
    _globals['_GETTYPERESPONSE_TYPE']._serialized_end = 212
    _globals['_GETBRAKETAGRESPONSE']._serialized_start = 214
    _globals['_GETBRAKETAGRESPONSE']._serialized_end = 254
    _globals['_GETMOTORTAGRESPONSE']._serialized_start = 256
    _globals['_GETMOTORTAGRESPONSE']._serialized_end = 296
    _globals['_POSITIONSENSORSERVICE']._serialized_start = 299
    _globals['_POSITIONSENSORSERVICE']._serialized_end = 818