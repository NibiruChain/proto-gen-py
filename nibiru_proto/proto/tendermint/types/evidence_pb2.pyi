"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import tendermint.types.types_pb2
import tendermint.types.validator_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Evidence(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DUPLICATE_VOTE_EVIDENCE_FIELD_NUMBER: builtins.int
    LIGHT_CLIENT_ATTACK_EVIDENCE_FIELD_NUMBER: builtins.int
    @property
    def duplicate_vote_evidence(self) -> global___DuplicateVoteEvidence: ...
    @property
    def light_client_attack_evidence(self) -> global___LightClientAttackEvidence: ...
    def __init__(self,
        *,
        duplicate_vote_evidence: typing.Optional[global___DuplicateVoteEvidence] = ...,
        light_client_attack_evidence: typing.Optional[global___LightClientAttackEvidence] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duplicate_vote_evidence",b"duplicate_vote_evidence","light_client_attack_evidence",b"light_client_attack_evidence","sum",b"sum"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duplicate_vote_evidence",b"duplicate_vote_evidence","light_client_attack_evidence",b"light_client_attack_evidence","sum",b"sum"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["sum",b"sum"]) -> typing.Optional[typing_extensions.Literal["duplicate_vote_evidence","light_client_attack_evidence"]]: ...
global___Evidence = Evidence

class DuplicateVoteEvidence(google.protobuf.message.Message):
    """DuplicateVoteEvidence contains evidence of a validator signed two conflicting votes."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VOTE_A_FIELD_NUMBER: builtins.int
    VOTE_B_FIELD_NUMBER: builtins.int
    TOTAL_VOTING_POWER_FIELD_NUMBER: builtins.int
    VALIDATOR_POWER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    @property
    def vote_a(self) -> tendermint.types.types_pb2.Vote: ...
    @property
    def vote_b(self) -> tendermint.types.types_pb2.Vote: ...
    total_voting_power: builtins.int
    validator_power: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        vote_a: typing.Optional[tendermint.types.types_pb2.Vote] = ...,
        vote_b: typing.Optional[tendermint.types.types_pb2.Vote] = ...,
        total_voting_power: builtins.int = ...,
        validator_power: builtins.int = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp","vote_a",b"vote_a","vote_b",b"vote_b"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp","total_voting_power",b"total_voting_power","validator_power",b"validator_power","vote_a",b"vote_a","vote_b",b"vote_b"]) -> None: ...
global___DuplicateVoteEvidence = DuplicateVoteEvidence

class LightClientAttackEvidence(google.protobuf.message.Message):
    """LightClientAttackEvidence contains evidence of a set of validators attempting to mislead a light client."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFLICTING_BLOCK_FIELD_NUMBER: builtins.int
    COMMON_HEIGHT_FIELD_NUMBER: builtins.int
    BYZANTINE_VALIDATORS_FIELD_NUMBER: builtins.int
    TOTAL_VOTING_POWER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    @property
    def conflicting_block(self) -> tendermint.types.types_pb2.LightBlock: ...
    common_height: builtins.int
    @property
    def byzantine_validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tendermint.types.validator_pb2.Validator]: ...
    total_voting_power: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        conflicting_block: typing.Optional[tendermint.types.types_pb2.LightBlock] = ...,
        common_height: builtins.int = ...,
        byzantine_validators: typing.Optional[typing.Iterable[tendermint.types.validator_pb2.Validator]] = ...,
        total_voting_power: builtins.int = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["conflicting_block",b"conflicting_block","timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["byzantine_validators",b"byzantine_validators","common_height",b"common_height","conflicting_block",b"conflicting_block","timestamp",b"timestamp","total_voting_power",b"total_voting_power"]) -> None: ...
global___LightClientAttackEvidence = LightClientAttackEvidence

class EvidenceList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EVIDENCE_FIELD_NUMBER: builtins.int
    @property
    def evidence(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Evidence]: ...
    def __init__(self,
        *,
        evidence: typing.Optional[typing.Iterable[global___Evidence]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["evidence",b"evidence"]) -> None: ...
global___EvidenceList = EvidenceList
