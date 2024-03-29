"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Module(google.protobuf.message.Message):
    """Module is the config object of the group module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_EXECUTION_PERIOD_FIELD_NUMBER: builtins.int
    MAX_METADATA_LEN_FIELD_NUMBER: builtins.int
    @property
    def max_execution_period(self) -> google.protobuf.duration_pb2.Duration:
        """max_execution_period defines the max duration after a proposal's voting period ends that members can send a MsgExec
        to execute the proposal.
        """
    max_metadata_len: builtins.int
    """max_metadata_len defines the max length of the metadata bytes field for various entities within the group module.
    Defaults to 255 if not explicitly set.
    """
    def __init__(
        self,
        *,
        max_execution_period: google.protobuf.duration_pb2.Duration | None = ...,
        max_metadata_len: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_execution_period", b"max_execution_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_execution_period", b"max_execution_period", "max_metadata_len", b"max_metadata_len"]) -> None: ...

global___Module = Module
