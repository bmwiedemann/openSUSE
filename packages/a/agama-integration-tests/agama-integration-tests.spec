#
# spec file for package agama-integration-tests
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


Name:           agama-integration-tests
Version:        0
Release:        0
Summary:        Example Agama integration tests
License:        GPL-2.0-or-later
URL:            https://github.com/agama-project/agama-integration-tests
# source_validator insists that if obscpio has no version then
# tarball must neither
Source0:        agama-integration-tests.tar
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
%include %_sourcedir/node_modules.spec.inc
BuildArch:      noarch
BuildRequires:  local-npm-registry
BuildRequires:  nodejs-devel
Requires:       nodejs(engine) >= 18

%description
This package provides only few example integration tests, the real tests should be added from
outside.

All needed NPM dependencies are bundled into the tests themselves, there are no external
dependencies.

%prep
%autosetup -p1 -n agama-integration-tests

%build
rm -f package-lock.json

# The --ignore-scripts option disables all NPM preinstall/postinstall scripts. It skips possible
# rebuilds of the binary plugins in the dependent "bufferutil" and "utf-8-validate" NPM packages.
# For some reason the rebuilds fail in OBS. But Webpack does not use the binaries in the final
# bundle anyway (and the code falls back to a native JavaScript implementation) so we can disable
# the rebuild scripts and then the package builds fine in OBS.
local-npm-registry %{_sourcedir} install --ignore-scripts --with=dev || ( find ~/.npm/_logs -name '*-debug.log' -print0 | xargs -0 cat; false)

ESLINT=0 npm run build

%install
install -D -d -m 0755 %{buildroot}%{_datadir}/agama/integration-tests
cp -aR %{_builddir}/agama-integration-tests/dist/* %{buildroot}%{_datadir}/agama/integration-tests

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_datadir}/agama
%{_datadir}/agama/integration-tests

%changelog
