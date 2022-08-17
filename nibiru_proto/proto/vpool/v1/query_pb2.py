# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vpool/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vpool.v1 import vpool_pb2 as vpool_dot_v1_dot_vpool__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14vpool/v1/query.proto\x12\x0fnibiru.vpool.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14vpool/v1/vpool.proto\")\n\x19QueryReserveAssetsRequest\x12\x0c\n\x04pair\x18\x01 \x01(\t\"\xb5\x01\n\x1aQueryReserveAssetsResponse\x12J\n\x12\x62\x61se_asset_reserve\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12K\n\x13quote_asset_reserve\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x16\n\x14QueryAllPoolsRequest\"p\n\x15QueryAllPoolsResponse\x12$\n\x05pools\x18\x01 \x03(\x0b\x32\x15.nibiru.vpool.v1.Pool\x12\x31\n\x06prices\x18\x02 \x03(\x0b\x32\x1b.nibiru.vpool.v1.PoolPricesB\x04\xc8\xde\x1f\x00\"\xa4\x01\n\x1aQueryBaseAssetPriceRequest\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12-\n\tdirection\x18\x02 \x01(\x0e\x32\x1a.nibiru.vpool.v1.Direction\x12I\n\x11\x62\x61se_asset_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"k\n\x1bQueryBaseAssetPriceResponse\x12L\n\x14price_in_quote_denom\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x32\xaa\x03\n\x05Query\x12\x8e\x01\n\rReserveAssets\x12*.nibiru.vpool.v1.QueryReserveAssetsRequest\x1a+.nibiru.vpool.v1.QueryReserveAssetsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/nibiru/vpool/reserve_assets\x12z\n\x08\x41llPools\x12%.nibiru.vpool.v1.QueryAllPoolsRequest\x1a&.nibiru.vpool.v1.QueryAllPoolsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/nibiru/vpool/all_pools\x12\x93\x01\n\x0e\x42\x61seAssetPrice\x12+.nibiru.vpool.v1.QueryBaseAssetPriceRequest\x1a,.nibiru.vpool.v1.QueryBaseAssetPriceResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/nibiru/vpool/base_asset_priceB-Z+github.com/NibiruChain/nibiru/x/vpool/typesb\x06proto3')



_QUERYRESERVEASSETSREQUEST = DESCRIPTOR.message_types_by_name['QueryReserveAssetsRequest']
_QUERYRESERVEASSETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryReserveAssetsResponse']
_QUERYALLPOOLSREQUEST = DESCRIPTOR.message_types_by_name['QueryAllPoolsRequest']
_QUERYALLPOOLSRESPONSE = DESCRIPTOR.message_types_by_name['QueryAllPoolsResponse']
_QUERYBASEASSETPRICEREQUEST = DESCRIPTOR.message_types_by_name['QueryBaseAssetPriceRequest']
_QUERYBASEASSETPRICERESPONSE = DESCRIPTOR.message_types_by_name['QueryBaseAssetPriceResponse']
QueryReserveAssetsRequest = _reflection.GeneratedProtocolMessageType('QueryReserveAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESERVEASSETSREQUEST,
  '__module__' : 'vpool.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.QueryReserveAssetsRequest)
  })
_sym_db.RegisterMessage(QueryReserveAssetsRequest)

QueryReserveAssetsResponse = _reflection.GeneratedProtocolMessageType('QueryReserveAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESERVEASSETSRESPONSE,
  '__module__' : 'vpool.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.QueryReserveAssetsResponse)
  })
_sym_db.RegisterMessage(QueryReserveAssetsResponse)

QueryAllPoolsRequest = _reflection.GeneratedProtocolMessageType('QueryAllPoolsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLPOOLSREQUEST,
  '__module__' : 'vpool.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.QueryAllPoolsRequest)
  })
_sym_db.RegisterMessage(QueryAllPoolsRequest)

QueryAllPoolsResponse = _reflection.GeneratedProtocolMessageType('QueryAllPoolsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLPOOLSRESPONSE,
  '__module__' : 'vpool.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.QueryAllPoolsResponse)
  })
_sym_db.RegisterMessage(QueryAllPoolsResponse)

QueryBaseAssetPriceRequest = _reflection.GeneratedProtocolMessageType('QueryBaseAssetPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBASEASSETPRICEREQUEST,
  '__module__' : 'vpool.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.QueryBaseAssetPriceRequest)
  })
_sym_db.RegisterMessage(QueryBaseAssetPriceRequest)

QueryBaseAssetPriceResponse = _reflection.GeneratedProtocolMessageType('QueryBaseAssetPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBASEASSETPRICERESPONSE,
  '__module__' : 'vpool.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.vpool.v1.QueryBaseAssetPriceResponse)
  })
_sym_db.RegisterMessage(QueryBaseAssetPriceResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/NibiruChain/nibiru/x/vpool/types'
  _QUERYRESERVEASSETSRESPONSE.fields_by_name['base_asset_reserve']._options = None
  _QUERYRESERVEASSETSRESPONSE.fields_by_name['base_asset_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYRESERVEASSETSRESPONSE.fields_by_name['quote_asset_reserve']._options = None
  _QUERYRESERVEASSETSRESPONSE.fields_by_name['quote_asset_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYALLPOOLSRESPONSE.fields_by_name['prices']._options = None
  _QUERYALLPOOLSRESPONSE.fields_by_name['prices']._serialized_options = b'\310\336\037\000'
  _QUERYBASEASSETPRICEREQUEST.fields_by_name['base_asset_amount']._options = None
  _QUERYBASEASSETPRICEREQUEST.fields_by_name['base_asset_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYBASEASSETPRICERESPONSE.fields_by_name['price_in_quote_denom']._options = None
  _QUERYBASEASSETPRICERESPONSE.fields_by_name['price_in_quote_denom']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERY.methods_by_name['ReserveAssets']._options = None
  _QUERY.methods_by_name['ReserveAssets']._serialized_options = b'\202\323\344\223\002\036\022\034/nibiru/vpool/reserve_assets'
  _QUERY.methods_by_name['AllPools']._options = None
  _QUERY.methods_by_name['AllPools']._serialized_options = b'\202\323\344\223\002\031\022\027/nibiru/vpool/all_pools'
  _QUERY.methods_by_name['BaseAssetPrice']._options = None
  _QUERY.methods_by_name['BaseAssetPrice']._serialized_options = b'\202\323\344\223\002 \022\036/nibiru/vpool/base_asset_price'
  _QUERYRESERVEASSETSREQUEST._serialized_start=115
  _QUERYRESERVEASSETSREQUEST._serialized_end=156
  _QUERYRESERVEASSETSRESPONSE._serialized_start=159
  _QUERYRESERVEASSETSRESPONSE._serialized_end=340
  _QUERYALLPOOLSREQUEST._serialized_start=342
  _QUERYALLPOOLSREQUEST._serialized_end=364
  _QUERYALLPOOLSRESPONSE._serialized_start=366
  _QUERYALLPOOLSRESPONSE._serialized_end=478
  _QUERYBASEASSETPRICEREQUEST._serialized_start=481
  _QUERYBASEASSETPRICEREQUEST._serialized_end=645
  _QUERYBASEASSETPRICERESPONSE._serialized_start=647
  _QUERYBASEASSETPRICERESPONSE._serialized_end=754
  _QUERY._serialized_start=757
  _QUERY._serialized_end=1183
# @@protoc_insertion_point(module_scope)