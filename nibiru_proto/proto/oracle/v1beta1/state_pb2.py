# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oracle/v1beta1/state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from oracle.v1beta1 import oracle_pb2 as oracle_dot_v1beta1_dot_oracle__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aoracle/v1beta1/state.proto\x12\x15nibiru.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1boracle/v1beta1/oracle.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xbc\x01\n\rPriceSnapshot\x12V\n\x04pair\x18\x01 \x01(\tBH\xf2\xde\x1f\x0byaml:\"pair\"\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.Pair\xc8\xde\x1f\x00\x12=\n\x05price\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x03\x42.Z,github.com/NibiruChain/nibiru/x/oracle/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'oracle.v1beta1.state_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/oracle/types'
  _PRICESNAPSHOT.fields_by_name['pair']._options = None
  _PRICESNAPSHOT.fields_by_name['pair']._serialized_options = b'\362\336\037\013yaml:\"pair\"\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair\310\336\037\000'
  _PRICESNAPSHOT.fields_by_name['price']._options = None
  _PRICESNAPSHOT.fields_by_name['price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PRICESNAPSHOT._serialized_start=167
  _PRICESNAPSHOT._serialized_end=355
# @@protoc_insertion_point(module_scope)
