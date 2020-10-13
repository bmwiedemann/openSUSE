#
# spec file for package ksystemlog
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
Name:           ksystemlog
Version:        20.08.2
Release:        0
Summary:        System Log Viewer Tool
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  oxygen5-icon-theme-large
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libsystemd)
Obsoletes:      ksystemlog5 < %{version}
Provides:       ksystemlog5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
This program is developed for use by beginner users, who do not know
how to find information about their Linux system and how the log files
are in their computer. But it is also designed for advanced users, who
want to quickly see problems occurring on their server.

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
  %suse_update_desktop_file org.kde.ksystemlog System Monitor
  for i in {16,22,32,48,64,128}; do
     mkdir -p %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
     cp %{_datadir}/icons/oxygen/base/"$i"x"$i"/apps/utilities-log-viewer.png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps/;
  done

%files
%license COPYING*
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/ksystemlog
%{_kf5_iconsdir}/hicolor/*/*/*.png
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_appstreamdir}/org.kde.ksystemlog.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
