#
# spec file for package ksirk
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
Name:           ksirk
Version:        24.05.2
Release:        0
Summary:        Risk-like game by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ksirk
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6)
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      ksirk5 < %{version}
Provides:       ksirk5 = %{version}

%description
KsirK is a computerized version of a well known strategy game.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license COPYING COPYING.DOC COPYING.LIB
%doc %lang(en) %{_kf6_htmldir}/en/ksirk/
%doc %lang(en) %{_kf6_htmldir}/en/ksirkskineditor/
%{_kf6_applicationsdir}/org.kde.ksirk.desktop
%{_kf6_applicationsdir}/org.kde.ksirkskineditor.desktop
%{_kf6_appstreamdir}/org.kde.ksirk.appdata.xml
%{_kf6_bindir}/ksirk
%{_kf6_bindir}/ksirkskineditor
%{_kf6_configkcfgdir}/ksirksettings.kcfg
%{_kf6_configkcfgdir}/ksirkskineditorsettings.kcfg
%{_kf6_debugdir}/ksirk.categories
%{_kf6_iconsdir}/hicolor/*/apps/ksirk.*
%{_kf6_knsrcfilesdir}/ksirk.knsrc
%{_kf6_sharedir}/ksirk/
%{_kf6_sharedir}/ksirkskineditor/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ksirk/
%exclude %{_kf6_htmldir}/en/ksirkskineditor/

%changelog
