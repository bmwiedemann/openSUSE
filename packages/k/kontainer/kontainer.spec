#
# spec file for package kontainer
#
# Copyright (c) 2026 SUSE LLC
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

%define appid io.github.DenysMb.Kontainer

Name:           kontainer
Version:        1.6.2
Release:        0
Summary:        A management tool built with Qt6 and KDE Frameworks 6
License:        GPL-3.0-or-later
URL:            https://invent.kde.org/denysmb/Kontainer
Source:         %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.20
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)

%description
Kontainer is a container/application management tool designed with Kirigami, 
leveraging Qt6 and KDE Frameworks 6.

%lang_package

%prep
%autosetup -p1

%build
%cmake 

%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
%ctest

%files
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{name}.lang

%changelog
