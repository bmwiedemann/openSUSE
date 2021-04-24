#
# spec file for package khelpcenter5
#
# Copyright (c) 2021 SUSE LLC
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


%define rname khelpcenter
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           khelpcenter5
Version:        21.04.0
Release:        0
Summary:        KDE Documentation Application
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://apps.kde.org/help
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libxapian-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
# khelpcenter uses some images and stylesheets from kdoctools (boo#1011094)
Requires:       kdoctools
Recommends:     %{name}-lang
Conflicts:      kdebase4-runtime < 17.04.1
Provides:       suse_help_viewer

%description
Application to show KDE Applications' documentation.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=share/locale/kf5
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %{kf5_find_lang}
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file    org.kde.Help          Documentation Viewer

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc README*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.Help.desktop
%{_kf5_appstreamdir}/org.kde.Help.appdata.xml
%{_kf5_bindir}/khelpcenter
%{_kf5_configkcfgdir}/khelpcenter.kcfg
%{_kf5_debugdir}/khelpcenter.categories
%{_kf5_kxmlguidir}/khelpcenter/
%{_kf5_libdir}/libexec/khc_*
%{_kf5_libdir}/libkdeinit5_khelpcenter.so
%{_kf5_servicesdir}/
%{_kf5_sharedir}/kde4/
%{_kf5_sharedir}/khelpcenter/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
