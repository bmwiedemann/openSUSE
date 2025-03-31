# openSUSE Tumbleweed ISC BIND 9: BIND9 Application Container
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

BIND (Berkeley Internet Name Domain) is a suite of software for interacting
with the Domain Name System (DNS). Its core component, `named`, serves as both
an authoritative name server for DNS zones and a recursive resolver for network
queries.

## Usage

This container image provides the `named` daemon from
openSUSE Tumbleweed, including the default configuration that comes
with the RPM package.

When no additional parameters are specified, the container entrypoint launches `named` in the foreground mode by default:

```ShellSession
$ podman run --rm -d -p 53/udp registry.opensuse.org/opensuse/bind:9
```

### Health Check

The container includes a health check script that performs a simple A-record
lookup and verifies that a valid IPv4 address is returned.

### Environment Variables

The container entrypoint accepts the following environment variables:

- **`NAMED_CONF`** (default: `/etc/named.conf`): Path to the configuration file
    for `named`. See the [upstream
    documentation](https://bind9.readthedocs.io/en/latest/chapter3.html) for
    syntax details.

- **`NAMED_CHECKCONF_BIN`** (default: `/usr/bin/named-checkconf`): Path to the
    configuration checker binary executed before launching `named`.

- **`NAMED_CHECKCONF_ARGS`** (default: empty): Arguments passed to
    `NAMED_CHECKCONF_BIN` in the entrypoint.

- **`ETC_RNDC_KEY`** (default: `/etc/rndc.key`): Location of the `rndc`
    configuration file. If not a symlink, it is moved to `NEW_RNDC_KEY`.

- **`NEW_RNDC_KEY`** (default: `/var/lib/named/rndc.key`): Target location where
    `ETC_RNDC_KEY` is moved if it is not a symlink. If `NEW_RNDC_KEY` does not
    exist, it is generated using `RNDC_BIN`.

- **`RNDC_BIN`** (default: `/usr/sbin/rndc`): Binary used to generate the `rndc`
    configuration file if it does not exist.

- **`RNDC_KEYSIZE`** (default: `512`): Key size passed to `RNDC_BIN` for
    generating the `rndc` configuration file.


### Differences compared to the RPM Package

The container does not use `systemd` to manage
`named`. Instead, `named` is launched directly by the container entrypoint in
foreground mode, with logs output to `stdout`.

Moreover, environment variables from `/etc/sysconfig/named` are not sourced
or used. You must set them explicitly using the container runtime,
for example:

```ShellSession
$ podman run --rm -d -e RNDC_KEYSIZE=1024 registry.opensuse.org/opensuse/bind:9
```

## Additional Information

For more details on BIND and `named`, refer to the [official
documentation](https://bind9.readthedocs.io/).


## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
