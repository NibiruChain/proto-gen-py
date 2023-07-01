# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/group/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x63osmos/group/v1/types.proto\x12\x0f\x63osmos.group.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x11\x61mino/amino.proto\"\xb6\x01\n\x06Member\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x16\n\x06weight\x18\x02 \x01(\tR\x06weight\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\x12\x44\n\x08\x61\x64\x64\x65\x64_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x07\x61\x64\x64\x65\x64\x41t\"w\n\rMemberRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x16\n\x06weight\x18\x02 \x01(\tR\x06weight\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\"\xc4\x01\n\x17ThresholdDecisionPolicy\x12\x1c\n\tthreshold\x18\x01 \x01(\tR\tthreshold\x12@\n\x07windows\x18\x02 \x01(\x0b\x32&.cosmos.group.v1.DecisionPolicyWindowsR\x07windows:I\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicy\x8a\xe7\xb0*\"cosmos-sdk/ThresholdDecisionPolicy\"\xc8\x01\n\x18PercentageDecisionPolicy\x12\x1e\n\npercentage\x18\x01 \x01(\tR\npercentage\x12@\n\x07windows\x18\x02 \x01(\x0b\x32&.cosmos.group.v1.DecisionPolicyWindowsR\x07windows:J\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicy\x8a\xe7\xb0*#cosmos-sdk/PercentageDecisionPolicy\"\xc2\x01\n\x15\x44\x65\x63isionPolicyWindows\x12M\n\rvoting_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x0cvotingPeriod\x12Z\n\x14min_execution_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x12minExecutionPeriod\"\xee\x01\n\tGroupInfo\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12.\n\x05\x61\x64min\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\x12\x18\n\x07version\x18\x04 \x01(\x04R\x07version\x12!\n\x0ctotal_weight\x18\x05 \x01(\tR\x0btotalWeight\x12H\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\tcreatedAt\"Y\n\x0bGroupMember\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\x12/\n\x06member\x18\x02 \x01(\x0b\x32\x17.cosmos.group.v1.MemberR\x06member\"\xfd\x02\n\x0fGroupPolicyInfo\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x19\n\x08group_id\x18\x02 \x01(\x04R\x07groupId\x12.\n\x05\x61\x64min\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x1a\n\x08metadata\x18\x04 \x01(\tR\x08metadata\x12\x18\n\x07version\x18\x05 \x01(\x04R\x07version\x12\x61\n\x0f\x64\x65\x63ision_policy\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyB\"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicyR\x0e\x64\x65\x63isionPolicy\x12H\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\tcreatedAt:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x01\"\xfe\x05\n\x08Proposal\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12J\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12groupPolicyAddress\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\x12\x36\n\tproposers\x18\x04 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tproposers\x12J\n\x0bsubmit_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\nsubmitTime\x12#\n\rgroup_version\x18\x06 \x01(\x04R\x0cgroupVersion\x12\x30\n\x14group_policy_version\x18\x07 \x01(\x04R\x12groupPolicyVersion\x12\x37\n\x06status\x18\x08 \x01(\x0e\x32\x1f.cosmos.group.v1.ProposalStatusR\x06status\x12U\n\x12\x66inal_tally_result\x18\t \x01(\x0b\x32\x1c.cosmos.group.v1.TallyResultB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x10\x66inalTallyResult\x12U\n\x11voting_period_end\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x0fvotingPeriodEnd\x12P\n\x0f\x65xecutor_result\x18\x0b \x01(\x0e\x32\'.cosmos.group.v1.ProposalExecutorResultR\x0e\x65xecutorResult\x12\x30\n\x08messages\x18\x0c \x03(\x0b\x32\x14.google.protobuf.AnyR\x08messages\x12\x14\n\x05title\x18\r \x01(\tR\x05title\x12\x18\n\x07summary\x18\x0e \x01(\tR\x07summary:\x04\x88\xa0\x1f\x00\"\x9d\x01\n\x0bTallyResult\x12\x1b\n\tyes_count\x18\x01 \x01(\tR\x08yesCount\x12#\n\rabstain_count\x18\x02 \x01(\tR\x0c\x61\x62stainCount\x12\x19\n\x08no_count\x18\x03 \x01(\tR\x07noCount\x12+\n\x12no_with_veto_count\x18\x04 \x01(\tR\x0fnoWithVetoCount:\x04\x88\xa0\x1f\x00\"\xf4\x01\n\x04Vote\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12.\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05voter\x12\x33\n\x06option\x18\x03 \x01(\x0e\x32\x1b.cosmos.group.v1.VoteOptionR\x06option\x12\x1a\n\x08metadata\x18\x04 \x01(\tR\x08metadata\x12J\n\x0bsubmit_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\nsubmitTime*\x8f\x01\n\nVoteOption\x12\x1b\n\x17VOTE_OPTION_UNSPECIFIED\x10\x00\x12\x13\n\x0fVOTE_OPTION_YES\x10\x01\x12\x17\n\x13VOTE_OPTION_ABSTAIN\x10\x02\x12\x12\n\x0eVOTE_OPTION_NO\x10\x03\x12\x1c\n\x18VOTE_OPTION_NO_WITH_VETO\x10\x04\x1a\x04\x88\xa3\x1e\x00*\xce\x01\n\x0eProposalStatus\x12\x1f\n\x1bPROPOSAL_STATUS_UNSPECIFIED\x10\x00\x12\x1d\n\x19PROPOSAL_STATUS_SUBMITTED\x10\x01\x12\x1c\n\x18PROPOSAL_STATUS_ACCEPTED\x10\x02\x12\x1c\n\x18PROPOSAL_STATUS_REJECTED\x10\x03\x12\x1b\n\x17PROPOSAL_STATUS_ABORTED\x10\x04\x12\x1d\n\x19PROPOSAL_STATUS_WITHDRAWN\x10\x05\x1a\x04\x88\xa3\x1e\x00*\xba\x01\n\x16ProposalExecutorResult\x12(\n$PROPOSAL_EXECUTOR_RESULT_UNSPECIFIED\x10\x00\x12$\n PROPOSAL_EXECUTOR_RESULT_NOT_RUN\x10\x01\x12$\n PROPOSAL_EXECUTOR_RESULT_SUCCESS\x10\x02\x12$\n PROPOSAL_EXECUTOR_RESULT_FAILURE\x10\x03\x1a\x04\x88\xa3\x1e\x00\x42&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'cosmos.group.v1.types_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
    _VOTEOPTION._options = None
    _VOTEOPTION._serialized_options = b'\210\243\036\000'
    _PROPOSALSTATUS._options = None
    _PROPOSALSTATUS._serialized_options = b'\210\243\036\000'
    _PROPOSALEXECUTORRESULT._options = None
    _PROPOSALEXECUTORRESULT._serialized_options = b'\210\243\036\000'
    _MEMBER.fields_by_name['address']._options = None
    _MEMBER.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _MEMBER.fields_by_name['added_at']._options = None
    _MEMBER.fields_by_name[
        'added_at'
    ]._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
    _MEMBERREQUEST.fields_by_name['address']._options = None
    _MEMBERREQUEST.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _THRESHOLDDECISIONPOLICY._options = None
    _THRESHOLDDECISIONPOLICY._serialized_options = b'\312\264-\036cosmos.group.v1.DecisionPolicy\212\347\260*\"cosmos-sdk/ThresholdDecisionPolicy'
    _PERCENTAGEDECISIONPOLICY._options = None
    _PERCENTAGEDECISIONPOLICY._serialized_options = b'\312\264-\036cosmos.group.v1.DecisionPolicy\212\347\260*#cosmos-sdk/PercentageDecisionPolicy'
    _DECISIONPOLICYWINDOWS.fields_by_name['voting_period']._options = None
    _DECISIONPOLICYWINDOWS.fields_by_name[
        'voting_period'
    ]._serialized_options = b'\310\336\037\000\230\337\037\001\250\347\260*\001'
    _DECISIONPOLICYWINDOWS.fields_by_name['min_execution_period']._options = None
    _DECISIONPOLICYWINDOWS.fields_by_name[
        'min_execution_period'
    ]._serialized_options = b'\310\336\037\000\230\337\037\001\250\347\260*\001'
    _GROUPINFO.fields_by_name['admin']._options = None
    _GROUPINFO.fields_by_name[
        'admin'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _GROUPINFO.fields_by_name['created_at']._options = None
    _GROUPINFO.fields_by_name[
        'created_at'
    ]._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
    _GROUPPOLICYINFO.fields_by_name['address']._options = None
    _GROUPPOLICYINFO.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _GROUPPOLICYINFO.fields_by_name['admin']._options = None
    _GROUPPOLICYINFO.fields_by_name[
        'admin'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _GROUPPOLICYINFO.fields_by_name['decision_policy']._options = None
    _GROUPPOLICYINFO.fields_by_name[
        'decision_policy'
    ]._serialized_options = b'\312\264-\036cosmos.group.v1.DecisionPolicy'
    _GROUPPOLICYINFO.fields_by_name['created_at']._options = None
    _GROUPPOLICYINFO.fields_by_name[
        'created_at'
    ]._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
    _GROUPPOLICYINFO._options = None
    _GROUPPOLICYINFO._serialized_options = b'\210\240\037\000\350\240\037\001'
    _PROPOSAL.fields_by_name['group_policy_address']._options = None
    _PROPOSAL.fields_by_name[
        'group_policy_address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _PROPOSAL.fields_by_name['proposers']._options = None
    _PROPOSAL.fields_by_name[
        'proposers'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _PROPOSAL.fields_by_name['submit_time']._options = None
    _PROPOSAL.fields_by_name[
        'submit_time'
    ]._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
    _PROPOSAL.fields_by_name['final_tally_result']._options = None
    _PROPOSAL.fields_by_name[
        'final_tally_result'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _PROPOSAL.fields_by_name['voting_period_end']._options = None
    _PROPOSAL.fields_by_name[
        'voting_period_end'
    ]._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
    _PROPOSAL._options = None
    _PROPOSAL._serialized_options = b'\210\240\037\000'
    _TALLYRESULT._options = None
    _TALLYRESULT._serialized_options = b'\210\240\037\000'
    _VOTE.fields_by_name['voter']._options = None
    _VOTE.fields_by_name[
        'voter'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _VOTE.fields_by_name['submit_time']._options = None
    _VOTE.fields_by_name[
        'submit_time'
    ]._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
    _globals['_VOTEOPTION']._serialized_start = 3006
    _globals['_VOTEOPTION']._serialized_end = 3149
    _globals['_PROPOSALSTATUS']._serialized_start = 3152
    _globals['_PROPOSALSTATUS']._serialized_end = 3358
    _globals['_PROPOSALEXECUTORRESULT']._serialized_start = 3361
    _globals['_PROPOSALEXECUTORRESULT']._serialized_end = 3547
    _globals['_MEMBER']._serialized_start = 209
    _globals['_MEMBER']._serialized_end = 391
    _globals['_MEMBERREQUEST']._serialized_start = 393
    _globals['_MEMBERREQUEST']._serialized_end = 512
    _globals['_THRESHOLDDECISIONPOLICY']._serialized_start = 515
    _globals['_THRESHOLDDECISIONPOLICY']._serialized_end = 711
    _globals['_PERCENTAGEDECISIONPOLICY']._serialized_start = 714
    _globals['_PERCENTAGEDECISIONPOLICY']._serialized_end = 914
    _globals['_DECISIONPOLICYWINDOWS']._serialized_start = 917
    _globals['_DECISIONPOLICYWINDOWS']._serialized_end = 1111
    _globals['_GROUPINFO']._serialized_start = 1114
    _globals['_GROUPINFO']._serialized_end = 1352
    _globals['_GROUPMEMBER']._serialized_start = 1354
    _globals['_GROUPMEMBER']._serialized_end = 1443
    _globals['_GROUPPOLICYINFO']._serialized_start = 1446
    _globals['_GROUPPOLICYINFO']._serialized_end = 1827
    _globals['_PROPOSAL']._serialized_start = 1830
    _globals['_PROPOSAL']._serialized_end = 2596
    _globals['_TALLYRESULT']._serialized_start = 2599
    _globals['_TALLYRESULT']._serialized_end = 2756
    _globals['_VOTE']._serialized_start = 2759
    _globals['_VOTE']._serialized_end = 3003
# @@protoc_insertion_point(module_scope)
