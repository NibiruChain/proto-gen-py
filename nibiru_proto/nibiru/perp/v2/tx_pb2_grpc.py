# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nibiru.perp.v2 import tx_pb2 as nibiru_dot_perp_dot_v2_dot_tx__pb2


class MsgStub(object):
    """Msg defines the x/perp Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RemoveMargin = channel.unary_unary(
                '/nibiru.perp.v2.Msg/RemoveMargin',
                request_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgRemoveMargin.SerializeToString,
                response_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgRemoveMarginResponse.FromString,
                )
        self.AddMargin = channel.unary_unary(
                '/nibiru.perp.v2.Msg/AddMargin',
                request_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgAddMargin.SerializeToString,
                response_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgAddMarginResponse.FromString,
                )
        self.MultiLiquidate = channel.unary_unary(
                '/nibiru.perp.v2.Msg/MultiLiquidate',
                request_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMultiLiquidate.SerializeToString,
                response_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMultiLiquidateResponse.FromString,
                )
        self.MarketOrder = channel.unary_unary(
                '/nibiru.perp.v2.Msg/MarketOrder',
                request_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMarketOrder.SerializeToString,
                response_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMarketOrderResponse.FromString,
                )
        self.ClosePosition = channel.unary_unary(
                '/nibiru.perp.v2.Msg/ClosePosition',
                request_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgClosePosition.SerializeToString,
                response_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgClosePositionResponse.FromString,
                )
        self.DonateToEcosystemFund = channel.unary_unary(
                '/nibiru.perp.v2.Msg/DonateToEcosystemFund',
                request_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgDonateToEcosystemFund.SerializeToString,
                response_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgDonateToEcosystemFundResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the x/perp Msg service.
    """

    def RemoveMargin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMargin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiLiquidate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClosePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DonateToEcosystemFund(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RemoveMargin': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveMargin,
                    request_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgRemoveMargin.FromString,
                    response_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgRemoveMarginResponse.SerializeToString,
            ),
            'AddMargin': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMargin,
                    request_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgAddMargin.FromString,
                    response_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgAddMarginResponse.SerializeToString,
            ),
            'MultiLiquidate': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiLiquidate,
                    request_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMultiLiquidate.FromString,
                    response_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMultiLiquidateResponse.SerializeToString,
            ),
            'MarketOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketOrder,
                    request_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMarketOrder.FromString,
                    response_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMarketOrderResponse.SerializeToString,
            ),
            'ClosePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.ClosePosition,
                    request_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgClosePosition.FromString,
                    response_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgClosePositionResponse.SerializeToString,
            ),
            'DonateToEcosystemFund': grpc.unary_unary_rpc_method_handler(
                    servicer.DonateToEcosystemFund,
                    request_deserializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgDonateToEcosystemFund.FromString,
                    response_serializer=nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgDonateToEcosystemFundResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nibiru.perp.v2.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the x/perp Msg service.
    """

    @staticmethod
    def RemoveMargin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.perp.v2.Msg/RemoveMargin',
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgRemoveMargin.SerializeToString,
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgRemoveMarginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMargin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.perp.v2.Msg/AddMargin',
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgAddMargin.SerializeToString,
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgAddMarginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiLiquidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.perp.v2.Msg/MultiLiquidate',
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMultiLiquidate.SerializeToString,
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMultiLiquidateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.perp.v2.Msg/MarketOrder',
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMarketOrder.SerializeToString,
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgMarketOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClosePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.perp.v2.Msg/ClosePosition',
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgClosePosition.SerializeToString,
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgClosePositionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DonateToEcosystemFund(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.perp.v2.Msg/DonateToEcosystemFund',
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgDonateToEcosystemFund.SerializeToString,
            nibiru_dot_perp_dot_v2_dot_tx__pb2.MsgDonateToEcosystemFundResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)