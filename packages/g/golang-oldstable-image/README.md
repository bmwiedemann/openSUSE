# Go 1.26 development container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

[Go](https://go.dev/) (a.k.a. Golang) is a statically-typed programming
language, with syntax loosely derived from C. Go offers additional features
such as garbage collection, type safety, certain dynamic-typing capabilities,
additional built-in types (for example, variable-length arrays and key-value
maps) and a large standard library.

## FIPS 140-3

Go binaries can natively operate in a mode that facilitates
[FIPS 140-3 compliance](https://go.dev/doc/security/fips140).
Go includes a cryptographic module certified under NIST's
Cryptographic Module Validation Program (CMVP).

### The GOFIPS140 environment variable

The `GOFIPS140` environment variable controls FIPS 140-3 mode during compilation
with `go build`, `go install`, and `go test`.

The available values are:

- **`off`** (default): Uses the standard library's cryptographic implementations in
  standard mode. The compiled binary does not enable FIPS mode by default at runtime.
- **`certified`**: Links against the latest frozen snapshot of the Go Cryptographic
  Module that has completed an official NIST CMVP validation certificate. Binaries
  compiled with `GOFIPS140=certified` automatically execute in FIPS 140-3 mode by
  default (`fips140=on`) at runtime.
- **`latest`**: Uses the current toolchain's cryptographic module and enables FIPS
  140-3 mode by default at runtime.
- **`<version>`** (for example, `v1.0.0`): Links against a specific frozen snapshot
  version of the cryptographic module.

To compile an application with the certified module enabled:

```ShellSession
$ GOFIPS140=certified go build -o myapp .
```

In a `Dockerfile`:

```Dockerfile
RUN GOFIPS140=certified go build -o /hello .
```

### The fips140 GODEBUG option

The `fips140` option in the `GODEBUG` environment variable controls FIPS 140-3 mode
during runtime execution. It defaults to `off` unless `GOFIPS140=certified` or
`GOFIPS140=latest` was specified at build time.

The possible values for `fips140` are:

- **`off`**: The Go Cryptographic Module does not operate in FIPS 140-3 mode.
- **`on`**: The Go Cryptographic Module operates in FIPS 140-3 mode. The runtime
  executes Power-On Self-Tests (POST) during initialization and key generation,
  enforces the NIST SP 800-90A DRBG for random number generation, and restricts
  `crypto/tls` to approved cipher suites, curves, and protocol versions (TLS 1.2 and TLS 1.3).
- **`only`**: Strict FIPS 140-3 mode. Cryptographic algorithms, key sizes, or
  configurations not approved by FIPS 140-3 return an error or panic. This setting
  is recommended in CI/CD pipelines to detect unapproved algorithms.

To run an application container with FIPS 140-3 mode explicitly enabled:

```ShellSession
$ podman run -e GODEBUG="fips140=on" my-golang-app
```

### Verifying the binary

To verify that a binary was compiled with the certified Go cryptographic module:

```ShellSession
$ go version -m myapp
```

The output will include the embedded module snapshot under `crypto/internal/fips140`.

### Migration from Go-openssl

Starting with Go 1.27, the legacy Go-openssl variant—which routed cryptographic
operations through OpenSSL via CGO—will no longer be supported or provided in openSUSE BCI.
All workloads requiring FIPS 140-3 compliance should migrate to this standard Go
container image.


#### How to migrate

1. Replace the legacy base image `registry.suse.com/bci/golang:<version>-openssl`
   with `registry.opensuse.org/opensuse/bci/golang:1.26`.
2. Build your binary with `GOFIPS140=certified` (for example,
   `RUN CGO_ENABLED=0 GOFIPS140=certified go build -o /hello .`).
3. Deploy the binary into a minimal container image such as `bci-nano`.


## Usage
We recommend using the Go image solely as a build environment so that
the compiler does not need to be shipped as part of deployed images.

There are two options for working with Go images. First, you can encapsulate your
application in a `bci-nano` container image, a minimal runtime environment containing
only basic locale data and CA certificates. This approach only works if your Go application does not
depend on libc or any other libraries or binaries, as they will not be available.

The second option uses a slim base container image (such as `bci-micro`) with the minimal
packages required to run the Go application.

To compile and deploy an application, copy the sources, fetch dependencies
(assuming `go.mod` is used for dependency management), and build the binary using
the following Dockerfile options.


### Building from `bci-nano`

```Dockerfile
# Build the application using the Go 1.26 development container image
FROM registry.opensuse.org/opensuse/bci/golang:1.26 AS build

WORKDIR /app

# Pre-copy/cache go.mod for pre-downloading dependencies and only
# redownloading them in subsequent builds if they change
COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . ./

# Disable CGO to create a statically linked binary using Go's built-in
# implementations rather than host operating system C libraries. This is
# required for bci-nano images as C runtime libraries (libc) are not available.
RUN CGO_ENABLED=0 go build -o /hello

# Bundle the application into a bci-nano image
FROM registry.suse.com/bci/bci-nano:latest

COPY --from=build /hello /usr/local/bin/hello

CMD ["/usr/local/bin/hello"]
```

Build and run the container image:

```ShellSession
$ podman build -t my-golang-app .
$ podman run -it --rm my-golang-app
```

To compile an application on the host using the containerized Go toolchain (without creating an application container image), run:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/golang:1.26 go build -v
```

To run application tests inside a container, run:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/golang:1.26 go test -v
```


### Building from openSUSE BCI

The [openSUSE BCI General Purpose Base Container Images](https://opensource.suse.com/bci-docs/documentation/general-purpose-bci/)
documentation describes four different options for deployment, depending on your exact requirements.

```Dockerfile
# Build the application using the Go 1.26 development container image
FROM registry.opensuse.org/opensuse/bci/golang:1.26 AS build

WORKDIR /app

# Pre-copy/cache go.mod for pre-downloading dependencies and only
# redownloading them in subsequent builds if they change
COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . ./

RUN go build -o /hello

# Bundle the application into a bci-micro image
FROM registry.opensuse.org/opensuse/bci/bci-micro:latest

COPY --from=build /hello /usr/local/bin/hello

CMD ["/usr/local/bin/hello"]
```

The above example uses the openSUSE BCI micro image as the deployment image for
the resulting application. See the [openSUSE BCI use with Go
documentation](https://opensource.suse.com/bci-docs/guides/use-with-golang/)
for further details.


## Additional tools

In addition to the standard openSUSE BCI development packages, the following tools
are included in the image:

- go1.26-race
- make

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
