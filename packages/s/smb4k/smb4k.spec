#
# spec file for package smb4k
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.0.0
%define qt6_version 6.6.2

Name:           smb4k
Version:        4.0.5
Release:        0
Summary:        Network Neighborhood Browser and Samba Share Mounting Utility
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/smb4k
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(KDSoapWSDiscoveryClient) >= 0.3.0
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= 6.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain) >= 0.14.2
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(smbclient)
Requires:       cifs-utils
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       libplasma6-components
Requires:       samba-client
Recommends:     rsync
Recommends:     smb4k-doc = %{version}

%description
Smb4K is an advanced network neighborhood browser and Samba share mounting
utility for the KDE Software Compilation. It scans your network neighborhood
for all available workgroups, servers and shares and can mount all desired
shares to your local file system.

%package doc
Summary:        Documentation for smb4k
Requires:       smb4k = %{version}

%description doc
Smb4K is an advanced network neighborhood browser and Samba share mounting
utility for the KDE Software Compilation. It scans your network neighborhood
for all available workgroups, servers and shares and can mount all desired
shares to your local file system.

This package provides the documentation for smb4k.

%lang_package

%prep
%autosetup -p1

# There are no changes between kdsoapwsdiscoveryclient 0.3 and 0.4 (needed for Leap 16)
sed -i 's#KDSoapWSDiscoveryClient 0\.4#KDSoapWSDiscoveryClient 0\.3#' CMakeLists.txt

%build
%cmake_kf6 \
  -DSMB4K_WITH_WS_DISCOVERY:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --all-name --with-html

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc AUTHORS BUGS ChangeLog README.md
%{_kf6_applicationsdir}/org.kde.smb4k.desktop
%{_kf6_appstreamdir}/org.kde.smb4k.appdata.xml
%if %{pkg_vcmp cmake(KF6Package) < 6.18}
%{_kf6_appstreamdir}/org.kde.smb4kqml.appdata.xml
%endif
%{_kf6_bindir}/smb4k
%{_kf6_configkcfgdir}/smb4k.kcfg
%{_kf6_dbuspolicydir}/org.kde.smb4k.mounthelper.conf
%{_kf6_iconsdir}/hicolor/*/apps/smb4k.png
%{_kf6_iconsdir}/oxygen/*/apps/smb4k.png
%{_kf6_libdir}/libsmb4kcore.so
%{_kf6_libdir}/libsmb4kdialogs.so
%{_kf6_libexecdir}/kauth/mounthelper
%{_kf6_notificationsdir}/smb4k.notifyrc
%{_kf6_plasmadir}/plasmoids/org.kde.smb4kqml/
%{_kf6_plugindir}/smb4kconfigdialog.so
%{_kf6_qmldir}/org/kde/smb4k/
%{_kf6_sharedir}/dbus-1/system-services/org.kde.smb4k.mounthelper.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.smb4k.mounthelper.policy

%files doc
%doc %lang(en) %{_kf6_htmldir}/en/smb4k/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/smb4k

%changelog
