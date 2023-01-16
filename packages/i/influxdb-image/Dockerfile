# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/influxdb:latest
#!BuildTag: opensuse/influxdb:%%MINOR%%
#!BuildTag: opensuse/influxdb:%%PKG_VERSION%%
#!BuildTag: opensuse/influxdb:%%PKG_VERSION%%-%RELEASE%

FROM opensuse/tumbleweed
LABEL maintainer="Thorsten Kukuk <kukuk@suse.com>"

# labelprefix=org.opensuse.influxdb
PREFIXEDLABEL org.opencontainers.image.title="InfluxDB v1.x container"
PREFIXEDLABEL org.opencontainers.image.description="InfluxDB v1.x container"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%-%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/influxdb:%%PKG_VERSION%%-%RELEASE%"

COPY entrypoint.sh /entrypoint.sh
COPY init-influxdb.sh /init-influxdb.sh

RUN zypper --non-interactive install --no-recommends influxdb && zypper clean && chmod 755 /entrypoint.sh /init-influxdb.sh

EXPOSE 8086
EXPOSE 6060
VOLUME /var/lib/influxdb

ENTRYPOINT ["/entrypoint.sh"]
CMD ["influxd"]
