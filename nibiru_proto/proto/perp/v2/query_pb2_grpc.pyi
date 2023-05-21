"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import perp.v2.query_pb2

class QueryStub:
    """Query defines the gRPC querier service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    QueryPosition: grpc.UnaryUnaryMultiCallable[
        perp.v2.query_pb2.QueryPositionRequest,
        perp.v2.query_pb2.QueryPositionResponse,
    ]
    QueryPositions: grpc.UnaryUnaryMultiCallable[
        perp.v2.query_pb2.QueryPositionsRequest,
        perp.v2.query_pb2.QueryPositionsResponse,
    ]
    ModuleAccounts: grpc.UnaryUnaryMultiCallable[
        perp.v2.query_pb2.QueryModuleAccountsRequest,
        perp.v2.query_pb2.QueryModuleAccountsResponse,
    ]
    """Queries the reserve assets in a given pool, identified by a token pair."""
    QueryMarkets: grpc.UnaryUnaryMultiCallable[
        perp.v2.query_pb2.QueryMarketsRequest,
        perp.v2.query_pb2.QueryMarketsResponse,
    ]

class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""

    @abc.abstractmethod
    def QueryPosition(
        self,
        request: perp.v2.query_pb2.QueryPositionRequest,
        context: grpc.ServicerContext,
    ) -> perp.v2.query_pb2.QueryPositionResponse: ...
    @abc.abstractmethod
    def QueryPositions(
        self,
        request: perp.v2.query_pb2.QueryPositionsRequest,
        context: grpc.ServicerContext,
    ) -> perp.v2.query_pb2.QueryPositionsResponse: ...
    @abc.abstractmethod
    def ModuleAccounts(
        self,
        request: perp.v2.query_pb2.QueryModuleAccountsRequest,
        context: grpc.ServicerContext,
    ) -> perp.v2.query_pb2.QueryModuleAccountsResponse:
        """Queries the reserve assets in a given pool, identified by a token pair."""
    @abc.abstractmethod
    def QueryMarkets(
        self,
        request: perp.v2.query_pb2.QueryMarketsRequest,
        context: grpc.ServicerContext,
    ) -> perp.v2.query_pb2.QueryMarketsResponse: ...

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
