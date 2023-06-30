def test_pkg_import():
    import nibiru_proto

    print("nibiru_proto directory", dir(nibiru_proto))
    import nibiru_proto.cosmos.bank
    import nibiru_proto.cosmos.auth
    import nibiru_proto.cosmos.tx
    import nibiru_proto.cosmos.gov
    import nibiru_proto.cosmos.staking
    import nibiru_proto.tendermint

    # imports for Nibi-Perps
    import nibiru_proto.nibiru.epochs
    import nibiru_proto.nibiru.inflation
    import nibiru_proto.nibiru.oracle
    import nibiru_proto.nibiru.perp
    import nibiru_proto.nibiru.spot
    import nibiru_proto.nibiru.stablecoin
    import nibiru_proto.nibiru.sudo

    print("imports succeeded")
