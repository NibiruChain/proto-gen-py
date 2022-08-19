"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.crisis.v1beta1.tx_pb2
import grpc

class MsgStub:
    """Msg defines the bank Msg service."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    VerifyInvariant: grpc.UnaryUnaryMultiCallable[
        cosmos.crisis.v1beta1.tx_pb2.MsgVerifyInvariant,
        cosmos.crisis.v1beta1.tx_pb2.MsgVerifyInvariantResponse]
    """VerifyInvariant defines a method to verify a particular invariance."""


class MsgServicer(metaclass=abc.ABCMeta):
    """Msg defines the bank Msg service."""
    @abc.abstractmethod
    def VerifyInvariant(self,
        request: cosmos.crisis.v1beta1.tx_pb2.MsgVerifyInvariant,
        context: grpc.ServicerContext,
    ) -> cosmos.crisis.v1beta1.tx_pb2.MsgVerifyInvariantResponse:
        """VerifyInvariant defines a method to verify a particular invariance."""
        pass


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
