#
# spec file for package kpat
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
Name:           kpat
Version:        19.08.0
Release:        0
Summary:        Patience card game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Card
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  freecell-solver-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       kdegames-carddecks-default
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KPatience is a collection of various patience games known all over the
world. It includes Klondike, Freecell, Yukon, Forty and Eight and many
more. The game has nice graphics and many different carddecks.

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
  %suse_update_desktop_file -r org.kde.kpat          Game CardGame

%post
%mime_database_post

%postun
%mime_database_postun

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
