#
# spec file for package gap-grpconst
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-grpconst
Version:        2.6.4
Release:        0
Summary:        GAP: Group construction of a given order
License:        GPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/grpconst/
#Git-Clone:     https://github.com/gap-packages/grpconst
Source:         https://github.com/gap-packages/grpconst/releases/download/v%version/grpconst-%version.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7
Requires:       gap-autpgrp >= 1.6
Requires:       gap-irredsol >= 1.2
Requires:       gap-smallgrp >= 1.4

%description
The GrpConst package contains methods to construct up to isomorphism
the groups of a given order. The FrattiniExtensionMethod constructs
all soluble groups of a given order. On request it gives only those
that are (or are not) nilpotent or supersolvable or that do (or do
not) have normal Sylow subgroups for some given set of primes. The
CyclicSplitExtensionMethod constructs all groups having a normal
Sylow subgroup for orders of the type p^n *q. The method relies on
the availability of a list of all groups of order p^n. The
UpwardsExtensions algorithm takes as input a permutation group G and
a positive integer s and returns a list of permutation groups, one
for each extension of G by a soluble group of order a divisor of s.
This method can used to construct the non-solvable groups of a given
order by taking the perfect groups of certain orders as input for G.
The programs in this package have been used to construct a large part
of the Small Groups library.

%prep
%autosetup -n grpconst-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
