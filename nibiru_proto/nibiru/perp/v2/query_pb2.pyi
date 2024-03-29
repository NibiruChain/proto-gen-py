"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import nibiru.perp.v2.state_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class QueryPositionsRequest(google.protobuf.message.Message):
    """---------------------------------------- Positions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRADER_FIELD_NUMBER: builtins.int
    trader: builtins.str
    def __init__(
        self,
        *,
        trader: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["trader", b"trader"]) -> None: ...

global___QueryPositionsRequest = QueryPositionsRequest

@typing_extensions.final
class QueryPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITIONS_FIELD_NUMBER: builtins.int
    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QueryPositionResponse]: ...
    def __init__(
        self,
        *,
        positions: collections.abc.Iterable[global___QueryPositionResponse] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["positions", b"positions"]) -> None: ...

global___QueryPositionsResponse = QueryPositionsResponse

@typing_extensions.final
class QueryPositionRequest(google.protobuf.message.Message):
    """---------------------------------------- Position

    QueryPositionRequest is the request type for the position of the x/perp
    module account.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_FIELD_NUMBER: builtins.int
    TRADER_FIELD_NUMBER: builtins.int
    pair: builtins.str
    trader: builtins.str
    def __init__(
        self,
        *,
        pair: builtins.str = ...,
        trader: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair", b"pair", "trader", b"trader"]) -> None: ...

global___QueryPositionRequest = QueryPositionRequest

@typing_extensions.final
class QueryPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_FIELD_NUMBER: builtins.int
    POSITION_NOTIONAL_FIELD_NUMBER: builtins.int
    UNREALIZED_PNL_FIELD_NUMBER: builtins.int
    MARGIN_RATIO_FIELD_NUMBER: builtins.int
    @property
    def position(self) -> nibiru.perp.v2.state_pb2.Position:
        """The position as it exists in the blockchain state"""
    position_notional: builtins.str
    """The position's current notional value, if it were to be entirely closed (in
    margin units).
    """
    unrealized_pnl: builtins.str
    """The position's unrealized PnL."""
    margin_ratio: builtins.str
    """margin ratio of the position based on the spot price"""
    def __init__(
        self,
        *,
        position: nibiru.perp.v2.state_pb2.Position | None = ...,
        position_notional: builtins.str = ...,
        unrealized_pnl: builtins.str = ...,
        margin_ratio: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["margin_ratio", b"margin_ratio", "position", b"position", "position_notional", b"position_notional", "unrealized_pnl", b"unrealized_pnl"]) -> None: ...

global___QueryPositionResponse = QueryPositionResponse

@typing_extensions.final
class QueryModuleAccountsRequest(google.protobuf.message.Message):
    """---------------------------------------- QueryModuleAccounts"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryModuleAccountsRequest = QueryModuleAccountsRequest

@typing_extensions.final
class QueryModuleAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AccountWithBalance]: ...
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[global___AccountWithBalance] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts"]) -> None: ...

global___QueryModuleAccountsResponse = QueryModuleAccountsResponse

@typing_extensions.final
class AccountWithBalance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    name: builtins.str
    address: builtins.str
    @property
    def balance(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        address: builtins.str = ...,
        balance: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "balance", b"balance", "name", b"name"]) -> None: ...

global___AccountWithBalance = AccountWithBalance

@typing_extensions.final
class AmmMarket(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MARKET_FIELD_NUMBER: builtins.int
    AMM_FIELD_NUMBER: builtins.int
    @property
    def market(self) -> nibiru.perp.v2.state_pb2.Market: ...
    @property
    def amm(self) -> nibiru.perp.v2.state_pb2.AMM: ...
    def __init__(
        self,
        *,
        market: nibiru.perp.v2.state_pb2.Market | None = ...,
        amm: nibiru.perp.v2.state_pb2.AMM | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["amm", b"amm", "market", b"market"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["amm", b"amm", "market", b"market"]) -> None: ...

global___AmmMarket = AmmMarket

@typing_extensions.final
class QueryMarketsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryMarketsRequest = QueryMarketsRequest

@typing_extensions.final
class QueryMarketsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMM_MARKETS_FIELD_NUMBER: builtins.int
    @property
    def amm_markets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AmmMarket]: ...
    def __init__(
        self,
        *,
        amm_markets: collections.abc.Iterable[global___AmmMarket] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amm_markets", b"amm_markets"]) -> None: ...

global___QueryMarketsResponse = QueryMarketsResponse
