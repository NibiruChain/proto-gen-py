"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Lock(google.protobuf.message.Message):
    """Lock represents a users locked tokens for a period of time.
    It stores owner, duration, unlock time and the amount of coins locked.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    lock_id: builtins.int
    """unique autoincrementing numeric lock id"""
    owner: builtins.str
    """the user's address who owns the tokens that are locked"""
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """the duration that the lock is locked for"""
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """when the lock was unlocked"""
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """the coins locked in this Lock"""
    def __init__(
        self,
        *,
        lock_id: builtins.int = ...,
        owner: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
        end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration", "end_time", b"end_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coins", b"coins", "duration", b"duration", "end_time", b"end_time", "lock_id", b"lock_id", "owner", b"owner"]) -> None: ...

global___Lock = Lock
