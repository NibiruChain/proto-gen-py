"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.47"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import tendermint.types.params_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MsgUpdateParams(google.protobuf.message.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHORITY_FIELD_NUMBER: builtins.int
    BLOCK_FIELD_NUMBER: builtins.int
    EVIDENCE_FIELD_NUMBER: builtins.int
    VALIDATOR_FIELD_NUMBER: builtins.int
    authority: builtins.str
    """authority is the address that controls the module (defaults to x/gov unless overwritten)."""
    @property
    def block(self) -> tendermint.types.params_pb2.BlockParams:
        """params defines the x/consensus parameters to update.
        VersionsParams is not included in this Msg because it is tracked
        separarately in x/upgrade.

        NOTE: All parameters must be supplied.
        """
    @property
    def evidence(self) -> tendermint.types.params_pb2.EvidenceParams: ...
    @property
    def validator(self) -> tendermint.types.params_pb2.ValidatorParams: ...
    def __init__(
        self,
        *,
        authority: builtins.str = ...,
        block: tendermint.types.params_pb2.BlockParams | None = ...,
        evidence: tendermint.types.params_pb2.EvidenceParams | None = ...,
        validator: tendermint.types.params_pb2.ValidatorParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block", b"block", "evidence", b"evidence", "validator", b"validator"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authority", b"authority", "block", b"block", "evidence", b"evidence", "validator", b"validator"]) -> None: ...

global___MsgUpdateParams = MsgUpdateParams

@typing_extensions.final
class MsgUpdateParamsResponse(google.protobuf.message.Message):
    """MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgUpdateParamsResponse = MsgUpdateParamsResponse
