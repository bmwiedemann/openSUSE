#
# spec file for package gap-modulargroup
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gap-modulargroup
Version:        2.0.3
Release:        0
Summary:        GAP: Finite-index subgroups of (P)SL(2,Integers)
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://ag-weitze-schmithusen.github.io/ModularGroup/
#Git-Clone:     https://github.com/AG-Weitze-Schmithusen/ModularGroup
Source:         https://github.com/AG-Weitze-Schmithusen/ModularGroup/releases/download/v%version/ModularGroup-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-congruence >= 1.1.1
Requires:       gap-core >= 4.12
Requires:       gap-ctbllib >= 1.2.2

%description
This GAP package implements finite-index subgroups of (P)SL_2(ZZ) and
various algorithms for working with them. These subgroups are stored
as tuples of permutations s and t which describe the action of a
certain set of generator matrices on the right cosets.

%prep
%autosetup -n ModularGroup-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
