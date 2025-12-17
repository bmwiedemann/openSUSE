# Samba Toolbox Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

Samba is a feature-rich open source implementation of the SMB and Active Directory protocols for Linux and UNIX-like systems.

This image comes with Samba tools and TDB tools.

## Usage

To check the available shares in a SMB file server, run the following command:

```ShellSession
$ podman run -it --rm registry.opensuse.org/opensuse/samba-toolbox:4.22 smbclient -L //SERVER/SHARE -U "DOMAIN\\username"
```

To check the available shares anonymously in a SMB file server, run the following command:

```ShellSession
$ podman run -it --rm registry.opensuse.org/opensuse/samba-toolbox:4.22 smbclient -L //SERVER/SHARE -N
```

To list all Samba users in the Samba database, run the following command:

```ShellSession
$ podman run -it --rm -v /path/to/samba/data:/var/lib/samba registry.opensuse.org/opensuse/samba-toolbox:4.22 pdbedit -L
```

To print all records in the Samba secrets database, run the following command:

```ShellSession
$ podman run -it --rm -v /path/to/samba/data:/var/lib/samba registry.opensuse.org/opensuse/samba-toolbox:4.22 tdbdump /var/lib/samba/private/secrets.tdb
```

## Licensing

`SPDX-License-Identifier: GPL-3.0-or-later`

This documentation and the build recipe are licensed as GPL-3.0-or-later.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
