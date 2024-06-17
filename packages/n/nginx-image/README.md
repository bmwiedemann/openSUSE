# NGINX container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

nginx (pronounced "engine-x") is an open-source reverse proxy server for the HTTP, HTTPS, SMTP, POP3, and IMAP protocols. nginx can also act as a load balancer, HTTP cache, and a web server (origin server).

## Usage

By default, the image launches nginx with the same configuration that comes with the SUSE Linux Enterprise Server.

```ShellSession
$ podman run -it --rm -p 8080:80 registry.opensuse.org/opensuse/nginx:1.27
```

Or:

```ShellSession
$ podman run -it --rm -p 8080:80 -v /path/to/html/:/srv/www/htdocs/:Z registry.opensuse.org/opensuse/nginx:1.27
```

**Note:** The directory `/srv/www/htdocs/` is the root directory used by the default server. Additional servers can use any other path.

You can access the served content on http://localhost:8080 or http://host-ip:8080.

## Using templates

By default, nginx doesn't support environment variables inside configuration blocks. This image includes a script that can extract environment variables before nginx creates configuration files.

The script reads `.template` files stored in `/etc/nginx/templates/` and saves the result of the [`envsubst`](https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html) command to the directory `/etc/nginx/conf.d/`.

For example, if you want nginx to use port 80, create a file named `/etc/nginx/templates/default.conf.template` containing the following variable definition:

```nginx
listen  ${NGINX_PORT};
```

The template above is then rendered to `/etc/nginx/conf.d/default.conf` as follows:

```nginx
listen  80;
```

## Environment variables

### NGINX_ENTRYPOINT_QUIET_LOGS

This optional environment variable controls the logging during container startup. Set the value to `1` to silence logs.

### NGINX_ENTRYPOINT_WORKER_PROCESSES_AUTOTUNE

This optional environment variable enables a script to autotune the number of worker processes. Set the value to `1` to enable autotune of the worker process parameter (default is disabled).

### NGINX_ENVSUBST_TEMPLATE_DIR

This optional environment variable specifies a directory containing template files (default is `/etc/nginx/templates`).

**Note:** The script ignores template processing if this directory doesn't exist

### NGINX_ENVSUBST_OUTPUT_DIR

This optional environment variable specifies a directory for storing results of running [`envsubst`](https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html) on templates (default is `/etc/nginx/conf.d`).

The output filename is the template filename with the suffix `.template` removed.

**Note:** Modifying this variable also requires changing the `nginx.conf`, so it recognizes the new directory location.

### NGINX_ENVSUBST_TEMPLATE_SUFFIX

This optional environment variable changes the suffix of template files (default is `.template`).

**Note:** The script only processes files that have the specified suffix in their names.

### NGINX_ENVSUBST_FILTER

This optional environment variable enables filtering out variables in the template processing. Environment variables that do not match the regular expression defined by `NGINX_ENVSUBST_FILTER` are not replaced.

## Configuration scripts

To use scripts to perform configuration actions, add one or more `*.envsh` or `*.sh` scripts under `/docker-entrypoint.d/`. Any executable `*.envsh` or `*.sh` script found in the directory is executed before starting the service, which can be used to perform further configuration steps.

Currently, the container image ships with the following helper scripts:

- `20-envsubst-on-templates.sh` - Enables the use of environment variables in templates.
- `30-tune-worker-processes.sh` - Enables autotuning the number of worker processes.

**Warning:** The container startup is aborted if any of the scripts exits with an error.

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
