#
# spec file for package libservicelog
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libservicelog
%define lname	libservicelog-1_1-1
Version:        1.1.19
Release:        0
Summary:        Servicelog Database and Library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/power-ras/libservicelog/

#Git-Clone:	https://github.com/power-ras/libservicelog.git
#Git-Web:	https://github.com/power-ras/libservicelog/
Source0:        https://github.com/power-ras/libservicelog/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        libservicelog-rpmlintrc
Requires(pre):  %{_sbindir}/groupadd
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  librtas-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  sqlite3-devel
ExclusiveArch:  ppc ppc64 ppc64le

%description
The libservicelog package contains a library to create and maintain a
database for storing events related to system service. This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the
system.

%package -n %lname
Summary:        Servicelog Database and Library
Group:          System/Libraries
Requires:       %name

%description -n %lname
The libservicelog package contains a library to create and maintain a
database for storing events related to system service. This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the
system.

%package        devel
Summary:        Development files for libservicelog
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel
Requires:       sqlite3-devel

%description    devel
Header files for building with libservicelog.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%pre
getent group service >/dev/null || %{_sbindir}/groupadd -r service

%post    -n %lname -p /sbin/ldconfig
%postun  -n %lname -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%attr( 754, root, service ) %dir /var/lib/servicelog
%attr( 644, root, service ) /var/lib/servicelog/servicelog.db

%files -n %lname
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/servicelog-1
%{_libdir}/pkgconfig/servicelog-1.pc
%{_libdir}/*.so

%changelog
