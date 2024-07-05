#
# spec file for package kosmindoormap
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

%bcond_without released
Name:           kosmindoormap
Version:        24.05.2
Release:        0
Summary:        OSM multi-floor indoor map renderer
License:        LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/kosmindoormap
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  bison
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KOpeningHours)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
# Fails because of https://bugzilla.opensuse.org/show_bug.cgi?id=1222343
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150500
BuildRequires:  pkgconfig(protobuf)
%endif
BuildRequires:  pkgconfig(zlib)

%description
OSM multi-floor indoor map renderer.

%package imports
Summary:      QML imports for kosmindoormap
Requires:       libKOSM1 = %{version}

%description imports
QML components for KOpeningHours.

%package -n libKOSM1
Summary:        OSM primitives for kosmindoormap
Requires:       kosmindoormap >= %{version}

%description -n libKOSM1
OSM primitives for kosmindoormap.

%package -n libKOSMIndoorMap1
Summary:        OSM multi-floor indoor map renderer

%description -n libKOSMIndoorMap1
OSM multi-floor indoor map renderer library.

%package devel
Summary:        Development package for kosmindoormap
Requires:       libKOSM1 = %{version}
Requires:       libKOSMIndoorMap1 = %{version}

%description devel
Development files for the KOSM and KOSMIndoorMap libraries.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_TESTING=ON

%kf6_build

%install
%kf6_install

%find_lang %{name}

%check
# Two tests fail on i586 (one minor floating point issue and a color one).
# Upstream is investigating
%ifnarch i586
%ctest
%endif

%ldconfig_scriptlets -n libKOSM1
%ldconfig_scriptlets -n libKOSMIndoorMap1

%files
%{_kf6_debugdir}/org_kde_kosmindoormap.categories

%files imports
%{_kf6_qmldir}/org/kde/kosmindoormap/
%{_kf6_qmldir}/org/kde/osm/

%files -n libKOSM1
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKOSM.so.*

%files -n libKOSMIndoorMap1
%{_kf6_libdir}/libKOSMIndoorMap.so.*

%files devel
%{_includedir}/KOSM/
%{_includedir}/KOSMIndoorMap/
%{_includedir}/kosm/
%{_includedir}/kosmindoormap/
%{_includedir}/kosmindoormap_version.h
%{_kf6_cmakedir}/KOSMIndoorMap/
%{_kf6_libdir}/libKOSM.so
%{_kf6_libdir}/libKOSMIndoorMap.so

%files lang -f %{name}.lang

%changelog
