#
# spec file for package connman
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


%define	openconnect_present	(0%{?suse_version} != 1110 && 0%{?suse_version} != 1315)
# hh2serial and tist is not building correctly on PPC and I don't intend to fix that
%ifarch ppc ppc64
%define hh2serial_working	0
%define tist_working		0
%else
%define hh2serial_working	1
%define tist_working		1
%endif
Name:           connman
Version:        1.37
Release:        0
Summary:        Connection Manager
License:        GPL-2.0-only
Group:          System/Daemons
URL:            http://www.moblin.org/
Source0:        http://www.kernel.org/pub/linux/network/connman/connman-%{version}.tar.xz
Source1:        http://www.kernel.org/pub/linux/network/connman/connman-%{version}.tar.sign
Source2:        connman.keyring
# PATCH-FIX-OPENSUSE -- Greate symlink to network.service
Patch0:         connman-1.35-service.patch
BuildRequires:  dhcp
BuildRequires:  openvpn
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  wpa_supplicant
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libiptc)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(xtables)
Requires:       bluez
Requires:       dhcp >= 3.0.2
Requires:       iptables
Requires:       wpa_supplicant
Recommends:     %{name}-client
%{?systemd_requires}

%description
Connection Manager provides a daemon for managing Internet connections
within embedded devices running the Linux operating system.

%package devel
Summary:        Development files for Connection Manager
Group:          Development/Libraries/C and C++
Requires:       %{name} >= %{version}

%description devel
connman-devel contains development files for use with connman.

%package doc
Summary:        Connman reference man pages
Group:          Documentation/Man

%description doc
Documentation in form of man pages for connman

##############################
#Plugins
##############################

%if %{hh2serial_working}
%package plugin-hh2serial-gps
Summary:        HH2Serial GPS plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description plugin-hh2serial-gps
Provides HH2Serial GPS device support for Connman (Connection Manager).
%endif
#-------------------------------------

%if %{openconnect_present}
%package plugin-openconnect
Summary:        OpenConnect plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openconnect)
Requires:       %{name} >= %{version}
Requires:       dbus-1 >= 1.0
Requires:       openconnect

%description plugin-openconnect
Provides OpenConnect support for Connman (Connection Manager).
OpenConnect is an open client for Cisco(TM) AnyConnect(TM) VPN.
#-------------------------------------
%endif #openconnect_present

%package plugin-vpnc
Summary:        VPNC plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  vpnc
Requires:       %{name} >= %{version}
Requires:       vpnc

%description plugin-vpnc
Provides VPNC support for Connman (Connection Manager).
#-------------------------------------

%package plugin-openvpn
Summary:        OpenVPN plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  openvpn
Requires:       %{name} >= %{version}
Requires:       openvpn

%description plugin-openvpn
Provides OpenVPN support for Connman (Connection Manager).
#-------------------------------------

%package plugin-pptp
Summary:        PPTP plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  vpnc
Requires:       %{name} >= %{version}
Requires:       vpnc

%description plugin-pptp
Provides PPTP support for Connman (Connection Manager).
#-------------------------------------

%if %{tist_working}
%package plugin-tist
Summary:        TIST plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description plugin-tist
Provides TI Shared Transport support for Connman (Connection Manager).
%endif # tist_working
#-------------------------------------

%package plugin-l2tp
Summary:        L2TP plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description plugin-l2tp
Provides L2TP (Layer 2 Tunneling Protocol) support for Connman (Connection Manager).
#-------------------------------------

%package plugin-iospm
Summary:        Intel OSPM plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  ppp-devel
Requires:       %{name} >= %{version}
Requires:       ppp

%description plugin-iospm
Provides Intel OSPM support for Connman (Connection Manager).
#-------------------------------------

%package test
Summary:        Test and example scripts for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description test
Provides test and example scripts for Connman (Connection Manager).
#-------------------------------------

%package nmcompat
Summary:        NetworkManager compatibility for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description nmcompat
Provides NetworkManager compatibility for Connman (Connection Manager).
#-------------------------------------

%package plugin-polkit
Summary:        PolicyKit plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}
Requires:       dbus-1 >= 1.0
Requires:       polkit

%description plugin-polkit
Provides PolicyKit support for Connman (Connection Manager).
#-------------------------------------

%package client
Summary:        Client script for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description client
Provides client interface for Connman (Connection Manager).

%prep
%setup -q -n connman-%{version}
%patch0 -p1

%build
# Using i586 repository, so explicitly forward it to CC.
# Necesary, because i386 will fail due to:
# undefined reference to `__sync_add_and_fetch_4'
# Restrict to Fedora right for now.
%if 0%{?fedora}
%ifarch i386 i486 i586
CFLAGS='-O2 -g -march=i586 -mtune=i686'
export CFLAGS
CXXFLAGS='-O2 -g -march=i586 -mtune=i686'
export CXXFLAGS
FFLAGS='-O2 -g -march=i586 -mtune=i686'
export FFLAGS
%endif
%endif

%configure --enable-shared \
           --with-systemdunitdir=%{_unitdir} \
           --disable-debug \
           --enable-pie \
%if %{hh2serial_working}
           --enable-hh2serial-gps \
%endif
%if %{openconnect_present}
           --enable-openconnect \
%endif
           --enable-openvpn \
           --enable-vpnc \
           --enable-l2tp \
           --enable-pptp \
           --enable-iospm \
%if %{tist_working}
           --enable-tist \
%endif
           --enable-test \
           --enable-nmcompat \
           --enable-polkit \
           --enable-loopback \
           --enable-ethernet \
           --enable-wifi \
           --enable-bluetooth \
           --enable-ofono \
           --enable-dundee \
           --enable-pacrunner \
           --enable-wispr \
           --enable-client \
           --enable-tools \
           --enable-datafiles

make %{?_smp_mflags}

%install
%make_install

mkdir -p \
	%{buildroot}%{_localstatedir}/lib/%{name} \
	%{buildroot}%{_localstatedir}/lib/%{name}-vpn

touch %{buildroot}%{_localstatedir}/lib/%{name}/settings

install -Dm0755 {client,%{buildroot}/%{_bindir}}/connmanctl
install -Dm0644 {src,%{buildroot}%{_sysconfdir}/%{name}}/main.conf

find %{buildroot} -type f -name "*.la" -delete -print
%if ! %{openconnect_present}
rm %{buildroot}%{_libdir}/%{name}/scripts/openconnect-script
%endif

%pre
%service_add_pre connman.service
%service_add_pre connman-vpn.service
%service_del_postun connman-wait-online.service

%post
%service_add_post connman.service
%service_add_post connman-vpn.service
%service_del_postun connman-wait-online.service
%tmpfiles_create %{_tmpfilesdir}/connman.conf
%tmpfiles_create %{_tmpfilesdir}/connman_resolvconf.conf
if ! readlink %{_sysconfdir}/systemd/system/network.service &> /dev/null; then
	%{_bindir}/systemctl --system daemon-reload || :
	%{_bindir}/systemctl --force enable connman.service || :
elif [ $1 -eq 1 ]; then
mkdir -p %{_localstatedir}/adm/update-messages
rm -f %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}
cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release} << EOF
INFO: Please ensure that the network services disabled:
INFO: Yast2 -> Network Settings -> Global Option -> Network Setup Method -> Network Services Disabled
INFO: or using the command line
INFO: systemctl disable $(readlink %{_sysconfdir}/systemd/system/network.service | sed 's/.*\///')
EOF
fi

%preun
%service_del_preun connman.service
%service_del_preun connman-vpn.service
%service_del_preun connman-wait-online.service

%postun
%service_del_postun connman.service
%service_del_postun connman-vpn.service
%service_del_postun connman-wait-online.service

%files
%doc AUTHORS COPYING ChangeLog README
%{_sbindir}/connmand
%{_sbindir}/connman-vpnd
%{_sbindir}/connmand-wait-online
%{_tmpfilesdir}/connman_resolvconf.conf
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/scripts
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins-vpn
%{_datadir}/dbus-1/system.d/connman.conf
%{_datadir}/dbus-1/system.d/connman-vpn-dbus.conf
%{_datadir}/dbus-1/system-services/net.connman.vpn.service
%{_unitdir}/connman.service
%{_unitdir}/connman-vpn.service
%{_unitdir}/connman-wait-online.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/main.conf
%ghost %dir %{_localstatedir}/lib/%{name}
%ghost %dir %{_localstatedir}/lib/%{name}-vpn
%ghost %{_localstatedir}/lib/%{name}/settings

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%files doc
%{_mandir}/*/*

#plugins
%if %{hh2serial_working}
%files plugin-hh2serial-gps
%{_libdir}/%{name}/plugins/hh2serial-gps.so
%endif

%if %{openconnect_present}
%files plugin-openconnect
%{_libdir}/%{name}/plugins-vpn/openconnect.so
%{_libdir}/%{name}/scripts/openconnect-script
%endif

%files plugin-vpnc
%{_libdir}/%{name}/plugins-vpn/vpnc.so

%files plugin-iospm
%{_libdir}/%{name}/plugins/iospm.so

%files plugin-l2tp
%{_libdir}/%{name}/plugins-vpn/l2tp.so
%{_libdir}/%{name}/scripts/libppp-plugin.so*

%files plugin-openvpn
%{_libdir}/%{name}/plugins-vpn/openvpn.so
%{_libdir}/%{name}/scripts/openvpn-script

%files plugin-pptp
%{_libdir}/%{name}/plugins-vpn/pptp.so

%if %{tist_working}
%files plugin-tist
%{_libdir}/%{name}/plugins/tist.so
%endif

%files test
%{_libdir}/%{name}/test

%files nmcompat
%{_datadir}/dbus-1/system.d/connman-nmcompat.conf

%files plugin-polkit
%{_datadir}/polkit-1/actions/net.connman.policy
%{_datadir}/polkit-1/actions/net.connman.vpn.policy

%files client
%{_bindir}/connmanctl

%changelog
