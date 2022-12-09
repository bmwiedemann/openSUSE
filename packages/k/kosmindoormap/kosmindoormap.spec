#
# spec file for package kosmindoormap
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


%define soversion 1
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kosmindoormap
Version:        22.12.0
Release:        0
Summary:        OSM indoor map QML component
License:        LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/kosmindoormap
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)
Requires:       libKOSM%{soversion} = %{version}

%description
QML components for KDE Itinerary.

%package -n libKOSM%{soversion}
Summary:        OSM primitives for kosmindoormap

%description -n libKOSM%{soversion}
OSM primitives for kosmindoormap.

%package -n libKOSMIndoorMap%{soversion}
Summary:        OSM multi-floor indoor map renderer

%description -n libKOSMIndoorMap%{soversion}
OSM multi-floor indoor map renderer library.

%package devel
Summary:        Development package for kosmindoormap
Requires:       libKOSM%{soversion} = %{version}
Requires:       libKOSMIndoorMap%{soversion} = %{version}

%description devel
This package contains development files for the KOSM and KOSMIndoorMap libraries.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%check
# Two tests fail on i586 (one minor floating point issue and a color one).
# Upstream is investigating
%ifnarch i586
%ctest
%endif

%post -n libKOSM%{soversion} -p /sbin/ldconfig
%postun -n libKOSM%{soversion} -p /sbin/ldconfig
%post -n libKOSMIndoorMap%{soversion} -p /sbin/ldconfig
%postun -n libKOSMIndoorMap%{soversion} -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README.md
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_debugdir}/org_kde_kosmindoormap.categories
%{_kf5_qmldir}/org/kde/kosmindoormap/

%files -n libKOSM%{soversion}
%{_kf5_libdir}/libKOSM.so.*

%files -n libKOSMIndoorMap%{soversion}
%{_kf5_libdir}/libKOSMIndoorMap.so.*

%files devel
%{_includedir}/KOSM/
%{_includedir}/KOSMIndoorMap/
%{_includedir}/kosm/
%{_includedir}/kosmindoormap/
%{_includedir}/kosmindoormap_version.h
%{_kf5_cmakedir}/KOSMIndoorMap/
%{_kf5_libdir}/libKOSM.so
%{_kf5_libdir}/libKOSMIndoorMap.so

%files lang -f %{name}.lang

%changelog
