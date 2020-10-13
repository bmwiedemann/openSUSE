#
# spec file for package ksirk
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without	lang
Name:           ksirk
Version:        20.08.2
Release:        0
Summary:        Risk-like game by KDE
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  libqca-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      ksirk5 < %{version}
Provides:       ksirk5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
KsirK is a computerized version of a well known strategy game.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
  rm %{buildroot}%{_kf5_libdir}/libiris_ksirk.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC COPYING.LIB
%config %{_kf5_configdir}/ksirk.knsrc
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/ksirk/
%doc %lang(en) %{_kf5_htmldir}/en/ksirkskineditor/
%{_kf5_applicationsdir}/org.kde.ksirk.desktop
%{_kf5_applicationsdir}/org.kde.ksirkskineditor.desktop
%{_kf5_appstreamdir}/org.kde.ksirk.appdata.xml
%{_kf5_bindir}/ksirk
%{_kf5_bindir}/ksirkskineditor
%{_kf5_configkcfgdir}/ksirk*.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/ksirk.*
%{_kf5_kxmlguidir}/ksirk/
%{_kf5_kxmlguidir}/ksirkskineditor/
%{_kf5_libdir}/libiris_ksirk.so.*
%{_kf5_sharedir}/ksirk/
%{_kf5_sharedir}/ksirkskineditor/
%{_kf5_debugdir}/ksirk.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
