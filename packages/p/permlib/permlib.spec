#
# spec file for package permlib
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           permlib
Version:        0.2.9
Release:        0
Summary:        C++ library for permutation computations
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            http://www.math.uni-rostock.de/~rehn/software/permlib.html

#Git-URL:	https://github.com/tremlin/PermLib
Source:         https://github.com/tremlin/PermLib/archive/v%version.tar.gz
Patch1:         modernize-boost.diff
BuildRequires:  c++_compiler
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
BuildRequires:  cmake
BuildArch:      noarch

%description
PermLib is a C++ library for permutation computations.
It is implemented in C++ header files only.

%package devel
Summary:        Header files for permlib, a permutation computation library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers-devel

%description devel
PermLib is a C++ library for permutation computations. It is
implemented in C++ header files only.

Currently, it supports set stabilizer and in-orbit computations,
based on bases and strong generating sets (BSGS). Additionally, it
computes automorphisms of symmetric matrices and find the
lexicographically smallest set in an orbit of sets. It also features
a very basic recognition of permutation group types.

%prep
%autosetup -n PermLib-%version -p1

%build
%cmake
# This is just the testsuite that gets built,
# but it's a worthwhile compiler/boost check.
%cmake_build

%install
mkdir -p "%buildroot/%_includedir/"
cp -a include/permlib "%buildroot/%_includedir/"

%files devel
%_includedir/permlib/
%license LICENSE

%changelog
