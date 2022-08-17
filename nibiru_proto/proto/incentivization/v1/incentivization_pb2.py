# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: incentivization/v1/incentivization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(incentivization/v1/incentivization.proto\x12\x19nibiru.incentivization.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xab\x02\n\x1fMsgCreateIncentivizationProgram\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08lp_denom\x18\x02 \x01(\t\x12<\n\x13min_lockup_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\x98\xdf\x1f\x01\x12\x34\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x0e\n\x06\x65pochs\x18\x05 \x01(\x03\x12\x62\n\rinitial_funds\x18\x07 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"=\n\'MsgCreateIncentivizationProgramResponse\x12\x12\n\nprogram_id\x18\x01 \x01(\x04\"\x97\x01\n\x1dMsgFundIncentivizationProgram\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12Z\n\x05\x66unds\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\'\n%MsgFundIncentivizationProgramResponse\"\xe4\x01\n\x16IncentivizationProgram\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x16\n\x0e\x65scrow_address\x18\x02 \x01(\t\x12\x18\n\x10remaining_epochs\x18\x03 \x01(\x03\x12\x10\n\x08lp_denom\x18\x04 \x01(\t\x12@\n\x13min_lockup_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x98\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x38\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\"c\n\x0cGenesisState\x12S\n\x18incentivization_programs\x18\x01 \x03(\x0b\x32\x31.nibiru.incentivization.v1.IncentivizationProgram\"0\n\"QueryIncentivizationProgramRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"y\n#QueryIncentivizationProgramResponse\x12R\n\x17incentivization_program\x18\x01 \x01(\x0b\x32\x31.nibiru.incentivization.v1.IncentivizationProgram\"a\n#QueryIncentivizationProgramsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb8\x01\n$QueryIncentivizationProgramsResponse\x12S\n\x18incentivization_programs\x18\x01 \x03(\x0b\x32\x31.nibiru.incentivization.v1.IncentivizationProgram\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x8f\x03\n\x03Msg\x12\xc6\x01\n\x1c\x43reateIncentivizationProgram\x12:.nibiru.incentivization.v1.MsgCreateIncentivizationProgram\x1a\x42.nibiru.incentivization.v1.MsgCreateIncentivizationProgramResponse\"&\x82\xd3\xe4\x93\x02 \"\x1e/nibiru/incentivization/create\x12\xbe\x01\n\x1a\x46undIncentivizationProgram\x12\x38.nibiru.incentivization.v1.MsgFundIncentivizationProgram\x1a@.nibiru.incentivization.v1.MsgFundIncentivizationProgramResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x1c/nibiru/incentivization/fund2\xb7\x03\n\x05Query\x12\xd3\x01\n\x16IncentivizationProgram\x12=.nibiru.incentivization.v1.QueryIncentivizationProgramRequest\x1a>.nibiru.incentivization.v1.QueryIncentivizationProgramResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/nibiru/incentivization/v1/incentivization_program\x12\xd7\x01\n\x17IncentivizationPrograms\x12>.nibiru.incentivization.v1.QueryIncentivizationProgramsRequest\x1a?.nibiru.incentivization.v1.QueryIncentivizationProgramsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/nibiru/incentivization/v1/incentivization_programsB7Z5github.com/NibiruChain/nibiru/x/incentivization/typesb\x06proto3')



_MSGCREATEINCENTIVIZATIONPROGRAM = DESCRIPTOR.message_types_by_name['MsgCreateIncentivizationProgram']
_MSGCREATEINCENTIVIZATIONPROGRAMRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateIncentivizationProgramResponse']
_MSGFUNDINCENTIVIZATIONPROGRAM = DESCRIPTOR.message_types_by_name['MsgFundIncentivizationProgram']
_MSGFUNDINCENTIVIZATIONPROGRAMRESPONSE = DESCRIPTOR.message_types_by_name['MsgFundIncentivizationProgramResponse']
_INCENTIVIZATIONPROGRAM = DESCRIPTOR.message_types_by_name['IncentivizationProgram']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_QUERYINCENTIVIZATIONPROGRAMREQUEST = DESCRIPTOR.message_types_by_name['QueryIncentivizationProgramRequest']
_QUERYINCENTIVIZATIONPROGRAMRESPONSE = DESCRIPTOR.message_types_by_name['QueryIncentivizationProgramResponse']
_QUERYINCENTIVIZATIONPROGRAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryIncentivizationProgramsRequest']
_QUERYINCENTIVIZATIONPROGRAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryIncentivizationProgramsResponse']
MsgCreateIncentivizationProgram = _reflection.GeneratedProtocolMessageType('MsgCreateIncentivizationProgram', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEINCENTIVIZATIONPROGRAM,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.MsgCreateIncentivizationProgram)
  })
_sym_db.RegisterMessage(MsgCreateIncentivizationProgram)

MsgCreateIncentivizationProgramResponse = _reflection.GeneratedProtocolMessageType('MsgCreateIncentivizationProgramResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEINCENTIVIZATIONPROGRAMRESPONSE,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.MsgCreateIncentivizationProgramResponse)
  })
_sym_db.RegisterMessage(MsgCreateIncentivizationProgramResponse)

MsgFundIncentivizationProgram = _reflection.GeneratedProtocolMessageType('MsgFundIncentivizationProgram', (_message.Message,), {
  'DESCRIPTOR' : _MSGFUNDINCENTIVIZATIONPROGRAM,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.MsgFundIncentivizationProgram)
  })
_sym_db.RegisterMessage(MsgFundIncentivizationProgram)

MsgFundIncentivizationProgramResponse = _reflection.GeneratedProtocolMessageType('MsgFundIncentivizationProgramResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGFUNDINCENTIVIZATIONPROGRAMRESPONSE,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.MsgFundIncentivizationProgramResponse)
  })
_sym_db.RegisterMessage(MsgFundIncentivizationProgramResponse)

IncentivizationProgram = _reflection.GeneratedProtocolMessageType('IncentivizationProgram', (_message.Message,), {
  'DESCRIPTOR' : _INCENTIVIZATIONPROGRAM,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.IncentivizationProgram)
  })
_sym_db.RegisterMessage(IncentivizationProgram)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

QueryIncentivizationProgramRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivizationProgramRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVIZATIONPROGRAMREQUEST,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.QueryIncentivizationProgramRequest)
  })
_sym_db.RegisterMessage(QueryIncentivizationProgramRequest)

QueryIncentivizationProgramResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivizationProgramResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVIZATIONPROGRAMRESPONSE,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.QueryIncentivizationProgramResponse)
  })
_sym_db.RegisterMessage(QueryIncentivizationProgramResponse)

QueryIncentivizationProgramsRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivizationProgramsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVIZATIONPROGRAMSREQUEST,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.QueryIncentivizationProgramsRequest)
  })
_sym_db.RegisterMessage(QueryIncentivizationProgramsRequest)

QueryIncentivizationProgramsResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivizationProgramsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINCENTIVIZATIONPROGRAMSRESPONSE,
  '__module__' : 'incentivization.v1.incentivization_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.incentivization.v1.QueryIncentivizationProgramsResponse)
  })
_sym_db.RegisterMessage(QueryIncentivizationProgramsResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/NibiruChain/nibiru/x/incentivization/types'
  _MSGCREATEINCENTIVIZATIONPROGRAM.fields_by_name['min_lockup_duration']._options = None
  _MSGCREATEINCENTIVIZATIONPROGRAM.fields_by_name['min_lockup_duration']._serialized_options = b'\230\337\037\001'
  _MSGCREATEINCENTIVIZATIONPROGRAM.fields_by_name['start_time']._options = None
  _MSGCREATEINCENTIVIZATIONPROGRAM.fields_by_name['start_time']._serialized_options = b'\220\337\037\001'
  _MSGCREATEINCENTIVIZATIONPROGRAM.fields_by_name['initial_funds']._options = None
  _MSGCREATEINCENTIVIZATIONPROGRAM.fields_by_name['initial_funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGFUNDINCENTIVIZATIONPROGRAM.fields_by_name['funds']._options = None
  _MSGFUNDINCENTIVIZATIONPROGRAM.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _INCENTIVIZATIONPROGRAM.fields_by_name['min_lockup_duration']._options = None
  _INCENTIVIZATIONPROGRAM.fields_by_name['min_lockup_duration']._serialized_options = b'\230\337\037\001\310\336\037\000'
  _INCENTIVIZATIONPROGRAM.fields_by_name['start_time']._options = None
  _INCENTIVIZATIONPROGRAM.fields_by_name['start_time']._serialized_options = b'\220\337\037\001\310\336\037\000'
  _MSG.methods_by_name['CreateIncentivizationProgram']._options = None
  _MSG.methods_by_name['CreateIncentivizationProgram']._serialized_options = b'\202\323\344\223\002 \"\036/nibiru/incentivization/create'
  _MSG.methods_by_name['FundIncentivizationProgram']._options = None
  _MSG.methods_by_name['FundIncentivizationProgram']._serialized_options = b'\202\323\344\223\002\036\"\034/nibiru/incentivization/fund'
  _QUERY.methods_by_name['IncentivizationProgram']._options = None
  _QUERY.methods_by_name['IncentivizationProgram']._serialized_options = b'\202\323\344\223\0024\0222/nibiru/incentivization/v1/incentivization_program'
  _QUERY.methods_by_name['IncentivizationPrograms']._options = None
  _QUERY.methods_by_name['IncentivizationPrograms']._serialized_options = b'\202\323\344\223\0025\0223/nibiru/incentivization/v1/incentivization_programs'
  _MSGCREATEINCENTIVIZATIONPROGRAM._serialized_start=265
  _MSGCREATEINCENTIVIZATIONPROGRAM._serialized_end=564
  _MSGCREATEINCENTIVIZATIONPROGRAMRESPONSE._serialized_start=566
  _MSGCREATEINCENTIVIZATIONPROGRAMRESPONSE._serialized_end=627
  _MSGFUNDINCENTIVIZATIONPROGRAM._serialized_start=630
  _MSGFUNDINCENTIVIZATIONPROGRAM._serialized_end=781
  _MSGFUNDINCENTIVIZATIONPROGRAMRESPONSE._serialized_start=783
  _MSGFUNDINCENTIVIZATIONPROGRAMRESPONSE._serialized_end=822
  _INCENTIVIZATIONPROGRAM._serialized_start=825
  _INCENTIVIZATIONPROGRAM._serialized_end=1053
  _GENESISSTATE._serialized_start=1055
  _GENESISSTATE._serialized_end=1154
  _QUERYINCENTIVIZATIONPROGRAMREQUEST._serialized_start=1156
  _QUERYINCENTIVIZATIONPROGRAMREQUEST._serialized_end=1204
  _QUERYINCENTIVIZATIONPROGRAMRESPONSE._serialized_start=1206
  _QUERYINCENTIVIZATIONPROGRAMRESPONSE._serialized_end=1327
  _QUERYINCENTIVIZATIONPROGRAMSREQUEST._serialized_start=1329
  _QUERYINCENTIVIZATIONPROGRAMSREQUEST._serialized_end=1426
  _QUERYINCENTIVIZATIONPROGRAMSRESPONSE._serialized_start=1429
  _QUERYINCENTIVIZATIONPROGRAMSRESPONSE._serialized_end=1613
  _MSG._serialized_start=1616
  _MSG._serialized_end=2015
  _QUERY._serialized_start=2018
  _QUERY._serialized_end=2457
# @@protoc_insertion_point(module_scope)