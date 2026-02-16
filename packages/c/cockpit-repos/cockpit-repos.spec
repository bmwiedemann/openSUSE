#
# spec file for package cockpit-repos
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

Name: cockpit-repos
Version: 4.7
Release: 0%{?dist}
Summary: A Cockpit module for managing system repositories
URL: https://github.com/openSUSE/cockpit-repos
License: LGPL-2.1-or-later

Source0: %{name}-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
%include %_sourcedir/node_modules.spec.inc
Patch10:        load-css-overrides.patch
Patch11:        esbuild-ppc64.patch

BuildArch: noarch
%if ! 0%{?suse_version}
ExclusiveArch: %{nodejs_arches} noarch
%endif
%if ! 0%{?rhel} || 0%{?rhel} >= 10
BuildRequires: nodejs >= 18
%endif
BuildRequires: make
BuildRequires: cockpit-devel >= 337
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

Requires: cockpit-bridge

Provides: bundled(npm(@patternfly/patternfly)) = 5.4.2
Provides: bundled(npm(@patternfly/react-core)) = 5.4.12
Provides: bundled(npm(@patternfly/react-core)) = 6.1.0
Provides: bundled(npm(@patternfly/react-icons)) = 5.4.2
Provides: bundled(npm(@patternfly/react-icons)) = 6.1.0
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-styles)) = 6.1.0
Provides: bundled(npm(@patternfly/react-table)) = 6.1.0
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.1.0
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.3.8
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.2.0
Provides: bundled(npm(tslib)) = 2.8.1

%description
A Cockpit module for managing system repositories

%prep
%autosetup -p1
rm -f package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts

%build
mkdir -p pkg
cp -r %{_datadir}/cockpit/devel/lib pkg/lib
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
