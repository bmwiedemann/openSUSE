# dovecot container

Dovecot is an open source IMAP and POP3 email server. It is an excellent
choice for both small and large installations. It's fast, simple to set up,
requires no special administration and it uses very little memory.

- [Guide](#guide)
  - [Run a new dovecot instance](#run-a-new-dovecot-instance)
  - [Data persistence](#data-persistence)
- [TLS](#tls)
  - [Auto-generated certificate](#auto-generated-certificate)
  - [Own certificate](#own-certificate)
  - [Disable TLS](#disable-tls)
- [Supported environment variables](#supported-environment-variables)
  - [Generic variables](#generic-variables)
  - [Variables for TLS](#variables-for-tls)
  - [Variables for LDAP](#variables-for-ldap)
  - [Various configuration variables](#various-configuration-variables)
- [Data persistence volumes](#data-persistence-volumes)


## Guide

### Run a new dovecot instance

This dovecot container will create and setup the configuration files at every
restart, but it is also possible to provide an own set of configuration
files.

The command to run this container is:

```sh
podman run -d --rm --name dovecot -p 110:110 -p 143:143 -p 993:993 -p 995:995 -e USE_LDAP=1 -e LDAP_BASE_DN="ou=mail,dc=example,dc=org" -e LDAP_BIND_DN="cn=mailAccountReader,ou=Manager,dc=example,dc=org" -e LDAP_BIND_PASSWORD="password" registry.opensuse.org/opensuse/dovecot
```

### Data persistence

There are some directories to store persistence data like `/var/spool/vmail` for
the emails and `/etc/certs` for the certificates.

If the UID and GID of the vmail user, which owns the `/var/spool/vmail`
hierachy, needs to match in the container and in the host, the `VMAIL_UID`
environment variable needs to be set explicitly.
This variable needs to match the `postfix` container `VMAIL_UID` variable.

## TLS
### Auto-generated certificate

TLS is be configured and enabled by default. If no certificate is provided, a
self-signed one is created during container startup for the container
hostname. The hostname for the certificate can be set e.g. by
`podman run -e HOSTNAME=ldap.example.org ...`

### Own certificate

You can set your custom certificate at run time, by mounting a volume with the
certificates into the container and adjusting the following environment variables:

```sh
podman run -v /srv/dovecot/certs:/etc/certs:Z \
       -e DOVECOT_TLS_CRT=/etc/certs/dovecot.crt \
       -e DOVECOT_TLS_KEY=/etc/certs/dovecot.key \
       -e DOVECOT_TLS_CA_CRT=/etc/certs/ca.crt \
       -d registry.opensuse.org/opensuse/dovecot:latest
```

### Disable TLS

Add `--env DOVECOT_TLS=0` to the run command: `podman run -e DOVECOT_TLS=0 ...`

## Supported environment variables:
### Generic variables:
- `DEBUG=[0|1]`            Enables "set -x" in the entrypoint script
- `TZ`                     Timezone to use in the container

### Variables for TLS:
- `DOVECOT_TLS=[1|0]`         Enable TLS. Defaults to `1` (true).
- `DOVECOT_TLS_CA_CRT`        Dovecot ssl CA certificate. Defaults to `/etc/certs/dovecot-ca.crt`.
- `DOVECOT_TLS_CA_KEY`        Private dovecot CA key. Defaults to `/etc/certs/dovecot-ca.key`.
- `DOVECOT_TLS_CRT`           Dovecot ssl certificate. Defaults to `/etc/certs/dovecot-tls.crt`.
- `DOVECOT_TLS_KEY`           Private dovecot ssl key. Defaults to `/etc/certs/dovecot-tls.key`.
- `DOVECOT_TLS_DH_PARAM`      Dovecot ssl certificate dh param file.
- `DOVECOT_TLS_ENFORCE=[0|1]` Enforce TLS but except ldapi connections. Defaults to `0` (false).
- `DOVECOT_TLS_CIPHER_SUITE`  TLS cipher suite.

### Variables for LDAP
- `USE_LDAP=[0|1]`	Use LDAP for user database
- `LDAP_HOSTS`		Hosts running ldap server
- `LDAP_BASE_DN`	Ldap base DN to look for accounts. Defaults to `ou=mail,dc=example,dc=org`
- `LDAP_BIND_DN		DN used to read user account data. Defaults to `cn=mailAccountReader,ou=Manager,dc=example,dc=org`
- `LDAP_BIND_PASSWORD`  Password for LDAP_BIND_DN.
- `LDAP_USE_TLS=[0|1]`  Use TLS for LDAP queries, defaults to `1`
- `LDAP_TLS_CA_CRT`     LDAP CA certificate to verify connections.

### Various configuration variables:
- `USE_VMAIL_USER=1`	     Enable VMAIL user, defaults to `1`  
- `VMAIL_UID=5000`           UID/GID of vmail user. All files in `/var/spool/vmail` will be changed to this UID/GID
- `ENABLE_IMAP=[0|1]`        Enables imap support, defaults to `1`
- `ENABLE_POP3=[0|1]`        Enables pop3 support, defaults to `0`
- `ENABLE_LMTP=[0|1]`	     Enables mail delivery via LMTP, defaults to `0`
- `ENABLE_SIEVE=[0|1]`       Enables sieve support if LMTP is enabled, defaults to `1`
- `ENABLE_MANAGESIEVE=[0|1]` Enables ManageSieve, requires to export Port 4190. Only available if ENABLE_LMTP and ENABLE_SIEVE are set to `1`. Defaults to `0`

## Data persistence volumes
- `/var/spool/vmail`	Mail storage
- `/etc/certs`		TLS certificates for dovecot
- `/etc/dovecot`	User supplied dovecot configuration files
