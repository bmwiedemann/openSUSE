#
# spec file for package NetworkManager
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


# Toggle this whenever enabling/disabling the nm-probe-radius-server-cert.patch patch (as we export additional symbols)
# Like this, g-c-c and NM-applet, which consume this symbol, will block updating NM if we have to disable the patch until
# they are touched too
%define with_cacert_patch 0
%define _udevdir %(pkg-config --variable udevdir udev)
Name:           NetworkManager
Version:        1.26.4
Release:        0
Summary:        Network Link Manager and user applications for it
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.gnome.org/projects/NetworkManager/
Source0:        https://download.gnome.org/sources/%{name}/1.26/%{name}-%{version}.tar.xz
Source1:        nfs
Source2:        NetworkManager.conf
Source3:        baselibs.conf
Source98:       macros.NetworkManager
Source99:       NetworkManager-rpmlintrc

# PATCH-FEATURE-OPENSUSE systemd-network-config.patch -- don't try to start NM under systemd if it is disabled in system configuration
Patch0:         systemd-network-config.patch
# PATCH-FIX-UPSTREAM nm-probe-radius-server-cert.patch bnc#574266 glin@suse.com -- Probe the RADIUS server certificate
Patch1:         nm-probe-radius-server-cert.patch
# PATCH-NEEDS-REBASE networkmanager-checks-po.patch tchvatal@suse.com -- fix translation validation error caused by our patch systemd-network-config.patch was: PATCH-FIX-OPENSUSE
Patch2:         networkmanager-checks-po.patch
# PATCH-NEEDS-REBASE networkmanager-obs-net.patch tchvatal@suse.com -- disable tests that are by design broken on OBS workers # WAS PATCH-FIX-OPENSUSE
Patch3:         networkmanager-obs-net.patch
# PATCH-FIX-OPENSUSE nm-dont-overwrite-resolv-conf.patch bsc#1021665, bsc#960153 sckang@suse.com -- NetworkManager spawns netconfig to update DNS settings, and terminates netconfig after 1s. But 1s isn't quite long enough for netconfig to complete the task. Adjust it to 0 seconds(don't send SIGKILL) to avoid NM overwriting /etc/resolv.conf.
Patch4:         nm-dont-overwrite-resolv-conf.patch
# PATCH-FIX-OPENSUSE NetworkManager-1.10.6-netconfig.patch boo#1092352 -- Don't return SR_NOTFOUND if netconfig fails to launch
Patch5:         NetworkManager-1.10.6-netconfig.patch
# PATCH-FIX-UPSTREAM 0001-Coerce-connectivity-LIMITED-to-NONE-when-device-is-d.patch boo#1103678
Patch6:         0001-Coerce-connectivity-LIMITED-to-NONE-when-device-is-d.patch
# PATCH-FIX-OPENSUSE nm-add-CAP_SYS_ADMIN-permission.patch bsc#1129587 sckang@suse.com -- Add CAP_SYS_ADMIN which netconfig needs to call setdomainname
Patch7:         nm-add-CAP_SYS_ADMIN-permission.patch

BuildRequires:  dnsmasq
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  iptables
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
# Required for tests
BuildRequires:  python3-dbus-python
BuildRequires:  python3-gobject
BuildRequires:  readline-devel
BuildRequires:  rp-pppoe
# Do not use suse-release, it's very late in build chain and not needed
# all it does is netconfig and ifconfig enablement
#BuildRequires:  suse-release
# for /sbin/netconfig: integration with netconfig is required
BuildRequires:  sysconfig-netconfig
BuildRequires:  translation-update-upstream
BuildRequires:  wireless-tools
BuildRequires:  perl(YAML)
BuildRequires:  pkgconfig(bluez) >= 5
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.94
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libndp)
BuildRequires:  pkgconfig(libnewt) >= 0.52.15
BuildRequires:  pkgconfig(libnl-3.0) >= 3.2.8
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libpsl) >= 0.1
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libteam)
BuildRequires:  pkgconfig(libudev) >= 175
BuildRequires:  pkgconfig(mm-glib) >= 0.7.991
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)
Requires:       NetworkManager-branding
Requires:       dhcp-client
Requires:       iproute2
Requires:       iputils
Requires:       mozilla-nss
Requires:       sysconfig-netconfig >= 0.80.5
Requires:       wpa_supplicant >= 0.6.4
%requires_eq    ppp
Recommends:     dnsmasq
Recommends:     iptables
Recommends:     org.freedesktop.ModemManager
# Recommend the rp-pppoe binary for PPP over Ethernet (common for ADSL) connections.
Recommends:     rp-pppoe
Provides:       dhcdbd = 1.14
Obsoletes:      dhcdbd < 1.14
Obsoletes:      libnm-glib-vpn1
Obsoletes:      libnm-glib4
Obsoletes:      libnm-util2
%{?systemd_requires}

%description
NetworkManager attempts to keep an active network connection available
at all times.  The point of NetworkManager is to make networking
configuration and setup as painless and automatic as possible.	If
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
Obsoletes:      %{name}-doc < %{version}

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
Summary:        Default upstream configuration for %{_sysconfdir}/NetworkManager/NetworkManager.conf
Group:          Productivity/Networking/System
Requires:       NetworkManager = %{version}
Supplements:    packageand(NetworkManager:branding-upstream)
Conflicts:      NetworkManager-branding
Provides:       NetworkManager-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides the default upstream configuration for
%{_sysconfdir}/NetworkManager/NetworkManager.conf. Specifically,
it is not configured for connection checking against
http://conncheck.opensuse.org. For, the version with connection
checking, install %{name}-branding-openSUSE.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch0 -p1
%if %{with_cacert_patch}
%patch1 -p1
%endif
#patch2 -p1
#patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
NOCONFIGURE=1 ./autogen.sh
pppddir=`ls -1d %{_libdir}/pppd/2*`
test -n "$pppddir" || exit 1
export CFLAGS="%{optflags} -fno-strict-aliasing -fcommon"
export PYTHON=%{_bindir}/python3
%configure \
    --disable-silent-rules \
    --with-hostname-persist=suse \
    --enable-ld-gc \
    --disable-static \
    --with-crypto=nss \
    --enable-gtk-doc \
    --enable-json-validation \
    --with-tests=yes \
    --with-netconfig=yes \
    --with-config-dns-rc-manager-default=netconfig \
    --enable-more-warnings=no \
    --with-pppd-plugin-dir=$pppddir \
    --with-dhclient=/sbin/dhclient \
    --with-dhcpcd=no \
    --with-udev-dir=%{_udevdir} \
    --with-modem-manager-1 \
    --enable-concheck \
    --enable-wifi=yes \
    --with-nmtui \
    --with-session-tracking=systemd \
    --with-suspend-resume=systemd \
    --with-iwd=yes
# Fail if netconfig was not detected. Avoids future occurences of bnc#817592
if grep "with_netconfig='no'" config.log; then
  print netconfig support was not found -- BUILD ABORTED
  false
fi
make %{?_smp_mflags} nmrundir="/run/%{name}"

%check
#make %%{?_smp_mflags} check

%install
%make_install nmrundir="/run/%{name}"
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/gtk-doc/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/VPN
mkdir -p %{buildroot}%{_localstatedir}/log/
mkdir -p %{buildroot}%{_localstatedir}/lib/NetworkManager
mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/VPN
touch %{buildroot}%{_localstatedir}/log/NetworkManager
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/system-connections
install -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/NetworkManager/
# Install RPM macros to be consumed by plugins
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 0644 %{SOURCE98} %{buildroot}%{_rpmmacrodir}/

# We package this one as %%doc in the default location.
rm %{buildroot}%{_datadir}/doc/NetworkManager/examples/server.conf

# drop on demand activation, it is handled as a system service
rm -f %{buildroot}%{_datadir}/dbus-1/system-services/org.freedesktop.NetworkManager.service

%pre
%service_add_pre NetworkManager.service NetworkManager-dispatcher.service nm-cloud-setup.service

%post
%service_add_post NetworkManager.service NetworkManager-dispatcher.service nm-cloud-setup.service

%preun
%service_del_preun NetworkManager.service NetworkManager-dispatcher.service nm-cloud-setup.service

%postun
%service_del_postun NetworkManager.service NetworkManager-dispatcher.service nm-cloud-setup.service

%post -n libnm0 -p /sbin/ldconfig
%postun -n libnm0 -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog NEWS AUTHORS README CONTRIBUTING TODO data/server.conf
%{_bindir}/nm-online
%{_bindir}/nmcli
%{_bindir}/nmtui*
%{_datadir}/bash-completion/completions/nmcli
%{_sbindir}/NetworkManager
%{_datadir}/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.NetworkManager.*
%{_datadir}/polkit-1/actions/org.freedesktop.NetworkManager.policy
%attr(0700,root,root) %{_localstatedir}/lib/NetworkManager
%{_mandir}/man1/nm-online.1%{ext_man}
%{_mandir}/man1/nmcli.1%{ext_man}
%{_mandir}/man1/nmtui.1%{?ext_man}
%{_mandir}/man1/nmtui-connect.1%{?ext_man}
%{_mandir}/man1/nmtui-edit.1%{?ext_man}
%{_mandir}/man1/nmtui-hostname.1%{?ext_man}
%{_mandir}/man5/nm-settings-keyfile.5%{?ext_man}
%{_mandir}/man5/NetworkManager.conf.5%{?ext_man}
%{_mandir}/man5/nm-settings.5%{?ext_man}
%{_mandir}/man5/nm-system-settings.conf.5%{?ext_man}
%{_mandir}/man5/nm-settings-dbus.5%{ext_man}
%{_mandir}/man5/nm-settings-nmcli.5%{ext_man}
%{_mandir}/man7/nm-openvswitch.7%{?ext_man}
%{_mandir}/man7/nmcli-examples.7%{?ext_man}
%{_mandir}/man8/NetworkManager.8%{ext_man}
%{_mandir}/man8/nm-initrd-generator.8%{ext_man}
%dir %{_libdir}/NetworkManager
%dir %{_libdir}/NetworkManager/%{version}
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-adsl.so
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-bluetooth.so
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-ovs.so
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-team.so
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-wifi.so
%{_libdir}/NetworkManager/%{version}/libnm-device-plugin-wwan.so
%{_libdir}/NetworkManager/%{version}/libnm-ppp-plugin.so
#%%{_libdir}/NetworkManager/%%{version}/libnm-settings-plugin-ibft.so
%{_libdir}/NetworkManager/%{version}/libnm-wwan.so
%dir %{_libdir}/pppd/2.*
%{_libdir}/pppd/2.*/nm-pppd-plugin.*
%{_libexecdir}/nm-cloud-setup
%{_libexecdir}/nm-dhcp-helper
%{_libexecdir}/nm-dispatcher
%{_libexecdir}/nm-iface-helper
%{_libexecdir}/nm-initrd-generator
%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.NetworkManager.conf
%config %{_sysconfdir}/dbus-1/system.d/nm-dispatcher.conf
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/VPN
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%dir %{_sysconfdir}/NetworkManager/system-connections
%attr(0755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/nfs
%{_unitdir}/NetworkManager.service
%{_unitdir}/NetworkManager-dispatcher.service
%{_unitdir}/NetworkManager-wait-online.service
%dir %{_unitdir}/NetworkManager.service.d
%{_unitdir}/NetworkManager.service.d/NetworkManager-ovs.conf
%{_udevdir}/rules.d/84-nm-drivers.rules
%{_udevdir}/rules.d/85-nm-unmanaged.rules
%{_udevdir}/rules.d/90-nm-thunderbolt.rules
%{_unitdir}/nm-cloud-setup.service
%{_unitdir}/nm-cloud-setup.timer
%ghost %config(noreplace) %{_localstatedir}/log/NetworkManager
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/no-wait.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/pre-up.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/pre-down.d
%dir %{_prefix}/lib/NetworkManager/VPN
%{_prefix}/lib/NetworkManager/dispatcher.d/90-nm-cloud-setup.sh
%{_prefix}/lib/NetworkManager/dispatcher.d/no-wait.d/90-nm-cloud-setup.sh
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/zones
%{_prefix}/lib/firewalld/zones/nm-shared.xml

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
%config(noreplace) %{_sysconfdir}/NetworkManager/NetworkManager.conf

%changelog
