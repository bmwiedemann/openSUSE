# openSUSE Tumbleweed Container Vulnerability Scanner: Trivy application container
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)


## Description

Trivy is a comprehensive and versatile security scanner. Trivy has scanners
that look for security issues, and targets where it can find those issues.


## Usage

This container provides the openSUSE Project version of Trivy.

Example of using the Trivy container:

```ShellSession
$ podman run registry.opensuse.org/opensuse/trivy:0 image registry.opensuse.org/opensuse/trivy:0
```

For more use cases and documentation, refer to the
[Trivy documentation](https://trivy.dev/latest/docs).


## Licensing

`SPDX-License-Identifier: Apache-2.0`

This documentation and the build recipe are licensed as Apache-2.0.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
