def test_pkg_import():
    import nibiru_proto
    print("nibiru_proto directory", dir(nibiru_proto))

    # imports for Nibi-Perps
    import nibiru_proto.nibiru.epochs
    import nibiru_proto.nibiru.inflation
    import nibiru_proto.nibiru.oracle
    import nibiru_proto.nibiru.perp
    import nibiru_proto.nibiru.spot
    import nibiru_proto.nibiru.stablecoin
    import nibiru_proto.nibiru.sudo
    print("imports succeeded")


def test_grpc_imports():
    import nibiru_proto.nibiru.epochs.v1.state_pb2_grpc
    import nibiru_proto.nibiru.epochs.v1.query_pb2_grpc
    assert nibiru_proto.nibiru.epochs.v1.query_pb2_grpc.QueryStub

    import nibiru_proto.nibiru.inflation.v1.query_pb2_grpc
    import nibiru_proto.nibiru.inflation.v1.inflation_pb2_grpc
    assert nibiru_proto.nibiru.inflation.v1.query_pb2_grpc.QueryStub

    import nibiru_proto.nibiru.oracle.v1.query_pb2_grpc
    import nibiru_proto.nibiru.oracle.v1.tx_pb2_grpc
    assert nibiru_proto.nibiru.oracle.v1.query_pb2_grpc.QueryStub

    import nibiru_proto.nibiru.perp.v2.tx_pb2_grpc
    import nibiru_proto.nibiru.perp.v2.query_pb2_grpc
    assert nibiru_proto.nibiru.perp.v2.query_pb2_grpc.QueryStub

    import nibiru_proto.nibiru.spot.v1.tx_pb2_grpc
    import nibiru_proto.nibiru.spot.v1.query_pb2_grpc
    assert nibiru_proto.nibiru.spot.v1.query_pb2_grpc.QueryStub

    import nibiru_proto.nibiru.stablecoin.v1.tx_pb2_grpc
    import nibiru_proto.nibiru.stablecoin.v1.query_pb2_grpc
    assert nibiru_proto.nibiru.stablecoin.v1.query_pb2_grpc.QueryStub

    import nibiru_proto.nibiru.sudo.v1.tx_pb2_grpc
    import nibiru_proto.nibiru.sudo.v1.query_pb2_grpc
    assert nibiru_proto.nibiru.sudo.v1.query_pb2_grpc.QueryStub


def test_cosmos_imports():
    import nibiru_proto.cosmos.bank
    import nibiru_proto.cosmos.auth
    import nibiru_proto.cosmos.tx
    import nibiru_proto.cosmos.gov
    import nibiru_proto.cosmos.staking
    import nibiru_proto.tendermint


def test_cosmos_subdir_imports():
    from nibiru_proto.cosmos.tx.v1beta1 import tx_pb2
    from nibiru_proto.cosmos.tx.v1beta1 import service_pb2
    from nibiru_proto.cosmos.base.tendermint.v1beta1 import (
        query_pb2 as tendermint_query,
    )

    from nibiru_proto.cosmos.bank.v1beta1 import tx_pb2
    from nibiru_proto.cosmos.distribution.v1beta1 import tx_pb2
    from nibiru_proto.cosmos.distribution.v1beta1 import distribution_pb2
