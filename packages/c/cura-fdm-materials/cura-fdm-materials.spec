#
# spec file for package cura-fdm-materials
#
# Copyright (c) 2022 SUSE LLC
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


Name:           cura-fdm-materials
Version:        4.13.0
Release:        0
Summary:        FDM material database
License:        CC0-1.0
Group:          Hardware/Printing
URL:            https://github.com/Ultimaker/fdm_materials
Source0:        fdm_materials-%{version}.tar.xz
BuildRequires:  xz
BuildArch:      noarch

%description
FDM material database for use with Cura

%prep
%setup -q -n fdm_materials-%version

%build

%install
mkdir -p %{buildroot}%{_datadir}/cura/resources/materials/
install -m 0644 -t %{buildroot}%{_datadir}/cura/resources/materials/ *.fdm_material

%files
%license LICENSE
%dir %{_datadir}/cura
%dir %{_datadir}/cura/resources
%{_datadir}/cura/resources/materials

%changelog
