#
# spec file for package whatsie
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


Name:           whatsie
Version:        4.16.3
Release:        0
Summary:        Feature rich WhatsApp Client for Desktop Linux
License:        MIT
URL:            https://github.com/keshavbhatt/whatsie
Source:         https://github.com/keshavbhatt/whatsie/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5PositioningQuick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickTest)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebEngineCore)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)

%description
Feature rich WhatsApp Client for Desktop Linux.

%prep
%autosetup

%build
%qmake5 src
%make_build

%install
make install INSTALL_ROOT=%{buildroot}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/whatsie
%{_datadir}/applications/com.ktechpit.whatsie.desktop
%{_datadir}/icons/hicolor/???x???/apps/com.ktechpit.whatsie.png
%{_datadir}/icons/hicolor/??x??/apps/com.ktechpit.whatsie.png
%{_datadir}/icons/hicolor/scalable/apps/com.ktechpit.whatsie.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.ktechpit.whatsie-symbolic.svg
%{_datadir}/metainfo/com.ktechpit.whatsie.appdata.xml
%dir %{_datadir}/org.keshavnrj.ubuntu
%dir %{_datadir}/org.keshavnrj.ubuntu/WhatSie/
%dir %{_datadir}/org.keshavnrj.ubuntu/WhatSie/qtwebengine_dictionaries
%{_datadir}/org.keshavnrj.ubuntu/WhatSie/qtwebengine_dictionaries/*.bdic

%changelog
