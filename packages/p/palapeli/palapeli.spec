#
# spec file for package palapeli
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
Name:           palapeli
Version:        24.05.1
Release:        0
Summary:        Jigsaw puzzle game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/palapeli
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       palapeli-data = %{version}

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you are not
limited to aligning pieces on imaginary grids. The pieces are freely moveable.
Also, Palapeli features real persistency, i.e. everything you do is saved on
your disk immediately.

%package data
Summary:        Palapeli's standard puzzle files
Requires:       palapeli = %{version}
BuildArch:      noarch

%description data
This package contains the standard puzzle files for Palapeli.

%package devel
Summary:        Development package for Palapeli
Requires:       palapeli = %{version}

%description devel
This package contains the development files for Palapeli.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/palapeli/
%{_kf6_applicationsdir}/org.kde.palapeli.desktop
%{_kf6_appstreamdir}/org.kde.palapeli.appdata.xml
%{_kf6_bindir}/palapeli
%{_kf6_debugdir}/palapeli.categories
%{_kf6_iconsdir}/hicolor/*/apps/palapeli.png
%{_kf6_iconsdir}/hicolor/*/mimetypes/application-x-palapeli.png
%{_kf6_libdir}/libpala.so.*
%{_kf6_notificationsdir}/palapeli.notifyrc
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/palathumbcreator.so
%{_kf6_plugindir}/palapelislicers/
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/palapeli_servicemenu.desktop
%{_kf6_sharedir}/mime/packages/palapeli-mimetypes.xml

%files data
%{_kf6_sharedir}/palapeli/
%config %{_kf6_configdir}/palapeli-collectionrc

%files devel
%{_includedir}/Pala
%{_kf6_libdir}/libpala.so
%{_kf6_cmakedir}/Pala/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/palapeli/

%changelog
