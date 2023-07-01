# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nibiru/spot/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nibiru.spot.v1 import pool_pb2 as nibiru_dot_spot_dot_v1_dot_pool__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17nibiru/spot/v1/tx.proto\x12\x0enibiru.spot.v1\x1a\x19nibiru/spot/v1/pool.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1cgoogle/api/annotations.proto\"\xc0\x01\n\rMsgCreatePool\x12\x18\n\x07\x63reator\x18\x01 \x01(\tR\x07\x63reator\x12S\n\x0bpool_params\x18\x02 \x01(\x0b\x32\x1a.nibiru.spot.v1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:\"pool_params\"R\npoolParams\x12@\n\x0bpool_assets\x18\x03 \x03(\x0b\x32\x19.nibiru.spot.v1.PoolAssetB\x04\xc8\xde\x1f\x00R\npoolAssets\"0\n\x15MsgCreatePoolResponse\x12\x17\n\x07pool_id\x18\x01 \x01(\x04R\x06poolId\"\xf5\x01\n\x0bMsgJoinPool\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12+\n\x07pool_id\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"R\x06poolId\x12P\n\ttokens_in\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"tokens_in\"R\x08tokensIn\x12<\n\ruse_all_coins\x18\x04 \x01(\x08\x42\x18\xf2\xde\x1f\x14yaml:\"use_all_coins\"R\x0buseAllCoins\"\x8b\x02\n\x13MsgJoinPoolResponse\x12(\n\x04pool\x18\x01 \x01(\x0b\x32\x14.nibiru.spot.v1.PoolR\x04pool\x12l\n\x13num_pool_shares_out\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:\"num_pool_shares_out\"R\x10numPoolSharesOut\x12\\\n\x0fremaining_coins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"tokens_in\"R\x0eremainingCoins\"\xbd\x01\n\x0bMsgExitPool\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12+\n\x07pool_id\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"R\x06poolId\x12V\n\x0bpool_shares\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:\"pool_shares\"R\npoolShares\"j\n\x13MsgExitPoolResponse\x12S\n\ntokens_out\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x19\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:\"tokens_out\"R\ttokensOut\"\xfa\x01\n\rMsgSwapAssets\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12+\n\x07pool_id\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"R\x06poolId\x12M\n\x08token_in\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"token_in\"R\x07tokenIn\x12\x42\n\x0ftoken_out_denom\x18\x04 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"token_out_denom\"R\rtokenOutDenom\"i\n\x15MsgSwapAssetsResponse\x12P\n\ttoken_out\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"token_out\"R\x08tokenOut2\xd3\x03\n\x03Msg\x12m\n\nCreatePool\x12\x1d.nibiru.spot.v1.MsgCreatePool\x1a%.nibiru.spot.v1.MsgCreatePoolResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/nibiru/spot/pool\x12q\n\x08JoinPool\x12\x1b.nibiru.spot.v1.MsgJoinPool\x1a#.nibiru.spot.v1.MsgJoinPoolResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/nibiru/spot/{pool_id}/join\x12q\n\x08\x45xitPool\x12\x1b.nibiru.spot.v1.MsgExitPool\x1a#.nibiru.spot.v1.MsgExitPoolResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/nibiru/spot/{pool_id}/exit\x12w\n\nSwapAssets\x12\x1d.nibiru.spot.v1.MsgSwapAssets\x1a%.nibiru.spot.v1.MsgSwapAssetsResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/nibiru/spot/{pool_id}/swapB,Z*github.com/NibiruChain/nibiru/x/spot/typesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nibiru.spot.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/spot/types'
    _MSGCREATEPOOL.fields_by_name['pool_params']._options = None
    _MSGCREATEPOOL.fields_by_name[
        'pool_params'
    ]._serialized_options = b'\362\336\037\022yaml:\"pool_params\"'
    _MSGCREATEPOOL.fields_by_name['pool_assets']._options = None
    _MSGCREATEPOOL.fields_by_name[
        'pool_assets'
    ]._serialized_options = b'\310\336\037\000'
    _MSGJOINPOOL.fields_by_name['sender']._options = None
    _MSGJOINPOOL.fields_by_name[
        'sender'
    ]._serialized_options = b'\362\336\037\ryaml:\"sender\"'
    _MSGJOINPOOL.fields_by_name['pool_id']._options = None
    _MSGJOINPOOL.fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _MSGJOINPOOL.fields_by_name['tokens_in']._options = None
    _MSGJOINPOOL.fields_by_name[
        'tokens_in'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"tokens_in\"'
    _MSGJOINPOOL.fields_by_name['use_all_coins']._options = None
    _MSGJOINPOOL.fields_by_name[
        'use_all_coins'
    ]._serialized_options = b'\362\336\037\024yaml:\"use_all_coins\"'
    _MSGJOINPOOLRESPONSE.fields_by_name['num_pool_shares_out']._options = None
    _MSGJOINPOOLRESPONSE.fields_by_name[
        'num_pool_shares_out'
    ]._serialized_options = (
        b'\310\336\037\000\362\336\037\032yaml:\"num_pool_shares_out\"'
    )
    _MSGJOINPOOLRESPONSE.fields_by_name['remaining_coins']._options = None
    _MSGJOINPOOLRESPONSE.fields_by_name[
        'remaining_coins'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"tokens_in\"'
    _MSGEXITPOOL.fields_by_name['sender']._options = None
    _MSGEXITPOOL.fields_by_name[
        'sender'
    ]._serialized_options = b'\362\336\037\ryaml:\"sender\"'
    _MSGEXITPOOL.fields_by_name['pool_id']._options = None
    _MSGEXITPOOL.fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _MSGEXITPOOL.fields_by_name['pool_shares']._options = None
    _MSGEXITPOOL.fields_by_name[
        'pool_shares'
    ]._serialized_options = b'\310\336\037\000\362\336\037\022yaml:\"pool_shares\"'
    _MSGEXITPOOLRESPONSE.fields_by_name['tokens_out']._options = None
    _MSGEXITPOOLRESPONSE.fields_by_name[
        'tokens_out'
    ]._serialized_options = b'\310\336\037\000\362\336\037\021yaml:\"tokens_out\"'
    _MSGSWAPASSETS.fields_by_name['sender']._options = None
    _MSGSWAPASSETS.fields_by_name[
        'sender'
    ]._serialized_options = b'\362\336\037\ryaml:\"sender\"'
    _MSGSWAPASSETS.fields_by_name['pool_id']._options = None
    _MSGSWAPASSETS.fields_by_name[
        'pool_id'
    ]._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
    _MSGSWAPASSETS.fields_by_name['token_in']._options = None
    _MSGSWAPASSETS.fields_by_name[
        'token_in'
    ]._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"token_in\"'
    _MSGSWAPASSETS.fields_by_name['token_out_denom']._options = None
    _MSGSWAPASSETS.fields_by_name[
        'token_out_denom'
    ]._serialized_options = b'\362\336\037\026yaml:\"token_out_denom\"'
    _MSGSWAPASSETSRESPONSE.fields_by_name['token_out']._options = None
    _MSGSWAPASSETSRESPONSE.fields_by_name[
        'token_out'
    ]._serialized_options = b'\310\336\037\000\362\336\037\020yaml:\"token_out\"'
    _MSG.methods_by_name['CreatePool']._options = None
    _MSG.methods_by_name[
        'CreatePool'
    ]._serialized_options = b'\202\323\344\223\002\023\"\021/nibiru/spot/pool'
    _MSG.methods_by_name['JoinPool']._options = None
    _MSG.methods_by_name[
        'JoinPool'
    ]._serialized_options = b'\202\323\344\223\002\035\"\033/nibiru/spot/{pool_id}/join'
    _MSG.methods_by_name['ExitPool']._options = None
    _MSG.methods_by_name[
        'ExitPool'
    ]._serialized_options = b'\202\323\344\223\002\035\"\033/nibiru/spot/{pool_id}/exit'
    _MSG.methods_by_name['SwapAssets']._options = None
    _MSG.methods_by_name[
        'SwapAssets'
    ]._serialized_options = b'\202\323\344\223\002\035\"\033/nibiru/spot/{pool_id}/swap'
    _globals['_MSGCREATEPOOL']._serialized_start = 155
    _globals['_MSGCREATEPOOL']._serialized_end = 347
    _globals['_MSGCREATEPOOLRESPONSE']._serialized_start = 349
    _globals['_MSGCREATEPOOLRESPONSE']._serialized_end = 397
    _globals['_MSGJOINPOOL']._serialized_start = 400
    _globals['_MSGJOINPOOL']._serialized_end = 645
    _globals['_MSGJOINPOOLRESPONSE']._serialized_start = 648
    _globals['_MSGJOINPOOLRESPONSE']._serialized_end = 915
    _globals['_MSGEXITPOOL']._serialized_start = 918
    _globals['_MSGEXITPOOL']._serialized_end = 1107
    _globals['_MSGEXITPOOLRESPONSE']._serialized_start = 1109
    _globals['_MSGEXITPOOLRESPONSE']._serialized_end = 1215
    _globals['_MSGSWAPASSETS']._serialized_start = 1218
    _globals['_MSGSWAPASSETS']._serialized_end = 1468
    _globals['_MSGSWAPASSETSRESPONSE']._serialized_start = 1470
    _globals['_MSGSWAPASSETSRESPONSE']._serialized_end = 1575
    _globals['_MSG']._serialized_start = 1578
    _globals['_MSG']._serialized_end = 2045
# @@protoc_insertion_point(module_scope)
