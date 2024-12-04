# openSUSE Tumbleweed with Git: Git application container
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)


## Description

Git is a distributed version control system that tracks
versions of files. Git is primarily designed for controlling source code in collaborative software development.


## Usage

This container provides the openSUSE Project version of Git.

Example of using Git container:

```ShellSession
$ podman run registry.opensuse.org/opensuse/git:2.47 git help
```

As Git requires a repository, the container
does not explicitly set an entrypoint. This way, you can launch the container in
interactive mode to clone a repository and work on it. To avoid losing all your changes when exiting the container, use a persistent volume mount on launch.

For more use cases and documentation, refer to the
[Git SCM documentation](https://git-scm.com/doc).


## Licensing

`SPDX-License-Identifier: GPL-2.0-only`

This documentation and the build recipe are licensed as GPL-2.0-only.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
