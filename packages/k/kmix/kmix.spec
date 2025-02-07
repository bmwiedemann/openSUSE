#
# spec file for package kmix
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


%define kf6_version 6.1.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kmix
Version:        24.12.2
Release:        0
Summary:        Sound Mixer
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kmix
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
Obsoletes:      kmix5 < %{version}
Provides:       kmix5 = %{version}

%description
KMix is a fully featured audio mixer by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION:STRING=6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license COPYING*
%config %{_kf6_configdir}/autostart/kmix_autostart.desktop
%config %{_kf6_configdir}/autostart/restore_kmix_volumes.desktop
%doc %lang(en) %{_kf6_htmldir}/en/kmix/
%{_kf6_applicationsdir}/org.kde.kmix.desktop
%{_kf6_appstreamdir}/org.kde.kmix.appdata.xml
%{_kf6_bindir}/kmix
%{_kf6_bindir}/kmixctrl
%{_kf6_bindir}/kmixremote
%{_kf6_configkcfgdir}/kmixsettings.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.kmix.*
%{_kf6_debugdir}/kmix.categories
%{_kf6_iconsdir}/hicolor/*/actions/kmix.png
%{_kf6_kxmlguidir}/kmix/
%{_kf6_libdir}/libkmixcore.so.*
%{_kf6_notificationsdir}/kmix.notifyrc
%{_kf6_sharedir}/kmix/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kmix/

%changelog
