# Postfix container

The command to run this container is:

```sh
podman run -d --rm --name postfix -p 25:25 -e SMTP_RELAYHOST=smtp.example.com registry.opensuse.org/opensuse/postfix
```

In all examples, `podman` can be replaced directly with `docker`.

## Supported environment variables:
- `DEBUG=yes|no`	Enables "set -x" in the entrypoint script.
- `TZ`			Timezone to use in the container.
- `SERVER_HOSTNAME` 	Server hostname. Emails will appear to come from the hostname's domain.
- `SERVER_DOMAIN`   	If not set, the domain part of `SERVER_HOSTNAME` will be used.
- `SMTP_RELAYHOST`	Name of the SMTP relay server to use.
- `SMTP_PORT=587`	The relayhost port.
- `SMTP_USERNAME`	Username to authenticate with on the relayserver.
- `SMTP_PASSWORD`	Password of the SMTP user, alternative `SMTP_PASSWORD_FILE` could be used to point to a file with the password
- `SMTP_NETWORKS`   	Comma seperated subnets who are allowed to use the relay. E.g. `SMTP_NETWORKS='xxx.xxx.xxx.xxx/xx, xxx.xxx.xxx.xxx/xx'`. 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16 are preset.
- `INET_PROTOCOLS`	The network interface protocols used for connections. Valid values are "all", "ipv4", "ipv6" or "ipv4,ipv6". The default value is "ipv4".
- `MASQUERADE_DOMAINS`	Comma separated list of domains that must have their subdomain structure stripped off.
- `MYDESTINATION`	List of domains for which mails are delivered locally instead of forwarding to another machine.
- `VIRTUAL_MBOX=1`	Create virtual mail boxes in /var/spool/vmail owned by user vmail.
- `VMAIL_UID=5000`	User ID and group ID of the vmail user for virtual domains and mailboxes.
- `VIRTUAL_DOMAINS=`	Whitespace seperated list of virtual domains, will be written to `/etc/postfix/vhosts`.
- `VIRTUAL_USERS=`	Whitespace seperated list of virtual users email addresses.


## Data persistence volumes
- `/var/spool/postfix`	Postfix mail queues. A data volume should be used in order to save the queue content if the container restarts.
- `/var/spool/vmail`	Virtual user mboxes. This directory contains the mails stored in Maildir format of the virtual users of the virtual domains. Everything is owned by the `vmail` user.

## Virtual domains and virtual users

The environment variable `VIRTUAL_MBOX=1` will enable support for virtual
domains and virtual users. It can be used in conjunction with a relay host.

Mails for virtual domains and users are stored in Maildir format in
`/var/spool/vmail` inside the container. To not loose the mail, this directory
should be a persistence volume.
`VMAIL_UID` specifies the UID and GID which owns all files below this
directory. This makes sure, that the container is using the same UID/GID as
the Container Host OS for the files and not regular users are owning this
files and can read and modify them. The default UID/Gid is `5000`.

There are two ways to provide the data vor virtual domains and users, via
environment variables or via files.

### Environment Variables

Beside the already mentioned environment variables, two futher variables
define the virtual domains and the virtual users.
`VIRTUAL_DOMAINS="example.com example2.com example3.com"` is a whitespace
seperated list which can contain one or more virtual domains. For every
domain, an own directory below `/var/spool/vmail` will be created.
`VIRTUAL_USERS="user1@example.com user@example3.com user2@example.com"`
Whitespace seperated list of virtual users email addresses.

The example call:
```sh
podman run -d --rm --name postfix -p "25:25" -e VIRTUAL_MBOX=1 -e VMAIL_UID=5000 -e VIRTUAL_DOMAINS="example.com example1.com" -e VIRTUAL_USERS="user1@example.com user2@example.com user@example1.com" -e SERVER_HOSTNAME=smtp.example.com -e SMTP_RELAYHOST=relay.example.com -e SMTP_USERNAME=mailer -e SMTP_PASSWORD='XXX' -v "/srv/postfix/vmail:/var/spool/vmail" registry.opensuse.org/opensuse/postfix:latest
```

Will store the mails for the users `user1@example.com`, `user2@example.com`,
`user@example2.com` into the directories inside of the container:
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

`/etc/postfix/vhosts` contains the list of virtual domains seperated by
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
podman run -d --rm --name postfix -p "25:25" -e VIRTUAL_MBOX=1 -e VMAIL_UID=5000 -e SERVER_HOSTNAME=smtp.example.com -e SMTP_RELAYHOST=relay.example.com -e SMTP_USERNAME=mailer -e SMTP_PASSWORD='XXX' -v "/srv/postfix/vmail:/var/spool/vmail" -v "/srv/postfix/etc/vhosts:/etc/postfix/vhosts:ro" -v "/srv/postfix/etc/vmaps:/etc/postfix/vmaps:ro" -v "/srv/postfix/etc/vquota:/etc/postfix/vquota:ro" registry.opensuse.org/opensuse/postfix:latest
```
