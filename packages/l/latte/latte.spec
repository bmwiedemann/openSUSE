#
# spec file for package latte
#
# Copyright (c) 2025 SUSE LLC
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


Name:           latte
Version:        1.7.6
Release:        0
Summary:        Computations with polyhedra
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.ucdavis.edu/~latte/
Source:         https://github.com/latte-int/latte/releases/download/version_1_7_6/latte-int-1.7.6.tar.gz
Patch1:         nothrow.diff
Patch2:         autoconf.diff
BuildRequires:  pkgconfig(cddlib) >= 0.94l
BuildRequires:  4ti2-devel
BuildRequires:  cddlib-tools
BuildRequires:  fdupes
BuildRequires:  gmp-devel >= 3.1.1
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ntl-devel >= 5.4
Requires:       4ti2
Requires:       cddlib-tools

%description
LattE (Lattice point Enumeration) is a software dedicated to the
problems of counting lattice points and integration inside convex
polytopes. LattE contains an implementation of Barvinok's algorithm.

%prep
%autosetup -p1 -n %name-int-%version

%build
autoreconf -fi
# explicitly select CDD variant (https://github.com/cddlib/cddlib/issues/49)
%configure --disable-static CDDLIB_LIBS=-lcddgmp
%make_build

%install
%make_install
b="%buildroot"
rm -f "$b/%_libdir"/*.la
# No headers available
rm -f "$b/%_libdir/liblatte.so"

mkdir -p "$b/%_docdir"
mv "$b/%_datadir/latte-int/doc" "$b/%_docdir/%name"
ln -s "%_docdir/%name" "$b/%_datadir/latte-int/doc"
%fdupes %buildroot/%_prefix

%check
if ! %make_build check; then
	cat code/latte/test-suite.log
	exit 1
fi

%ldconfig_scriptlets

%files
%_bindir/ConvertCDD*
%_bindir/count*
%_bindir/integrate
%_bindir/latte*
%_bindir/polyhedron-to-cones
%_bindir/*ehrhart*
%_bindir/triangulate
%_libdir/liblatte.so.0*
%_datadir/latte-int/
%_docdir/%name/
%license COPYING

%changelog
