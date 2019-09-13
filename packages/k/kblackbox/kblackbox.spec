#
# spec file for package kblackbox
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
Name:           kblackbox
Version:        19.08.1
Release:        0
Summary:        Logic game with elements of hide-and-seek
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
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
KBlackbox is a graphical logical game, inspired by emacs's blackbox. It
is a game of hide and seek played on an grid of boxes.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kblackbox-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kblackbox       Game BoardGame

%files
%license COPYING COPYING.DOC
%dir %{_kf5_appstreamdir}
%{_kf5_applicationsdir}/org.kde.kblackbox.desktop
%{_kf5_appsdir}/kblackbox/
%{_kf5_appstreamdir}/org.kde.kblackbox.appdata.xml
%{_kf5_bindir}/kblackbox
%doc %lang(en) %{_kf5_htmldir}/en/kblackbox/
%{_kf5_iconsdir}/hicolor/*/apps/kblackbox.*
%{_kf5_kxmlguidir}/kblackbox/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
