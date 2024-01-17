# spamassassin container

SpamAssassin is an intelligent email filter which uses a diverse range
of tests to identify unsolicited bulk email, more commonly known as "spam".

- [Guide](#guide)
- [Data persistence](#data-persistence)
- [Supported environment variables](#supported-environment-variables)
- [Volumes](#volumes)
- [SpamAssassin Documentation](#spamassassin-documentation)

## Guide

The command to run this container is:

```sh
podman run -d --rm --name spamassassin -v /srv/spamassassin/etc:/etc/spamassassin -p 783:783 registry.opensuse.org/opensuse/spamassassin
```

This will run `spamd` on port 783 to classify emails. Admin provided
configuration files in `/etc/spamassassin` will be merged at startup.

The rules are updated at every start of the container.

## Data persistence

The updated database is not stored in a persistence way, it will be
updated at every start again. Except a volume for /var/lib/spamassassin
is created and provided.

## Supported environment variables:
- `DEBUG=0|1`		Enables debug mode
- `TZ`			Timezone to use

## Volumes
- `/var/lib/spamassassin`	Store the updated rules
- `/etc/spamassassin`		Additional local configuration files

## Spamassassin documentation

To read the current spamassassin confiuration file documentation:

```sh
podman run registry.opensuse.org/opensuse/spamassassin man Mail::SpamAssassin::Conf
```
