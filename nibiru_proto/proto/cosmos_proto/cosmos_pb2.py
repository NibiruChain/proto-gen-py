# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos_proto/cosmos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63osmos_proto/cosmos.proto\x12\x0c\x63osmos_proto\x1a google/protobuf/descriptor.proto:9\n\x0einterface_type\x12\x1f.google.protobuf.MessageOptions\x18\xc9\xd6\x05 \x01(\t:?\n\x14implements_interface\x12\x1f.google.protobuf.MessageOptions\x18\xca\xd6\x05 \x01(\t::\n\x11\x61\x63\x63\x65pts_interface\x12\x1d.google.protobuf.FieldOptions\x18\xc9\xd6\x05 \x01(\tB\'Z%github.com/regen-network/cosmos-protob\x06proto3')


INTERFACE_TYPE_FIELD_NUMBER = 93001
interface_type = DESCRIPTOR.extensions_by_name['interface_type']
IMPLEMENTS_INTERFACE_FIELD_NUMBER = 93002
implements_interface = DESCRIPTOR.extensions_by_name['implements_interface']
ACCEPTS_INTERFACE_FIELD_NUMBER = 93001
accepts_interface = DESCRIPTOR.extensions_by_name['accepts_interface']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(interface_type)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(implements_interface)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(accepts_interface)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%github.com/regen-network/cosmos-proto'
# @@protoc_insertion_point(module_scope)
