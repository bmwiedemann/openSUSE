# The openSUSE Tumbleweed Opencode sandbox container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

This image provides a sandbox for [Opencode](https://opencode.ai), running as a
non-root `sandbox` user (uid `1000`). Use `/workspace` as the volume mount point
for files that AI should have access to.

The image is published in two flavors:

| Flavor  | Description                                                      |
| ------- | ---------------------------------------------------------------- |
| `base`  | The hardened runtime image, with `opencode` and basic tools.     |
| `devel` | The development image, that can be extended with source tooling. |

Some features are disabled by default.
See [disabled features](#disabled-features) section.

## Usage

To start opencode and give AI access to files in current directory use:

```Shell
podman run --rm -it \
    --userns=keep-id:uid=1000 \
    -v $HOME/.cache/opencode:/home/sandbox/.cache/opencode:Z \
    -v $HOME/.config/opencode:/home/sandbox/.config/opencode:Z \
    -v $HOME/.local/share/opencode:/home/sandbox/.local/share/opencode:Z \
    -v $PWD:/workspace:Z \
    registry.opensuse.org/opensuse/opencode:base
```

## Disabled features

Syntax highlighting, formatters, LSP integrations, provider SDKs and self update
are disabled out of the box. To enable desired features set environment
variables outlined below:

- `OPENCODE_ALLOW_GRAMMAR_DOWNLOAD=1` - Allow opencode to download grammar files
  (language definitions used for syntax highlighting and templating).
- `OPENCODE_ALLOW_NPM_INSTALL=1` - Allow the installation of formatters,
  LSP integrations and provider SDKs using npm.
- `OPENCODE_ENABLE_AUTOUPDATE=1` - Enable opencode's automatic update checker.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
