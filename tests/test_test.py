def test_pkg_import():
    import nibiru_proto

    print("nibiru_proto directory", dir(nibiru_proto))
    import nibiru_proto.proto.cosmos.auth
    import nibiru_proto.proto.cosmos.bank
    import nibiru_proto.proto.cosmos.gov
    import nibiru_proto.proto.cosmos.staking
    import nibiru_proto.proto.cosmos.tx
    import nibiru_proto.proto.epochs.v1
    import nibiru_proto.proto.oracle.v1

    # imports for Nibi-Perps
    import nibiru_proto.proto.perp.v2
    import nibiru_proto.proto.spot.v1
    import nibiru_proto.proto.tendermint

    print("imports succeeded")
