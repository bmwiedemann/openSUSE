-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Format: 3.0 (quilt)
Source: lighttpd
Binary: lighttpd, lighttpd-doc, lighttpd-mod-mysql-vhost, lighttpd-mod-vhostdb-dbi, lighttpd-mod-vhostdb-ldap, lighttpd-mod-vhostdb-mysql, lighttpd-mod-vhostdb-pgsql, lighttpd-mod-trigger-b4-dl, lighttpd-mod-cml, lighttpd-mod-magnet, lighttpd-mod-webdav, lighttpd-mod-authn-gssapi, lighttpd-mod-authn-ldap, lighttpd-mod-authn-mysql, lighttpd-mod-authn-sasl, lighttpd-mod-geoip
Architecture: any all
Version: 1.4.49-1.1
Maintainer: Lighttpd upstream <contact@lighttpd.net>
Homepage: https://www.lighttpd.net/
Standards-Version: 4.1.3
Vcs-Browser: https://salsa.debian.org/debian/lighttpd
Vcs-Git: https://salsa.debian.org/debian/lighttpd.git
Build-Depends: dpkg-dev (>= 1.16.1~), debhelper (>= 9.20130624~), debhelper (>= 9.20160709) | dh-systemd (>= 1.3), dh-autoreconf, mime-support, libssl-dev, zlib1g-dev, libbz2-dev, libattr1-dev, libpcre3-dev, libdbi-dev, libpq-dev, default-libmysqlclient-dev | libmysqlclient-dev, libfam-dev, libldap2-dev, libfcgi-dev, libgdbm-dev, libgeoip-dev, liblua5.1-0-dev, libmemcached-dev, pkg-config, uuid-dev, libsqlite3-dev, libxml2-dev, libkrb5-dev, libsasl2-dev, perl, libcgi-pm-perl
Package-List:
 lighttpd deb httpd optional arch=any
 lighttpd-doc deb doc optional arch=all
 lighttpd-mod-authn-gssapi deb httpd optional arch=any
 lighttpd-mod-authn-ldap deb httpd optional arch=any
 lighttpd-mod-authn-mysql deb httpd optional arch=any
 lighttpd-mod-authn-sasl deb httpd optional arch=any
 lighttpd-mod-cml deb httpd optional arch=any
 lighttpd-mod-geoip deb httpd optional arch=any
 lighttpd-mod-magnet deb httpd optional arch=any
 lighttpd-mod-mysql-vhost deb httpd optional arch=any
 lighttpd-mod-trigger-b4-dl deb httpd optional arch=any
 lighttpd-mod-vhostdb-dbi deb httpd optional arch=any
 lighttpd-mod-vhostdb-ldap deb httpd optional arch=any
 lighttpd-mod-vhostdb-mysql deb httpd optional arch=any
 lighttpd-mod-vhostdb-pgsql deb httpd optional arch=any
 lighttpd-mod-webdav deb httpd optional arch=any
Checksums-Sha1:
 242ea14ca1b4c80c72ab4b7964875ac99f53fd81 725188 lighttpd_1.4.49.orig.tar.xz
 c16230150405bf6c52960230339ec3ebec2f8296  47400 lighttpd_1.4.49-1.1.debian.tar.xz
Checksums-Sha256:
 9e26f417feff34f4d2901328bc273633b6d3a0d42f5d3dcd89d3b7e939384844 725188 lighttpd_1.4.49.orig.tar.xz
 a6e69c6d7900fe41e3302efc96ac733c30a1a55eabd82bb4ef5b7d0c90172515  47400 lighttpd_1.4.49-1.1.debian.tar.xz
Files:
 fa1ea87b602d067dac2225c49bdf595f 725188 lighttpd_1.4.49.orig.tar.xz
 9f9738803913c1c0254423fe014de048  47400 lighttpd_1.4.49-1.1.debian.tar.xz

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEx8oenincd/VICJSy4OfQFx6VutcFAlq/ZKgACgkQ4OfQFx6V
utcSLg//SkIHrDPNRR2E3D1+3L1Yn0IlLPalbSl44gZ5MyruET694gcKR6cEtfWH
x/oiYvbjpXeHgmbO6xm8Gi6hFSuSLoZ270OoyxaNfeXrZgn6Nttxvfz9IytSRiee
WaJGXbL9Xu4eRRfUR4StNLwxnVUFDut4HqIwlZQCpHuVtevUY0pxVwoKuYnlTKvF
AlOrPmEKP+pHG23vMLLGdt4APpMKIFeWaxNo2vcw5+BmOHKkcffvnISmkgiTOX8A
0ENml6LnjhSg188tRmcYGchDrt+jRsVMVbv7zG0HN9devsdxrg2RxmVxkGfvmOjF
+hq0+7Op0txBdIkNOooJMsMh0+1/zZD7TzYR+dfHm9mVZCs7p3uvA5dKfM471kIi
gsXAdZrnbYqQWOCo81S02R9pJrhhl4zIPDc0JlMZsOy3esSSkk9TFi7ocXMqDbOX
NLbaC7skn/wBpPH+VNnZLF9BbIjQrDPFDlAQtqVZvP5kZbymaHvMzVwA0MGfyYSO
P8Aon58fUwnidd7C4atyDuLxm9V0Ba5Rp2MfJZV2h5gUO7Wde6NF/4fl56902YYy
8/THKDtdYABgDX+C4wIziXQfhHGYj1Y611FE2BV2ZK8cSMb9EYa+9zHMRnP42olN
VQJoLZOaa9DmS0mONbPIEIUD4paps1FIOOrLC3+PSZ/gxBTaCW0=
=v8aM
-----END PGP SIGNATURE-----
