#
# spec file for package gap-rcwa
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


Name:           gap-rcwa
Version:        4.7.1
Release:        0
Summary:        GAP: Residue-Class-Wise Affine Groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/rcwa/
#Git-Clone:     https://github.com/gap-packages/rcwa
Source:         https://github.com/gap-packages/rcwa/releases/download/v%version/rcwa-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9.1
Requires:       gap-fr >= 2.2.1
Requires:       gap-gapdoc >= 1.5.1
Requires:       gap-grape >= 4.7
Requires:       gap-polycyclic >= 2.11
Requires:       gap-resclasses >= 4.7.2
Requires:       gap-utils >= 0.40

%description
This package for GAP 4 introduces a new class of groups which are
accessible to computational methods. In principle, it can deal at
least with the follo- wing types of groups:

* Finite groups.
* Free groups of finite rank.
* Free products of finitely many finite groups, thus in particular
  the modular group PSL(2,Z).
* Direct products of such groups.
* Wreath products of such groups with finite groups and with (Z,+).

Among these groups there are finitely generated groups which are not
finitely presented, and such with unsolvable membership problem.
Further, any finite group embeds into some divisible torsion group
which RCWA can deal with.

%prep
%autosetup -n rcwa-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
