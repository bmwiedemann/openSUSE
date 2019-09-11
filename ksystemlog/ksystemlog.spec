#
# spec file for package ksystemlog
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
Name:           ksystemlog
Version:        19.08.0
Release:        0
Summary:        System Log Viewer Tool
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kdelibs4support-devel
BuildRequires:  oxygen5-icon-theme-large
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(libsystemd)
Obsoletes:      ksystemlog5 < %{version}
Provides:       ksystemlog5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This program is developed for use by beginner users, who do not know
how to find information about their Linux system and how the log files
are in their computer. But it is also designed for advanced users, who
want to quickly see problems occurring on their server.

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
  %suse_update_desktop_file org.kde.ksystemlog System Monitor
  for i in {16,22,32,48,64,128}; do
     mkdir -p %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
     cp %{_datadir}/icons/oxygen/base/"$i"x"$i"/apps/utilities-log-viewer.png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps/;
%else
     cp %{_datadir}/icons/oxygen/"$i"x"$i"/apps/utilities-log-viewer.png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps/;
%endif
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
