#
# spec file for package kalgebra
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


# Internal QML imports
%global __requires_exclude qt6qmlimport\\((widgets|org\\.kde\\.kalgebra\\.mobile).*

%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define plasma6_version 5.27.80

%bcond_without released
Name:           kalgebra
Version:        24.05.1
Release:        0
Summary:        Math Expression Solver and Plotter
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  readline-devel
BuildRequires:  cmake(Analitza6)
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Obsoletes:      kalgebra5 < %{version}
Provides:       kalgebra5 = %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
KAlgebra is a math expression solver and plotter.

%package mobile
Summary:        Math Expression Solver and Plotter - mobile version
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}

%description mobile
KAlgebra is a math expression solver and plotter. This package includes
a QtQuick based version for use in mobile (phone, tablet) environments.

%lang_package
%lang_package -n %{name}-mobile

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kalgebra --with-html
%find_lang kalgebramobile

# 'nothing provides qt6qmlimport(org.kde.plasma.components.2) needed by kalgebra'
rm -r %{buildroot}%{_kf6_plasmadir}/plasmoids/org.kde.graphsplasmoid/

%fdupes %{buildroot}

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/kalgebra
%{_kf6_applicationsdir}/org.kde.kalgebra.desktop
%{_kf6_appstreamdir}/org.kde.kalgebra.appdata.xml
%{_kf6_appstreamdir}/org.kde.graphsplasmoid.appdata.xml
%{_kf6_bindir}/calgebra
%{_kf6_bindir}/kalgebra
%{_kf6_iconsdir}/hicolor/*/apps/kalgebra.*
%dir %{_kf6_sharedir}/katepart5
%dir %{_kf6_sharedir}/katepart5/syntax
%{_kf6_sharedir}/katepart5/syntax/kalgebra.xml

%files mobile
%license COPYING*
%{_kf6_applicationsdir}/org.kde.kalgebramobile.desktop
%{_kf6_bindir}/kalgebramobile
%{_kf6_appstreamdir}/org.kde.kalgebramobile.appdata.xml

%files lang -f kalgebra.lang
%exclude %{_kf6_htmldir}/en/kalgebra

%files mobile-lang -f kalgebramobile.lang

%changelog
