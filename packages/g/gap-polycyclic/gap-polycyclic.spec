#
# spec file for package gap-polycyclic
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-polycyclic
Version:        2.16
Release:        0
Summary:        GAP: Computation with polycyclic groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/polycyclic/
#Git-Clone:     https://github.com/gap-packages/polycyclic
Source:         https://github.com/gap-packages/polycyclic/releases/download/v%version/polycyclic-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-alnuth >= 3.0
Requires:       gap-autpgrp >= 1.6
Requires:       gap-core >= 4.9

%description
The Polycyclic package provides a basis for working with polycyclic
groups defined by polycyclic presentations.

The features of this package include
        
* creating a polycyclic group from a polycyclic presentation
* arithmetic in a polycyclic group
* computation with subgroups and factor groups of a polycyclic group
* computation of standard subgroup series such as the derived series,
  the lower central series
* computation of the first and second cohomology
* computation of group extensions
* computation of normalizers and centralizers
* solutions to the conjugacy problems for elements and subgroups
* computation of Torsion and various finite subgroups
* computation of various subgroups of finite index
* computation of teh Schur multiplicator, the non-abelian exterior
  square and the non-abelian tenor square

%prep
%autosetup -n polycyclic-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
