#
# spec file for package kalzium
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
Name:           kalzium
Version:        22.12.1
Release:        0
Summary:        Periodic Table of Elements
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  eigen3-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gettext-devel
BuildRequires:  glew-devel
BuildRequires:  libopenbabel-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-facile-devel
BuildRequires:  oxygen5-icon-theme-large
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(KF5UnitConversion)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)

%description
Kalzium shows a periodic table of the elements.

%package devel
Summary:        Periodic Table of Elements
Requires:       kalzium = %{version}

%description devel
Kalzium shows a periodic table of the elements.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc %lang(en) %{_kf5_htmldir}/en/kalzium/
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.kalzium.desktop
%{_kf5_applicationsdir}/org.kde.kalzium_cml.desktop
%{_kf5_appstreamdir}/org.kde.kalzium.appdata.xml
%{_kf5_bindir}/kalzium
%{_kf5_configkcfgdir}/
%{_kf5_debugdir}/kalzium.categories
%{_kf5_iconsdir}/hicolor/*/apps/kalzium.*
%{_kf5_libdir}/libscience.so.*
%{_kf5_mandir}/man1/kalzium.1%{ext_man}
%{_kf5_sharedir}/kalzium/
%{_kf5_sharedir}/libkdeedu/

%files devel
%{_includedir}/libkdeedu/
%{_kf5_libdir}/libscience.so

%files lang -f %{name}.lang

%changelog
