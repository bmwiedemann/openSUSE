#
# spec file for package gap-cubefree
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-cubefree
Version:        1.20
Release:        0
Summary:        GAP: Construction of groups of a given cubefree order
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/cubefree/
#Git-Clone:     https://github.com/gap-packages/cubefree

Source:         https://github.com/gap-packages/cubefree/releases/download/v%version/cubefree-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.8
Requires:       gap-grpconst >= 2.5
Requires:       gap-polycyclic >= 2.11

%description
The Cubefree package contains methods to construct up to isomorphism
the groups of a given (reasonable) cubefree order. The main function
ConstructAllCFGroups(n) constructs all groups of a given cubefree
order n. The function NumberCFGroups(n) counts all groups of a
cubefree order n. Furthermore, IrreducibleSubgroupsOfGL(2,q)
constructs the irreducible subgroups of GL(2,q), q=p^r, p>=5 prime,
up to conjugacy and RewriteAbsolutelyIrreducibleMatrixGroup(G)
rewrites the absolutely irreducible matrix group G (over a finite
field) over a minimal subfield.

%prep
%autosetup -n cubefree-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
