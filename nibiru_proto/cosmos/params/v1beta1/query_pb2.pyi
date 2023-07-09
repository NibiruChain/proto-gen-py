"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.params.v1beta1.params_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSPACE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    subspace: builtins.str
    """subspace defines the module to query the parameter for."""
    key: builtins.str
    """key defines the key of the parameter in the subspace."""
    def __init__(
        self,
        *,
        subspace: builtins.str = ...,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "subspace", b"subspace"]) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

@typing_extensions.final
class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAM_FIELD_NUMBER: builtins.int
    @property
    def param(self) -> cosmos.params.v1beta1.params_pb2.ParamChange:
        """param defines the queried parameter."""
    def __init__(
        self,
        *,
        param: cosmos.params.v1beta1.params_pb2.ParamChange | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["param", b"param"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["param", b"param"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

@typing_extensions.final
class QuerySubspacesRequest(google.protobuf.message.Message):
    """QuerySubspacesRequest defines a request type for querying for all registered
    subspaces and all keys for a subspace.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QuerySubspacesRequest = QuerySubspacesRequest

@typing_extensions.final
class QuerySubspacesResponse(google.protobuf.message.Message):
    """QuerySubspacesResponse defines the response types for querying for all
    registered subspaces and all keys for a subspace.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSPACES_FIELD_NUMBER: builtins.int
    @property
    def subspaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Subspace]: ...
    def __init__(
        self,
        *,
        subspaces: collections.abc.Iterable[global___Subspace] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subspaces", b"subspaces"]) -> None: ...

global___QuerySubspacesResponse = QuerySubspacesResponse

@typing_extensions.final
class Subspace(google.protobuf.message.Message):
    """Subspace defines a parameter subspace name and all the keys that exist for
    the subspace.

    Since: cosmos-sdk 0.46
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSPACE_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    subspace: builtins.str
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        subspace: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys", b"keys", "subspace", b"subspace"]) -> None: ...

global___Subspace = Subspace
