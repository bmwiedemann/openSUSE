# Postfix container

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

- [Guide](#guide)
  - [Create new postfix server](#create-new-postfix-server)
- [Supported environment variables](#supported-environment-variables)
  - [Generic variables](#generic-variables)
  - [SMTP related variables](#smtp-related-variables)
  - [Activate additional checks](#activate-additional-checks)
  - [Virtual mailbox related variables](#virtual-mailbox-related-variables)
  - [LDAP related variables](#ldap-related-variables)
- [Data persistence volumes](#data-persistence-volumes)
- [Virtual domains and virtual users](#virtual-domains-and-virtual-users)
  - [Environment Variables](#environment-variables)
  - [Files](#files)
- [Mail delivery via LMTP](#mail-delivery-via-lmtp)

## Guide

### Create new postfix server

By default a simple relayhost postfix instance is started.

The command to run this container is:

```sh
podman run -d --rm --name postfix -p 25:25 -e SMTP_RELAYHOST=smtp.example.com registry.opensuse.org/opensuse/postfix:%%postfix_version%%
```

In all examples, `podman` can be replaced directly with `docker`.

## Supported environment variables
### Generic variables
- `DEBUG=[0|1]`		Enables "set -x" in the entrypoint script.
- `TZ`			Timezone to use in the container.

### SMTP related variables
- `SERVER_HOSTNAME` 	Server hostname. Emails will appear to come from the hostname's domain.
- `SERVER_DOMAIN`   	If not set, the domain part of `SERVER_HOSTNAME` will be used.
- `SMTP_RELAYHOST`	Name of the SMTP relay server to use.
- `SMTP_PORT=587`	The relayhost port.
- `SMTP_USERNAME`	Username to authenticate with on the relayserver.
- `SMTP_PASSWORD`	Password of the SMTP user, alternative `SMTP_PASSWORD_FILE` could be used to point to a file with the password
- `SMTP_NETWORKS`   	Comma separated subnets who are allowed to use the relay. E.g. `SMTP_NETWORKS='xxx.xxx.xxx.xxx/xx, xxx.xxx.xxx.xxx/xx'`. 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16 are preset.
- `INET_PROTOCOLS`	The network interface protocols used for connections. Valid values are "all", "ipv4", "ipv6" or "ipv4,ipv6". The default value is "ipv4".
- `MASQUERADE_DOMAINS`	Comma separated list of domains that must have their subdomain structure stripped off.
- `MYDESTINATION`	List of domains for which mails are delivered locally instead of forwarding to another machine.
- `NULLCLIENT=[0|1]`	Don't accept any mails locally but relay them to a remote host. Ignored if `MYDESTINATION` is set. The default is `1`.
- `SMTP_TLS_SECURITY_LEVEL`	SMTP TLS security level. The default is `may`.
- `LMTP=host`           Host on which the lmtp service is running. This will disable the usage of the vmail user account.

### Accepting mails on port 587 (submission) and 465 (submissions/smtps)
- `ENABLE_SUBMISSION=[0|1]`	Enable submission port. The default is `0`.
- `ENABLE_SUBMISSIONS=[0|1]`    Enable submissions/smtps port. This requires `SMTPD_USE_TLS=1`. The default is `0`.
- `SMTPD_USE_TLS=[0|1]`         Enforce TLS. The default is `0`.
- `SMTPD_TLS_CRT=`              Path to certificate, default `/etc/postfix/ssl/certs/tls.crt`
- `SMTPD_TLS_KEY=`              Path to public key, default `/etc/postfix/ssl/certs/tls.key`



### Virtual mailbox related variables
- `VIRTUAL_MBOX=[0|1]`	Create virtual mail boxes in /var/spool/vmail owned by user vmail.
- `VMAIL_UID=5000`	User ID and group ID of the vmail user for virtual domains and mailboxes.
- `VIRTUAL_DOMAINS=`	Whitespace separated list of virtual domains, will be written to `/etc/postfix/vhosts`.
- `VIRTUAL_USERS=`	Whitespace separated list of virtual users email addresses.

### LDAP related variables
- `USE_LDAP=[0|1]`	Use LDAP for virtual mail box user accounts.
- `LDAP_BASE_DN`	LDAP base DN, defaults to `dc=example,dc=org`.
- `LDAP_SERVER_URL`	LDAP Server URL, defaults to `ldap://localhost`.
- `LDAP_BIND_DN`        DN to bind, defaults to `cn=mailAccountReader,ou=Manager,dc=example,dc=org`
- `LDAP_BIND_PASSWORD`	The password for the distinguished name to bind (`LDAP_BIND_DN`)
- `LDAP_USE_TLS=[1|0]`	Use TLS for LDAP queries, by default enabled.
- `LDAP_TLS_CA_CRT`	LDAP SSL CA certificate.

## Data persistence volumes
- `/var/spool/postfix`	Postfix mail queues. A data volume should be used in order to save the queue content if the container restarts.
- `/var/spool/vmail`	Virtual user mboxes. This directory contains the mails stored in Maildir format of the virtual users of the virtual domains. Everything is owned by the `vmail` user.
- `/etc/pki`		PKI directories for CA certificates

## Virtual domains and virtual users

The environment variable `VIRTUAL_MBOX=1` will enable support for virtual
domains and virtual users. It can be used in conjunction with a relay host.

Mails for virtual domains and users are stored in Maildir format in
`/var/spool/vmail` inside the container. To not loose the mail, this directory
should be a persistence volume.
`VMAIL_UID` specifies the UID and GID which owns all files below this
directory. This makes sure, that the container is using the same UID/GID as
the Container Host OS for the files and not regular users are owning this
files and can read and modify them. The default UID/GID is `5000`.

There are three ways to provide the data for virtual domains and users, via
environment variables, files or LDAP.

### Environment Variables

Beside the already mentioned environment variables, two further variables
define the virtual domains and the virtual users.
`VIRTUAL_DOMAINS="example.com example2.com example3.com"` is a whitespace
separated list which can contain one or more virtual domains. For every
domain, an own directory below `/var/spool/vmail` will be created.
`VIRTUAL_USERS="user1@example.com user@example3.com user2@example.com"`
Whitespace separated list of virtual users email addresses.

The example call:
```sh
podman run -d --rm --name postfix -p "25:25" \
    -e VIRTUAL_MBOX=1 \
    -e VMAIL_UID=5000 \
    -e VIRTUAL_DOMAINS="example.com example1.com" \
    -e VIRTUAL_USERS="user1@example.com user2@example.com user@example1.com" \
    -e SERVER_HOSTNAME=smtp.example.com \
    -e SMTP_RELAYHOST=relay.example.com \
    -e SMTP_USERNAME=mailer \
    -e SMTP_PASSWORD='XXX' \
    -v "/srv/postfix/vmail:/var/spool/vmail:Z" \
    registry.opensuse.org/opensuse/postfix:%%postfix_version%%
```

Will store the mails for the users `user1@example.com`, `user2@example.com`,
`user@example1.com` into the directories inside of the container:
- `/var/spool/vmail/example.com/user1/`
- `/var/spool/vmail/example.com/user2/`
- `/var/spool/vmail/example1.com/user/`

and outside the container:
- `/srv/postfix/vmail/example.com/user1/`
- `/srv/postfix/vmail/example.com/user2/`
- `/srv/postfix/vmail/example1.com/user/`

owned by the user `vmail` with UID and GID `5000`. All other mails are
forwarded to the relay `relay.example.com` with the account `mailer` and the
password `XXX`.

### Files

Instead of maintaining a long list of environment variables, the configuration
files could also be provided and mapped into /etc/postfix of the container.

`/etc/postfix/vhosts` contains the list of virtual domains separated by
newlines:

```
example.com
example1.com
```

`/etc/postfix/vmaps` contains the list of the virtual users, where to store
them below the vmail directory and if mbox format or Maildir should be used.
For Maildir, the configuration file for the above example would look like:
```
user1@example.com example.com/user1/
user2@example.com example.com/user2/
user@example1.com example1.com/user/
```
For mbox format, the trailing '/' needs to be removed.

Additional a `/etc/postfix/vquota` file is required, which contains the quota
of the virtual users mailbox. To disable it, the file would look like:
```
user1@example.com 0
user2@example.com 0
user@example1.com 0
```

The example call:
```sh
podman run -d --rm --name postfix -p 25:25 \
    -e VIRTUAL_MBOX=1 \
    -e VMAIL_UID=5000 \
    -e SERVER_HOSTNAME=smtp.example.com \
    -e SMTP_RELAYHOST=relay.example.com \
    -e SMTP_USERNAME=mailer \
    -e SMTP_PASSWORD='XXX' \
    -v "/srv/postfix/vmail:/var/spool/vmail:z" \
    -v "/srv/postfix/etc/vhosts:/etc/postfix/vhosts:z,ro" \
    -v "/srv/postfix/etc/vmaps:/etc/postfix/vmaps:z,ro" \
    -v "/srv/postfix/etc/vquota:/etc/postfix/vquota:z,ro" \
    registry.opensuse.org/opensuse/postfix:%%postfix_version%%
```

### LDAP

With LDAP (use `VIRTUAL_MBOX=1` and `USE_LDAP=1`) the postfix schema is used: `maildrop` is the real email address, while `mailacceptinggeneralid` are aliases.
If the `VIRTUAL_DOMAINS` environment variable is not set, the virtual domains are take from the email addresses used in `mailacceptinggeneralid`. In this case,
the email domains of the aliases must be different then the one of `maildrop`. If the virtual domains are specified with `VIRTUAL_DOMAINS`, `mailacceptinggeneralid`
are handled as normal mail aliases and the domain could be the same as for `maildrop`.

## Mail delivery via LMTP

To deliver the mails via a LMTP service, the container needs to know the host
on which such a service is running:

```sh
podman run -d --rm --name postfix -p 25:25 -e MYDESTINATION=example.com -e LMTP=lmtp.example.com registry.opensuse.org/opensuse/postfix:%%postfix_version%%
```

## Licensing

`SPDX-License-Identifier: (EPL-2.0 OR IPL-1.0) AND MIT`

This documentation and the build recipe are licensed as (EPL-2.0 OR IPL-1.0) AND MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
