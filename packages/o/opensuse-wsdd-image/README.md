# wsdd container

wsdd implements a Web Service Discovery host daemon. This enables (Samba) hosts
to be found by Web Service Discovery Clients like Windows.

- [Guide](#guide)
  - [Run a new wsdd instance](#run-a-new-wsdd-instance)
  - [Environment variables](#environment-variables)

## Guide

### Run a new wsdd instance

The command to run this container is:

```sh
podman run -d --rm --name wsdd --net=host -e HOSTNAME=$(hostname) registry.opensuse.org/home/kukuk/container/container/wsdd
```

### Environment variables:
  DEBUG=[0|1]		Enable debug mode
  HOSTNAME=<hostname>	Samba Netbios name to report.
  WORKGROUP=<name>	Workgroup name
  DOMAIN=<domain>	Report being a member of an AD DOMAIN. Disables WORKGROUP if set.
