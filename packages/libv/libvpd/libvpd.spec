#
# spec file for package libvpd
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


%define soversion -2_2-3
# 15.2 is no longer updated but is supported migration target
# versions before 15.2 cannot have a package that obsoletes libvpd2
# to be able to migrate to 15.2 which has lsvpd that requires libvpd2
# let libvpd2 provide the udev rules instead
%define basepackage ( ! 0%{?sle_version} || 0%{?sle_version} >= 150200 )

Name:           libvpd
Version:        2.2.9
Release:        0
Summary:        VPD Database access library for lsvpd
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/power-ras/libvpd
Source:         https://github.com/power-ras/libvpd/archive/v%{version}.tar.gz#/%{name}2-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         libvpd2.makefile.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(zlib)

%description
The libvpd package contains classes that are used to access a Vital
Product Data (VPD) database created by vpdupdate in the lsvpd package.

%package -n %{name}%{soversion}
Summary:        VPD Database access library for lsvpd
Group:          System/Libraries
%if %basepackage
Requires:       %{name}-base
%else
Requires:       libvpd2
%endif

%description -n %{name}%{soversion}
The libvpd package contains classes that are used to access a Vital
Product Data (VPD) database created by vpdupdate in the lsvpd package.

%package base
Summary:        Udev rules for VPD Database access library
Group:          System/Libraries
Obsoletes:      libvpd2 < 2.2.9

%description base
Udev rules for libvpd library used to access a vpd database created by
vpdupdate in the lsvpd package.

%package devel
Summary:        VPD Database access library for lsvpd
Group:          Development/Languages/C and C++
Requires:       %{name}%{soversion} = %{version}-%{release}
Requires:       pkgconfig(sqlite3)
Obsoletes:      libvpd2-devel < 2.2.9

%description devel
The libvpd-devel package contains development libraries and header
files that are used to access a vpd database created by vpdupdate in
the lsvpd package.

%prep
%autosetup -p1

%build
%if 0%{?sle_version} && 0%{?sle_version} < 150000
CFLAGS="%optflags -std=gnu99"
export CFLAGS
%endif
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if ! %basepackage
rm %{buildroot}%{_udevrulesdir}/90-vpdupdate.rules
rmdir -p --ignore-fail-on-non-empty %{buildroot}%{_udevrulesdir}
%endif

%post -n %{name}%{soversion} -p /sbin/ldconfig
%postun -n %{name}%{soversion} -p /sbin/ldconfig

%files -n %{name}%{soversion}
%{_libdir}/*.so.*

%if %basepackage
%files base
%{_udevrulesdir}/90-vpdupdate.rules
%endif

%files devel
%license COPYING
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
