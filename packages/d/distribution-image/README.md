# openSUSE Tumbleweed OCI Container Registry (Distribution): Suitable for running a local OCI registry
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description
This container image allows running a local OCI registry.


## Usage
Before you start the container,
you need to create a `config.yml` with the following content:

```yaml
---
version: 0.1
log:
  level: info
storage:
  filesystem:
    rootdirectory: /var/lib/docker-registry
http:
  addr: 0.0.0.0:5000
```

You can also create an empty directory for storing the images outside the container:

```bash
mkdir -p /var/lib/docker-registry
```

Then you can start the container with the following command:

```bash
podman run -it --restart=always -p 5000:5000 -v /path/to/config.yml:/etc/registry/config.yml \
  -v /var/lib/docker-registry:/var/lib/docker-registry --name registry registry.opensuse.org/opensuse/registry:3.1
```

The registry is available at `http://localhost:5000`.

To run the registry as a Systemd service using Podman Quadlet, create a unit file named `/etc/containers/systemd/registry.container` with the following content (update variables accordingly):

```
[Unit]
Description=openSUSE Tumbleweed OCI Container Registry (Distribution)

[Container]
Image=registry.opensuse.org/opensuse/registry:3.1
ContainerName=registry
PublishPort=5000:5000
Volume=/path/to/config.yml:/etc/registry/config.yml:Z
Volume=/var/lib/docker-registry:/var/lib/docker-registry:Z

[Service]
Restart=always

[Install]
WantedBy=multi-user.target
```

To generate a systemd service for the registry container, execute the following command:

```bash
sudo systemctl daemon-reload
```

To enable and start the registry service, execute the following command:

```bash
sudo systemctl enable --now registry
```

## Licensing

`SPDX-License-Identifier: Apache-2.0`

This documentation and the build recipe are licensed as Apache-2.0.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
