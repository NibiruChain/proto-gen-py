"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.distribution.v1beta1.query_pb2
import grpc

class QueryStub:
    """Query defines the gRPC querier service for distribution module."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Params: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryParamsRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryParamsResponse]
    """Params queries params of the distribution module."""

    ValidatorOutstandingRewards: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsResponse]
    """ValidatorOutstandingRewards queries rewards of a validator address."""

    ValidatorCommission: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionResponse]
    """ValidatorCommission queries accumulated commission for a validator."""

    ValidatorSlashes: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesResponse]
    """ValidatorSlashes queries slash events of a validator."""

    DelegationRewards: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsResponse]
    """DelegationRewards queries the total rewards accrued by a delegation."""

    DelegationTotalRewards: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsResponse]
    """DelegationTotalRewards queries the total rewards accrued by a each
    validator.
    """

    DelegatorValidators: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsResponse]
    """DelegatorValidators queries the validators of a delegator."""

    DelegatorWithdrawAddress: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressResponse]
    """DelegatorWithdrawAddress queries withdraw address of a delegator."""

    CommunityPool: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolRequest,
        cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolResponse]
    """CommunityPool queries the community pool coins."""


class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service for distribution module."""
    @abc.abstractmethod
    def Params(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryParamsResponse:
        """Params queries params of the distribution module."""
        pass

    @abc.abstractmethod
    def ValidatorOutstandingRewards(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsResponse:
        """ValidatorOutstandingRewards queries rewards of a validator address."""
        pass

    @abc.abstractmethod
    def ValidatorCommission(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionResponse:
        """ValidatorCommission queries accumulated commission for a validator."""
        pass

    @abc.abstractmethod
    def ValidatorSlashes(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesResponse:
        """ValidatorSlashes queries slash events of a validator."""
        pass

    @abc.abstractmethod
    def DelegationRewards(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsResponse:
        """DelegationRewards queries the total rewards accrued by a delegation."""
        pass

    @abc.abstractmethod
    def DelegationTotalRewards(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsResponse:
        """DelegationTotalRewards queries the total rewards accrued by a each
        validator.
        """
        pass

    @abc.abstractmethod
    def DelegatorValidators(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsResponse:
        """DelegatorValidators queries the validators of a delegator."""
        pass

    @abc.abstractmethod
    def DelegatorWithdrawAddress(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressResponse:
        """DelegatorWithdrawAddress queries withdraw address of a delegator."""
        pass

    @abc.abstractmethod
    def CommunityPool(self,
        request: cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolResponse:
        """CommunityPool queries the community pool coins."""
        pass


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
