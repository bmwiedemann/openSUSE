#
# spec file for package kicad-templates
#
# Copyright (c) 2019 SUSE LLC.
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

Name:           kicad-templates
Version:        5.1.5
Release:        0
Summary:        Project templates for KiCad
# License is CC-BY-SA-4.0 but there is an exception
# See included LICENSE.md and kicad-pcb.org/libraries/license/
License:        CC-BY-SA-4.0
Group:          Productivity/Scientific/Electronics
URL:            http://kicad-pcb.org
Source:         https://github.com/KiCad/kicad-templates/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildArch:      noarch
Provides:       kicad-templates = %{compatversion}

%description
KiCad is a software suite used for Electronic Design Automation (EDA).

This is the project templates package for KiCad.

%prep
%setup -q

%build
%cmake \
    -DKICAD_DATA:PATH=%{_datadir}/kicad
%make_jobs

%install
%cmake_install
%fdupes -s %{buildroot}/%{_datadir}/kicad/template/

%files
%{_datadir}/kicad/
%license LICENSE.md

%changelog
