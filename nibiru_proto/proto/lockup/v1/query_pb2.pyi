"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import lockup.v1.lock_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryLockedCoinsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    address: typing.Text
    def __init__(self,
        *,
        address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address"]) -> None: ...
global___QueryLockedCoinsRequest = QueryLockedCoinsRequest

class QueryLockedCoinsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCKED_COINS_FIELD_NUMBER: builtins.int
    @property
    def locked_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        locked_coins: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locked_coins",b"locked_coins"]) -> None: ...
global___QueryLockedCoinsResponse = QueryLockedCoinsResponse

class QueryLockRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.int
    def __init__(self,
        *,
        id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___QueryLockRequest = QueryLockRequest

class QueryLockResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCK_FIELD_NUMBER: builtins.int
    @property
    def lock(self) -> lockup.v1.lock_pb2.Lock: ...
    def __init__(self,
        *,
        lock: typing.Optional[lockup.v1.lock_pb2.Lock] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lock",b"lock"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["lock",b"lock"]) -> None: ...
global___QueryLockResponse = QueryLockResponse

class QueryLocksByAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    address: typing.Text
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(self,
        *,
        address: typing.Text = ...,
        pagination: typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","pagination",b"pagination"]) -> None: ...
global___QueryLocksByAddress = QueryLocksByAddress

class QueryLocksByAddressResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCKS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[lockup.v1.lock_pb2.Lock]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(self,
        *,
        locks: typing.Optional[typing.Iterable[lockup.v1.lock_pb2.Lock]] = ...,
        pagination: typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks",b"locks","pagination",b"pagination"]) -> None: ...
global___QueryLocksByAddressResponse = QueryLocksByAddressResponse