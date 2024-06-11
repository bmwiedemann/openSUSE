# PostgreSQL 15 Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

PostgreSQL (often spelled as Postgres) is an extensible and SQL-compliant relational database management system (RDBMS).

PostgreSQL implements most of the SQL:2011 standard, and the RDBMS is ACID-compliant and transactional (including most DDL statements). The latter prevents locking issues using multiversion concurrency control (MVCC) as well as provides immunity to dirty reads and full serializability. PostgreSQL can handle complex SQL queries using different indexing methods that are not available in other databases. It features updateable views and materialized views, triggers, and foreign keys. The RDBMS supports functions and stored procedures. PostgreSQL's functionality can be extended using a vast collection of available extensions.

## Usage

By default, the image launches PostgreSQL with the same configuration that comes with SUSE Linux Enterprise Server.

The only environment variable required to start the container is the PostgreSQL root password.

```ShellSession
$ podman run -it --rm -p 5432:5432 -e POSTGRES_PASSWORD=my-password -v /path/to/data:/var/lib/pgsql/data:Z registry.opensuse.org/opensuse/postgres:15
```

## Volumes

### `/var/lib/pgsql/data`

PostgreSQL data directory location.

## Environment variables

The PostgreSQL image uses several environment variables to configure the database initialization.

The only mandatory variable is `POSTGRES_PASSWORD`; other environment variables are optional.

### POSTGRES_PASSWORD

The `POSTGRES_PASSWORD` environment variable is required to use the PostgreSQL image. It must not be empty or undefined. This environment variable sets the superuser password for PostgreSQL.

### POSTGRES_USER

This optional environment variable is used in conjunction with `POSTGRES_PASSWORD` to set a user and its password. This variable creates the specified user with superuser power and a database with the same name. If it is not specified, the default user of `postgres` is used.

### POSTGRES_DB

This optional environment variable can be used to define a different name for the default database created when the image is first started. If it is not specified, the value of `POSTGRES_USER` is used.

### POSTGRES_INITDB_ARGS

This optional environment variable can be used to send arguments to `postgres initdb`. The value is a space-separated string of arguments as `postgres initdb` expects them. This is useful for adding actions like data page checksums: `-e POSTGRES_INITDB_ARGS="--data-checksums"`.

### POSTGRES_INITDB_WALDIR

This optional environment variable can be used to define another location for the Postgres transaction log. By default, the transaction log is stored in a subdirectory of the main Postgres data folder (`PGDATA`). In certain situations, it is desirable to store the transaction log in a different directory that may be backed by storage with different performance or reliability characteristics.

### POSTGRES_HOST_AUTH_METHOD

This optional variable can be used to control the `auth-method` for host connections for all databases, users, and addresses. If unspecified, the `scram-sha-256` password authentication is used.

On an uninitialized database, this populates `pg_hba.conf` via this approximate line:

`echo "host all all all $POSTGRES_HOST_AUTH_METHOD" >> pg_hba.conf`

For more information about possible values and their meanings, refer to the PostgreSQL documentation on [password Authentication](https://www.postgresql.org/docs/14/auth-password.html) and [pg_hba.conf](https://www.postgresql.org/docs/14/auth-pg-hba-conf.html).

**Note 1:** If you set `POSTGRES_HOST_AUTH_METHOD` to `trust`, then `POSTGRES_PASSWORD` is not required, since it allows anyone to connect without a password.

**Note 2:** If you set `POSTGRES_HOST_AUTH_METHOD` to an alternative value, you might need additional `POSTGRES_INITDB_ARGS` for the database to initialize correctly.

### PGDATA

The value for this variable is `/var/lib/pgsql/data`. This location is a volume and another location is currently not supported.

## Sensitive information

As an alternative to passing sensitive information via environment variables, `_FILE` can be appended to `POSTGRES_INITDB_ARGS`, `POSTGRES_PASSWORD`, `POSTGRES_USER`, and `POSTGRES_DB` environment variables. This makes the initialization script load the values for those variables from files present in the container. To, e.g., pass the password securely, you can store the password in a secret called `postgress-pw` and launch the container as follows:

```ShellSession
$ podman run -it --rm
    -p 5432:5432 \
    -e POSTGRES_PASSWORD_FILE=/run/secrets/postgress-pw \
    --secret postgress-pw \
    -v /path/to/data:/var/lib/pgsql/data:Z \
    registry.opensuse.org/opensuse/postgres:15
```

## Health, liveness, and readiness

There is one explicit health check added to the container image. This check executes the `pg_isready` for host `localhost` and port `5432`.

The utility [pg_isread](https://www.postgresql.org/docs/current/app-pg-isready.html) checks the connection status of the server, and the exit status specifies the result of the connection check.

## Initialization scripts

To perform additional initialization in an image derived from this one, add one or more `*.sql`, `*.sql.gz`, or `*.sh` scripts under `/docker-entrypoint-initdb.d`. After the entrypoint calls `initdb` to create the default PostgreSQL user and database, it runs any `*.sql` files, runs any executable `*.sh` scripts, and sources any non-executable `*.sh` scripts found in that directory to perform further initialization before starting the service.

**Warning:** Scripts in `/docker-entrypoint-initdb.d` are only executed when you start the container with an empty data directory. Any pre-existing databases are left untouched when the container starts.

**Note:** If one of the `/docker-entrypoint-initdb.d` scripts fails, and the container restarts with the already initialized data directory, it aborts the running scripts.

## Database configuration

For information on the available configuration options, refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config.html) covering the specific version of your PostgreSQL server.

Below is a list of the most common configuration options:

- Set options directly on the container run line via `-c`.
- Use a custom configuration file and mount it.

**Note:** Configuration files (`postgresql.auto.conf`, `postgresql.conf`, `pg_hba.conf`, and `pg_ident.conf`) are stored in the location defined in `PGDATA`.

## Backup and restore

The utilities `pg_dump` and `pg_dumpall` are available in the container.

To dump the entire contents of a database cluster, run the following command:

```ShellSession
$ podman exec -t $CONTAINER_ID pg_dumpall -c -U $POSTGRES_USER > dump.sql
```

To restore a dump, run the following command:

```ShellSession
$ cat dump.sql | podman exec -i $CONTAINER_ID psql -U $POSTGRES_USER -d $POSTGRES_DB
```

For more information on how to perform backup and restore, refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/backup.html).

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
