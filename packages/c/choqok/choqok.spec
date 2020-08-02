#
# spec file for package choqok
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


Name:           choqok
Version:        1.7.0
Release:        0
Summary:        Micro-Blogging Client for KDE
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://choqok.kde.org
Source:         https://download.kde.org/stable/%{name}/1.7/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-retrieving-Twitter-conversations.patch
Patch1:         Link-to-the-original-post-for-retweets.patch
Patch2:         twitter-Dont-overwrite-contents-of-retweets.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Attica)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WebKit)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(TelepathyQt5)

%description
A micro-blogging client for the K Desktop Environment.
The name comes from an ancient Persian word which means Sparrow.
It currently supports twitter.com and identi.ca services.

%package devel
Summary:        Micro-Blogging Client for KDE
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
A micro-blogging client for the K Desktop Environment.
The name comes from an ancient Persian word which means Sparrow.
It currently supports twitter.com and identi.ca services.

%prep
%setup -q
%autopatch -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}
  %suse_update_desktop_file -C "KDE Micro-blogging Client" org.kde.choqok InstantMessaging
  %find_lang choqok

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc AUTHORS changelog README
%{_kf5_applicationsdir}/org.kde.choqok.desktop
%{_kf5_appsdir}/choqok/
%{_kf5_appsdir}/dbus-1/services/org.kde.choqok.service
%{_kf5_appstreamdir}/org.kde.choqok.appdata.xml
%{_kf5_bindir}/choqok
%{_kf5_configkcfgdir}/
%{_kf5_htmldir}/*
%{_kf5_iconsdir}/hicolor/*/actions/retweet.*
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_kxmlguidir}/*/
%{_kf5_libdir}/libchoqok.so.*
%{_kf5_libdir}/libgnusocialapihelper.so.*
%{_kf5_libdir}/libtwitterapihelper.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/choqok_*.so
%{_kf5_plugindir}/kcm_choqok_*.so
%{_kf5_plugindir}/kf5/parts/
%{_kf5_plugindir}/kf5/purpose/
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_servicesdir}/choqok*
%{_kf5_servicesdir}/konqchoqok.desktop
%{_kf5_servicetypesdir}/choqok*

%files devel
%{_kf5_appsdir}/cmake/modules/
%{_includedir}/choqok/
%{_kf5_libdir}/libchoqok.so
%{_kf5_libdir}/libgnusocialapihelper.so
%{_kf5_libdir}/libtwitterapihelper.so

%changelog
