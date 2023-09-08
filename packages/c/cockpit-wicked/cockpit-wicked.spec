#
# spec file for package cockpit-wicked
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


Name:           cockpit-wicked
Version:        5~git0.82629da
Release:        0
Summary:        Cockpit user interface for Wicked
License:        GPL-2.0-only
URL:            https://github.com/openSUSE/cockpit-wicked
Source:         %{name}-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
%include %_sourcedir/node_modules.spec.inc
BuildArch:      noarch
BuildRequires:  appstream-glib
BuildRequires:  appstream-glib
BuildRequires:  cockpit-devel >= 293
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  npm

Requires:       cockpit-bridge
Requires:       wicked

BuildRequires:  nodejs-devel
BuildRequires:  npm

Conflicts:      cockpit-networkmanager

%description
Cockpit component for managing network configuration through Wicked

%prep
%setup -q -n %{name}-%{version}
rm -f package-lock.json
rm -rf node_modules
local-npm-registry %{_sourcedir} install --with=dev || ( find ~/.npm/_logs -name '*-debug.log' -print0 | xargs -0 cat; false)

%build
mkdir -p pkg
cp -r %{_datadir}/cockpit/devel/lib pkg/lib
NODE_ENV=production npm run build

%install
PREFIX=/usr DESTDIR=%{buildroot} make install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%files
%doc README.md
%license LICENSE
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
