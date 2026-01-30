#
# spec file for package cockpit-subscriptions
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

Name: cockpit-subscriptions
Version: 14.4
Release: 1%{?dist}
Summary: Cockpit module for managing and registering subscriptions
License: LGPL-2.1-or-later

Source0:        ./cockpit-subscriptions-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       update_version.sh
%include %_sourcedir/node_modules.spec.inc
Patch10:        load-css-overrides.patch

BuildArch: noarch
BuildRequires: local-npm-registry
BuildRequires: nodejs >= 18
BuildRequires: make
BuildRequires: appstream-glib
BuildRequires: gettext

Requires: cockpit-bridge
Requires: suseconnect-ng

Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.3.8
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.4.0
Provides: bundled(npm(tslib)) = 2.8.1

%description
A Cockpit module for managing and registering subscriptions

%prep
%autosetup -p1
rm -f package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts

%build
NODE_ENV=production make

%install
%make_install PREFIX=/usr

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

# this can't be meaningfully tested during package build; tests happen through
# FMF (see plans/all.fmf) during package gating

%files
%doc README.md
%license LICENSE
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
