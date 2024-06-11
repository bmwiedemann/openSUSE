# The PHP FPM 8 Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

PHP is a general-purpose scripting language used primarily for server-side web
development. It can be used directly, embedded in HTML files, or executed via a
server-side Apache2 module or CGI scripts.

## How to use the image

The image contains [PHP-FPM](https://php-fpm.org/), a FastCGI implementation
for PHP that serves content via the FastCGI protocol and not via HTTP(S). This
requires a reverse proxy that can handle FastCGI and can serve content via
HTTP(s).

**Caution:** FastCGI does not offer any protection or access control, so the
open socket must be protected via network separation. This means that the
PHP-FPM container must run in a separate private network or a pod, and its
socket must be exposed to the reverse proxy only.

To deploy an application in the PHP-FPM container, copy the application into
`/srv/www/htdocs` (this directory is the `WORKDIR` of the container image):

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-fpm:8

RUN set -eux; \
    zypper -n in $my_dependencies; \
    # additional setup steps

# Copy the app into the PHP-FPM document root
COPY app/ .
```

To configure NGINX as a reverse proxy, add the following to the
`server` section in `/etc/nginx/nginx.conf`:
```
        location ~ \.php$ {
           include                   fastcgi_params;
           fastcgi_index             index.php;
           root           /srv/www/htdocs/;
           fastcgi_pass   127.0.0.1:9000;
           fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        }
```

Additionally, create `/etc/nginx/fastcgi_params` with the following contents:
```
fastcgi_param  QUERY_STRING       $query_string;
fastcgi_param  REQUEST_METHOD     $request_method;
fastcgi_param  CONTENT_TYPE       $content_type;
fastcgi_param  CONTENT_LENGTH     $content_length;

fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
fastcgi_param  REQUEST_URI        $request_uri;
fastcgi_param  DOCUMENT_URI       $document_uri;
fastcgi_param  DOCUMENT_ROOT      $document_root;
fastcgi_param  SERVER_PROTOCOL    $server_protocol;
fastcgi_param  REQUEST_SCHEME     $scheme;
fastcgi_param  HTTPS              $https if_not_empty;

fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;

fastcgi_param  REMOTE_ADDR        $remote_addr;
fastcgi_param  REMOTE_PORT        $remote_port;
fastcgi_param  SERVER_ADDR        $server_addr;
fastcgi_param  SERVER_PORT        $server_port;
fastcgi_param  SERVER_NAME        $server_name;

# PHP only, required if PHP was built with --enable-force-cgi-redirect
fastcgi_param  REDIRECT_STATUS    200;
```

If you are using a NGINX container with the above changes, you can
use a Podman pod to deploy the application:
```ShellSession
$ podman pod create --name fpm -p 80:8080
$ podman run -d --pod fpm name-of-my-fpm-container
$ podman run -d --pod fpm name-of-my-nginx-container
```

The website is served on port 8080, and the FastCGI application is not
accessible from outside of the `fpm` pod.

## How to install PHP extensions

PHP extensions must be installed using the `zypper` package manager. PHP
extensions are named using the `php8-$extension_name` scheme,
and they can be installed as follows:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-fpm:8

RUN zypper -n in php8-gd php8-intl
```

Alternatively, you can use the `docker-php-ext-install` script. It is provided
for compatibility with the [PHP DockerHub Image](https://hub.docker.com/_/php)
but it uses zypper to install the extensions from RPMs. It is provided for
compatibility reasons and can be used similar to the script from PHP DockerHub
image:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-fpm:8

RUN docker-php-ext-install gd intl
```

## How to install PECL extensions

[PECL](https://pecl.php.net/) is a package repository hosting PHP extensions. It
can be used as an alternative source to obtain PHP extensions, but without any
guarantee of interoperability with this image and without any official support.

PECL extensions can be installed as follows:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/php-fpm:8

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
