# MariaDB Server container image

## Description
MariaDB is an open-source, multi-threaded, relational database management system. It's a backward-compatible branch of the MySQL Community Server that provides a drop-in replacement for MySQL.


## Usage
By default, the image launches MariaDB with the same configuration that comes with SUSE Linux Enterprise Server, with two exceptions: logging is sent to stdout, and binding to `localhost` is disabled.

The only environment variable required to start the container is the MariaDB root password.

```ShellSession
$ podman run -it --rm -p 3306:3306 -e MARIADB_ROOT_PASSWORD=my-password registry.opensuse.org/opensuse/mariadb:11.2
```

or:

```ShellSession
$ podman run -it --rm -p 3306:3306 -e MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=1 registry.opensuse.org/opensuse/mariadb:11.2
```

### Volumes

The database is stored in the directory `/var/lib/mysql`.

When using the MariaDB image, we recommend one of the following options:

* Use a named volume to manage the storage of your database data. This is the default option and it is easy to use. The downside is that the files may be hard to locate for tools and applications that run directly on the host system, i.e. outside containers.
* Create a data directory on the host system (outside the container) and mount the created directory to a directory accessible from inside the container. This stores the database files in a known location on the host system and makes it easy for tools and applications on the host system to access the files. If you choose this approach, make sure that the specified directory exists, and its permissions along with other security mechanisms on the host system are set up correctly.

To mount a host directory as a volume for your data run the following command:

```ShellSession
$ podman run -it --rm -v /my/own/datadir:/var/lib/mysql:Z -p 3306:3306 -e MARIADB_ROOT_PASSWORD=my-password registry.opensuse.org/opensuse/mariadb:11.2
```

The `-v /my/own/datadir:/var/lib/mysql:Z` part of the command mounts the `/my/own/datadir` directory from the underlying host system as `/var/lib/mysql` inside the container, where MariaDB will by default write its data files.

### Environment variables

One of `MARIADB_RANDOM_ROOT_PASSWORD`, `MARIADB_ROOT_PASSWORD_HASH`, `MARIADB_ROOT_PASSWORD` or `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD` (or equivalents, including `*_FILE`), is required.

All other environment variables are optional.

All environment variables are documented in the MariaDB's Knowledge Base [MariaDB Server Docker Official Image Environment Variables](https://mariadb.com/kb/en/mariadb-server-docker-official-image-environment-variables/).

### Health, liveness and readiness

There are no explicit health checks added to the container image. However, you can use the `healthcheck.sh` script to choose from a limited selection of tests to check for what you consider health, liveness, and readiness.

If there is no database initialized when the container starts, a default database is created. This means that incoming connections are not accepted until the initialization is completed. Use the `healthcheck.sh` script to check for container readiness.

To learn about `healthcheck.sh`, how to use it, and what tests are provided, refer to the MariaDB's Knowledge Base [Using Healthcheck.sh](https://mariadb.com/kb/en/using-healthcheck-sh/).

## Usage against an existing database

If you start a MariaDB container instance with a data directory that already contains a database (specifically, a MySQL subdirectory), no environment variables that control initialization are needed or examined, and no pre-existing databases are changed.

The only exception is the `MARIADB_AUTO_UPGRADE` environment variable. If it's set, it may run `mysql_upgrade` or `mariadb-upgrade`, potentially causing changes to the system tables.

### Backup and restore

Information on how to perform backup and restore can be found on the MariaDB Knowledge Base [Container Backup and Restoration](https://mariadb.com/kb/en/container-backup-and-restoration/).

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
