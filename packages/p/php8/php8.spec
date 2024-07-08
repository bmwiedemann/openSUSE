#
# spec file for package php8
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global flavor @BUILD_FLAVOR@%{nil}

%define php_name php8

%if "%{flavor}" == "apache2"
%define pprefix apache2-mod_
%define psuffix %{nil}
%endif

%if "%{flavor}" == "embed" || "%{flavor}" == "fastcgi" || "%{flavor}" == "fpm"
%define pprefix %{nil}
%define psuffix -%{flavor}
%endif

%if "%{flavor}" == "test"
%define pprefix %{nil}
%define psuffix -test
%endif

%if "%{flavor}" == ""
%define pprefix %{nil}
%define psuffix %{nil}
%endif

%global apiver            20230831
%global zendver           20230831
%define extension_dir     %{_libdir}/%{php_name}/extensions
%define php_sysconf       %{_sysconfdir}/%{php_name}

%bcond_without	apparmor
%if 0%{?suse_version} >= 1500
%bcond_without	argon2
%else
%bcond_with	argon2
%endif
%bcond_with	asan
%bcond_with	debug
%bcond_with	firebird
%bcond_without	sodium

Name:           %{pprefix}%{php_name}%{psuffix}
Version:        8.3.9
Release:        0
Summary:        Interpreter for the PHP scripting language version 8
License:        MIT AND PHP-3.01
Group:          Development/Libraries/PHP
URL:            https://secure.php.net
Source0:        https://secure.php.net/distributions/php-%{version}.tar.xz
Source1:        mod_%{php_name}.conf
Source2:        %{php_name}-fpm.conf
Source5:        README.macros
Source6:        macros.php
# temporarily repacked tarball https://github.com/php/php-src/issues/11300
Source8:        https://secure.php.net/distributions/php-%{version}.tar.xz.asc
# Source9:       https://www.php.net/distributions/php-keyring.gpg#/%%{php_name}.keyring
Source9:        %{php_name}.keyring
Source11:       %{php_name}.rpmlintrc
Source12:       php-fpm.tmpfiles.d
Source100:      build-test.sh
## SUSE specific patches
# adjust includedir
Patch0:         php-phpize.patch
# reproducible builds: (D)eterministic archives; --enable-deterministic-archives is not used in binutils
Patch1:         php-ar-flags.patch
# adjust includedir
Patch2:         php-php-config.patch
# SUSE specific ini defaults
Patch3:         php-ini.patch
# use of the system timezone database
# https://git.remirepo.net/cgit/rpms/scl-php83/php.git/plain/php-8.3.0-systzdata-v24.patch
Patch4:         php-systzdata-v24.patch
# adjust upstream systemd unit to SUSE needs
Patch5:         php-systemd-unit.patch
# PATCH-FEATURE-OPENSUSE use ordered input files for reproducible /usr/bin/phar.phar
Patch6:         php-sort-filelist-phar.patch
## Bugfix patches
# should be upstreamed, will do later
Patch22:        php-date-regenerate-lexers.patch
# PATCH-FEATURE-UPSTREAM https://github.com/php/php-src/pull/6564
Patch19:        php-build-reproducible-phar.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  curl
BuildRequires:  db-devel
BuildRequires:  freetds-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gpg2
BuildRequires:  libacl-devel
BuildRequires:  libbz2-devel
BuildRequires:  libtidy-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  postfix
BuildRequires:  postgresql-devel
BuildRequires:  re2c
BuildRequires:  tcpd-devel
BuildRequires:  update-alternatives
BuildRequires:  xz
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150200
BuildRequires:  pkgconfig(enchant) >= 1.4.2
%else
BuildRequires:  pkgconfig(enchant-2)
%endif
BuildRequires:  pkgconfig(gdlib) >= 2.1.0
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc) >= 50.1
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(libcurl) >= 7.29.0
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libffi) >= 3.0.11
BuildRequires:  pkgconfig(libpcre2-8) >= 10.30
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  pkgconfig(libxslt) >= 1.1.0
BuildRequires:  pkgconfig(libzip) >= 0.11
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(openssl) >= 1.0.2
BuildRequires:  pkgconfig(sqlite3) >= 3.7.7
BuildRequires:  pkgconfig(zlib) >= 1.2.0.4
%if %{with apparmor}
BuildRequires:  pkgconfig(libapparmor)
%endif
%if %{with firebird}
# firebird-devel was merged into libfbclient2-devel for firebird 3
BuildRequires:  firebird-devel
BuildRequires:  libfbclient2-devel
%endif
%if %{with sodium}
BuildRequires:  pkgconfig(libsodium) >= 1.0.8
%endif
%if %{with argon2}
BuildRequires:  pkgconfig(libargon2)
%endif
%if "%{flavor}" == "test"
BuildRequires:  mod_php_any = %{version}
BuildRequires:  php-cli = %{version}
BuildRequires:  php-fpm = %{version}
%endif

%if "%{flavor}" == ""
Requires:       php-sapi = %{version}
Requires:       timezone
Recommends:     php-ctype = %{version}
Recommends:     php-dom = %{version}
Recommends:     php-iconv = %{version}
Recommends:     php-openssl = %{version}
Recommends:     php-sqlite = %{version}
Recommends:     php-tokenizer = %{version}
Recommends:     php-xmlreader = %{version}
Recommends:     php-xmlwriter = %{version}
# Recommends instead of Requires smtp_daemon bsc#1115213
Recommends:     smtp_daemon
# Suggest php-* = %%{version} instead of php-* [bsc#1022158c#4]
Suggests:       php-cli = %{version}
Suggests:       php-gd = %{version}
Suggests:       php-gettext = %{version}
Suggests:       php-mbstring = %{version}
Suggests:       php-mysql = %{version}
## Provides
Provides:       php = %{version}
Provides:       php-api = %{apiver}
Provides:       php-zend-abi = %{zendver}
Provides:       php(api) = %{apiver}
Provides:       php(zend-abi) = %{zendver}
# builtin extensions
Provides:       php-date = %{version}
Provides:       php-filter = %{version}
Provides:       php-hash = %{version}
Provides:       php-json = %{version}
Provides:       php-pcre = %{version}
Provides:       php-reflection = %{version}
Provides:       php-session = %{version}
Provides:       php-simplexml = %{version}
Provides:       php-spl = %{version}
Provides:       php-xml = %{version}
Provides:       zend = %{zendver}
# conflicts other php major versions with and should replace it
Conflicts:      php < %{version}
Conflicts:      php72
# mcrypt was removed in php 7.2
Obsoletes:      php7-mcrypt
# json is now integral part of core, cannot be disabled
Obsoletes:      php7-json
# xmlrpc moved to PECL
Obsoletes:      php7-xmlrpc

%description
PHP is a server-side HTML embedded scripting language designed
primarily for web development but also used as a general-purpose
programming language.

This package contains the base files for all subpackages and
must be installed in order to use PHP. Additionally, extension
modules and server modules (e.g. for Apache) may be installed.

%package cli
Summary:        Interpreter for the PHP scripting language version 8
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-cli = %{version}
Provides:       php-sapi = %{version}
Conflicts:      php-cli < %{version}

%description cli
PHP is a server-side HTML embedded scripting language designed
primarily for web development but also used as a general-purpose
programming language.

This package contains the standard implementation of PHP, namely Zend
PHP. Included are the PHP command-line binary and the configuration
file (php.ini).

Additional documentation is available in package php-doc.

%package devel
# this is required by the installed  development headers
Summary:        PHP development files for C/C++ extensions
Group:          Development/Libraries/PHP
Requires:       %{php_name}-pear
Requires:       %{php_name}-pecl
Requires:       glibc-devel
Requires:       php = %{version}
Requires:       pkgconfig(libpcre2-8) >= 10.30
Requires:       pkgconfig(libxml-2.0) >= 2.9.0
Provides:       php-devel = %{version}
Conflicts:      php-devel < %{version}

%description devel
PHP is a server-side HTML embedded scripting language designed
primarily for web development but also used as a general-purpose
programming language.

This package contains the C headers to build PHP extensions.
%endif

%if "%{flavor}" == "test"
Requires:       php-cli = %{version}

%description
Run php upstream testsuite.
%endif

%if "%{flavor}" == "apache2"
Summary:        PHP module for the Apache 2.x webserver
Group:          Development/Libraries/PHP
BuildRequires:  apache-rpm-macros-control
BuildRequires:  apache2-devel
BuildRequires:  php = %{version}
Requires:       %{apache_mmn}
Requires:       apache2-prefork
Requires:       php = %{version}
Requires(post): %{_sbindir}/a2enmod
Requires(preun): %{_sbindir}/a2enmod
Provides:       mod_php_any = %{version}
Provides:       php-sapi = %{version}
Obsoletes:      mod_php_any < %{version}

%description
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that, have a look at the example archive sites and some of the other
resources available in the links section.

Please refer to %{_docdir}/%{php_name}/README.SUSE for
information on how to load the module into the Apache webserver.
%endif

%if "%{flavor}" == "fastcgi"
Summary:        FastCGI PHP Module
Group:          Development/Libraries/PHP
BuildRequires:  php = %{version}
Requires:       php = %{version}
Provides:       php-cgi = %{version}
Provides:       php-fastcgi = %{version}
Provides:       php-sapi = %{version}
Conflicts:      php-fastcgi < %{version}

%description
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.
%endif

%if "%{flavor}" == "fpm"
Summary:        FastCGI Process Manager PHP Module
Group:          Development/Libraries/PHP
BuildRequires:  php = %{version}
BuildRequires:  pkgconfig(libsystemd) >= 209
Requires:       php = %{version}
Requires:       group(www)
Requires:       user(wwwrun)
Provides:       php-fpm = %{version}
Provides:       php-sapi = %{version}
Conflicts:      php-fpm < %{version}
%{?systemd_ordering}

%description
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.

%package apache
Summary:        Apache configuration for PHP-FPM
Group:          Development/Libraries/PHP
BuildRequires:  apache-rpm-macros-control
BuildRequires:  apache2
Requires:       apache2
Requires:       php-fpm = %{version}
Requires(post): %{_sbindir}/a2enmod
Supplements:    (php-fpm and apache2)
Conflicts:      mod_php_any
BuildArch:      noarch

%description apache
Configuration for Apache to pass all requests for PHP scripts to the
PHP-FPM server using reverse proxy.
%endif

%if "%{flavor}" == "embed"
Summary:        Embedded SAPI Library
Group:          Development/Libraries/PHP
BuildRequires:  php = %{version}
Requires:       php = %{version}
Provides:       php-sapi = %{version}

%description
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.
%endif

%if "%{flavor}" == ""
%package bcmath
Summary:        "Binary Calculator" extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-bcmath = %{version}
Obsoletes:      php-bcmath < %{version}

%description bcmath
Binary Calculator which supports numbers of any size and precision,
represented as strings.

%package bz2
Summary:        PHP bzip2 codec support
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-bz2 = %{version}
Obsoletes:      php-bz2 < %{version}

%description bz2
PHP functions to read and write bzip2 (.bz2) compressed files.

%package calendar
Summary:        PHP Extension Module
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-calendar = %{version}
Obsoletes:      php-calendar < %{version}

%description calendar
PHP functions for converting between different calendar formats.

%package ctype
Summary:        Character class extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-ctype = %{version}
Obsoletes:      php-ctype < %{version}

%description ctype
PHP functions for checking whether a character or string falls into a
certain character class according to the current locale.

%package curl
Summary:        PHP libcurl integration
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-curl = %{version}
Obsoletes:      php-curl < %{version}

%description curl
PHP interface to libcurl that allows you to connect to and communicate
with servers of many different types, using protocols of many different
types.

%package dba
Summary:        Database abstraction layer for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-dba = %{version}
Obsoletes:      php-dba < %{version}

%description dba
This is a general abstraction layer for several file-based databases.
As such, functionality is limited to a common subset of features
supported by modern databases such as Sleepycat Software's DB2. (This
is not to be confused with IBM's DB2 software, which is supported
through the ODBC functions.)

%package dom
Summary:        Document Object Model extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-dom = %{version}
Obsoletes:      php-dom < %{version}

%description dom
This module adds Document Object Model (DOM) support.

%package enchant
Summary:        Spell checking extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-enchant = %{version}
Obsoletes:      php-enchant < %{version}
# Obsolete pspell plugin as enchant is favored solution (goodbye aspell)
Obsoletes:      php7-pspell

%description enchant
Enchant is the PHP binding for the Enchant library. Enchant steps in
to provide uniformity and conformity on top of all spelling
libraries, and implements certain features that may be lacking in any
individual provider library. Everything should "just work" for any
and every definition of "just working."

%package exif
Summary:        EXIF metadata extensions for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-mbstring = %{version}
Provides:       php-exif = %{version}
Obsoletes:      php-exif < %{version}

%description exif
PHP functions for extracting EXIF (Exchangable Image File Format;
metadata from images) information stored in headers of JPEG and TIFF
images.

%package ffi
Summary:        Main interface to C code and data
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-ffi = %{version}

%description ffi
This extension allows the loading of shared libraries (.DLL or .so),
calling of C functions and accessing of C data structures in pure PHP,
without having to have deep knowledge of the Zend extension API, and
without having to learn a third "intermediate" language.

%package fileinfo
Summary:        File identification extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-fileinfo = %{version}
Obsoletes:      php-fileinfo < %{version}

%description fileinfo
The functions in this module try to guess the content type and
encoding of a file by looking for certain magic byte sequences at
specific positions within the file. It uses (a bundled version of)
libmagic to heuristically determine this.

%package ftp
Summary:        FTP protocol support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-ftp = %{version}
Obsoletes:      php-ftp < %{version}

%description ftp
PHP functions for access to file servers speaking the File Transfer
Protocol (FTP) as defined in RFC 959.

%package gd
Summary:        GD Graphics Library extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-gd = %{version}
Obsoletes:      php-gd < %{version}

%description gd
PHP functions to create and manipulate image files in a variety of
different image formats, including GIF, PNG, JPEG, WBMP, and XPM. Even
more convenient: PHP can output image streams directly to a browser.

%package gettext
Summary:        Native language support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-gettext = %{version}
Obsoletes:      php-gettext < %{version}

%description gettext
PHP functions that implement a Native Language Support (NLS) API which
can be used to internationalize your PHP applications.

%package gmp
Summary:        Bignum extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-gmp = %{version}
Obsoletes:      php-gmp < %{version}

%description gmp
PHP functions for work with arbitrary-length integers using the GNU MP
library.

%package iconv
Summary:        Character set conversion functions for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-iconv = %{version}
Obsoletes:      php-iconv < %{version}

%description iconv
This module contains an interface to iconv character set conversion
facility. With this module, a string represented by a local character
set can be turned into another character set, which may be the
Unicode character set. Supported character sets depend on the iconv
implementation of your system.

%package intl
Summary:        ICU integration for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-intl = %{version}
Obsoletes:      php-intl < %{version}

%description intl
The internationalization (intl) extension is a wrapper for the ICU
library, enabling PHP programmers to perform UCA (Unicode Collation
Algorithm) conformant collation as well as date, time, number and
currency formatting in their scripts.

%package ldap
Summary:        LDAP protocol support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-ldap = %{version}
Obsoletes:      php-ldap < %{version}

%description ldap
PHP interface to the Lightweight Directory Access Protocol (LDAP).

%package mbstring
Summary:        Multibyte string functions for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-mbstring = %{version}
Obsoletes:      php-mbstring < %{version}

%description mbstring
mbstring provides multibyte specific string functions that help
dealing with multibyte encodings in PHP. mbstring handles character
encoding conversion between the possible encoding pairs. mbstring
handles Unicode-based encodings such as UTF-8 and UCS-2 and many
single-byte encodings for convenience.

%package mysql
Summary:        MySQL database client for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-pdo = %{version}
Provides:       php-mysql = %{version}
Provides:       php-mysqli = %{version}
Provides:       php-pdo_mysql = %{version}
Provides:       php_any_db = %{version}
Obsoletes:      php-mysql < %{version}

%description mysql
PHP functions for access to MySQL database servers.

%if %{with firebird}
%package firebird
Summary:        Firebird database client for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-pdo = %{version}
Provides:       php-firebird = %{version}
Provides:       php_any_db = %{version}
Obsoletes:      php-firebird < %{version}

%description firebird
PHP functions for access to firebird database servers.
%endif

%package odbc
Summary:        ODBC extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-pdo = %{version}
Provides:       php-odbc = %{version}
Provides:       php-pdo_odbc = %{version}
Obsoletes:      php-odbc < %{version}

%description odbc
This module adds Open Database Connectivity (ODBC) support.

%package opcache
Summary:        Opcode cache extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-opcache = %{version}
Obsoletes:      php-opcache < %{version}

%description opcache
OPcache improves PHP performance by storing precompiled script
bytecode in shared memory, thereby removing the need for PHP to load
and parse scripts on each request.

%package openssl
Summary:        OpenSSL integration for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-openssl = %{version}
Obsoletes:      php-openssl < %{version}

%description openssl
This extension binds functions of OpenSSL library for symmetric and
asymmetric encryption and decryption, PBKDF2, PKCS#7, PKCS#12, X.509
and other crypto operations. It also provides an implementation of
TLS streams.

%package pcntl
Summary:        Process Control extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-pcntl = %{version}
Obsoletes:      php-pcntl < %{version}

%description pcntl
Process Control support in PHP implements the Unix style of process
creation, program execution, signal handling and process termination
(fork, waitpid, signal, WIF flags, etc.)

%package phar
Summary:        PHP Archive extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-zlib = %{version}
Provides:       php-phar = %{version}
Conflicts:      php-phar < %{version}

%description phar
The phar extension provides a way to put entire PHP applications into
a single file called a "phar" (PHP Archive) for distribution and
installation.

In addition, the phar extension also provides a file-format
abstraction method for creating and manipulating tar and zip files
through the PharData class, much as PDO provides a unified interface
for accessing different databases. Phar also can convert between tar,
zip and phar file formats.

%package pdo
Summary:        PHP Data Objects extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-pdo = %{version}
Obsoletes:      php-pdo < %{version}

%description pdo
The PHP Data Objects (PDO) extension defines an interface for
accessing databases in PHP. Each database driver that implements the
PDO interface can expose database-specific features as regular
extension functions. Note that you use a database-specific PDO driver
to access a database server.

PDO provides a data-access abstraction layer, which means that,
regardless of the database used, you use the same functions to issue
queries and fetch data. PDO does not provide a database abstraction;
it does not rewrite SQL or emulate missing features.

%package pgsql
Summary:        PostgreSQL database client for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-pdo = %{version}
Provides:       php-pdo_pgsql = %{version}
Provides:       php-pgsql = %{version}
Provides:       php_any_db = %{version}
Obsoletes:      php-pgsql < %{version}

%description pgsql
PHP functions for access to PostgreSQL database servers. It includes
both traditional pgsql and pdo_pgsql drivers.

%package posix
Summary:        POSIX functions for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-posix = %{version}
Obsoletes:      php-posix < %{version}

%description posix
This module contains an interface to those functions defined in the
IEEE 1003.1 (POSIX.1) standards document which are not accessible
through other means.

%package readline
Summary:        PHP readline extension
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-readline = %{version}
Obsoletes:      php-readline < %{version}

%description readline
PHP interface to libedit, which provides editable command line as well
as PHP interactive mode (php -a).

%package shmop
Summary:        Alternate, low-level shared memory implementation for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-shmop = %{version}
Obsoletes:      php-shmop < %{version}

%description shmop
An extension created as an alternative to the sysvmsg module.

%package snmp
Summary:        SNMP extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-snmp = %{version}
Obsoletes:      php-snmp < %{version}

%description snmp
The SNMP extension provides a toolset for managing remote devices via
the Simple Network Management Protocol.

As it is a wrapper around the underlying Net-SNMP library, all basic
concepts are the same and the PHP functions change their behavior
depending on the Net-SNMP configuration files and environment
variables.

%package soap
Summary:        SOAP/WSDL extension module for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-soap = %{version}
Obsoletes:      php-soap < %{version}

%description soap
This module provides SOAP support.

SOAP extension can be used to write SOAP Servers and Clients. It
supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package sockets
Summary:        Berkeley sockets API for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-sockets = %{version}
Obsoletes:      php-sockets < %{version}

%description sockets
The socket extension implements a low-level interface to the socket
communication functions based on the BSD sockets API, providing the
possibility to act as a socket server as well as a client.

%if %{with sodium}
%package sodium
Summary:        Cryptographic Extension Based on Libsodium
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-sodium = %{version}
Obsoletes:      php-sodium < %{version}

%description sodium
PHP binding to libsodium software library for encryption, decryption,
signatures, password hashing and more.
%endif

%package sqlite
Summary:        SQLite database client for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-pdo = %{version}
Provides:       php-pdo_sqlite = %{version}
Provides:       php-sqlite = %{version}
Obsoletes:      php-sqlite < %{version}

%description sqlite
This is an extension for the SQLite Embeddable SQL Database Engine.
https://www.sqlite.org

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

This package includes sqlite and pdo_sqlite modules for sqlite version
2 and 3 respectively.

%package sysvmsg
Summary:        SysV Message Queue support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-sysvmsg = %{version}
Obsoletes:      php-sysvmsg < %{version}

%description sysvmsg
This module provides System V Message Queue support.

%package sysvsem
Summary:        SysV Semaphore support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-sysvsem = %{version}
Obsoletes:      php-sysvsem < %{version}

%description sysvsem
PHP interface for System V semaphores.

%package sysvshm
Summary:        SysV Shared Memory support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-sysvshm = %{version}
Obsoletes:      php-sysvshm < %{version}

%description sysvshm
PHP interface for System V shared memory.

%package tidy
Summary:        PHP binding for the Tidy HTML cleaner
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-tidy = %{version}
Obsoletes:      php-tidy < %{version}

%description tidy
Tidy is an extension based on Libtidy (http://tidy.sourceforge.net) and allows
a PHP developer to clean, repair, and traverse HTML, XHTML, and XML
documents -- including ones with embedded scripting languages such as
PHP or ASP within them using OO constructs.

%package tokenizer
Summary:        Extension module to access Zend Engine's PHP tokenizer
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-tokenizer = %{version}
Obsoletes:      php-tokenizer < %{version}

%description tokenizer
The tokenizer functions provide an interface to the PHP tokenizer
embedded in the Zend Engine. Using these functions you may write your
own PHP source analyzing or modification tools without having to deal
with the language specification at the lexical level.

%package xsl
Summary:        PHP Extension Module
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-dom = %{version}
Provides:       php-xsl = %{version}
Obsoletes:      php-xsl < %{version}

%description xsl
PHP's XSL extension implements the XSL (Extensible Stylesheet
Language) standard, performing XSLT transformations using the libxslt
library

%package xmlreader
Summary:        Streaming XML reader extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Requires:       php-dom = %{version}
Provides:       php-xmlreader = %{version}
Obsoletes:      php-xmlreader < %{version}

%description xmlreader
The XMLReader extension is an XML Pull parser. The reader acts as a
cursor going forward on the document stream and stopping at each node
on the way.

%package xmlwriter
Summary:        Streaming-based XML writer extension for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-xmlwriter = %{version}
Obsoletes:      php-xmlwriter < %{version}

%description xmlwriter
XMLWriter wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or
files containing XML data.

%package zip
Summary:        ZIP archive support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-zip = %{version}
Obsoletes:      php-zip < %{version}

%description zip
This extension allows to transparently read or write ZIP compressed
archives and the files inside them.

%package zlib
Summary:        Zlib compression support for PHP
Group:          Development/Libraries/PHP
Requires:       php = %{version}
Provides:       php-zlib = %{version}
Obsoletes:      php-zlib < %{version}

%description zlib
This module enables to transparently read and write gzip (.gz)
compressed files, through versions of most of the filesystem
functions which work with gzip-compressed files (and uncompressed
files, too, but not with sockets).
%endif

%prep
%setup -q -n php-%{version}
cp %{SOURCE5} .

%autopatch -p1 -v

# use system pcre2
rm -r ext/pcre/pcre2lib

# get parsers regenerated
for parser in $(find -type f -name "*.re");do
    rm -v ${parser%.*}.c
done

# Safety check for API version change.
vapi=$(sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h)
if test "x${vapi}" != "x%{apiver}"; then
    : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
    : Update the apiver macro and rebuild.
    exit 1
fi
vzend=$(sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h)
if test "x${vzend}" != "x%{zendver}"; then
    : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
    : Update the zendver macro and rebuild.
    exit 1
fi

%build
%if 150000 <= 0%{?sle_version} && 0%{?sle_version} <= 150200
# former libcrypt does not support extended DES, so the build would fail
# with --with-external-libcrypt
sed -i 's:|| test "$ac_cv_crypt_ext_des" = "no"::' ext/standard/config.m4
%endif

# regenerate configure etc.
./buildconf --force

# export flags
CFLAGS="%{optflags} -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
CXXFLAGS="%{optflags} -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
%if %{with firebird}
CFLAGS="$CFLAGS -I/usr/include/firebird"
CXXFLAGS="$CXXFLAGS -I/usr/include/firebird"
%endif
%if %{with debug}
CFLAGS="$CFLAGS -Og"
CXXFLAGS="$CXXFLAGS -Og"
%endif
export CFLAGS
export CXXFLAGS
export LDFLAGS="-pie"
export NO_INTERACTION=true
# Totally fake, it wasnt and will never be reliable anyway.
export PHP_UNAME="Linux suse 2.6.36 #1 SMP 2011-02-21 10:34:10 +0100 x86_64 x86_64 x86_64 GNU/Linux"
# where to install extensions
export EXTENSION_DIR=%{extension_dir}
# Fix build-cli for arm and aarch64
export LIBS=-ltinfo
# Some extensions are broken when linking with -z now
export SUSE_ZNOW=0

# build function
Build()
{
    sapi=$1
    shift
    %configure \
        --datadir=%{_datadir}/%{php_name} \
        --with-libdir=%{_lib} \
        --includedir=%{_includedir} \
        --sysconfdir=%{php_sysconf}/$sapi \
        --with-config-file-path=%{php_sysconf}/$sapi \
        --with-config-file-scan-dir=%{php_sysconf}/conf.d \
        --with-libxml \
        --enable-session \
        --with-external-pcre \
        --enable-xml \
        --enable-simplexml \
        --enable-filter \
        --disable-debug \
        --enable-inline-optimization \
        --disable-rpath \
        --disable-static \
        --enable-shared \
        --with-pic \
        --with-gnu-ld \
        --enable-re2c-cgoto \
        --with-system-tzdata=%{_datadir}/zoneinfo \
        --with-external-libcrypt \
        --with-mhash \
        --disable-phpdbg \
%if %{with argon2}
        --with-password-argon2=%{_usr} \
%endif
        "$@" || { cat config.log; exit 1; }
    # Some modules are builtin, reasons:
    #  - libxml can not be shared (and is needed by PEAR)
    #  - spl doesn't build shared
    #  - simplexml is needed by spl
    #  - session need to be builtin, otherwise sqlite and other session engines fail
    #  - pcre is needed for PEAR
    #  - filter is builtin due security reasons
    # We have still have harcoded RPATH in some modules
    sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
           -e 's|^runpath_var=LD_RUN_PATH|runpath_var=LIBTOOL_IS_BROKED|g' \
           libtool
    # build mod_phpN.so instead of libphp.so
    # rename does not suffice, see bsc#1089487
    if [ $sapi == apache2 ]; then
        sed -i 's/libphp/mod_%{php_name}/g' Makefile
    fi
%if %{with asan}
    sed -i -e 's/\(^CFLAGS.*\)/\1 -fsanitize=address/' \
           -e 's/\(^EXTRA_LIBS =.*\)/\1 -lasan/' \
           Makefile
%endif
    %make_build
}

%if "%{flavor}" == "apache2"
Build apache2 \
    --with-apxs2=%{apache_apxs} \
    --disable-all \
    --disable-cgi \
    --disable-cli
%endif

%if "%{flavor}" == "fastcgi"
Build fastcgi \
    --bindir=%{_bindir} \
    --disable-all \
    --enable-cgi \
    --disable-cli
%endif

%if "%{flavor}" == "fpm"
Build fpm \
    --enable-fpm \
    --with-fpm-acl \
%if %{with apparmor}
    --with-fpm-apparmor \
%endif
    --with-fpm-systemd \
    --with-fpm-user=%{apache_user} \
    --with-fpm-group=%{apache_group} \
    --bindir=%{_bindir} \
    --disable-all \
    --disable-cgi \
    --disable-cli \
    --localstatedir=%{_localstatedir}
%endif

%if "%{flavor}" == "embed"
Build embed \
    --enable-embed=shared \
    --disable-all \
    --disable-cgi \
    --disable-cli
%endif

%if "%{flavor}" == ""
Build cli \
    --enable-cli \
    --enable-bcmath=shared \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --enable-dom=shared \
    --enable-exif=shared \
    --enable-ftp=shared \
    --enable-mbstring=shared \
    --enable-mbregex \
    --enable-mysqlnd=shared \
    --enable-pcntl=shared \
    --enable-posix=shared \
    --enable-shmop=shared \
    --enable-soap=shared \
    --enable-sockets=shared \
    --enable-sysvmsg=shared \
    --enable-sysvsem=shared \
    --enable-sysvshm=shared \
    --enable-tokenizer=shared \
    --enable-fileinfo=shared \
    --with-zlib=shared \
    --with-bz2=shared \
    --with-curl=shared \
    --enable-gd=shared \
    --with-external-gd \
    --with-avif \
    --with-ffi=shared \
    --with-gettext=shared \
    --with-gmp=shared \
    --with-iconv=shared \
    --with-kerberos \
    --with-ldap=shared \
    --with-ldap-sasl \
    --with-libedit=shared \
    --with-mysql-sock=%{_rundir}/mysql/mysql.sock \
    --with-mysqli=shared,mysqlnd \
    --with-unixODBC=shared,%{_usr} \
    --with-openssl=shared \
    --with-system-ciphers \
    --with-pgsql=shared,%{_usr} \
    --enable-phar=shared \
    --with-enchant=shared \
    --with-snmp=shared \
    --enable-xmlreader=shared \
    --enable-xmlwriter=shared \
    --with-xsl=shared \
    --with-tidy=shared,%{_usr} \
    --enable-dba=shared \
    --with-db4=%{_usr} \
    --with-lmdb=%{_usr} \
    --without-gdbm \
    --with-cdb \
    --enable-pdo=shared \
    --with-pdo-sqlite=shared \
    --with-sqlite3=shared \
    --with-pdo-mysql=shared,mysqlnd \
%if %{with firebird}
    --with-pdo-firebird=shared \
%endif
    --with-pdo-pgsql=shared,%{_usr} \
    --with-pdo-odbc=shared,unixODBC,%{_usr} \
%if %{with sodium}
    --with-sodium=shared \
%endif
    --enable-opcache=shared \
    --with-zip=shared \
    --enable-intl=shared \
    --disable-cgi
%endif

%check
%if %{with asan}
# no need for ASAN build
exit 0
%endif

%if "%{flavor}" == "test"
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 LANG=POSIX LC_ALL=POSIX
unset TZ
# We save results for further investigation for QA
TEST_PHP_EXECUTABLE=/usr/bin/php php run-tests.php | tee testresults.txt || true
set +x
for f in $(find .. -name "*.diff" -type f -print); do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
done
set -x
unset NO_INTERACTION REPORT_EXIT_STATUS
exit 0
%endif

%if "%{flavor}" == ""
# check if we link against system libcrypt
if [ -z "$(ldd sapi/cli/php | grep libcrypt.so)" ]; then
    echo 'php does not link against system libcrypt.'
    exit 1
fi

# check if we link against system libgd
if [ -z "$(ldd modules/gd.so | grep libgd.so)" ]; then
    echo 'php-gd does not link against system libgd.'
    exit 1
fi
%endif

%install
# do the actual installation

%if "%{flavor}" == "apache2"
install -m 755 -D .libs/mod_php8.so %{buildroot}%{apache_libexecdir}/mod_php8.so
# php sapi configuration
install -dm 755 %{buildroot}%{php_sysconf}/apache2
sed "s=@extdir@=%{extension_dir}=" php.ini-production > %{buildroot}%{php_sysconf}/apache2/php.ini
# apache configuration
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d
install -m 644 %{SOURCE1} %{buildroot}%{apache_sysconfdir}/conf.d/mod_%{php_name}.conf
%endif

%if "%{flavor}" == "embed"
install -m 755 -D .libs/libphp.so %{buildroot}%{_libdir}/lib%{php_name}.so
%endif

%if "%{flavor}" == "fastcgi"
make install-binaries INSTALL_ROOT=%{buildroot}
install -dm 755 %{buildroot}%{php_sysconf}/fastcgi
sed "s=@extdir@=%{extension_dir}=" php.ini-production > %{buildroot}%{php_sysconf}/fastcgi/php.ini
# provide compat symlink
mkdir -p %{buildroot}%{apache_serverroot}/cgi-bin
ln -s %{_bindir}/php-cgi %{buildroot}%{apache_serverroot}/cgi-bin/php
%endif

%if "%{flavor}" == "fpm"
make install-binaries INSTALL_ROOT=%{buildroot}
install -dm 755 %{buildroot}%{php_sysconf}/fpm
sed "s=@extdir@=%{extension_dir}=" php.ini-production > %{buildroot}%{php_sysconf}/fpm/php.ini
#install fpm init script.
install -D -m 0644 sapi/fpm/php-fpm.service %{buildroot}%{_unitdir}/php-fpm.service
ln -s service %{buildroot}%{_sbindir}/rcphp-fpm
# bug 1173786
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE12} %{buildroot}%{_tmpfilesdir}/php-fpm.conf
# bug 1192414
mv %{buildroot}%{php_sysconf}/fpm/php-fpm.conf{.default,}
mv %{buildroot}%{php_sysconf}/fpm/php-fpm.d/www.conf{.default,}
# apache configuration
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d
install -m 644 %{SOURCE2} %{buildroot}%{apache_sysconfdir}/conf.d/%{php_name}-fpm.conf
%endif

%if "%{flavor}" == ""
make install INSTALL_ROOT=%{buildroot}
# generate php.ini from php.ini-production:
install -dm 755 %{buildroot}%{_datadir}/php
install -dm 755 %{buildroot}%{_datadir}/%{php_name}
install -dm 755 %{buildroot}%{php_sysconf}/conf.d
install -dm 755 %{buildroot}%{php_sysconf}/cli
sed "s=@extdir@=%{extension_dir}=" php.ini-production | sed -r 's/^(html_errors|implicit_flush|max_execution_time|register_argc_argv)/;\1/' > %{buildroot}%{php_sysconf}/cli/php.ini

# prepare configuration files for each extension
for f in %{buildroot}%{extension_dir}/*; do
    if test ${f##*.} = a; then
        rm $f
        continue
    fi
    if test ${f##*.} = so; then
        f=${f%.so}
    fi
    ext=${f##*/}
    zend_=''
    case $ext in
      # priority 0 (will be loaded first)
      opcache)
        ini_name=00-${ext}
        zend_='zend_';;
      # priority 2 (will be loaded after < 2)
      pdo_*|mysqli|xmlreader)
        ini_name=20-${ext};;
      # priority 1 (will be loaded after < 1)
      *)
        ini_name=10-${ext};;
    esac
    echo "; comment out next line to disable $ext extension in php" > %{buildroot}%{php_sysconf}/conf.d/${ini_name}.ini
    echo "${zend_}extension=$ext.so" >> %{buildroot}%{php_sysconf}/conf.d/${ini_name}.ini
done
# directory for sessions
install -d %{buildroot}%{_localstatedir}/lib/%{php_name}/sessions
# fix symlink (bnc#734176)
ln -s %{_bindir}/php %{buildroot}%{_bindir}/%{php_name}
# install the macros file:
install -d %{buildroot}%{_rpmconfigdir}/macros.d
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/" %{SOURCE6} > macros.php
install -m 644 -c macros.php %{buildroot}%{_rpmconfigdir}/macros.d/macros.php
# install missing SAPI headers for embed
install -d %{buildroot}%{_includedir}/%{php_name}/sapi/embed
install -m 644 sapi/embed/php_embed.h %{buildroot}%{_includedir}/%{php_name}/sapi/embed/php_embed.h
# fix file contains a shebang
for f in %{buildroot}%{_datadir}/%{php_name}/build/{gen_stub.php,run-tests.php}; do
    sed -i '1{s|env ||}' $f
done
%endif

%if "%{flavor}" == "apache2"
%post
if [ $1 -eq 1 ]; then
    # package is just installed
    a2enmod %{php_name} > /dev/null
fi

%preun
if [ $1 -eq 0 ]; then
    # package will be uninstalled
    a2enmod -d %{php_name} > /dev/null
fi

%postun
# request restart apache instances (which loaded php module) after apache2-mod_phpN package update
if [ $1 -eq 1 ]; then
  %apache_request_restart -m %{php_name}
fi

%posttrans
# restart apache instances which have this module after zypper or rpm transaction, if not
# have restarted already in other posttrans
%apache_restart_if_needed
%endif

%if "%{flavor}" == "fpm"
%pre
%service_add_pre php-fpm.service

%post
%service_add_post php-fpm.service
%tmpfiles_create %{_tmpfilesdir}/php-fpm.conf

%preun
%service_del_preun php-fpm.service

%postun
%service_del_postun php-fpm.service

%post apache
if [ $1 -eq 1 ]; then
    # package is just installed, check/enable required Apache modules
    for m in proxy proxy_fcgi; do
        a2enmod -q ${m} && continue
        a2enmod ${m}
        %apache_request_restart -m ${m}
    done
fi

%posttrans apache
%apache_restart_if_needed
%endif

%if "%{flavor}" == "embed"
%if 0%{?suse_version} > 1500
%ldconfig_scriptlets
%else
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif
%endif

%if "%{flavor}" == ""
%files
%defattr(-, root, root)
%doc README.md CODING_STANDARDS.md EXTENSIONS NEWS UPGRADING CONTRIBUTING.md README.REDIST.BINS UPGRADING.INTERNALS
%license LICENSE
%dir %{_datadir}/php
%dir %{_datadir}/%{php_name}
%dir %{_libdir}/%{php_name}
%dir %{extension_dir}
%dir %{php_sysconf}
%dir %{php_sysconf}/conf.d
%attr(0755, %{apache_user}, root) %dir %{_localstatedir}/lib/%{php_name}
%attr(0755, %{apache_user}, root) %dir %{_localstatedir}/lib/%{php_name}/sessions

%files cli
%defattr(-, root, root)
%config(noreplace) %{php_sysconf}/cli/php.ini
%dir %{php_sysconf}/cli
%{_bindir}/php
%{_bindir}/%{php_name}
%{_mandir}/man1/php.1%{?ext_man}

%files devel
%defattr(-, root, root)
%doc README.macros
%{_bindir}/phpize
%{_bindir}/php-config
%{_datadir}/%{php_name}/build
%attr(0755, root, root) %{_datadir}/%{php_name}/build/{gen_stub.php,run-tests.php}
%{_includedir}/%{php_name}
%{_mandir}/man1/phpize.1%{?ext_man}
%{_mandir}/man1/php-config.1%{?ext_man}
%{_rpmconfigdir}/macros.d/macros.php
%endif

%if "%{flavor}" == "embed"
%files
%defattr(-, root, root)
%{_libdir}/lib%{php_name}.so
%endif

%if "%{flavor}" == "fastcgi"
%files
%defattr(-, root, root)
%config(noreplace) %{php_sysconf}/fastcgi/php.ini
%dir %{php_sysconf}/fastcgi
%{_bindir}/php-cgi
%{_mandir}/man1/php-cgi.1%{?ext_man}
%{apache_serverroot}/cgi-bin/php
%endif

%if "%{flavor}" == "fpm"
%files
%defattr(-, root, root)
%dir %{php_sysconf}/fpm
%dir %{php_sysconf}/fpm/php-fpm.d
%config(noreplace) %{php_sysconf}/fpm/php.ini
%config(noreplace) %{php_sysconf}/fpm/php-fpm.conf
%config(noreplace) %{php_sysconf}/fpm/php-fpm.d/www.conf
%dir %{_datadir}/%{php_name}/fpm
%{_datadir}/%{php_name}/fpm/status.html
%{_sbindir}/php-fpm
%{_sbindir}/rcphp-fpm
%{_mandir}/man8/php-fpm.8%{?ext_man}
%{_unitdir}/php-fpm.service
%{_tmpfilesdir}/php-fpm.conf
%ghost %dir %attr(711,root,root) /run/php-fpm

%files apache
%config(noreplace) %{apache_sysconfdir}/conf.d/%{php_name}-fpm.conf
%endif

%if "%{flavor}" == "apache2"
%files
%defattr(-, root, root)
%config(noreplace) %{php_sysconf}/apache2/php.ini
%config(noreplace) %{apache_sysconfdir}/conf.d/mod_%{php_name}.conf
%dir %{php_sysconf}/apache2
%{apache_libexecdir}/mod_%{php_name}.so
%endif

%if "%{flavor}" == ""
%files bcmath
%defattr(-, root, root)
%{extension_dir}/bcmath.so
%config(noreplace) %{php_sysconf}/conf.d/*bcmath.ini

%files bz2
%defattr(-, root, root)
%{extension_dir}/bz2.so
%config(noreplace) %{php_sysconf}/conf.d/*bz2.ini

%files calendar
%defattr(-, root, root)
%{extension_dir}/calendar.so
%config(noreplace) %{php_sysconf}/conf.d/*calendar.ini

%files ctype
%defattr(-, root, root)
%{extension_dir}/ctype.so
%config(noreplace) %{php_sysconf}/conf.d/*ctype.ini

%files curl
%defattr(-, root, root)
%{extension_dir}/curl.so
%config(noreplace) %{php_sysconf}/conf.d/*curl.ini

%files dba
%defattr(-, root, root)
%{extension_dir}/dba.so
%config(noreplace) %{php_sysconf}/conf.d/*dba.ini

%files dom
%defattr(-, root, root)
%{extension_dir}/dom.so
%config(noreplace) %{php_sysconf}/conf.d/*dom.ini

%files enchant
%defattr(-, root, root)
%{extension_dir}/enchant.so
%config(noreplace) %{php_sysconf}/conf.d/*enchant.ini

%files exif
%defattr(-, root, root)
%{extension_dir}/exif.so
%config(noreplace) %{php_sysconf}/conf.d/*exif.ini

%files ffi
%defattr(-, root, root)
%{extension_dir}/ffi.so
%config(noreplace) %{php_sysconf}/conf.d/*ffi.ini

%files fileinfo
%defattr(-, root, root)
%{extension_dir}/fileinfo.so
%config(noreplace) %{php_sysconf}/conf.d/*fileinfo.ini

%files ftp
%defattr(-, root, root)
%{extension_dir}/ftp.so
%config(noreplace) %{php_sysconf}/conf.d/*ftp.ini

%files gd
%defattr(-, root, root)
%{extension_dir}/gd.so
%config(noreplace) %{php_sysconf}/conf.d/*gd.ini

%files gettext
%defattr(-, root, root)
%{extension_dir}/gettext.so
%config(noreplace) %{php_sysconf}/conf.d/*gettext.ini

%files gmp
%defattr(-, root, root)
%{extension_dir}/gmp.so
%config(noreplace) %{php_sysconf}/conf.d/*gmp.ini

%files iconv
%defattr(-, root, root)
%{extension_dir}/iconv.so
%config(noreplace) %{php_sysconf}/conf.d/*iconv.ini

%files intl
%defattr(-, root, root)
%{extension_dir}/intl.so
%config(noreplace) %{php_sysconf}/conf.d/*intl.ini

%files ldap
%defattr(-, root, root)
%{extension_dir}/ldap.so
%config(noreplace) %{php_sysconf}/conf.d/*ldap.ini

%files mbstring
%defattr(-, root, root)
%{extension_dir}/mbstring.so
%config(noreplace) %{php_sysconf}/conf.d/*mbstring.ini

%files mysql
%defattr(-, root, root)
%{extension_dir}/mysqli.so
%config(noreplace) %{php_sysconf}/conf.d/*mysqli.ini
%{extension_dir}/mysqlnd.so
%config(noreplace) %{php_sysconf}/conf.d/*mysqlnd.ini
%{extension_dir}/pdo_mysql.so
%config(noreplace) %{php_sysconf}/conf.d/*pdo_mysql.ini

%if %{with firebird}
%files firebird
%defattr(-, root, root)
%{extension_dir}/pdo_firebird.so
%config(noreplace) %{php_sysconf}/conf.d/*pdo_firebird.ini
%endif

%files odbc
%defattr(-, root, root)
%{extension_dir}/odbc.so
%config(noreplace) %{php_sysconf}/conf.d/*odbc.ini
%{extension_dir}/pdo_odbc.so
%config(noreplace) %{php_sysconf}/conf.d/*pdo_odbc.ini

%files opcache
%defattr(-, root, root)
%{extension_dir}/opcache.so
%config(noreplace) %{php_sysconf}/conf.d/*opcache.ini

%files openssl
%defattr(-, root, root)
%{extension_dir}/openssl.so
%config(noreplace) %{php_sysconf}/conf.d/*openssl.ini

%files phar
%defattr(-, root, root)
%{_mandir}/man1/phar.1%{?ext_man}
%{_mandir}/man1/phar.phar.1%{?ext_man}
%{extension_dir}/phar.so
%config(noreplace) %{php_sysconf}/conf.d/*phar.ini
%{_bindir}/phar
%{_bindir}/phar.phar

%files pcntl
%defattr(-, root, root)
%{extension_dir}/pcntl.so
%config(noreplace) %{php_sysconf}/conf.d/*pcntl.ini

%files pdo
%defattr(-, root, root)
%{extension_dir}/pdo.so
%config(noreplace) %{php_sysconf}/conf.d/*pdo.ini

%files pgsql
%defattr(-, root, root)
%{extension_dir}/pgsql.so
%config(noreplace) %{php_sysconf}/conf.d/*pgsql.ini
%{extension_dir}/pdo_pgsql.so
%config(noreplace) %{php_sysconf}/conf.d/*pdo_pgsql.ini

%files posix
%defattr(-, root, root)
%{extension_dir}/posix.so
%config(noreplace) %{php_sysconf}/conf.d/*posix.ini

%files readline
%defattr(-, root, root)
%{extension_dir}/readline.so
%config(noreplace) %{php_sysconf}/conf.d/*readline.ini

%files shmop
%defattr(-, root, root)
%{extension_dir}/shmop.so
%config(noreplace) %{php_sysconf}/conf.d/*shmop.ini

%files snmp
%defattr(-, root, root)
%{extension_dir}/snmp.so
%config(noreplace) %{php_sysconf}/conf.d/*snmp.ini

%files soap
%defattr(-, root, root)
%{extension_dir}/soap.so
%config(noreplace) %{php_sysconf}/conf.d/*soap.ini

%if %{with sodium}
%files sodium
%defattr(-, root, root)
%{extension_dir}/sodium.so
%config(noreplace) %{php_sysconf}/conf.d/*sodium.ini
%endif

%files sockets
%defattr(-, root, root)
%{extension_dir}/sockets.so
%config(noreplace) %{php_sysconf}/conf.d/*sockets.ini

%files sqlite
%defattr(-, root, root)
%{extension_dir}/pdo_sqlite.so
%config(noreplace) %{php_sysconf}/conf.d/*pdo_sqlite.ini
%{extension_dir}/sqlite3.so
%config(noreplace) %{php_sysconf}/conf.d/*sqlite3.ini

%files sysvmsg
%defattr(-, root, root)
%{extension_dir}/sysvmsg.so
%config(noreplace) %{php_sysconf}/conf.d/*sysvmsg.ini

%files sysvsem
%defattr(-, root, root)
%{extension_dir}/sysvsem.so
%config(noreplace) %{php_sysconf}/conf.d/*sysvsem.ini

%files sysvshm
%defattr(-, root, root)
%{extension_dir}/sysvshm.so
%config(noreplace) %{php_sysconf}/conf.d/*sysvshm.ini

%files tidy
%defattr(-, root, root)
%{extension_dir}/tidy.so
%config(noreplace) %{php_sysconf}/conf.d/*tidy.ini

%files tokenizer
%defattr(-, root, root)
%{extension_dir}/tokenizer.so
%config(noreplace) %{php_sysconf}/conf.d/*tokenizer.ini

%files xmlreader
%defattr(-, root, root)
%{extension_dir}/xmlreader.so
%config(noreplace) %{php_sysconf}/conf.d/*xmlreader.ini

%files xmlwriter
%defattr(-, root, root)
%{extension_dir}/xmlwriter.so
%config(noreplace) %{php_sysconf}/conf.d/*xmlwriter.ini

%files xsl
%defattr(-, root, root)
%{extension_dir}/xsl.so
%config(noreplace) %{php_sysconf}/conf.d/*xsl.ini

%files zip
%defattr(-, root, root)
%{extension_dir}/zip.so
%config(noreplace) %{php_sysconf}/conf.d/*zip.ini

%files zlib
%defattr(-, root, root)
%{extension_dir}/zlib.so
%config(noreplace) %{php_sysconf}/conf.d/*zlib.ini
%endif

%if "%{flavor}" == "test"
%files
%defattr(-, root, root)
%doc testresults.txt
%endif

%changelog
