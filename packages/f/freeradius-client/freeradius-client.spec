#
# spec file for package freeradius-client
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           freeradius-client
Version:        1.1.7
Release:        0
Summary:        FreeRADIUS Client Software
License:        BSD-2-Clause
Group:          Productivity/Networking/Radius/Clients
Url:            http://www.freeradius.org/freeradius-client/
Source:         ftp://ftp.freeradius.org/pub/freeradius/%{name}-%{version}.tar.gz
Source1:        README.SUSE
Source2:        login.example
Patch:          freeradius-client-missing_size_t_definition.patch
BuildRequires:  libnettle-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
Obsoletes:      radiusclient
Obsoletes:      radiusclient-ng
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A portable, easy-to-use and standard compliant library suitable for
developing free and commercial software that need support for a RADIUS
protocol (RFCs 2128 and 2139).

%package libs
Summary:        Shared library of FreeRADIUS Client
Group:          Productivity/Networking/Radius/Clients

%description libs
The package contains the shared library of FreeRADIUS Client

%package devel
Summary:        Header files, libraries and development documentation for freeradius-client
Group:          Productivity/Networking/Radius/Clients
Requires:       %{name}-libs = %{version} glibc-devel

%description devel
This package contains the header files, static libraries and
development documentation for freeradius-client. You need to install
freeradius-client-devel if you want to develop applications using
freeradius-client.

%prep
%setup -q
%patch -p1
find -type d -name CVS -print | xargs rm -rf
cp %{SOURCE1} .
cp %{SOURCE2} login.radius

%build
autoreconf -fiv
%configure \
    --localstatedir=%{_localstatedir}/lib \
    --enable-shadow \
    --with-nettle \
    --with-secure-path \
	--disable-static \
	--with-pic
make %{?_smp_mflags}

%install
make "DESTDIR=$RPM_BUILD_ROOT" install
rm -f %{buildroot}/%{_sbindir}/login.radius
rm -f login.radius/Makefile*
rm -f login.radius/migs/Makefile*
find %{buildroot} -type f -name "*.la" -delete -print

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc BUGS COPYRIGHT README.radexample doc/ChangeLog doc/instop.html doc/login.example
%doc login.radius README.SUSE
%dir %{_sysconfdir}/radiusclient
%{_sysconfdir}/radiusclient/dictionary
%{_sysconfdir}/radiusclient/dictionary.*
%config(noreplace) %{_sysconfdir}/radiusclient/radiusclient.conf
%config(noreplace) %{_sysconfdir}/radiusclient/issue
%config(noreplace) %{_sysconfdir}/radiusclient/port-id-map
%config(noreplace) %{_sysconfdir}/radiusclient/servers
%{_sbindir}/*

%files libs
%defattr(-, root, root)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
