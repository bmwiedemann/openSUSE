#
# spec file for package gap-matricesforhomalg
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


Name:           gap-matricesforhomalg
Version:        2024.11.02
%define sillyver 2024.11-02
Release:        0
Summary:        GAP: Matrices for the homalg project
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/MatricesForHomalg
#Git-Clone:     https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/MatricesForHomalg-%sillyver/MatricesForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-toolsforhomalg >= 2023.11.01

%description
The MatricesForHomalg package provides lazy evaluated matrices with
clever operations for the homalg project.

%prep
%autosetup -n MatricesForHomalg-%sillyver

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
