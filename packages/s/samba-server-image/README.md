# Samba Server Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

Samba is a feature-rich open source implementation of the SMB and Active Directory
protocols for Linux and UNIX-like systems.

Samba is a high-performance, scalable distributed software platform for providing access to
various cluster file systems. It enables cloud platform-as-a-service (PaaS) providers,
software-defined storage (SDS) solutions, high-performance computing (HPC) applications,
and enterprise-grade network attached storage (NAS) to support the latest security and
SMB capabilities.

## Usage

By default, the image launches with no shares enabled, uses the `tdbsam` backend, and local user accounts.

To create a home directory for each user and a public share, you can use the example below for `smb.conf`:

```
[global]
	workgroup = WORKGROUP
	passdb backend = tdbsam
	load printers = No
	map to guest = Bad User
	guest account = nobody
	usershare allow guests = Yes

[homes]
	comment = Home Directories
	path = /shares/users/%U
	guest ok = No
	browseable = No
	read only = No
	inherit acls = Yes
	create mask = 0600
	directory mask = 0700
	valid users = %S
	invalid users = root nobody noguest

[public]
	comment = Public files
	path = /shares/public
	guest ok = Yes
	browseable = Yes
	read only = No
	inherit acls = Yes
	create mask = 0664
	directory mask = 0775
```

To run the container, use the following command:

```ShellSession
$ podman run -it --rm -p 5445:445 \
             -v /path/to/smb.conf:/etc/samba/smb.conf:Z \
             -v /path/to/samba-shares:/shares:Z \
             -v /path/to/samba-data:/var/lib/samba:Z \
            registry.opensuse.org/opensuse/samba-server:4.22
```

To create a new Samba user called `bob` you can use `smbuser`.

```ShellSession
$ podman exec <container-name-or-id> smbuser -u bob -p p433w0rd -d /shares/users/bob
```

### Volumes

The image has two volumes, `/shares` and `/var/lib/samba`.

The volume `/shares` should be used to mount all shared resources.

The volume `/var/lib/samba` consists of persistent data used by the Samba server,
and is used to persist data across restarts.

### Helper scripts

The image comes with a helper script called `smbuser`. This script can be used
to create local users and set the Samba password.

```ShellSession
$ smbuser -u <username> -p <password> -d <user-home-path>
```

## Licensing

`SPDX-License-Identifier: GPL-3.0-or-later`

This documentation and the build recipe are licensed as GPL-3.0-or-later.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
