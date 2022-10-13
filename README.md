# sdk-proto-gen

Generates the `nibiru_proto` Python package for the [Nibiru Python SDK][repo-py-sdk].

<!-- Badges -->
[![][discord-badge]][discord-url]
[![PyPI Version][pypi-image]][pypi-url]
[![MIT license][license-badge]][license-link]

## Python Code Generation 

All you need to do is run:
```sh
make proto-gen
```
This executes the code generation script, [proto-gen-py.sh][script-proto-gen].

The protobuf files come from the [NibiruChain/nibiru repo][repo-nibiru], which is private (for now), so you'll need these files on your local machine. It's assumed you have the `nibiru` repo as a neighbor to `sdk-proto-gen` when running the code generation script.

## Other Development Guidelines

Our recommended Python setup is to use `pyenv` in combination with `poetry`.

- `pyenv` is a tool for installing and managing Python interpreters. This will let you seamlessly switch between Python versions.
- `poetry` is used for managing virtual environments, dependency resolution, package installations, package building, and package publishing.
- We assume you're on a Unix machine such as WSL2 Ubuntu, MacOS, or a common Linux distro.

See [NibiruChain/py-sdk][repo-py-sdk] for installation instructions.

## Testing

```sh
poetry install
poetry run pytest
```

## Publishing to PyPI

The publish workflow looks like this:

1. Code-gen the new types from the chain. If there are changes, these should be committed.
   ```sh
   make proto-gen
   ```
2. Increment the package version. For example, use `poetry version preminor` to do a pre-release for a minor version.
   ```sh
   poetry version [update-keyword]
   ```
3. Create a build for the wheel and source code.
   ```sh
   poetry build
   ```
4. Put your PyPI credentials into the `.env` file. Then, use the `dotenv` CLI tool from `npm` to pass variables from the `.env` into the `poetry publish` command.
   ```sh
   dotenv -e .env poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
   ```

## 🔓 License

This software is licensed under the MIT license. See [LICENSE](./LICENSE) for full disclosure.

© 2022 Nibi, Inc.

<p align="center">
<img src="https://cdn-images-1.medium.com/max/2400/1*ZHWKH2guuV6JL8_mdCbtLQ.png" width="800">
</p>

[repo-nibiru]: https://github.com/NibiruChain/nibiru
[repo-py-sdk]: https://github.com/NibiruChain/py-sdk
[script-proto-gen]: https://github.com/NibiruChain/sdk-proto-gen/blob/main/scripts/proto-gen-py.sh

<!-- Badges links -->
[pypi-image]: https://img.shields.io/pypi/v/nibiru-proto
[pypi-url]: https://pypi.org/project/nibiru-proto/
[discord-badge]: https://img.shields.io/badge/Nibiru%20Chain-%237289DA.svg?style=&logo=discord&logoColor=white
[discord-url]: https://discord.gg/sgPw8ZYfpQ
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/NibiruChain/sdk-proto-gen/blob/master/LICENSE