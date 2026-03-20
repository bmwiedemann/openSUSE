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
Version: 16
Release: 1%{?dist}
Summary: Cockpit module for managing and registering subscriptions
License: LGPL-2.1-or-later

Source0:        ./cockpit-subscriptions-%{version}.tar.xz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       update_version.sh
%include %_sourcedir/node_modules.spec.inc
Patch10:        load-css-overrides.patch
Patch11:        esbuild-ppc64.patch

BuildArch: noarch
BuildRequires: local-npm-registry
BuildRequires: nodejs >= 18
BuildRequires: make
BuildRequires: appstream-glib
BuildRequires: gettext

Requires: cockpit-bridge
Requires: suseconnect-ng

Provides: bundled(npm(@bufbuild/protobuf)) = 2.11.0
Provides: bundled(npm(@esbuild/aix-ppc64)) = 0.27.3
Provides: bundled(npm(@esbuild/android-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/android-arm)) = 0.27.3
Provides: bundled(npm(@esbuild/android-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/darwin-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/darwin-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/freebsd-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/freebsd-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-arm)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-ia32)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-loong64)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-mips64el)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-ppc64)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-riscv64)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-s390x)) = 0.27.3
Provides: bundled(npm(@esbuild/linux-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/netbsd-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/netbsd-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/openbsd-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/openbsd-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/openharmony-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/sunos-x64)) = 0.27.3
Provides: bundled(npm(@esbuild/win32-arm64)) = 0.27.3
Provides: bundled(npm(@esbuild/win32-ia32)) = 0.27.3
Provides: bundled(npm(@esbuild/win32-x64)) = 0.27.3
Provides: bundled(npm(@parcel/watcher-android-arm64)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-darwin-arm64)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-darwin-x64)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-freebsd-x64)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-linux-arm-glibc)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-linux-arm-musl)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-linux-arm64-glibc)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-linux-arm64-musl)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-linux-x64-glibc)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-linux-x64-musl)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-win32-arm64)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-win32-ia32)) = 2.5.6
Provides: bundled(npm(@parcel/watcher-win32-x64)) = 2.5.6
Provides: bundled(npm(@parcel/watcher)) = 2.5.6
Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(argparse)) = 2.0.1
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(chokidar)) = 4.0.3
Provides: bundled(npm(colorjs.io)) = 0.5.2
Provides: bundled(npm(content-type)) = 1.0.5
Provides: bundled(npm(detect-libc)) = 2.1.2
Provides: bundled(npm(encoding)) = 0.1.13
Provides: bundled(npm(esbuild-sass-plugin)) = 3.7.0
Provides: bundled(npm(esbuild)) = 0.27.3
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(gettext-parser)) = 9.0.1
Provides: bundled(npm(has-flag)) = 4.0.0
Provides: bundled(npm(hasown)) = 2.0.2
Provides: bundled(npm(iconv-lite)) = 0.6.3
Provides: bundled(npm(immutable)) = 5.1.5
Provides: bundled(npm(is-core-module)) = 2.16.1
Provides: bundled(npm(is-extglob)) = 2.1.1
Provides: bundled(npm(is-glob)) = 4.0.3
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(node-addon-api)) = 7.1.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(picomatch)) = 4.0.3
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.4.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(readdirp)) = 4.1.2
Provides: bundled(npm(resolve)) = 1.22.11
Provides: bundled(npm(rxjs)) = 7.8.2
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sass-embedded-all-unknown)) = 1.97.3
Provides: bundled(npm(sass-embedded-android-arm64)) = 1.97.3
Provides: bundled(npm(sass-embedded-android-arm)) = 1.97.3
Provides: bundled(npm(sass-embedded-android-riscv64)) = 1.97.3
Provides: bundled(npm(sass-embedded-android-x64)) = 1.97.3
Provides: bundled(npm(sass-embedded-darwin-arm64)) = 1.97.3
Provides: bundled(npm(sass-embedded-darwin-x64)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-arm64)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-arm)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-musl-arm64)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-musl-arm)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-musl-riscv64)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-musl-x64)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-riscv64)) = 1.97.3
Provides: bundled(npm(sass-embedded-linux-x64)) = 1.97.3
Provides: bundled(npm(sass-embedded-unknown-all)) = 1.97.3
Provides: bundled(npm(sass-embedded-win32-arm64)) = 1.97.3
Provides: bundled(npm(sass-embedded-win32-x64)) = 1.97.3
Provides: bundled(npm(sass-embedded)) = 1.97.3
Provides: bundled(npm(sass)) = 1.97.3
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(source-map-js)) = 1.2.1
Provides: bundled(npm(supports-color)) = 8.1.1
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(sync-child-process)) = 1.0.2
Provides: bundled(npm(sync-message-port)) = 1.2.0
Provides: bundled(npm(tabbable)) = 6.4.0
Provides: bundled(npm(tslib)) = 2.8.1
Provides: bundled(npm(varint)) = 6.0.0

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
