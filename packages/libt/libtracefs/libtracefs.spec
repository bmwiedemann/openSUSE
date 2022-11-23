#
# spec file for package libtracefs
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


Name:           libtracefs
%define lname   libtracefs1
Version:        1.6.0
Release:        0
Summary:        Linux kernel trace file system library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
Source:         https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/%name-%version.tar.gz
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libtraceevent) >= 1.3

%description
This library provides C APIs to access the kernel trace file system.

%package -n %lname
Summary:        Linux kernel trace file system library
Group:          System/Libraries

%description -n %lname
This library provides C APIs to access the kernel trace file system.

%package devel
Summary:        Development files for libtracefs
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This library provides C APIs to access the kernel trace file system.

This subpackage contains the header files.

%prep
%autosetup -p1

%build
%make_build V=1 prefix="%_prefix"

%install
%make_install V=1 prefix="%_prefix" \
	pkgconfig_dir=%{_libdir}/pkgconfig \
        %nil
# always the same issues
find "%buildroot/%_includedir" -type f -name "*.h" -exec chmod a-x {} +
rm -f "%buildroot/%_libdir"/*.a
if ldd -r "%buildroot/%_libdir/libtracefs.so" 2>&1 | grep -q undefined; then
	exit 1
fi

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libtracefs.so.1*
%license LICENSES/LGPL-2.1

%files devel
%_includedir/*
%_libdir/libtracefs.so
%_libdir/pkgconfig/*.pc

%changelog
