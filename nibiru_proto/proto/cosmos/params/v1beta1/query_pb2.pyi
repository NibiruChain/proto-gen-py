"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.params.v1beta1.params_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBSPACE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    subspace: typing.Text
    """subspace defines the module to query the parameter for."""

    key: typing.Text
    """key defines the key of the parameter in the subspace."""

    def __init__(self,
        *,
        subspace: typing.Text = ...,
        key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","subspace",b"subspace"]) -> None: ...
global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARAM_FIELD_NUMBER: builtins.int
    @property
    def param(self) -> cosmos.params.v1beta1.params_pb2.ParamChange:
        """param defines the queried parameter."""
        pass
    def __init__(self,
        *,
        param: typing.Optional[cosmos.params.v1beta1.params_pb2.ParamChange] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["param",b"param"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["param",b"param"]) -> None: ...
global___QueryParamsResponse = QueryParamsResponse