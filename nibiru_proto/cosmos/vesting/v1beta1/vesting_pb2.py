# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/vesting/v1beta1/vesting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from amino import amino_pb2 as amino_dot_amino__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16\x63osmos.vesting.v1beta1\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\"\x9b\x04\n\x12\x42\x61seVestingAccount\x12I\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01R\x0b\x62\x61seAccount\x12{\n\x10original_vesting\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x0foriginalVesting\x12w\n\x0e\x64\x65legated_free\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\rdelegatedFree\x12}\n\x11\x64\x65legated_vesting\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x10\x64\x65legatedVesting\x12\x19\n\x08\x65nd_time\x18\x05 \x01(\x03R\x07\x65ndTime:*\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x8a\xe7\xb0*\x1d\x63osmos-sdk/BaseVestingAccount\"\xcf\x01\n\x18\x43ontinuousVestingAccount\x12\x62\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01R\x12\x62\x61seVestingAccount\x12\x1d\n\nstart_time\x18\x02 \x01(\x03R\tstartTime:0\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x8a\xe7\xb0*#cosmos-sdk/ContinuousVestingAccount\"\xaa\x01\n\x15\x44\x65layedVestingAccount\x12\x62\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01R\x12\x62\x61seVestingAccount:-\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x8a\xe7\xb0* cosmos-sdk/DelayedVestingAccount\"\x90\x01\n\x06Period\x12\x16\n\x06length\x18\x01 \x01(\x03R\x06length\x12h\n\x06\x61mount\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x06\x61mount:\x04\x98\xa0\x1f\x00\"\x9f\x02\n\x16PeriodicVestingAccount\x12\x62\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01R\x12\x62\x61seVestingAccount\x12\x1d\n\nstart_time\x18\x02 \x01(\x03R\tstartTime\x12R\n\x0fvesting_periods\x18\x03 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0evestingPeriods:.\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x8a\xe7\xb0*!cosmos-sdk/PeriodicVestingAccount\"\xac\x01\n\x16PermanentLockedAccount\x12\x62\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01R\x12\x62\x61seVestingAccount:.\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x8a\xe7\xb0*!cosmos-sdk/PermanentLockedAccountB3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'cosmos.vesting.v1beta1.vesting_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
    )
    _BASEVESTINGACCOUNT.fields_by_name['base_account']._options = None
    _BASEVESTINGACCOUNT.fields_by_name[
        'base_account'
    ]._serialized_options = b'\320\336\037\001'
    _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._options = None
    _BASEVESTINGACCOUNT.fields_by_name[
        'original_vesting'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._options = None
    _BASEVESTINGACCOUNT.fields_by_name[
        'delegated_free'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._options = None
    _BASEVESTINGACCOUNT.fields_by_name[
        'delegated_vesting'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _BASEVESTINGACCOUNT._options = None
    _BASEVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\212\347\260*\035cosmos-sdk/BaseVestingAccount'
    _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
    _CONTINUOUSVESTINGACCOUNT.fields_by_name[
        'base_vesting_account'
    ]._serialized_options = b'\320\336\037\001'
    _CONTINUOUSVESTINGACCOUNT._options = None
    _CONTINUOUSVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\212\347\260*#cosmos-sdk/ContinuousVestingAccount'
    _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
    _DELAYEDVESTINGACCOUNT.fields_by_name[
        'base_vesting_account'
    ]._serialized_options = b'\320\336\037\001'
    _DELAYEDVESTINGACCOUNT._options = None
    _DELAYEDVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\212\347\260* cosmos-sdk/DelayedVestingAccount'
    _PERIOD.fields_by_name['amount']._options = None
    _PERIOD.fields_by_name[
        'amount'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _PERIOD._options = None
    _PERIOD._serialized_options = b'\230\240\037\000'
    _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
    _PERIODICVESTINGACCOUNT.fields_by_name[
        'base_vesting_account'
    ]._serialized_options = b'\320\336\037\001'
    _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
    _PERIODICVESTINGACCOUNT.fields_by_name[
        'vesting_periods'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _PERIODICVESTINGACCOUNT._options = None
    _PERIODICVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\212\347\260*!cosmos-sdk/PeriodicVestingAccount'
    _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._options = None
    _PERMANENTLOCKEDACCOUNT.fields_by_name[
        'base_vesting_account'
    ]._serialized_options = b'\320\336\037\001'
    _PERMANENTLOCKEDACCOUNT._options = None
    _PERMANENTLOCKEDACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\212\347\260*!cosmos-sdk/PermanentLockedAccount'
    _globals['_BASEVESTINGACCOUNT']._serialized_start = 170
    _globals['_BASEVESTINGACCOUNT']._serialized_end = 709
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_start = 712
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_end = 919
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_start = 922
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_end = 1092
    _globals['_PERIOD']._serialized_start = 1095
    _globals['_PERIOD']._serialized_end = 1239
    _globals['_PERIODICVESTINGACCOUNT']._serialized_start = 1242
    _globals['_PERIODICVESTINGACCOUNT']._serialized_end = 1529
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_start = 1532
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_end = 1704
# @@protoc_insertion_point(module_scope)
