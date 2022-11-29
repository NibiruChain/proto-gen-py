# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dex/v1/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64\x65x/v1/event.proto\x12\rnibiru.dex.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xd5\x01\n\x0f\x45ventPoolJoined\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07pool_id\x18\x02 \x01(\x04\x12\x32\n\ttokens_in\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x38\n\x0fpool_shares_out\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x32\n\trem_coins\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"4\n\x10\x45ventPoolCreated\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07pool_id\x18\x02 \x01(\x04\"\xa1\x01\n\x0f\x45ventPoolExited\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07pool_id\x18\x02 \x01(\x04\x12\x37\n\x0epool_shares_in\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x33\n\ntokens_out\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x9d\x01\n\x12\x45ventAssetsSwapped\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07pool_id\x18\x02 \x01(\x04\x12\x31\n\x08token_in\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x32\n\ttoken_out\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x42+Z)github.com/NibiruChain/nibiru/x/dex/typesb\x06proto3')



_EVENTPOOLJOINED = DESCRIPTOR.message_types_by_name['EventPoolJoined']
_EVENTPOOLCREATED = DESCRIPTOR.message_types_by_name['EventPoolCreated']
_EVENTPOOLEXITED = DESCRIPTOR.message_types_by_name['EventPoolExited']
_EVENTASSETSSWAPPED = DESCRIPTOR.message_types_by_name['EventAssetsSwapped']
EventPoolJoined = _reflection.GeneratedProtocolMessageType('EventPoolJoined', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPOOLJOINED,
  '__module__' : 'dex.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.dex.v1.EventPoolJoined)
  })
_sym_db.RegisterMessage(EventPoolJoined)

EventPoolCreated = _reflection.GeneratedProtocolMessageType('EventPoolCreated', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPOOLCREATED,
  '__module__' : 'dex.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.dex.v1.EventPoolCreated)
  })
_sym_db.RegisterMessage(EventPoolCreated)

EventPoolExited = _reflection.GeneratedProtocolMessageType('EventPoolExited', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPOOLEXITED,
  '__module__' : 'dex.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.dex.v1.EventPoolExited)
  })
_sym_db.RegisterMessage(EventPoolExited)

EventAssetsSwapped = _reflection.GeneratedProtocolMessageType('EventAssetsSwapped', (_message.Message,), {
  'DESCRIPTOR' : _EVENTASSETSSWAPPED,
  '__module__' : 'dex.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.dex.v1.EventAssetsSwapped)
  })
_sym_db.RegisterMessage(EventAssetsSwapped)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/NibiruChain/nibiru/x/dex/types'
  _EVENTPOOLJOINED.fields_by_name['tokens_in']._options = None
  _EVENTPOOLJOINED.fields_by_name['tokens_in']._serialized_options = b'\310\336\037\000'
  _EVENTPOOLJOINED.fields_by_name['pool_shares_out']._options = None
  _EVENTPOOLJOINED.fields_by_name['pool_shares_out']._serialized_options = b'\310\336\037\000'
  _EVENTPOOLJOINED.fields_by_name['rem_coins']._options = None
  _EVENTPOOLJOINED.fields_by_name['rem_coins']._serialized_options = b'\310\336\037\000'
  _EVENTPOOLEXITED.fields_by_name['pool_shares_in']._options = None
  _EVENTPOOLEXITED.fields_by_name['pool_shares_in']._serialized_options = b'\310\336\037\000'
  _EVENTPOOLEXITED.fields_by_name['tokens_out']._options = None
  _EVENTPOOLEXITED.fields_by_name['tokens_out']._serialized_options = b'\310\336\037\000'
  _EVENTASSETSSWAPPED.fields_by_name['token_in']._options = None
  _EVENTASSETSSWAPPED.fields_by_name['token_in']._serialized_options = b'\310\336\037\000'
  _EVENTASSETSSWAPPED.fields_by_name['token_out']._options = None
  _EVENTASSETSSWAPPED.fields_by_name['token_out']._serialized_options = b'\310\336\037\000'
  _EVENTPOOLJOINED._serialized_start=92
  _EVENTPOOLJOINED._serialized_end=305
  _EVENTPOOLCREATED._serialized_start=307
  _EVENTPOOLCREATED._serialized_end=359
  _EVENTPOOLEXITED._serialized_start=362
  _EVENTPOOLEXITED._serialized_end=523
  _EVENTASSETSSWAPPED._serialized_start=526
  _EVENTASSETSSWAPPED._serialized_end=683
# @@protoc_insertion_point(module_scope)
