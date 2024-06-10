#
# spec file for package kvantum
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define dsc_suffix Qt6
%endif
%if "%{flavor}" == "qt5"
%define qt5 1
%define pkg_suffix -qt5
%define dsc_suffix Qt5
%endif
Name:           kvantum%{?pkg_suffix}
Version:        1.1.2
Release:        0
Summary:        SVG-based theme engine for Qt5 and Qt6
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/tsujan/Kvantum
Source0:        https://github.com/tsujan/Kvantum/archive/V%{version}.tar.gz#/kvantum-%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?qt5}
BuildRequires:  kwindowsystem-devel
BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  cmake(Qt5Core) > 5.15
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
%if 0%{?qt6}
BuildRequires:  fdupes
%if 0%{?suse_version} > 1600
BuildRequires:  kf6-kwindowsystem-devel
%endif
BuildRequires:  qt6-linguist-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
%endif

%description
Kvantum is an SVG-based theme engine for Qt, tuned to Plasma and LXQt, with an emphasis on elegance, usability and practicality.
Its homepage is https://github.com/tsujan/Kvantum.

Kvantum also comes with extra themes that can be selected and activated by using Kvantum Manager.

This package provides Kvantum theme engine for %{dsc_suffix}.

%package -n kvantum-manager
Summary:        GUI for installing, selecting and manipulating Kvantum themes
Requires:       kvantum-qt6 = %{version}

%description -n kvantum-manager
This package provides configuration manager - GUI appligation for installing, selecting and manipulating Kvantum themes.

%package -n kvantum-manager-lang
Summary:        Translations for Kvantum manager
Requires:       kvantum-manager = %{version}
BuildArch:      noarch

%description -n kvantum-manager-lang

This package provides translations for Kvantum manager.

%package -n kvantum-doc
Summary:        Documentation for Kvantum engine
BuildArch:      noarch

%description -n kvantum-doc
This package provides instructions on how to change configuration or make new themes for Kvantum engine.

%package -n kvantum-themes
Summary:        Themes for Kvantum engine
Requires:       (kvantum-qt6 = %{version} or kvantum-qt5 = %{version})
BuildArch:      noarch

%description -n kvantum-themes

This package provides extra themes for Kvantum engine.

%package -n kvantum-openbox-themes
Summary:        Openbox themes for Kvantum engine
BuildArch:      noarch

%description -n kvantum-openbox-themes

This package provides extra Openbox themes for Kvantum engine.

%prep
%setup -q -n Kvantum-%{version}

%build

pushd Kvantum
%if 0%{?qt5}
%cmake -DENABLE_QT5=ON
%cmake_build
%endif
%if 0%{?qt6}
%if 0%{?suse_version} > 1600
%cmake_qt6
%else
%cmake_qt6 -DWITHOUT_KF=ON
%endif
%{qt6_build}
%endif

%install
pushd Kvantum
%if 0%{?qt5}
%cmake_install
%endif
%if 0%{?qt6}
%{qt6_install}
%endif

%if 0%{?qt6}
%fdupes %{buildroot}%{_datadir}/themes
%suse_update_desktop_file kvantummanager Utility Settings DesktopSettings X-XFCE-SettingsDialog X-XFCE-PersonalSettings X-GNOME-PersonalSettings
%endif

%files
%dir %{_libdir}/%{flavor}/plugins/styles
%{_libdir}/%{flavor}/plugins/styles/*
%license Kvantum/COPYING
%doc Kvantum/README.md

%if 0%{?qt6}
%files -n kvantum-manager
%{_bindir}/*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg

%files -n kvantum-manager-lang
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantummanager/translations
%dir %{_datadir}/kvantumpreview/translations
%{_datadir}/kvantummanager/translations/*
%{_datadir}/kvantumpreview/translations/*

%files -n kvantum-doc

%doc Kvantum/doc/*

%files -n kvantum-themes
%exclude %{_datadir}/kde4/apps/color-schemes/*
%dir %{_datadir}/color-schemes/
%dir %{_datadir}/Kvantum
%dir %{_datadir}/Kvantum/Kv*
%{_datadir}/color-schemes/*
%{_datadir}/Kvantum/Kv*/*
%endif

%changelog
