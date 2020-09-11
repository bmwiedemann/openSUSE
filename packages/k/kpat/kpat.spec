#
# spec file for package kpat
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
%bcond_without lang
Name:           kpat
Version:        20.08.1
Release:        0
Summary:        Patience card game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Card
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  freecell-solver-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kdegames-carddecks-default
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
KPatience is a collection of various patience games known all over the
world. It includes Klondike, Freecell, Yukon, Forty and Eight and many
more. The game has nice graphics and many different carddecks.

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
  %suse_update_desktop_file -r org.kde.kpat          Game CardGame

%files
%license COPYING COPYING.DOC
%config %{_kf5_configdir}/kcardtheme.knsrc
%config %{_kf5_configdir}/kpat.knsrc
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/24x24/apps
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_iconsdir}/hicolor/64x64
%dir %{_kf5_iconsdir}/hicolor/64x64/apps
%doc %lang(en) %{_kf5_htmldir}/en/kpat/
%{_kf5_applicationsdir}/org.kde.kpat.desktop
%{_kf5_appstreamdir}/org.kde.kpat.appdata.xml
%{_kf5_appsdir}/kpat/
%{_kf5_bindir}/kpat
%{_kf5_configkcfgdir}/kpat.kcfg
%{_kf5_iconsdir}/hicolor/*/*/kpat.*
%{_kf5_kxmlguidir}/kpat/
%{_kf5_libdir}/libkcardgame.so
%{_kf5_mandir}/man6/kpat.6.gz
%{_kf5_sharedir}/mime/packages/kpatience.xml
%{_kf5_debugdir}/kpat.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
