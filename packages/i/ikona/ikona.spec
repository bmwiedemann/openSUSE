#
# spec file for package ikona
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define rdns_name	me.appadeia.ikona

Name:           ikona
Version:        0.7.1
Release:        0
Summary:        Icon Preview designed for Plasma
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://invent.kde.org/KDE/ikona
Source0:        %{name}-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5PlasmaQuick)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       kirigami2
Requires:       plasma-framework-components

%description
A utility to preview icons as they are being made.

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/ikona
%{_datadir}/icons/hicolor/scalable/apps/%{rdns_name}.svg
%{_datadir}/applications/%{rdns_name}.desktop
%{_datadir}/metainfo/%{rdns_name}.appdata.xml

%changelog
