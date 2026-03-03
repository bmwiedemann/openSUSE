#
# spec file for package cockpit-packages
#
# Copyright (c) 2025 SUSE LLC
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

Name: cockpit-snapshots
Version: 3.1
Release: 0%{?dist}
Summary: Cockpit Snapshots module for interacting with Snapper snapshots
License: LGPL-2.1-or-later

Source0: %{name}-%{version}.tar.xz
Source10: package-lock.json
Source11: node_modules.spec.inc
patch10: load-css-overrides.patch

%include %_sourcedir/node_modules.spec.inc

BuildArch: noarch
%if ! 0%{?suse_version}
ExclusiveArch: %{nodejs_arches} noarch
%endif
%if ! 0%{?rhel} || 0%{?rhel} >= 10
BuildRequires: nodejs >= 18
%endif
BuildRequires: make
%if 0%{?suse_version}
# Suse's package has a different name
BuildRequires: appstream-glib
%else
BuildRequires: libappstream-glib
%endif
BuildRequires: gettext
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif
BuildRequires: local-npm-registry
BuildRequires: cockpit-devel >= 351

Requires: cockpit-bridge
Recommends: (sndiff if snapper)

Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.2
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(@patternfly/patternfly)) = 6.1.0
Provides: bundled(npm(@patternfly/react-core)) = 6.1.0
Provides: bundled(npm(@patternfly/react-core)) = 6.3.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.1.0
Provides: bundled(npm(@patternfly/react-icons)) = 6.3.1
Provides: bundled(npm(@patternfly/react-styles)) = 6.3.1
Provides: bundled(npm(@patternfly/react-table)) = 6.3.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.3.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.3.8
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.2.0
Provides: bundled(npm(tslib)) = 2.8.1

%description
Cockpit Snapshots module for interacting with Snapper snapshots

%prep
%setup -q -n %{name}-%{version}
%patch -P 10 -p1

rm -rf node_modules
rm -f package-lock.json
rm -rf pkg/lib
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts

# ignore pre-built bundle in release tarball and rebuild it
# but keep it in RHEL/CentOS-8/9, as that has a too old nodejs
%if ! 0%{?rhel} || 0%{?rhel} >= 10
rm -rf dist
%endif

%build
mkdir -p pkg
cp -r %{_datadir}/cockpit/devel/lib pkg/lib
NODE_ENV=production make
# Bug in how cockpit devel is built
sed -i 's/import glob from "glob"/import { glob } from "glob"/' pkg/lib/cockpit-po-plugin.js
NODE_ENV=production npm run build

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
%license LICENSE dist/index.js.LEGAL.txt
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
