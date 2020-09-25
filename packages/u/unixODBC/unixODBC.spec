#
# spec file for package unixODBC
#
# Copyright (c) 2020 SUSE LLC
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


Name:           unixODBC
Version:        2.3.9
Release:        0
Summary:        ODBC driver manager with some drivers included
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Databases/Tools
URL:            http://www.unixodbc.org/
Source0:        ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        unixODBC-rpmlintrc
Patch1:         unixODBC-paths.patch
Patch2:         unixODBC-gccwarnings.patch
# https://github.com/lurcher/unixODBC/issues/8
Patch3:         unixODBC-2.3.1-libodbcinst-exports.patch
Patch4:         unixODBC-2.3.6-declarations.patch 
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  libltdl-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
# bsc#1062860: to stay feature complete
Recommends:     psqlODBC

%package -n libodbc2
Summary:        Open Database Connectivity API
Group:          System/Libraries

%description -n libodbc2
ODBC is an API that abstracts the access to different database
management systems.

%package devel
Summary:        Includes for ODBC Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libodbc2 = %{version}
Conflicts:      libiodbc-devel

%description
UnixODBC aims to provide a complete ODBC solution for the Linux
platform. Further drivers can be found at http://www.unixodbc.org/.

%description devel
Includes for ODBC development (based on unixODBC).

%prep
%setup -q
%patch1
%patch2
%patch3 -p1
%patch4 -p1

%build
perl -i -pe 's{^ACLOCAL_AMFLAGS.*}{}' Makefile.am
export -n LANG LINGUAS LC_ALL
rm -rf libltdl
autoreconf -fvi
%configure \
    --with-gnu-ld \
    --enable-ltdllib \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --enable-iconv \
    --with-iconv-char-enc=UTF8 \
    --with-iconv-ucode-enc=UTF16LE \
    --enable-fastvalidate \
    --enable-threads \
    --enable-gui=no \
    --disable-stats \
    --enable-driverc \
    --enable-drivers \
    --enable-driver-conf
%make_build

%install
install -d -m 755 "%{buildroot}/%{_sysconfdir}/%{name}"
install -d -m 755 "%{buildroot}/%{_libdir}/%{name}"
%make_install
rm -rf "%{buildroot}/%{_datadir}/libtool"
# packaged in gui-gtk
rm -f "%{buildroot}/%{_libdir}"/libmimerS.*
find %{buildroot} -type f -name "*.la" -delete -print

# bsc#1062860: we want psqlODBC instead of this unmaintained example driver
rm -f "%{buildroot}/%{_libdir}"/unixODBC/libodbcpsql.*

%post   -n libodbc2 -p /sbin/ldconfig
%postun -n libodbc2 -p /sbin/ldconfig

%files
%license COPYING
%attr(644,root,root) %doc AUTHORS ChangeLog NEWS README doc/*.html doc/*.gif
%docdir %{_mandir}
%{_mandir}/man1/dltest.1%{?ext_man}
%{_mandir}/man1/isql.1%{?ext_man}
%{_mandir}/man1/iusql.1%{?ext_man}
%{_mandir}/man1/odbc_config.1%{?ext_man}
%{_mandir}/man1/odbcinst.1%{?ext_man}
%{_mandir}/man5/odbc.ini.5%{?ext_man}
%{_mandir}/man5/odbcinst.ini.5%{?ext_man}
%{_mandir}/man7/unixODBC.7%{?ext_man}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/ODBCDataSources
%dir %{_libdir}/%{name}
%config %{_sysconfdir}/%{name}/odbc.ini
%config %{_sysconfdir}/%{name}/odbcinst.ini
%{_bindir}/dltest
%{_bindir}/isql
%{_bindir}/iusql
%{_bindir}/odbcinst
%{_bindir}/odbc_config
%{_bindir}/slencheck
%{_libdir}/libodbc.so
%{_libdir}/libodbcinst.so
%{_libdir}/libodbccr.so
%{_libdir}/%{name}

%files -n libodbc2
%{_libdir}/libodbc.so.*
%{_libdir}/libodbcinst.so.*
%{_libdir}/libodbccr.so.*

# All .so files are in the main package as many ext apps
# dlopen those so you need these on regular package.
%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/odbc.pc
%{_libdir}/pkgconfig/odbccr.pc
%{_libdir}/pkgconfig/odbcinst.pc

%changelog
