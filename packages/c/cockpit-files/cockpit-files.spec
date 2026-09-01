#
# spec file for package cockpit-file
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


Name:           cockpit-files
Version:        43
Release:        0
Summary:        Cockpit component for File Manager
License:        LGPL-2.1-or-later
URL:            https://github.com/cockpit-project/cockpit-files
Source:         https://github.com/cockpit-project/cockpit-files/releases/download/%{version}/cockpit-files-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       update_version.sh
Patch10:        load-css-overrides.patch
%include %_sourcedir/node_modules.spec.inc
BuildArch:      noarch
BuildRequires:  cockpit-devel >= 346
BuildRequires:  local-npm-registry
BuildRequires:  appstream-glib

%description
File manager as a cockipit component

%prep
%autosetup -p1 -n "%name"
rm -f package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts
echo "{}" > package-lock.json

%build
export PREFIX=%{_prefix}
mkdir -p pkg/lib
cp -r %{_datadir}/cockpit/devel/lib/* pkg/lib

NODE_ENV=production npm run build

%install
export PREFIX=%{_prefix}
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
