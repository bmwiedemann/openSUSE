#
# spec file for package libHX
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


Name:           libHX
%define lname   libHX32
Version:        4.8
Release:        0
Summary:        Collection of routines for C and C++ programming
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://inai.de/projects/libhx/

Source:         https://inai.de/files/libhx/libHX-%version.tar.xz
Source2:        https://inai.de/files/libhx/libHX-%version.tar.asc
Source3:        baselibs.conf
Source4:        %name.keyring
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  xz

%description
libHX is a C library (with some C++ bindings available) that provides
data structures and functions commonly needed, such as maps, deques,
linked lists, string formatting and autoresizing, option and config
file parsing, type checking casts and more.

%package -n %lname
Summary:        Collection of routines for C and C++ programming
Group:          System/Libraries

%description -n %lname
libHX is a C library (with some C++ bindings available) that provides
data structures and functions commonly needed, such as maps, deques,
linked lists, string formatting and autoresizing, option and config
file parsing, type checking casts and more.

%package devel
Summary:        Development for libHX, a routines collection for C and C++ programming
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libHX is a C library (with some C++ bindings available) that provides
data structures and functions commonly needed, such as maps, deques,
linked lists, string formatting and autoresizing, option and config
file parsing, type checking casts and more.

This subpackage contains the header files.

%prep
%autosetup -p1

%build
mkdir obj
pushd obj/
%define _configure ../configure
%configure --includedir="%_includedir/%name" --docdir="%_docdir/%name"
%make_build
popd

%install
b="%buildroot"
%make_install -C obj
mkdir -p "$b/%_docdir/%name"
install -pm0644 doc/* "$b/%_docdir/%name"
rm -f "$b/%_docdir/%name"/Makefile*
find "$b/%_libdir" -type f -name "*.la" -delete

%check
%make_build -C obj check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libHX*.so.32*

%files devel
%_docdir/%name/
%_includedir/%name/
%_libdir/libHX*.so
%_libdir/pkgconfig/libHX.pc

%changelog
