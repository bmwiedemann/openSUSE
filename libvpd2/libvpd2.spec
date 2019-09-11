#
# spec file for package libvpd2
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


Name:           libvpd2
Version:        2.2.6
Release:        0
Summary:        VPD Database access library for lsvpd
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/open-power-host-os/libvpd
Source:         http://downloads.sourceforge.net/project/linux-diag/libvpd/%{version}/libvpd-%{version}.tar.gz
Source2:        baselibs.conf
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
The libvpd_cxx package contains the classes that are used to access a
vpd database created by vpdupdate in the lsvpd package.

%package devel
Summary:        VPD Database access library for lsvpd
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(sqlite3)

%description devel
The libvpd-devel package contains development libraries and header
files that are used to access a vpd database created by vpdupdate in
the lsvpd package.

%prep
%setup -q -n libvpd-%{version}
%patch1 -p1

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*
%{_udevrulesdir}/90-vpdupdate.rules

%files devel
%license COPYING
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
