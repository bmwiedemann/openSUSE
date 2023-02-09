#
# spec file for package kaidan
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


Name:           kaidan
Version:        0.8.0
Release:        0
Summary:        A XMPP client based on KDE Framework
License:        GPL-3.0-or-later AND SUSE-GPL-3.0+-with-openssl-exception AND MIT AND AML AND CC-BY-SA-4.0
URL:            https://www.kaidan.im
Source0:        https://download.kde.org/unstable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/unstable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kaidan.keyring
# PATCH-FIX-UPSTREAM
Patch0:         0001-QrCodeDecoder-Replace-deprecated-BarcodeFormat-QR_CO.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-QrCodeGenerator-Replace-deprecated-BarcodeFormat-QR_.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Support-ZXing-2.0.patch
BuildRequires:  cmake >= 3.3
BuildRequires:  extra-cmake-modules >= 5.40.0
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Kirigami2) >= 5.67.0
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5QQC2DeskopStyle)
BuildRequires:  cmake(QXmpp) >= 1.3.0
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Location)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(ZXing) >= 1.0.8
Requires:       kirigami2 >= 5.67.0
Requires:       libqt5-qtquickcontrols2

%description
Kaidan is a simple Jabber/XMPP client providing a user-interface using
Kirigami and QtQuick. The back-end of Kaidan is entirely written in C++
using the qxmpp XMPP client library and Qt 5.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build '-DI18N:BOOL=ON' '-DQUICK_COMPILER:BOOL=ON'
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file im.kaidan.kaidan

%files
%license LICENSE
%doc README.md NEWS
%dir %{_kf5_sharedir}/%{name}
%{_kf5_applicationsdir}/im.kaidan.kaidan.desktop
%{_kf5_appstreamdir}/im.kaidan.kaidan.appdata.xml
%{_kf5_bindir}/%{name}
%{_kf5_iconsdir}/hicolor/*/apps/%{name}.*
%{_kf5_notifydir}/kaidan.notifyrc
%{_kf5_sharedir}/%{name}/images
%{_kf5_sharedir}/%{name}/servers.json

%changelog
