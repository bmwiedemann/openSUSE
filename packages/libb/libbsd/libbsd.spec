#
# spec file for package libbsd
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


%define lname	libbsd0
Name:           libbsd
Version:        0.9.1
Release:        0
Summary:        Provides useful functions commonly found on BSD systems
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            http://libbsd.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/git/libbsd
#Git-Web:	http://cgit.freedesktop.org/libbsd/
Source0:        https://archive.hadrons.org/software/%{name}/%{name}-%{version}.tar.xz
Source1:        https://archive.hadrons.org/software/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
This library provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package -n %{lname}
Summary:        Provides useful functions commonly found on BSD systems
Group:          System/Libraries

%description -n %{lname}
This library provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package devel
Summary:        Development headers and files for libbsd
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
This library provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package ctor-static
Summary:        Development headers and files for libbsd
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}-%{release}
Requires:       pkgconfig

%description ctor-static
The libbsd-ctor static library is required if setproctitle() is to be used
when libbsd is loaded via dlopen() from a threaded program.  This can be
configured using "pkg-config --libs libbsd-ctor".

%prep
%setup -q

%build
%define _lto_cflags %{nil}
%configure \
	--disable-static \
	--with-pic
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s  %{buildroot}

%check
make %{?_smp_mflags} check

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
