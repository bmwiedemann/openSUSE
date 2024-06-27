# openSUSE Tumbleweed BCI Micro: Suitable for deploying static binaries
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

The `bci-micro` image includes the RPM database, but not the RPM package
manager. This means that the image is smaller than `bci-minimal`. The primary
use case for the image is deploying static binaries produced externally or
during multi-stage builds.


## Usage

As there is no straightforward way to install additional
dependencies inside the container image, we recommend deploying a project
using the `bci-micro` image only when the final build artifact bundles all
dependencies and needs no further installation of packages.

Example using a Go application:

```Dockerfile
FROM registry.suse.com/bci/golang:stable as build

WORKDIR /app

RUN go install github.com/go-training/helloworld@latest

# Create an image to bundle the app
FROM registry.suse.com/bci/bci-micro:latest

COPY --from=build /go/bin/helloworld /usr/local/bin/helloworld

CMD ["/usr/local/bin/helloworld"]
```


## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
