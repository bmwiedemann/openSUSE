Format: 1.0
Source: gromox
Architecture: any
Version: 2.6
DEBTRANSFORM-RELEASE: 1
Maintainer: Gromox <null@gromox.com>
Homepage: https://gromox.com
Standards-Version: 4.5.0
# libbfio is in the require list because libpff-dev is lacking it (bug)
Build-Depends:
 autoconf (>= 2.69),
 automake (>= 1:1.11) | automake1.11,
 autotools-dev,
 binutils (>= 2.20),
 debhelper-compat (>= 12),
 devscripts,
 fakeroot,
 g++ (>= 7),
 gettext,
 libbfio-dev,
 libcurl4-openssl-dev,
 libfmt-dev,
 libgumbo-dev,
 libhx-dev (>= 4.3),
 libjsoncpp-dev (>= 1.4.0),
 libldap2-dev,
 libmariadbclient-dev | libmysqlclient-dev | libmariadb-dev,
 libpam0g-dev,
 libpff-dev,
 libsqlite3-dev,
 libssl-dev,
 libtinyxml2-dev (>= 8),
 libtool (>= 2),
 libtool-bin (>= 2) | libtool (>= 2),
 lsb-release,
 make,
 m4,
 openssl,
 php-dev (>= 7.0),
 pkg-config (>= 0.23),
 sed,
 systemd,
 uuid-dev,
 zlib1g-dev
Files:
