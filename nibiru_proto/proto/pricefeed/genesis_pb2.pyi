"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pricefeed.state_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the pricefeed module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    POSTED_PRICES_FIELD_NUMBER: builtins.int
    GENESIS_ORACLES_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> pricefeed.state_pb2.Params:
        """params defines all the paramaters of the module."""
    @property
    def posted_prices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pricefeed.state_pb2.PostedPrice]: ...
    @property
    def genesis_oracles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        params: pricefeed.state_pb2.Params | None = ...,
        posted_prices: collections.abc.Iterable[pricefeed.state_pb2.PostedPrice] | None = ...,
        genesis_oracles: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["genesis_oracles", b"genesis_oracles", "params", b"params", "posted_prices", b"posted_prices"]) -> None: ...

global___GenesisState = GenesisState
