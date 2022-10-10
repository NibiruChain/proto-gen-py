"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import perp.v1.state_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the perp module's genesis state."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARAMS_FIELD_NUMBER: builtins.int
    PAIR_METADATA_FIELD_NUMBER: builtins.int
    POSITIONS_FIELD_NUMBER: builtins.int
    PREPAID_BAD_DEBTS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> perp.v1.state_pb2.Params: ...
    @property
    def pair_metadata(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[perp.v1.state_pb2.PairMetadata]: ...
    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[perp.v1.state_pb2.Position]: ...
    @property
    def prepaid_bad_debts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[perp.v1.state_pb2.PrepaidBadDebt]: ...
    def __init__(self,
        *,
        params: typing.Optional[perp.v1.state_pb2.Params] = ...,
        pair_metadata: typing.Optional[typing.Iterable[perp.v1.state_pb2.PairMetadata]] = ...,
        positions: typing.Optional[typing.Iterable[perp.v1.state_pb2.Position]] = ...,
        prepaid_bad_debts: typing.Optional[typing.Iterable[perp.v1.state_pb2.PrepaidBadDebt]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair_metadata",b"pair_metadata","params",b"params","positions",b"positions","prepaid_bad_debts",b"prepaid_bad_debts"]) -> None: ...
global___GenesisState = GenesisState
