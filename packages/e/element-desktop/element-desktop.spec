#
# spec file for package element-desktop
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


Name:           element-desktop
Version:        1.11.17
Release:        0
Summary:        A glossy Matrix collaboration client - desktop
License:        Apache-2.0
URL:            https://github.com/vector-im/element-desktop
Source0:        https://github.com/vector-im/element-desktop/archive/v%{version}.tar.gz#/element-desktop-%{version}.tar.gz
Source1:        https://github.com/vector-im/element-web/archive/v%{version}.tar.gz#/element-web-%{version}.tar.gz
Source2:        npm-packages-offline-cache.tar.gz
Source3:        io.element.Element.desktop
Source4:        element-desktop.sh
Source5:        prepare.sh
BuildRequires:  element-web = %{version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  jq
BuildRequires:  moreutils
BuildRequires:  nodejs-electron-devel
BuildRequires:  yarn
Requires:       element-web = %{version}
Requires:       nodejs-electron

#Element contains no native code
BuildArch:      noarch

%description
A glossy Matrix collaboration client - desktop

%prep
%setup -q
SYSTEM_ELECTRON_VERSION=$(<%{_libdir}/electron/version)
jq -c '.build["electronVersion"]="'$SYSTEM_ELECTRON_VERSION'" | .build["electronDist"]="%{_libdir}/electron"' < package.json | sponge package.json
jq -c '.build["linux"]["target"]="dir"' < package.json | sponge package.json
cat package.json
jq '.piwik=false | .update_base_url=null' < element.io/release/config.json | sponge element.io/release/config.json
pwd
cd ..
pwd
ls -l
tar xvf %{SOURCE1}
cd element-desktop-%{version}

%build
echo 'yarn-offline-mirror "./npm-packages-offline-cache"' >> .yarnrc
echo 'nodedir %{_includedir}/electron' >> .yarnrc
tar xf %{SOURCE2}
ls ./npm-packages-offline-cache | head

export ELECTRON_SKIP_BINARY_DOWNLOAD=1
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1

yarn install --offline --pure-lockfile

#tar xf %%{SOURCE6}
export PATH="$PATH:node_modules/.bin"
#export ELECTRON_BUILDER_CACHE="$(pwd)/electron-builder-offline-cache/"
#yarn run build:native
yarn run build:universal

%install
install -d %{buildroot}{%{_datadir}/element/,%{_sysconfdir}/webapps/element}

# Install the app content, replace the webapp with a symlink to the system package
cp -pr dist/linux-universal-unpacked/resources/* "%{buildroot}%{_datadir}/element/"
ln -s %{_datadir}/webapps/element "%{buildroot}%{_datadir}/element/webapp"

# Config file
ln -s %{_sysconfdir}/element/config.json "%{buildroot}%{_sysconfdir}/webapps/element/config.json"
install -Dm644 element.io/release/config.json -t "%{buildroot}%{_sysconfdir}/element"
mkdir -p "%{buildroot}%{_datadir}/webapps/element/"
ln -s %{_sysconfdir}/webapps/element/config.json "%{buildroot}%{_datadir}/webapps/element/config.json" # moved here from element-web to make symlink check happy

# Required extras
install -Dm644 %{SOURCE3} -t "%{buildroot}%{_datadir}/applications/"
install -Dm755 %{SOURCE4} "%{buildroot}%{_bindir}/%{name}"

# Icons
install -Dm644 ../element-web-%{version}/res/themes/element/img/logos/element-logo.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.element.Element.svg"
for i in 16 24 48 64 96 128 256 512; do
	install -Dm644 build/icons/${i}x${i}.png "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.element.Element.png"
done

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/element/
%config %{_sysconfdir}/element/config.json
%config %{_sysconfdir}/webapps/element/config.json
%{_datadir}/webapps/element/config.json
%{_sysconfdir}/element/
%{_datadir}/applications/io.element.Element.desktop
%{_datadir}/icons/hicolor/scalable/apps/io.element.Element.svg
%{_datadir}/icons/hicolor/*/apps/io.element.Element.png

%changelog
