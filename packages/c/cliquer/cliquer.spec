#
# spec file for package cliquer
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


Name:           cliquer
%define lname   libcliquer1
Version:        1.22
Release:        0
Summary:        C routines for finding cliques in graphs
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://users.aalto.fi/~pat/cliquer.html
Source:         https://github.com/dimpase/autocliquer/releases/download/v%version/%name-%version.tar.gz
Source9:        %name-rpmlintrc
Conflicts:      python3-cl

%description
Cliquer is a set of C routines for finding cliques in an arbitrary
weighted graph. It uses an exact branch-and-bound algorithm.
Features:

  * support for both weighted and unweighted graphs (faster routines
    for unweighted graphs)
  * search for maximum clique / maximum-weight clique
  * search for clique with size / weight within a given range
  * restrict search to maximal cliques
  * store found cliques in memory
  * call a user-defined function for every clique found
  * Cliquer is re-entrant, so you can use the clique-searching
    functions from within the callback function

%package -n %lname
Summary:        C library for finding cliques in graphs
Group:          System/Libraries

%description -n %lname
Cliquer is a set of C routines for finding cliques in an arbitrary
weighted graph and uses an exact branch-and-bound algorithm.

%package devel
Summary:        Development files for Cliquer
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Cliquer is a set of C routines for finding cliques in an arbitrary
weighted graph and uses an exact branch-and-bound algorithm.

This subpackage provides the development headers for Cliquer's library.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/cl
%_datadir/cliquer
%license COPYING

%files -n libcliquer1
%_libdir/libcliquer.so.1*

%files devel
%_includedir/cliq*
%_libdir/libcliquer.so

%changelog
