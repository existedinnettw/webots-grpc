"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'robot.proto')
_sym_db = _symbol_database.Default()
from . import device_pb2 as device__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0brobot.proto\x12\x06webots\x1a\x0cdevice.proto\x1a\x1bgoogle/protobuf/empty.proto"!\n\x11RobotNameResponse\x12\x0c\n\x04name\x18\x01 \x01(\t"#\n\x12RobotModelResponse\x12\r\n\x05model\x18\x01 \x01(\t"!\n\x11CustomDataRequest\x12\x0c\n\x04data\x18\x01 \x01(\t""\n\x12CustomDataResponse\x12\x0c\n\x04data\x18\x01 \x01(\t"=\n\x12DeviceListResponse\x12\'\n\x07devices\x18\x01 \x03(\x0b2\x16.webots.DeviceResponse"3\n\x18GetBasicTimeStepResponse\x12\x17\n\x0fbasic_time_step\x18\x01 \x01(\x01" \n\x0bStepRequest\x12\x11\n\ttime_step\x18\x01 \x01(\x05"\x1f\n\x0cStepResponse\x12\x0f\n\x07success\x18\x01 \x01(\x082\xa1\x04\n\x0cRobotService\x12A\n\x0cGetRobotName\x12\x16.google.protobuf.Empty\x1a\x19.webots.RobotNameResponse\x12C\n\rGetRobotModel\x12\x16.google.protobuf.Empty\x1a\x1a.webots.RobotModelResponse\x12C\n\rGetCustomData\x12\x16.google.protobuf.Empty\x1a\x1a.webots.CustomDataResponse\x12B\n\rSetCustomData\x12\x19.webots.CustomDataRequest\x1a\x16.google.protobuf.Empty\x12:\n\tGetDevice\x12\x15.webots.DeviceRequest\x1a\x16.webots.DeviceResponse\x12C\n\rGetDeviceList\x12\x16.google.protobuf.Empty\x1a\x1a.webots.DeviceListResponse\x12L\n\x10GetBasicTimeStep\x12\x16.google.protobuf.Empty\x1a .webots.GetBasicTimeStepResponse\x121\n\x04Step\x12\x13.webots.StepRequest\x1a\x14.webots.StepResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'robot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_ROBOTNAMERESPONSE']._serialized_start = 66
    _globals['_ROBOTNAMERESPONSE']._serialized_end = 99
    _globals['_ROBOTMODELRESPONSE']._serialized_start = 101
    _globals['_ROBOTMODELRESPONSE']._serialized_end = 136
    _globals['_CUSTOMDATAREQUEST']._serialized_start = 138
    _globals['_CUSTOMDATAREQUEST']._serialized_end = 171
    _globals['_CUSTOMDATARESPONSE']._serialized_start = 173
    _globals['_CUSTOMDATARESPONSE']._serialized_end = 207
    _globals['_DEVICELISTRESPONSE']._serialized_start = 209
    _globals['_DEVICELISTRESPONSE']._serialized_end = 270
    _globals['_GETBASICTIMESTEPRESPONSE']._serialized_start = 272
    _globals['_GETBASICTIMESTEPRESPONSE']._serialized_end = 323
    _globals['_STEPREQUEST']._serialized_start = 325
    _globals['_STEPREQUEST']._serialized_end = 357
    _globals['_STEPRESPONSE']._serialized_start = 359
    _globals['_STEPRESPONSE']._serialized_end = 390
    _globals['_ROBOTSERVICE']._serialized_start = 393
    _globals['_ROBOTSERVICE']._serialized_end = 938