# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inflation/v1/inflation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cinflation/v1/inflation.proto\x12\x13nibiru.inflation.v1\x1a\x14gogoproto/gogo.proto\"\xf4\x01\n\x15InflationDistribution\x12G\n\x0fstaking_rewards\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x46\n\x0e\x63ommunity_pool\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12J\n\x12strategic_reserves\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xc9\x01\n\x16\x45xponentialCalculation\x12\x39\n\x01\x61\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x39\n\x01r\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x39\n\x01\x63\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x31Z/github.com/NibiruChain/nibiru/x/inflation/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inflation.v1.inflation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/NibiruChain/nibiru/x/inflation/types'
  _INFLATIONDISTRIBUTION.fields_by_name['staking_rewards']._options = None
  _INFLATIONDISTRIBUTION.fields_by_name['staking_rewards']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _INFLATIONDISTRIBUTION.fields_by_name['community_pool']._options = None
  _INFLATIONDISTRIBUTION.fields_by_name['community_pool']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _INFLATIONDISTRIBUTION.fields_by_name['strategic_reserves']._options = None
  _INFLATIONDISTRIBUTION.fields_by_name['strategic_reserves']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EXPONENTIALCALCULATION.fields_by_name['a']._options = None
  _EXPONENTIALCALCULATION.fields_by_name['a']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EXPONENTIALCALCULATION.fields_by_name['r']._options = None
  _EXPONENTIALCALCULATION.fields_by_name['r']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EXPONENTIALCALCULATION.fields_by_name['c']._options = None
  _EXPONENTIALCALCULATION.fields_by_name['c']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _INFLATIONDISTRIBUTION._serialized_start=76
  _INFLATIONDISTRIBUTION._serialized_end=320
  _EXPONENTIALCALCULATION._serialized_start=323
  _EXPONENTIALCALCULATION._serialized_end=524
# @@protoc_insertion_point(module_scope)
