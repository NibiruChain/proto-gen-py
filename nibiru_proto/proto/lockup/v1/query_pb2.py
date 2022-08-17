# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lockup/v1/query.proto
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
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from lockup.v1 import lock_pb2 as lockup_dot_v1_dot_lock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15lockup/v1/query.proto\x12\x10nibiru.lockup.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14lockup/v1/lock.proto\"*\n\x17QueryLockedCoinsRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"}\n\x18QueryLockedCoinsResponse\x12\x61\n\x0clocked_coins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x1e\n\x10QueryLockRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"9\n\x11QueryLockResponse\x12$\n\x04lock\x18\x01 \x01(\x0b\x32\x16.nibiru.lockup.v1.Lock\"b\n\x13QueryLocksByAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x81\x01\n\x1bQueryLocksByAddressResponse\x12%\n\x05locks\x18\x01 \x03(\x0b\x32\x16.nibiru.lockup.v1.Lock\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x93\x03\n\x05Query\x12\x89\x01\n\x0bLockedCoins\x12).nibiru.lockup.v1.QueryLockedCoinsRequest\x1a*.nibiru.lockup.v1.QueryLockedCoinsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/nibiru/lockup/locked_coins\x12l\n\x04Lock\x12\".nibiru.lockup.v1.QueryLockRequest\x1a#.nibiru.lockup.v1.QueryLockResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/nibiru/lockup/lock\x12\x8f\x01\n\x0eLocksByAddress\x12%.nibiru.lockup.v1.QueryLocksByAddress\x1a-.nibiru.lockup.v1.QueryLocksByAddressResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/nibiru/lockup/locks_by_addressB.Z,github.com/NibiruChain/nibiru/x/lockup/typesb\x06proto3')



_QUERYLOCKEDCOINSREQUEST = DESCRIPTOR.message_types_by_name['QueryLockedCoinsRequest']
_QUERYLOCKEDCOINSRESPONSE = DESCRIPTOR.message_types_by_name['QueryLockedCoinsResponse']
_QUERYLOCKREQUEST = DESCRIPTOR.message_types_by_name['QueryLockRequest']
_QUERYLOCKRESPONSE = DESCRIPTOR.message_types_by_name['QueryLockResponse']
_QUERYLOCKSBYADDRESS = DESCRIPTOR.message_types_by_name['QueryLocksByAddress']
_QUERYLOCKSBYADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['QueryLocksByAddressResponse']
QueryLockedCoinsRequest = _reflection.GeneratedProtocolMessageType('QueryLockedCoinsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLOCKEDCOINSREQUEST,
  '__module__' : 'lockup.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.QueryLockedCoinsRequest)
  })
_sym_db.RegisterMessage(QueryLockedCoinsRequest)

QueryLockedCoinsResponse = _reflection.GeneratedProtocolMessageType('QueryLockedCoinsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLOCKEDCOINSRESPONSE,
  '__module__' : 'lockup.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.QueryLockedCoinsResponse)
  })
_sym_db.RegisterMessage(QueryLockedCoinsResponse)

QueryLockRequest = _reflection.GeneratedProtocolMessageType('QueryLockRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLOCKREQUEST,
  '__module__' : 'lockup.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.QueryLockRequest)
  })
_sym_db.RegisterMessage(QueryLockRequest)

QueryLockResponse = _reflection.GeneratedProtocolMessageType('QueryLockResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLOCKRESPONSE,
  '__module__' : 'lockup.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.QueryLockResponse)
  })
_sym_db.RegisterMessage(QueryLockResponse)

QueryLocksByAddress = _reflection.GeneratedProtocolMessageType('QueryLocksByAddress', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLOCKSBYADDRESS,
  '__module__' : 'lockup.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.QueryLocksByAddress)
  })
_sym_db.RegisterMessage(QueryLocksByAddress)

QueryLocksByAddressResponse = _reflection.GeneratedProtocolMessageType('QueryLocksByAddressResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLOCKSBYADDRESSRESPONSE,
  '__module__' : 'lockup.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.QueryLocksByAddressResponse)
  })
_sym_db.RegisterMessage(QueryLocksByAddressResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/lockup/types'
  _QUERYLOCKEDCOINSRESPONSE.fields_by_name['locked_coins']._options = None
  _QUERYLOCKEDCOINSRESPONSE.fields_by_name['locked_coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERY.methods_by_name['LockedCoins']._options = None
  _QUERY.methods_by_name['LockedCoins']._serialized_options = b'\202\323\344\223\002\035\022\033/nibiru/lockup/locked_coins'
  _QUERY.methods_by_name['Lock']._options = None
  _QUERY.methods_by_name['Lock']._serialized_options = b'\202\323\344\223\002\025\022\023/nibiru/lockup/lock'
  _QUERY.methods_by_name['LocksByAddress']._options = None
  _QUERY.methods_by_name['LocksByAddress']._serialized_options = b'\202\323\344\223\002!\022\037/nibiru/lockup/locks_by_address'
  _QUERYLOCKEDCOINSREQUEST._serialized_start=193
  _QUERYLOCKEDCOINSREQUEST._serialized_end=235
  _QUERYLOCKEDCOINSRESPONSE._serialized_start=237
  _QUERYLOCKEDCOINSRESPONSE._serialized_end=362
  _QUERYLOCKREQUEST._serialized_start=364
  _QUERYLOCKREQUEST._serialized_end=394
  _QUERYLOCKRESPONSE._serialized_start=396
  _QUERYLOCKRESPONSE._serialized_end=453
  _QUERYLOCKSBYADDRESS._serialized_start=455
  _QUERYLOCKSBYADDRESS._serialized_end=553
  _QUERYLOCKSBYADDRESSRESPONSE._serialized_start=556
  _QUERYLOCKSBYADDRESSRESPONSE._serialized_end=685
  _QUERY._serialized_start=688
  _QUERY._serialized_end=1091
# @@protoc_insertion_point(module_scope)