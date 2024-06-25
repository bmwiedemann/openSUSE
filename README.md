# Go 1.22 development container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

[Go](https://go.dev/) (a.k.a., Golang) is a statically-typed programming
language, with syntax loosely derived from C. Go offers additional features
such as garbage collection, type safety, certain dynamic-typing capabilities,
additional built-in types (for example, variable-length arrays and key-value
maps) as well as a large standard library.


## Usage
We recommend using the Go image as a build environment. Thus,  
the compiler does not need to be shipped as part of the images that are
deployed. Instead, we recommend to use the Go image as the
builder image only.

There are two options to work with Go images. First, you can encapsulate your
application in a `scratch` container image, essentially an empty filesystem
image. This approach only works if your Go application does not depend on libc
or any other library or files, as they will not be available.

The second option uses a slim base container image with just the minimal
packages required to run the Go application.

To compile and deploy an application, copy the sources, fetch dependencies
(assuming go.mod is used for dependency management), and build the binary using
the following Dockerfile options.


### Building from `scratch`

```Dockerfile
# Build the application using the Go 1.22 development container image
FROM registry.opensuse.org/opensuse/bci/golang:1.22 as build

WORKDIR /app

# pre-copy/cache go.mod for pre-downloading dependencies and only
# redownloading them in subsequent builds if they change
COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . ./

# Make sure to build the application with CGO disabled.
# This will force Go to use some Go implementations of code
# rather than those supplied by the host operating system.
# You need this for scratch images as those supporting libraries
# are not available.
RUN CGO_ENABLED=0 go build -o /hello

# Bundle the application into a scratch image
FROM scratch

COPY --from=build /hello /usr/local/bin/hello

CMD ["/usr/local/bin/hello"]
```

Build and run the container image:

```ShellSession
$ podman build -t my-golang-app .
$ podman run -it --rm my-golang-app
```

There are situations when you don't want to run an application inside a container.

To compile the application, without running it inside a container instance, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/golang:1.22 go build -v
```

To run the application tests inside a container, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/golang:1.22 go test -v
```


### Building from SLE BCI

The [SLE BCI General Purpose Base Containers](https://opensource.suse.com/bci-docs/documentation/general-purpose-bci/)
images offer four different options for deployment, depending on your exact requirements.

```Dockerfile
# Build the application using the Go 1.22 development Container Image
FROM registry.opensuse.org/opensuse/bci/golang:1.22 as build

WORKDIR /app

# pre-copy/cache go.mod for pre-downloading dependencies and only
# redownloading them in subsequent builds if they change
COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . ./

RUN go build -o /hello

# Bundle the application into a scratch image
FROM registry.suse.com/bci/bci-micro:15.4

COPY --from=build /hello /usr/local/bin/hello

CMD ["/usr/local/bin/hello"]
```

The above example uses the SLE BCI micro image as the deployment image for
the resulting application. See the [SLE BCI use with Go
documentation](https://opensource.suse.com/bci-docs/guides/use-with-golang/)
for further details.


## Additional tools

The following tools are also included in the image:

- go1.22-race
- make
- git-core

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
