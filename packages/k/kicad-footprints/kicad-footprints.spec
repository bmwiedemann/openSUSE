#
# spec file for package kicad-footprints
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


# 8.0.x are bugfix versions, do not require users to upgrade symbols/footprints/packages
%define compatversion 8.0.0

Name:           kicad-footprints
Version:        8.0.3
%define file_version 8.0.3
Release:        0
Summary:        Footprint library for KiCad
# License is CC-BY-SA-4.0 but there is an exception
# See included LICENSE.md and kicad.org/libraries/license/
License:        CC-BY-SA-4.0
Group:          Productivity/Scientific/Electronics
URL:            https://www.kicad.org
Source:         https://gitlab.com/kicad/libraries/kicad-footprints/-/archive/%{file_version}/kicad-footprints-%{file_version}.tar.bz2#/%{name}-%{version}.tar.bz2
BuildRequires:  cmake >= 3.10
BuildRequires:  fdupes
BuildArch:      noarch
Provides:       kicad-footprints = %{compatversion}
# kicad library has been removed, fp-lib-table was moved
Conflicts:      kicad-library <= 4.0.7
Provides:       kicad-library:%{_datadir}/kicad/template/fp-lib-table

%description
KiCad is a software suite used for Electronic Design Automation (EDA).

This is the footprints library package for KiCad.

%prep
%setup -q -n %{name}-%{file_version}

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_datadir}/kicad/modules/

%files
%doc README.md CONTRIBUTING.md
%license LICENSE.md
%{_datadir}/kicad/

%changelog
