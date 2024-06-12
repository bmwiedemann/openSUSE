#
# spec file for package element-web
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


Name:           element-web
Version:        1.11.68
Release:        0
Summary:        A glossy Matrix collaboration client - web files
License:        Apache-2.0
Group:          Productivity/Networking/Talk/Clients
URL:            https://github.com/vector-im/element-web
Source0:        https://github.com/vector-im/element-web/archive/v%{version}.tar.gz#/element-web-%{version}.tar.gz
Source1:        npm-packages-offline-cache.tar.gz
Source2:        jitsi_external_api.min.js
Source3:        prepare.sh
Patch0:         fix-webpack-oom.patch
BuildRequires:  fdupes
BuildRequires:  nodejs-packaging
BuildRequires:  yarn
BuildRequires:  rust
BuildRequires:  cargo
BuildArch:      noarch

%description
A glossy Matrix collaboration client - web files

%prep
%autosetup -n element-web-%{version} -a1 -p1

%build
echo 'yarn-offline-mirror "./npm-packages-offline-cache"' > .yarnrc
ls -l ./npm-packages-offline-cache | head

# fix some strange dependency
#cp npm-packages-offline-cache/matrix-analytics-events-0.0.1.tgz \
#   npm-packages-offline-cache/@matrix-analytics-events-0.0.1.tgz
#ls -l ./npm-packages-offline-cache/*matrix-analytics-events*

#sed -i -e 's|    matrix-analytics-events "github:matrix-org/matrix-analytics-events.git#[^"]*"|    matrix-analytics-events "^0.0.1"|' yarn.lock
#sed -i -e 's|"matrix-analytics-events@github:matrix-org/matrix-analytics-events#[^"]*"|matrix-analytics-events@^0.0.1|' yarn.lock

export SENTRYCLI_SKIP_DOWNLOAD=1

yarn install --offline --pure-lockfile

mkdir -p webapp
cp %{SOURCE2} ./webapp/jitsi_external_api.min.js
echo > scripts/build-jitsi.ts

DIST_VERSION=%{version} ./scripts/package.sh

pushd dist || exit 1
tar xf element-%{version}.tar.gz
popd
cp LICENSE dist/element-%{version}/LICENSE

%install
install -d -m 0755 %{buildroot}%{_datadir}/webapps/element

cp -av dist/element-%{version}/* "%{buildroot}%{_datadir}/webapps/element/"

install -d -m 0755 %{buildroot}%{_sysconfdir}/webapps/element/
install -m 0644 config.sample.json "%{buildroot}%{_sysconfdir}/webapps/element/config.sample.json"

%fdupes %{buildroot}%{_datadir}/webapps/element/

%files
%license LICENSE
%dir %{_datadir}/webapps
%{_datadir}/webapps/element
%dir %{_sysconfdir}/webapps
%dir %{_sysconfdir}/webapps/element
%config %{_sysconfdir}/webapps/element/config.sample.json

%changelog
