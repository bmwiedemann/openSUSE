#
# spec file for package bliss
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libbliss0_77
Name:           bliss
Version:        0.77
Release:        0
Summary:        A Tool for Computing Automorphism Groups and Canonical Labelings of Graphs
License:        LGPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://users.aalto.fi/~tjunttil/bliss/
Source:         https://users.aalto.fi/~tjunttil/bliss/downloads/bliss-%version.zip
Patch1:         bliss-nodate.diff
Patch2:         cmake.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  unzip

%description
bliss is a tool for computing automorphism groups and canonical forms
of graphs. It has both a command line user interface as well as C++
and C programming language APIs.

%package -n %lname
Summary:        Library for computing automorphism groups and canonical forms of graphs
Group:          System/Libraries

%description -n %lname
bliss is a tool for computing automorphism groups and canonical forms
of graphs.

%package devel
Summary:        Development files for bliss, a math library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
bliss is a tool for computing automorphism groups and canonical forms
of graphs.

This subpackage contains libraries and header files for developing
applications that want to make use of the Bliss library.

%prep
%autosetup -p1

%build
%cmake -DUSE_GMP=ON -DBUILD_STATIC=OFF
%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%license COPYING*
%_bindir/bliss*

%files -n %lname
%_libdir/libbliss.so.%version

%files devel
%doc CHANGES.txt README.txt
%_libdir/libbliss.so
%_includedir/bliss/

%changelog
