#
# spec file for package calligra-plan
#
# Copyright (c) 2021 SUSE LLC
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


Name:           calligra-plan
Version:        3.3.0
Release:        0
Summary:        Project Management Application
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.calligra.org/
Source0:        https://download.kde.org/stable/calligra/%{version}/calligraplan-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  perl-base
BuildRequires:  cmake(KChart) >= 2.8.0
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KGantt) >= 2.8.0
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
# For mimetype definitions
Requires:       kcoreaddons
# some icons were part of the main calligra package before 3.1.0
Conflicts:      calligra < 3.1.0
Obsoletes:      calligra5-plan

%description
Plan is the project management application of the Calligra Suite.

%lang_package

%prep
%autosetup -p1 -n calligraplan-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build
%kf5_find_lang %{name}
%kf5_find_htmldocs

# not needed
rm %{buildroot}/%{_kf5_libdir}/libplan*.so

%ldconfig_scriptlets

%files
%license COPYING*
%doc CHANGELOG
%config %{_kf5_configdir}/calligra*rc
%{_kf5_applicationsdir}/org.kde.calligraplan.desktop
%{_kf5_applicationsdir}/org.kde.calligraplanwork.desktop
%{_kf5_appstreamdir}/org.kde.calligraplan.appdata.xml
%{_kf5_bindir}/calligraplan
%{_kf5_bindir}/calligraplanwork
%dir %{_kf5_configkcfgdir}
%{_kf5_configkcfgdir}/calligraplan*.kcfg
%doc %lang(en) %{_kf5_htmldir}/en
%{_kf5_iconsdir}/hicolor/
%{_kf5_kxmlguidir}/calligraplan/
%{_kf5_kxmlguidir}/calligraplanwork/
%{_kf5_libdir}/libkdeinit5_calligraplan*.so
%{_kf5_libdir}/libplan*.so.*
%{_kf5_plugindir}/calligraplan/
%{_kf5_plugindir}/calligraplanworkpart.so
%{_kf5_sharedir}/calligraplan/
%{_kf5_sharedir}/calligraplanwork/

%files lang -f %{name}.lang

%changelog
