#
# spec file for package kopete
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 16.08 in KA, but 16.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kopete
Version:        22.12.1
Release:        0
Summary:        Instant Messenger
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kopete
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  giflib-devel
BuildRequires:  libgadu-devel
BuildRequires:  libidn-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  libv4l-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  meanwhile-devel
BuildRequires:  openslp-devel
BuildRequires:  pkgconfig
BuildRequires:  speex-devel
BuildRequires:  sqlite-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libotr) >= 4.0.0
BuildRequires:  pkgconfig(libsrtp)
%if 0%{?is_opensuse} || !0%{?sle_version}
BuildRequires:  mediastreamer2-devel
%endif
%if 0%{?is_opensuse} || !0%{?sle_version}
BuildRequires:  pkgconfig(ortp) >= 0.22
%endif

%description
Kopete is the KDE instant messenger and supports multiple protocols.

%package devel
Summary:        Instant Messenger - Development Files
Requires:       kopete >= %{version}

%description devel
Kopete is the KDE instant messenger and supports multiple protocols.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file org.kde.kopete Network InstantMessaging

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/kopete/
%{_kf5_applicationsdir}/org.kde.kopete.desktop
%{_kf5_appsdir}/kconf_update/
%{_kf5_appsdir}/kopete_history/
%{_kf5_appstreamdir}/org.kde.kopete.appdata.xml
%{_kf5_bindir}/kopete
%{_kf5_bindir}/winpopup-*
%{_kf5_configdir}/kopeterc
%{_kf5_configkcfgdir}/
%{_kf5_debugdir}/kopete.categories
%{_kf5_iconsdir}/hicolor/*/*/
%{_kf5_iconsdir}/oxygen/*/*/
%{_kf5_kxmlguidir}/kopete*/
%{_kf5_libdir}/libkopete*.so.*
%{_kf5_libdir}/libkopete.so.*
%{_kf5_libdir}/liboscar.so.*
%{_kf5_libdir}/libqgroupwise.so
%{_kf5_notifydir}/kopete.notifyrc
%{_kf5_plugindir}/accessible/
%{_kf5_plugindir}/chattexteditpart.so
%{_kf5_plugindir}/kcm_kopete_*.so
%{_kf5_plugindir}/kopete_*.so
%{_kf5_servicesdir}/*.desktop
%{_kf5_servicesdir}/*.protocol
%{_kf5_servicesdir}/kconfiguredialog/
%{_kf5_servicetypesdir}/*.desktop
%{_kf5_sharedir}/dbus-1/interfaces/
%{_kf5_sharedir}/kopete/
%{_kf5_sharedir}/sounds/*.ogg

%files devel
%{_includedir}/kopete/
%{_kf5_libdir}/libkopete.so
%{_kf5_libdir}/libkopete*.so
%{_kf5_libdir}/liboscar.so

%files lang -f %{name}.lang

%changelog
