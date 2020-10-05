#
# spec file for package kicad-packages3D
#
# Copyright (c) 2020 SUSE LLC
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


# 5.0.x are bugfix versions, do not require users to upgrade symbols/footprints/packages
%define compatversion 5.0.0

Name:           kicad-packages3D
Version:        5.1.7
Release:        0
Summary:        3D model libraries for rendering and MCAD integration
# License is CC-BY-SA-4.0 but there is an exception
# See included LICENSE.md and kicad-pcb.org/libraries/license/
License:        CC-BY-SA-4.0
Group:          Productivity/Scientific/Electronics
URL:            https://kicad-pcb.org
Source:         https://github.com/KiCad/kicad-packages3D/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       kicad-footprints = %{version}
Provides:       kicad-library-3d = %{version}
Provides:       kicad-packages3D = %{compatversion}
Obsoletes:      kicad-library-3d < 5.0.0
Suggests:       FreeCAD

%description
KiCad is a software suite used for Electronic Design Automation (EDA).

This package contains 3D models associated with the various KiCad footprint
library components for rendering and mechanical CAD (MCAD) integration.

%prep
%setup -q

%build
%cmake \
    -DKICAD_DATA:PATH=%{_datadir}/kicad
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/kicad/modules/

%files
%doc README.md CREDITS.md
%license LICENSE.md
%dir %{_datadir}/kicad/
%dir %{_datadir}/kicad/modules/
%dir %{_datadir}/kicad/modules/packages3d
%dir %{_datadir}/kicad/modules/packages3d/*
%{_datadir}/kicad/modules/packages3d/*/*.step
%{_datadir}/kicad/modules/packages3d/*/*.wrl

%changelog
