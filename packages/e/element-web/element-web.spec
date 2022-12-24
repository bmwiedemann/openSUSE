#
# spec file for package element-web
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


Name:           element-web
Version:        1.11.17
Release:        0
Summary:        A glossy Matrix collaboration client - web files
License:        Apache-2.0
URL:            https://github.com/vector-im/element-web
Source0:        https://github.com/vector-im/element-web/archive/v%{version}.tar.gz#/element-web-%{version}.tar.gz
Source1:        npm-packages-offline-cache.tar.gz
Source2:        jitsi_external_api.min.js
Source3:        prepare.sh
Patch0:         fix-webpack-oom.patch
BuildRequires:  yarn
BuildRequires:  nodejs18
BuildArch:      noarch

%description
A glossy Matrix collaboration client - web files

%prep
%autosetup -n element-web-%{version} -p0

%build
echo 'yarn-offline-mirror "./npm-packages-offline-cache"' > .yarnrc
tar xf %{SOURCE1}
ls ./npm-packages-offline-cache | head

# fix some strange dependency
cd ./npm-packages-offline-cache
cp matrix-analytics-events-0.0.1.tgz @matrix-analytics-events-0.0.1.tgz
cd ..
ls ./npm-packages-offline-cache | grep matrix-analytics-events
sed -i -e 's|    matrix-analytics-events "github:matrix-org/matrix-analytics-events.git#[^"]*"|    matrix-analytics-events "^0.0.1"|' yarn.lock
sed -i -e 's|"matrix-analytics-events@github:matrix-org/matrix-analytics-events#[^"]*"|matrix-analytics-events@^0.0.1|' yarn.lock

yarn install --offline --pure-lockfile

mkdir -p webapp
cp %{SOURCE2} ./webapp/jitsi_external_api.min.js
echo 'return;' > scripts/build-jitsi.js

DIST_VERSION=%{version} ./scripts/package.sh

cd dist
tar xf element-%{version}.tar.gz
cd element-%{version}
cp ../../LICENSE ./

%install
cd dist
cd element-%{version}
install -d %{buildroot}/{usr/share/webapps,etc/webapps}/element

cp -r * "%{buildroot}%{_datadir}/webapps/element/"
install -Dm644 config.sample.json -t "%{buildroot}%{_sysconfdir}/webapps/element/"

%files
%license LICENSE
%dir %{_datadir}/webapps
%dir %{_sysconfdir}/webapps
%{_datadir}/webapps/element
%{_sysconfdir}/webapps/element

%changelog
