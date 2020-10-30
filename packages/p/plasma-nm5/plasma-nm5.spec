#
# spec file for package plasma-nm5
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


%bcond_without lang
%define mm_support 1
Name:           plasma-nm5
Version:        5.20.2
Release:        0
Summary:        Plasma applet written in QML for managing network connections
License:        (LGPL-2.1-only OR LGPL-3.0-only) AND (GPL-2.0-only OR GPL-3.0-only)
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-nm-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-nm-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  NetworkManager-devel >= 0.9.8.4
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion) >= 5.25.0
BuildRequires:  cmake(KF5ConfigWidgets) >= 5.25.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.25.0
BuildRequires:  cmake(KF5DBusAddons) >= 5.25.0
BuildRequires:  cmake(KF5Declarative) >= 5.25.0
BuildRequires:  cmake(KF5I18n) >= 5.25.0
BuildRequires:  cmake(KF5IconThemes) >= 5.25.0
BuildRequires:  cmake(KF5Init) >= 5.25.0
BuildRequires:  cmake(KF5ItemViews) >= 5.25.0
BuildRequires:  cmake(KF5KDELibs4Support) >= 5.25.0
BuildRequires:  cmake(KF5KIO) >= 5.25.0
BuildRequires:  cmake(KF5NetworkManagerQt) >=  5.25.0
BuildRequires:  cmake(KF5Notifications) >= 5.25.0
BuildRequires:  cmake(KF5Plasma) >= 5.25.0
BuildRequires:  cmake(KF5Service) >= 5.25.0
BuildRequires:  cmake(KF5Solid) >= 5.25.0
BuildRequires:  cmake(KF5Wallet) >= 5.25.0
BuildRequires:  cmake(KF5WidgetsAddons) >= 5.25.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.25.0
BuildRequires:  cmake(KF5XmlGui) >= 5.25.0
BuildRequires:  cmake(Qca-qt5) >= 2.1.0
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Network) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5UiTools) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  pkgconfig(openconnect) >= 5.2
Requires:       NetworkManager
Requires:       kded
Requires:       kirigami2
Requires:       kwalletd5
Requires:       prison-qt5-imports
Recommends:     mobile-broadband-provider-info
Recommends:     %{name}-lang
Provides:       NetworkManager-client
Provides:       plasma-nm-kf5 = %{version}
Obsoletes:      plasma-nm-kf5 < %{version}
# Merged into the core in 5.15.80
Provides:       %{name}-wireguard = %{version}
Obsoletes:      %{name}-wireguard < %{version}
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm = %{version}
Obsoletes:      plasma-nm < %{version}
%endif
%if 0%{?mm_support}
BuildRequires:  cmake(KF5ModemManagerQt) >= 5.54.0
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
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-openvpn = %{version}
Obsoletes:      plasma-nm-openvpn < %{version}
%endif
Obsoletes:      NetworkManager-openvpn-kde4

%description openvpn
OpenVPN plugin for plasma-nm components.

%package vpnc
Summary:        vpnc support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-vpnc
Supplements:    packageand(%{name}:NetworkManager-vpnc)
Provides:       NetworkManager-vpnc-frontend
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-vpnc = %{version}
Obsoletes:      plasma-nm-vpnc < %{version}
%endif
Obsoletes:      NetworkManager-vpnc-kde4

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
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-openconnect = %{version}
Obsoletes:      plasma-nm-openconnect < %{version}
%endif
Obsoletes:      NetworkManager-openconnect-kde4

%description openconnect
OpenConnect plugin for plasma-nm components.

%package openswan
Summary:        Openswan support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
%if 0%{?suse_version} <= 1500
Requires:       NetworkManager-openswan
%endif
Supplements:    packageand(%{name}:NetworkManager-openswan)
Provides:       NetworkManager-openswan-frontend
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-openswan = %{version}
Obsoletes:      plasma-nm-openswan < %{version}
%endif

%description openswan
Openswan plugin for plasma-nm components.

%package strongswan
Summary:        strongSwan support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-strongswan
Supplements:    packageand(%{name}:NetworkManager-strongswan)
Provides:       NetworkManager-strongswan-frontend
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-strongswan = %{version}
Obsoletes:      plasma-nm-strongswan < %{version}
%endif

%description strongswan
strongSwan plugin for plasma-nm components.

%package l2tp
Summary:        L2TP support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-l2tp
Supplements:    packageand(%{name}:NetworkManager-l2tp)
Provides:       NetworkManager-l2tp-frontend
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-l2tp = %{version}
Obsoletes:      plasma-nm-l2tp < %{version}
%endif

%description l2tp
Layer Two Tunneling Protocol (L2TP) plugin for plasma-nm components.

%package pptp
Summary:        PPTP support for %{name}
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       NetworkManager-pptp
Supplements:    packageand(%{name}:NetworkManager-pptp)
Provides:       NetworkManager-pptp-frontend
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-nm-pptp = %{version}
Obsoletes:      plasma-nm-pptp < %{version}
%endif
Obsoletes:      NetworkManager-pptp-kde4

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
# NetworkManager-fortisslvpn doesn't exist in Factory
#Requires:       NetworkManager-fortisslvpn
Supplements:    packageand(%{name}:NetworkManager-fortisslvpn)
Provides:       NetworkManager-fortisslvpn-frontend

%description fortisslvpn
FortiGate SSL VPN plugin for plasma-nm components.

%lang_package

%prep
%autosetup -p1 -n plasma-nm-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

  %fdupes %{buildroot}

%files
%license COPYING*
%{_kf5_libdir}/libplasmanm_editor.so
%{_kf5_libdir}/libplasmanm_internal.so
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/networkmanagement.so
%{_kf5_qmldir}/
%{_kf5_notifydir}/
%{_kf5_servicesdir}/plasma-applet*.desktop
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/plasma/
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.plasma.networkmanagement.appdata.xml
%{_kf5_plugindir}/kcm_networkmanagement.so
%{_datadir}/kcm_networkmanagement/
%{_kf5_servicesdir}/kcm_networkmanagement.desktop

%files openvpn
%license COPYING*
%{_kf5_plugindir}/*_openvpnui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_openvpnui.desktop

%files vpnc
%license COPYING*
%{_kf5_plugindir}/*_vpncui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_vpncui.desktop

%files openconnect
%license COPYING*
%{_kf5_plugindir}/*_openconnectui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_openconnectui.desktop
%{_kf5_servicesdir}/plasmanetworkmanagement_openconnect_juniperui.desktop
%{_kf5_servicesdir}/plasmanetworkmanagement_openconnect_globalprotectui.desktop

%files openswan
%license COPYING*
%{_kf5_plugindir}/*_openswanui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_openswanui.desktop

%files strongswan
%license COPYING*
%{_kf5_plugindir}/*_strongswanui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_strongswanui.desktop

%files l2tp
%license COPYING*
%{_kf5_plugindir}/*_l2tpui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_l2tpui.desktop

%files pptp
%license COPYING*
%{_kf5_plugindir}/*_pptpui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_pptpui.desktop

%files ssh
%license COPYING*
%{_kf5_plugindir}/*_sshui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_sshui.desktop

%files sstp
%license COPYING*
%{_kf5_plugindir}/*_sstpui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_sstpui.desktop

%files iodine
%license COPYING*
%{_kf5_plugindir}/*_iodineui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_iodineui.desktop

%files fortisslvpn
%license COPYING*
%{_kf5_plugindir}/l*_fortisslvpnui.so
%{_kf5_servicesdir}/plasmanetworkmanagement_fortisslvpnui.desktop

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
