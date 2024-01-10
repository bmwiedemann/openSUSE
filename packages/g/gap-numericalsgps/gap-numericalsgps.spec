#
# spec file for package gap-numericalsgps
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


Name:           gap-numericalsgps
Version:        1.3.1
Release:        0
Summary:        GAP: A package for numerical semigroups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/numericalsgps

#Git-Clone:     https://github.com/gap-packages/numericalsgps
Source:         https://github.com/gap-packages/numericalsgps/releases/download/v%version/NumericalSgps-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7

%description
The features of this package include

* Defining numerical semigroups;

* Computing several properties of numerical semigroups, namely:
  multiplicity, Frobenius number, (minimal) system of generators,
  Apéry set, gaps, fundamental gaps, etc.;

* Performing several operations on numerical semigroups, namely:
  intersection, quotient by an integer, decompose into
  irreducible semigroups, add a special gap;

%prep
%setup -qn NumericalSgps-%version

%build
find . -type f -name "*~" -delete

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
