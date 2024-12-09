# KIWI Appliance Builder (kiwi) container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

[KIWI NG](https://osinside.github.io/kiwi/) is a command-line utility for
building Linux system appliances. An appliance is a ready to use image of an
operating system that includes a pre-configured application for a specific
use case. The appliance is provided as an image file and needs to be deployed
to or activated in the target system or service.

KIWI NG can create different types of appliances. In addition to the standard
installation ISOs and images for virtual machines, KIWI NG can also build
images that boot via PXE or Vagrant boxes.

## Usage

To build a system image, you need to create a KIWI image description and
mount it into your container.
[The KIWI image description](https://osinside.github.io/kiwi/image_description.html)
is a collection of human-readable files stored in a directory. Provide at
least one XML file named `config.xml` or `*.kiwi`. There can be other files
like scripts or configuration files.

To build a KIWI NG appliance, launch the container in privileged mode:

```ShellSession
$ podman run --privileged -v /path/to/kiwi/descr:/image:Z registry.opensuse.org/opensuse/bci/kiwi:10.2
```

For more information about KIWI NG, see the [KIWI NG documentation](https://osinside.github.io/kiwi/),
specifically the [Getting Started Guide](https://osinside.github.io/kiwi/quickstart.html).


## Licensing

`SPDX-License-Identifier: GPL-3.0-or-later`

This documentation and the build recipe are licensed as GPL-3.0-or-later.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
