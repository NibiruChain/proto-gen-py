# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pricefeed/params.proto
"""Generated protocol buffer code."""
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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16pricefeed/params.proto\x12\x13nibiru.pricefeed.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x13\x63ommon/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbc\x01\n\x06Params\x12-\n\x05pairs\x18\x01 \x03(\x0b\x32\x18.nibiru.common.AssetPairB\x04\xc8\xde\x1f\x00\x12\x82\x01\n\x14twap_lookback_window\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationBI\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x1etwap_lookback_window,omitempty\xf2\xde\x1f\x1byaml:\"twap_lookback_window\"\"V\n\x10OraclesMarshaler\x12\x42\n\x07oracles\x18\x01 \x03(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\"(\n\x13\x41\x63tivePairMarshaler\x12\x11\n\tis_active\x18\x01 \x01(\x08\"\xaf\x01\n\x0bPostedPrice\x12\x1b\n\x07pair_id\x18\x01 \x01(\tB\n\xe2\xde\x1f\x06PairID\x12\x0e\n\x06oracle\x18\x02 \x01(\t\x12=\n\x05price\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x34\n\x06\x65xpiry\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"j\n\x0c\x43urrentPrice\x12\x1b\n\x07pair_id\x18\x01 \x01(\tB\n\xe2\xde\x1f\x06PairID\x12=\n\x05price\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xf1\x01\n\x0b\x43urrentTWAP\x12\x1b\n\x07pair_id\x18\x01 \x01(\tB\n\xe2\xde\x1f\x06PairID\x12\x41\n\tnumerator\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x43\n\x0b\x64\x65nominator\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12=\n\x05price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x35Z/github.com/NibiruChain/nibiru/x/pricefeed/types\xa8\xe2\x1e\x01\x62\x06proto3')



_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_ORACLESMARSHALER = DESCRIPTOR.message_types_by_name['OraclesMarshaler']
_ACTIVEPAIRMARSHALER = DESCRIPTOR.message_types_by_name['ActivePairMarshaler']
_POSTEDPRICE = DESCRIPTOR.message_types_by_name['PostedPrice']
_CURRENTPRICE = DESCRIPTOR.message_types_by_name['CurrentPrice']
_CURRENTTWAP = DESCRIPTOR.message_types_by_name['CurrentTWAP']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'pricefeed.params_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.pricefeed.v1.Params)
  })
_sym_db.RegisterMessage(Params)

OraclesMarshaler = _reflection.GeneratedProtocolMessageType('OraclesMarshaler', (_message.Message,), {
  'DESCRIPTOR' : _ORACLESMARSHALER,
  '__module__' : 'pricefeed.params_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.pricefeed.v1.OraclesMarshaler)
  })
_sym_db.RegisterMessage(OraclesMarshaler)

ActivePairMarshaler = _reflection.GeneratedProtocolMessageType('ActivePairMarshaler', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVEPAIRMARSHALER,
  '__module__' : 'pricefeed.params_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.pricefeed.v1.ActivePairMarshaler)
  })
_sym_db.RegisterMessage(ActivePairMarshaler)

PostedPrice = _reflection.GeneratedProtocolMessageType('PostedPrice', (_message.Message,), {
  'DESCRIPTOR' : _POSTEDPRICE,
  '__module__' : 'pricefeed.params_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.pricefeed.v1.PostedPrice)
  })
_sym_db.RegisterMessage(PostedPrice)

CurrentPrice = _reflection.GeneratedProtocolMessageType('CurrentPrice', (_message.Message,), {
  'DESCRIPTOR' : _CURRENTPRICE,
  '__module__' : 'pricefeed.params_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.pricefeed.v1.CurrentPrice)
  })
_sym_db.RegisterMessage(CurrentPrice)

CurrentTWAP = _reflection.GeneratedProtocolMessageType('CurrentTWAP', (_message.Message,), {
  'DESCRIPTOR' : _CURRENTTWAP,
  '__module__' : 'pricefeed.params_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.pricefeed.v1.CurrentTWAP)
  })
_sym_db.RegisterMessage(CurrentTWAP)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/NibiruChain/nibiru/x/pricefeed/types\250\342\036\001'
  _PARAMS.fields_by_name['pairs']._options = None
  _PARAMS.fields_by_name['pairs']._serialized_options = b'\310\336\037\000'
  _PARAMS.fields_by_name['twap_lookback_window']._options = None
  _PARAMS.fields_by_name['twap_lookback_window']._serialized_options = b'\310\336\037\000\230\337\037\001\352\336\037\036twap_lookback_window,omitempty\362\336\037\033yaml:\"twap_lookback_window\"'
  _ORACLESMARSHALER.fields_by_name['oracles']._options = None
  _ORACLESMARSHALER.fields_by_name['oracles']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _POSTEDPRICE.fields_by_name['pair_id']._options = None
  _POSTEDPRICE.fields_by_name['pair_id']._serialized_options = b'\342\336\037\006PairID'
  _POSTEDPRICE.fields_by_name['price']._options = None
  _POSTEDPRICE.fields_by_name['price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _POSTEDPRICE.fields_by_name['expiry']._options = None
  _POSTEDPRICE.fields_by_name['expiry']._serialized_options = b'\220\337\037\001\310\336\037\000'
  _CURRENTPRICE.fields_by_name['pair_id']._options = None
  _CURRENTPRICE.fields_by_name['pair_id']._serialized_options = b'\342\336\037\006PairID'
  _CURRENTPRICE.fields_by_name['price']._options = None
  _CURRENTPRICE.fields_by_name['price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _CURRENTTWAP.fields_by_name['pair_id']._options = None
  _CURRENTTWAP.fields_by_name['pair_id']._serialized_options = b'\342\336\037\006PairID'
  _CURRENTTWAP.fields_by_name['numerator']._options = None
  _CURRENTTWAP.fields_by_name['numerator']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _CURRENTTWAP.fields_by_name['denominator']._options = None
  _CURRENTTWAP.fields_by_name['denominator']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _CURRENTTWAP.fields_by_name['price']._options = None
  _CURRENTTWAP.fields_by_name['price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS._serialized_start=183
  _PARAMS._serialized_end=371
  _ORACLESMARSHALER._serialized_start=373
  _ORACLESMARSHALER._serialized_end=459
  _ACTIVEPAIRMARSHALER._serialized_start=461
  _ACTIVEPAIRMARSHALER._serialized_end=501
  _POSTEDPRICE._serialized_start=504
  _POSTEDPRICE._serialized_end=679
  _CURRENTPRICE._serialized_start=681
  _CURRENTPRICE._serialized_end=787
  _CURRENTTWAP._serialized_start=790
  _CURRENTTWAP._serialized_end=1031
# @@protoc_insertion_point(module_scope)