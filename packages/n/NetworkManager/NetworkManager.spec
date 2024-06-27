#
# spec file for package NetworkManager
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


# Toggle this whenever enabling/disabling the nm-probe-radius-server-cert.patch patch (as we export additional symbols)
# Like this, g-c-c and NM-applet, which consume this symbol, will block updating NM if we have to disable the patch until
# they are touched too
%define with_cacert_patch 0
%global _udevdir %(pkg-config --variable udevdir udev)
%global _pppddir %(ls -d %{_libdir}/pppd/2.?.?)
%global _dbusconfdir %{_datadir}/dbus-1/system.d

### Handy switches for easy testing of experimental features:
# (Remember that _with = OFF and _without = ON)

# FIXME: We should find out how to run specific tests and avoid
# tests that are doomed to fail in OBS.
# From "test-client.py --help":
#   test-client.py MyTestCase.testSomething  - run MyTestCase.testSomething
# Summary of Failures:
#07/74 check-local-exports-libnm    FAIL  0.11s  exit status 1
#08/74 platform/test-address-linux  FAIL  0.03s  killed by signal 6 SIGABRT
#10/74 platform/test-cleanup-linux  FAIL  0.03s  killed by signal 6 SIGABRT
#12/74 platform/test-link-linux     FAIL  0.03s  killed by signal 6 SIGABRT
#16/74 platform/test-route-linux    FAIL  0.03s  killed by signal 6 SIGABRT
#17/74 platform/test-tc-linux       FAIL  0.03s  killed by signal 6 SIGABRT
#24/74 test-l3cfg                   FAIL  0.10s  killed by signal 6 SIGABRT
#38/74 devices/test-acd             FAIL  0.04s  killed by signal 6 SIGABRT
%bcond_with TESTS
%if %{with TESTS}
%define tests_meson_opt yes
%else
%define tests_meson_opt no
%endif

# NetworkManager uses netconfig in SLES products only.
%if 0%{?suse_version} > 1500
%define with_netconfig 0
%else
%define with_netconfig 1
%endif

# Libaudit: yes-disabled-by-default enables support, but disables
# it unless explicitly configured via NetworkManager.conf
%bcond_without LIBAUDIT
%if %{with LIBAUDIT}
%define libaudit_meson_opt yes-disabled-by-default
%else
%define libaudit_meson_opt no
%endif

Name:           NetworkManager
Version:        1.48.2
Release:        0
Summary:        Standard Linux network configuration tool suite
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/System
URL:            https://networkmanager.dev/
Source0:        %{name}-%{version}.tar.zst
Source1:        nfs
Source2:        NetworkManager.conf
Source3:        baselibs.conf
Source4:        conncheck-disabled.conf
Source98:       macros.NetworkManager
Source99:       NetworkManager-rpmlintrc

# PATCH-FEATURE-OPENSUSE systemd-network-config.patch -- don't try to start NM under systemd if it is disabled in system configuration
Patch0:         systemd-network-config.patch
# PATCH-FIX-UPSTREAM nm-probe-radius-server-cert.patch bnc#574266 glin@suse.com -- Probe the RADIUS server certificate
Patch1:         nm-probe-radius-server-cert.patch
# PATCH-FIX-OPENSUSE nm-dont-overwrite-resolv-conf.patch bsc#1021665, bsc#960153 sckang@suse.com -- NetworkManager spawns netconfig to update DNS settings, and terminates netconfig after 1s. But 1s isn't quite long enough for netconfig to complete the task. Adjust it to 0 seconds(don't send SIGKILL) to avoid NM overwriting /etc/resolv.conf.
Patch4:         nm-dont-overwrite-resolv-conf.patch
# PATCH-FIX-OPENSUSE NetworkManager-1.10.6-netconfig.patch boo#1092352 -- Don't return SR_NOTFOUND if netconfig fails to launch
Patch5:         NetworkManager-1.10.6-netconfig.patch
# PATCH-FIX-UPSTREAM 0001-Coerce-connectivity-LIMITED-to-NONE-when-device-is-d.patch boo#1103678
Patch6:         0001-Coerce-connectivity-LIMITED-to-NONE-when-device-is-d.patch
# PATCH-FIX-OPENSUSE nm-add-CAP_SYS_ADMIN-permission.patch bsc#1129587 sckang@suse.com -- Add CAP_SYS_ADMIN which netconfig needs to call setdomainname
Patch7:         nm-add-CAP_SYS_ADMIN-permission.patch
# PATCH-FIX-SLE python3.6-in-sle.patch yfjiang@suse.com -- SLE still takes python 3.6 as primary runtime system, the patch makes meson find python 3.6
Patch8:         python3.6-in-sle.patch

BuildRequires:  c++_compiler
BuildRequires:  dnsmasq
BuildRequires:  fdupes
BuildRequires:  meson >= 0.51.0
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
BuildRequires:  python3-dbus-python
BuildRequires:  readline-devel
BuildRequires:  rp-pppoe
BuildRequires:  wireless-tools
BuildRequires:  perl(YAML)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.94
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(jansson) >= 2.7
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libndp)
BuildRequires:  pkgconfig(libnewt) >= 0.52.15
BuildRequires:  pkgconfig(libnl-3.0) >= 3.2.8
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libpsl) >= 0.1
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libudev) >= 175
BuildRequires:  pkgconfig(mm-glib) >= 0.7.991
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)
### Conditional BRs
%if %{with LIBAUDIT}
BuildRequires:  pkgconfig(audit)
%endif
## Required for tests
%if %{with TESTS}
#BuildRequires:  python3-gobject
%endif
##
Requires:       NetworkManager-branding
Requires:       mozilla-nss
%if %{with_netconfig}
Requires:       sysconfig-netconfig >= 0.80.5
%endif
Requires:       wpa_supplicant >= 0.6.4
Recommends:     dnsmasq
Recommends:     iproute2
Recommends:     iputils
Recommends:     nftables
# Provides required by sysconfig. The latter is used by older versions.
Provides:       dhcdbd = 1.14
Provides:       service(network)
Provides:       sysvinit(network)
Obsoletes:      dhcdbd < 1.14
Obsoletes:      libnm-glib-vpn1 < 1.32
Obsoletes:      libnm-glib4 < 1.32
Obsoletes:      libnm-util2 < 1.32
# NetworkManager-wifi was folded back into the main package
# The dep chain is not really different and it causes too many
# problems for users having that split. Not worth the pain
Provides:       NetworkManager-wifi = %{version}
Obsoletes:      NetworkManager-wifi < %{version}

%{?systemd_ordering}

%description
NetworkManager attempts to keep an active network connection available
at all times. The point of NetworkManager is to make networking
configuration and setup as painless and automatic as possible. If
using DHCP, NetworkManager is intended to replace default routes,
obtain IP addresses from a DHCP server, and change name servers
whenever it sees fit.

%package devel
Summary:        Libraries and headers for adding NetworkManager support to applications
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       libnm0 = %{version}
Requires:       typelib-1_0-NM-1_0 = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < 0.9.1

%description devel
This package contains various headers accessing some NetworkManager
functionality from applications.

%package -n libnm0
Summary:        Convenience library for clients of NetworkManager
Group:          System/Libraries

%description -n libnm0
This package contains the libraries that make it easier to use some
Network Manager functionality from applications that use glib.

%package -n typelib-1_0-NM-1_0
Summary:        Introspection bindings for the NetworkManager client convenience library
Group:          System/Libraries

%description -n typelib-1_0-NM-1_0
This package contains the gi-bindings that make it easier to use some
Network Manager functionality from applications that use glib.

This package provides the GObject Introspection bindings for the
NetworkManager library.

%package branding-upstream
Summary:        Default upstream configuration for NetworkManager
Group:          Productivity/Networking/System
Requires:       NetworkManager = %{version}
Supplements:    (NetworkManager and branding-upstream)
Conflicts:      NetworkManager-branding
Provides:       NetworkManager-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides the default upstream configuration for
NetworkManager. Specifically,
it is not configured for connection checking against
http://conncheck.opensuse.org. For, the version with connection
checking, install %{name}-branding-openSUSE.

%package pppoe
Summary:        NetworkManager plugin for ADSL connections
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Enhances:       %{name}
Supplements:    (%{name} and rp-pppoe)
Requires:       rp-pppoe
%requires_eq    ppp

%description pppoe
NetworkManager plugin for ADSL connections.

This package is needed to configure PPPoE interfaces

%package bluetooth
Summary:        Bluetooth device plugin for NetworkManager
Group:          System Environment/Base
Requires:       %{name} = %{version}
Requires:       NetworkManager-wwan = %{version}
BuildRequires:  pkgconfig(bluez) >= 5
Supplements:    (NetworkManager and bluez)

%description bluetooth
This package contains NetworkManager support for Bluetooth devices.

%package wwan
Summary:        Mobile broadband device plugin for NetworkManager
Group:          System Environment/Base
Requires:       %{name} = %{version}
Requires:       ModemManager

%description wwan
This package contains NetworkManager support for mobile broadband (WWAN)
devices.

%package ovs
Summary:        Open vSwitch device plugin for NetworkManager
Group:          System Environment/Base
Requires:       %{name} = %{version}
Requires:       openvswitch
Supplements:    (NetworkManager and openvswitch)

%description ovs
This package contains NetworkManager support for Open vSwitch bridges.

%package tui
Summary:        NetworkManager curses-based UI
Group:          System Environment/Base
Requires:       %{name} = %{version}
Requires:       libnm0 = %{version}
Supplements:    (patterns-base-enhanced_base and NetworkManager)

%description tui
This adds a curses-based "TUI" (Text User Interface) to
NetworkManager, to allow performing some of the operations supported
by nm-connection-editor and nm-applet in a non-graphical environment.

%package cloud-setup
Summary:        Automatically configure NetworkManager in cloud
Group:          System Environment/Base
Requires:       %{name} = %{version}
Requires:       libnm0 = %{version}

%description cloud-setup
Installs a nm-cloud-setup tool that can automatically configure
NetworkManager in cloud setups. Currently only EC2 is supported.
This tool is still experimental.

%lang_package

%prep
%setup -q
%patch -P 0 -p1
%if %{with_cacert_patch}
%patch -P 1 -p1
%endif
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%patch -P 8 -p1
%endif

# Fix server.conf's location, to end up in %%{_defaultdocdir}/%%{name},
# rather then %%{_datadir}/doc/%%{name}/examples:
sed -i -r "/install_dir: join_paths/s/(nm_datadir, 'doc)\
(', nm_name), 'examples'/\1\/packages\2/" data/meson.build

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -fno-strict-aliasing -fcommon"
export PYTHON=%{_bindir}/python3
%meson \
    -Dsystemdsystemunitdir=%{_unitdir} \
    -Dudev_dir=%{_udevdir} \
    -Ddbus_conf_dir=%{_dbusconfdir} \
    -Ddnsmasq=%{_sbindir}/dnsmasq \
    -Ddist_version=%{version} \
    -Dpolkit_agent_helper_1=%{_libexecdir}/polkit-1/polkit-agent-helper-1 \
    -Dhostname_persist=suse \
    -Dlibaudit=%{libaudit_meson_opt} \
    -Diwd=true \
    -Dpppd=%{_sbindir}/pppd \
    -Dpppd_plugin_dir=%{_pppddir} \
    -Dnm_cloud_setup=true \
    -Dbluez5_dun=true \
%if %{suse_version} >= 1550
    -Dnetconfig=%{_sbindir}/netconfig \
%else
    -Dnetconfig=/sbin/netconfig \
%endif
    -Dconfig_dhcp_default=internal \
    -Ddhcpcanon=no \
    -Ddhcpcd=no \
    -Ddhclient=%{_sbindir}/dhclient \
    -Ddocs=true \
    -Dtests=%{tests_meson_opt} \
    -Dmore_asserts=0 \
    -Dmore_logging=false \
    -Dqt=false \
    -Db_lto=true \
    -Dsession_tracking=systemd \
    -Dsession_tracking_consolekit=false \
    %{nil}
%meson_build

%if %{with TESTS}
%check
%meson_test
%endif

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/gtk-doc/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/{VPN,conf.d}
mkdir -p %{buildroot}%{_localstatedir}/log/
mkdir -p %{buildroot}%{_localstatedir}/lib/NetworkManager/dispatcher.d
mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/VPN
touch %{buildroot}%{_localstatedir}/log/NetworkManager
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/system-connections
install -m 0755 %{SOURCE1} %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/NetworkManager/
chmod 0644 %{buildroot}%{_prefix}/lib/NetworkManager/NetworkManager.conf
install -m 0644 %{SOURCE4} %{buildroot}%{_prefix}/lib/NetworkManager/conf.d
# Install RPM macros to be consumed by plugins
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 0644 %{SOURCE98} %{buildroot}%{_rpmmacrodir}/

# drop on demand activation, it is handled as a system service
rm -f %{buildroot}%{_datadir}/dbus-1/system-services/org.freedesktop.NetworkManager.service

%pre
%service_add_pre NetworkManager.service NetworkManager-dispatcher.service nm-priv-helper.service

%post
%service_add_post NetworkManager.service NetworkManager-dispatcher.service nm-priv-helper.service

%preun
%service_del_preun NetworkManager.service NetworkManager-dispatcher.service nm-priv-helper.service

%postun
%service_del_postun NetworkManager.service NetworkManager-dispatcher.service nm-priv-helper.service

%pre cloud-setup
%service_add_pre nm-cloud-setup.service

%post cloud-setup
%service_add_post nm-cloud-setup.service

%preun cloud-setup
%service_del_preun nm-cloud-setup.service

%postun cloud-setup
%service_del_postun nm-cloud-setup.service

%post -n libnm0 -p /sbin/ldconfig
%postun -n libnm0 -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog NEWS AUTHORS TODO
%{_bindir}/nm-online
%{_bindir}/nmcli
%{_datadir}/bash-completion/completions/nmcli
%{_sbindir}/NetworkManager
%{_datadir}/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.NetworkManager.*
%{_datadir}/polkit-1/actions/org.freedesktop.NetworkManager.policy
%attr(0700,root,root) %{_localstatedir}/lib/NetworkManager
%{_mandir}/man1/nm-online.1%{?ext_man}
%{_mandir}/man1/nmcli.1%{?ext_man}
%{_mandir}/man5/nm-settings-keyfile.5%{?ext_man}
%{_mandir}/man5/NetworkManager.conf.5%{?ext_man}
%{_mandir}/man5/nm-settings.5%{?ext_man}
%{_mandir}/man5/nm-system-settings.conf.5%{?ext_man}
%{_mandir}/man5/nm-settings-dbus.5%{?ext_man}
%{_mandir}/man5/nm-settings-nmcli.5%{?ext_man}
%{_mandir}/man7/nmcli-examples.7%{?ext_man}
%{_mandir}/man8/NetworkManager-dispatcher.8%{?ext_man}
%{_mandir}/man8/NetworkManager-wait-online.service.8%{?ext_man}
%{_mandir}/man8/NetworkManager.8%{?ext_man}
%{_mandir}/man8/nm-initrd-generator.8%{?ext_man}
%dir %{_libdir}/NetworkManager
%dir %{_libdir}/NetworkManager/%{version}
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-wifi.so
%{_libexecdir}/nm-daemon-helper
%{_libexecdir}/nm-dhcp-helper
%{_libexecdir}/nm-dispatcher
%{_libexecdir}/nm-initrd-generator
%{_libexecdir}/nm-priv-helper
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/VPN
%dir %{_sysconfdir}/NetworkManager/conf.d
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%dir %{_sysconfdir}/NetworkManager/system-connections
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/nfs
%{_unitdir}/NetworkManager.service
%{_unitdir}/NetworkManager-dispatcher.service
%{_unitdir}/NetworkManager-wait-online.service
%dir %{_unitdir}/NetworkManager.service.d
%{_udevdir}/rules.d/84-nm-drivers.rules
%{_udevdir}/rules.d/85-nm-unmanaged.rules
%{_udevdir}/rules.d/90-nm-thunderbolt.rules
%{_unitdir}/nm-priv-helper.service
%ghost %config(noreplace) %{_localstatedir}/log/NetworkManager
%dir %{_prefix}/lib/NetworkManager
%{_prefix}/lib/NetworkManager/NetworkManager.conf
%dir %{_prefix}/lib/NetworkManager/conf.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/no-wait.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/pre-up.d
%{_prefix}/lib/NetworkManager/dispatcher.d/pre-up.d/90-nm-cloud-setup.sh
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/pre-down.d
%dir %{_prefix}/lib/NetworkManager/VPN
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/zones
%{_prefix}/lib/firewalld/zones/nm-shared.xml
%{_dbusconfdir}/nm-dispatcher.conf
%{_dbusconfdir}/org.freedesktop.NetworkManager.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.nm_priv_helper.service
%{_dbusconfdir}/nm-priv-helper.conf
%{_defaultdocdir}/NetworkManager/server.conf

%files devel
%{_includedir}/libnm/
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libnm.deps
%{_datadir}/vala/vapi/libnm.vapi
%{_libdir}/libnm.so
%{_libdir}/pkgconfig/libnm.pc
%doc %{_datadir}/gtk-doc/html/NetworkManager/
%doc %{_datadir}/gtk-doc/html/libnm/
%{_rpmmacrodir}/macros.NetworkManager

%files -n libnm0
%{_libdir}/libnm.so.*

%files -n typelib-1_0-NM-1_0
%{_libdir}/girepository-1.0/NM-1.0.typelib

%files lang -f %{name}.lang

%files branding-upstream
%{_prefix}/lib/NetworkManager/conf.d/conncheck-disabled.conf

%files pppoe
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-adsl.so
%{_libdir}/NetworkManager/%{version}/libnm-ppp-plugin.so
%dir %{_libdir}/pppd/2.*
%{_libdir}/pppd/2.*/nm-pppd-plugin.*

%files bluetooth
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-bluetooth.so

%files wwan
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-wwan.so
%{_libdir}/NetworkManager/%{version}/libnm-wwan.so

%files ovs
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-ovs.so
%{_unitdir}/NetworkManager.service.d/NetworkManager-ovs.conf
%{_mandir}/man7/nm-openvswitch.7%{?ext_man}

%files tui
%{_bindir}/nmtui*
%{_mandir}/man1/nmtui.1%{?ext_man}
%{_mandir}/man1/nmtui-connect.1%{?ext_man}
%{_mandir}/man1/nmtui-edit.1%{?ext_man}
%{_mandir}/man1/nmtui-hostname.1%{?ext_man}

%files cloud-setup
%{_libexecdir}/nm-cloud-setup
%{_unitdir}/nm-cloud-setup.service
%{_unitdir}/nm-cloud-setup.timer
%{_prefix}/lib/NetworkManager/dispatcher.d/90-nm-cloud-setup.sh
%{_prefix}/lib/NetworkManager/dispatcher.d/no-wait.d/90-nm-cloud-setup.sh
%{_mandir}/man8/nm-cloud-setup.8%{?ext_man}

%changelog
