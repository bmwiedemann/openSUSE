#
# spec file for package plasma6-nm
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

%define rname plasma-nm
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
%ifnarch %ix86 %arm ppc64 ppc64le s390x
# QtWebEngine is required if the openconnect plugin is built
%bcond_without openconnect
%endif
Name:           plasma6-nm
Version:        6.1.1
Release:        0
Summary:        Plasma applet written in QML for managing network connections
License:        (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6ModemManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6DBus)
BuildRequires:  cmake(Qca-qt6) >= 2.1.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
%if %{with openconnect}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  pkgconfig(libnm) >= 1.4.0
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
%if %{with openconnect}
BuildRequires:  pkgconfig(openconnect) >= 5.2
%endif
Requires:       NetworkManager
Requires:       kf6-kded
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-networkmanager-qt-imports >= %{kf6_version}
Requires:       kf6-prison-imports >= %{kf6_version}
Requires:       kwalletd6
Recommends:     mobile-broadband-provider-info
Supplements:    (plasma6-desktop and NetworkManager)
Provides:       plasma-nm-kf5 = %{version}
Obsoletes:      plasma-nm-kf5 < %{version}
Provides:       plasma-nm5 = %{version}
Obsoletes:      plasma-nm5 < %{version}
Obsoletes:      plasma-nm5-lang < %{version}
Provides:       NetworkManager-client

%description
Plasma applet for controlling network connections on systems
that use the NetworkManager service.

%package openvpn
Summary:        OpenVPN support for plasma6-nm
Requires:       NetworkManager-openvpn
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-openvpn)
Provides:       NetworkManager-openvpn-frontend
Provides:       plasma-nm5-openvpn = %{version}
Obsoletes:      plasma-nm5-openvpn < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-openvpn = %{version}
Obsoletes:      plasma-nm-openvpn < %{version}

%description openvpn
OpenVPN plugin for plasma-nm components.

%package vpnc
Summary:        vpnc support for plasma6-nm
Requires:       NetworkManager-vpnc
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-vpnc)
Provides:       NetworkManager-vpnc-frontend
Provides:       plasma-nm5-vpnc = %{version}
Obsoletes:      plasma-nm5-vpnc < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-vpnc = %{version}
Obsoletes:      plasma-nm-vpnc < %{version}

%description vpnc
vpnc plugin for plasma-nm components.

%if %{with openconnect}
%package openconnect
Summary:        OpenConnect support for plasma6-nm
Requires:       NetworkManager-openconnect
Requires:       openconnect
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-openconnect)
Provides:       NetworkManager-openconnect-frontend
Provides:       plasma-nm5-openconnect = %{version}
Obsoletes:      plasma-nm5-openconnect < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-openconnect = %{version}
Obsoletes:      plasma-nm-openconnect < %{version}

%description openconnect
OpenConnect plugin for plasma-nm components.
%endif

%package libreswan
Summary:        Libreswan support for plasma6-nm
Requires:       NetworkManager-libreswan
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-libreswan)
Provides:       NetworkManager-libreswan-frontend
Provides:       plasma-nm5-libreswan = %{version}
Obsoletes:      plasma-nm5-libreswan < %{version}
Provides:       plasma-nm5-openswan = %{version}
Obsoletes:      plasma-nm5-openswan < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-openswan = %{version}
Obsoletes:      plasma-nm-openswan < %{version}

%description libreswan
Libreswan plugin for plasma-nm components.

%package strongswan
Summary:        strongSwan support for plasma6-nm
Requires:       NetworkManager-strongswan
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-strongswan)
Provides:       NetworkManager-strongswan-frontend
Provides:       plasma-nm5-strongswan = %{version}
Obsoletes:      plasma-nm5-strongswan < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-strongswan = %{version}
Obsoletes:      plasma-nm-strongswan < %{version}

%description strongswan
strongSwan plugin for plasma-nm components.

%package l2tp
Summary:        L2TP support for plasma6-nm
Requires:       NetworkManager-l2tp
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-l2tp)
Provides:       NetworkManager-l2tp-frontend
Provides:       plasma-nm5-l2tp = %{version}
Obsoletes:      plasma-nm5-l2tp < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-l2tp = %{version}
Obsoletes:      plasma-nm-l2tp < %{version}

%description l2tp
Layer Two Tunneling Protocol (L2TP) plugin for plasma-nm components.

%package pptp
Summary:        PPTP support for plasma6-nm
Requires:       NetworkManager-pptp
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-pptp)
Provides:       NetworkManager-pptp-frontend
Provides:       plasma-nm5-pptp = %{version}
Obsoletes:      plasma-nm5-pptp < %{version}
# Old names provided / Obsoleted by plasma-nm5
Provides:       plasma-nm-pptp = %{version}
Obsoletes:      plasma-nm-pptp < %{version}

%description pptp
Point-To-Point Tunneling Protocol (PPTP) plugin for plasma-nm components.

%package ssh
Summary:        SSH support for plasma6-nm
Requires:       plasma6-nm = %{version}
# NetworkManager-ssh doesn't exist in Factory
#Requires:       NetworkManager-ssh
Supplements:    (plasma6-nm and NetworkManager-ssh)
Provides:       NetworkManager-ssh-frontend
Provides:       plasma-nm5-ssh = %{version}
Obsoletes:      plasma-nm5-ssh < %{version}

%description ssh
Secure Shell (SSH) plugin for plasma-nm components.

%package sstp
Summary:        SSTP support for plasma6-nm
Requires:       plasma6-nm = %{version}
# NetworkManager-sstp doesn't exist in Factory
#Requires:       NetworkManager-sstp
Supplements:    (plasma6-nm and NetworkManager-sstp)
Provides:       NetworkManager-sstp-frontend
Obsoletes:      plasma-nm5-sstp < %{version}

%description sstp
Secure Sockets Tunneling Protocol (SSTP) plugin for plasma-nm components.

%package iodine
Summary:        VPN support for plasma6-nm
Requires:       NetworkManager-iodine
Requires:       plasma6-nm = %{version}
Supplements:    (plasma6-nm and NetworkManager-iodine)
Provides:       NetworkManager-iodine-frontend
Obsoletes:      plasma-nm5-iodine < %{version}

%description iodine
Iodine (VPN through DNS tunnel) plugin for plasma-nm components.

%package fortisslvpn
Summary:        FortiGate SSL VPN support for plasma6-nm
Requires:       plasma6-nm = %{version}
# Not available in oS:F stagings, leading to installcheck failure
# TODO ↑ still true?
# Requires:       NetworkManager-fortisslvpn
Supplements:    (plasma6-nm and NetworkManager-fortisslvpn)
Provides:       NetworkManager-fortisslvpn-frontend
Obsoletes:      plasma-nm5-fortisslvpn < %{version}

%description fortisslvpn
FortiGate SSL VPN plugin for plasma-nm components.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%fdupes %{buildroot}

%files
%license LICENSES/*
%dir %{_kf6_plugindir}/plasma/network
%dir %{_kf6_plugindir}/plasma/network/vpn
%{_kf6_applicationsdir}/kcm_networkmanagement.desktop
%{_kf6_appstreamdir}/org.kde.plasma.networkmanagement.appdata.xml
%{_kf6_debugdir}/plasma-nm.categories
%{_kf6_libdir}/libplasmanm_editor.so
%{_kf6_libdir}/libplasmanm_internal.so
%{_kf6_notificationsdir}/networkmanagement.notifyrc
%{_kf6_plugindir}/kf6/kded/networkmanagement.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%dir %{_kf6_qmldir}/org/kde/plasma
%{_kf6_qmldir}/org/kde/plasma/networkmanagement/
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.networkmanagement/
%{_kf6_sharedir}/kcm_networkmanagement/

%files openvpn
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so

%files vpnc
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_vpncui.so

%if %{with openconnect}
%files openconnect
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
%endif

%files libreswan
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so

%files strongswan
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so

%files l2tp
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so

%files pptp
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_pptpui.so

%files ssh
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%files sstp
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_sstpui.so

%files iodine
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so

%files fortisslvpn
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so

%files lang -f %{name}.lang

%changelog
