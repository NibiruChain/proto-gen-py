"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PublicKey(google.protobuf.message.Message):
    """PublicKey defines the keys available for use with Validators"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ED25519_FIELD_NUMBER: builtins.int
    SECP256K1_FIELD_NUMBER: builtins.int
    ed25519: builtins.bytes
    secp256k1: builtins.bytes
    def __init__(
        self,
        *,
        ed25519: builtins.bytes = ...,
        secp256k1: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ed25519", b"ed25519", "secp256k1", b"secp256k1", "sum", b"sum"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ed25519", b"ed25519", "secp256k1", b"secp256k1", "sum", b"sum"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["sum", b"sum"]) -> typing_extensions.Literal["ed25519", "secp256k1"] | None: ...

global___PublicKey = PublicKey
