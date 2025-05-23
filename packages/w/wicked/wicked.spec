#
# spec file for package wicked
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


%define		release_prefix  %{?snapshot:%{snapshot}}%{!?snapshot:0}
Name:           wicked
Version:        0.6.78
Release:        %{release_prefix}.0.0
Summary:        Network configuration infrastructure
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/openSUSE/wicked
Source0:        %{name}-%{version}.tar.bz2
Source1:        wicked-rpmlintrc
#
# Upstream First - openSUSE Build Service Policy:
#
# Never add any patches to this package without the upstream commit id in
# the patch. Any patches added here without a very good reason to make an
# exception will be silently removed with the next version update.
# Note, that wicked.spec file is generated from wicked.spec.in which is in git.
# Please use pull requests at https://github.com/openSUSE/wicked/ instead.
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
%if %{with wicked_devel}
# libwicked-%%{version}.so shlib package compatible match for wicked-devel
Provides:       libwicked-0_6_78 = %{version}-%{release}
%endif
# uninstall obsolete libwicked-0-6 (libwicked-0.so.6, wicked < 0.6.60)
Provides:       libwicked-0-6 = %{version}
Obsoletes:      libwicked-0-6 < %{version}

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150500
%bcond_without  nbft
%else
%bcond_with     nbft
%endif
%if 0%{?suse_version} >= 1500
%bcond_without  rfc4361_cid
%else
%bcond_with     rfc4361_cid
%endif
%if 0%{?suse_version} >= 1500
%bcond_without  dhcp6_nis
%else
%bcond_with     dhcp6_nis
%endif

# optional and disabled (not needed): enable man page
# template rebuild from md sources using pandoc(-cli)
%bcond_with	pandoc

%if %{with pandoc}
BuildRequires:  pandoc
%endif

%bcond_with     wicked_devel

# Note: teamd is enabled by default
%bcond_without  use_teamd

# Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
%define _fillupdir /var/adm/fillup-templates
%endif

BuildRequires:  libnl3-devel
BuildRequires:  dbus-1-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config

# Prerequire the logger package
%if 0%{?suse_version} > 1310
Requires(pre):       util-linux-systemd
%else
Requires(pre):       util-linux
%endif

BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
%{?systemd_requires}
%if 0%{?suse_version:1}
Requires(pre):  %fillup_prereq
Requires:       sysconfig-netconfig
%endif
Requires:       %{name}-service = %{version}
%if %{defined _rundir}
%define         wicked_piddir   %_rundir/%{name}
%define         wicked_statedir %_rundir/%{name}
%else
%define         wicked_piddir   %_localstatedir/run/%{name}
%define         wicked_statedir %_localstatedir/run/%{name}
%endif
%define         wicked_storedir %_localstatedir/lib/%{name}
%if 0%{?suse_version} >= 1550
%define		dbus_config_base %_datadir/dbus-1
%define		dbus_config_tag	 %nil
%else
%define		dbus_config_base %_sysconfdir/dbus-1
%define		dbus_config_tag	 %config
%endif

%description
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

%if %{with nbft}

%package nbft
Summary:        Network configuration infrastructure - nbft support
Group:          System/Management
Requires:       %name = %{version}
# Support for the "nvme nbft show" command
Requires:       nvme-cli >= 2.4+17.gf4cfca93998a
Requires:       jq >= 1.6

%description nbft
This package provides an extension to retrieve the NBFT firmware
network interface configuration according to the NVM Express Boot
Specification 1.0 and convert it to wicked configuration.

%endif

%package service
Summary:        Network configuration infrastructure - systemd service
Group:          System/Management
Requires(pre):  %name = %{version}
Requires:       sysconfig >= 0.81.0
Provides:       /sbin/ifup
Provides:       service(network)
Provides:       sysvinit(network)
Conflicts:      otherproviders(/sbin/ifup)

%description service
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked systemd service files.


%if %{with wicked_devel}
%package devel
Summary:        Network configuration infrastructure - Development files
Group:          Development/Libraries/C and C++
Requires:       dbus-1-devel
Requires:       libnl3-devel
Requires:       libwicked-0_6_78 = %{version}-%{release}

%description devel
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked development files.
%endif

%prep
%setup

%build
test -x ./configure || autoreconf --force --install
export CFLAGS="-std=gnu89 $RPM_OPT_FLAGS -fPIC" LDFLAGS="-pie"
%configure \
	--with-piddir=%{wicked_piddir}	\
	--with-statedir=%{wicked_statedir}\
	--with-storedir=%{wicked_storedir}\
	--with-compat=suse		\
	--with-fillup-templatesdir=%{_fillupdir}\
%if %{without dhcp6_nis}
	--disable-dhcp6-nis		\
%endif
%if %{without rfc4361_cid}
	--disable-dhcp4-rfc4361-cid	\
%endif
%if %{without use_teamd}
	--disable-teamd			\
%endif
%if %{without nbft}
	--disable-nbft			\
%endif
	--enable-systemd		\
	--with-systemd-unitdir=%{_unitdir} \
	--without-dbus-servicedir	\
	--with-dbus-configdir=%{dbus_config_base}/system.d \
%if %{without pandoc}
	--disable-pandoc		\
%endif
	--disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT}
%if 0%{?suse_version} < 1550
# install /sbin/{ifup,ifown,ifstatus,ifprobe} links
%__mkdir_p -m 0755 ${RPM_BUILD_ROOT}/sbin
%__ln_s %_sbindir/ifup	${RPM_BUILD_ROOT}/sbin/ifup
%endif
for i in ifdown ifstatus ifprobe; do
%if 0%{?suse_version} < 1550
%__ln_s ifup ${RPM_BUILD_ROOT}/sbin/$i
%else
%__ln_s ifup ${RPM_BUILD_ROOT}%{_sbindir}/$i
%endif
done
# remove libwicked.a and la
%__rm -f ${RPM_BUILD_ROOT}%_libdir/libwicked*.*a
# create reboot-persistent (leases) store directory
%__mkdir_p -m 0750 ${RPM_BUILD_ROOT}%{wicked_storedir}
ln -sf service ${RPM_BUILD_ROOT}%_sbindir/rcwicked
ln -sf service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd
ln -sf service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-nanny
ln -sf service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-dhcp6
ln -sf service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-dhcp4
ln -sf service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-auto4

%if %{without wicked_devel}
pushd $RPM_BUILD_ROOT
rm -rfv \
	.%_libdir/libwicked.so \
	.%_datadir/pkgconfig/wicked.pc \
	.%_mandir/man7/wicked.7* \
	.%_includedir/wicked
popd
%endif

%pre service
%{service_add_pre wicked.service}

%post service
%{service_add_post wicked.service}
# See bnc#843526: presets do not apply for upgrade / are not sufficient
#                 to handle sysconfig-network|wicked -> wicked migration
_id=`readlink /etc/systemd/system/network.service 2>/dev/null` || :
case "${_id##*/}" in
""|wicked.service|network.service)
	/usr/bin/systemctl --system daemon-reload || :
	/usr/bin/systemctl --force enable wicked.service || :
;;
esac

%preun service
# stop the daemons on removal
# - stopping wickedd should be sufficient ... other just to be sure.
# - stopping of the wicked.service does not stop network, but removes
#   the wicked.service --> network.service link and resets its status.
%{service_del_preun wickedd.service wickedd-auto4.service wickedd-dhcp4.service wickedd-dhcp6.service wickedd-nanny.service wicked.service}

%postun service
# restart wickedd after upgrade
%{service_del_postun wickedd.service}

%post
/sbin/ldconfig
%{fillup_only -dns config wicked network}
%{fillup_only -dns dhcp wicked network}
# reload dbus after install or upgrade to apply new policies
/usr/bin/systemctl reload dbus.service 2>/dev/null || :
# migrate `wicked redfish enable` to `wicked firmware enable`
if test -f %_sysconfdir/wicked/client-redfish.xml -a \
      ! -f %_sysconfdir/wicked/client-firmware.xml ; then
	mv -f -- %_sysconfdir/wicked/client-redfish.xml \
		 %_sysconfdir/wicked/client-firmware.xml || :
fi
rm -f -- %_sysconfdir/wicked/client-redfish.xml || :

%postun
/sbin/ldconfig
# reload dbus after uninstall, our policies are gone again
if [ ${FIRST_ARG:-$1} -eq 0 ]; then
	/usr/bin/systemctl reload dbus.service 2>/dev/null || :
fi

%if %{with nbft}

%postun nbft
# revert nbft override in client-firmware.xml config
if [ ${FIRST_ARG:-$1} -eq 0 ]; then
	%_sbindir/wicked firmware revert nbft 2>/dev/null || :
fi

%endif

%files
%defattr (-,root,root)
%doc ChangeLog ANNOUNCE README TODO samples
%license COPYING
%_sbindir/wicked
%_sbindir/wickedd
%_sbindir/wickedd-nanny
%_libdir/libwicked-*.so*
%dir %_libexecdir/%{name}
%dir %_libexecdir/%{name}/bin
%_libexecdir/%{name}/bin/wickedd-auto4
%_libexecdir/%{name}/bin/wickedd-dhcp4
%_libexecdir/%{name}/bin/wickedd-dhcp6
%dir %_sysconfdir/wicked
%config(noreplace) %_sysconfdir/wicked/common.xml
%config(noreplace) %_sysconfdir/wicked/client.xml
%config(noreplace) %_sysconfdir/wicked/server.xml
%config(noreplace) %_sysconfdir/wicked/nanny.xml
%dir %_sysconfdir/wicked/scripts
%config(noreplace) %_sysconfdir/wicked/scripts/*
%dir %_sysconfdir/wicked/extensions
%config(noreplace) %_sysconfdir/wicked/extensions/dispatch
%config(noreplace) %_sysconfdir/wicked/extensions/firewall
%config(noreplace) %_sysconfdir/wicked/extensions/hostname
%config(noreplace) %_sysconfdir/wicked/extensions/ibft
%config(noreplace) %_sysconfdir/wicked/extensions/netconfig
%config(noreplace) %_sysconfdir/wicked/extensions/redfish-config
%dir %_sysconfdir/wicked/ifconfig
%dir %{dbus_config_base}
%dir %{dbus_config_base}/system.d
# mark the policies as config to keep backup, but replace on upgrade
%{dbus_config_tag} %{dbus_config_base}/system.d/org.opensuse.Network.conf
%{dbus_config_tag} %{dbus_config_base}/system.d/org.opensuse.Network.AUTO4.conf
%{dbus_config_tag} %{dbus_config_base}/system.d/org.opensuse.Network.DHCP4.conf
%{dbus_config_tag} %{dbus_config_base}/system.d/org.opensuse.Network.DHCP6.conf
%{dbus_config_tag} %{dbus_config_base}/system.d/org.opensuse.Network.Nanny.conf
%dir %_datadir/wicked
%dir %_datadir/wicked/schema
%_datadir/wicked/schema/*.xml
%_mandir/man5/wicked-config.5*
%_mandir/man5/ifcfg-bond.5*
%_mandir/man5/ifcfg-bonding.5*
%_mandir/man5/ifcfg-bridge.5*
%_mandir/man5/ifcfg-dummy.5*
%_mandir/man5/ifcfg-infiniband.5*
%_mandir/man5/ifcfg-ipoib.5*
%_mandir/man5/ifcfg-ipvlan.5*
%_mandir/man5/ifcfg-ipvtap.5*
%_mandir/man5/ifcfg-macvlan.5*
%_mandir/man5/ifcfg-macvtap.5*
%_mandir/man5/ifcfg-ppp.5*
%_mandir/man5/ifcfg-ovs-bridge.5*
%_mandir/man5/ifcfg-team.5*
%_mandir/man5/ifcfg-tunnel.5*
%_mandir/man5/ifcfg-vlan.5*
%_mandir/man5/ifcfg-vxlan.5*
%_mandir/man5/ifcfg-wireless.5*
%_mandir/man5/ifcfg-dhcp.5*
%_mandir/man5/ifcfg-lo.5*
%_mandir/man5/ifcfg.5*
%_mandir/man5/ifroute.5*
%_mandir/man5/ifrule.5*
%_mandir/man5/ifsysctl.5*
%_mandir/man5/routes.5*
%_mandir/man8/wicked.8*
%_mandir/man8/wickedd.8*
%_mandir/man8/wicked-ethtool.8*
%_mandir/man8/wicked-firmware.8*
%_mandir/man8/wicked-redfish.8*
%_mandir/man8/ifdown.8*
%_mandir/man8/ifstatus.8*
%_mandir/man8/ifup.8*
%_fillupdir/sysconfig.config-wicked
%_fillupdir/sysconfig.dhcp-wicked
%attr(0750,root,root) %dir        %wicked_storedir

%if %{with nbft}

%files nbft
%config(noreplace) %_sysconfdir/wicked/client-nbft.xml
%config(noreplace) %_sysconfdir/wicked/extensions/nbft

%endif

%files service
%defattr (-,root,root)
%_unitdir/wickedd-auto4.service
%_unitdir/wickedd-dhcp4.service
%_unitdir/wickedd-dhcp6.service
%_unitdir/wickedd-nanny.service
%_unitdir/wickedd.service
%_unitdir/wicked.service
%_unitdir/wickedd-pppd@.service
%dir /etc/sysconfig/network
%attr(0600,root,root) %config /etc/sysconfig/network/ifcfg-lo
%_sbindir/ifup
%if 0%{?suse_version} < 1550
/sbin/ifup
/sbin/ifdown
/sbin/ifstatus
/sbin/ifprobe
%else
%_sbindir/ifdown
%_sbindir/ifstatus
%_sbindir/ifprobe
%endif
%_sbindir/rcwickedd-nanny
%_sbindir/rcwickedd-dhcp6
%_sbindir/rcwickedd-dhcp4
%_sbindir/rcwickedd-auto4
%_sbindir/rcwickedd
%_sbindir/rcwicked

%if %{with wicked_devel}
%files devel
%defattr (-,root,root)
%dir %_includedir/wicked
%_includedir/wicked/*
%_libdir/libwicked.so
%_datadir/pkgconfig/wicked.pc
%_mandir/man7/wicked.7*
%endif

%changelog
