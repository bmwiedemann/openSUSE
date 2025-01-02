#
# spec file for package gap-generalizedmorphismsforcap
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


Name:           gap-generalizedmorphismsforcap
Version:        2024.09.03
%define sillyver 2024.09-03
Release:        0
Summary:        GAP: Implementations of generalized morphisms for the CAP project
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/GeneralizedMorphismsForCAP
#Git-Clone:     https://github.com/homalg-project/CAP_project
Source:         https://github.com/homalg-project/CAP_project/releases/download/GeneralizedMorphismsForCAP-%sillyver/GeneralizedMorphismsForCAP-%sillyver.tar.gz
BuildRequires:  gap-devel >= 4.13.0
BuildRequires:  gap-rpm-devel
Requires:       gap-cap >= 2021.05.01
Requires:       gap-core >= 4.12.1
Requires:       gap-gapdoc >= 1.5
Requires:       gap-monoidalcategories >= 2024.01.03

%description
This package provides implementations of generalized morphisms for
the CAP module in GAP.

%prep
%autosetup -n GeneralizedMorphismsForCAP-%sillyver

%build
find . -type f -size 0 -name _Chunks.xml -print -delete
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
