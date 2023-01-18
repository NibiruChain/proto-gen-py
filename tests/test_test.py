def test_pkg_import():
    import nibiru_proto

    print("nibiru_proto directory", dir(nibiru_proto))
    import nibiru_proto.proto.common.common_pb2
    import nibiru_proto.proto.cosmos.bank
    import nibiru_proto.proto.cosmos.auth
    import nibiru_proto.proto.cosmos.tx
    import nibiru_proto.proto.cosmos.gov
    import nibiru_proto.proto.cosmos.staking
    import nibiru_proto.proto.tendermint

    # imports for Nibi-Perps
    import nibiru_proto.proto.perp
    import nibiru_proto.proto.vpool
    import nibiru_proto.proto.dex
    import nibiru_proto.proto.epochs
    import nibiru_proto.proto.oracle

    print("imports succeeded")
