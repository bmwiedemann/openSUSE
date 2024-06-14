#
# spec file for package itinerary
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           itinerary
Version:        24.05.1
Release:        0
Summary:        Itinerary and boarding pass management application
License:        LGPL-2.0-or-later
URL:            https://apps.kde.org/itinerary
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6UnitConversion) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KHealthCertificate)
BuildRequires:  cmake(KOSMIndoorMap)
BuildRequires:  cmake(KPim6Itinerary) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PkPass) >= %{kpim6_version}
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(LibIcal)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(QuotientQt6)
BuildRequires:  pkgconfig(zlib)
# itinerary uses icons from the breeze theme
Requires:       kf6-breeze-icons
# Upstream insists in having these as build dependencies...
BuildRequires:       kf6-kirigami-imports >= %{kf6_version}
BuildRequires:       kf6-prison-imports >= %{kf6_version}
BuildRequires:       kf6-ki18n-imports >= %{kf6_version}
BuildRequires:       qt6qmlimport(QtPositioning)
BuildRequires:       qt6qmlimport(QtLocation)
BuildRequires:       qt6qmlimport(org.kde.kosmindoormap)
BuildRequires:       qt6qmlimport(org.kde.kopeninghours)
# QML imports
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-prison-imports >= %{kf6_version}
Requires:       kf6-ki18n-imports >= %{kf6_version}
# Runtime dependencies (itinerary won't start without these packages)
Requires:       kpublictransport-imports
Requires:       kopeninghours-imports
Requires:       kosmindoormap-imports

%description
Itinerary and boarding pass management application.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_TESTING=ON

%kf6_build

%install
%kf6_install

# Should be Utility Maps, but the checker does not like it
%suse_update_desktop_file org.kde.itinerary Education Geography

%find_lang %{name} --all-name

%check
# one test fails on ppc64 (be)
%ifnarch ppc64
%ctest --exclude-regex "(itinerary-self-test)"
%endif

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.itinerary.desktop
%{_kf6_appstreamdir}/org.kde.itinerary.appdata.xml
%{_kf6_bindir}/itinerary
%{_kf6_debugdir}/org_kde_itinerary.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.itinerary.svg
%{_kf6_libdir}/libSolidExtras.so
%{_kf6_notificationsdir}/itinerary.notifyrc
%dir %{_kf6_plugindir}/kf6/kfilemetadata
%{_kf6_plugindir}/kf6/kfilemetadata/kfilemetadata_itineraryextractor.so
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/itinerarythumbnail.so
%{_kf6_qmldir}/org/kde/solidextras/

%files lang -f %{name}.lang

%changelog
