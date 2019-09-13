#
# spec file for package kalgebra
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           kalgebra
Version:        19.08.1
Release:        0
Summary:        Math Expression Solver and Plotter
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  analitza-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(glu)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KAlgebra is a math expression solver and plotter.

%package mobile
Summary:        Math Expression Solver and Plotter - mobile version
Group:          Productivity/Scientific/Math
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-lang

%description mobile
KAlgebra is a math expression solver and plotter. This package includes
a QtQuick based version for use in mobile (phone, tablet) environments.

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
    %{kf5_find_htmldocs}
  %endif
  %fdupes -s %{buildroot}

%files
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kalgebra.desktop
%{_kf5_appstreamdir}/org.kde.kalgebra.appdata.xml
%{_kf5_bindir}/calgebra
%{_kf5_bindir}/kalgebra
%doc %lang(en) %{_kf5_htmldir}/en/kalgebra
%{_kf5_iconsdir}/hicolor/*/apps/kalgebra.*
%{_kf5_plasmadir}/
%{_kf5_servicesdir}
%{_kf5_sharedir}/katepart5

%files mobile
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kalgebramobile.desktop
%{_kf5_bindir}/kalgebramobile
%{_kf5_sharedir}/kalgebramobile/
%{_kf5_appstreamdir}/org.kde.kalgebramobile.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
