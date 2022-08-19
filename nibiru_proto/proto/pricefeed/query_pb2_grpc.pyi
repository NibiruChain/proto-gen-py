"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import pricefeed.query_pb2

class QueryStub:
    """Query defines the gRPC querier service for pricefeed module"""
    def __init__(self, channel: grpc.Channel) -> None: ...
    QueryParams: grpc.UnaryUnaryMultiCallable[
        pricefeed.query_pb2.QueryParamsRequest,
        pricefeed.query_pb2.QueryParamsResponse]
    """QueryParams queries all parameters of the pricefeed module."""

    QueryPrice: grpc.UnaryUnaryMultiCallable[
        pricefeed.query_pb2.QueryPriceRequest,
        pricefeed.query_pb2.QueryPriceResponse]
    """QueryPrice queries price details for a pair"""

    QueryPrices: grpc.UnaryUnaryMultiCallable[
        pricefeed.query_pb2.QueryPricesRequest,
        pricefeed.query_pb2.QueryPricesResponse]
    """QueryPrices queries all prices"""

    QueryRawPrices: grpc.UnaryUnaryMultiCallable[
        pricefeed.query_pb2.QueryRawPricesRequest,
        pricefeed.query_pb2.QueryRawPricesResponse]
    """QueryRawPrices queries all raw prices for an asset pair"""

    QueryOracles: grpc.UnaryUnaryMultiCallable[
        pricefeed.query_pb2.QueryOraclesRequest,
        pricefeed.query_pb2.QueryOraclesResponse]
    """QueryOracles queries all oracles for an asset pair"""

    QueryMarkets: grpc.UnaryUnaryMultiCallable[
        pricefeed.query_pb2.QueryMarketsRequest,
        pricefeed.query_pb2.QueryMarketsResponse]
    """QueryMarkets queries all markets"""


class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service for pricefeed module"""
    @abc.abstractmethod
    def QueryParams(self,
        request: pricefeed.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> pricefeed.query_pb2.QueryParamsResponse:
        """QueryParams queries all parameters of the pricefeed module."""
        pass

    @abc.abstractmethod
    def QueryPrice(self,
        request: pricefeed.query_pb2.QueryPriceRequest,
        context: grpc.ServicerContext,
    ) -> pricefeed.query_pb2.QueryPriceResponse:
        """QueryPrice queries price details for a pair"""
        pass

    @abc.abstractmethod
    def QueryPrices(self,
        request: pricefeed.query_pb2.QueryPricesRequest,
        context: grpc.ServicerContext,
    ) -> pricefeed.query_pb2.QueryPricesResponse:
        """QueryPrices queries all prices"""
        pass

    @abc.abstractmethod
    def QueryRawPrices(self,
        request: pricefeed.query_pb2.QueryRawPricesRequest,
        context: grpc.ServicerContext,
    ) -> pricefeed.query_pb2.QueryRawPricesResponse:
        """QueryRawPrices queries all raw prices for an asset pair"""
        pass

    @abc.abstractmethod
    def QueryOracles(self,
        request: pricefeed.query_pb2.QueryOraclesRequest,
        context: grpc.ServicerContext,
    ) -> pricefeed.query_pb2.QueryOraclesResponse:
        """QueryOracles queries all oracles for an asset pair"""
        pass

    @abc.abstractmethod
    def QueryMarkets(self,
        request: pricefeed.query_pb2.QueryMarketsRequest,
        context: grpc.ServicerContext,
    ) -> pricefeed.query_pb2.QueryMarketsResponse:
        """QueryMarkets queries all markets"""
        pass


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
