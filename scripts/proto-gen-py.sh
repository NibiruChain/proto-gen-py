#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

OUT_DIR="nibiru_proto"
NIBIRU_PROTO="nibiru/proto"

rm -rf OUT_DIR
mkdir -p "$OUT_DIR"
nibiru_cosmos_sdk_version=v0.45.10

cd nibiru
go get github.com/regen-network/cosmos-proto/protoc-gen-gocosmos@latest 2>/dev/null
go get github.com/cosmos/cosmos-sdk@$nibiru_cosmos_sdk_version 2>/dev/null
cosmos_sdk_dir=$(go list -f '{{ .Dir }}' -m github.com/cosmos/cosmos-sdk)

cd ..
proto_dirs=$(find $cosmos_sdk_dir/proto $cosmos_sdk_dir/third_party/proto nibiru/proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)

echo "Processing nibiru proto files ..."

cd nibiru

python -m grpc_tools.protoc \
  --proto_path $cosmos_sdk_dir/proto \
  --proto_path $cosmos_sdk_dir/third_party/proto \
  --proto_path proto \
  --python_betterproto_out=../${OUT_DIR} \
  --mypy_out=../${OUT_DIR} \
  $(find $cosmos_sdk_dir/proto $cosmos_sdk_dir/third_party/proto proto -path -prune -o -name '*.proto' -print0 | xargs -0)
