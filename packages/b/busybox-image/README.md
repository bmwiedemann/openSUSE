# openSUSE Tumbleweed BCI BusyBox: the smallest and GPLv3-free image
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description
This image comes with the most basic tools provided by the BusyBox project.
The image contains no GPLv3 licensed software. When using the image, keep in mind that
there are differences between the BusyBox tools and the GNU Coreutils.
This means that scripts written for a system that uses GNU Coreutils may require
modification to work with BusyBox. If you need a SLES compatible image with the GNU Coreutils,
consider using the corresponding Micro image instead.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
