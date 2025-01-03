# OpenJDK 17 development container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

[OpenJDK](https://openjdk.org/) (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE). OpenJDK is the official reference implementation of Java SE since version 7.

The OpenJDK development image is intended to be used as a build environment. For runtime, use the OpenJDK runtime image.

## Usage

To compile and deploy an application, copy the sources and build the binary:

```Dockerfile
# Build the application using the OpenJDK development image
FROM registry.opensuse.org/opensuse/bci/openjdk-devel:17 as build

WORKDIR /app

COPY . ./

RUN javac Hello.java

# Bundle the application into OpenJDK runtime image
FROM registry.opensuse.org/opensuse/bci/openjdk:17

WORKDIR /app

COPY --from=build /app/Hello.class /app

CMD ["java", "Hello"]
```

Build and run the container image:

```ShellSession
$ podman build -t my-java-app .
$ podman run -it --rm my-java-app
```

There are situations, where you don't want to run an application inside a container.

To compile the application, without running it inside a container instance, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/openjdk-devel:17 javac Hello.java
```

## Additional tools

The OpenJDK 17 development image includes [Git](https://git-scm.com/) and [Apache Maven](https://maven.apache.org/). [Apache Ant](https://ant.apache.org/) is available in the repositories.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
