# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vpool/v1/vpool.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14vpool/v1/vpool.proto\x12\x0fnibiru.vpool.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x13\x63ommon/common.proto\"\xd6\x01\n\x0fReserveSnapshot\x12J\n\x12\x62\x61se_asset_reserve\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12K\n\x13quote_asset_reserve\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x03\x12\x14\n\x0c\x62lock_number\x18\x04 \x01(\x03\"\xd2\x04\n\x04Pool\x12,\n\x04pair\x18\x01 \x01(\x0b\x32\x18.nibiru.common.AssetPairB\x04\xc8\xde\x1f\x00\x12J\n\x12\x62\x61se_asset_reserve\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12K\n\x13quote_asset_reserve\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12I\n\x11trade_limit_ratio\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x66luctuation_limit_ratio\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17max_oracle_spread_ratio\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12P\n\x18maintenance_margin_ratio\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0cmax_leverage\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xdd\x02\n\nPoolPrices\x12\x0c\n\x04pair\x18\t \x01(\t\x12\x42\n\nmark_price\x18\n \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12\x43\n\x0bindex_price\x18\x0b \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12\x41\n\ttwap_mark\x18\x0c \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12_\n\x0eswap_invariant\x18\r \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"swap_invariant\"\xc8\xde\x1f\x01\x12\x14\n\x0c\x62lock_number\x18\x0e \x01(\x03*M\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x41\x44\x44_TO_POOL\x10\x01\x12\x14\n\x10REMOVE_FROM_POOL\x10\x02*g\n\x0eTwapCalcOption\x12 \n\x1cTWAP_CALC_OPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04SPOT\x10\x01\x12\x14\n\x10QUOTE_ASSET_SWAP\x10\x02\x12\x13\n\x0f\x42\x41SE_ASSET_SWAP\x10\x03\x42-Z+github.com/NibiruChain/nibiru/x/vpool/typesb\x06proto3')

_DIRECTION = DESCRIPTOR.enum_types_by_name['Direction']
Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
_TWAPCALCOPTION = DESCRIPTOR.enum_types_by_name['TwapCalcOption']
TwapCalcOption = enum_type_wrapper.EnumTypeWrapper(_TWAPCALCOPTION)
DIRECTION_UNSPECIFIED = 0
ADD_TO_POOL = 1
REMOVE_FROM_POOL = 2
TWAP_CALC_OPTION_UNSPECIFIED = 0
SPOT = 1
QUOTE_ASSET_SWAP = 2
BASE_ASSET_SWAP = 3


_RESERVESNAPSHOT = DESCRIPTOR.message_types_by_name['ReserveSnapshot']
_POOL = DESCRIPTOR.message_types_by_name['Pool']
_POOLPRICES = DESCRIPTOR.message_types_by_name['PoolPrices']
ReserveSnapshot = _reflection.GeneratedProtocolMessageType('ReserveSnapshot', (_message.Message,), {
  'DESCRIPTOR' : _RESERVESNAPSHOT,
  '__module__' : 'vpool.v1.vpool_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.ReserveSnapshot)
  })
_sym_db.RegisterMessage(ReserveSnapshot)

Pool = _reflection.GeneratedProtocolMessageType('Pool', (_message.Message,), {
  'DESCRIPTOR' : _POOL,
  '__module__' : 'vpool.v1.vpool_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.Pool)
  })
_sym_db.RegisterMessage(Pool)

PoolPrices = _reflection.GeneratedProtocolMessageType('PoolPrices', (_message.Message,), {
  'DESCRIPTOR' : _POOLPRICES,
  '__module__' : 'vpool.v1.vpool_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.PoolPrices)
  })
_sym_db.RegisterMessage(PoolPrices)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/NibiruChain/nibiru/x/vpool/types'
  _RESERVESNAPSHOT.fields_by_name['base_asset_reserve']._options = None
  _RESERVESNAPSHOT.fields_by_name['base_asset_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _RESERVESNAPSHOT.fields_by_name['quote_asset_reserve']._options = None
  _RESERVESNAPSHOT.fields_by_name['quote_asset_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['pair']._options = None
  _POOL.fields_by_name['pair']._serialized_options = b'\310\336\037\000'
  _POOL.fields_by_name['base_asset_reserve']._options = None
  _POOL.fields_by_name['base_asset_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['quote_asset_reserve']._options = None
  _POOL.fields_by_name['quote_asset_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['trade_limit_ratio']._options = None
  _POOL.fields_by_name['trade_limit_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['fluctuation_limit_ratio']._options = None
  _POOL.fields_by_name['fluctuation_limit_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['max_oracle_spread_ratio']._options = None
  _POOL.fields_by_name['max_oracle_spread_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['maintenance_margin_ratio']._options = None
  _POOL.fields_by_name['maintenance_margin_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOL.fields_by_name['max_leverage']._options = None
  _POOL.fields_by_name['max_leverage']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POOLPRICES.fields_by_name['mark_price']._options = None
  _POOLPRICES.fields_by_name['mark_price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'
  _POOLPRICES.fields_by_name['index_price']._options = None
  _POOLPRICES.fields_by_name['index_price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'
  _POOLPRICES.fields_by_name['twap_mark']._options = None
  _POOLPRICES.fields_by_name['twap_mark']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\001'
  _POOLPRICES.fields_by_name['swap_invariant']._options = None
  _POOLPRICES.fields_by_name['swap_invariant']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"swap_invariant\"\310\336\037\001'
  _DIRECTION._serialized_start=1277
  _DIRECTION._serialized_end=1354
  _TWAPCALCOPTION._serialized_start=1356
  _TWAPCALCOPTION._serialized_end=1459
  _RESERVESNAPSHOT._serialized_start=112
  _RESERVESNAPSHOT._serialized_end=326
  _POOL._serialized_start=329
  _POOL._serialized_end=923
  _POOLPRICES._serialized_start=926
  _POOLPRICES._serialized_end=1275
# @@protoc_insertion_point(module_scope)
