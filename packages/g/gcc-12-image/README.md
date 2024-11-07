# openSUSE Tumbleweed BCI GNU Compiler Collection container image (GCC)
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

# Description
The GNU Compiler Collection (GCC) is an optimizing compiler for various
architectures and operating systems. It is the default compiler in the GNU
project and most Linux distributions, including SUSE Linux Enterprise and
openSUSE.


## Usage

### Compile an application with a `Dockerfile`

Normally, you'd want to compile an application and distribute it as part of a
custom container image. To do this, create a `Dockerfile` similar to the one
below. The `Dockerfile` uses this image to build a custom container image,
copies the sources to a working directory, and compiles the application:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/gcc:12
WORKDIR /src/
COPY . /src/
RUN gcc main.c src1.c src2.c
CMD ["./a.out"]
```

It is also possible to compile a static binary with gcc as part of a multistage
build:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/gcc:12 as builder
WORKDIR /src/
COPY . /src/
RUN gcc -o app main.c src1.c src2.c

FROM registry.opensuse.org/opensuse/bci/bci-micro:latest
WORKDIR /build/
COPY --from=builder /src/app /build/
CMD ["/build/app"]
```

Note that you must build a static binary to deploy it into bci-micro; otherwise
shared libraries might be missing. You cannot deploy such an app into a
`scratch` image, as it is not possible to statically link glibc.


### Available build systems

The container image comes with `make` by default. Other build systems and
related utilities are available in the repository, and they can be installed
using `zypper`. This includes the following:
- `meson`
- `cmake`
- `ninja`
- `autoconf` & `automake`


### Available compiler frontends

The GNU Compiler Collections supports a wide range of frontends. The container
image ships the C,  C++  and fortran frontends available as `gcc`, `g++` and `gfortran`
respectively. The following additional frontends can be installed from the
repository:
- `gcc12-ada` for the Ada frontend (GNAT)
- `gcc12-go` for the Go frontend
- `gcc12-objc` and `gcc12-obj-c++` for the Objective C and Objective C++
- `gcc12-d` for the frontend to the D Language


### Using the container image interactively

You can use the image to create ephemeral containers that execute only gcc. This
can be useful in situations, where building a full container image is not
practical. One way to do this is to mount the working directory of an
application into the launched container and compile the application there:

```bash
podman run --rm -it -v $(pwd):/src/:Z registry.opensuse.org/opensuse/bci/gcc:12 \
    gcc -o /src/app.out /src/*.c
```
or by invoking `make`
```bash
podman run --rm -it -v $(pwd):/src/:Z --workdir /src/ \
    registry.opensuse.org/opensuse/bci/gcc:12 \
    make
```

Note that the binary built using this approach are unlikely to work on a local
machine. They only work on operating systems that are binary-compatible to
openSUSE Tumbleweed.

## Licensing

`SPDX-License-Identifier: GPL-3.0-or-later`

This documentation and the build recipe are licensed as GPL-3.0-or-later.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
