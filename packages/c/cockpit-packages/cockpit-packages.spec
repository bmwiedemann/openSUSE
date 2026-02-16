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

Name: cockpit-packages
Version: 4.1
Release: 0%{?dist}
Summary: A cockpit module for (un)installing packages
License: LGPL-2.1-or-later

Source:         %{name}-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Patch10:        load-css-overrides.patch
Patch11:        esbuild-ppc64.patch
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
BuildRequires: cockpit-devel >= 337

Requires: cockpit-bridge
Requires: PackageKit

%description
A cockpit module for (un)installing packages

%prep
%setup -q -n %{name}-%{version}
%patch -P 10 -p1
%patch -P 11 -p1
rm -rf node_modules
rm -f package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts

%build
mkdir -p pkg
cp -r %{_datadir}/cockpit/devel/lib pkg/lib
# Bug in how cockpit devel is built
sed -i 's/import glob from "glob"/import { glob } from "glob"/' pkg/lib/cockpit-po-plugin.js
NODE_ENV=production npm run build

%install
PREFIX=/usr DESTDIR=%{buildroot} make install

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
