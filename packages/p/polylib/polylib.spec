#
# spec file for package polylib
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


%define lname	libpolylibgmp8
Name:           polylib
Version:        5.22.5
Release:        0
Summary:        Library for computing homotopy continuation of roots
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://icps.u-strasbg.fr/polylib/
Source:         https://icps.u-strasbg.fr/polylib/polylib_src/%name-%version.tar.gz
Patch1:         static-decls.patch
BuildRequires:  gcc-c++
BuildRequires:  ntl-devel
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1590
BuildRequires:  pkgconfig(gmp)
%else
BuildRequires:  gmp-devel
%endif

%description
The Polyhedral Library (PolyLib) operates on objects made up of
unions of polyhedra of any dimension.

%package -n %lname
Summary:        Library for computing homotopy continuation of roots
Group:          System/Libraries

%description -n %lname
The Polyhedral Library (PolyLib) operates on objects made up of
unions of polyhedra of any dimension.

%package devel
Summary:        Development files for PolyLib
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
%if 0%{?suse_version} >= 1590
Requires:       pkgconfig(gmp)
%else
Requires:       gmp-devel
%endif

%description devel
The Polyhedral Library (PolyLib) operates on objects made up of
unions of polyhedra of any dimension.

It can manipulate non-parameterized unions of polyhedra
(intersection, difference, union, convex hull, simplify, image and
preimage, plus some input and output functions), parameterized
vertices computation, and Ehrhart polynomials computation.

This subpackage contains the include files and library links for
developing with PolyLib.

%prep
%autosetup -p1

%build
%configure --disable-static --with-libgmp
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files
%_bindir/c2p
%_bindir/disjoint*
%_bindir/*ehrhart*
%_bindir/findv
%_bindir/ppgmp
%_bindir/r2p

%files -n %lname
%_libdir/libpolylibgmp.so.8*

%files devel
%license COPYING
%_includedir/polylib/
%_libdir/libpolylibgmp.so
%_libdir/pkgconfig/*.pc

%changelog
