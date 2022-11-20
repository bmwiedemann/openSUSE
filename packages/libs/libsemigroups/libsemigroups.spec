#
# spec file for package libsemigroups
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


Name:           libsemigroups
%define lname	libsemigroups2
Version:        2.3.2
Release:        0
Summary:        Library with algorithms for computing finite and finitely presented semigroups
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/libsemigroups/libsemigroups
Source:         https://github.com/libsemigroups/libsemigroups/releases/download/v%version/%name-%version.tar.gz
Patch1:         pkgconfig.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fmt) >= 8.1.1

%description
A C++14 library containing implementations of several algorithms for
computing finite and finitely presented semigroups.

%package -n %lname
Summary:        Library with algorithms for computing finite and finitely presented semigroups
Group:          System/Libraries

%description -n %lname
A C++14 library containing implementations of several algorithms for
computing finite and finitely presented semigroups, namely:

  * the Froidure-Pin algorithm for computing finite semigroups
  * the Todd-Coxeter algorithm for finitely presented semigroups and monoids;
  * the Knuth-Bendix algorithm for finitely presented semigroups and monoids;
  * the Schreier-Sims algorithm for permutation groups.

%package devel
Summary:        Development files for the Semigroups library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A C++14 library containing implementations of several algorithms for
computing finite and finitely presented semigroups, namely.

This subpackage provides the development headers for it.

%prep
%autosetup -p1

%build
autoreconf -fi
# hpcombi requires AVX-256, which is not guaranteed to exist everywhere
%configure --disable-static --disable-hpcombi \
	--enable-eigen --with-external-eigen \
	--enable-fmt --with-external-fmt
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libsemigroups.so.2*

%files devel
%_includedir/libsemigroups/
%_libdir/libsemigroups.so
%_libdir/pkgconfig/*.pc
%license LICENSE
%doc README.rst

%changelog
