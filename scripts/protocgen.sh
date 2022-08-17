#!/usr/bin/env bash
# pip install mypy-protobuf grpcio-tools

set -eo pipefail

protoc_gen_gocosmos() {
  if ! grep "github.com/gogo/protobuf => github.com/regen-network/protobuf" go.mod &>/dev/null; then
    echo -e "\tPlease run this command from somewhere inside the cosmos-sdk folder."
    return 1
  fi

  # get protoc executions
  go get github.com/regen-network/cosmos-proto/protoc-gen-gocosmos@latest 2>/dev/null
  # get cosmos sdk from github
  go get github.com/cosmos/cosmos-sdk@v0.45.6 2>/dev/null
}

PKG_PATH="nibiru_proto"
PKG_PROTO_SUBDIR="$PKG_PATH/proto"

echo > $PKG_PATH/__init__.py

echo "Refreshing proto files"
if [ $(basename $(pwd)) = sdk-proto-gen ]
then
  echo "Refreshing proto files"
  rm -rf $PKG_PROTO_SUBDIR # if the nibiru_proto directory already exists,
else
  echo "Ran protocgen.sh from the wrong directory"
  exit 1
fi

echo "grabbing cosmos-sdk proto file locations from disk"
echo "current dir: $(pwd)"
cd ../nibiru;
protoc_gen_gocosmos
cosmos_sdk_dir=$(go list -f '{{ .Dir }}' -m github.com/cosmos/cosmos-sdk)

echo "grab all of the proto directories"
echo "current dir: $(pwd)"
cd -;
proto_dirs=$(find $cosmos_sdk_dir/proto $cosmos_sdk_dir/third_party/proto ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
echo "Proto Directories: "
echo $proto_dirs

# generate the protos for each directory
for dir in $proto_dirs; do \
  string=dir
  prefix=$HOME/go/pkg/mod/github/
  prefix_removed_string=${string/#$prefix}
  echo "------------ generating $prefix_removed_string ------------" 
  # echo "$cosmos_sdk_dir"
  mkdir -p ./$PKG_PATH/${dir};
  python -m grpc_tools.protoc \
    -I proto \
    -I "$cosmos_sdk_dir/third_party/proto" \
    -I "$cosmos_sdk_dir/proto" \
    --python_out=$PKG_PROTO_SUBDIR \
    --grpc_python_out=$PKG_PROTO_SUBDIR \
    --mypy_out=$PKG_PROTO_SUBDIR \
    --mypy_grpc_out=$PKG_PROTO_SUBDIR \
    $(find "${dir}" -type f -name '*.proto')
done; \

printf "import os\nimport sys\n\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" > $PKG_PROTO_SUBDIR/__init__.py

echo "Complete - successfully generated Python types from proto"