#
# spec file for package colord-kde
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


%global __requires_exclude qt6qmlimport\\(kcmcolord.*
%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           colord-kde
Version:        24.05.2
Release:        0
Summary:        KDE interfaces and session daemon to colord
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/graphics/colord-kde
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr)
Requires:       colord
# Enable calibrate functional if gnome-color-manager installed
Suggests:       gnome-color-manager

%description
Colord-kde provides KCM module and KDE daemon module for colord support.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

%files
%license COPYING
%doc MAINTAINERS
%{_kf6_applicationsdir}/colordkdeiccimporter.desktop
%{_kf6_applicationsdir}/kcm_colord.desktop
%{_kf6_bindir}/colord-kde-icc-importer
%{_kf6_plugindir}/kf6/kded/colord.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_colord.so

%files lang -f %{name}.lang

%changelog
