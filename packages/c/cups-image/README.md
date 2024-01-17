# CUPS Container Image

## Description

This container image contains the latest cups server from openSUSE Tumbleweed.

## Usage

### Start the container

```bash

podman run -d --rm -p 631:631 --name cups registry.opensuse.org/opensuse/cups:latest

```

### Configuration

This CUPS container comes with a default cups configuration which allows remote access for adminitration. An own configuration can be provided as volume: `-v /srv/cups:/etc/cups`, where the example assumes you have your cups configuration stored in `/srv/cups`.

For further configuration, login to the CUPS web interface on port 631 (e.g.
`https://localhost:631`) and configure CUPS to your need.
*IMPORTANT*: you need to use `https://`, else cups will do a wrong redirect!

The default administration account is: `admin`

For security reasons there is no default password, it has to be set with
the environment variable _ADMIN_PASSWORD_.

```bash

podman run -d --rm -p 631:631 -v /srv/cups:/etc/cups -e ADMIN_PASSWORD=mySecretPassword --name cups registry.opensuse.org/opensuse/cups:latest

```


