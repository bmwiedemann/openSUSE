#
# spec file for package gap-laguna
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-laguna
Version:        3.9.7
Release:        0
Summary:        GAP: Lie AlGebras and UNits of group Algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/laguna/
#Git-Clone:     https://github.com/gap-packages/laguna
Source:         https://github.com/gap-packages/laguna/releases/download/v%version/laguna-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.6.1
Suggests:       gap-sophus >= 1.24

%description
LAGUNA extends GAP functionality for computations in group rings.
Besides computing some general properties and attributes of group
rings and their elements, LAGUNA is able to perform two main kinds of
computations. Namely, it can verify whether a group algebra of a
finite group satisfies certain Lie properties; and it can calculate
the structure of the normalized unit group of a group algebra of a
finite p-group over the field of p elements.

%prep
%autosetup -n laguna-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
