#
# spec file for package sysconfig
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} >= 1230
%define         udevdir	%{_prefix}/lib/udev
BuildRequires:  pkgconfig(systemd)
%else
%define         udevdir	/lib/udev
%endif
Name:           sysconfig
Version:        0.85.6
Release:        0
Summary:        The sysconfig scheme for traditional network scripts
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/sysconfig
Source:         %{name}-%{version}.tar.bz2
#
# Upstream First - openSUSE Build Service Policy:
#
# Never add any patches to this package without the upstream commit id in
# the patch. Any patches added here without a very good reason to make an
# exception will be silently removed with the next version update.
# Please use pull requests at https://github.com/openSUSE/sysconfig/ instead.
#
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       /sbin/ifup
Requires:       /sbin/netconfig
Requires:       sysvinit(network)
Requires(post): %fillup_prereq
Requires(post): /usr/bin/grep
Requires(post): /usr/bin/chmod /usr/bin/mkdir /usr/bin/touch
Recommends:     wicked-service
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides the SUSE system configuration scheme for the
traditional "ifup" alias "netcontrol" network scripts.

%package netconfig
Summary:        Script to apply network provided settings
Group:          System/Base
Requires:       /bin/gawk
Requires:       /bin/logger
Requires:       /usr/bin/sed
Requires(pre):  sysconfig = %{version}
Provides:       /sbin/netconfig

%description netconfig
This package provides the netconfig scripts to apply network
provided settings like DNS or NIS into system files.

%prep
%setup -q

%build
autoreconf -fvi
CFLAGS="%{optflags} -fPIC" \
%configure --prefix=/ \
            --sbindir=/sbin \
            --libdir=/%{_lib} \
            --sysconfdir=%{_sysconfdir} \
            --mandir=%{_mandir} \
            --with-unitdir=%{_unitdir} \
            --with-udevdir=%{udevdir} \
            --with-fillup-templatesdir=%{_fillupdir}
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
touch %{buildroot}%{_sysconfdir}/sysconfig/network/config
touch %{buildroot}%{_sysconfdir}/sysconfig/network/dhcp
mkdir -p %{buildroot}/sbin
ln -s /sbin/service %{buildroot}/sbin/rcnetwork
rm -f %{buildroot}%{_docdir}/sysconfig/COPYING

mkdir -p %{buildroot}%{_tmpfilesdir}
cat >%{buildroot}%{_tmpfilesdir}/netconfig.conf <<-EOF
	d /run/netconfig 0755 root root -
	f /run/netconfig/resolv.conf 0644 root root -
	f /run/netconfig/yp.conf 0644 root root -
	L /etc/resolv.conf - - - - /run/netconfig/resolv.conf
	L /etc/yp.conf - - - - /run/netconfig/yp.conf
EOF

%files
%defattr(-,root,root)
%license doc/COPYING
%config %{_sysconfdir}/sysconfig/network/ifcfg.template
%ghost %{_sysconfdir}/sysconfig/network/config
%ghost %{_sysconfdir}/sysconfig/network/dhcp
%dir %{_docdir}/sysconfig
%doc %{_docdir}/sysconfig/Contents
%{_sysconfdir}/sysconfig/network/scripts/functions.rpm-utils
%{_fillupdir}/sysconfig.dhcp-network
%{_fillupdir}/sysconfig.config-network
/sbin/rcnetwork
/sbin/ifuser
%dir %attr(0750,root,root) %{_sysconfdir}/ppp
%dir %{_sysconfdir}/ppp/ip-up.d
%dir %{_sysconfdir}/ppp/ip-down.d
%dir %{_sysconfdir}/ppp/ipv6-up.d
%dir %{_sysconfdir}/ppp/ipv6-down.d
%dir %{_sysconfdir}/ppp/pre-start.d
%dir %{_sysconfdir}/ppp/post-stop.d
%{_sysconfdir}/ppp/ip-up
%{_sysconfdir}/ppp/ip-down
%{_sysconfdir}/ppp/ipv6-up
%{_sysconfdir}/ppp/ipv6-down
%{_sysconfdir}/ppp/post-stop
%{_sysconfdir}/ppp/pre-start

%files netconfig
%defattr(-,root,root)
%dir %{_sysconfdir}/netconfig.d
%{_sysconfdir}/netconfig.d/*
%{_sysconfdir}/sysconfig/network/scripts/functions.netconfig
/sbin/netconfig
%{_mandir}/man8/netconfig.8%{ext_man}
%doc %{_docdir}/sysconfig/netconfig.png
%{_sysconfdir}/ppp/netconfig
%{_sysconfdir}/ppp/ip-up.d/10-netconfig
%{_sysconfdir}/ppp/ip-down.d/90-netconfig
%{_sysconfdir}/ppp/pre-start.d/10-netconfig
%{_sysconfdir}/ppp/post-stop.d/90-netconfig
%{_tmpfilesdir}/netconfig.conf
%ghost %dir /run/netconfig
%ghost /run/netconfig/resolv.conf
%ghost /run/netconfig/yp.conf
%ghost /etc/resolv.conf
%ghost %config(noreplace) %{_sysconfdir}/yp.conf

%post -p /bin/bash
#
## we provide own, improved variant of the remove_and_set suse
## rpm macro that is able to handle files in subdirs, and more
. etc/sysconfig/network/scripts/functions.rpm-utils
#
# remove obsolete sysconfig-network specific variables
sysconfig_remove_and_set network/config NOZEROCONF
sysconfig_remove_and_set network/config LINKLOCAL_INTERFACES
sysconfig_remove_and_set network/config IFPLUGD_OPTIONS
sysconfig_remove_and_set network/config DEFAULT_BROADCAST
sysconfig_remove_and_set network/config FORCE_PERSISTENT_NAMES
sysconfig_remove_and_set network/config MANDATORY_DEVICES
sysconfig_remove_and_set network/config USE_SYSLOG
sysconfig_remove_and_set network/dhcp   DHCLIENT_BIN
sysconfig_remove_and_set network/dhcp   DHCLIENT6_BIN
sysconfig_remove_and_set network/dhcp   DHCLIENT_DEBUG
sysconfig_remove_and_set network/dhcp   DHCLIENT_WAIT_LINK
sysconfig_remove_and_set network/dhcp   DHCLIENT_USER_OPTIONS
sysconfig_remove_and_set network/dhcp   DHCLIENT_PRIMARY_DEVICE
sysconfig_remove_and_set network/dhcp   DHCLIENT6_USER_OPTIONS
sysconfig_remove_and_set network/dhcp   DHCPCD_USER_OPTIONS
sysconfig_remove_and_set network/dhcp   DHCP6C_USER_OPTIONS
##
%{fillup_only -dns dhcp network network}
%{fillup_only -dns config network network}
/sbin/ldconfig
# remove obsolete dhcp and per interface variables
_umask=`umask`
for file in etc/sysconfig/network/dhcp etc/sysconfig/network/ifcfg-* ; do
	name="${file##*\/ifcfg-}"
	case $name in
	(lo|""|*" "*|*~|*.old|*.rpmnew|*.rpmsave|*.scpmbackup) continue ;;
	esac
	case $file in
		(*/ifcfg-*) umask 0177 ;;
	esac
	sysconfig_remove_and_set -b "" $file \
		DHCLIENT_MODIFY_NTP_CONF     \
		DHCLIENT_ADDITIONAL_OPTIONS  \
		DHCLIENT_SCRIPT_EXE
	umask $_umask
done
# be a little bit paranoid and set the correct mode even we set umask
chmod 0600 etc/sysconfig/network/ifcfg-* 2>/dev/null || :

%postun -p /sbin/ldconfig

%post netconfig -p /bin/bash
%tmpfiles_create %{_tmpfilesdir}/netconfig.conf

%changelog
