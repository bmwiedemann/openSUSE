#
# spec file for package munit
#
# Copyright (c) 2020 SUSE LLC
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


Name:           munit
%define lname libmunit0suse0
Version:        0.2.0+git38
Release:        0
Summary:        Unit testing framework for C
License:        MIT
Group:          Development/Tools/Building
URL:            https://github.com/nemequ/munit/

Source:         %name-%version.tar.xz
Patch1:         0001-build-invert-install-condition-for-libmunit.so.patch
Patch2:         unversioned-libs.patch
BuildRequires:  meson

%description
µnit is a unit testing framework for C.

%package -n %lname
Summary:        Unit testing framework for C
Group:          System/Libraries

%description -n %lname
µnit is a unit testing framework for C.
 * Assertion macros which make for nice error messages.
 * Repeatable cross-platform random number generation, including
   support for supplying a seed via CLI.
 * Timing of both wall-clock and CPU time.
 * Parameterized tests, nested test suites.

%package devel
Summary:        Headers for the munit testing framework for C
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Headers for µnit, a unit testing framework for C.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libmunit.so.*

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%license COPYING

%changelog
