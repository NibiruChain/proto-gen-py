# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nibiru.oracle.v1 import tx_pb2 as nibiru_dot_oracle_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the oracle Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AggregateExchangeRatePrevote = channel.unary_unary(
                '/nibiru.oracle.v1.Msg/AggregateExchangeRatePrevote',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRatePrevote.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRatePrevoteResponse.FromString,
                )
        self.AggregateExchangeRateVote = channel.unary_unary(
                '/nibiru.oracle.v1.Msg/AggregateExchangeRateVote',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRateVote.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRateVoteResponse.FromString,
                )
        self.DelegateFeedConsent = channel.unary_unary(
                '/nibiru.oracle.v1.Msg/DelegateFeedConsent',
                request_serializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgDelegateFeedConsent.SerializeToString,
                response_deserializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgDelegateFeedConsentResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the oracle Msg service.
    """

    def AggregateExchangeRatePrevote(self, request, context):
        """AggregateExchangeRatePrevote defines a method for submitting
        aggregate exchange rate prevote
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AggregateExchangeRateVote(self, request, context):
        """AggregateExchangeRateVote defines a method for submitting
        aggregate exchange rate vote
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegateFeedConsent(self, request, context):
        """DelegateFeedConsent defines a method for delegating oracle voting rights
        to another address known as a price feeder.
        See https://github.com/NibiruChain/pricefeeder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AggregateExchangeRatePrevote': grpc.unary_unary_rpc_method_handler(
                    servicer.AggregateExchangeRatePrevote,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRatePrevote.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRatePrevoteResponse.SerializeToString,
            ),
            'AggregateExchangeRateVote': grpc.unary_unary_rpc_method_handler(
                    servicer.AggregateExchangeRateVote,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRateVote.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRateVoteResponse.SerializeToString,
            ),
            'DelegateFeedConsent': grpc.unary_unary_rpc_method_handler(
                    servicer.DelegateFeedConsent,
                    request_deserializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgDelegateFeedConsent.FromString,
                    response_serializer=nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgDelegateFeedConsentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nibiru.oracle.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the oracle Msg service.
    """

    @staticmethod
    def AggregateExchangeRatePrevote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Msg/AggregateExchangeRatePrevote',
            nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRatePrevote.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRatePrevoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AggregateExchangeRateVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Msg/AggregateExchangeRateVote',
            nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRateVote.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgAggregateExchangeRateVoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegateFeedConsent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.oracle.v1.Msg/DelegateFeedConsent',
            nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgDelegateFeedConsent.SerializeToString,
            nibiru_dot_oracle_dot_v1_dot_tx__pb2.MsgDelegateFeedConsentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
