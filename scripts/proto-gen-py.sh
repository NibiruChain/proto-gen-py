#!/usr/bin/env bash

set -e pipefail # see https://stackoverflow.com/a/68465418/13305627

# ------------------------------------------------ CONFIG
PKG_PATH="nibiru_proto"
# PKG_PROTO_SUBDIR="$PKG_PATH/proto"
PKG_PROTO_SUBDIR="$PKG_PATH"
nibiru_cosmos_sdk_version="v0.47.3"
nibiru_chain_version="realu/python-protos"
# nibiru_chain_version="v0.21.3"
# ------------------------------------------------

init_globals() {
  PY_SDK_PATH=$(pwd)
  cd ../nibiru
  NIBIRU_PATH=$(pwd)
  echo "PY_SDK_PATH: $PY_SDK_PATH"
  echo "NIBIRU_PATH: $NIBIRU_PATH"
}

init_globals

protoc_gen_gocosmos() {
  if ! grep "github.com/gogo/protobuf => github.com/regen-network/protobuf" go.mod &>/dev/null; then
    echo -e "\tPlease run this command from somewhere inside the cosmos-sdk folder."
    return 1
  fi

  # get protoc gocosmos plugin
  go get github.com/regen-network/cosmos-proto/protoc-gen-gocosmos@latest 2>/dev/null
  # get cosmos sdk from github
  go get github.com/cosmos/cosmos-sdk@$nibiru_cosmos_sdk_version 2>/dev/null
}

# Add PKG_PATH as dir if it doesn't exist.
clean() {
  cd $PY_SDK_PATH
  rm -rf ./proto/
  rm -rf ./nibiru/
  rm -rf $PKG_PATH
  mkdir $PKG_PATH
  echo > $PKG_PATH/__init__.py
}

copy_nibiru_protobuf_from_remote() {
  git clone --depth 1 --branch $nibiru_chain_version https://github.com/NibiruChain/nibiru.git
  cp -r ./nibiru/proto/ ./proto/
  cp ./nibiru/go.mod go.mod
  cp ./nibiru/go.sum go.sum
}

copy_nibiru_protobuf_from_local() {
  cd $NIBIRU_PATH # move to nibiru
  git checkout $nibiru_chain_version
  cd $PY_SDK_PATH         # move to py-sdk
  cp -r $NIBIRU_PATH/proto $PY_SDK_PATH
  cp $NIBIRU_PATH/go.mod $PY_SDK_PATH/go.mod
  cp $NIBIRU_PATH/go.sum $PY_SDK_PATH/go.sum
}

code_gen() {
  echo "grabbing cosmos-sdk proto file locations from disk"
  echo "current dir: $(pwd)"

  # cd ./nibiru
  protoc_gen_gocosmos
  cosmos_sdk_dir=$(go list -f '{{ .Dir }}' -m github.com/cosmos/cosmos-sdk)
  cd $PY_SDK_PATH

  echo "grab all of the proto directories"
  echo "current dir: $(pwd)"
  # proto_dirs=$(find $cosmos_sdk_dir/proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
  # proto_dirs=$(find $cosmos_sdk_dir/proto ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
 
  
  # proto_dirs=$(printf "$cosmos_sdk_dir/proto/amino\n$cosmos_sdk_dir/proto/cosmos\n$cosmos_sdk_dir/proto/tendermint")
  # proto_dirs=$(printf "$cosmos_sdk_dir/proto")
  proto_dirs=()
  proto_dirs+=("$cosmos_sdk_dir/proto")
  proto_dirs+=("$NIBIRU_PATH/proto")

  echo "Proto Directories: "
  echo $proto_dirs

  # generate the protos for each directory
  for proto_dir in "${proto_dirs[@]}"; do
    string=$proto_dir
    prefix=$HOME/go/pkg/mod/github.com/
    prefix_removed_string=${string/#$prefix/}
    echo "------------ generating $prefix_removed_string ------------"
    # echo "$cosmos_sdk_dir"
    mkdir -p $PY_SDK_PATH/$PKG_PATH/${proto_dir}

    echo "NIBIRU_PATH: $NIBIRU_PATH"
    local out_dir=$PY_SDK_PATH/$PKG_PATH
    echo "out_dir: $out_dir"
    # TODO: check if buf is installed and tell the user to get it if not.
    buf generate $proto_dir --template $NIBIRU_PATH/proto/buf.gen.py.yaml -o $out_dir

  done
}

# ------------------------------------------------
# __main__ : Start of script execution
# ------------------------------------------------


main() {
  clean

  # copy_nibiru_protobuf_from_remote
  copy_nibiru_protobuf_from_local

  code_gen

  printf "import os\nimport sys\n\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" >$PKG_PROTO_SUBDIR/__init__.py
  echo "Complete - generated Python types from proto"

  echo "final cleanup..."
  cd $PY_SDK_PATH
  # -z "$var" to check for empty
  # -n "$var" to check for not empty
  if [ -n "$PY_SDK_PATH" ]; then  
    rm -rf $PY_SDK_PATH/$PKG_PATH/home
    rm go.mod go.sum
  fi

  poetry run pytest
}

if main; then 
  echo "🔥 Generated Python proto types successfully. "
else 
  echo "❌ Generation failed."
fi
