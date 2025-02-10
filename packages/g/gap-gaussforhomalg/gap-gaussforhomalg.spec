#
# spec file for package gap-gaussforhomalg
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


Name:           gap-gaussforhomalg
Version:        2024.08.01
%define sillyver 2024.08-01
Release:        0
Summary:        GAP: Gauss Functionality for homalg
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/GaussForHomalg
#Git-Clone:	https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/GaussForHomalg-%sillyver/GaussForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-gauss >= 2021.04.01
Requires:       gap-matricesforhomalg >= 2023.10.01
Requires:       gap-toolsforhomalg >= 2023.11.01

%description
The GaussForHomalg package links the homalg package together with the
Gauss package.

%prep
%autosetup -n GaussForHomalg-%sillyver

%build
rm -v doc/clean doc/.gitignore

%install
%gappkg_simple_install

%files -f %name.files

%changelog
