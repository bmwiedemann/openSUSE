# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/memcached:latest
#!BuildTag: opensuse/memcached:%%MINOR%%
#!BuildTag: opensuse/memcached:%%PKG_VERSION%%
#!BuildTag: opensuse/memcached:%%PKG_VERSION%%-%RELEASE%
FROM opensuse/tumbleweed
# labelprefix=org.opensuse.memcached
PREFIXEDLABEL org.opencontainers.image.title="memcached"
PREFIXEDLABEL org.opencontainers.image.description="A high-performance, distributed memory object caching system version %PKG_VERSION%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/memcached:%PKG_VERSION%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
# Fill the image with content and clean the cache(s)
RUN zypper --non-interactive in memcached && zypper clean -a
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
USER memcached
EXPOSE 11211
CMD ["memcached"]
