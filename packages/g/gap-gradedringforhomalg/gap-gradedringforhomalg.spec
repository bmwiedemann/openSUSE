#
# spec file for package gap-gradedringforhomalg
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


Name:           gap-gradedringforhomalg
Version:        2024.07.01
%define sillyver 2024.07-01
Release:        0
Summary:        GAP: Endow Commutative Rings with an Abelian Grading
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/GradedRingForHomalg
#Git-Clone:     https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/GradedRingForHomalg-%sillyver/GradedRingForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-homalg >= 2011.08.16
Requires:       gap-homalgtocas >= 2023.08.01
Requires:       gap-matricesforhomalg >= 2023.08.01
Requires:       gap-modules >= 2023.08.01
Requires:       gap-ringsforhomalg >= 2023.08.01
Suggests:       gap-4ti2interface >= 2019.09.03
Suggests:       gap-nconvex >= 2020.03.02

%description
This package is part of the homalg-project and manages graded rings.

%prep
%autosetup -n GradedRingForHomalg-%sillyver

%build
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
