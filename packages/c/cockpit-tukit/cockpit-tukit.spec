#
# spec file for package cockpit-tukit
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

Name:           cockpit-tukit
Version:        0.1.7~git0.61e54f1
Release:        0%{?dist}
Summary:        Cockpit module for Transactional Update
License:        LGPL-2.1-or-later

URL:            https://github.com/openSUSE/cockpit-tukit
Source:         %{name}-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
%include %_sourcedir/node_modules.spec.inc
Patch2:         load-css-overrides.patch
BuildArch:      noarch
BuildRequires:  appstream-glib
BuildRequires:  cockpit-devel >= 293
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  npm

Requires:       cockpit-system
Requires:       tukitd

%define debug_package %{nil}

%description
Cockpit module for Transactional Update

%prep
%autosetup -p1 -n %{name}-%{version}

rm -f package-lock.json
rm -rf node_modules
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts|| ( find ~/.npm/_logs -name '*-debug.log' -print0 | xargs -0 cat; false)
touch package-lock.json

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
%license LICENSE dist/index.js.LEGAL.txt
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
