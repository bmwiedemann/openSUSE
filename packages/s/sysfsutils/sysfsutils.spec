#
# spec file for package sysfsutils
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


Name:           sysfsutils
Version:        2.1.1
Release:        0
Summary:        System Utilities Package / Libsysfs
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/linux-ras/sysfsutils
Source:         sysfsutils-2_1_1.tar.gz
Provides:       libsysfs
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
This package's purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.

%package -n libsysfs2
Summary:        Library for interfacing with the kernel's sysfs filesystem
Group:          System/Libraries

%description -n libsysfs2
This package's purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.

%package devel
Summary:        Development files for libsysfs
Group:          Development/Libraries/C and C++
Requires:       libsysfs2 = %{version}

%description devel
Libsysfs's purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.

This package contains the development files for libsysfs.

%prep
%autosetup -p1

%build
%global optflags %{optflags} -fcommon
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
rm -v %{buildroot}/%{_libdir}/libsysfs.la
# don't install the tools
rm -f %{buildroot}/%{_bindir}/dlist_test
rm -f %{buildroot}/%{_bindir}/get_device
rm -f %{buildroot}/%{_bindir}/get_driver
rm -f %{buildroot}/%{_bindir}/get_module
rm -f %{buildroot}/%{_bindir}/testlibsysfs

%post   -n libsysfs2 -p /sbin/ldconfig
%postun -n libsysfs2 -p /sbin/ldconfig

%files
%{_bindir}/systool
%{_mandir}/man1/systool.1.gz

%files -n libsysfs2
%{_libdir}/libsysfs.so.*
%doc README
%license COPYING

%files devel
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
%{_libdir}/libsysfs.so
%{_libdir}/pkgconfig/libsysfs.pc

%changelog
