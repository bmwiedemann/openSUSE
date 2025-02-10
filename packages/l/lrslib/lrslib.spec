#
# spec file for package lrslib
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


%define dullver	073
%define dullver2 073
%define lname   liblrs1
Name:           lrslib
Version:        7.3
Release:        0
Summary:        Reverse Search Vertex Enumeration program
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://cgm.cs.mcgill.ca/~avis/C/lrs.html
Source:         http://cgm.cs.mcgill.ca/~avis/C/lrslib/archive/%name-%dullver.tar.gz
Patch1:         lrs-128.diff
Patch2:         lrs-compile.diff
Patch3:         lrs-types.diff
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libtool >= 2

%description
lrslib is a library for the reverse search algorithm for vertex
enumeration/convex hull problems and comes with a choice of three
arithmetic packages. Input file formats are compatible with the
cddlib package. All computations are done exactly in either
multiple precision or fixed integer arithmetic. Output is not stored
in memory, so even problems with very large output sizes can
sometimes be solved.

%package -n %lname
Summary:        Reverse Search Vertex Enumeration library
Group:          System/Libraries

%description -n %lname
lrslib is a library for the reverse search algorithm for vertex
enumeration/convex hull problems and comes with a choice of three
arithmetic packages. Input file formats are compatible with the
cddlib package. Computations are done in multiprecision
arithmetic.

%package devel
Summary:        Development files for Reverse Search Vertex Enumeration
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
lrslib is a library for the reverse search algorithm for vertex
enumeration/convex hull problems and comes with a choice of three
arithmetic packages.

This subpackage contains libraries and header files for developing
applications that want to make use of lrslib.

%prep
%autosetup -n %name-%dullver -p1

%build
%make_build CFLAGS="%optflags -Ilrsarith-011" CXXFLAGS="%optflags -Ilrsarith-011" \
	PACKAGE_VERSION="%version" all-shared

%install
%make_install prefix="%_prefix" PACKAGE_VERSION="%version"
# stupid things
if [ "%_lib" != lib ]; then
	mkdir -p "%buildroot/%_libdir"
	mv "%buildroot/%_libdir/../lib"/* "%buildroot/%_libdir/"
fi
chmod a-x COPYING README "%buildroot/%_includedir/lrslib"/*.h

%ldconfig_scriptlets -n %lname

%files
%_bindir/*
%license COPYING
%doc README

%files -n %lname
%_libdir/liblrs.so.1*

%files devel
%_includedir/lrslib/
%_libdir/liblrs.so

%changelog
