# fetchmail container

fetchmail retrievs mails and forwards them; it fetches the mail from remote
IMAP or POP3 servers and forwards them to your local machine.

- [Guide](#guide)
  - [Run a new fetchmail instance](#run-a-new-fetchmail-instance)
  - [Data persistence](#data-persistence)
  - [Fetchmail documentation](#fetchmail-documentation)
- [Supported environment variables](#supported-environment-variables)
- [Configuration file](#configuration-file)

## Guide

### Run a new fetchmail instance

This fetchmail container requires a `fetchmailrc` configuration file provided
by the user.

The command to run this container is:

```sh
podman run -d --rm --name fetchmail -v /etc/fetchmailrc:/etc/fetchmailrc:ro registry.opensuse.org/opensuse/fetchmail
```

### Data persistence

fetchmail does not store anything local, but forwards all emails to a local
mail system.

### Fetchmail documentation

To read the current fetchmail documentation:

```sh
podman run registry.opensuse.org/opensuse/fetchmail man fetchmail
```

## Supported environment variables:
- `DEBUG=0|1`		Enables debug mode
- `TZ`			Timezone to use
- `POLLING_INTERVAL`	Interval to poll for new mails, default is `600`
- `FETCHALL=[0|1]`	Retrieve both old (seen) and new messages, default `1`
- `SILENT=[0|1]`	Suppresses all progress/status messages
- `SMTP_HOSTS`		Comma seprated list of hosts to forward mail to

## Configuration file
- `/etc/fetchmailrc`	Configuration file for fetchmail
