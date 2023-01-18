"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import oracle.v1beta1.query_pb2

class QueryStub:
    """Query defines the gRPC querier service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    ExchangeRate: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryExchangeRateRequest,
        oracle.v1beta1.query_pb2.QueryExchangeRateResponse,
    ]
    """ExchangeRate returns exchange rate of a pair"""
    ExchangeRateTwap: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryExchangeRateRequest,
        oracle.v1beta1.query_pb2.QueryExchangeRateResponse,
    ]
    """ExchangeRateTwap returns exchange rate of a pair"""
    ExchangeRates: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryExchangeRatesRequest,
        oracle.v1beta1.query_pb2.QueryExchangeRatesResponse,
    ]
    """ExchangeRates returns exchange rates of all pairs"""
    Actives: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryActivesRequest,
        oracle.v1beta1.query_pb2.QueryActivesResponse,
    ]
    """Actives returns all active pairs"""
    VoteTargets: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryVoteTargetsRequest,
        oracle.v1beta1.query_pb2.QueryVoteTargetsResponse,
    ]
    """VoteTargets returns all vote target for pairs"""
    FeederDelegation: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryFeederDelegationRequest,
        oracle.v1beta1.query_pb2.QueryFeederDelegationResponse,
    ]
    """FeederDelegation returns feeder delegation of a validator"""
    MissCounter: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryMissCounterRequest,
        oracle.v1beta1.query_pb2.QueryMissCounterResponse,
    ]
    """MissCounter returns oracle miss counter of a validator"""
    AggregatePrevote: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryAggregatePrevoteRequest,
        oracle.v1beta1.query_pb2.QueryAggregatePrevoteResponse,
    ]
    """AggregatePrevote returns an aggregate prevote of a validator"""
    AggregatePrevotes: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryAggregatePrevotesRequest,
        oracle.v1beta1.query_pb2.QueryAggregatePrevotesResponse,
    ]
    """AggregatePrevotes returns aggregate prevotes of all validators"""
    AggregateVote: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryAggregateVoteRequest,
        oracle.v1beta1.query_pb2.QueryAggregateVoteResponse,
    ]
    """AggregateVote returns an aggregate vote of a validator"""
    AggregateVotes: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryAggregateVotesRequest,
        oracle.v1beta1.query_pb2.QueryAggregateVotesResponse,
    ]
    """AggregateVotes returns aggregate votes of all validators"""
    Params: grpc.UnaryUnaryMultiCallable[
        oracle.v1beta1.query_pb2.QueryParamsRequest,
        oracle.v1beta1.query_pb2.QueryParamsResponse,
    ]
    """Params queries all parameters."""

class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""

    @abc.abstractmethod
    def ExchangeRate(
        self,
        request: oracle.v1beta1.query_pb2.QueryExchangeRateRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryExchangeRateResponse:
        """ExchangeRate returns exchange rate of a pair"""
    @abc.abstractmethod
    def ExchangeRateTwap(
        self,
        request: oracle.v1beta1.query_pb2.QueryExchangeRateRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryExchangeRateResponse:
        """ExchangeRateTwap returns exchange rate of a pair"""
    @abc.abstractmethod
    def ExchangeRates(
        self,
        request: oracle.v1beta1.query_pb2.QueryExchangeRatesRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryExchangeRatesResponse:
        """ExchangeRates returns exchange rates of all pairs"""
    @abc.abstractmethod
    def Actives(
        self,
        request: oracle.v1beta1.query_pb2.QueryActivesRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryActivesResponse:
        """Actives returns all active pairs"""
    @abc.abstractmethod
    def VoteTargets(
        self,
        request: oracle.v1beta1.query_pb2.QueryVoteTargetsRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryVoteTargetsResponse:
        """VoteTargets returns all vote target for pairs"""
    @abc.abstractmethod
    def FeederDelegation(
        self,
        request: oracle.v1beta1.query_pb2.QueryFeederDelegationRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryFeederDelegationResponse:
        """FeederDelegation returns feeder delegation of a validator"""
    @abc.abstractmethod
    def MissCounter(
        self,
        request: oracle.v1beta1.query_pb2.QueryMissCounterRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryMissCounterResponse:
        """MissCounter returns oracle miss counter of a validator"""
    @abc.abstractmethod
    def AggregatePrevote(
        self,
        request: oracle.v1beta1.query_pb2.QueryAggregatePrevoteRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryAggregatePrevoteResponse:
        """AggregatePrevote returns an aggregate prevote of a validator"""
    @abc.abstractmethod
    def AggregatePrevotes(
        self,
        request: oracle.v1beta1.query_pb2.QueryAggregatePrevotesRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryAggregatePrevotesResponse:
        """AggregatePrevotes returns aggregate prevotes of all validators"""
    @abc.abstractmethod
    def AggregateVote(
        self,
        request: oracle.v1beta1.query_pb2.QueryAggregateVoteRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryAggregateVoteResponse:
        """AggregateVote returns an aggregate vote of a validator"""
    @abc.abstractmethod
    def AggregateVotes(
        self,
        request: oracle.v1beta1.query_pb2.QueryAggregateVotesRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryAggregateVotesResponse:
        """AggregateVotes returns aggregate votes of all validators"""
    @abc.abstractmethod
    def Params(
        self,
        request: oracle.v1beta1.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> oracle.v1beta1.query_pb2.QueryParamsResponse:
        """Params queries all parameters."""

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
