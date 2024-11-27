# The Valkey 8.0 container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

Valkey is a high-performance data structure server that primarily serves
key/value workloads. It supports a wide range of native structures and
an extensible plugin system for adding new data structures and access
patterns.

## How to use the image

The image ships with the valkey server and a persistent storage configured
to `/data`.

To start an instance, follow these instructions:


```ShellSession
podman run --rm registry.opensuse.org/opensuse/valkey:8.0
```

In case you want start with persistent storage, run this:

```ShellSession
podman run --rm registry.opensuse.org/opensuse/valkey:8.0 valkey-server --save 60 1
```

This one will save a snapshot of the DB every 60 seconds if at least 1
write operation was performed. If persistence is enabled, data is stored
in the VOLUME /data, which can be used with `-v /host/dir:/data`.


## Licensing

`SPDX-License-Identifier: BSD-3-Clause`

This documentation and the build recipe are licensed as BSD-3-Clause.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
