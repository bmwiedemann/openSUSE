#
# spec file for package azove
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           azove
Version:        2.0
Release:        0
Summary:        Another Zero One Vertex Enumeration tool
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.mpi-inf.mpg.de/~behle/azove.html

# without a cookie, mpi-inf.mpg.de presents a landing page, failing the download check :(
#Source:         https://www.mpi-inf.mpg.de/~behle/%name-%version.tar.gz
Source:         %name-%version.tar.gz
Patch1:         azove-cpp.diff
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
azove is a tool designed for counting (without explicit enumeration)
and enumeration of 0/1 vertices.

Given a polytope by a linear relaxation or facet description P = {x |
Ax <= b}, all 0/1 points lying in P can be counted or enumerated.
This is done by intersecting the polytope P with the unit-hypercube
[0,1]^d. The integral vertices (no fractional ones) of this
intersection will be enumerated. If P is a 0/1 polytope, azove solves
the vertex enumeration problem. In fact, it can also solve the 0/1
knapsack problem and the 0/1 subset sum problem.

%prep
%autosetup -p1

%build
make %{?_smp_mflags} COMPILER_FLAGS="%optflags"

%install
c="%buildroot/%_bindir"
mkdir -p "$c"
install -pm0755 azove2 "$c"

%files
%_bindir/azove2
%license COPYING

%changelog
