#
# spec file for package plasma-nm5
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


%bcond_without released
%define mm_support 1
Name:           plasma-nm5
Version:        5.26.4
Release:        0
Summary:        Plasma applet written in QML for managing network connections
License:        (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-nm-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-nm-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  NetworkManager-devel >= 0.9.8.4
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion) >= 5.98.0
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qca-qt5) >= 2.1.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(openconnect) >= 5.2
Requires:       NetworkManager
Requires:       kded
Requires:       kirigami2
Requires:       kwalletd5
Requires:       prison-qt5-imports
Recommends:     %{name}-lang
Recommends:     mobile-broadband-provider-info
Provides:       NetworkManager-client
Provides:       plasma-nm-kf5 = %{version}
Obsoletes:      plasma-nm-kf5 < %{version}
# Merged into the core in 5.15.80
Provides:       %{name}-wireguard = %{version}
Obsoletes:      %{name}-wireguard < %{version}
Provides:       plasma-nm = %{version}
Obsoletes:      plasma-nm < %{version}
%if 0%{?mm_support}
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0
%endif
Obsoletes:      NetworkManager-kde4-devel
Obsoletes:      NetworkManager-kde4-libs
Obsoletes:      NetworkManager-kde4-libs-lang
Obsoletes:      NetworkManager-novellvpn-kde4
Obsoletes:      plasmoid-networkmanagement
Supplements:    packageand(plasma5-desktop:NetworkManager)

%description
Plasma applet for controlling network connections on systems
that use the NetworkManager service.

%package openvpn
Summary:        OpenVPN support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-openvpn
Supplements:    packageand(%{name}:NetworkManager-openvpn)
Provides:       NetworkManager-openvpn-frontend
Provides:       plasma-nm-openvpn = %{version}
Obsoletes:      NetworkManager-openvpn-kde4
Obsoletes:      plasma-nm-openvpn < %{version}

%description openvpn
OpenVPN plugin for plasma-nm components.

%package vpnc
Summary:        vpnc support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-vpnc
Supplements:    packageand(%{name}:NetworkManager-vpnc)
Provides:       NetworkManager-vpnc-frontend
Provides:       plasma-nm-vpnc = %{version}
Obsoletes:      NetworkManager-vpnc-kde4
Obsoletes:      plasma-nm-vpnc < %{version}

%description vpnc
vpnc plugin for plasma-nm components.

%package openconnect
Summary:        OpenConnect support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-openconnect
Requires:       openconnect
Supplements:    packageand(%{name}:NetworkManager-openconnect)
Provides:       NetworkManager-openconnect-frontend
Provides:       plasma-nm-openconnect = %{version}
Obsoletes:      NetworkManager-openconnect-kde4
Obsoletes:      plasma-nm-openconnect < %{version}

%description openconnect
OpenConnect plugin for plasma-nm components.

%package libreswan
Summary:        Libreswan support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-libreswan
Supplements:    packageand(%{name}:NetworkManager-libreswan)
Provides:       NetworkManager-libreswan-frontend
# Old names
Provides:       plasma-nm-openswan = %{version}
Obsoletes:      plasma-nm-openswan < %{version}
Provides:       %{name}-openswan = %{version}
Obsoletes:      %{name}-openswan < %{version}

%description libreswan
Libreswan plugin for plasma-nm components.

%package strongswan
Summary:        strongSwan support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-strongswan
Supplements:    packageand(%{name}:NetworkManager-strongswan)
Provides:       NetworkManager-strongswan-frontend
Provides:       plasma-nm-strongswan = %{version}
Obsoletes:      plasma-nm-strongswan < %{version}

%description strongswan
strongSwan plugin for plasma-nm components.

%package l2tp
Summary:        L2TP support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-l2tp
Supplements:    packageand(%{name}:NetworkManager-l2tp)
Provides:       NetworkManager-l2tp-frontend
Provides:       plasma-nm-l2tp = %{version}
Obsoletes:      plasma-nm-l2tp < %{version}

%description l2tp
Layer Two Tunneling Protocol (L2TP) plugin for plasma-nm components.

%package pptp
Summary:        PPTP support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-pptp
Supplements:    packageand(%{name}:NetworkManager-pptp)
Provides:       NetworkManager-pptp-frontend
Provides:       plasma-nm-pptp = %{version}
Obsoletes:      NetworkManager-pptp-kde4
Obsoletes:      plasma-nm-pptp < %{version}

%description pptp
Point-To-Point Tunneling Protocol (PPTP) plugin for plasma-nm components.

%package ssh
Summary:        SSH support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
# NetworkManager-ssh doesn't exist in Factory
#Requires:       NetworkManager-ssh
Supplements:    packageand(%{name}:NetworkManager-ssh)
Provides:       NetworkManager-ssh-frontend

%description ssh
Secure Shell (SSH) plugin for plasma-nm components.

%package sstp
Summary:        SSTP support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
# NetworkManager-sstp doesn't exist in Factory
#Requires:       NetworkManager-sstp
Supplements:    packageand(%{name}:NetworkManager-sstp)
Provides:       NetworkManager-sstp-frontend

%description sstp
Secure Sockets Tunneling Protocol (SSTP) plugin for plasma-nm components.

%package iodine
Summary:        VPN support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-iodine
Supplements:    packageand(%{name}:NetworkManager-iodine)
Provides:       NetworkManager-iodine-frontend

%description iodine
Iodine (VPN through DNS tunnel) plugin for plasma-nm components.

%package fortisslvpn
Summary:        FortiGate SSL VPN support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
# Not available in oS:F stagings, leading to installcheck failure
# Requires:       NetworkManager-fortisslvpn
Supplements:    packageand(%{name}:NetworkManager-fortisslvpn)
Provides:       NetworkManager-fortisslvpn-frontend

%description fortisslvpn
FortiGate SSL VPN plugin for plasma-nm components.

%package mobile
Summary:        Mobile settings support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}

%description mobile
KConfig Modules and applets for
wireless connectivity on Plasma Mobile.

%lang_package

%prep
%autosetup -p1 -n plasma-nm-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir} -DBUILD_MOBILE=ON
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

  %fdupes %{buildroot}

%files
%license LICENSES/*
%{_kf5_applicationsdir}/kcm_networkmanagement.desktop
%{_kf5_libdir}/libplasmanm_editor.so
%{_kf5_libdir}/libplasmanm_internal.so
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/networkmanagement.so
%dir %{_kf5_plugindir}/plasma/network
%dir %{_kf5_plugindir}/plasma/network/vpn
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf5_qmldir}/
%{_kf5_notifydir}/
%{_kf5_sharedir}/plasma/
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.plasma.networkmanagement.appdata.xml
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%{_kf5_debugdir}/plasma-nm.categories
%{_datadir}/kcm_networkmanagement/

%files openvpn
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/*_openvpnui.so

%files vpnc
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/*_vpncui.so

%files openconnect
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so

%files libreswan
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so

%files strongswan
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so

%files l2tp
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so

%files pptp
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_pptpui.so

%files ssh
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%files sstp
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_sstpui.so

%files iodine
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so

%files fortisslvpn
%license LICENSES/*
%{_kf5_plugindir}/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so

%files mobile
%license LICENSES/*
%dir %{_kf5_plugindir}/kcms/
%{_kf5_plugindir}/kcms/kcm_mobile_hotspot.so
%{_kf5_plugindir}/kcms/kcm_mobile_wifi.so
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_mobile_hotspot/
%{_kf5_sharedir}/kpackage/kcms/kcm_mobile_wifi/

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
