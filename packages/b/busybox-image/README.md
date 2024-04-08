# SLE BCI-BusyBox: the smallest and GPLv3-free image

The SLE BCI-BusyBox image comes with the most basic tools provided by the BusyBox project. The image contains no GPLv3 licensed software. When using the image, keep in mind that there are differences between the BusyBox tools and the GNU Coreutils. This means that scripts written for a system that uses GNU Coreutils may require modification to work with BusyBox.

## Licensing
`SPDX-License-Identifier: MIT`

The build recipe and this documentation is licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
