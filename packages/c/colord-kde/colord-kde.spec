#
# spec file for package colord-kde
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without released
Name:           colord-kde
Version:        22.12.1
Release:        0
Summary:        KDE interfaces and session daemon to colord
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/graphics/colord-kde
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr)
Requires:       colord
Recommends:     %{name}-lang
# Enable calibrate functional if gnome-color-manager installed
Suggests:       gnome-color-manager

%description
Colord-kde provides KCM module and KDE daemon module for colord support.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%files
%license COPYING
%doc MAINTAINERS TODO
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_applicationsdir}/colordkdeiccimporter.desktop
%{_kf5_bindir}/colord-kde-icc-importer
%{_kf5_plugindir}/kcm_colord.so
%{_kf5_servicesdir}/kcm_colord.desktop
%{_kf5_plugindir}/kf5/kded/colord.so

%files lang -f %{name}.lang

%changelog
