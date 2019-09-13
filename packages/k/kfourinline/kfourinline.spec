#
# spec file for package kfourinline
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
Name:           kfourinline
Version:        19.08.1
Release:        0
Summary:        Four Wins game
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Amusements/Toys/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdnssd-framework-devel
BuildRequires:  ki18n-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang

%description
Four wins is a two-player board game where you have to align four
(gravity-affected) pieces of the same colour to win.

%lang_package

%prep
%setup -q -n kfourinline-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kfourinline     Game BoardGame

%files
%license COPYING COPYING.DOC COPYING.LIB
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/kfourinline/
%{_kf5_applicationsdir}/org.kde.kfourinline.desktop
%{_kf5_appsdir}/kfourinline/
%{_kf5_bindir}/kfourinline
%{_kf5_bindir}/kfourinlineproc
%{_kf5_configkcfgdir}/kwin4.kcfg
%{_kf5_iconsdir}/hicolor/*/*/kfourinline.*
%{_kf5_debugdir}/kfourinline.categories
%{_kf5_appstreamdir}/org.kde.kfourinline.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
