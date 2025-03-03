# Ruby 3.4 Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

[Ruby](https://www.ruby-lang.org/) is a dynamic, reflective, object-oriented, general-purpose, open-source programming language. It supports multiple programming paradigms, including functional, object-oriented, and imperative. It also has a dynamic type system and automatic memory management.

## Usage

To deploy an application, install dependencies, copy the sources, and configure the application's main script:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/ruby:3.4

# displays an error message if Gemfile and Gemfile.lock are not in sync
RUN bundle config --global frozen 1

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

CMD [ "ruby", "./main-script.rb" ]
```

Build and run the container image:

```ShellSession
$ podman build -t my-ruby-app .
$ podman run -it --rm my-ruby-app
```

The example above assumes that there is a `Gemfile.lock` file in the application directory.
To generate a `Gemfile.lock` file, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/ruby:3.4 bundle lock
```

To run a single script inside a container, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/ruby:3.4 ruby script.rb
```

## Encoding

The Ruby image sets the locale environment variable `LANG` to `C.UTF-8`.

## Additional tools

In addition to the standard SLE BCI development packages the following
additional tools are included in the image:

- gcc-c++
- make
- sqlite3-devel
- timezone

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
