# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PaulaCastillejoBravo_Protobuf-puerta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*PaulaCastillejoBravo_Protobuf-puerta.proto\"\xf1\x01\n\x0bSwitchboard\x12\n\n\x02id\x18\x01 \x01(\x05\x12\'\n\x06option\x18\x02 \x01(\x0e\x32\x17.Switchboard.OptionType\x12\'\n\x08openDoor\x18\x03 \x01(\x0e\x32\x15.Switchboard.OpenType\x12\x10\n\x08openTime\x18\x04 \x01(\x05\x12\x10\n\x08obstacle\x18\x05 \x01(\t\x12\r\n\x05motor\x18\x06 \x01(\t\",\n\nOptionType\x12\x08\n\x04OPEN\x10\x00\x12\t\n\x05\x43LOSE\x10\x01\x12\t\n\x05STATE\x10\x02\"#\n\x08OpenType\x12\n\n\x06PERSON\x10\x00\x12\x0b\n\x07VEHICLE\x10\x01\"\x8f\x01\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\x05\x12 \n\x06result\x18\x02 \x01(\x0e\x32\x10.Response.Result\"U\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0e\x44OOR_JUST_OPEN\x10\x01\x12\x13\n\x0f\x44OOR_JUST_CLOSE\x10\x02\x12\x0c\n\x08OBSTACLE\x10\x03\x12\x0c\n\x08NO_MOTOR\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PaulaCastillejoBravo_Protobuf_puerta_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SWITCHBOARD']._serialized_start=47
  _globals['_SWITCHBOARD']._serialized_end=288
  _globals['_SWITCHBOARD_OPTIONTYPE']._serialized_start=207
  _globals['_SWITCHBOARD_OPTIONTYPE']._serialized_end=251
  _globals['_SWITCHBOARD_OPENTYPE']._serialized_start=253
  _globals['_SWITCHBOARD_OPENTYPE']._serialized_end=288
  _globals['_RESPONSE']._serialized_start=291
  _globals['_RESPONSE']._serialized_end=434
  _globals['_RESPONSE_RESULT']._serialized_start=349
  _globals['_RESPONSE_RESULT']._serialized_end=434
# @@protoc_insertion_point(module_scope)