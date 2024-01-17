#
# spec file for package coxeter
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


Name:           coxeter
Version:        3.1+git7
Release:        0
Summary:        Computation on Coxeter groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://math.univ-lyon1.fr/~ducloux/coxeter/coxeter3/english/coxeter3_e.html
Source:         %name-%version.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  xz

%description
The Coxeter 3 C++ library can be used to do computation on and with

  * General Coxeter groups, implemented through the combinatorics of
    reduced words;
  * Reduced expression and normal form computations;
  * Bruhat ordering;
  * Ordinary Kazhdan-Lusztig polynomials;
  * Kazhdan-Lusztig polynomials with unequal parameters;
  * Inverse Kazhdan-Lusztig polynomials;
  * Cells and W-graphs;

%prep
%autosetup -p1

%build
%make_build cflags="-c %optflags"

%install
mkdir -p "%buildroot/%_bindir"
cp -a coxeter "%buildroot/%_bindir/"

%files
%_bindir/coxeter

%changelog
