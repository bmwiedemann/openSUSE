# PHP8/Nginx container

This container image contains PHP8 with Nginx as webserver

- [Guide](#guide)
  - [Run a new php8 instance](#run-a-new-php8-instance)
  - [Environment variables](#environment-variables)

## Guide

### Run a new PHP8 instance

The command to run this container is:

```sh
podman run -d --rm --name php8-nginx -v /srv/www/htdocs:/srv/www/htdocs registry.opensuse.org/opensuse/php8-nginx
```

### Environment variables:
```
  DEBUG=[0|1]           Enable debug mode
  TZ=<timezone>         Set timezone
```
Additional Environment variables can be found in the description for the openSUSE nginx container image.
