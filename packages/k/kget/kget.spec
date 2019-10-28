#
# spec file for package kget
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
%bcond_without	lang
Name:           kget
Version:        19.08.2
Release:        0
Summary:        Download Manager
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gpgme-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  libktorrent-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  libqgpgme-devel
BuildRequires:  pkgconfig
BuildRequires:  solid-devel
BuildRequires:  sqlite-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Obsoletes:      kget5 < %{version}
Provides:       kget5 = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
An advanced download manager by KDE

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
  %suse_update_desktop_file -r org.kde.kget         System   TrayIcon

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC
%doc README
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/kget/
%{_kf5_applicationsdir}/org.kde.kget.desktop
%{_kf5_bindir}/kget
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kget.*
%{_kf5_libdir}/libkgetcore.so*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kget.service
%{_kf5_sharedir}/dolphinpart/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kget/
%{_kf5_sharedir}/khtml/
%{_kf5_sharedir}/kwebkitpart/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_appstreamdir}/org.kde.kget.appdata.xml
%{_kf5_debugdir}/kget.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
