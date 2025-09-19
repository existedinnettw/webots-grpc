"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'device.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cdevice.proto\x12\x06webots"\x1d\n\rDeviceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"@\n\x0eDeviceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x11\n\tnode_type\x18\x03 \x01(\x05"$\n\x13DeviceModelResponse\x12\r\n\x05model\x18\x01 \x01(\t"%\n\x10NodeTypeResponse\x12\x11\n\tnode_type\x18\x01 \x01(\x05" \n\x11DeviceTagResponse\x12\x0b\n\x03tag\x18\x01 \x01(\x052\xd1\x01\n\rDeviceService\x12D\n\x0eGetDeviceModel\x12\x15.webots.DeviceRequest\x1a\x1b.webots.DeviceModelResponse\x12>\n\x0bGetNodeType\x12\x15.webots.DeviceRequest\x1a\x18.webots.NodeTypeResponse\x12:\n\x06GetTag\x12\x15.webots.DeviceRequest\x1a\x19.webots.DeviceTagResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'device_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DEVICEREQUEST']._serialized_start = 24
    _globals['_DEVICEREQUEST']._serialized_end = 53
    _globals['_DEVICERESPONSE']._serialized_start = 55
    _globals['_DEVICERESPONSE']._serialized_end = 119
    _globals['_DEVICEMODELRESPONSE']._serialized_start = 121
    _globals['_DEVICEMODELRESPONSE']._serialized_end = 157
    _globals['_NODETYPERESPONSE']._serialized_start = 159
    _globals['_NODETYPERESPONSE']._serialized_end = 196
    _globals['_DEVICETAGRESPONSE']._serialized_start = 198
    _globals['_DEVICETAGRESPONSE']._serialized_end = 230
    _globals['_DEVICESERVICE']._serialized_start = 233
    _globals['_DEVICESERVICE']._serialized_end = 442