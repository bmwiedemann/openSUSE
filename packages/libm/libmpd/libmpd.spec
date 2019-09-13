#
# spec file for package libmpd
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libmpd
Version:        11.8.17
Release:        0
Summary:        Client Library to the Music Player Daemon
License:        GPL-2.0+
Group:          System/Libraries
Url:            http://gmpclient.org/
Source:         http://download.sarine.nl/Programs/gmpc/11.8/libmpd-%{version}.tar.gz
Source1:        baselibs.conf
#PATCH-FIX-UPSTREAM libmpd-glibc-2.20.patch avvissu@yandex.ru -- Fix build with glibc-2.20
Patch1:         libmpd-glibc-2.20.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libtool
%if 0%{?suse_version} == 1110
BuildRequires:  glib2-devel
%else
BuildRequires:  pkgconfig(glib-2.0)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define libname libmpd1

%description
libmpd is a library that provides high-level, callback-based access to Music
Player Daemon.

%package -n %libname
Summary:        The libmpd package
Group:          System/Libraries

%description -n %libname
libmpd is a library that provides high-level, callback-based access to Music
Player Daemon.

%package devel
Summary:        Development Files for libmpd
Group:          Development/Languages/C and C++
Requires:       pkgconfig(glib-2.0)
Requires:       %libname = %version

%description devel
This package provides the API documentation and development files needed to
develop applications based on libmpd.


%prep
%setup -q
%patch1 -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}
make doc

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la
%fdupes -s doc

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc ChangeLog COPYING doc/html
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc

%changelog
