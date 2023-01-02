#
# spec file for package libtracefs
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.6.3
Release:        0
Summary:        Linux kernel trace file system library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
Source:         https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/%name-%version.tar.gz
Patch1:         0001-libtracefs-Add-initial-support-for-meson.patch
BuildRequires:  asciidoc
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  source-highlight
BuildRequires:  xmlto
BuildRequires:  xz
BuildRequires:  pkgconfig(libtraceevent) >= 1.3

%description
This library provides C APIs to access the kernel trace file system.

%package -n %lname
Summary:        Linux kernel trace file system library
Group:          System/Libraries

%description -n %lname
This library provides C APIs to access the kernel trace file system.

%package tools
Summary:        Tools for libtracefs
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description tools
This library provides C APIs to access the kernel trace file system.

This subpackage contains tools.

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
%meson \
    -Ddocs-build=true \
    -Dhtmldir="%_docdir/%name"
%meson_build

%install
%meson_install

%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libtracefs.so.1*
%license LICENSES/LGPL-2.1

%files tools
%_bindir/sqlhist
%_mandir/man1/*

%files devel
%_includedir/*
%_libdir/libtracefs.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*
%_docdir/%name/

%changelog
