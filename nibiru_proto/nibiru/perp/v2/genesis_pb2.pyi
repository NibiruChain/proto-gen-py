"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import nibiru.perp.v2.state_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the perp module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MARKETS_FIELD_NUMBER: builtins.int
    AMMS_FIELD_NUMBER: builtins.int
    POSITIONS_FIELD_NUMBER: builtins.int
    RESERVE_SNAPSHOTS_FIELD_NUMBER: builtins.int
    @property
    def markets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nibiru.perp.v2.state_pb2.Market]: ...
    @property
    def amms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nibiru.perp.v2.state_pb2.AMM]: ...
    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nibiru.perp.v2.state_pb2.Position]: ...
    @property
    def reserve_snapshots(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[nibiru.perp.v2.state_pb2.ReserveSnapshot]: ...
    def __init__(
        self,
        *,
        markets: collections.abc.Iterable[nibiru.perp.v2.state_pb2.Market] | None = ...,
        amms: collections.abc.Iterable[nibiru.perp.v2.state_pb2.AMM] | None = ...,
        positions: collections.abc.Iterable[nibiru.perp.v2.state_pb2.Position] | None = ...,
        reserve_snapshots: collections.abc.Iterable[nibiru.perp.v2.state_pb2.ReserveSnapshot] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amms", b"amms", "markets", b"markets", "positions", b"positions", "reserve_snapshots", b"reserve_snapshots"]) -> None: ...

global___GenesisState = GenesisState