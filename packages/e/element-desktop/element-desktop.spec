#
# spec file for package element-desktop
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


Name:           element-desktop
Version:        1.11.43
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
Source6:        hak.tar.gz
BuildRequires:  element-web = %{version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jq
BuildRequires:  moreutils
BuildRequires:  nodejs-electron-devel
BuildRequires:  yarn
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  python3
BuildRequires:  sqlcipher-devel
BuildRequires:  libsecret-devel
BuildRequires:  gcc-c++
Requires:       element-web = %{version}
Requires:       nodejs-electron
%if 0%{?suse_version} <= 1540
BuildRequires:  nodejs18
%endif

# hak*.tar.gz only available for those architectures
ExclusiveArch:  x86_64 aarch64

%description
A glossy Matrix collaboration client - desktop

%prep
%setup -q -a1 -a2 -a6
%autopatch -p1
SYSTEM_ELECTRON_VERSION=$(<%{_libdir}/electron/version)
jq -c '.build["electronVersion"]="'$SYSTEM_ELECTRON_VERSION'" | .build["electronDist"]="%{_libdir}/electron"' < package.json | sponge package.json
jq -c '.build["linux"]["target"]="dir"' < package.json | sponge package.json
cat package.json
jq '.piwik=false | .update_base_url=null' < element.io/release/config.json | sponge element.io/release/config.json

# build tools expect python3 interpreter behind "python"
mkdir -p $HOME/bin
ln -sf /usr/bin/python3 $HOME/bin/python

%ifarch aarch64
mv -v .hak/matrix-seshat/x86_64-unknown-linux-gnu .hak/matrix-seshat/aarch64-unknown-linux-gnu
mv -v .hak/keytar/x86_64-unknown-linux-gnu .hak/keytar/aarch64-unknown-linux-gnu
%endif

%build
echo 'yarn-offline-mirror "./npm-packages-offline-cache"' >> .yarnrc
echo 'nodedir %{_includedir}/electron' >> .yarnrc

export ELECTRON_SKIP_BINARY_DOWNLOAD=1
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1

yarn install --offline --pure-lockfile

export PATH="$(pwd)/node_modules/.bin:${HOME}/bin:${PATH}"
#export ELECTRON_BUILDER_CACHE="$(pwd)/electron-builder-offline-cache/"

yarn run hak build
yarn run hak copyandlink

yarn run build:native
yarn run build:universal

%install
# Install the app content, replace the webapp with a symlink to the system package
install -d -m 0755 "%{buildroot}%{_datadir}/element/"
cp -av dist/linux-universal-unpacked/resources/* "%{buildroot}%{_datadir}/element/"
ln -s %{_datadir}/webapps/element "%{buildroot}%{_datadir}/element/webapp"

# Install binaries to /usr/lib
install -d -m 0755 "%{buildroot}%{_prefix}/lib/element/"
install -m0755 dist/linux-universal-unpacked/resources/app.asar.unpacked/node_modules/keytar/build/Release/keytar.node "%{buildroot}%{_prefix}/lib/element/keytar.node"
install -m0755 dist/linux-universal-unpacked/resources/app.asar.unpacked/node_modules/matrix-seshat/index.node "%{buildroot}%{_prefix}/lib/element/matrix-seshat.node"
ln -sfv "%{_prefix}/lib/element/keytar.node" "%{buildroot}%{_datadir}/element/app.asar.unpacked/node_modules/keytar/build/Release/keytar.node"
ln -sfv "%{_prefix}/lib/element/matrix-seshat.node" "%{buildroot}%{_datadir}/element/app.asar.unpacked/node_modules/matrix-seshat/index.node"

# Config file
install -m 0755 -d %{buildroot}%{_sysconfdir}/element
install -m 0644 element.io/release/config.json "%{buildroot}%{_sysconfdir}/element/config.json"

install -m 0755 -d %{buildroot}%{_sysconfdir}/webapps/element
ln -s %{_sysconfdir}/element/config.json "%{buildroot}%{_sysconfdir}/webapps/element/config.json"

install -d -m 0755 "%{buildroot}%{_datadir}/webapps/element/"
ln -s %{_sysconfdir}/element/config.json "%{buildroot}%{_datadir}/webapps/element/config.json" # moved here from element-web to make symlink check happy

# Required extras
install -d -m 0755 "%{buildroot}%{_datadir}/applications/"
install -m 0644 %{SOURCE3} "%{buildroot}%{_datadir}/applications/io.element.Element.desktop"
install -d -m 0755 "%{buildroot}%{_bindir}/"
install -m 0755 %{SOURCE4} "%{buildroot}%{_bindir}/%{name}"

# Icons
install -d -m 0755 "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/"
install -m 0644 element-web-%{version}/res/themes/element/img/logos/element-logo.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.element.Element.svg"
for i in 16 24 48 64 96 128 256 512; do
	install -d -m 0755 "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/"
	install -m 0644 build/icons/${i}x${i}.png "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.element.Element.png"
done

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/element/
%{_prefix}/lib/element/
%config(noreplace) %{_sysconfdir}/element/config.json
%{_sysconfdir}/webapps/element/config.json
%{_datadir}/webapps/element/config.json
%dir %{_sysconfdir}/element/
%{_datadir}/applications/io.element.Element.desktop
%{_datadir}/icons/hicolor/scalable/apps/io.element.Element.svg
%{_datadir}/icons/hicolor/*/apps/io.element.Element.png

%changelog
