#
# spec file for package pplite
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


%define lname   libpplite1
%define _lto_cflags %nil
Name:           pplite
Version:        0.7
Release:        0
Summary:        Computations with polyhedra
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.cs.unipr.it/~zaffanella/PPLite/
Source:         https://www.cs.unipr.it/~zaffanella/PPLite/releases/%name-%version.tar.gz
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
PPLite is a C++ library implementing the abstract domain of convex polyhedra,
to be used in tools for static analysis and verification.

%package -n %lname
Summary:        Library for computations with polyhedra
Group:          System/Libraries

%description -n %lname
PPLite is a C++ library implementing the abstract domain of convex polyhedra,
to be used in tools for static analysis and verification.

%package devel
Summary:        Headers and generators for pplite
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
PPLite is a C++ library implementing the abstract domain of convex polyhedra,
to be used in tools for static analysis and verification.
The main characteristics of PPLite:

  * Both closed and NNC rational convex polyhedra are supported.
  * Exact computations are based on FLINT.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libpplite.so.*

%files devel
%_bindir/pplite_lcdd
%_libdir/libpplite.so
%_includedir/pplite/

%changelog
