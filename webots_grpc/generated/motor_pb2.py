"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'motor.proto')
_sym_db = _symbol_database.Default()
from . import device_pb2 as device__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmotor.proto\x12\x06webots\x1a\x0cdevice.proto\x1a\x1bgoogle/protobuf/empty.proto"\x1c\n\x0cMotorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x85\x01\n\rMotorResponse\x12&\n\x06device\x18\x01 \x01(\x0b2\x16.webots.DeviceResponse\x12(\n\x04type\x18\x02 \x01(\x0e2\x1a.webots.MotorResponse.Type""\n\x04Type\x12\x0e\n\nROTATIONAL\x10\x00\x12\n\n\x06LINEAR\x10\x01"4\n\x12SetPositionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08position\x18\x02 \x01(\x02"4\n\x12SetVelocityRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08velocity\x18\x02 \x01(\x02"\'\n\x13GetVelocityResponse\x12\x10\n\x08velocity\x18\x01 \x01(\x02"0\n\x10SetTorqueRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06torque\x18\x02 \x01(\x02"+\n\x19GetTorqueFeedbackResponse\x12\x0e\n\x06torque\x18\x01 \x01(\x02".\n\x16GetMinPositionResponse\x12\x14\n\x0cmin_position\x18\x01 \x01(\x02".\n\x16GetMaxPositionResponse\x12\x14\n\x0cmax_position\x18\x01 \x01(\x02"E\n\x14SetControlPIDRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01p\x18\x02 \x01(\x02\x12\t\n\x01i\x18\x03 \x01(\x02\x12\t\n\x01d\x18\x04 \x01(\x02"4\n\x19GetTargetPositionResponse\x12\x17\n\x0ftarget_position\x18\x01 \x01(\x02"9\n\x19GetPositionSensorResponse\x12\x1c\n\x14position_sensor_name\x18\x01 \x01(\t2\xd4\x06\n\x0cMotorService\x127\n\x08GetMotor\x12\x14.webots.MotorRequest\x1a\x15.webots.MotorResponse\x12A\n\x0bSetPosition\x12\x1a.webots.SetPositionRequest\x1a\x16.google.protobuf.Empty\x12A\n\x0bSetVelocity\x12\x1a.webots.SetVelocityRequest\x1a\x16.google.protobuf.Empty\x12@\n\x0bGetVelocity\x12\x14.webots.MotorRequest\x1a\x1b.webots.GetVelocityResponse\x12C\n\x0eGetMaxVelocity\x12\x14.webots.MotorRequest\x1a\x1b.webots.GetVelocityResponse\x12=\n\tSetTorque\x12\x18.webots.SetTorqueRequest\x1a\x16.google.protobuf.Empty\x12L\n\x11GetTorqueFeedback\x12\x14.webots.MotorRequest\x1a!.webots.GetTorqueFeedbackResponse\x12F\n\x0eGetMinPosition\x12\x14.webots.MotorRequest\x1a\x1e.webots.GetMinPositionResponse\x12F\n\x0eGetMaxPosition\x12\x14.webots.MotorRequest\x1a\x1e.webots.GetMaxPositionResponse\x12E\n\rSetControlPID\x12\x1c.webots.SetControlPIDRequest\x1a\x16.google.protobuf.Empty\x12L\n\x11GetTargetPosition\x12\x14.webots.MotorRequest\x1a!.webots.GetTargetPositionResponse\x12L\n\x11GetPositionSensor\x12\x14.webots.MotorRequest\x1a!.webots.GetPositionSensorResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'motor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_MOTORREQUEST']._serialized_start = 66
    _globals['_MOTORREQUEST']._serialized_end = 94
    _globals['_MOTORRESPONSE']._serialized_start = 97
    _globals['_MOTORRESPONSE']._serialized_end = 230
    _globals['_MOTORRESPONSE_TYPE']._serialized_start = 196
    _globals['_MOTORRESPONSE_TYPE']._serialized_end = 230
    _globals['_SETPOSITIONREQUEST']._serialized_start = 232
    _globals['_SETPOSITIONREQUEST']._serialized_end = 284
    _globals['_SETVELOCITYREQUEST']._serialized_start = 286
    _globals['_SETVELOCITYREQUEST']._serialized_end = 338
    _globals['_GETVELOCITYRESPONSE']._serialized_start = 340
    _globals['_GETVELOCITYRESPONSE']._serialized_end = 379
    _globals['_SETTORQUEREQUEST']._serialized_start = 381
    _globals['_SETTORQUEREQUEST']._serialized_end = 429
    _globals['_GETTORQUEFEEDBACKRESPONSE']._serialized_start = 431
    _globals['_GETTORQUEFEEDBACKRESPONSE']._serialized_end = 474
    _globals['_GETMINPOSITIONRESPONSE']._serialized_start = 476
    _globals['_GETMINPOSITIONRESPONSE']._serialized_end = 522
    _globals['_GETMAXPOSITIONRESPONSE']._serialized_start = 524
    _globals['_GETMAXPOSITIONRESPONSE']._serialized_end = 570
    _globals['_SETCONTROLPIDREQUEST']._serialized_start = 572
    _globals['_SETCONTROLPIDREQUEST']._serialized_end = 641
    _globals['_GETTARGETPOSITIONRESPONSE']._serialized_start = 643
    _globals['_GETTARGETPOSITIONRESPONSE']._serialized_end = 695
    _globals['_GETPOSITIONSENSORRESPONSE']._serialized_start = 697
    _globals['_GETPOSITIONSENSORRESPONSE']._serialized_end = 754
    _globals['_MOTORSERVICE']._serialized_start = 757
    _globals['_MOTORSERVICE']._serialized_end = 1609