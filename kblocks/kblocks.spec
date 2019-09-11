#
# spec file for package kblocks
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
Name:           kblocks
Version:        19.08.1
Release:        0
Summary:        A classic falling blocks game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Real Time
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KBlocks is the KDE version of the classic falling blocks game.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kblocks-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%files
%license COPYING COPYING.DOC
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%{_kf5_applicationsdir}/org.kde.kblocks.desktop
%{_kf5_appsdir}/kblocks/
%{_kf5_appstreamdir}/org.kde.kblocks.appdata.xml
%{_kf5_bindir}/kblocks
%config %{_kf5_configdir}/kblocks.knsrc
%{_kf5_configkcfgdir}/kblocks.kcfg
%doc %lang(en) %{_kf5_htmldir}/en/kblocks/
%{_kf5_iconsdir}/hicolor/*/*/kblocks.*
%{_kf5_kxmlguidir}/kblocks/
%{_kf5_debugdir}/kblocks.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
