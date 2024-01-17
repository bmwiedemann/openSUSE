#
# spec file for package gap-alnuth
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gap-alnuth
Version:        3.2.1
Release:        0
Summary:        GAP: Algebraic number theory and an interface to KANT
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/alnuth/
#Git-Clone:     https://github.com/gap-packages/alnuth
Source:         https://github.com/gap-packages/alnuth/releases/download/v%version/alnuth-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-polycyclic >= 1.1
Requires:       pari-gp >= 2.5

%description
The Alnuth package provides various methods to compute with number
fields which are given by a defining polynomial or by generators. The
main methods included in Alnuth are: creating a number field,
computing its maximal order, computing its unit group and a
presentation of this unit group, computing the elements of a given
norm of the number field, determining a presentation for a finitely
generated multiplicative subgroup, and factoring polynomials defined
over number fields.

%prep
%autosetup -n alnuth-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
