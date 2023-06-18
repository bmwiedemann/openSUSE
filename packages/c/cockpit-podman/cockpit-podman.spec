#
# spec file for package cockpit-podman
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


Name:           cockpit-podman
Version:        70
Release:        0
Summary:        Cockpit component for Podman containers
License:        LGPL-2.1-or-later
URL:            https://github.com/cockpit-project/cockpit-podman
Source:         https://github.com/cockpit-project/cockpit-podman/archive/%{version}.tar.gz#/cockpit-podman-%{version}.tar.gz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
%include %_sourcedir/node_modules.spec.inc
Patch1:         1299.patch
Patch10:        load-css-overrides.patch
BuildArch:      noarch
BuildRequires:  appstream-glib
Requires:       cockpit-bridge >= 138
Requires:       cockpit-shell >= 138
Requires:       podman >= 2.0.4
#
BuildRequires:  cockpit-devel >= 293
BuildRequires:  local-npm-registry
BuildRequires:  sassc

%description
Cockpit component for managing Podman containers

%prep
%autosetup -p1
rm -r node_modules
local-npm-registry %{_sourcedir} install --with=dev

%build
export PREFIX=%{_prefix}
mkdir -p pkg/lib
cp -r %{_datadir}/cockpit/devel/lib/* pkg/lib

npm run build

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
