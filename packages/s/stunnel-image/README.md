# Stunnel Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)


## Description

Stunnel is an open-source multi-platform application that provides a universal
TLS/SSL tunneling service.


## How to use this image

By default, the Stunnel container image launches `stunnel` using a minimal
configuration file that specifies the following:
- run in foreground
- load further configuration files from `/etc/stunnel/conf.d`

Custom configuration files must be placed into the directory
`/etc/stunnel/conf.d`.

The container entry point configures TLS/SSL automatically by setting the key
and certificate to the values of the environment variables `STUNNEL_KEY` and
`STUNNEL_CERT`. If one of the environment variables is unset, then the
entrypoint defaults to `/etc/stunnel/stunnel.key` for `STUNNEL_KEY` and
`/etc/stunnel/stunnel.pem` for `STUNNEL_CERT`.

The entrypoint can set up a single service via environment variables, so that
the user doesn't have to write and mount their own configuration file. This can
be specified via the environment variables `STUNNEL_SERVICE_NAME`,
`STUNNEL_ACCEPT` and `STUNNEL_CONNECT`:

- `STUNNEL_SERVICE_NAME`: name or otherwise unique identifier of the service
  (used for documentation purpose only)

- `STUNNEL_ACCEPT`: address on which new connections should be accepted. It can
  be either a hostname and a port number or just a port number (in which case,
  localhost is assumed to be the host)

- `STUNNEL_CONNECT`: address on which the unencrypted service is listening and
  to which stunnel connects. It can be either a hostname and port number or just
  a port number (in which case, localhost is assumed to be the host)


For example, to create an SSL endpoint for a webserver listening on port `8000`
on localhost, run the following command:

```bash
podman run --rm -d \
    -p 8443:8443 \
    -e STUNNEL_SERVICE_NAME=webserver \
    -e STUNNEL_ACCEPT=0.0.0.0:8443 \
    -e STUNNEL_CONNECT=0.0.0.0:8000 \
    -v=path/to/server.pem:/etc/stunnel/stunnel.pem:Z \
    -v=path/to/server.crt:/etc/stunnel/stunnel.crt:Z \
    registry.opensuse.org/opensuse/stunnel:5
```


### Logging

Stunnel supports eight log levels, from 0 (emergency) to 7 (debug) with 5
(notice) being the default. The log level can be configured via the environment
variable `STUNNEL_DEBUG` using either the number or the log level name. For the
supported logging levels, refer to the [upstream
documentation](https://www.stunnel.org/static/stunnel.html#debug-FACILITY.-LEVEL).


### Pitfalls

The Stunnel container image is configured to launch `stunnel` as the `stunnel`
user. But by default, files mounted into a running container belong to the
`root` user. Set the file permissions of mounted files accordingly, so that
non-owners and non-group members can read them.

Stunnel's `inetd` mode is not supported in the container image, and it does not
ship a package manager for installing any services.


## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
