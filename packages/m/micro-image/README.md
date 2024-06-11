# openSUSE Tumbleweed BCI Micro: Suitable for deploying static binaries
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description
This image is similar to Minimal but without the RPM package manager.
The primary use case for the image is deploying static binaries produced
externally or during multi-stage builds. As there is no straightforward
way to install additional dependencies inside the container image,
we recommend deploying a project using the Minimal image only
when the final build artifact bundles all dependencies and has no
external runtime requirements (like Python or Ruby).

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
