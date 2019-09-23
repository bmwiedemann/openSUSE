#
# spec file for package kfind
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


%define kf5_version 5.28.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kfind
Version:        19.08.1
Release:        0
Summary:        KDE Find File Utility
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  karchive-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kfilemetadata5-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang

%description
KFind allows you to search for directories and files.

%lang_package

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

  %suse_update_desktop_file org.kde.kfind          System Filesystem core

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING*
%{_kf5_debugdir}/*.categories
%dir %{_kf5_appstreamdir}
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/kfind/
%doc %{_kf5_mandir}/man1/kfind.*
%{_kf5_applicationsdir}/org.kde.kfind.desktop
%{_kf5_appstreamdir}/org.kde.kfind.appdata.xml
%{_kf5_bindir}/kfind
%{_kf5_iconsdir}/hicolor/*/apps/kfind.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
