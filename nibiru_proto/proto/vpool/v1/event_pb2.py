# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vpool/v1/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14vpool/v1/event.proto\x12\x0fnibiru.vpool.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x02\n\x19ReserveSnapshotSavedEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\x45\n\rquote_reserve\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0c\x62\x61se_reserve\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nmark_price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0c\x62lock_height\x18\x05 \x01(\x03\x12=\n\x0f\x62lock_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"\xab\x01\n\x10SwapOnVpoolEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\x44\n\x0cquote_amount\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x43\n\x0b\x62\x61se_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xa3\x01\n\x15MarkPriceChangedEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12=\n\x05price\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12=\n\x0f\x62lock_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x42-Z+github.com/NibiruChain/nibiru/x/vpool/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vpool.v1.event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/NibiruChain/nibiru/x/vpool/types'
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['quote_reserve']._options = None
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['quote_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['base_reserve']._options = None
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['base_reserve']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['mark_price']._options = None
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['mark_price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['block_timestamp']._options = None
  _RESERVESNAPSHOTSAVEDEVENT.fields_by_name['block_timestamp']._serialized_options = b'\220\337\037\001\310\336\037\000'
  _SWAPONVPOOLEVENT.fields_by_name['quote_amount']._options = None
  _SWAPONVPOOLEVENT.fields_by_name['quote_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _SWAPONVPOOLEVENT.fields_by_name['base_amount']._options = None
  _SWAPONVPOOLEVENT.fields_by_name['base_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MARKPRICECHANGEDEVENT.fields_by_name['price']._options = None
  _MARKPRICECHANGEDEVENT.fields_by_name['price']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MARKPRICECHANGEDEVENT.fields_by_name['block_timestamp']._options = None
  _MARKPRICECHANGEDEVENT.fields_by_name['block_timestamp']._serialized_options = b'\220\337\037\001\310\336\037\000'
  _RESERVESNAPSHOTSAVEDEVENT._serialized_start=156
  _RESERVESNAPSHOTSAVEDEVENT._serialized_end=491
  _SWAPONVPOOLEVENT._serialized_start=494
  _SWAPONVPOOLEVENT._serialized_end=665
  _MARKPRICECHANGEDEVENT._serialized_start=668
  _MARKPRICECHANGEDEVENT._serialized_end=831
# @@protoc_insertion_point(module_scope)
