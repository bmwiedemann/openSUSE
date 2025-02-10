#
# spec file for package gap-lpres
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gap-lpres
Version:        1.1.1
Release:        0
Summary:        GAP: Nilpotent Quotients of L-Presented Groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/lpres
#Git-Clone:     https://github.com/gap-packages/lpres
Source:         https://github.com/gap-packages/lpres/releases/download/v%version/lpres-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.9
Requires:       gap-fga >= 1.1.0.1
Requires:       gap-polycyclic >= 2.5
Suggests:       gap-ace >= 5.0
Suggests:       gap-autpgrp >= 1.4
Suggests:       gap-pargap >= 1.1.2

%description
The LPRES package defines new GAP objects to work with L-presented
groups, namely groups given by a finite generating set and a
possibly-infinite set of relations given as iterates of finitely many
seed relations by a finite set of endomorphisms. The package
implements nilpotent quotient, Todd-Coxeter and Reidemeister-Schreier
algorithms for L-presented groups.

%prep
%autosetup -n lpres-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
