# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/spot/v1/params.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bnibiru/spot/v1/params.proto\x12\x0enibiru.spot.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x83\x02\n\x06Params\x12\x30\n\x14starting_pool_number\x18\x01 \x01(\x04R\x12startingPoolNumber\x12\x93\x01\n\x11pool_creation_fee\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBL\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:\"pool_creation_fee\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x0fpoolCreationFee\x12+\n\x11whitelisted_asset\x18\x03 \x03(\tR\x10whitelistedAsset:\x04\x98\xa0\x1f\x00\x42,Z*github.com/NibiruChain/nibiru/x/spot/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nibiru.spot.v1.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/spot/types'
  _PARAMS.fields_by_name['pool_creation_fee']._options = None
  _PARAMS.fields_by_name['pool_creation_fee']._serialized_options = b'\310\336\037\000\362\336\037\030yaml:\"pool_creation_fee\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\230\240\037\000'
  _PARAMS._serialized_start=129
  _PARAMS._serialized_end=388
# @@protoc_insertion_point(module_scope)
