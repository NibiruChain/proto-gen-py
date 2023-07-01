# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/nft/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import (
    pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.nft.v1beta1 import nft_pb2 as cosmos_dot_nft_dot_v1beta1_dot_nft__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1e\x63osmos/nft/v1beta1/query.proto\x12\x12\x63osmos.nft.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1c\x63osmos/nft/v1beta1/nft.proto\"F\n\x13QueryBalanceRequest\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x14\n\x05owner\x18\x02 \x01(\tR\x05owner\".\n\x14QueryBalanceResponse\x12\x16\n\x06\x61mount\x18\x01 \x01(\x04R\x06\x61mount\">\n\x11QueryOwnerRequest\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\"*\n\x12QueryOwnerResponse\x12\x14\n\x05owner\x18\x01 \x01(\tR\x05owner\"/\n\x12QuerySupplyRequest\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\"-\n\x13QuerySupplyResponse\x12\x16\n\x06\x61mount\x18\x01 \x01(\x04R\x06\x61mount\"\x8b\x01\n\x10QueryNFTsRequest\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x14\n\x05owner\x18\x02 \x01(\tR\x05owner\x12\x46\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x89\x01\n\x11QueryNFTsResponse\x12+\n\x04nfts\x18\x01 \x03(\x0b\x32\x17.cosmos.nft.v1beta1.NFTR\x04nfts\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"<\n\x0fQueryNFTRequest\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\"=\n\x10QueryNFTResponse\x12)\n\x03nft\x18\x01 \x01(\x0b\x32\x17.cosmos.nft.v1beta1.NFTR\x03nft\".\n\x11QueryClassRequest\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\"E\n\x12QueryClassResponse\x12/\n\x05\x63lass\x18\x01 \x01(\x0b\x32\x19.cosmos.nft.v1beta1.ClassR\x05\x63lass\"]\n\x13QueryClassesRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x94\x01\n\x14QueryClassesResponse\x12\x33\n\x07\x63lasses\x18\x01 \x03(\x0b\x32\x19.cosmos.nft.v1beta1.ClassR\x07\x63lasses\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination2\xbe\x07\n\x05Query\x12\x94\x01\n\x07\x42\x61lance\x12\'.cosmos.nft.v1beta1.QueryBalanceRequest\x1a(.cosmos.nft.v1beta1.QueryBalanceResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./cosmos/nft/v1beta1/balance/{owner}/{class_id}\x12\x89\x01\n\x05Owner\x12%.cosmos.nft.v1beta1.QueryOwnerRequest\x1a&.cosmos.nft.v1beta1.QueryOwnerResponse\"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/nft/v1beta1/owner/{class_id}/{id}\x12\x88\x01\n\x06Supply\x12&.cosmos.nft.v1beta1.QuerySupplyRequest\x1a\'.cosmos.nft.v1beta1.QuerySupplyResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/cosmos/nft/v1beta1/supply/{class_id}\x12u\n\x04NFTs\x12$.cosmos.nft.v1beta1.QueryNFTsRequest\x1a%.cosmos.nft.v1beta1.QueryNFTsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/cosmos/nft/v1beta1/nfts\x12\x82\x01\n\x03NFT\x12#.cosmos.nft.v1beta1.QueryNFTRequest\x1a$.cosmos.nft.v1beta1.QueryNFTResponse\"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/nft/v1beta1/nfts/{class_id}/{id}\x12\x86\x01\n\x05\x43lass\x12%.cosmos.nft.v1beta1.QueryClassRequest\x1a&.cosmos.nft.v1beta1.QueryClassResponse\".\x82\xd3\xe4\x93\x02(\x12&/cosmos/nft/v1beta1/classes/{class_id}\x12\x81\x01\n\x07\x43lasses\x12\'.cosmos.nft.v1beta1.QueryClassesRequest\x1a(.cosmos.nft.v1beta1.QueryClassesResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/nft/v1beta1/classesB$Z\"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'cosmos.nft.v1beta1.query_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\"github.com/cosmos/cosmos-sdk/x/nft'
    _QUERY.methods_by_name['Balance']._options = None
    _QUERY.methods_by_name[
        'Balance'
    ]._serialized_options = (
        b'\202\323\344\223\0020\022./cosmos/nft/v1beta1/balance/{owner}/{class_id}'
    )
    _QUERY.methods_by_name['Owner']._options = None
    _QUERY.methods_by_name[
        'Owner'
    ]._serialized_options = (
        b'\202\323\344\223\002+\022)/cosmos/nft/v1beta1/owner/{class_id}/{id}'
    )
    _QUERY.methods_by_name['Supply']._options = None
    _QUERY.methods_by_name[
        'Supply'
    ]._serialized_options = (
        b'\202\323\344\223\002\'\022%/cosmos/nft/v1beta1/supply/{class_id}'
    )
    _QUERY.methods_by_name['NFTs']._options = None
    _QUERY.methods_by_name[
        'NFTs'
    ]._serialized_options = b'\202\323\344\223\002\032\022\030/cosmos/nft/v1beta1/nfts'
    _QUERY.methods_by_name['NFT']._options = None
    _QUERY.methods_by_name[
        'NFT'
    ]._serialized_options = (
        b'\202\323\344\223\002*\022(/cosmos/nft/v1beta1/nfts/{class_id}/{id}'
    )
    _QUERY.methods_by_name['Class']._options = None
    _QUERY.methods_by_name[
        'Class'
    ]._serialized_options = (
        b'\202\323\344\223\002(\022&/cosmos/nft/v1beta1/classes/{class_id}'
    )
    _QUERY.methods_by_name['Classes']._options = None
    _QUERY.methods_by_name[
        'Classes'
    ]._serialized_options = (
        b'\202\323\344\223\002\035\022\033/cosmos/nft/v1beta1/classes'
    )
    _globals['_QUERYBALANCEREQUEST']._serialized_start = 158
    _globals['_QUERYBALANCEREQUEST']._serialized_end = 228
    _globals['_QUERYBALANCERESPONSE']._serialized_start = 230
    _globals['_QUERYBALANCERESPONSE']._serialized_end = 276
    _globals['_QUERYOWNERREQUEST']._serialized_start = 278
    _globals['_QUERYOWNERREQUEST']._serialized_end = 340
    _globals['_QUERYOWNERRESPONSE']._serialized_start = 342
    _globals['_QUERYOWNERRESPONSE']._serialized_end = 384
    _globals['_QUERYSUPPLYREQUEST']._serialized_start = 386
    _globals['_QUERYSUPPLYREQUEST']._serialized_end = 433
    _globals['_QUERYSUPPLYRESPONSE']._serialized_start = 435
    _globals['_QUERYSUPPLYRESPONSE']._serialized_end = 480
    _globals['_QUERYNFTSREQUEST']._serialized_start = 483
    _globals['_QUERYNFTSREQUEST']._serialized_end = 622
    _globals['_QUERYNFTSRESPONSE']._serialized_start = 625
    _globals['_QUERYNFTSRESPONSE']._serialized_end = 762
    _globals['_QUERYNFTREQUEST']._serialized_start = 764
    _globals['_QUERYNFTREQUEST']._serialized_end = 824
    _globals['_QUERYNFTRESPONSE']._serialized_start = 826
    _globals['_QUERYNFTRESPONSE']._serialized_end = 887
    _globals['_QUERYCLASSREQUEST']._serialized_start = 889
    _globals['_QUERYCLASSREQUEST']._serialized_end = 935
    _globals['_QUERYCLASSRESPONSE']._serialized_start = 937
    _globals['_QUERYCLASSRESPONSE']._serialized_end = 1006
    _globals['_QUERYCLASSESREQUEST']._serialized_start = 1008
    _globals['_QUERYCLASSESREQUEST']._serialized_end = 1101
    _globals['_QUERYCLASSESRESPONSE']._serialized_start = 1104
    _globals['_QUERYCLASSESRESPONSE']._serialized_end = 1252
    _globals['_QUERY']._serialized_start = 1255
    _globals['_QUERY']._serialized_end = 2213
# @@protoc_insertion_point(module_scope)
