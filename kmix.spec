#
# spec file for package kmix
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kmix
Version:        22.12.1
Release:        0
Summary:        Sound Mixer
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kmix
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  glib2-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libcanberra-devel
BuildRequires:  libpulse-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
KMix is a fully featured audio mixer by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kmix AudioVideo Mixer

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%config %{_kf5_configdir}/autostart/*kmix*.desktop
%doc %lang(en) %{_kf5_htmldir}/en/kmix/
%{_kf5_applicationsdir}/*kmix*.desktop
%{_kf5_appstreamdir}/org.kde.kmix.appdata.xml
%{_kf5_bindir}/kmix*
%{_kf5_configkcfgdir}/kmixsettings.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kmix.*
%{_kf5_debugdir}/kmix.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kmix/
%{_kf5_notifydir}/kmix.notifyrc
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/kmix/
%{_libdir}/libkmixcore.so.*

%files lang -f %{name}.lang

%changelog
