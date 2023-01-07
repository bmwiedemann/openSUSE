#
# spec file for package itinerary
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           itinerary
Version:        22.12.1
Release:        0
Summary:        Itinerary and boarding pass management application
License:        LGPL-2.0-or-later
URL:            https://apps.kde.org/itinerary
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5QQC2DeskopStyle)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KOSMIndoorMap)
BuildRequires:  cmake(KPimItinerary)
BuildRequires:  cmake(KPimPkPass)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Location)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} <= 1500
# variadic macro causes build issues
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
# QML imports
Requires:       kirigami2
Requires:       prison-qt5-imports
# Runtime dependencies (itinerary won't start without these packages)
Requires:       kopeninghours
Requires:       kosmindoormap
Requires:       kpublictransport

%description
Itinerary and boarding pass management application.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} <= 1500
  export CXX=g++-10
%endif

%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

# Should be Utility Maps, but the checker does not like it
%suse_update_desktop_file org.kde.itinerary Education Geography
install -m0644 -D %{_kf5_iconsdir}/breeze/actions/22/map-globe.svg \
  %{buildroot}%{_kf5_iconsdir}/hicolor/22x22/actions/map-globe.svg

%check
# one test fails on ppc64 (be). Upstream is investigating
%ifnarch ppc64
%ctest
%endif

%find_lang %{name} --all-name

%files lang -f %{name}.lang

%files
%license LICENSES/*
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_applicationsdir}/org.kde.itinerary.desktop
%{_kf5_appstreamdir}/org.kde.itinerary.appdata.xml
%{_kf5_bindir}/itinerary
%{_kf5_debugdir}/org_kde_itinerary.categories
%{_kf5_iconsdir}/hicolor/
%{_kf5_libdir}/libSolidExtras.so
%{_kf5_notifydir}/itinerary.notifyrc
%{_kf5_qmldir}/org/kde/solidextras/
%{_kf5_qmldir}/org/kde/itinerary/

%changelog
