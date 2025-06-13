# Samba Client Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

Samba is a feature-rich Open Source implementation of the SMB and Active Directory protocols for Linux and UNIX-like systems.

This image contains the Samba client.

## Usage

To connect to a SMB file server, run the following command:

```ShellSession
$ podman run -it --rm registry.opensuse.org/opensuse/samba-client:4.22 smbclient //SERVER/SHARE -U "DOMAIN\\username"
```

## Licensing

`SPDX-License-Identifier: GPL-3.0-or-later`

This documentation and the build recipe are licensed as GPL-3.0-or-later.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
