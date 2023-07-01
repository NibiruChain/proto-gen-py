# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/oracle/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from nibiru.oracle.v1 import oracle_pb2 as nibiru_dot_oracle_dot_v1_dot_oracle__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1enibiru/oracle/v1/genesis.proto\x12\x10nibiru.oracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x1dnibiru/oracle/v1/oracle.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xd2\x05\n\x0cGenesisState\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32\x18.nibiru.oracle.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12W\n\x12\x66\x65\x65\x64\x65r_delegations\x18\x02 \x03(\x0b\x32\".nibiru.oracle.v1.FeederDelegationB\x04\xc8\xde\x1f\x00R\x11\x66\x65\x65\x64\x65rDelegations\x12\x66\n\x0e\x65xchange_rates\x18\x03 \x03(\x0b\x32#.nibiru.oracle.v1.ExchangeRateTupleB\x1a\xc8\xde\x1f\x00\xaa\xdf\x1f\x12\x45xchangeRateTuplesR\rexchangeRates\x12H\n\rmiss_counters\x18\x04 \x03(\x0b\x32\x1d.nibiru.oracle.v1.MissCounterB\x04\xc8\xde\x1f\x00R\x0cmissCounters\x12}\n aggregate_exchange_rate_prevotes\x18\x05 \x03(\x0b\x32..nibiru.oracle.v1.AggregateExchangeRatePrevoteB\x04\xc8\xde\x1f\x00R\x1d\x61ggregateExchangeRatePrevotes\x12t\n\x1d\x61ggregate_exchange_rate_votes\x18\x06 \x03(\x0b\x32+.nibiru.oracle.v1.AggregateExchangeRateVoteB\x04\xc8\xde\x1f\x00R\x1a\x61ggregateExchangeRateVotes\x12O\n\x05pairs\x18\x07 \x03(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x31github.com/NibiruChain/nibiru/x/common/asset.PairR\x05pairs\x12\x39\n\x07rewards\x18\x08 \x03(\x0b\x32\x19.nibiru.oracle.v1.RewardsB\x04\xc8\xde\x1f\x00R\x07rewards\"f\n\x10\x46\x65\x65\x64\x65rDelegation\x12%\n\x0e\x66\x65\x65\x64\x65r_address\x18\x01 \x01(\tR\rfeederAddress\x12+\n\x11validator_address\x18\x02 \x01(\tR\x10validatorAddress\"]\n\x0bMissCounter\x12+\n\x11validator_address\x18\x01 \x01(\tR\x10validatorAddress\x12!\n\x0cmiss_counter\x18\x02 \x01(\x04R\x0bmissCounterB.Z,github.com/NibiruChain/nibiru/x/oracle/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'nibiru.oracle.v1.genesis_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/oracle/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
    _GENESISSTATE.fields_by_name['feeder_delegations']._options = None
    _GENESISSTATE.fields_by_name[
        'feeder_delegations'
    ]._serialized_options = b'\310\336\037\000'
    _GENESISSTATE.fields_by_name['exchange_rates']._options = None
    _GENESISSTATE.fields_by_name[
        'exchange_rates'
    ]._serialized_options = b'\310\336\037\000\252\337\037\022ExchangeRateTuples'
    _GENESISSTATE.fields_by_name['miss_counters']._options = None
    _GENESISSTATE.fields_by_name[
        'miss_counters'
    ]._serialized_options = b'\310\336\037\000'
    _GENESISSTATE.fields_by_name['aggregate_exchange_rate_prevotes']._options = None
    _GENESISSTATE.fields_by_name[
        'aggregate_exchange_rate_prevotes'
    ]._serialized_options = b'\310\336\037\000'
    _GENESISSTATE.fields_by_name['aggregate_exchange_rate_votes']._options = None
    _GENESISSTATE.fields_by_name[
        'aggregate_exchange_rate_votes'
    ]._serialized_options = b'\310\336\037\000'
    _GENESISSTATE.fields_by_name['pairs']._options = None
    _GENESISSTATE.fields_by_name[
        'pairs'
    ]._serialized_options = b'\310\336\037\000\332\336\0371github.com/NibiruChain/nibiru/x/common/asset.Pair'
    _GENESISSTATE.fields_by_name['rewards']._options = None
    _GENESISSTATE.fields_by_name['rewards']._serialized_options = b'\310\336\037\000'
    _globals['_GENESISSTATE']._serialized_start = 138
    _globals['_GENESISSTATE']._serialized_end = 860
    _globals['_FEEDERDELEGATION']._serialized_start = 862
    _globals['_FEEDERDELEGATION']._serialized_end = 964
    _globals['_MISSCOUNTER']._serialized_start = 966
    _globals['_MISSCOUNTER']._serialized_end = 1059
# @@protoc_insertion_point(module_scope)
