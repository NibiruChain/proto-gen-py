# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/spot/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import (
    pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2,
)
from nibiru.spot.v1 import params_pb2 as nibiru_dot_spot_dot_v1_dot_params__pb2
from nibiru.spot.v1 import pool_pb2 as nibiru_dot_spot_dot_v1_dot_pool__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1anibiru/spot/v1/query.proto\x12\x0enibiru.spot.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1bnibiru/spot/v1/params.proto\x1a\x19nibiru/spot/v1/pool.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x14\n\x12QueryParamsRequest\"K\n\x13QueryParamsResponse\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32\x16.nibiru.spot.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"\x18\n\x16QueryPoolNumberRequest\"2\n\x17QueryPoolNumberResponse\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"+\n\x10QueryPoolRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"=\n\x11QueryPoolResponse\x12(\n\x04pool\x18\x01 \x01(\x0b\x32\x14.nibiru.spot.v1.PoolR\x04pool\"[\n\x11QueryPoolsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x89\x01\n\x12QueryPoolsResponse\x12*\n\x05pools\x18\x01 \x03(\x0b\x32\x14.nibiru.spot.v1.PoolR\x05pools\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"1\n\x16QueryPoolParamsRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"V\n\x17QueryPoolParamsResponse\x12;\n\x0bpool_params\x18\x01 \x01(\x0b\x32\x1a.nibiru.spot.v1.PoolParamsR\npoolParams\"\x16\n\x14QueryNumPoolsRequest\"4\n\x15QueryNumPoolsResponse\x12\x1b\n\tnum_pools\x18\x01 \x01(\x04R\x08numPools\"\x1c\n\x1aQueryTotalLiquidityRequest\"\x9c\x01\n\x1bQueryTotalLiquidityResponse\x12}\n\tliquidity\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"liquidity\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\tliquidity\"9\n\x1eQueryTotalPoolLiquidityRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"\xa0\x01\n\x1fQueryTotalPoolLiquidityResponse\x12}\n\tliquidity\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"liquidity\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\tliquidity\"2\n\x17QueryTotalSharesRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"u\n\x18QueryTotalSharesResponse\x12Y\n\x0ctotal_shares\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"total_shares\"R\x0btotalShares\"~\n\x15QuerySpotPriceRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\x12$\n\x0etoken_in_denom\x18\x02 \x01(\tR\x0ctokenInDenom\x12&\n\x0ftoken_out_denom\x18\x03 \x01(\tR\rtokenOutDenom\"7\n\x16QuerySpotPriceResponse\x12\x1d\n\nspot_price\x18\x01 \x01(\tR\tspotPrice\"\xaf\x01\n\x1dQuerySwapExactAmountInRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\x12M\n\x08token_in\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"token_in\"R\x07tokenIn\x12&\n\x0ftoken_out_denom\x18\x03 \x01(\tR\rtokenOutDenom\"\xb3\x01\n\x1eQuerySwapExactAmountInResponse\x12P\n\ttoken_out\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"token_out\"R\x08tokenOut\x12?\n\x03\x66\x65\x65\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x12\xc8\xde\x1f\x00\xf2\xde\x1f\nyaml:\"fee\"R\x03\x66\x65\x65\"\xb1\x01\n\x1eQuerySwapExactAmountOutRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\x12P\n\ttoken_out\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"token_out\"R\x08tokenOut\x12$\n\x0etoken_in_denom\x18\x03 \x01(\tR\x0ctokenInDenom\"p\n\x1fQuerySwapExactAmountOutResponse\x12M\n\x08token_in\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"token_in\"R\x07tokenIn\"\xb6\x01\n\x1dQueryJoinExactAmountInRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\x12|\n\ttokens_in\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"tokens_in\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x08tokensIn\"\x90\x02\n\x1eQueryJoinExactAmountInResponse\x12p\n\x0fpool_shares_out\x18\x01 \x01(\tBH\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:\"pool_shares_out\"R\rpoolSharesOut\x12|\n\trem_coins\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"rem_coins\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x08remCoins\"9\n\x1eQueryJoinExactAmountOutRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"!\n\x1fQueryJoinExactAmountOutResponse\"\xa7\x01\n\x1dQueryExitExactAmountInRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\x12m\n\x0epool_shares_in\x18\x02 \x01(\tBG\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"pool_shares_in\"R\x0cpoolSharesIn\"\x91\x02\n\x1eQueryExitExactAmountInResponse\x12\x7f\n\ntokens_out\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBE\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:\"tokens_out\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\ttokensOut\x12n\n\x04\x66\x65\x65s\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB?\xc8\xde\x1f\x00\xf2\xde\x1f\x0byaml:\"fees\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x04\x66\x65\x65s\"9\n\x1eQueryExitExactAmountOutRequest\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"!\n\x1fQueryExitExactAmountOutResponse2\xa5\x13\n\x05Query\x12n\n\x06Params\x12\".nibiru.spot.v1.QueryParamsRequest\x1a#.nibiru.spot.v1.QueryParamsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/nibiru/spot/params\x12\x7f\n\nPoolNumber\x12&.nibiru.spot.v1.QueryPoolNumberRequest\x1a\'.nibiru.spot.v1.QueryPoolNumberResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/nibiru/spot/pool_number\x12\x66\n\x04Pool\x12 .nibiru.spot.v1.QueryPoolRequest\x1a!.nibiru.spot.v1.QueryPoolResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/nibiru/spot/pool\x12j\n\x05Pools\x12!.nibiru.spot.v1.QueryPoolsRequest\x1a\".nibiru.spot.v1.QueryPoolsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/nibiru/spot/pools\x12\x8a\x01\n\nPoolParams\x12&.nibiru.spot.v1.QueryPoolParamsRequest\x1a\'.nibiru.spot.v1.QueryPoolParamsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/nibiru/spot/pools/{pool_id}/params\x12w\n\x08NumPools\x12$.nibiru.spot.v1.QueryNumPoolsRequest\x1a%.nibiru.spot.v1.QueryNumPoolsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/nibiru/spot/num_pools\x12\x8f\x01\n\x0eTotalLiquidity\x12*.nibiru.spot.v1.QueryTotalLiquidityRequest\x1a+.nibiru.spot.v1.QueryTotalLiquidityResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/nibiru/spot/total_liquidity\x12\xb0\x01\n\x12TotalPoolLiquidity\x12..nibiru.spot.v1.QueryTotalPoolLiquidityRequest\x1a/.nibiru.spot.v1.QueryTotalPoolLiquidityResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/nibiru/spot/pools/{pool_id}/total_pool_liquidity\x12\x93\x01\n\x0bTotalShares\x12\'.nibiru.spot.v1.QueryTotalSharesRequest\x1a(.nibiru.spot.v1.QueryTotalSharesResponse\"1\x82\xd3\xe4\x93\x02+\x12)/nibiru/spot/pools/{pool_id}/total_shares\x12\x87\x01\n\tSpotPrice\x12%.nibiru.spot.v1.QuerySpotPriceRequest\x1a&.nibiru.spot.v1.QuerySpotPriceResponse\"+\x82\xd3\xe4\x93\x02%\x12#/nibiru/spot/pools/{pool_id}/prices\x12\xb8\x01\n\x19\x45stimateSwapExactAmountIn\x12-.nibiru.spot.v1.QuerySwapExactAmountInRequest\x1a..nibiru.spot.v1.QuerySwapExactAmountInResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/nibiru/spot/{pool_id}/estimate/swap_exact_amount_in\x12\xbc\x01\n\x1a\x45stimateSwapExactAmountOut\x12..nibiru.spot.v1.QuerySwapExactAmountOutRequest\x1a/.nibiru.spot.v1.QuerySwapExactAmountOutResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/nibiru/spot/{pool_id}/estimate/swap_exact_amount_out\x12\xb8\x01\n\x19\x45stimateJoinExactAmountIn\x12-.nibiru.spot.v1.QueryJoinExactAmountInRequest\x1a..nibiru.spot.v1.QueryJoinExactAmountInResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/nibiru/spot/{pool_id}/estimate/join_exact_amount_in\x12\xbc\x01\n\x1a\x45stimateJoinExactAmountOut\x12..nibiru.spot.v1.QueryJoinExactAmountOutRequest\x1a/.nibiru.spot.v1.QueryJoinExactAmountOutResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/nibiru/spot/{pool_id}/estimate/join_exact_amount_out\x12\xb8\x01\n\x19\x45stimateExitExactAmountIn\x12-.nibiru.spot.v1.QueryExitExactAmountInRequest\x1a..nibiru.spot.v1.QueryExitExactAmountInResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/nibiru/spot/{pool_id}/estimate/exit_exact_amount_in\x12\xbc\x01\n\x1a\x45stimateExitExactAmountOut\x12..nibiru.spot.v1.QueryExitExactAmountOutRequest\x1a/.nibiru.spot.v1.QueryExitExactAmountOutResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/nibiru/spot/{pool_id}/estimate/exit_exact_amount_outB,Z*github.com/NibiruChain/nibiru/x/spot/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'nibiru.spot.v1.query_pb2', _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/spot/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name[
        'params'
    ]._serialized_options = b'\310\336\037\000'
    _QUERYTOTALLIQUIDITYRESPONSE.fields_by_name['liquidity']._options = None
    _QUERYTOTALLIQUIDITYRESPONSE.fields_by_name[
        'liquidity'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"liquidity\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALPOOLLIQUIDITYRESPONSE.fields_by_name['liquidity']._options = None
    _QUERYTOTALPOOLLIQUIDITYRESPONSE.fields_by_name[
        'liquidity'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"liquidity\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALSHARESRESPONSE.fields_by_name['total_shares']._options = None
    _QUERYTOTALSHARESRESPONSE.fields_by_name[
        'total_shares'
    ]._serialized_options = b'\310\336\037\000\362\336\037\023yaml:\"total_shares\"'
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['token_in']._options = None
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name[
        'token_in'
    ]._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"token_in\"'
    _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name['token_out']._options = None
    _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name[
        'token_out'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"token_out\"'
    _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name['fee']._options = None
    _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name[
        'fee'
    ]._serialized_options = b'\310\336\037\000\362\336\037\nyaml:\"fee\"'
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['token_out']._options = None
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name[
        'token_out'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"token_out\"'
    _QUERYSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['token_in']._options = None
    _QUERYSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name[
        'token_in'
    ]._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"token_in\"'
    _QUERYJOINEXACTAMOUNTINREQUEST.fields_by_name['tokens_in']._options = None
    _QUERYJOINEXACTAMOUNTINREQUEST.fields_by_name[
        'tokens_in'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"tokens_in\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYJOINEXACTAMOUNTINRESPONSE.fields_by_name['pool_shares_out']._options = None
    _QUERYJOINEXACTAMOUNTINRESPONSE.fields_by_name[
        'pool_shares_out'
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\026yaml:\"pool_shares_out\"'
    _QUERYJOINEXACTAMOUNTINRESPONSE.fields_by_name['rem_coins']._options = None
    _QUERYJOINEXACTAMOUNTINRESPONSE.fields_by_name[
        'rem_coins'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"rem_coins\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYEXITEXACTAMOUNTINREQUEST.fields_by_name['pool_shares_in']._options = None
    _QUERYEXITEXACTAMOUNTINREQUEST.fields_by_name[
        'pool_shares_in'
    ]._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"pool_shares_in\"'
    _QUERYEXITEXACTAMOUNTINRESPONSE.fields_by_name['tokens_out']._options = None
    _QUERYEXITEXACTAMOUNTINRESPONSE.fields_by_name[
        'tokens_out'
    ]._serialized_options = b'\310\336\037\000\362\336\037\021yaml:\"tokens_out\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYEXITEXACTAMOUNTINRESPONSE.fields_by_name['fees']._options = None
    _QUERYEXITEXACTAMOUNTINRESPONSE.fields_by_name[
        'fees'
    ]._serialized_options = b'\310\336\037\000\362\336\037\013yaml:\"fees\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name[
        'Params'
    ]._serialized_options = b'\202\323\344\223\002\025\022\023/nibiru/spot/params'
    _QUERY.methods_by_name['PoolNumber']._options = None
    _QUERY.methods_by_name[
        'PoolNumber'
    ]._serialized_options = b'\202\323\344\223\002\032\022\030/nibiru/spot/pool_number'
    _QUERY.methods_by_name['Pool']._options = None
    _QUERY.methods_by_name[
        'Pool'
    ]._serialized_options = b'\202\323\344\223\002\023\022\021/nibiru/spot/pool'
    _QUERY.methods_by_name['Pools']._options = None
    _QUERY.methods_by_name[
        'Pools'
    ]._serialized_options = b'\202\323\344\223\002\024\022\022/nibiru/spot/pools'
    _QUERY.methods_by_name['PoolParams']._options = None
    _QUERY.methods_by_name[
        'PoolParams'
    ]._serialized_options = (
        b'\202\323\344\223\002%\022#/nibiru/spot/pools/{pool_id}/params'
    )
    _QUERY.methods_by_name['NumPools']._options = None
    _QUERY.methods_by_name[
        'NumPools'
    ]._serialized_options = b'\202\323\344\223\002\030\022\026/nibiru/spot/num_pools'
    _QUERY.methods_by_name['TotalLiquidity']._options = None
    _QUERY.methods_by_name[
        'TotalLiquidity'
    ]._serialized_options = (
        b'\202\323\344\223\002\036\022\034/nibiru/spot/total_liquidity'
    )
    _QUERY.methods_by_name['TotalPoolLiquidity']._options = None
    _QUERY.methods_by_name[
        'TotalPoolLiquidity'
    ]._serialized_options = (
        b'\202\323\344\223\0023\0221/nibiru/spot/pools/{pool_id}/total_pool_liquidity'
    )
    _QUERY.methods_by_name['TotalShares']._options = None
    _QUERY.methods_by_name[
        'TotalShares'
    ]._serialized_options = (
        b'\202\323\344\223\002+\022)/nibiru/spot/pools/{pool_id}/total_shares'
    )
    _QUERY.methods_by_name['SpotPrice']._options = None
    _QUERY.methods_by_name[
        'SpotPrice'
    ]._serialized_options = (
        b'\202\323\344\223\002%\022#/nibiru/spot/pools/{pool_id}/prices'
    )
    _QUERY.methods_by_name['EstimateSwapExactAmountIn']._options = None
    _QUERY.methods_by_name[
        'EstimateSwapExactAmountIn'
    ]._serialized_options = b'\202\323\344\223\0026\0224/nibiru/spot/{pool_id}/estimate/swap_exact_amount_in'
    _QUERY.methods_by_name['EstimateSwapExactAmountOut']._options = None
    _QUERY.methods_by_name[
        'EstimateSwapExactAmountOut'
    ]._serialized_options = b'\202\323\344\223\0027\0225/nibiru/spot/{pool_id}/estimate/swap_exact_amount_out'
    _QUERY.methods_by_name['EstimateJoinExactAmountIn']._options = None
    _QUERY.methods_by_name[
        'EstimateJoinExactAmountIn'
    ]._serialized_options = b'\202\323\344\223\0026\0224/nibiru/spot/{pool_id}/estimate/join_exact_amount_in'
    _QUERY.methods_by_name['EstimateJoinExactAmountOut']._options = None
    _QUERY.methods_by_name[
        'EstimateJoinExactAmountOut'
    ]._serialized_options = b'\202\323\344\223\0027\0225/nibiru/spot/{pool_id}/estimate/join_exact_amount_out'
    _QUERY.methods_by_name['EstimateExitExactAmountIn']._options = None
    _QUERY.methods_by_name[
        'EstimateExitExactAmountIn'
    ]._serialized_options = b'\202\323\344\223\0026\0224/nibiru/spot/{pool_id}/estimate/exit_exact_amount_in'
    _QUERY.methods_by_name['EstimateExitExactAmountOut']._options = None
    _QUERY.methods_by_name[
        'EstimateExitExactAmountOut'
    ]._serialized_options = b'\202\323\344\223\0027\0225/nibiru/spot/{pool_id}/estimate/exit_exact_amount_out'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 230
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 250
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 252
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 327
    _globals['_QUERYPOOLNUMBERREQUEST']._serialized_start = 329
    _globals['_QUERYPOOLNUMBERREQUEST']._serialized_end = 353
    _globals['_QUERYPOOLNUMBERRESPONSE']._serialized_start = 355
    _globals['_QUERYPOOLNUMBERRESPONSE']._serialized_end = 405
    _globals['_QUERYPOOLREQUEST']._serialized_start = 407
    _globals['_QUERYPOOLREQUEST']._serialized_end = 450
    _globals['_QUERYPOOLRESPONSE']._serialized_start = 452
    _globals['_QUERYPOOLRESPONSE']._serialized_end = 513
    _globals['_QUERYPOOLSREQUEST']._serialized_start = 515
    _globals['_QUERYPOOLSREQUEST']._serialized_end = 606
    _globals['_QUERYPOOLSRESPONSE']._serialized_start = 609
    _globals['_QUERYPOOLSRESPONSE']._serialized_end = 746
    _globals['_QUERYPOOLPARAMSREQUEST']._serialized_start = 748
    _globals['_QUERYPOOLPARAMSREQUEST']._serialized_end = 797
    _globals['_QUERYPOOLPARAMSRESPONSE']._serialized_start = 799
    _globals['_QUERYPOOLPARAMSRESPONSE']._serialized_end = 885
    _globals['_QUERYNUMPOOLSREQUEST']._serialized_start = 887
    _globals['_QUERYNUMPOOLSREQUEST']._serialized_end = 909
    _globals['_QUERYNUMPOOLSRESPONSE']._serialized_start = 911
    _globals['_QUERYNUMPOOLSRESPONSE']._serialized_end = 963
    _globals['_QUERYTOTALLIQUIDITYREQUEST']._serialized_start = 965
    _globals['_QUERYTOTALLIQUIDITYREQUEST']._serialized_end = 993
    _globals['_QUERYTOTALLIQUIDITYRESPONSE']._serialized_start = 996
    _globals['_QUERYTOTALLIQUIDITYRESPONSE']._serialized_end = 1152
    _globals['_QUERYTOTALPOOLLIQUIDITYREQUEST']._serialized_start = 1154
    _globals['_QUERYTOTALPOOLLIQUIDITYREQUEST']._serialized_end = 1211
    _globals['_QUERYTOTALPOOLLIQUIDITYRESPONSE']._serialized_start = 1214
    _globals['_QUERYTOTALPOOLLIQUIDITYRESPONSE']._serialized_end = 1374
    _globals['_QUERYTOTALSHARESREQUEST']._serialized_start = 1376
    _globals['_QUERYTOTALSHARESREQUEST']._serialized_end = 1426
    _globals['_QUERYTOTALSHARESRESPONSE']._serialized_start = 1428
    _globals['_QUERYTOTALSHARESRESPONSE']._serialized_end = 1545
    _globals['_QUERYSPOTPRICEREQUEST']._serialized_start = 1547
    _globals['_QUERYSPOTPRICEREQUEST']._serialized_end = 1673
    _globals['_QUERYSPOTPRICERESPONSE']._serialized_start = 1675
    _globals['_QUERYSPOTPRICERESPONSE']._serialized_end = 1730
    _globals['_QUERYSWAPEXACTAMOUNTINREQUEST']._serialized_start = 1733
    _globals['_QUERYSWAPEXACTAMOUNTINREQUEST']._serialized_end = 1908
    _globals['_QUERYSWAPEXACTAMOUNTINRESPONSE']._serialized_start = 1911
    _globals['_QUERYSWAPEXACTAMOUNTINRESPONSE']._serialized_end = 2090
    _globals['_QUERYSWAPEXACTAMOUNTOUTREQUEST']._serialized_start = 2093
    _globals['_QUERYSWAPEXACTAMOUNTOUTREQUEST']._serialized_end = 2270
    _globals['_QUERYSWAPEXACTAMOUNTOUTRESPONSE']._serialized_start = 2272
    _globals['_QUERYSWAPEXACTAMOUNTOUTRESPONSE']._serialized_end = 2384
    _globals['_QUERYJOINEXACTAMOUNTINREQUEST']._serialized_start = 2387
    _globals['_QUERYJOINEXACTAMOUNTINREQUEST']._serialized_end = 2569
    _globals['_QUERYJOINEXACTAMOUNTINRESPONSE']._serialized_start = 2572
    _globals['_QUERYJOINEXACTAMOUNTINRESPONSE']._serialized_end = 2844
    _globals['_QUERYJOINEXACTAMOUNTOUTREQUEST']._serialized_start = 2846
    _globals['_QUERYJOINEXACTAMOUNTOUTREQUEST']._serialized_end = 2903
    _globals['_QUERYJOINEXACTAMOUNTOUTRESPONSE']._serialized_start = 2905
    _globals['_QUERYJOINEXACTAMOUNTOUTRESPONSE']._serialized_end = 2938
    _globals['_QUERYEXITEXACTAMOUNTINREQUEST']._serialized_start = 2941
    _globals['_QUERYEXITEXACTAMOUNTINREQUEST']._serialized_end = 3108
    _globals['_QUERYEXITEXACTAMOUNTINRESPONSE']._serialized_start = 3111
    _globals['_QUERYEXITEXACTAMOUNTINRESPONSE']._serialized_end = 3384
    _globals['_QUERYEXITEXACTAMOUNTOUTREQUEST']._serialized_start = 3386
    _globals['_QUERYEXITEXACTAMOUNTOUTREQUEST']._serialized_end = 3443
    _globals['_QUERYEXITEXACTAMOUNTOUTRESPONSE']._serialized_start = 3445
    _globals['_QUERYEXITEXACTAMOUNTOUTRESPONSE']._serialized_end = 3478
    _globals['_QUERY']._serialized_start = 3481
    _globals['_QUERY']._serialized_end = 5950
# @@protoc_insertion_point(module_scope)
