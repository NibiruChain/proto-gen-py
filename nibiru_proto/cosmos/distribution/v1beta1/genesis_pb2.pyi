"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import cosmos.distribution.v1beta1.distribution_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DelegatorWithdrawInfo(google.protobuf.message.Message):
    """DelegatorWithdrawInfo is the address for where distributions rewards are
    withdrawn to by default this struct is only used at genesis to feed in
    default withdraw addresses.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    WITHDRAW_ADDRESS_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    """delegator_address is the address of the delegator."""
    withdraw_address: builtins.str
    """withdraw_address is the address to withdraw the delegation rewards to."""
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
        withdraw_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_address", b"delegator_address", "withdraw_address", b"withdraw_address"]) -> None: ...

global___DelegatorWithdrawInfo = DelegatorWithdrawInfo

@typing_extensions.final
class ValidatorOutstandingRewardsRecord(google.protobuf.message.Message):
    """ValidatorOutstandingRewardsRecord is used for import/export via genesis json."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    OUTSTANDING_REWARDS_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    """validator_address is the address of the validator."""
    @property
    def outstanding_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]:
        """outstanding_rewards represents the oustanding rewards of a validator."""
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        outstanding_rewards: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["outstanding_rewards", b"outstanding_rewards", "validator_address", b"validator_address"]) -> None: ...

global___ValidatorOutstandingRewardsRecord = ValidatorOutstandingRewardsRecord

@typing_extensions.final
class ValidatorAccumulatedCommissionRecord(google.protobuf.message.Message):
    """ValidatorAccumulatedCommissionRecord is used for import / export via genesis
    json.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    ACCUMULATED_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    """validator_address is the address of the validator."""
    @property
    def accumulated(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorAccumulatedCommission:
        """accumulated is the accumulated commission of a validator."""
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        accumulated: cosmos.distribution.v1beta1.distribution_pb2.ValidatorAccumulatedCommission | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["accumulated", b"accumulated"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accumulated", b"accumulated", "validator_address", b"validator_address"]) -> None: ...

global___ValidatorAccumulatedCommissionRecord = ValidatorAccumulatedCommissionRecord

@typing_extensions.final
class ValidatorHistoricalRewardsRecord(google.protobuf.message.Message):
    """ValidatorHistoricalRewardsRecord is used for import / export via genesis
    json.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    REWARDS_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    """validator_address is the address of the validator."""
    period: builtins.int
    """period defines the period the historical rewards apply to."""
    @property
    def rewards(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorHistoricalRewards:
        """rewards defines the historical rewards of a validator."""
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        period: builtins.int = ...,
        rewards: cosmos.distribution.v1beta1.distribution_pb2.ValidatorHistoricalRewards | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rewards", b"rewards"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["period", b"period", "rewards", b"rewards", "validator_address", b"validator_address"]) -> None: ...

global___ValidatorHistoricalRewardsRecord = ValidatorHistoricalRewardsRecord

@typing_extensions.final
class ValidatorCurrentRewardsRecord(google.protobuf.message.Message):
    """ValidatorCurrentRewardsRecord is used for import / export via genesis json."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    REWARDS_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    """validator_address is the address of the validator."""
    @property
    def rewards(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorCurrentRewards:
        """rewards defines the current rewards of a validator."""
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        rewards: cosmos.distribution.v1beta1.distribution_pb2.ValidatorCurrentRewards | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rewards", b"rewards"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["rewards", b"rewards", "validator_address", b"validator_address"]) -> None: ...

global___ValidatorCurrentRewardsRecord = ValidatorCurrentRewardsRecord

@typing_extensions.final
class DelegatorStartingInfoRecord(google.protobuf.message.Message):
    """DelegatorStartingInfoRecord used for import / export via genesis json."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    STARTING_INFO_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    """delegator_address is the address of the delegator."""
    validator_address: builtins.str
    """validator_address is the address of the validator."""
    @property
    def starting_info(self) -> cosmos.distribution.v1beta1.distribution_pb2.DelegatorStartingInfo:
        """starting_info defines the starting info of a delegator."""
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
        validator_address: builtins.str = ...,
        starting_info: cosmos.distribution.v1beta1.distribution_pb2.DelegatorStartingInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["starting_info", b"starting_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_address", b"delegator_address", "starting_info", b"starting_info", "validator_address", b"validator_address"]) -> None: ...

global___DelegatorStartingInfoRecord = DelegatorStartingInfoRecord

@typing_extensions.final
class ValidatorSlashEventRecord(google.protobuf.message.Message):
    """ValidatorSlashEventRecord is used for import / export via genesis json."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    VALIDATOR_SLASH_EVENT_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    """validator_address is the address of the validator."""
    height: builtins.int
    """height defines the block height at which the slash event occured."""
    period: builtins.int
    """period is the period of the slash event."""
    @property
    def validator_slash_event(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorSlashEvent:
        """validator_slash_event describes the slash event."""
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        height: builtins.int = ...,
        period: builtins.int = ...,
        validator_slash_event: cosmos.distribution.v1beta1.distribution_pb2.ValidatorSlashEvent | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["validator_slash_event", b"validator_slash_event"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "period", b"period", "validator_address", b"validator_address", "validator_slash_event", b"validator_slash_event"]) -> None: ...

global___ValidatorSlashEventRecord = ValidatorSlashEventRecord

@typing_extensions.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the distribution module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    FEE_POOL_FIELD_NUMBER: builtins.int
    DELEGATOR_WITHDRAW_INFOS_FIELD_NUMBER: builtins.int
    PREVIOUS_PROPOSER_FIELD_NUMBER: builtins.int
    OUTSTANDING_REWARDS_FIELD_NUMBER: builtins.int
    VALIDATOR_ACCUMULATED_COMMISSIONS_FIELD_NUMBER: builtins.int
    VALIDATOR_HISTORICAL_REWARDS_FIELD_NUMBER: builtins.int
    VALIDATOR_CURRENT_REWARDS_FIELD_NUMBER: builtins.int
    DELEGATOR_STARTING_INFOS_FIELD_NUMBER: builtins.int
    VALIDATOR_SLASH_EVENTS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> cosmos.distribution.v1beta1.distribution_pb2.Params:
        """params defines all the paramaters of the module."""
    @property
    def fee_pool(self) -> cosmos.distribution.v1beta1.distribution_pb2.FeePool:
        """fee_pool defines the fee pool at genesis."""
    @property
    def delegator_withdraw_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DelegatorWithdrawInfo]:
        """fee_pool defines the delegator withdraw infos at genesis."""
    previous_proposer: builtins.str
    """fee_pool defines the previous proposer at genesis."""
    @property
    def outstanding_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorOutstandingRewardsRecord]:
        """fee_pool defines the outstanding rewards of all validators at genesis."""
    @property
    def validator_accumulated_commissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorAccumulatedCommissionRecord]:
        """fee_pool defines the accumulated commisions of all validators at genesis."""
    @property
    def validator_historical_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorHistoricalRewardsRecord]:
        """fee_pool defines the historical rewards of all validators at genesis."""
    @property
    def validator_current_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorCurrentRewardsRecord]:
        """fee_pool defines the current rewards of all validators at genesis."""
    @property
    def delegator_starting_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DelegatorStartingInfoRecord]:
        """fee_pool defines the delegator starting infos at genesis."""
    @property
    def validator_slash_events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorSlashEventRecord]:
        """fee_pool defines the validator slash events at genesis."""
    def __init__(
        self,
        *,
        params: cosmos.distribution.v1beta1.distribution_pb2.Params | None = ...,
        fee_pool: cosmos.distribution.v1beta1.distribution_pb2.FeePool | None = ...,
        delegator_withdraw_infos: collections.abc.Iterable[global___DelegatorWithdrawInfo] | None = ...,
        previous_proposer: builtins.str = ...,
        outstanding_rewards: collections.abc.Iterable[global___ValidatorOutstandingRewardsRecord] | None = ...,
        validator_accumulated_commissions: collections.abc.Iterable[global___ValidatorAccumulatedCommissionRecord] | None = ...,
        validator_historical_rewards: collections.abc.Iterable[global___ValidatorHistoricalRewardsRecord] | None = ...,
        validator_current_rewards: collections.abc.Iterable[global___ValidatorCurrentRewardsRecord] | None = ...,
        delegator_starting_infos: collections.abc.Iterable[global___DelegatorStartingInfoRecord] | None = ...,
        validator_slash_events: collections.abc.Iterable[global___ValidatorSlashEventRecord] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fee_pool", b"fee_pool", "params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_starting_infos", b"delegator_starting_infos", "delegator_withdraw_infos", b"delegator_withdraw_infos", "fee_pool", b"fee_pool", "outstanding_rewards", b"outstanding_rewards", "params", b"params", "previous_proposer", b"previous_proposer", "validator_accumulated_commissions", b"validator_accumulated_commissions", "validator_current_rewards", b"validator_current_rewards", "validator_historical_rewards", b"validator_historical_rewards", "validator_slash_events", b"validator_slash_events"]) -> None: ...

global___GenesisState = GenesisState
