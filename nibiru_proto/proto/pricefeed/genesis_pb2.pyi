"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pricefeed.state_pb2
import typing
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
        pass
    @property
    def posted_prices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pricefeed.state_pb2.PostedPrice]: ...
    @property
    def genesis_oracles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        params: typing.Optional[pricefeed.state_pb2.Params] = ...,
        posted_prices: typing.Optional[typing.Iterable[pricefeed.state_pb2.PostedPrice]] = ...,
        genesis_oracles: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["genesis_oracles",b"genesis_oracles","params",b"params","posted_prices",b"posted_prices"]) -> None: ...
global___GenesisState = GenesisState
