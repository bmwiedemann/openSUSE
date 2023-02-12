#
# spec file for package blasphemer
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


Name:           blasphemer
Version:        0.1.8
Release:        0
Summary:        Replacement game files for Heretic game engines
License:        BSD-3-Clause
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/Blasphemer
Source:         https://github.com/Blasphemer/blasphemer/releases/download/v%{version}/blasphem-%{version}.zip
Source2:        https://github.com/Blasphemer/blasphemer/releases/download/v%{version}/blasphdm-%{version}.zip
BuildArch:      noarch
BuildRequires:  unzip

%description
Blasphemer aims to create a free content package for the Heretic engine,
with a theme of metal-inspired dark fantasy.

%prep
%setup -Tcq -a0 -a2

%build
# Game data files. Nothing to build!

%install
mkdir -p "%{buildroot}/%{_datadir}/doom"
cp -av *.wad "%{buildroot}/%{_datadir}/doom/"

%files
%{_datadir}/doom/

%changelog
