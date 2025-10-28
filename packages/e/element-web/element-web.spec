#
# spec file for package element-web
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           element-web
Version:        1.12.2
Release:        0
Summary:        A glossy Matrix collaboration client - web files
License:        AGPL-3.0-only OR GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://github.com/vector-im/element-web
Source0:        https://github.com/vector-im/element-web/archive/v%{version}.tar.gz#/element-web-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        jitsi_external_api.min.js
Source3:        prepare.sh
Source4:        README.md
Patch0:         fix-webpack-oom.patch
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  nodejs-packaging
BuildRequires:  rust
BuildRequires:  yarn
BuildRequires:  zstd
BuildArch:      noarch

%description
A glossy Matrix collaboration client - web files

%prep
%autosetup -n element-web-%{version} -a1 -p1

%build
export SENTRYCLI_SKIP_DOWNLOAD=1

yarn build

mkdir -p webapp
cp %{SOURCE2} ./webapp/jitsi_external_api.min.js
echo > scripts/build-jitsi.ts

DIST_VERSION=%{version} ./scripts/package.sh

pushd dist || exit 1
tar xf element-%{version}.tar.gz
popd
cp -v LICENSE* dist/element-%{version}/

%install
install -d -m 0755 %{buildroot}%{_datadir}/webapps/element

cp -av dist/element-%{version}/* "%{buildroot}%{_datadir}/webapps/element/"

install -d -m 0755 %{buildroot}%{_sysconfdir}/webapps/element/
install -m 0644 config.sample.json "%{buildroot}%{_sysconfdir}/webapps/element/config.sample.json"

%fdupes %{buildroot}%{_datadir}/webapps/element/

%files
%license LICENSE-AGPL-3.0 LICENSE-GPL-3.0
%dir %{_datadir}/webapps
%{_datadir}/webapps/element
%dir %{_sysconfdir}/webapps
%dir %{_sysconfdir}/webapps/element
%config %{_sysconfdir}/webapps/element/config.sample.json

%changelog
