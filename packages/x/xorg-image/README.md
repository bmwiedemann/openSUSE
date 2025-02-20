# openSUSE Tumbleweed Xorg Server
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

X.Org Server is the free and open-source implementation of the X Window System
(X11) display server stewarded by the X.Org Foundation.


## Usage

This container image is intended for consumption via a helm chart which launches
the container in the intended fashion.

To launch the container manually, switch to a tty and execute the following
command as `root`:

```ShellSession
# podman run \
      --privileged -d \
      -e XAUTHORITY=/home/user/xauthority/.xauth \
      -v xauthority:/home/user/xauthority:rw \
      -v xsocket:/tmp/.X11-unix:rw \
      -v /run/udev/data:/run/udev/data:rw \
      --security-opt=no-new-privileges \
      registry.opensuse.org/opensuse/xorg:21
```

The volumes are optional and can be omitted if you wish to only start X. The
volumes are necessary to launch additional graphical applications using the
containerized Xorg container.


## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
