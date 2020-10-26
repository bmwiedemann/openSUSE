# OpenLDAP container

- [Guide](#guide)
  - [Create new ldap server](#create-new-ldap-server)
  - [Data persistence](#data-persistence)
  - [Server configuration](#server-configuration)
  - [Seed ldap database with ldif](#seed-ldap-database-with-ldif)
- [TLS](#tls)
  - [Auto-generated certificate](#auto-generated-certificate)
  - [Own certificate](#own-certificate)
  - [Disable TLS](#disable-tls)
- [Supported environment variables](#supported-environment-variables)
  - [Generic variables](#generic-variables)
  - [Variables for new database](#variables-for-new-database)
  - [Variables for TLS](#variables-for-tls)
  - [Various configuration variables](#various-configuration-variables)
- [Data persistence volumes](#data-persistence-volumes)

## Guide

### Create new ldap server

This is the default behavior when you run this image.
It will create an empty ldap for the company **Example Inc.** and the domain **example.org**.

Two passwords are required to startup the container:

  - `LDAP_ADMIN_PASSWORD` Ldap admin password for `cn=admin,dc=example,dc=org`
  - `LDAP_CONFIG_PASSWORD` Ldap admin password for `cn=admin,dc=example,dc=org`

The command to run this container is:

```sh
podman run -d --rm --name openldap -p 389:389 -p 636:636 -e LDAP_ADMIN_PASSWORD="admin" -e LDAP_CONFIG_PASSWORD="config" registry.opensuse.org/opensuse/openldap
```

To test the container a LDAP search could be issued:

```sh
podman exec -it openldap ldapsearch -x -W -H ldapi:/// -b dc=example,dc=org -D "cn=admin,dc=example,dc=org"
```

In all examples, `podman` can be replaced directly with `docker`.

### Data persistence

The directories `/var/lib/ldap` (LDAP database files) and
`/etc/openldap/slapd.d` (LDAP config files) are used to store the schema and
data information. They will be re-created at every container startup if they
are not mapped as volumes, means your ldap files are saved outside the
container. Normally this data should be stored, but for various use-cases it
could be usefull to throw them away afterwards.

If the UID and GID of the ldap user needs to match in the container and in the
host, the `LDAP_UID` and `LDAP_GID` environment variables needs to be set
explicitly:

```sh
podman run -d --rm --name openldap -p 389:389 -p 636:636 -e LDAP_UID=333 -e LDAP_GID=333 -e LDAP_ADMIN_PASSWORD="admin" -e LDAP_CONFIG_PASSWORD="config" registry.opensuse.org/opensuse/openldap
```

### Server configuration

Since slapd.conf is not used the ldap utils `ldapmodify`, `ldapadd` and
`ldapdelete` are required to adjust the server configuration.

### Seed ldap database with ldif

This image can load ldif and schema files at startup from an internal
path. This is useful if a continuous integration service mounts automatically
the working copy (sources) into a docker service, which has a relation to the
ci job.

In order to seed ldif or schema files from internal path you must set the
specific environment variable `LDAP_SEED_LDIF_PATH` and/or
`LDAP_SEED_SCHEMA_PATH`. If set this will copy any *.ldif or *.schema file
into the default seeding directories of this image.

## TLS
### Auto-generated certificate

TLS is be default configured and enabled. If no certificate is provided, a
self-signed one is created during container startup for the container
hostname. The container hostname can be set e.g. by
`podman run --hostname ldap.example.org ...`

### Own certificate

You can set your custom certificate at run time, by mounting a volume with the
certificates into the container and adjusting the following environment variables:

```sh
podman run --hostname ldap.example.org -v /srv/openldap/certs:/etc/openldap/certs:Z \
       -e LDAP_TLS_CRT=/etc/openldap/certs/ldap.crt \
       -e LDAP_TLS_KEY=/etc/openldap/certs/ldap.key \
       -e LDAP_TLS_CA_CRT=/etc/openldap/certs/ca.crt \
       -d registry.opensuse.org/opensuse/openldap:latest
```

### Disable TLS

Add --env LDAP_TLS=0 to the run command: `podman run -e LDAP_TLS=0 ...`

## Supported environment variables:
### Generic variables:
- `DEBUG=[0|1]`		   Enables "set -x" in the entrypoint script
- `TZ`			   Timezone to use in the container

### Variables for new database:
- `LDAP_DOMAIN`		   Ldap domain. Defaults to `example.org`
- `LDAP_BASE_DN`	   Ldap base DN. If empty automatically set from `LDAP_DOMAIN` value. Defaults to (`empty`)
- `LDAP_ORGANIZATION`	   Organization name. Defaults to `Example Inc.`
- `LDAP_ADMIN_PASSWORD`	   Ldap admin password. It's required to supply one if no database exists at startup.
- `LDAP_CONFIG_PASSWORD`   Ldap config password. It's required to supply one if no database exists at startup.
- `LDAP_BACKEND`	   Database backend, defaults to `mdb`
- `LDAP_SEED_LDIF_PATH`    Path with additional ldif files which will be loaded
- `LDAP_SEED_SCHEMA_PATH`  Path with additional schema which will be loaded

### Variables for TLS:
- `LDAP_TLS=[1|0]`	   Enable TLS. Defaults to `1` (true).
- `LDAP_TLS_CA_CRT`	   LDAP ssl CA certificate. Defaults to `/etc/openldap/certs/openldap-ca.crt`.
- `LDAP_TLS_CA_KEY`	   Private LDAP CA key. Defaults to `/etc/openldap/certs/openldap-ca.key`.
- `LDAP_TLS_CRT`	   LDAP ssl certificate. Defaults to `/etc/openldap/certs/tls.crt`.
- `LDAP_TLS_KEY`	   Private LDAP ssl key. Defaults to `/etc/openldap/certs/tls.key`.
- `LDAP_TLS_DH_PARAM`	   LDAP ssl certificate dh param file.
- `LDAP_TLS_ENFORCE=[0|1]` Enforce TLS but except ldapi connections. Defaults to `0` (false).
- `LDAP_TLS_CIPHER_SUITE`  TLS cipher suite.
- `LDAP_TLS_VERIFY_CLIENT` TLS verify client. Defaults to `demand`.

### Various configuration variables:
- `LDAP_NOFILE` 	   Number of open files (ulimt -n), default `1024`
- `LDAP_PORT`   	   Port for ldap:///, defaults to `389`
- `LDAPS_PORT`		   Port for ldaps:///, defaults to `636`
- `LDAPI_URL`		   Ldapi url, defaults to `ldapi:///run/slapd/ldapi`
- `LDAP_UID`               UID of ldap user. All LDAP related files will be changed to this UID
- `LDAP_GID`		   GID of ldap group. All LDAP related files will be changed to this GID
- `LDAP_BACKEND`	   Database backend, defaults to `mdb`
- `SLAPD_LOG_LEVEL`        Slapd debug devel, defaults to `0`
- `SETUP_FOR_MAILSERVER`   The mail organization will be created (ldif/mailserver/), defaults to `0`

## Data persistence volumes
- `/etc/openldap/certs`	   TLS certificates for slapd
- `/etc/openldap/slapd.d`  Slapd configuration files
- `/var/lib/ldap`	   OpenLDAP database
