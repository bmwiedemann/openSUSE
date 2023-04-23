#
# spec file for package angelfish
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


%bcond_without  released
Name:           angelfish
Version:        23.04.0
Release:        0
Summary:        Mobile web browser
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/angelfish
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  hicolor-icon-theme
# Cargo is only needed if Corrosion is present
# BuildRequires:  cmake(Corrosion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kirigami-addons
Requires:       kirigami2
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
Angelfish is a mobile web browser. It supports typical browser features, such
as bookmarks, history and tabs.

%prep
%autosetup -p1

%lang_package

%build
%if 0%{?suse_version} == 1500
  export CXX=g++-10
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%files
%doc README.md
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.angelfish.desktop
%{_kf5_appstreamdir}/org.kde.angelfish.metainfo.xml
%{_kf5_bindir}/angelfish
%{_kf5_bindir}/angelfish-webapp
%{_kf5_configkcfgdir}/angelfishsettings.kcfg
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.angelfish.svg
%{_kf5_notifydir}/angelfish.notifyrc

%files lang -f %{name}.lang

%changelog
