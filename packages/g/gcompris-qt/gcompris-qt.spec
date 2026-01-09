#
# spec file for package gcompris-qt
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define qt6_version 6.5.0

Name:           gcompris-qt
Version:        25.1
Release:        0
Summary:        Multiactivity educational software for children aged 2–10 (Qt version)
License:        AGPL-3.0-or-later AND CC-BY-4.0 AND Apache-2.0 AND MPL-2.0 AND OFL-1.1 AND GFDL-1.2-or-later AND MIT AND CC0-1.0 AND BSD-2-Clause AND BSD-3-Clause
Group:          Amusements/Teaching/Other
URL:            https://gcompris.net
Source0:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz.sig
Source2:        https://share.kde.org/index.php/s/YjKzYs1bgDsOo5V/download#/%{name}.keyring
#PATCH-FIX-OPENSUSE -- gcompris-25.1.1-qt-6.10.patch
Patch1:         gcompris-25.1.1-qt-6.10.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  qml-box2d
BuildRequires:  qt6-waylandclient-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6Charts) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6QmlTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6QmlWorkerScript) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2Basic) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2BasicStyleImpl) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(openssl)
Requires:       %{name}-activities = %{version}
Recommends:     %{name}-voices = %{version}
Provides:       gcompris = 17.10
Obsoletes:      gcompris < 17.10

%description
GCompris-Qt is an educational software suite comprising
of numerous activities for children aged 2 to 10. Some of the
activities are game orientated, but nonetheless still educational.

Currently, GCompris offers in excess of 100 activities. New
activities can be added, and an activity can implement its own game
scheme.

%package activities
Summary:        Activity files for %{name}
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description activities
This package contains the bundle of activities for %{name}.
More than 100 activities are available.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CXX=g++-13 CC=gcc-13
%cmake \
	-DQML_BOX2D_MODULE=system \
	-DQML_BOX2D_LIBRARY=/usr/lib64/Box2D/libqmlbox2d.so build
%cmake_build
%endif
%if 0%{?suse_version} >= 1600
%cmake_kf6 \
	-DQML_BOX2D_MODULE=system \
	-DQML_BOX2D_LIBRARY=/usr/lib64/Box2D/libqmlbox2d.so build
%kf6_build
%endif

%install
%if 0%{?suse_version} < 1600
%cmake_install
%endif
%if 0%{?suse_version} >= 1600
%kf6_install
%endif

%files
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/256x256/
%{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/applications/org.kde.gcompris.desktop
%{_datadir}/icons/hicolor/256x256/apps/gcompris-qt.png
%{_datadir}/icons/hicolor/scalable/apps/gcompris-qt.svg
%{_datadir}/metainfo/org.kde.gcompris.appdata.xml

%files activities
%license LICENSES/*
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/rcc
%{_datadir}/%{name}/rcc/*.rcc

%files lang
%license LICENSES/*
%doc README.md
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.qm

%changelog
