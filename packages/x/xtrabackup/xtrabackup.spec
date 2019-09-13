#
# spec file for package xtrabackup
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xtrabackup
Version:        2.4.12
Release:        0
Summary:        Online backup for MySQL / InnoDB
License:        GPL-2.0-only
Group:          Productivity/Archiving/Backup
URL:            http://www.percona.com/software/percona-xtrabackup/
# stripped source tarball generated from URL below using xtrabackup-nodoc.sh
# https://www.percona.com/downloads/XtraBackup/Percona-XtraBackup-%%{version}/source/tarball/percona-xtrabackup-%%{version}.tar.gz
Source:         percona-xtrabackup-%{version}-nodoc.tar.xz
Source2:        https://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.bz2
Source4:        xtrabackup-nodoc.sh
Patch3:         percona-xtrabackup-2.2.9-nodoc.patch
Patch4:         percona-xtrabackup-2.3.3-disable-version-check.patch
Patch5:         percona-xtrabackup-2.3.2-unbundle-jsnm.patch
Patch6:         gcc9-warning.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cmake >= 2.6.3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jsmn-devel
BuildRequires:  libaio-devel
BuildRequires:  libcurl-devel
BuildRequires:  libev-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  procps
BuildRequires:  pwdutils
BuildRequires:  readline-devel
BuildRequires:  tcpd-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
#
Requires:       rsync
Recommends:     qpress
# This is to ease migration from Percona's generic packages
Provides:       percona-xtrabackup = %{version}
Obsoletes:      percona-xtrabackup < %{version}

%description
Percona XtraBackup is an online (non-blocking) backup solution for InnoDB
engines. It features uninterrupted transaction processing during backups for
InnoDB, but can also backup MyISAM tables.

%package test
Summary:        Test suite for Percona XtraBackup
Group:          Productivity/Archiving/Backup
Requires:       %{_bindir}/mysql
Requires:       %{name} = %{version}

%description test
This package contains the test suite for Percona XtraBackup %{version}

%prep
%setup -q -n percona-xtrabackup-%{version} -a 2
rm -rf storage/innobase/xtrabackup/src/jsmn

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%define _lto_cflags %{nil}
%cmake \
    -DCMAKE_C_FLAGS:STRING="%{optflags} -DXTRABACKUP_VERSION=\\\"%{version}\\\" -DDBUG_OFF" \
    -DCMAKE_CXX_FLAGS:STRING="%{optflags} -DXTRABACKUP_VERSION=\\\"%{version}\\\" -DDBUG_OFF" \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -pie -Wl,-z,relro,-z,now" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -pie -Wl,-z,relro,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -pie -Wl,-z,relro,-z,now" \
    -DBUILD_CONFIG=xtrabackup_release -DWITH_SSL=system \
    -DINSTALL_MYSQLTESTDIR=%{_datadir}/percona-xtrabackup-test \
    -DINSTALL_PLUGINDIR="%{_lib}/xtrabackup/plugins" \
    -DMYSQL_UNIX_ADDR=%{_rundir}/mysql/mysql.sock \
    -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_STATIC_LIBS:BOOL=ON \
    -DWITH_BOOST=../boost_1_59_0

make %{?_smp_mflags}

%install
%cmake_install
find %{buildroot} -type f -name "*.a" -print -delete

%files
%license COPYING
%{_bindir}/innobackupex
%{_bindir}/xtrabackup
%{_bindir}/xbstream
%{_bindir}/xbcrypt
%{_bindir}/xbcloud
%{_bindir}/xbcloud_osenv
%dir %{_libdir}/xtrabackup
%dir %{_libdir}/xtrabackup/plugins
%{_libdir}/xtrabackup/plugins/*.so

%files test
%{_datadir}/percona-xtrabackup-test

%changelog
