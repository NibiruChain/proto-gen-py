# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/module/v1/module.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/bank/module/v1/module.proto\x12\x15\x63osmos.bank.module.v1\x1a cosmos/app/v1alpha1/module.proto\"\x9c\x01\n\x06Module\x12G\n blocked_module_accounts_override\x18\x01 \x03(\tR\x1d\x62lockedModuleAccountsOverride\x12\x1c\n\tauthority\x18\x02 \x01(\tR\tauthority:+\xba\xc0\x96\xda\x01%\n#github.com/cosmos/cosmos-sdk/x/bankb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.module.v1.module_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODULE._options = None
  _MODULE._serialized_options = b'\272\300\226\332\001%\n#github.com/cosmos/cosmos-sdk/x/bank'
  _MODULE._serialized_start=96
  _MODULE._serialized_end=252
# @@protoc_insertion_point(module_scope)
