# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/inflation/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from nibiru.inflation.v1 import (
    inflation_pb2 as nibiru_dot_inflation_dot_v1_dot_inflation__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n!nibiru/inflation/v1/genesis.proto\x12\x13nibiru.inflation.v1\x1a\x14gogoproto/gogo.proto\x1a#nibiru/inflation/v1/inflation.proto\"\x88\x01\n\x0cGenesisState\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32\x1b.nibiru.inflation.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12\x16\n\x06period\x18\x02 \x01(\x04R\x06period\x12%\n\x0eskipped_epochs\x18\x03 \x01(\x04R\rskippedEpochs\"\xb6\x02\n\x06Params\x12+\n\x11inflation_enabled\x18\x01 \x01(\x08R\x10inflationEnabled\x12j\n\x17\x65xponential_calculation\x18\x02 \x01(\x0b\x32+.nibiru.inflation.v1.ExponentialCalculationB\x04\xc8\xde\x1f\x00R\x16\x65xponentialCalculation\x12g\n\x16inflation_distribution\x18\x03 \x01(\x0b\x32*.nibiru.inflation.v1.InflationDistributionB\x04\xc8\xde\x1f\x00R\x15inflationDistribution\x12*\n\x11\x65pochs_per_period\x18\x04 \x01(\x04R\x0f\x65pochsPerPeriodB1Z/github.com/NibiruChain/nibiru/x/inflation/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'nibiru.inflation.v1.genesis_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b'Z/github.com/NibiruChain/nibiru/x/inflation/types'
    )
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
    _PARAMS.fields_by_name['exponential_calculation']._options = None
    _PARAMS.fields_by_name[
        'exponential_calculation'
    ]._serialized_options = b'\310\336\037\000'
    _PARAMS.fields_by_name['inflation_distribution']._options = None
    _PARAMS.fields_by_name[
        'inflation_distribution'
    ]._serialized_options = b'\310\336\037\000'
    _globals['_GENESISSTATE']._serialized_start = 118
    _globals['_GENESISSTATE']._serialized_end = 254
    _globals['_PARAMS']._serialized_start = 257
    _globals['_PARAMS']._serialized_end = 567
# @@protoc_insertion_point(module_scope)
