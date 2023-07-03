# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nibiru.oracle.v1 import query_pb2 as nibiru_dot_oracle_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExchangeRate = channel.unary_unary(
                '/nibiru.oracle.v1.Query/ExchangeRate',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateResponse.FromString,
                )
        self.ExchangeRateTwap = channel.unary_unary(
                '/nibiru.oracle.v1.Query/ExchangeRateTwap',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateResponse.FromString,
                )
        self.ExchangeRates = channel.unary_unary(
                '/nibiru.oracle.v1.Query/ExchangeRates',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRatesRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRatesResponse.FromString,
                )
        self.Actives = channel.unary_unary(
                '/nibiru.oracle.v1.Query/Actives',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryActivesRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryActivesResponse.FromString,
                )
        self.VoteTargets = channel.unary_unary(
                '/nibiru.oracle.v1.Query/VoteTargets',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryVoteTargetsRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryVoteTargetsResponse.FromString,
                )
        self.FeederDelegation = channel.unary_unary(
                '/nibiru.oracle.v1.Query/FeederDelegation',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryFeederDelegationRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryFeederDelegationResponse.FromString,
                )
        self.MissCounter = channel.unary_unary(
                '/nibiru.oracle.v1.Query/MissCounter',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryMissCounterRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryMissCounterResponse.FromString,
                )
        self.AggregatePrevote = channel.unary_unary(
                '/nibiru.oracle.v1.Query/AggregatePrevote',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevoteRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevoteResponse.FromString,
                )
        self.AggregatePrevotes = channel.unary_unary(
                '/nibiru.oracle.v1.Query/AggregatePrevotes',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevotesRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevotesResponse.FromString,
                )
        self.AggregateVote = channel.unary_unary(
                '/nibiru.oracle.v1.Query/AggregateVote',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVoteRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVoteResponse.FromString,
                )
        self.AggregateVotes = channel.unary_unary(
                '/nibiru.oracle.v1.Query/AggregateVotes',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVotesRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVotesResponse.FromString,
                )
        self.Params = channel.unary_unary(
                '/nibiru.oracle.v1.Query/Params',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def ExchangeRate(self, request, context):
        """ExchangeRate returns exchange rate of a pair
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExchangeRateTwap(self, request, context):
        """ExchangeRateTwap returns twap exchange rate of a pair
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExchangeRates(self, request, context):
        """ExchangeRates returns exchange rates of all pairs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Actives(self, request, context):
        """Actives returns all active pairs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteTargets(self, request, context):
        """VoteTargets returns all vote target for pairs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FeederDelegation(self, request, context):
        """FeederDelegation returns feeder delegation of a validator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MissCounter(self, request, context):
        """MissCounter returns oracle miss counter of a validator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregatePrevote(self, request, context):
        """AggregatePrevote returns an aggregate prevote of a validator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregatePrevotes(self, request, context):
        """AggregatePrevotes returns aggregate prevotes of all validators
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregateVote(self, request, context):
        """AggregateVote returns an aggregate vote of a validator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregateVotes(self, request, context):
        """AggregateVotes returns aggregate votes of all validators
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries all parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExchangeRate': grpc.unary_unary_rpc_method_handler(
                    servicer.ExchangeRate,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateResponse.SerializeToString,
            ),
            'ExchangeRateTwap': grpc.unary_unary_rpc_method_handler(
                    servicer.ExchangeRateTwap,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateResponse.SerializeToString,
            ),
            'ExchangeRates': grpc.unary_unary_rpc_method_handler(
                    servicer.ExchangeRates,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRatesRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRatesResponse.SerializeToString,
            ),
            'Actives': grpc.unary_unary_rpc_method_handler(
                    servicer.Actives,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryActivesRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryActivesResponse.SerializeToString,
            ),
            'VoteTargets': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteTargets,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryVoteTargetsRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryVoteTargetsResponse.SerializeToString,
            ),
            'FeederDelegation': grpc.unary_unary_rpc_method_handler(
                    servicer.FeederDelegation,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryFeederDelegationRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryFeederDelegationResponse.SerializeToString,
            ),
            'MissCounter': grpc.unary_unary_rpc_method_handler(
                    servicer.MissCounter,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryMissCounterRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryMissCounterResponse.SerializeToString,
            ),
            'AggregatePrevote': grpc.unary_unary_rpc_method_handler(
                    servicer.AggregatePrevote,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevoteRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevoteResponse.SerializeToString,
            ),
            'AggregatePrevotes': grpc.unary_unary_rpc_method_handler(
                    servicer.AggregatePrevotes,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevotesRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevotesResponse.SerializeToString,
            ),
            'AggregateVote': grpc.unary_unary_rpc_method_handler(
                    servicer.AggregateVote,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVoteRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVoteResponse.SerializeToString,
            ),
            'AggregateVotes': grpc.unary_unary_rpc_method_handler(
                    servicer.AggregateVotes,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVotesRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVotesResponse.SerializeToString,
            ),
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nibiru.oracle.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def ExchangeRate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/ExchangeRate',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExchangeRateTwap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/ExchangeRateTwap',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExchangeRates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/ExchangeRates',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRatesRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryExchangeRatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Actives(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/Actives',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryActivesRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryActivesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteTargets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/VoteTargets',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryVoteTargetsRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryVoteTargetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FeederDelegation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/FeederDelegation',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryFeederDelegationRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryFeederDelegationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MissCounter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/MissCounter',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryMissCounterRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryMissCounterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregatePrevote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/AggregatePrevote',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevoteRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregatePrevotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/AggregatePrevotes',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevotesRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregatePrevotesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregateVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/AggregateVote',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVoteRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregateVotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/AggregateVotes',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVotesRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryAggregateVotesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Query/Params',
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)