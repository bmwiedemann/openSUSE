#
# spec file for package libkgeomap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkgeomap
Version:        19.08.1
Release:        0
Summary:        Wrapper around different world-map components
License:        LGPL-2.1-only AND GPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  libkexiv2-devel
BuildRequires:  marble-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       libKF5KGeoMap10_0_0 = %{version}
Obsoletes:      libkgeomap-kf5 < %{version}
Provides:       libkgeomap-kf5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

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
Requires:       kconfig-devel
Requires:       ki18n-devel
Requires:       libKF5KGeoMap10_0_0 = %{version}
Requires:       marble-devel
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5Gui)
Requires:       pkgconfig(Qt5WebKitWidgets)
Requires:       pkgconfig(Qt5Widgets)
Requires:       pkgconfig(Qt5Xml)
Obsoletes:      libkgeomap-kf5-devel < %{version}
Provides:       libkgeomap-kf5-devel = %{version}

%description devel
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap,
This library is used by kipi-plugins, digiKam and other kipi host programs

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

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
