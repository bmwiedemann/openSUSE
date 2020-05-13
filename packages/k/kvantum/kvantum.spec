#
# spec file for package kvantum
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


Name:           kvantum
Version:        0.15.3
Release:        1
Summary:        SVG-based theme engine for Qt5
License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/Kvantum
Source0:        https://github.com/tsujan/Kvantum/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kwindowsystem-devel
BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  update-desktop-files
%description
Kvantum is an SVG-based theme engine for Qt, tuned to Plasma and LXQt, with an emphasis on elegance, usability and practicality.
Its homepage is https://github.com/tsujan/Kvantum.

Kvantum also comes with extra themes that can be selected and activated by using Kvantum Manager.

%package qt5
Summary:        SVG-based theme engine for Qt5

%description qt5
Kvantum is an SVG-based theme engine for Qt, tuned to Plasma and LXQt, with an emphasis on elegance, usability and practicality.
Its homepage is https://github.com/tsujan/Kvantum.

Kvantum also comes with extra themes that can be selected and activated by using Kvantum Manager.

This package provides Kvantum theme engine for Qt5.

%package manager
Summary:        GUI for installing, selecting and manipulating Kvantum themes
Requires:       %{name}-qt5 = %{version}

%description manager
This package provides configuration manager - GUI appligation for installing, selecting and manipulating Kvantum themes.

%package manager-lang
Summary:        Translations for Kvantum manager
Requires:       %{name}-manager = %{version}
BuildArch:      noarch

%description manager-lang

This package provides translations for Kvantum manager.

%package doc
Summary:        Documentation for Kvantum engine
BuildArch:      noarch

%description doc
This package provides instructions on how to change configuration or make new themes for Kvantum engine.

%package themes
Summary:        Themes for Kvantum engine
Requires:       %{name}-qt5 = %{version}
BuildArch:      noarch

%description themes

This package provides extra themes for Kvantum engine.

%package openbox-themes
Summary:        Openbox themes for Kvantum engine
BuildArch:      noarch

%description openbox-themes

This package provides extra Openbox themes for Kvantum engine.

%prep
%setup -q -n Kvantum-%{version}

%build
pushd Kvantum
%cmake
%cmake_build

%install
pushd Kvantum
%cmake_install
%fdupes %{buildroot}%{_datadir}/themes
%suse_update_desktop_file kvantummanager Utility Settings DesktopSettings X-XFCE-SettingsDialog X-XFCE-PersonalSettings X-GNOME-PersonalSettings

%files qt5
%dir %{_libdir}/qt5/plugins/styles
%{_libdir}/qt5/plugins/styles/*
%license Kvantum/COPYING
%doc Kvantum/README.md

%files manager
%{_bindir}/*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg

%files manager-lang
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantummanager/translations
%dir %{_datadir}/kvantumpreview/translations
%{_datadir}/kvantummanager/translations/*
%{_datadir}/kvantumpreview/translations/*

%files doc

%doc Kvantum/doc/*

%files themes
%exclude %{_datadir}/kde4/apps/color-schemes/*
%dir %{_datadir}/color-schemes/
%dir %{_datadir}/Kvantum
%dir %{_datadir}/Kvantum/Kv*
%{_datadir}/color-schemes/*
%{_datadir}/Kvantum/Kv*/*

%files openbox-themes
%dir %{_datadir}/themes/Kv*
%dir %{_datadir}/themes/Kv*/openbox-3
%{_datadir}/themes/Kv*/openbox-3/*

%changelog
