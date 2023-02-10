"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import oracle.v1beta1.tx_pb2

class MsgStub:
    """Msg defines the oracle Msg service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    AggregateExchangeRatePrevote: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.tx_pb2.MsgAggregateExchangeRatePrevote,
        oracle.v1beta1.tx_pb2.MsgAggregateExchangeRatePrevoteResponse,
    ]
    """AggregateExchangeRatePrevote defines a method for submitting
    aggregate exchange rate prevote
    """
    AggregateExchangeRateVote: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.tx_pb2.MsgAggregateExchangeRateVote,
        oracle.v1beta1.tx_pb2.MsgAggregateExchangeRateVoteResponse,
    ]
    """AggregateExchangeRateVote defines a method for submitting
    aggregate exchange rate vote
    """
    DelegateFeedConsent: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.tx_pb2.MsgDelegateFeedConsent,
        oracle.v1beta1.tx_pb2.MsgDelegateFeedConsentResponse,
    ]
    """DelegateFeedConsent defines a method for delegating oracle voting rights 
    to another address known as a price feeder. 
    See https://github.com/NibiruChain/pricefeeder.
    """

class MsgServicer(metaclass=abc.ABCMeta):
    """Msg defines the oracle Msg service."""

    @abc.abstractmethod
    def AggregateExchangeRatePrevote(
        self,
        request: oracle.v1beta1.tx_pb2.MsgAggregateExchangeRatePrevote,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.tx_pb2.MsgAggregateExchangeRatePrevoteResponse:
        """AggregateExchangeRatePrevote defines a method for submitting
        aggregate exchange rate prevote
        """
    @abc.abstractmethod
    def AggregateExchangeRateVote(
        self,
        request: oracle.v1beta1.tx_pb2.MsgAggregateExchangeRateVote,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.tx_pb2.MsgAggregateExchangeRateVoteResponse:
        """AggregateExchangeRateVote defines a method for submitting
        aggregate exchange rate vote
        """
    @abc.abstractmethod
    def DelegateFeedConsent(
        self,
        request: oracle.v1beta1.tx_pb2.MsgDelegateFeedConsent,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.tx_pb2.MsgDelegateFeedConsentResponse:
        """DelegateFeedConsent defines a method for delegating oracle voting rights 
        to another address known as a price feeder. 
        See https://github.com/NibiruChain/pricefeeder.
        """

def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
