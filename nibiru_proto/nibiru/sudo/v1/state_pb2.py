# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/sudo/v1/state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1anibiru/sudo/v1/state.proto\x12\x0enibiru.sudo.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\"A\n\x07Sudoers\x12\x12\n\x04root\x18\x01 \x01(\tR\x04root\x12\x1c\n\tcontracts\x18\x02 \x03(\tR\tcontracts:\x04\x98\xa0\x1f\x00\"G\n\x0cGenesisState\x12\x37\n\x07sudoers\x18\x01 \x01(\x0b\x32\x17.nibiru.sudo.v1.SudoersB\x04\xc8\xde\x1f\x00R\x07sudoersB)Z\'github.com/NibiruChain/nibiru/x/sudo/pbb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'nibiru.sudo.v1.state_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\'github.com/NibiruChain/nibiru/x/sudo/pb'
    _SUDOERS._options = None
    _SUDOERS._serialized_options = b'\230\240\037\000'
    _GENESISSTATE.fields_by_name['sudoers']._options = None
    _GENESISSTATE.fields_by_name['sudoers']._serialized_options = b'\310\336\037\000'
    _globals['_SUDOERS']._serialized_start = 98
    _globals['_SUDOERS']._serialized_end = 163
    _globals['_GENESISSTATE']._serialized_start = 165
    _globals['_GENESISSTATE']._serialized_end = 236
# @@protoc_insertion_point(module_scope)