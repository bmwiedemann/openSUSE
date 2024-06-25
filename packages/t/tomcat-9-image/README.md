# Tomcat 9 container image
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description
Apache Tomcat (Tomcat for short) is a free and open-source implementation of the
Jakarta Servlet, Jakarta Expression Language, and WebSocket technologies. It
provides a pure Java HTTP web server environment that can run Java code. It is a
Java web application server and not a complete JEE application server.


## Usage
By default, the image launches Tomcat with the same configuration as the one
that comes with SUSE Linux Enterprise Server. The difference is that logging is
sent to stdout, meaning that the `podman logs tomcat` command displays Tomcat
logs.

For security reasons, the image runs as the **tomcat** user. This means that
additional packages cannot be installed via `zypper`, unless the user becomes
`root`.

To deploy an application, copy the `.war` file into
`$CATALINA_BASE/webapps` (either during a container build or by bind-mounting
the directory), and launch the container using the following command:
```ShellSession
$ podman run -d --rm -p 8080:8080 registry.opensuse.org/opensuse/tomcat:9
```

The deployed webapp is then accessible via `http://localhost:8080/$webapp_name`.


### How to use the image with rootless Podman

The container image can be used in rootless mode with Podman. Keep in mind that
Podman remaps the `tomcat` user in the container to a different user on the
host. This user does not have write access to the mounted directory. To avoid
permission issues change permissions of the shared directory to `0777` as
follows:

```ShellSession
$ chmod 0777 /path/to/my/app
$ podman run --rm -d -v /path/to/my/app:/usr/share/tomcat/webapps:z \
      -p 8080:8080 registry.opensuse.org/opensuse/tomcat:9
```


## Configuration

The main Tomcat configuration files (for example
`/etc/tomcat/logging.properties`) are stored in `/etc/tomcat/`.

Tomcat's runtime options can be configured using the environment variables
`JAVA_OPTS` and `CATALINA_OPTS`. `JAVA_OPTS` specifies general options used for
the JVM, whereas `CATALINA_OPTS` specifies Tomcat's flags. You can pass the
options to the container runtime using the `-e` flag:
```ShellSession
$ podman run -it --rm \
      -e JAVA_OPTS="-Xmx1024m" -p 8080:8080 \
      registry.opensuse.org/opensuse/tomcat:9
```

The image ships with `CATALINA_HOME` set to `/usr/share/tomcat`
and `CATALINA_BASE` set to `/usr/share/tomcat`.


## Samples

By default, the sample applications shipped with Tomcat are not installed in
the container image. Add them by installing one of the following
packages:
- tomcat-webapps
- tomcat-admin-webapps



## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
