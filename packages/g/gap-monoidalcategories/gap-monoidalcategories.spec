#
# spec file for package gap-monoidalcategories
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


Name:           gap-monoidalcategories
Version:        2025.01.02
%define sillyver 2025.01-02
Release:        0
Summary:        GAP: Monoidal and monoidal (co-)closed categories
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/MonoidalCategories
Source:         https://github.com/homalg-project/CAP_project/releases/download/MonoidalCategories-%sillyver/MonoidalCategories-%sillyver.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-cap >= 2023.08.16
Requires:       gap-core >= 4.12.1
Requires:       gap-toolsforhomalg >= 2018.05.22

%description
Monoidal and monoidal (co-)closed categories for GAP.

%prep
%autosetup -n MonoidalCategories-%sillyver

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
