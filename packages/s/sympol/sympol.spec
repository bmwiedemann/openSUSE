#
# spec file for package sympol
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


Name:           sympol
%define lname	libsympol0_1
Version:        0.1.9
Release:        0
Summary:        Tool to work with symmetric polyhedra
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.math.uni-rostock.de/~rehn/software/sympol.html

#Git-Clone:     https://github.com/tremlin/SymPol
Source:         https://github.com/tremlin/SymPol/archive/refs/tags/v%version.tar.gz
Patch1:         unbundle.diff
Patch2:         cddlib.diff
Patch3:         bliss-0.77.diff
BuildRequires:  bliss-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 2.6
BuildRequires:  gmp-devel
BuildRequires:  libboost_headers-devel >= 1.34.1
BuildRequires:  libboost_program_options-devel >= 1.34.1
BuildRequires:  libboost_test-devel >= 1.34.1
BuildRequires:  lrslib-devel >= 0.4.2c
BuildRequires:  permlib-devel >= 0.2.8
BuildRequires:  pkgconfig(cddlib) >= 0.94f
BuildRequires:  pkgconfig(eigen3) >= 3.0

%description
SymPol is a C++ tool to work with symmetric polyhedra. It helps to
compute restricted automorphisms (parts of the linear symmetry group)
of polyhedra and performs polyhedral description conversion up to a
given or computed symmetry group.

%package -n %lname
Summary:        Library for working with symmetric polyhedra
Group:          System/Libraries

%description -n %lname
SymPol is a C++ tool to work with symmetric polyhedra. It helps to
compute restricted automorphisms (parts of the linear symmetry group)
of polyhedra and performs polyhedral description conversion up to a
given or computed symmetry group.

%package devel
Summary:        Header files for the sympol library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       permlib-devel >= 0.2.8

%description devel
SymPol is a C++ tool to work with symmetric polyhedra.
This package contains the header files for using the sympol library.

%prep
%autosetup -p1 -n SymPol-%version
rm -Rf external/cdd* external/lrs* external/permlib

%build
%cmake
%cmake_build

%install
%cmake_install
ln -s . "%buildroot/%_includedir/sympol/yal"
perl -i -lpe 's{#include ".*/}{#include "}g' "%buildroot/%_includedir/sympol"/*.h

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/sympol
%_mandir/m*/sympol*

%files -n %lname
%_libdir/libsympol.so.0*

%files devel
%_includedir/sympol/
%_libdir/libsympol.so

%changelog
