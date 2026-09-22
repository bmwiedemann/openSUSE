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
Version:        44
Release:        0
Summary:        Cockpit component for File Manager
License:        LGPL-2.1-or-later
URL:            https://github.com/cockpit-project/cockpit-files
Source:         https://github.com/cockpit-project/cockpit-files/releases/download/%{version}/cockpit-files-%{version}.tar.xz
Source10:       package-lock.json
#!CreateArchive
Source11:       node_modules
Source12:       update_version.sh
# CVE-2026-91202, CVE-2026-91203, CVE-2026-91205
Patch1:         prevent-filename-directory-names-misinterpreation.patch
Patch2:         never-derefernce-a-symlink.patch
Patch3:         premissions-spell-out-commandline-options.patch
Patch4:         apply-no-derefernce-to-chmod.patch 
Patch10:        load-css-overrides.patch
BuildArch:      noarch
BuildRequires:  cockpit-devel >= 346
BuildRequires:  local-npm-registry
BuildRequires:  appstream-glib

%description
File manager as a cockipit component

%prep
%autosetup -p1 -n "%name"
rm -f package-lock.json
local-npm-registry %{_sourcedir}/node_modules install --include=dev --ignore-scripts
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
