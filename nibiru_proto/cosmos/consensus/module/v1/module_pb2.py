# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/consensus/module/v1/module.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.app.v1alpha1 import (
    module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\'cosmos/consensus/module/v1/module.proto\x12\x1a\x63osmos.consensus.module.v1\x1a cosmos/app/v1alpha1/module.proto\"X\n\x06Module\x12\x1c\n\tauthority\x18\x01 \x01(\tR\tauthority:0\xba\xc0\x96\xda\x01*\n(github.com/cosmos/cosmos-sdk/x/consensusb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'cosmos.consensus.module.v1.module_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _MODULE._options = None
    _MODULE._serialized_options = (
        b'\272\300\226\332\001*\n(github.com/cosmos/cosmos-sdk/x/consensus'
    )
    _globals['_MODULE']._serialized_start = 105
    _globals['_MODULE']._serialized_end = 193
# @@protoc_insertion_point(module_scope)
