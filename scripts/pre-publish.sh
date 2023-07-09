#!/usr/bin/env bash
set -e

# assert attempts to run an arbitrary command and errors out of the script otherwise.
assert() {
  local arg_cmd="$@"
  echo "arg_cmd: $arg_cmd"

  if ! $arg_cmd ; then
    echo "Failed to execute command: $arg_cmd"
    exit 1
  fi
}

# check_bash_deps accepts a sequence of strings as an argument and calls "which" to 
# see if those commands can be located. It returns exit code 0 if all commands can be 
# found and 1 if any of them cannot.
check_bash_deps() {
  local tools=("$@")
  local tools_installed=()
  local ok_code="0"

  for tool in "${tools[@]}"; do
    if ! which "$tool" >/dev/null 2>&1; then
      echo "Error ❌: $tool is not installed."
      ok_code="1"
    else 
      tools_installed+=("$tool")
    fi
  done 

  echo "Successfully found deps: ${tools_installed[@]}"
  return $ok_code
}

poetry_cmds() {
  poetry install
  poetry run black .
  poetry run isort
  poetry run pytest
}

check_bash_deps poetry
assert poetry_cmds
