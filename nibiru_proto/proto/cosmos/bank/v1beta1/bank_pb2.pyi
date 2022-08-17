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

class Params(google.protobuf.message.Message):
    """Params defines the parameters for the bank module."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SEND_ENABLED_FIELD_NUMBER: builtins.int
    DEFAULT_SEND_ENABLED_FIELD_NUMBER: builtins.int
    @property
    def send_enabled(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SendEnabled]: ...
    default_send_enabled: builtins.bool
    def __init__(self,
        *,
        send_enabled: typing.Optional[typing.Iterable[global___SendEnabled]] = ...,
        default_send_enabled: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_send_enabled",b"default_send_enabled","send_enabled",b"send_enabled"]) -> None: ...
global___Params = Params

class SendEnabled(google.protobuf.message.Message):
    """SendEnabled maps coin denom to a send_enabled status (whether a denom is
    sendable).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DENOM_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    denom: typing.Text
    enabled: builtins.bool
    def __init__(self,
        *,
        denom: typing.Text = ...,
        enabled: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom",b"denom","enabled",b"enabled"]) -> None: ...
global___SendEnabled = SendEnabled

class Input(google.protobuf.message.Message):
    """Input models transaction input."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    address: typing.Text
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        address: typing.Text = ...,
        coins: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","coins",b"coins"]) -> None: ...
global___Input = Input

class Output(google.protobuf.message.Message):
    """Output models transaction outputs."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    address: typing.Text
    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        address: typing.Text = ...,
        coins: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","coins",b"coins"]) -> None: ...
global___Output = Output

class Supply(google.protobuf.message.Message):
    """Supply represents a struct that passively keeps track of the total supply
    amounts in the network.
    This message is deprecated now that supply is indexed by denom.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOTAL_FIELD_NUMBER: builtins.int
    @property
    def total(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(self,
        *,
        total: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["total",b"total"]) -> None: ...
global___Supply = Supply

class DenomUnit(google.protobuf.message.Message):
    """DenomUnit represents a struct that describes a given
    denomination unit of the basic token.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DENOM_FIELD_NUMBER: builtins.int
    EXPONENT_FIELD_NUMBER: builtins.int
    ALIASES_FIELD_NUMBER: builtins.int
    denom: typing.Text
    """denom represents the string name of the given denom unit (e.g uatom)."""

    exponent: builtins.int
    """exponent represents power of 10 exponent that one must
    raise the base_denom to in order to equal the given DenomUnit's denom
    1 denom = 1^exponent base_denom
    (e.g. with a base_denom of uatom, one can create a DenomUnit of 'atom' with
    exponent = 6, thus: 1 atom = 10^6 uatom).
    """

    @property
    def aliases(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """aliases is a list of string aliases for the given denom"""
        pass
    def __init__(self,
        *,
        denom: typing.Text = ...,
        exponent: builtins.int = ...,
        aliases: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aliases",b"aliases","denom",b"denom","exponent",b"exponent"]) -> None: ...
global___DenomUnit = DenomUnit

class Metadata(google.protobuf.message.Message):
    """Metadata represents a struct that describes
    a basic token.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DENOM_UNITS_FIELD_NUMBER: builtins.int
    BASE_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SYMBOL_FIELD_NUMBER: builtins.int
    description: typing.Text
    @property
    def denom_units(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DenomUnit]:
        """denom_units represents the list of DenomUnit's for a given coin"""
        pass
    base: typing.Text
    """base represents the base denom (should be the DenomUnit with exponent = 0)."""

    display: typing.Text
    """display indicates the suggested denom that should be
    displayed in clients.
    """

    name: typing.Text
    """name defines the name of the token (eg: Cosmos Atom)

    Since: cosmos-sdk 0.43
    """

    symbol: typing.Text
    """symbol is the token symbol usually shown on exchanges (eg: ATOM). This can
    be the same as the display.

    Since: cosmos-sdk 0.43
    """

    def __init__(self,
        *,
        description: typing.Text = ...,
        denom_units: typing.Optional[typing.Iterable[global___DenomUnit]] = ...,
        base: typing.Text = ...,
        display: typing.Text = ...,
        name: typing.Text = ...,
        symbol: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","denom_units",b"denom_units","description",b"description","display",b"display","name",b"name","symbol",b"symbol"]) -> None: ...
global___Metadata = Metadata