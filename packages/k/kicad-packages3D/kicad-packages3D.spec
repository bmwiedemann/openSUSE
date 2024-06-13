#
# spec file for package kicad-packages3D
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

# LZMA compression is too slow and causes frequent build failures
# due to timeouts
%define _binary_payload w5T.xzdio

Name:           kicad-packages3D
Version:        8.0.3
Release:        0
Summary:        3D model libraries for rendering and MCAD integration
# License is CC-BY-SA-4.0 but there is an exception
# See included LICENSE.md and kicad.org/libraries/license/
License:        CC-BY-SA-4.0
Group:          Productivity/Scientific/Electronics
URL:            https://www.kicad.org
Source:         https://gitlab.com/kicad/libraries/kicad-packages3D/-/archive/%{version}/kicad-packages3D-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
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
%fdupes %{buildroot}%{_datadir}/kicad/3dmodels/

%files
%doc README.md CREDITS.md
%license LICENSE.md
%dir %{_datadir}/kicad/
%dir %{_datadir}/kicad/3dmodels
%dir %{_datadir}/kicad/3dmodels/*
%{_datadir}/kicad/3dmodels/*/*.step
%{_datadir}/kicad/3dmodels/*/*.wrl

%changelog
