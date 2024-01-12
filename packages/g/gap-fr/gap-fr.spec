#
# spec file for package gap-fr
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


Name:           gap-fr
Version:        2.4.13
Release:        0
Summary:        GAP: Computations with functionally recursive groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/fr/
#Git-Clone:     https://github.com/gap-packages/fr
Source:         https://github.com/gap-packages/fr/releases/download/v%version/fr-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-fga >= 1.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-io >= 4.0
Requires:       gap-polycyclic >= 2.2
Suggests:       gap-gbnp >= 0.9
Suggests:       gap-nq >= 2.4
Suggests:       gap-lpres >= 0.1

%description
This package implements Functionally Recursive and Mealy automata in
GAP. These objects can be manipulated as group elements, and various
specific commands allow their manipulation as automorphisms of
infinite rooted trees. Permutation quotients can also be created and
manipulated as standard GAP groups or semigroups.

%prep
%autosetup -n fr-%version

%build

%install
rm -Rf cnf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
