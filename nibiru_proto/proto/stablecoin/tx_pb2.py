# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stablecoin/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13stablecoin/tx.proto\x12\x14nibiru.stablecoin.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\"Q\n\rMsgMintStable\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12/\n\x06stable\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x8a\x02\n\x15MsgMintStableResponse\x12/\n\x06stable\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12_\n\nused_coins\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12_\n\nfees_payed\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"Q\n\rMsgBurnStable\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12/\n\x06stable\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\xdb\x01\n\x15MsgBurnStableResponse\x12\x33\n\ncollateral\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12,\n\x03gov\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12_\n\nfees_payed\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"T\n\x12MsgRecollateralize\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12-\n\x04\x63oll\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"J\n\x1aMsgRecollateralizeResponse\x12,\n\x03gov\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"K\n\nMsgBuyback\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12,\n\x03gov\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"C\n\x12MsgBuybackResponse\x12-\n\x04\x63oll\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x32\x9d\x04\n\x03Msg\x12\x82\x01\n\nMintStable\x12#.nibiru.stablecoin.v1.MsgMintStable\x1a+.nibiru.stablecoin.v1.MsgMintStableResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/stablecoin/mint-sc\x12\x82\x01\n\nBurnStable\x12#.nibiru.stablecoin.v1.MsgBurnStable\x1a+.nibiru.stablecoin.v1.MsgBurnStableResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/stablecoin/burn-sc\x12\x90\x01\n\x0fRecollateralize\x12(.nibiru.stablecoin.v1.MsgRecollateralize\x1a\x30.nibiru.stablecoin.v1.MsgRecollateralizeResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/nibiru/stablecoin/recoll\x12y\n\x07\x42uyback\x12 .nibiru.stablecoin.v1.MsgBuyback\x1a(.nibiru.stablecoin.v1.MsgBuybackResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/stablecoin/buybackB2Z0github.com/NibiruChain/nibiru/x/stablecoin/typesb\x06proto3')



_MSGMINTSTABLE = DESCRIPTOR.message_types_by_name['MsgMintStable']
_MSGMINTSTABLERESPONSE = DESCRIPTOR.message_types_by_name['MsgMintStableResponse']
_MSGBURNSTABLE = DESCRIPTOR.message_types_by_name['MsgBurnStable']
_MSGBURNSTABLERESPONSE = DESCRIPTOR.message_types_by_name['MsgBurnStableResponse']
_MSGRECOLLATERALIZE = DESCRIPTOR.message_types_by_name['MsgRecollateralize']
_MSGRECOLLATERALIZERESPONSE = DESCRIPTOR.message_types_by_name['MsgRecollateralizeResponse']
_MSGBUYBACK = DESCRIPTOR.message_types_by_name['MsgBuyback']
_MSGBUYBACKRESPONSE = DESCRIPTOR.message_types_by_name['MsgBuybackResponse']
MsgMintStable = _reflection.GeneratedProtocolMessageType('MsgMintStable', (_message.Message,), {
  'DESCRIPTOR' : _MSGMINTSTABLE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgMintStable)
  })
_sym_db.RegisterMessage(MsgMintStable)

MsgMintStableResponse = _reflection.GeneratedProtocolMessageType('MsgMintStableResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGMINTSTABLERESPONSE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgMintStableResponse)
  })
_sym_db.RegisterMessage(MsgMintStableResponse)

MsgBurnStable = _reflection.GeneratedProtocolMessageType('MsgBurnStable', (_message.Message,), {
  'DESCRIPTOR' : _MSGBURNSTABLE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgBurnStable)
  })
_sym_db.RegisterMessage(MsgBurnStable)

MsgBurnStableResponse = _reflection.GeneratedProtocolMessageType('MsgBurnStableResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGBURNSTABLERESPONSE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgBurnStableResponse)
  })
_sym_db.RegisterMessage(MsgBurnStableResponse)

MsgRecollateralize = _reflection.GeneratedProtocolMessageType('MsgRecollateralize', (_message.Message,), {
  'DESCRIPTOR' : _MSGRECOLLATERALIZE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgRecollateralize)
  })
_sym_db.RegisterMessage(MsgRecollateralize)

MsgRecollateralizeResponse = _reflection.GeneratedProtocolMessageType('MsgRecollateralizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGRECOLLATERALIZERESPONSE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgRecollateralizeResponse)
  })
_sym_db.RegisterMessage(MsgRecollateralizeResponse)

MsgBuyback = _reflection.GeneratedProtocolMessageType('MsgBuyback', (_message.Message,), {
  'DESCRIPTOR' : _MSGBUYBACK,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgBuyback)
  })
_sym_db.RegisterMessage(MsgBuyback)

MsgBuybackResponse = _reflection.GeneratedProtocolMessageType('MsgBuybackResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGBUYBACKRESPONSE,
  '__module__' : 'stablecoin.tx_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.MsgBuybackResponse)
  })
_sym_db.RegisterMessage(MsgBuybackResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/NibiruChain/nibiru/x/stablecoin/types'
  _MSGMINTSTABLE.fields_by_name['stable']._options = None
  _MSGMINTSTABLE.fields_by_name['stable']._serialized_options = b'\310\336\037\000'
  _MSGMINTSTABLERESPONSE.fields_by_name['stable']._options = None
  _MSGMINTSTABLERESPONSE.fields_by_name['stable']._serialized_options = b'\310\336\037\000'
  _MSGMINTSTABLERESPONSE.fields_by_name['used_coins']._options = None
  _MSGMINTSTABLERESPONSE.fields_by_name['used_coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGMINTSTABLERESPONSE.fields_by_name['fees_payed']._options = None
  _MSGMINTSTABLERESPONSE.fields_by_name['fees_payed']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGBURNSTABLE.fields_by_name['stable']._options = None
  _MSGBURNSTABLE.fields_by_name['stable']._serialized_options = b'\310\336\037\000'
  _MSGBURNSTABLERESPONSE.fields_by_name['collateral']._options = None
  _MSGBURNSTABLERESPONSE.fields_by_name['collateral']._serialized_options = b'\310\336\037\000'
  _MSGBURNSTABLERESPONSE.fields_by_name['gov']._options = None
  _MSGBURNSTABLERESPONSE.fields_by_name['gov']._serialized_options = b'\310\336\037\000'
  _MSGBURNSTABLERESPONSE.fields_by_name['fees_payed']._options = None
  _MSGBURNSTABLERESPONSE.fields_by_name['fees_payed']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGRECOLLATERALIZE.fields_by_name['coll']._options = None
  _MSGRECOLLATERALIZE.fields_by_name['coll']._serialized_options = b'\310\336\037\000'
  _MSGRECOLLATERALIZERESPONSE.fields_by_name['gov']._options = None
  _MSGRECOLLATERALIZERESPONSE.fields_by_name['gov']._serialized_options = b'\310\336\037\000'
  _MSGBUYBACK.fields_by_name['gov']._options = None
  _MSGBUYBACK.fields_by_name['gov']._serialized_options = b'\310\336\037\000'
  _MSGBUYBACKRESPONSE.fields_by_name['coll']._options = None
  _MSGBUYBACKRESPONSE.fields_by_name['coll']._serialized_options = b'\310\336\037\000'
  _MSG.methods_by_name['MintStable']._options = None
  _MSG.methods_by_name['MintStable']._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/stablecoin/mint-sc'
  _MSG.methods_by_name['BurnStable']._options = None
  _MSG.methods_by_name['BurnStable']._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/stablecoin/burn-sc'
  _MSG.methods_by_name['Recollateralize']._options = None
  _MSG.methods_by_name['Recollateralize']._serialized_options = b'\202\323\344\223\002\033\"\031/nibiru/stablecoin/recoll'
  _MSG.methods_by_name['Buyback']._options = None
  _MSG.methods_by_name['Buyback']._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/stablecoin/buyback'
  _MSGMINTSTABLE._serialized_start=129
  _MSGMINTSTABLE._serialized_end=210
  _MSGMINTSTABLERESPONSE._serialized_start=213
  _MSGMINTSTABLERESPONSE._serialized_end=479
  _MSGBURNSTABLE._serialized_start=481
  _MSGBURNSTABLE._serialized_end=562
  _MSGBURNSTABLERESPONSE._serialized_start=565
  _MSGBURNSTABLERESPONSE._serialized_end=784
  _MSGRECOLLATERALIZE._serialized_start=786
  _MSGRECOLLATERALIZE._serialized_end=870
  _MSGRECOLLATERALIZERESPONSE._serialized_start=872
  _MSGRECOLLATERALIZERESPONSE._serialized_end=946
  _MSGBUYBACK._serialized_start=948
  _MSGBUYBACK._serialized_end=1023
  _MSGBUYBACKRESPONSE._serialized_start=1025
  _MSGBUYBACKRESPONSE._serialized_end=1092
  _MSG._serialized_start=1095
  _MSG._serialized_end=1636
# @@protoc_insertion_point(module_scope)