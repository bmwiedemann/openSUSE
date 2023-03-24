#
# spec file for package libbsd
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	libbsd0
Name:           libbsd
Version:        0.11.7
Release:        0
Summary:        Library with functions commonly found on BSD systems
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://libbsd.freedesktop.org/
Source0:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz
Source1:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch0:         libbsd-glibc-2.34-closefrom.patch
BuildRequires:  fdupes
BuildRequires:  libmd-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
This library provides functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package -n %{lname}
Summary:        Library with functions commonly found on BSD systems
Group:          System/Libraries

%description -n %{lname}
This library provides functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package devel
Summary:        Development headers and files for libbsd
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Requires:       libmd-devel

%description devel
This library provides functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package ctor-static
Summary:        Development headers and files for libbsd
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}
Requires:       pkgconfig

%description ctor-static
The libbsd-ctor static library is required if setproctitle() is to be used
when libbsd is loaded via dlopen() from a threaded program.  This can be
configured using "pkg-config --libs libbsd-ctor".

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -ffat-lto-objects"
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s  %{buildroot}

%check
%make_build check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%doc ChangeLog
%{_libdir}/libbsd.so.0*

%files devel
%{_includedir}/bsd
%{_libdir}/libbsd.so
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_libdir}/pkgconfig/libbsd.pc
%{_libdir}/pkgconfig/libbsd-overlay.pc

%files ctor-static
%{_libdir}/libbsd-ctor.a
%{_libdir}/pkgconfig/libbsd-ctor.pc

%changelog
