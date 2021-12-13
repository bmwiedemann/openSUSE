#
# spec file for package element-desktop
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.9.7
Release:        0
Summary:        A glossy Matrix collaboration client - desktop
License:        Apache-2.0
URL:            https://github.com/vector-im/element-desktop
Source0:        https://github.com/vector-im/element-desktop/archive/v%{version}.tar.gz#/element-desktop-%{version}.tar.gz
Source1:        https://github.com/vector-im/element-web/archive/v%{version}.tar.gz#/element-web-%{version}.tar.gz
Source2:        dist.tar.gz
Source3:        io.element.Element.desktop
Source4:        element-desktop.sh
Source5:        prepare_tarball.sh
BuildRequires:  element-web
BuildRequires:  hicolor-icon-theme
BuildRequires:  nodejs-electron
Requires:       element-web
Requires:       nodejs-electron
BuildArch:      noarch

%description
A glossy Matrix collaboration client - desktop

%prep
%setup -q
sed -i 's@"electronVersion": "11.2.3"@"electronVersion": "12.0.4"@g' package.json
sed -i 's@"https://packages.riot.im/desktop/update/"@null@g' element.io/release/config.json
pwd
cd ..
pwd
ls -l
tar xvf %{SOURCE1}
cd element-desktop-%{version}

%build
# Unpack prepared (see prepare.sh) webapp
tar xvf %{SOURCE2}

%install
install -d %{buildroot}{%{_prefix}/lib/element/,%{_sysconfdir}/webapps/element}

# Install the app content, replace the webapp with a symlink to the system package
cp -r dist/linux-unpacked/resources/* "%{buildroot}%{_prefix}/lib/element/"
ln -s %{_datadir}/webapps/element "%{buildroot}%{_prefix}/lib/element/webapp"

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
%{_prefix}/lib/element/
%{_sysconfdir}/webapps/element/config.json
%{_datadir}/webapps/element/config.json
%{_sysconfdir}/element/
%{_datadir}/applications/io.element.Element.desktop
%{_datadir}/icons/hicolor/scalable/apps/io.element.Element.svg
%{_datadir}/icons/hicolor/*/apps/io.element.Element.png

%changelog
