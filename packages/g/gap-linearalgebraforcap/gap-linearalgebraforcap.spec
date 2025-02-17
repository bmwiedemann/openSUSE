#
# spec file for package gap-linearalgebraforcap
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


Name:           gap-linearalgebraforcap
Version:        2024.10.01
%define sillyver 2024.10-01
Release:        0
Summary:        GAP: Category of Matrices over a Field for CAP
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/LinearAlgebraForCAP
#Git-Clone:     https://github.com/homalg-project/CAP_project
Source:         https://github.com/homalg-project/CAP_project/releases/download/LinearAlgebraForCAP-%sillyver/LinearAlgebraForCAP-%sillyver.tar.gz
BuildRequires:  gap-devel >= 4.12.1
BuildRequires:  gap-rpm-devel
Requires:       gap-cap >= 2023.10.07
Requires:       gap-core >= 4.13.0
Requires:       gap-gapdoc >= 1.5
Requires:       gap-gaussforhomalg >= 2021.04.02
Requires:       gap-matricesforhomalg >= 2023.01.01
Requires:       gap-monoidalcategories >= 2024.09.02
Requires:       gap-toolsforhomalg >= 2015.09.18
Suggests:       gap-freydcategoriesforcap >= 2024.01.04

%description
This package adds support for categories of matrices over a field
for CAP.

%prep
%autosetup -n LinearAlgebraForCAP-%sillyver

%build
find . -type f -size 0 -name _Chunks.xml -delete
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
