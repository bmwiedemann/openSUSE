#
# spec file for package libkgeomap
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkgeomap
Version:        20.08.1
Release:        0
Summary:        Wrapper around different world-map components
License:        LGPL-2.1-only AND GPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KExiv2)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       libKF5KGeoMap10_0_0 = %{version}
Obsoletes:      libkgeomap-kf5 < %{version}
Provides:       libkgeomap-kf5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap,
This library is used by kipi-plugins, digiKam and other kipi host programs

%package -n libKF5KGeoMap10_0_0
Summary:        Wrapper around different world-map components
Group:          Development/Libraries/KDE
Recommends:     marble5

%description -n libKF5KGeoMap10_0_0
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap,
This library is used by kipi-plugins, digiKam and other kipi host programs

%package devel
Summary:        Wrapper around different world-map components
Group:          Development/Libraries/KDE
Requires:       libKF5KGeoMap10_0_0 = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5I18n)
Requires:       cmake(Marble)
Requires:       cmake(Qt5Concurrent)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Gui)
Requires:       cmake(Qt5WebKitWidgets)
Requires:       cmake(Qt5Widgets)
Requires:       cmake(Qt5Xml)
Obsoletes:      libkgeomap-kf5-devel < %{version}
Provides:       libkgeomap-kf5-devel = %{version}

%description devel
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap,
This library is used by kipi-plugins, digiKam and other kipi host programs

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5KGeoMap10_0_0 -p /sbin/ldconfig
%postun -n libKF5KGeoMap10_0_0 -p /sbin/ldconfig

%files devel
%doc README
%{_kf5_cmakedir}/KF5KGeoMap/
%{_kf5_includedir}/KGeoMap/
%{_kf5_includedir}/libkgeomap_version.h
%{_kf5_libdir}/libKF5KGeoMap.so

%files -n libKF5KGeoMap10_0_0
%{_libdir}/libKF5KGeoMap.so.*

%files
%{_datadir}/libkgeomap/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
