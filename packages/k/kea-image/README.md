# Kea DHCP Server Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

Kea is an open-source DHCP server developed by the [Internet Systems
Consortium](https://www.isc.org/) and the successor of the now deprecated
DHCPd. The Kea distribution includes a DHCPv4 server, a DHCPv6 server, and a
Dynamic DNS (DDNS) server. Significant features include: support for IPv6 prefix
delegation, host reservations (which may be optionally stored in a separate back
end database), Preboot Execution Environment (PXE) boot, client classification,
shared networks, and high-availability (failover pairs). Kea can store leases
locally in a memfile, or in a PostgreSQL or MySQL database. Kea has a supported
API for writing optional extensions, using 'hooks'.

## How to use this Container Image


The container image expects configuration file in the directory `/etc/kea`.
Execute the following command to run DHCP using the configuration provided in the directory `/etc/kea`:

```ShellSession
podman container runlabel run \
      registry.opensuse.org/opensuse/kea:2.6
```
To run a DHCP6 server using the configuration file supplied in the directory `/etc/kea`, execute the following command:

```ShellSession
podman container runlabel run_dhcp6 \
      registry.opensuse.org/opensuse/kea:2.6
```

The Kea configuration file can also be provided in the current working directory.
To run a DHCP or a DHCP6 server using the configuration file in the current working directory, execute the following commands:

```ShellSession
$ # for DHCP
$ podman container runlabel runcwd \
      registry.opensuse.org/opensuse/kea:2.6
$ # for DHCP6
$ podman container runlabel runcwd_dhcp6 \
      registry.opensuse.org/opensuse/kea:2.6
```

## Licensing

`SPDX-License-Identifier: MPL-2.0`

This documentation and the build recipe are licensed as MPL-2.0.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
