"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Pairs(google.protobuf.message.Message):
    """Pairs defines a repeated slice of Pair objects."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIRS_FIELD_NUMBER: builtins.int
    @property
    def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Pair]: ...
    def __init__(self,
        *,
        pairs: typing.Optional[typing.Iterable[global___Pair]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pairs",b"pairs"]) -> None: ...
global___Pairs = Pairs

class Pair(google.protobuf.message.Message):
    """Pair defines a key/value bytes tuple."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    value: builtins.bytes
    def __init__(self,
        *,
        key: builtins.bytes = ...,
        value: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...
global___Pair = Pair