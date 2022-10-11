"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CreatePoolProposal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    PAIR_FIELD_NUMBER: builtins.int
    TRADE_LIMIT_RATIO_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_RESERVE_FIELD_NUMBER: builtins.int
    BASE_ASSET_RESERVE_FIELD_NUMBER: builtins.int
    FLUCTUATION_LIMIT_RATIO_FIELD_NUMBER: builtins.int
    MAX_ORACLE_SPREAD_RATIO_FIELD_NUMBER: builtins.int
    MAINTENANCE_MARGIN_RATIO_FIELD_NUMBER: builtins.int
    MAX_LEVERAGE_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    pair: builtins.str
    """pair represents the pair of the vpool."""
    trade_limit_ratio: builtins.str
    """trade_limit_ratio represents the limit on trading amounts."""
    quote_asset_reserve: builtins.str
    """quote_asset_reserve is the amount of quote asset the pool will be initialized with."""
    base_asset_reserve: builtins.str
    """base_asset_reserve is the amount of base asset the pool will be initialized with."""
    fluctuation_limit_ratio: builtins.str
    """fluctuation_limit_ratio represents the maximum price
    percentage difference a trade can create on the pool.
    """
    max_oracle_spread_ratio: builtins.str
    """max_oracle_spread_ratio represents the maximum price percentage
    difference that can exist between oracle price and vpool prices after a trade.
    """
    maintenance_margin_ratio: builtins.str
    """maintenance_margin_ratio"""
    max_leverage: builtins.str
    """max_leverage"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        pair: builtins.str = ...,
        trade_limit_ratio: builtins.str = ...,
        quote_asset_reserve: builtins.str = ...,
        base_asset_reserve: builtins.str = ...,
        fluctuation_limit_ratio: builtins.str = ...,
        max_oracle_spread_ratio: builtins.str = ...,
        maintenance_margin_ratio: builtins.str = ...,
        max_leverage: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_asset_reserve", b"base_asset_reserve", "description", b"description", "fluctuation_limit_ratio", b"fluctuation_limit_ratio", "maintenance_margin_ratio", b"maintenance_margin_ratio", "max_leverage", b"max_leverage", "max_oracle_spread_ratio", b"max_oracle_spread_ratio", "pair", b"pair", "quote_asset_reserve", b"quote_asset_reserve", "title", b"title", "trade_limit_ratio", b"trade_limit_ratio"]) -> None: ...

global___CreatePoolProposal = CreatePoolProposal
