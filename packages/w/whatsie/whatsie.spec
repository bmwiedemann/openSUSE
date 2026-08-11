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
Version:        5.1.0
Release:        0
Summary:        Feature rich WhatsApp Client for Desktop Linux
License:        MIT
URL:            https://github.com/keshavbhatt/whatsie
Source:         %{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel >= 6.10
BuildRequires:  qt6-webenginecore-devel
BuildRequires:  pkgconfig(Qt6Location)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6PositioningQuick)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickTest)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6WebChannel)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
ExcludeArch:    %{ix86}

%description
Feature rich WhatsApp Client for Desktop Linux.

%prep
%autosetup -p1

%build
%cmake

%install
%cmake_install

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

%changelog
