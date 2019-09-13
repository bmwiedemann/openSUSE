#
# spec file for package choqok
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


Name:           choqok
Version:        1.6.0
Release:        0
Summary:        Micro-Blogging Client for KDE
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/1.6/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-build-with-Qt-5_13.patch
BuildRequires:  attica-qt5-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kcmutils-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdewebkit-devel
BuildRequires:  kemoticons-devel
BuildRequires:  kglobalaccel-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  qoauth-qt5-devel
BuildRequires:  sonnet-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)

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
%autosetup -p1

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
%doc AUTHORS changelog README TODO
%dir %{_kf5_appstreamdir}
%{_datadir}/config.kcfg/
%{_datadir}/knotifications5/
%{_kf5_applicationsdir}/org.kde.choqok.desktop
%{_kf5_appsdir}/choqok/
%{_kf5_appsdir}/dbus-1
%{_kf5_appstreamdir}/org.kde.choqok.appdata.xml
%{_kf5_bindir}/choqok
%{_kf5_htmldir}/*
%{_kf5_iconsdir}/hicolor/*/actions/retweet.*
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_kxmlguidir}/*/
%{_kf5_libdir}/libchoqok.so.*
%{_kf5_libdir}/libgnusocialapihelper.so.*
%{_kf5_libdir}/libtwitterapihelper.so.*
%{_kf5_plugindir}/choqok_*.so
%{_kf5_plugindir}/kcm_choqok_*.so
%{_kf5_plugindir}/kf5/parts/
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
