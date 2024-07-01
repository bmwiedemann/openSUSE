#
# spec file for package gcompris-qt
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Ioda-Net Sàrl, Charmoille, Switzerland. Bruno Friedmann
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


Name:           gcompris-qt
Version:        4.1
Release:        0
Summary:        Multiactivity educational software for children aged 2–10 (Qt version)
License:        AGPL-3.0-or-later AND CC-BY-4.0 AND Apache-2.0 AND MPL-2.0 AND OFL-1.1 AND GFDL-1.2-or-later AND MIT AND CC0-1.0 AND BSD-2-Clause AND BSD-3-Clause
Group:          Amusements/Teaching/Other
URL:            https://gcompris.net
Source0:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz.sig
Source2:        https://share.kde.org/index.php/s/YjKzYs1bgDsOo5V/download#/%{name}.keyring
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libqt5-qtcharts-imports >= 5.12.0
BuildRequires:  libqt5-qtgraphicaleffects >= 5.12.0
BuildRequires:  libqt5-qtimageformats >= 5.12.0
BuildRequires:  pkgconfig
BuildRequires:  qml-box2d
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Charts) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.12.0
# We don't want the Administrative documentation
# BuildRequires:  kdoctools-devel
BuildRequires:  pkgconfig(Qt5Core) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.12.0
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.12.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Quick) >= 5.12.0
BuildRequires:  pkgconfig(Qt5QuickControls2) >= 5.12.0
BuildRequires:  pkgconfig(Qt5QuickTemplates2) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Script) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12.0
BuildRequires:  pkgconfig(openssl)
# Runtime requirements, it doesn't start without them (boo#1011125)
Requires:       %{name}-activities = %{version}
Requires:       libQt5Multimedia5 >= 5.12.0
Requires:       libQt5Svg5 >= 5.12.0
Requires:       libqt5-qtcharts-imports >= 5.12.0
Requires:       libqt5-qtgraphicaleffects >= 5.12.0
Requires:       libqt5-qtimageformats >= 5.12.0
Requires:       qml-box2d
Recommends:     %{name}-voices = %{version}
Provides:       gcompris = 17.10
Obsoletes:      gcompris < 17.10
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(Qt5QmlModels) >= 5.12.0
%else
BuildRequires:  pkgconfig(Qt5Qml) >= 5.12.0
%endif

%description
GCompris-Qt is an educational software suite comprising
of numerous activities for children aged 2 to 10. Some of the
activities are game orientated, but nonetheless still educational.

Currently, GCompris offers in excess of 100 activities. New
activities can be added, and an activity can implement its own game
scheme.

This version is a rewrite of GCompris using the QtQuick
technology.

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
%setup -q

%build
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
export CFLAGS="%{optflags} -fPIE -pie -fno-strict-aliasing -DNDEBUG"
export CXXFLAGS="%{optflags} -fPIE -pie -fno-strict-aliasing -DNDEBUG"

find . -name CMakeLists.txt \
  -exec sed -i -re '/^[[:blank:]]*[sS][eE][tT][[:blank:]]*\([[:blank:]]*(CMAKE_BUILD_TYPE|CMAKE_COLOR_MAKEFILE|CMAKE_INSTALL_PREFIX|CMAKE_VERBOSE_MAKEFILE).*\)/{s/^/#IGNORE /}' {} +
%cmake_kf5 -d build

%make_build
# Build translastions too.
%make_build BuildTranslations

%install
%cmake_install
#Fix wrong place of man page temporaly
rm -fr %{buildroot}/%{_prefix}/man
# Install desktop file
install -d %{buildroot}/%{_datadir}/applications
install org.kde.gcompris.desktop %{buildroot}/%{_datadir}/applications/org.kde.gcompris.desktop
%suse_update_desktop_file org.kde.gcompris Education Math Languages
# Install icon file
install -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 images/sc-apps-gcompris-qt.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/gcompris-qt.svg

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
#Activities
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/rcc
%{_datadir}/%{name}/rcc/*.rcc

%files lang
%license LICENSES/*
%doc README.md
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.qm

%changelog
