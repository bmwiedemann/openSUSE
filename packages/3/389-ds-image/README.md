# 389 Directory Server container image

## Description

[389 Directory Server](https://www.port389.org/) is a highly usable, fully
featured, reliable and secure LDAP server implementation.

## Usage

By default, the image launches 389 Directory Server with the same
configuration that comes with the SUSE Linux Enterprise Server. However there
is also included a pre-configured Name Service Switch (NSS) configuration
file (`/etc/nsswitch.conf`).

```ShellSession
$ podman run -it --rm -p 3389:3389 -p 3636:3636 registry.opensuse.org/opensuse/389-ds:3.1
```

## Volumes

The database is stored in the volume mounted as directory `/data`. A new
empty database is created during container startup, unless an existing
database is already present in `/data`.

To mount a host directory as a volume for your database, run the following
command:

```ShellSession
$ podman run -it --rm -v /my/own/datadir:/data:Z -p 3389:3389 -p 3636:3636 registry.opensuse.org/opensuse/389-ds:3.1
```

## Certificates

By default, the container uses a self-signed CA certificate and a server
certificate signed by that CA.

Place a custom TLS certificate in PEM format in `/data/tls/server.crt` and
the key in and `/data/tls/server.key`. Place the CA certificates (each as a
separate file) to `/data/tls/ca/`, for example, `/data/tls/ca/ca1.crt` and
`/data/tls/ca/ca2.crt`.

## Environment variables

### DS_ERRORLOG_LEVEL

Use this optional environment variable to set the log level for
`ns-slapd` (default is `266354688`).

### DS_DM_PASSWORD

Use this optional environment variable to set the `cn=Directory Manager`
password (a default password is generated randomly). The default randomly
generated password can be viewed in the setup log.

### DS_MEMORY_PERCENTAGE

Use this optional environment variable to set the LDBM autotune
percentage (`nsslapd-cache-autosize`) (default is unset).

### DS_REINDEX

Use this optional environment variable to run a database re-index task. Set
the value to `1` to enable the task (default is disabled).

### DS_SUFFIX_NAME

Use this optional environment variable to set the default database
suffix name for `basedn` (default one is derived from the hostname).

### DS_STARTUP_TIMEOUT

Use this optional environment variable to change the time to wait for the
instance to start (default is `60` seconds).

### DS_STOP_TIMEOUT

Use this optional environment variable to change the time to wait for the
instance to stop (default is `60` seconds).

## Health, liveness, and readiness

The container image includes one explicit health check. This check will
verify if the service is misconfigured, `ns-slapd` is running, and if the
LDAPI is functional.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
