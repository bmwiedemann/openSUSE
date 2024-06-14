#
# spec file for package kalzium
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
Name:           kalzium
Version:        24.05.1
Release:        0
Summary:        Periodic Table of Elements
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  ocaml
BuildRequires:  ocaml-facile-devel
BuildRequires:  openbabel-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Plotting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UnitConversion) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(chemical-mime-data)
BuildRequires:  pkgconfig(eigen3)

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
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kalzium/
%doc %lang(en) %{_kf6_mandir}/man1/kalzium.1%{ext_man}
%{_kf6_applicationsdir}/org.kde.kalzium.desktop
%{_kf6_applicationsdir}/org.kde.kalzium_cml.desktop
%{_kf6_appstreamdir}/org.kde.kalzium.appdata.xml
%{_kf6_bindir}/kalzium
%{_kf6_configkcfgdir}/kalzium.kcfg
%{_kf6_debugdir}/kalzium.categories
%{_kf6_iconsdir}/hicolor/*/apps/kalzium.*
%{_kf6_libdir}/libscience.so.*
%{_kf6_sharedir}/kalzium/
%{_kf6_sharedir}/libkdeedu/

%files devel
%{_includedir}/libkdeedu/
%{_kf6_libdir}/libscience.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kalzium/

%changelog
