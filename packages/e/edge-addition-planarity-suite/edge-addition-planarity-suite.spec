#
# spec file for package edge-addition-planarity-suite
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


%define lname   libplanarity0
Name:           edge-addition-planarity-suite
Version:        3.0.2.0
Release:        0
Summary:        Edge Addition Planarity Suite
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/graph-algorithms/edge-addition-planarity-suite
Source:         https://github.com/graph-algorithms/edge-addition-planarity-suite/archive/Version_%version.tar.gz
BuildRequires:  libtool

%description
EAPS provides implementations of the edge addition planar graph
embedding algorithm and related algorithms, including a planar graph
drawing method, an isolator for a minimal subgraph obstructing
planarity in non-planar graphs, outerplanar graph embedder and
obstruction isolator algorithms, and tester/isolator algorithms for
subgraphs homeomorphic to K_{2,3}, K_4, and K_{3,3}.

%package -n %lname
Summary:        Edge Addition Planarity Suite main library
Group:          System/Libraries

%description -n %lname
EAPS provides implementations of the edge addition planar graph
embedding algorithm and related algorithms.

%package devel
Summary:        Development files for the Edge Addition Planarity suite
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
EAPS provides implementations of the edge addition planar
graph embedding algorithm and related algorithms

This subpackage provides the development headers for it.

%prep
%autosetup -p1 -n %name-Version_%version

%build
autoreconf -fi
%configure --disable-static --docdir="%_defaultdocdir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%doc README.md
%doc %_defaultdocdir/%name
%_bindir/planarity
%_mandir/man1/planarity.1*

%files -n %lname
%license LICENSE.TXT
%_libdir/libplanarity.so.0*

%files devel
%_includedir/planarity/
%_libdir/libplanarity.so
%license LICENSE*

%changelog
