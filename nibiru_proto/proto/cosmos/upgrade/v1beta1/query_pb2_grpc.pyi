"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.upgrade.v1beta1.query_pb2
import grpc

class QueryStub:
    """Query defines the gRPC upgrade querier service."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    CurrentPlan: grpc.UnaryUnaryMultiCallable[
        cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanRequest,
        cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanResponse]
    """CurrentPlan queries the current upgrade plan."""

    AppliedPlan: grpc.UnaryUnaryMultiCallable[
        cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanRequest,
        cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanResponse]
    """AppliedPlan queries a previously applied upgrade plan by its name."""

    UpgradedConsensusState: grpc.UnaryUnaryMultiCallable[
        cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateRequest,
        cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateResponse]
    """UpgradedConsensusState queries the consensus state that will serve
    as a trusted kernel for the next version of this chain. It will only be
    stored at the last height of this chain.
    UpgradedConsensusState RPC not supported with legacy querier
    This rpc is deprecated now that IBC has its own replacement
    (https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)
    """

    ModuleVersions: grpc.UnaryUnaryMultiCallable[
        cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsRequest,
        cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsResponse]
    """ModuleVersions queries the list of module versions from state.

    Since: cosmos-sdk 0.43
    """


class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC upgrade querier service."""
    @abc.abstractmethod
    def CurrentPlan(self,
        request: cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanResponse:
        """CurrentPlan queries the current upgrade plan."""
        pass

    @abc.abstractmethod
    def AppliedPlan(self,
        request: cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanResponse:
        """AppliedPlan queries a previously applied upgrade plan by its name."""
        pass

    @abc.abstractmethod
    def UpgradedConsensusState(self,
        request: cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateResponse:
        """UpgradedConsensusState queries the consensus state that will serve
        as a trusted kernel for the next version of this chain. It will only be
        stored at the last height of this chain.
        UpgradedConsensusState RPC not supported with legacy querier
        This rpc is deprecated now that IBC has its own replacement
        (https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)
        """
        pass

    @abc.abstractmethod
    def ModuleVersions(self,
        request: cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsResponse:
        """ModuleVersions queries the list of module versions from state.

        Since: cosmos-sdk 0.43
        """
        pass


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
