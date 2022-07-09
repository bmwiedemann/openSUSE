#
# spec file for package kalendar
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


%define kf5_version 5.91.0
%bcond_without released
Name:           kalendar
Version:        22.04.3
Release:        0
Summary:        Calendar Application
License:        GPL-3.0-only
URL:            https://apps.kde.org/kalendar
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# No QtWebEngine for other archs
ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 %{mips} %{riscv}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5Akonadi) >= 5.19.0
BuildRequires:  cmake(KF5AkonadiContact) >= 5.19.0
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport) >= 5.19.0
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5EventViews) >= 5.19.0
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
Requires:       kalendarac
Requires:       kdepim-addons
Requires:       kdepim-runtime
# No automatic qmlimport requires for embedded resources :-/
Requires:       kirigami2 >= %{kf5_version}
Requires:       qt5qmlimport(QtGraphicalEffects.1)
Requires:       qt5qmlimport(QtLocation.5)
Requires:       qt5qmlimport(QtQuick.Dialogs.1)
Requires:       qt5qmlimport(org.kde.kitemmodels.1)
# Got vendored for now
#Requires:       qt5qmlimport(org.kde.kirigamiaddons.treeview.1)

%description
Calendar application using Akonadi to sync with external services (NextCloud, GMail, ...).

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with released}
  %find_lang %{name} --with-man --all-name
%endif

%files
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.kalendar.desktop
%{_kf5_appstreamdir}/org.kde.kalendar.appdata.xml
%{_kf5_bindir}/kalendar
%{_kf5_debugdir}/kalendar.categories
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.kalendar.svg

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
