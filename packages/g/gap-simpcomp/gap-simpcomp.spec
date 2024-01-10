#
# spec file for package gap-simpcomp
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


Name:           gap-simpcomp
Version:        2.1.14
Release:        0
Summary:        GAP toolbox for simplicial complexes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://simpcomp-team.github.io/simpcomp/
#Git-Clone:     https://github.com/simpcomp-team/simpcomp
Source:         https://github.com/simpcomp-team/simpcomp/releases/download/v%version/simpcomp-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.5
Requires:       gap-gapdoc >= 0.9999
Requires:       gap-io >= 3.0
Suggests:       gap-homology >= 1.4.4
Suggests:       gap-grape >= 4.4
Suggests:       gap-gauss >= 2011.08.22
Suggests:       gap-matricesforhomalg >= 2011.10.08
Suggests:       gap-homalg >= 2011.10.05
Suggests:       gap-gaussforhomalg >= 2011.08.10
Suggests:       gap-modules >= 2011.10.05

%description
simpcomp is a GAP package for working with simplicial complexes. It
allows the computation of many properties of simplicial complexes
(such as the f-, g- and h-vecors, the face lattice, the automorphism
group, (co-)homology with explicit basis computation, intersection
form, etc.) and provides the user with functions to compute new
complexes from old (simplex links and stars, connected sums,
cartesian products, handle additions, bistellar flips, etc.).

Furthermore, it comes with an extensive library of known
triangulations of manifolds and provides the user with the
possibility to create own complex libraries. simpcomp caches computed
properties of a simplicial complex, thus avoiding unnecessary
computations, internally handles the vertex labeling of the complexes
and insures the consistency of a simplicial complex throughout all
operations.

%prep
%autosetup -n simpcomp-%version

%build
./configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir"
rm -Rf install-sh configure depcomp missing config.log
popd

%files -f %name.files

%changelog
