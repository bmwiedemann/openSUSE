# The PHP Apache 8 container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

PHP is a general-purpose scripting language used primarily for server-side web
development. It can be used directly, embedded in HTML files, or executed via a
server-side Apache2 module or CGI scripts.

## How to use the image

The image ships with the Apache web server and the `mod_php` module.

To deploy an application, copy its sources into the htdocs folder
`/srv/www/htdocs` (this directory is the `WORKDIR` of the container image):

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-apache:8

RUN set -eux; \
    zypper -n in $my_dependencies; \
    # additional setup steps

# Copy the app into the Apache2 document root
COPY app/ .
```

Build the image and run the resulting container:

```ShellSession
$ buildah bud -t my-app .
$ podman run -d -p 8080:80 my-app
```

Alternatively, you can mount the application's source code directly into the
container:

```ShellSession
$ podman run -d -p 8080:80 -v ./app/:/srv/www/htdocs:Z registry.opensuse.org/opensuse/bci/php-apache:8-%RELEASE%
```

## How to install PHP extensions

PHP extensions must be installed using the `zypper` package manager. PHP
extensions are named using the `php8-$extension_name` scheme,
and they can be installed as follows:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-apache:8

RUN zypper -n in php8-gd php8-intl
```

Alternatively, you can use the `docker-php-ext-install` script. It is provided
for compatibility with the [PHP DockerHub Image](https://hub.docker.com/_/php)
but it uses zypper to install the extensions from RPMs. It is provided for
compatibility reasons and can be used similar to the script from PHP DockerHub
image:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-apache:8

RUN docker-php-ext-install gd intl
```

## How to install PECL extensions

[PECL](https://pecl.php.net/) is a package repository hosting PHP extensions. It
can be used as an alternative source to obtain PHP extensions, but without any
guarantee of interoperability with this image and without any official support.

PECL extensions can be installed as follows:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-apache:8

RUN set -euo pipefail; \
    zypper -n in $PHPIZE_DEPS php8-pecl; \
    pecl install APCu-5.1.21;
```

**Note:** Building an extension may require installing additional dependencies.


## Compatibility with the DockerHub Image

The following scripts ship with the image to keep it compatible with the
DockerHub image: `docker-php-source`, `docker-php-ext-configure`,
`docker-php-ext-enable`, and `docker-php-ext-install`. Note that only
`docker-php-ext-install` performs an actual job. None of the other scripts
require to be executed in the image.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
