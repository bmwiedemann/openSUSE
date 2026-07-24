# NGINX container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

nginx (pronounced "engine-x") is an open source reverse proxy server for the HTTP, HTTPS, SMTP, POP3 and IMAP protocols. nginx can also act as a load balancer, HTTP cache and Web server (origin server).

## Usage

By default, the image launches nginx with the same configuration that comes with SUSE Linux Enterprise Server.

```ShellSession
$ podman run -it --rm -p 8080:80 registry.opensuse.org/opensuse/nginx:1.31
```

Or:

```ShellSession
$ podman run -it --rm -p 8080:80 -v /path/to/html/:/srv/www/htdocs/:Z registry.opensuse.org/opensuse/nginx:1.31
```

**Note:** The directory `/srv/www/htdocs/` is the root directory used by the default server. Additional servers can use any other path.

You can access the served content on http://localhost:8080 or http://host-ip:8080.

## Using templates

By default, nginx does not support environment variables inside configuration blocks. This image includes a script that extracts environment variables before nginx creates the configuration files.

The script reads `.template` files stored in `/etc/nginx/templates/` and saves the results of the [`envsubst`](https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html) command to the `/etc/nginx/conf.d/` directory.

For example, to configure nginx to use port 80, create a file named `/etc/nginx/templates/default.conf.template` containing the following variable definition:

```nginx
listen  ${NGINX_PORT};
```

This template is rendered to `/etc/nginx/conf.d/default.conf` as follows:

```nginx
listen  80;
```

## Running nginx as a non-root user

To run the image as a less-privileged `nginx` user, run the following command:

```ShellSession
$ podman run -it --user nginx --rm -p 8080:8080 -v /path/to/html/:/srv/www/htdocs/:Z registry.opensuse.org/opensuse/nginx:1.31
```

The included script `40-unprivileged-mode.sh` changes the default listening port from 80 to 8080, removes the `user` directive from `/etc/nginx/nginx.conf`,
 and configures temporary paths and the PID file to use writable locations under `/tmp` and `/var/run/nginx`, respectively.

**Note:** When running as the `nginx` user, the default port is 8080.

## Environment variables

### NGINX_ENTRYPOINT_QUIET_LOGS

This optional environment variable controls logging during container startup. Set its value to `1` to silence startup logs.

### NGINX_ENTRYPOINT_WORKER_PROCESSES_AUTOTUNE

This optional environment variable enables automatic tuning of the number of worker processes. Set its value to `1` to enable autotuning of the worker processes (disabled by default).

### NGINX_ENVSUBST_TEMPLATE_DIR

This optional environment variable specifies the directory containing template files (default is `/etc/nginx/templates`).

**Note:** The script skips template processing if this directory does not exist.

### NGINX_ENVSUBST_OUTPUT_DIR

This optional environment variable specifies the directory for storing the results of running [`envsubst`](https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html) on templates (default is `/etc/nginx/conf.d`).

The output filename is the template filename with the `.template` suffix removed.

**Note:** Modifying this variable requires updating `nginx.conf` so that it recognizes the new directory location.

### NGINX_ENVSUBST_TEMPLATE_SUFFIX

This optional environment variable changes the suffix of template files (default is `.template`).

**Note:** The script only processes files with the specified suffix.

### NGINX_ENVSUBST_FILTER

This optional environment variable enables filtering of environment variables during template processing. Environment variables that do not match the regular expression defined by `NGINX_ENVSUBST_FILTER` are not replaced.

## Configuration scripts

To run custom initialization scripts, add one or more `*.envsh` or `*.sh` scripts under `/docker-entrypoint.d/`. Any executable `*.envsh` or `*.sh` script found in this directory is executed before starting NGINX.

Currently, the container image ships with the following helper scripts:

- `20-envsubst-on-templates.sh` - Enables the use of environment variables in templates.
- `30-tune-worker-processes.sh` - Enables autotuning the number of nginx worker processes.
- `40-unprivileged-mode.sh` - Enables running in unprivileged mode if the container is started as a non-root user (UID > 0).

**Warning:** The container startup is aborted if any script exits with an error.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
