"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Equivocation(google.protobuf.message.Message):
    """Equivocation implements the Evidence interface and defines evidence of double
    signing misbehavior.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    POWER_FIELD_NUMBER: builtins.int
    CONSENSUS_ADDRESS_FIELD_NUMBER: builtins.int
    height: builtins.int
    """height is the equivocation height."""
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """time is the equivocation time."""
    power: builtins.int
    """power is the equivocation validator power."""
    consensus_address: builtins.str
    """consensus_address is the equivocation validator consensus address."""
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        power: builtins.int = ...,
        consensus_address: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time", b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consensus_address", b"consensus_address", "height", b"height", "power", b"power", "time", b"time"]) -> None: ...

global___Equivocation = Equivocation
