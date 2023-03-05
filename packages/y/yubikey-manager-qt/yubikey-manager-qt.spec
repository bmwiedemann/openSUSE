#
# spec file for package yubikey-manager-qt
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


%define bname ykman-gui
Name:           yubikey-manager-qt
Version:        1.2.5
Release:        0
Summary:        Graphical application for configuring a YubiKey
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://developers.yubico.com/yubikey-manager-qt/Releases
Source0:        https://developers.yubico.com/yubikey-manager-qt/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubikey-manager-qt/Releases/%{name}-%{version}.tar.gz.sig
Source2:        yubikey-manager-qt.keyring
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Requires:       python3-pyotherside
Requires:       python3-yubikey-manager >= 4.0.7

%description
A graphical application for configuring a YubiKey over all transport modes..

%prep
%setup -q -n %{name}
sed -i 's|yubikey-manager==|yubikey-manager>=|' requirements.txt
# Fix build for Leap 15 and SLE 15
sed -i 's|python |python3 |g' ykman-cli/ykman-cli.pro
sed -i 's|python |python3 |g' ykman-gui/ykman-gui.pro

%build
%qmake5
%make_build

%install
make install INSTALL_ROOT="%{buildroot}";
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 resources/icons/ykman.png %{buildroot}%{_datadir}/pixmaps/
%suse_update_desktop_file -i %{bname} System Security

%files
%doc NEWS README
%license COPYING
%{_bindir}/%{bname}
%{_datadir}/applications/%{bname}.desktop
%{_datadir}/pixmaps/ykman.png

%changelog
