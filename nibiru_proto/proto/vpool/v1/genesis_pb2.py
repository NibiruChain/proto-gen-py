# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vpool/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from vpool.v1 import state_pb2 as vpool_dot_v1_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16vpool/v1/genesis.proto\x12\x0fnibiru.vpool.v1\x1a\x14gogoproto/gogo.proto\x1a\x14vpool/v1/state.proto\"<\n\x0cGenesisState\x12,\n\x06vpools\x18\x01 \x03(\x0b\x32\x16.nibiru.vpool.v1.VpoolB\x04\xc8\xde\x1f\x00\x42-Z+github.com/NibiruChain/nibiru/x/vpool/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'vpool.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/NibiruChain/nibiru/x/vpool/types'
  _GENESISSTATE.fields_by_name['vpools']._options = None
  _GENESISSTATE.fields_by_name['vpools']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=87
  _GENESISSTATE._serialized_end=147
# @@protoc_insertion_point(module_scope)
