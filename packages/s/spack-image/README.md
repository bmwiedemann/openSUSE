# Spack 0.22.0 Container Image
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description
Spack is a package manager for supercomputers. It provides build recipes
for more than 6000 software components, and it allows to build entire
HPC application stacks with little to no prerequisites.

This container image serves as a build environment for a `Dockerfile`
or an `apptainter.def` file created by `spack containerize`. It can be
used to run spack commands directly as well. Doing this may require to
bind-mount local directories into the container.

## Usage
This image may be used to build and containerize application stacks using
Spack. The stack is installed in a base container such as SLE BCI Base.
To build a containerized application stack, create the file `spack.yaml`
in an empty directory with the following content:
```yaml
spack:
  specs:
  - <application spec>

  container:
    format: <container_format>
    images:
      build: "registry.opensuse.org/opensuse/bci/spack:0.22.0"
      final: "registry.suse.com/bci/bci-base:latest"
    os_packages:
      command: zypper
      build:
      - <additional packages for building>
      final:
      - <additional packages for final container>
```
Replace 'application spec' with the actual application name, and provide optional
build specifications (for details see the
[Spack documentation](https://spack.readthedocs.io/en/latest/)).
The 'container_format' can be either `docker` for a docker/OCI container
image or `singularity` for a Singularity/Apptainer container image.
The `os_packages` section is optional. Here you may specify additional
packages to install in the build container or in the final
runtime container image.
To build an Apptainer container, run the following commands in the same
directory:
```ShellSession
$ spack containerize > apptainer.def
$ apptainer build apptainer.sif apptainer.def
```
This builds `apptainer.sif` as the final Singularity/Apptainer image that can then be run as follows:
```ShellSession
$ apptainer exec ./apptainer.sif <command line ...>
```
To build a docker/OCI container, run the following commands:
```ShellSession
$ spack containerize > Containerfile
$ podman build -t <target_name> --format=docker .
```
This builds a Docker container that you can run as follows:
```
$ podman run -it --rm <target_name> <command line ...>
```
If you do not have a local installation of Spack, you can use this container
to run Spack commands - like `spack containerize`:
```ShellSession
$ podman run -v $(pwd):/root:Z --rm registry.opensuse.org/opensuse/bci/spack:0.22.0 containerize > Containerfile
```
For further information, refer to the
[Spack documentation on container images](https://spack.readthedocs.io/en/latest/containers.html).
## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
