#
# spec file for package gap-toricvarieties
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


Name:           gap-toricvarieties
Version:        2022.07.13
%define sillyver 2022-07-13
Release:        0
Summary:        GAP: A package to handle toric varieties
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/ToricVarieties_project/ToricVarieties
Source:         https://github.com/homalg-project/ToricVarieties_project/releases/download/%sillyver/ToricVarieties-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-autodoc >= 2016.02.16
Requires:       gap-core >= 4.7
Requires:       gap-gradedmodules >= 2015.12.04
Requires:       gap-gradedringforhomalg >= 2020.04.25
Requires:       gap-modules >= 2016.01.20
Requires:       gap-nconvex >= 2020.11.04
Requires:       gap-toolsforhomalg >= 2016.02.17
Suggests:       gap-4ti2interface >= 2020.04.25
Suggests:       gap-convex >= 2021.04.24
Suggests:       gap-topcominterface >= 2019.06.016

%description
ToricVarieties provides data structures to handle toric varieties by
their commutative algebra structure and by their combinatorics. For
combinatorics, it uses the Convex package. Its goal is to provide a
suitable framework to work with toric varieties.

%prep
%autosetup -n ToricVarieties

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
