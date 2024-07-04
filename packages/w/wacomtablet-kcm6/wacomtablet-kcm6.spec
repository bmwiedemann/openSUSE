#
# spec file for package wacomtablet-kcm6
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname wacomtablet
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
# wacomtablet is too generic for this package
Name:           wacomtablet-kcm6
Version:        6.1.2
Release:        0
Summary:        Wacom drivers KCM
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/wacomtablet
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xorg-wacom)
# Used by the .desktop file
Requires:       systemsettings6
Supplements:    (xf86-input-wacom and plasma6-workspace)
Provides:       kcm_tablet = %{version}
Obsoletes:      kcm_tablet < %{version}
Obsoletes:      kcm_tablet-lang < %{version}

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button / pen layouts per profile.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%files
%license COPYING
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol/
%{_kf6_appstreamdir}/org.kde.plasma.wacomtablet.appdata.xml
%{_kf6_appstreamdir}/org.kde.wacomtablet.metainfo.xml
%{_kf6_applicationsdir}/kcm_wacomtablet.desktop
%{_kf6_applicationsdir}/kde_wacom_tabletfinder.desktop
%{_kf6_bindir}/kde_wacom_tabletfinder
%{_kf6_debugdir}/wacomtablet.categories
%{_kf6_dbusinterfacesdir}/org.kde.Wacom.xml
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.wacomtablet/
%dir %{_kf6_sharedir}/plasma5support/
%dir %{_kf6_sharedir}/plasma5support/services
%{_kf6_sharedir}/plasma5support/services/wacomtablet.operations
%{_kf6_plugindir}/kf6/kded/wacomtablet.so
%dir %{_kf6_plugindir}/plasma5support
%dir %{_kf6_plugindir}/plasma5support/dataengine
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_wacomtablet.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_wacomtablet.so
%{_kf6_sharedir}/wacomtablet/
%{_kf6_notificationsdir}/wacomtablet.notifyrc

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol/

%changelog
