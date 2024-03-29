"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.46"""
import builtins
import cosmos.group.v1.types_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class EventCreateGroup(google.protobuf.message.Message):
    """EventCreateGroup is an event emitted when a group is created."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    group_id: builtins.int
    """group_id is the unique ID of the group."""
    def __init__(
        self,
        *,
        group_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_id", b"group_id"]) -> None: ...

global___EventCreateGroup = EventCreateGroup

@typing_extensions.final
class EventUpdateGroup(google.protobuf.message.Message):
    """EventUpdateGroup is an event emitted when a group is updated."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    group_id: builtins.int
    """group_id is the unique ID of the group."""
    def __init__(
        self,
        *,
        group_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_id", b"group_id"]) -> None: ...

global___EventUpdateGroup = EventUpdateGroup

@typing_extensions.final
class EventCreateGroupPolicy(google.protobuf.message.Message):
    """EventCreateGroupPolicy is an event emitted when a group policy is created."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """address is the account address of the group policy."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address"]) -> None: ...

global___EventCreateGroupPolicy = EventCreateGroupPolicy

@typing_extensions.final
class EventUpdateGroupPolicy(google.protobuf.message.Message):
    """EventUpdateGroupPolicy is an event emitted when a group policy is updated."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """address is the account address of the group policy."""
    def __init__(
        self,
        *,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address"]) -> None: ...

global___EventUpdateGroupPolicy = EventUpdateGroupPolicy

@typing_extensions.final
class EventSubmitProposal(google.protobuf.message.Message):
    """EventSubmitProposal is an event emitted when a proposal is created."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id is the unique ID of the proposal."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id"]) -> None: ...

global___EventSubmitProposal = EventSubmitProposal

@typing_extensions.final
class EventWithdrawProposal(google.protobuf.message.Message):
    """EventWithdrawProposal is an event emitted when a proposal is withdrawn."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id is the unique ID of the proposal."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id"]) -> None: ...

global___EventWithdrawProposal = EventWithdrawProposal

@typing_extensions.final
class EventVote(google.protobuf.message.Message):
    """EventVote is an event emitted when a voter votes on a proposal."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id is the unique ID of the proposal."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id"]) -> None: ...

global___EventVote = EventVote

@typing_extensions.final
class EventExec(google.protobuf.message.Message):
    """EventExec is an event emitted when a proposal is executed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    LOGS_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id is the unique ID of the proposal."""
    result: cosmos.group.v1.types_pb2.ProposalExecutorResult.ValueType
    """result is the proposal execution result."""
    logs: builtins.str
    """logs contains error logs in case the execution result is FAILURE."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        result: cosmos.group.v1.types_pb2.ProposalExecutorResult.ValueType = ...,
        logs: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["logs", b"logs", "proposal_id", b"proposal_id", "result", b"result"]) -> None: ...

global___EventExec = EventExec

@typing_extensions.final
class EventLeaveGroup(google.protobuf.message.Message):
    """EventLeaveGroup is an event emitted when group member leaves the group."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    group_id: builtins.int
    """group_id is the unique ID of the group."""
    address: builtins.str
    """address is the account address of the group member."""
    def __init__(
        self,
        *,
        group_id: builtins.int = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "group_id", b"group_id"]) -> None: ...

global___EventLeaveGroup = EventLeaveGroup

@typing_extensions.final
class EventProposalPruned(google.protobuf.message.Message):
    """EventProposalPruned is an event emitted when a proposal is pruned."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROPOSAL_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TALLY_RESULT_FIELD_NUMBER: builtins.int
    proposal_id: builtins.int
    """proposal_id is the unique ID of the proposal."""
    status: cosmos.group.v1.types_pb2.ProposalStatus.ValueType
    """status is the proposal status (UNSPECIFIED, SUBMITTED, ACCEPTED, REJECTED, ABORTED, WITHDRAWN)."""
    @property
    def tally_result(self) -> cosmos.group.v1.types_pb2.TallyResult:
        """tally_result is the proposal tally result (when applicable)."""
    def __init__(
        self,
        *,
        proposal_id: builtins.int = ...,
        status: cosmos.group.v1.types_pb2.ProposalStatus.ValueType = ...,
        tally_result: cosmos.group.v1.types_pb2.TallyResult | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tally_result", b"tally_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["proposal_id", b"proposal_id", "status", b"status", "tally_result", b"tally_result"]) -> None: ...

global___EventProposalPruned = EventProposalPruned
