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
Version:        0.0.3~git28.b446f50
Release:        0%{?dist}
Summary:        Cockpit module for Transactional Update
License:        LGPL-2.1-or-later

URL:            https://github.com/openSUSE/cockpit-tukit
Source:         %{name}-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
%include %_sourcedir/node_modules.spec.inc
Patch0:         load-css-overrides.patch
BuildArch:      noarch
BuildRequires:  appstream-glib
BuildRequires:  cockpit-devel >= 251
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
%setup -q -n %{name}-%{version}
%patch0 -p1
rm -f package-lock.json
local-npm-registry %{_sourcedir} install --with=dev --legacy-peer-deps || ( find ~/.npm/_logs -name '*-debug.log' -print0 | xargs -0 cat; false)

%build
cp -r %{_datadir}/cockpit/devel/lib src/lib
NODE_ENV=production npm run build

%install
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%files
%doc README.md
%license LICENSE dist/index.js.LICENSE.txt.gz
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
