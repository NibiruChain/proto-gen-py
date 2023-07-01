# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1c\x63osmos/bank/v1beta1/tx.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\x9b\x02\n\x07MsgSend\x12;\n\x0c\x66rom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0b\x66romAddress\x12\x37\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\ttoAddress\x12h\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x06\x61mount:0\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0c\x66rom_address\x8a\xe7\xb0*\x12\x63osmos-sdk/MsgSend\"\x11\n\x0fMsgSendResponse\"\xbc\x01\n\x0cMsgMultiSend\x12=\n\x06inputs\x18\x01 \x03(\x0b\x32\x1a.cosmos.bank.v1beta1.InputB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06inputs\x12@\n\x07outputs\x18\x02 \x03(\x0b\x32\x1b.cosmos.bank.v1beta1.OutputB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07outputs:+\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06inputs\x8a\xe7\xb0*\x17\x63osmos-sdk/MsgMultiSend\"\x16\n\x14MsgMultiSendResponse\"\xbf\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12>\n\x06params\x18\x02 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params:4\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*!cosmos-sdk/x/bank/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xe9\x01\n\x11MsgSetSendEnabled\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x43\n\x0csend_enabled\x18\x02 \x03(\x0b\x32 .cosmos.bank.v1beta1.SendEnabledR\x0bsendEnabled\x12&\n\x0fuse_default_for\x18\x03 \x03(\tR\ruseDefaultFor:/\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1c\x63osmos-sdk/MsgSetSendEnabled\"\x1b\n\x19MsgSetSendEnabledResponse2\x81\x03\n\x03Msg\x12J\n\x04Send\x12\x1c.cosmos.bank.v1beta1.MsgSend\x1a$.cosmos.bank.v1beta1.MsgSendResponse\x12Y\n\tMultiSend\x12!.cosmos.bank.v1beta1.MsgMultiSend\x1a).cosmos.bank.v1beta1.MsgMultiSendResponse\x12\x62\n\x0cUpdateParams\x12$.cosmos.bank.v1beta1.MsgUpdateParams\x1a,.cosmos.bank.v1beta1.MsgUpdateParamsResponse\x12h\n\x0eSetSendEnabled\x12&.cosmos.bank.v1beta1.MsgSetSendEnabled\x1a..cosmos.bank.v1beta1.MsgSetSendEnabledResponse\x1a\x05\x80\xe7\xb0*\x01\x42+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'cosmos.bank.v1beta1.tx_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _MSGSEND.fields_by_name['from_address']._options = None
    _MSGSEND.fields_by_name[
        'from_address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _MSGSEND.fields_by_name['to_address']._options = None
    _MSGSEND.fields_by_name[
        'to_address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _MSGSEND.fields_by_name['amount']._options = None
    _MSGSEND.fields_by_name[
        'amount'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _MSGSEND._options = None
    _MSGSEND._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\014from_address\212\347\260*\022cosmos-sdk/MsgSend'
    _MSGMULTISEND.fields_by_name['inputs']._options = None
    _MSGMULTISEND.fields_by_name[
        'inputs'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _MSGMULTISEND.fields_by_name['outputs']._options = None
    _MSGMULTISEND.fields_by_name[
        'outputs'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _MSGMULTISEND._options = None
    _MSGMULTISEND._serialized_options = b'\350\240\037\000\202\347\260*\006inputs\212\347\260*\027cosmos-sdk/MsgMultiSend'
    _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
    _MSGUPDATEPARAMS.fields_by_name[
        'authority'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _MSGUPDATEPARAMS.fields_by_name['params']._options = None
    _MSGUPDATEPARAMS.fields_by_name[
        'params'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _MSGUPDATEPARAMS._options = None
    _MSGUPDATEPARAMS._serialized_options = (
        b'\202\347\260*\tauthority\212\347\260*!cosmos-sdk/x/bank/MsgUpdateParams'
    )
    _MSGSETSENDENABLED.fields_by_name['authority']._options = None
    _MSGSETSENDENABLED.fields_by_name[
        'authority'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _MSGSETSENDENABLED._options = None
    _MSGSETSENDENABLED._serialized_options = (
        b'\202\347\260*\tauthority\212\347\260*\034cosmos-sdk/MsgSetSendEnabled'
    )
    _MSG._options = None
    _MSG._serialized_options = b'\200\347\260*\001'
    _globals['_MSGSEND']._serialized_start = 211
    _globals['_MSGSEND']._serialized_end = 494
    _globals['_MSGSENDRESPONSE']._serialized_start = 496
    _globals['_MSGSENDRESPONSE']._serialized_end = 513
    _globals['_MSGMULTISEND']._serialized_start = 516
    _globals['_MSGMULTISEND']._serialized_end = 704
    _globals['_MSGMULTISENDRESPONSE']._serialized_start = 706
    _globals['_MSGMULTISENDRESPONSE']._serialized_end = 728
    _globals['_MSGUPDATEPARAMS']._serialized_start = 731
    _globals['_MSGUPDATEPARAMS']._serialized_end = 922
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 924
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 949
    _globals['_MSGSETSENDENABLED']._serialized_start = 952
    _globals['_MSGSETSENDENABLED']._serialized_end = 1185
    _globals['_MSGSETSENDENABLEDRESPONSE']._serialized_start = 1187
    _globals['_MSGSETSENDENABLEDRESPONSE']._serialized_end = 1214
    _globals['_MSG']._serialized_start = 1217
    _globals['_MSG']._serialized_end = 1602
# @@protoc_insertion_point(module_scope)