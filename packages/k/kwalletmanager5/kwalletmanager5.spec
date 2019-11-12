#
# spec file for package kwalletmanager5
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


%define rname   kwalletmanager
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kwalletmanager5
Version:        19.08.3
Release:        0
Summary:        Wallet Management Tool
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  karchive-devel
BuildRequires:  kauth-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  knotifications-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwallet-framework-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Recommends:     %{name}-lang
Provides:       kwalletmanager = %{version}
Obsoletes:      kwalletmanager < %{version}

%description
This application allows you to manage your KDE password wallet.

%lang_package

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/*kwalletmanager5*.desktop
%{_kf5_bindir}/kwalletmanager5
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_libdir}/libexec/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_kf5_dbuspolicydir}/org.kde.kcontrol.kcmkwallet5.conf
%{_kf5_appstreamdir}/org.kde.kwalletmanager5.appdata.xml
%{_kf5_debugdir}/kwalletmanager.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
