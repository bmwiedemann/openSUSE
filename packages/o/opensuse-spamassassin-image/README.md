# spamassassin container

The command to run this container is:

```sh
podman run -d --rm --name spamassassin -p 783:783 registry.opensuse.org/opensuse/spamassassin
```

## Description

This container provides the spamassassin daemon (spamd). The rules are
updated at every start of the container.


## Spamassassin documentation

To read the current spamassassin documentation:

```sh
podman run registry.opensuse.org/opensuse/spamassassin man spamassassin
```

## Supported environment variables:
- `DEBUG=0|1`		Enables debug mode
- `TZ`			Timezone to use

## Volumes
- `/var/lib/spamassassin`	Store the updated rules
