"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PositionChangedEvent(google.protobuf.message.Message):
    """Emitted when a position changes.
    TODO: Is there a way to split this into different events without creating too much complexity?
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    TRADER_ADDRESS_FIELD_NUMBER: builtins.int
    MARGIN_FIELD_NUMBER: builtins.int
    POSITION_NOTIONAL_FIELD_NUMBER: builtins.int
    EXCHANGED_POSITION_SIZE_FIELD_NUMBER: builtins.int
    TRANSACTION_FEE_FIELD_NUMBER: builtins.int
    POSITION_SIZE_FIELD_NUMBER: builtins.int
    REALIZED_PNL_FIELD_NUMBER: builtins.int
    UNREALIZED_PNL_AFTER_FIELD_NUMBER: builtins.int
    BAD_DEBT_FIELD_NUMBER: builtins.int
    LIQUIDATION_PENALTY_FIELD_NUMBER: builtins.int
    MARK_PRICE_FIELD_NUMBER: builtins.int
    FUNDING_PAYMENT_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    BLOCK_TIME_MS_FIELD_NUMBER: builtins.int
    pair: typing.Text
    """identifier of the corresponding virtual pool for the position"""

    trader_address: typing.Text
    """owner of the position."""

    @property
    def margin(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """amount of margin backing the position."""
        pass
    position_notional: typing.Text
    """margin * leverage * vPrice. 'notional' is the virtual size times the virtual price on 'vpool'."""

    exchanged_position_size: typing.Text
    """magnitude of the change to vsize. The vsize is the amount of base assets for the position, margin * leverage * priceBasePerQuote."""

    @property
    def transaction_fee(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """transaction fee paid"""
        pass
    position_size: typing.Text
    """position virtual size after the change"""

    realized_pnl: typing.Text
    """realize profits and losses after the change"""

    unrealized_pnl_after: typing.Text
    """unrealized profits and losses after the change"""

    @property
    def bad_debt(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Amount of bad debt cleared by the PerpEF during the change. 
        Bad debt is negative net margin past the liquidation point of a position.
        """
        pass
    liquidation_penalty: typing.Text
    """amt of margin (y) lost due to liquidation"""

    mark_price: typing.Text
    """Mark price, synonymous with mark price in this context, is the quotient of
    the quote reserves and base reserves
    """

    funding_payment: typing.Text
    """A funding payment made or received by the trader on the current position. 
    'fundingPayment' is positive if 'owner' is the sender and negative if 'owner'
    is the receiver of the payment. Its magnitude is abs(vSize * fundingRate). 
    Funding payments act to converge the mark price (vPrice) and index price 
    (average price on major exchanges).
    """

    block_height: builtins.int
    """The block number at which this position was changed."""

    block_time_ms: builtins.int
    """The block time in unix milliseconds at which this position was changed."""

    def __init__(self,
        *,
        pair: typing.Text = ...,
        trader_address: typing.Text = ...,
        margin: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        position_notional: typing.Text = ...,
        exchanged_position_size: typing.Text = ...,
        transaction_fee: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        position_size: typing.Text = ...,
        realized_pnl: typing.Text = ...,
        unrealized_pnl_after: typing.Text = ...,
        bad_debt: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        liquidation_penalty: typing.Text = ...,
        mark_price: typing.Text = ...,
        funding_payment: typing.Text = ...,
        block_height: builtins.int = ...,
        block_time_ms: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bad_debt",b"bad_debt","margin",b"margin","transaction_fee",b"transaction_fee"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bad_debt",b"bad_debt","block_height",b"block_height","block_time_ms",b"block_time_ms","exchanged_position_size",b"exchanged_position_size","funding_payment",b"funding_payment","liquidation_penalty",b"liquidation_penalty","margin",b"margin","mark_price",b"mark_price","pair",b"pair","position_notional",b"position_notional","position_size",b"position_size","realized_pnl",b"realized_pnl","trader_address",b"trader_address","transaction_fee",b"transaction_fee","unrealized_pnl_after",b"unrealized_pnl_after"]) -> None: ...
global___PositionChangedEvent = PositionChangedEvent

class PositionLiquidatedEvent(google.protobuf.message.Message):
    """Emitted when a position is liquidated."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    TRADER_ADDRESS_FIELD_NUMBER: builtins.int
    EXCHANGED_QUOTE_AMOUNT_FIELD_NUMBER: builtins.int
    EXCHANGED_POSITION_SIZE_FIELD_NUMBER: builtins.int
    LIQUIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    FEE_TO_LIQUIDATOR_FIELD_NUMBER: builtins.int
    FEE_TO_ECOSYSTEM_FUND_FIELD_NUMBER: builtins.int
    BAD_DEBT_FIELD_NUMBER: builtins.int
    MARGIN_FIELD_NUMBER: builtins.int
    POSITION_NOTIONAL_FIELD_NUMBER: builtins.int
    POSITION_SIZE_FIELD_NUMBER: builtins.int
    UNREALIZEDPNL_FIELD_NUMBER: builtins.int
    MARK_PRICE_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    BLOCK_TIME_MS_FIELD_NUMBER: builtins.int
    pair: typing.Text
    """identifier of the corresponding virtual pool for the position"""

    trader_address: typing.Text
    """owner of the position."""

    exchanged_quote_amount: typing.Text
    """margin * leverage * vPrice. 'notional' is the virtual size times  the virtual price on 'vpool'."""

    exchanged_position_size: typing.Text
    """virtual amount of base assets for the position, which would be margin * leverage * priceBasePerQuote."""

    liquidator_address: typing.Text
    """Address of the account that executed the tx."""

    @property
    def fee_to_liquidator(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Commission (in margin units) received by 'liquidator'."""
        pass
    @property
    def fee_to_ecosystem_fund(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Commission (in margin units) given to the ecosystem fund."""
        pass
    @property
    def bad_debt(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """ Bad debt (margin units) cleared by the PerpEF during the tx. Bad debt is negative net margin past the liquidation point of a position."""
        pass
    @property
    def margin(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Remaining margin in the position after liquidation"""
        pass
    position_notional: typing.Text
    """Remaining position notional in the position after liquidation"""

    position_size: typing.Text
    """Remaining position size in the position after liquidation"""

    unrealizedPnl: typing.Text
    """Unrealized PnL in the position after liquidation"""

    mark_price: typing.Text
    """Spot price of the vAMM after liquidation"""

    block_height: builtins.int
    """The block number at which this liquidation occured."""

    block_time_ms: builtins.int
    """The unix timestamp in milliseconds at which this liquidation occured."""

    def __init__(self,
        *,
        pair: typing.Text = ...,
        trader_address: typing.Text = ...,
        exchanged_quote_amount: typing.Text = ...,
        exchanged_position_size: typing.Text = ...,
        liquidator_address: typing.Text = ...,
        fee_to_liquidator: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        fee_to_ecosystem_fund: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        bad_debt: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        margin: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        position_notional: typing.Text = ...,
        position_size: typing.Text = ...,
        unrealizedPnl: typing.Text = ...,
        mark_price: typing.Text = ...,
        block_height: builtins.int = ...,
        block_time_ms: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bad_debt",b"bad_debt","fee_to_ecosystem_fund",b"fee_to_ecosystem_fund","fee_to_liquidator",b"fee_to_liquidator","margin",b"margin"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bad_debt",b"bad_debt","block_height",b"block_height","block_time_ms",b"block_time_ms","exchanged_position_size",b"exchanged_position_size","exchanged_quote_amount",b"exchanged_quote_amount","fee_to_ecosystem_fund",b"fee_to_ecosystem_fund","fee_to_liquidator",b"fee_to_liquidator","liquidator_address",b"liquidator_address","margin",b"margin","mark_price",b"mark_price","pair",b"pair","position_notional",b"position_notional","position_size",b"position_size","trader_address",b"trader_address","unrealizedPnl",b"unrealizedPnl"]) -> None: ...
global___PositionLiquidatedEvent = PositionLiquidatedEvent

class PositionSettledEvent(google.protobuf.message.Message):
    """Emitted when a position is settled."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    TRADER_ADDRESS_FIELD_NUMBER: builtins.int
    SETTLED_COINS_FIELD_NUMBER: builtins.int
    pair: typing.Text
    """Identifier for the virtual pool of the position."""

    trader_address: typing.Text
    """Owner of the position."""

    @property
    def settled_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """Settled coin as dictated by the settlement price of the vpool."""
        pass
    def __init__(self,
        *,
        pair: typing.Text = ...,
        trader_address: typing.Text = ...,
        settled_coins: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair",b"pair","settled_coins",b"settled_coins","trader_address",b"trader_address"]) -> None: ...
global___PositionSettledEvent = PositionSettledEvent

class FundingRateChangedEvent(google.protobuf.message.Message):
    """Emitted when a new funding rate is calculated."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    MARK_PRICE_FIELD_NUMBER: builtins.int
    INDEX_PRICE_FIELD_NUMBER: builtins.int
    LATEST_FUNDING_RATE_FIELD_NUMBER: builtins.int
    LATEST_PREMIUM_FRACTION_FIELD_NUMBER: builtins.int
    CUMULATIVE_PREMIUM_FRACTION_FIELD_NUMBER: builtins.int
    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    BLOCK_TIME_MS_FIELD_NUMBER: builtins.int
    pair: typing.Text
    """The pair for which the funding rate was calculated."""

    mark_price: typing.Text
    """The mark price of the pair."""

    index_price: typing.Text
    """The oracle index price of the pair."""

    latest_funding_rate: typing.Text
    """The latest funding rate."""

    latest_premium_fraction: typing.Text
    """The latest premium fraction just calculated."""

    cumulative_premium_fraction: typing.Text
    """The latest cumulative premium fraction.
    The funding payment a position will pay is the difference between this value
    and the latest cumulative premium fraction on the position, multiplied by the position size.
    """

    block_height: builtins.int
    """The block number at which the funding rate was calculated."""

    block_time_ms: builtins.int
    """The block time in unix milliseconds at which the funding rate was calculated."""

    def __init__(self,
        *,
        pair: typing.Text = ...,
        mark_price: typing.Text = ...,
        index_price: typing.Text = ...,
        latest_funding_rate: typing.Text = ...,
        latest_premium_fraction: typing.Text = ...,
        cumulative_premium_fraction: typing.Text = ...,
        block_height: builtins.int = ...,
        block_time_ms: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height",b"block_height","block_time_ms",b"block_time_ms","cumulative_premium_fraction",b"cumulative_premium_fraction","index_price",b"index_price","latest_funding_rate",b"latest_funding_rate","latest_premium_fraction",b"latest_premium_fraction","mark_price",b"mark_price","pair",b"pair"]) -> None: ...
global___FundingRateChangedEvent = FundingRateChangedEvent
