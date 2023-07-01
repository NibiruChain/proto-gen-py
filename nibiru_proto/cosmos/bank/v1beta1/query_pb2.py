# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/query.proto
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
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x63osmos/bank/v1beta1/query.proto\x12\x13\x63osmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1b\x63osmos/query/v1/query.proto\x1a\x11\x61mino/amino.proto\"i\n\x13QueryBalanceRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"K\n\x14QueryBalanceResponse\x12\x33\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x07\x62\x61lance\"\x9f\x01\n\x17QueryAllBalancesRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xd1\x01\n\x18QueryAllBalancesResponse\x12l\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x08\x62\x61lances\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\xa5\x01\n\x1dQuerySpendableBalancesRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xd7\x01\n\x1eQuerySpendableBalancesResponse\x12l\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x08\x62\x61lances\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"y\n#QuerySpendableBalanceByDenomRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"[\n$QuerySpendableBalanceByDenomResponse\x12\x33\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x07\x62\x61lance\"k\n\x17QueryTotalSupplyRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xcd\x01\n\x18QueryTotalSupplyResponse\x12h\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01R\x06supply\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\",\n\x14QuerySupplyOfRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"U\n\x15QuerySupplyOfResponse\x12<\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06\x61mount\"\x14\n\x12QueryParamsRequest\"U\n\x13QueryParamsResponse\x12>\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\"d\n\x1aQueryDenomsMetadataRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xae\x01\n\x1bQueryDenomsMetadataResponse\x12\x46\n\tmetadatas\x18\x01 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\tmetadatas\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"1\n\x19QueryDenomMetadataRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"b\n\x1aQueryDenomMetadataResponse\x12\x44\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x08metadata\"w\n\x17QueryDenomOwnersRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x80\x01\n\nDenomOwner\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12>\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x62\x61lance\"\xa7\x01\n\x18QueryDenomOwnersResponse\x12\x42\n\x0c\x64\x65nom_owners\x18\x01 \x03(\x0b\x32\x1f.cosmos.bank.v1beta1.DenomOwnerR\x0b\x64\x65nomOwners\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"y\n\x17QuerySendEnabledRequest\x12\x16\n\x06\x64\x65noms\x18\x01 \x03(\tR\x06\x64\x65noms\x12\x46\n\npagination\x18\x63 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa8\x01\n\x18QuerySendEnabledResponse\x12\x43\n\x0csend_enabled\x18\x01 \x03(\x0b\x32 .cosmos.bank.v1beta1.SendEnabledR\x0bsendEnabled\x12G\n\npagination\x18\x63 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination2\xb2\x0e\n\x05Query\x12\x9d\x01\n\x07\x42\x61lance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse\"=\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/bank/v1beta1/balances/{address}/by_denom\x12\xa0\x01\n\x0b\x41llBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse\"4\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\xbc\x01\n\x11SpendableBalances\x12\x32.cosmos.bank.v1beta1.QuerySpendableBalancesRequest\x1a\x33.cosmos.bank.v1beta1.QuerySpendableBalancesResponse\">\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/bank/v1beta1/spendable_balances/{address}\x12\xd7\x01\n\x17SpendableBalanceByDenom\x12\x38.cosmos.bank.v1beta1.QuerySpendableBalanceByDenomRequest\x1a\x39.cosmos.bank.v1beta1.QuerySpendableBalanceByDenomResponse\"G\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02<\x12:/cosmos/bank/v1beta1/spendable_balances/{address}/by_denom\x12\x94\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x94\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse\"1\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/supply/by_denom\x12\x85\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xab\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse\"9\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xa6\x01\n\x0e\x44\x65nomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a\x30.cosmos.bank.v1beta1.QueryDenomsMetadataResponse\"1\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadata\x12\xa2\x01\n\x0b\x44\x65nomOwners\x12,.cosmos.bank.v1beta1.QueryDenomOwnersRequest\x1a-.cosmos.bank.v1beta1.QueryDenomOwnersResponse\"6\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02+\x12)/cosmos/bank/v1beta1/denom_owners/{denom}\x12\x9a\x01\n\x0bSendEnabled\x12,.cosmos.bank.v1beta1.QuerySendEnabledRequest\x1a-.cosmos.bank.v1beta1.QuerySendEnabledResponse\".\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02#\x12!/cosmos/bank/v1beta1/send_enabledB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'cosmos.bank.v1beta1.query_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _QUERYBALANCEREQUEST.fields_by_name['address']._options = None
    _QUERYBALANCEREQUEST.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _QUERYBALANCEREQUEST._options = None
    _QUERYBALANCEREQUEST._serialized_options = b'\210\240\037\000\350\240\037\000'
    _QUERYALLBALANCESREQUEST.fields_by_name['address']._options = None
    _QUERYALLBALANCESREQUEST.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _QUERYALLBALANCESREQUEST._options = None
    _QUERYALLBALANCESREQUEST._serialized_options = b'\210\240\037\000\350\240\037\000'
    _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._options = None
    _QUERYALLBALANCESRESPONSE.fields_by_name[
        'balances'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _QUERYSPENDABLEBALANCESREQUEST.fields_by_name['address']._options = None
    _QUERYSPENDABLEBALANCESREQUEST.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _QUERYSPENDABLEBALANCESREQUEST._options = None
    _QUERYSPENDABLEBALANCESREQUEST._serialized_options = (
        b'\210\240\037\000\350\240\037\000'
    )
    _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._options = None
    _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name[
        'balances'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _QUERYSPENDABLEBALANCEBYDENOMREQUEST.fields_by_name['address']._options = None
    _QUERYSPENDABLEBALANCEBYDENOMREQUEST.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _QUERYSPENDABLEBALANCEBYDENOMREQUEST._options = None
    _QUERYSPENDABLEBALANCEBYDENOMREQUEST._serialized_options = (
        b'\210\240\037\000\350\240\037\000'
    )
    _QUERYTOTALSUPPLYREQUEST._options = None
    _QUERYTOTALSUPPLYREQUEST._serialized_options = b'\210\240\037\000\350\240\037\000'
    _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._options = None
    _QUERYTOTALSUPPLYRESPONSE.fields_by_name[
        'supply'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
    _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._options = None
    _QUERYSUPPLYOFRESPONSE.fields_by_name[
        'amount'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name[
        'params'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._options = None
    _QUERYDENOMSMETADATARESPONSE.fields_by_name[
        'metadatas'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._options = None
    _QUERYDENOMMETADATARESPONSE.fields_by_name[
        'metadata'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _DENOMOWNER.fields_by_name['address']._options = None
    _DENOMOWNER.fields_by_name[
        'address'
    ]._serialized_options = b'\322\264-\024cosmos.AddressString'
    _DENOMOWNER.fields_by_name['balance']._options = None
    _DENOMOWNER.fields_by_name[
        'balance'
    ]._serialized_options = b'\310\336\037\000\250\347\260*\001'
    _QUERY.methods_by_name['Balance']._options = None
    _QUERY.methods_by_name[
        'Balance'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\0022\0220/cosmos/bank/v1beta1/balances/{address}/by_denom'
    _QUERY.methods_by_name['AllBalances']._options = None
    _QUERY.methods_by_name[
        'AllBalances'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\002)\022\'/cosmos/bank/v1beta1/balances/{address}'
    _QUERY.methods_by_name['SpendableBalances']._options = None
    _QUERY.methods_by_name[
        'SpendableBalances'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\0023\0221/cosmos/bank/v1beta1/spendable_balances/{address}'
    _QUERY.methods_by_name['SpendableBalanceByDenom']._options = None
    _QUERY.methods_by_name[
        'SpendableBalanceByDenom'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\002<\022:/cosmos/bank/v1beta1/spendable_balances/{address}/by_denom'
    _QUERY.methods_by_name['TotalSupply']._options = None
    _QUERY.methods_by_name[
        'TotalSupply'
    ]._serialized_options = (
        b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/supply'
    )
    _QUERY.methods_by_name['SupplyOf']._options = None
    _QUERY.methods_by_name[
        'SupplyOf'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\002&\022$/cosmos/bank/v1beta1/supply/by_denom'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name[
        'Params'
    ]._serialized_options = (
        b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/params'
    )
    _QUERY.methods_by_name['DenomMetadata']._options = None
    _QUERY.methods_by_name[
        'DenomMetadata'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\002.\022,/cosmos/bank/v1beta1/denoms_metadata/{denom}'
    _QUERY.methods_by_name['DenomsMetadata']._options = None
    _QUERY.methods_by_name[
        'DenomsMetadata'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\002&\022$/cosmos/bank/v1beta1/denoms_metadata'
    _QUERY.methods_by_name['DenomOwners']._options = None
    _QUERY.methods_by_name[
        'DenomOwners'
    ]._serialized_options = b'\210\347\260*\001\202\323\344\223\002+\022)/cosmos/bank/v1beta1/denom_owners/{denom}'
    _QUERY.methods_by_name['SendEnabled']._options = None
    _QUERY.methods_by_name[
        'SendEnabled'
    ]._serialized_options = (
        b'\210\347\260*\001\202\323\344\223\002#\022!/cosmos/bank/v1beta1/send_enabled'
    )
    _globals['_QUERYBALANCEREQUEST']._serialized_start = 291
    _globals['_QUERYBALANCEREQUEST']._serialized_end = 396
    _globals['_QUERYBALANCERESPONSE']._serialized_start = 398
    _globals['_QUERYBALANCERESPONSE']._serialized_end = 473
    _globals['_QUERYALLBALANCESREQUEST']._serialized_start = 476
    _globals['_QUERYALLBALANCESREQUEST']._serialized_end = 635
    _globals['_QUERYALLBALANCESRESPONSE']._serialized_start = 638
    _globals['_QUERYALLBALANCESRESPONSE']._serialized_end = 847
    _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_start = 850
    _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_end = 1015
    _globals['_QUERYSPENDABLEBALANCESRESPONSE']._serialized_start = 1018
    _globals['_QUERYSPENDABLEBALANCESRESPONSE']._serialized_end = 1233
    _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST']._serialized_start = 1235
    _globals['_QUERYSPENDABLEBALANCEBYDENOMREQUEST']._serialized_end = 1356
    _globals['_QUERYSPENDABLEBALANCEBYDENOMRESPONSE']._serialized_start = 1358
    _globals['_QUERYSPENDABLEBALANCEBYDENOMRESPONSE']._serialized_end = 1449
    _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_start = 1451
    _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_end = 1558
    _globals['_QUERYTOTALSUPPLYRESPONSE']._serialized_start = 1561
    _globals['_QUERYTOTALSUPPLYRESPONSE']._serialized_end = 1766
    _globals['_QUERYSUPPLYOFREQUEST']._serialized_start = 1768
    _globals['_QUERYSUPPLYOFREQUEST']._serialized_end = 1812
    _globals['_QUERYSUPPLYOFRESPONSE']._serialized_start = 1814
    _globals['_QUERYSUPPLYOFRESPONSE']._serialized_end = 1899
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 1901
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 1921
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1923
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 2008
    _globals['_QUERYDENOMSMETADATAREQUEST']._serialized_start = 2010
    _globals['_QUERYDENOMSMETADATAREQUEST']._serialized_end = 2110
    _globals['_QUERYDENOMSMETADATARESPONSE']._serialized_start = 2113
    _globals['_QUERYDENOMSMETADATARESPONSE']._serialized_end = 2287
    _globals['_QUERYDENOMMETADATAREQUEST']._serialized_start = 2289
    _globals['_QUERYDENOMMETADATAREQUEST']._serialized_end = 2338
    _globals['_QUERYDENOMMETADATARESPONSE']._serialized_start = 2340
    _globals['_QUERYDENOMMETADATARESPONSE']._serialized_end = 2438
    _globals['_QUERYDENOMOWNERSREQUEST']._serialized_start = 2440
    _globals['_QUERYDENOMOWNERSREQUEST']._serialized_end = 2559
    _globals['_DENOMOWNER']._serialized_start = 2562
    _globals['_DENOMOWNER']._serialized_end = 2690
    _globals['_QUERYDENOMOWNERSRESPONSE']._serialized_start = 2693
    _globals['_QUERYDENOMOWNERSRESPONSE']._serialized_end = 2860
    _globals['_QUERYSENDENABLEDREQUEST']._serialized_start = 2862
    _globals['_QUERYSENDENABLEDREQUEST']._serialized_end = 2983
    _globals['_QUERYSENDENABLEDRESPONSE']._serialized_start = 2986
    _globals['_QUERYSENDENABLEDRESPONSE']._serialized_end = 3154
    _globals['_QUERY']._serialized_start = 3157
    _globals['_QUERY']._serialized_end = 4999
# @@protoc_insertion_point(module_scope)