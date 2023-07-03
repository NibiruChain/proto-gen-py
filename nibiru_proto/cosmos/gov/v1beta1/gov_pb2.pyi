"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _VoteOption:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VoteOptionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VoteOption.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VOTE_OPTION_UNSPECIFIED: _VoteOption.ValueType  # 0
    """VOTE_OPTION_UNSPECIFIED defines a no-op vote option."""
    VOTE_OPTION_YES: _VoteOption.ValueType  # 1
    """VOTE_OPTION_YES defines a yes vote option."""
    VOTE_OPTION_ABSTAIN: _VoteOption.ValueType  # 2
    """VOTE_OPTION_ABSTAIN defines an abstain vote option."""
    VOTE_OPTION_NO: _VoteOption.ValueType  # 3
    """VOTE_OPTION_NO defines a no vote option."""
    VOTE_OPTION_NO_WITH_VETO: _VoteOption.ValueType  # 4
    """VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option."""

class VoteOption(_VoteOption, metaclass=_VoteOptionEnumTypeWrapper):
    """VoteOption enumerates the valid vote options for a given governance proposal."""

VOTE_OPTION_UNSPECIFIED: VoteOption.ValueType  # 0
"""VOTE_OPTION_UNSPECIFIED defines a no-op vote option."""
VOTE_OPTION_YES: VoteOption.ValueType  # 1
"""VOTE_OPTION_YES defines a yes vote option."""
VOTE_OPTION_ABSTAIN: VoteOption.ValueType  # 2
"""VOTE_OPTION_ABSTAIN defines an abstain vote option."""
VOTE_OPTION_NO: VoteOption.ValueType  # 3
"""VOTE_OPTION_NO defines a no vote option."""
VOTE_OPTION_NO_WITH_VETO: VoteOption.ValueType  # 4
"""VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option."""
global___VoteOption = VoteOption

class _ProposalStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProposalStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProposalStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROPOSAL_STATUS_UNSPECIFIED: _ProposalStatus.ValueType  # 0
    """PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status."""
    PROPOSAL_STATUS_DEPOSIT_PERIOD: _ProposalStatus.ValueType  # 1
    """PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit
    period.
    """
    PROPOSAL_STATUS_VOTING_PERIOD: _ProposalStatus.ValueType  # 2
    """PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting
    period.
    """
    PROPOSAL_STATUS_PASSED: _ProposalStatus.ValueType  # 3
    """PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has
    passed.
    """
    PROPOSAL_STATUS_REJECTED: _ProposalStatus.ValueType  # 4
    """PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has
    been rejected.
    """
    PROPOSAL_STATUS_FAILED: _ProposalStatus.ValueType  # 5
    """PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has
    failed.
    """

class ProposalStatus(_ProposalStatus, metaclass=_ProposalStatusEnumTypeWrapper):
    """ProposalStatus enumerates the valid statuses of a proposal."""

PROPOSAL_STATUS_UNSPECIFIED: ProposalStatus.ValueType  # 0
"""PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status."""
PROPOSAL_STATUS_DEPOSIT_PERIOD: ProposalStatus.ValueType  # 1
"""PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit
period.
"""
PROPOSAL_STATUS_VOTING_PERIOD: ProposalStatus.ValueType  # 2
"""PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting
period.
"""
PROPOSAL_STATUS_PASSED: ProposalStatus.ValueType  # 3
"""PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has
passed.
"""
PROPOSAL_STATUS_REJECTED: ProposalStatus.ValueType  # 4
"""PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has
been rejected.
"""
PROPOSAL_STATUS_FAILED: ProposalStatus.ValueType  # 5
"""PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has
failed.
"""
global___ProposalStatus = ProposalStatus

@typing_extensions.final
class WeightedVoteOption(google.protobuf.message.Message):
    """WeightedVoteOption defines a unit of vote for vote split.

    Since: cosmos-sdk 0.43
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPTION_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    option: global___VoteOption.ValueType
    """option defines the valid vote options, it must not contain duplicate vote options."""
    weight: builtins.str
    """weight is the vote weight associated with the vote option."""
    def __init__(
        self,
        *,
        option: global___VoteOption.ValueType = ...,
        weight: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["option", b"option", "weight", b"weight"]) -> None: ...

global___WeightedVoteOption = WeightedVoteOption

@typing_extensions.final
class TextProposal(google.protobuf.message.Message):
    """TextProposal defines a standard text proposal whose changes need to be
    manually updated in case of approval.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    title: builtins.str
    """title of the proposal."""
    description: builtins.str
    """description associated with the proposal."""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "title", b"title"]) -> None: ...

global___TextProposal = TextProposal

@typing_extensions.final
class Deposit(google.protobuf.message.Message):
    """Deposit defines an amount deposited by an account address to an active
    proposal.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    DEPOSITOR_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    depositor: builtins.str
    """depositor defines the deposit addresses from the proposals."""
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """amount to be deposited by depositor."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        depositor: builtins.str = ...,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "depositor", b"depositor", "proposal_id", b"proposal_id"]) -> None: ...

global___Deposit = Deposit

@typing_extensions.final
class Proposal(google.protobuf.message.Message):
    """Proposal defines the core field members of a governance proposal."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    FINAL_TALLY_RESULT_FIELD_NUMBER: builtins.int
    SUBMIT_TIME_FIELD_NUMBER: builtins.int
    DEPOSIT_END_TIME_FIELD_NUMBER: builtins.int
    TOTAL_DEPOSIT_FIELD_NUMBER: builtins.int
    VOTING_START_TIME_FIELD_NUMBER: builtins.int
    VOTING_END_TIME_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    @property
    def content(self) -> google.protobuf.any_pb2.Any:
        """content is the proposal's content."""
    status: global___ProposalStatus.ValueType
    """status defines the proposal status."""
    @property
    def final_tally_result(self) -> global___TallyResult:
        """final_tally_result is the final tally result of the proposal. When
        querying a proposal via gRPC, this field is not populated until the
        proposal's voting period has ended.
        """
    @property
    def submit_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """submit_time is the time of proposal submission."""
    @property
    def deposit_end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """deposit_end_time is the end time for deposition."""
    @property
    def total_deposit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """total_deposit is the total deposit on the proposal."""
    @property
    def voting_start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """voting_start_time is the starting time to vote on a proposal."""
    @property
    def voting_end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """voting_end_time is the end time of voting on a proposal."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        content: google.protobuf.any_pb2.Any | None = ...,
        status: global___ProposalStatus.ValueType = ...,
        final_tally_result: global___TallyResult | None = ...,
        submit_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        deposit_end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        total_deposit: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        voting_start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        voting_end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content", b"content", "deposit_end_time", b"deposit_end_time", "final_tally_result", b"final_tally_result", "submit_time", b"submit_time", "voting_end_time", b"voting_end_time", "voting_start_time", b"voting_start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content", "deposit_end_time", b"deposit_end_time", "final_tally_result", b"final_tally_result", "proposal_id", b"proposal_id", "status", b"status", "submit_time", b"submit_time", "total_deposit", b"total_deposit", "voting_end_time", b"voting_end_time", "voting_start_time", b"voting_start_time"]) -> None: ...

global___Proposal = Proposal

@typing_extensions.final
class TallyResult(google.protobuf.message.Message):
    """TallyResult defines a standard tally for a governance proposal."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    YES_FIELD_NUMBER: builtins.int
    ABSTAIN_FIELD_NUMBER: builtins.int
    NO_FIELD_NUMBER: builtins.int
    NO_WITH_VETO_FIELD_NUMBER: builtins.int
    yes: builtins.str
    """yes is the number of yes votes on a proposal."""
    abstain: builtins.str
    """abstain is the number of abstain votes on a proposal."""
    no: builtins.str
    """no is the number of no votes on a proposal."""
    no_with_veto: builtins.str
    """no_with_veto is the number of no with veto votes on a proposal."""
    def __init__(
        self,
        *,
        yes: builtins.str = ...,
        abstain: builtins.str = ...,
        no: builtins.str = ...,
        no_with_veto: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["abstain", b"abstain", "no", b"no", "no_with_veto", b"no_with_veto", "yes", b"yes"]) -> None: ...

global___TallyResult = TallyResult

@typing_extensions.final
class Vote(google.protobuf.message.Message):
    """Vote defines a vote on a governance proposal.
    A Vote consists of a proposal ID, the voter, and the vote option.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    VOTER_FIELD_NUMBER: builtins.int
    OPTION_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id defines the unique id of the proposal."""
    voter: builtins.str
    """voter is the voter address of the proposal."""
    option: global___VoteOption.ValueType
    """Deprecated: Prefer to use `options` instead. This field is set in queries
    if and only if `len(options) == 1` and that option has weight 1. In all
    other cases, this field will default to VOTE_OPTION_UNSPECIFIED.
    """
    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WeightedVoteOption]:
        """options is the weighted vote options.

        Since: cosmos-sdk 0.43
        """
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        voter: builtins.str = ...,
        option: global___VoteOption.ValueType = ...,
        options: collections.abc.Iterable[global___WeightedVoteOption] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["option", b"option", "options", b"options", "proposal_id", b"proposal_id", "voter", b"voter"]) -> None: ...

global___Vote = Vote

@typing_extensions.final
class DepositParams(google.protobuf.message.Message):
    """DepositParams defines the params for deposits on governance proposals."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_DEPOSIT_FIELD_NUMBER: builtins.int
    MAX_DEPOSIT_PERIOD_FIELD_NUMBER: builtins.int
    @property
    def min_deposit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """Minimum deposit for a proposal to enter voting period."""
    @property
    def max_deposit_period(self) -> google.protobuf.duration_pb2.Duration:
        """Maximum period for Atom holders to deposit on a proposal. Initial value: 2
        months.
        """
    def __init__(
        self,
        *,
        min_deposit: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        max_deposit_period: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_deposit_period", b"max_deposit_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_deposit_period", b"max_deposit_period", "min_deposit", b"min_deposit"]) -> None: ...

global___DepositParams = DepositParams

@typing_extensions.final
class VotingParams(google.protobuf.message.Message):
    """VotingParams defines the params for voting on governance proposals."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOTING_PERIOD_FIELD_NUMBER: builtins.int
    @property
    def voting_period(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the voting period."""
    def __init__(
        self,
        *,
        voting_period: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["voting_period", b"voting_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["voting_period", b"voting_period"]) -> None: ...

global___VotingParams = VotingParams

@typing_extensions.final
class TallyParams(google.protobuf.message.Message):
    """TallyParams defines the params for tallying votes on governance proposals."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUORUM_FIELD_NUMBER: builtins.int
    THRESHOLD_FIELD_NUMBER: builtins.int
    VETO_THRESHOLD_FIELD_NUMBER: builtins.int
    quorum: builtins.bytes
    """Minimum percentage of total stake needed to vote for a result to be
    considered valid.
    """
    threshold: builtins.bytes
    """Minimum proportion of Yes votes for proposal to pass. Default value: 0.5."""
    veto_threshold: builtins.bytes
    """Minimum value of Veto votes to Total votes ratio for proposal to be
    vetoed. Default value: 1/3.
    """
    def __init__(
        self,
        *,
        quorum: builtins.bytes = ...,
        threshold: builtins.bytes = ...,
        veto_threshold: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["quorum", b"quorum", "threshold", b"threshold", "veto_threshold", b"veto_threshold"]) -> None: ...

global___TallyParams = TallyParams
