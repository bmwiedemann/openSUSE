#
# spec file for package kalgebra
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


# Internal QML imports
%global __requires_exclude qmlimport\\((widgets|org\\.kde\\.kalgebra\\.mobile).*

# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kalgebra
Version:        22.12.1
Release:        0
Summary:        Math Expression Solver and Plotter
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  xz
BuildRequires:  cmake(Analitza5)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(eigen3)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
KAlgebra is a math expression solver and plotter.

%package mobile
Summary:        Math Expression Solver and Plotter - mobile version
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-lang

%description mobile
KAlgebra is a math expression solver and plotter. This package includes
a QtQuick based version for use in mobile (phone, tablet) environments.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%fdupes -s %{buildroot}

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/kalgebra
%{_kf5_applicationsdir}/org.kde.kalgebra.desktop
%{_kf5_appstreamdir}/org.kde.kalgebra.appdata.xml
%{_kf5_bindir}/calgebra
%{_kf5_bindir}/kalgebra
%{_kf5_iconsdir}/hicolor/*/apps/kalgebra.*
%{_kf5_plasmadir}/
%{_kf5_servicesdir}
%{_kf5_sharedir}/katepart5

%files mobile
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kalgebramobile.desktop
%{_kf5_bindir}/kalgebramobile
%{_kf5_appstreamdir}/org.kde.kalgebramobile.appdata.xml

%files lang -f %{name}.lang

%changelog
