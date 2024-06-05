# openSUSE Tumbleweed BCI Minimal: Base Container image without Zypper
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)


## Description
This image comes without Zypper, but it does have the RPM package manager installed.
While RPM can install and remove packages, it lacks support for repositories and automated dependency resolution.
It is therefore intended for creating deployment containers, and then installing the desired
RPM packages inside the containers.

While you can install the required dependencies, you need to download and resolve them manually.
However, this approach is not recommended as it is prone to errors.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
