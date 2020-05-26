Format: 1.0
Source: kopano
Architecture: any all
Version: 10.0.5-0
DEBTRANSFORM-RELEASE: 1
Maintainer: Kopano Development <development@kopano.io>
Homepage: https://kopano.com
Standards-Version: 3.9.4
# You need to update both .dsc and debian.control (*sigh* - Debian)
Build-Depends:
 autoconf (>= 2.59),
 automake (>= 1:1.10) | automake1.10,
 autotools-dev,
 binutils (>= 2.20),
 debhelper (>= 9),
 devscripts,
 dh-python,
 dh-systemd (>= 1.5),
 dts4debian [amd64],
 fakeroot,
 g++ (>= 6),
 gettext,
 gsoap (>= 2.8.49),
 libcurl3-dev | libcurl4-openssl-dev,
 libdb++-dev,
 libgoogle-perftools-dev,
 libhx-dev (>= 1.10),
 libical3-dev | libical-dev,
 libicu-dev,
 libjsoncpp-dev (>= 1.4.0),
 libkrb5-dev,
 libldap2-dev,
 libmariadbclient-dev | libmysqlclient-dev,
 libncurses5-dev,
 libncursesw5-dev,
 libpam0g-dev,
 librrd-dev (>= 1.3),
 libs3-dev (>= 4.1),
 libssl-dev,
 libtool (>= 1.5),
 libtool-bin | libtool,
 libvmime-dev (>= 0.9.2),
 libxapian-dev,
 libxml2-dev,
 lsb-release,
 m4,
 openssl,
 php-dev | php7.3-dev | php7.2-dev | php7.1-dev | php7.0-dev,
 pkg-config (>= 0.18),
 python3-dev,
 python3-setuptools,
 swig,
 systemd,
 tidy-html5-dev,
 uuid-dev,
 zlib1g-dev,
 libkcoidc-dev [amd64]
Files:
