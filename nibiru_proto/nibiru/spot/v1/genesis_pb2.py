# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/spot/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nibiru_proto.nibiru.spot.v1 import params_pb2 as nibiru_dot_spot_dot_v1_dot_params__pb2
from nibiru_proto.nibiru.spot.v1 import pool_pb2 as nibiru_dot_spot_dot_v1_dot_pool__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cnibiru/spot/v1/genesis.proto\x12\x0enibiru.spot.v1\x1a\x1bnibiru/spot/v1/params.proto\x1a\x19nibiru/spot/v1/pool.proto\x1a\x14gogoproto/gogo.proto\"v\n\x0cGenesisState\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32\x16.nibiru.spot.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12\x30\n\x05pools\x18\x02 \x03(\x0b\x32\x14.nibiru.spot.v1.PoolB\x04\xc8\xde\x1f\x00R\x05poolsB,Z*github.com/NibiruChain/nibiru/x/spot/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nibiru.spot.v1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/spot/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['pools']._options = None
  _GENESISSTATE.fields_by_name['pools']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=126
  _GENESISSTATE._serialized_end=244
# @@protoc_insertion_point(module_scope)
