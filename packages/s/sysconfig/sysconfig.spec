#
# spec file for package sysconfig
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


#
# Upstream First - openSUSE Build Service Policy:
#
# Never add any patches to this package without the upstream commit id in
# the patch. Any patches added here without a very good reason to make an
# exception will be silently removed with the next version update.
# This .spec file is tracked in git as well.
# Please use pull requests at https://github.com/openSUSE/sysconfig/ instead.
#

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} >= 1550
%bcond_with     ifuser
%else
%bcond_without  ifuser
%endif
%if 0%{?suse_version} >= 1230
%define         udevdir	%{_prefix}/lib/udev
BuildRequires:  pkgconfig(systemd)
%else
%define         udevdir	/lib/udev
%endif
Name:           sysconfig
Version:        0.90.0
Release:        0
Summary:        The sysconfig scheme for traditional network scripts
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/sysconfig
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires(post): %fillup_prereq
Requires(post): /usr/bin/grep
Requires(post): /usr/bin/chmod /usr/bin/mkdir /usr/bin/touch
%if 0%{?suse_version} < 1550
Requires:       /sbin/netconfig
Requires:       (sysvinit(network) or service(network))
Recommends:     wicked-service
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides the SUSE system configuration scheme for the
traditional "ifup" alias "netcontrol" network scripts.

%package netconfig
Summary:        Script to apply network provided settings
Group:          System/Base
Requires:       /bin/gawk
Requires:       /bin/logger
Requires(pre):  sysconfig = %{version}
Provides:       /sbin/netconfig

%description netconfig
This package provides the netconfig scripts to apply network
provided settings like DNS or NIS into system files.

%prep
%setup -q

%build
autoreconf -fvi
CFLAGS="%{optflags} -fPIC" LDFLAGS="-pie" \
%configure --prefix=/ \
            --sbindir=%{_sbindir} \
            --libdir=%{_libdir} \
            --sysconfdir=%{_sysconfdir} \
            --libexecdir=%{_libexecdir} \
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
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/network/scripts
ln -s %{_libexecdir}/netconfig/functions.netconfig \
      %{buildroot}%{_sysconfdir}/sysconfig/network/scripts
%if !0%{?usrmerged}
mkdir -p %{buildroot}/sbin
ln -s %{_sbindir}/netconfig %{buildroot}/sbin/netconfig
%endif
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcnetwork
rm -f %{buildroot}%{_docdir}/sysconfig/COPYING
%if %{without ifuser}
rm -f %{buildroot}%{_sbindir}/ifuser
%endif

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
%dir %{_sysconfdir}/sysconfig/network
%config %{_sysconfdir}/sysconfig/network/ifcfg.template
%ghost %{_sysconfdir}/sysconfig/network/config
%ghost %{_sysconfdir}/sysconfig/network/dhcp
%dir %{_docdir}/sysconfig
%doc %{_docdir}/sysconfig/Contents
%{_fillupdir}/sysconfig.dhcp-network
%{_fillupdir}/sysconfig.config-network
%{_sbindir}/rcnetwork
%if %{with ifuser}
%{_sbindir}/ifuser
%endif
%dir %attr(0750,root,root) %{_libexecdir}/ppp
%dir %{_libexecdir}/ppp/ip-up.d
%dir %{_libexecdir}/ppp/ip-down.d
%dir %{_libexecdir}/ppp/ipv6-up.d
%dir %{_libexecdir}/ppp/ipv6-down.d
%dir %{_libexecdir}/ppp/ip-pre-up.d
%dir %{_libexecdir}/ppp/pre-start.d
%dir %{_libexecdir}/ppp/post-stop.d
%{_libexecdir}/ppp/ip-up
%dir %attr(0750,root,root) %{_sysconfdir}/ppp
%dir %{_sysconfdir}/ppp/ip-up.d
%dir %{_sysconfdir}/ppp/ip-down.d
%dir %{_sysconfdir}/ppp/ipv6-up.d
%dir %{_sysconfdir}/ppp/ipv6-down.d
%dir %{_sysconfdir}/ppp/ip-pre-up.d
%dir %{_sysconfdir}/ppp/pre-start.d
%dir %{_sysconfdir}/ppp/post-stop.d
%{_sysconfdir}/ppp/ip-up
%{_sysconfdir}/ppp/ip-down
%{_sysconfdir}/ppp/ipv6-up
%{_sysconfdir}/ppp/ipv6-down
%{_sysconfdir}/ppp/ip-pre-up
%{_sysconfdir}/ppp/post-stop
%{_sysconfdir}/ppp/pre-start

%files netconfig
%defattr(-,root,root)
%dir %{_libexecdir}/netconfig
%dir %{_libexecdir}/netconfig/ppp
%dir %{_libexecdir}/netconfig/netconfig.d
%{_libexecdir}/netconfig/netconfig.d/*
%{_libexecdir}/netconfig/functions.netconfig
%dir %{_sysconfdir}/sysconfig/network/scripts
%{_sysconfdir}/sysconfig/network/scripts/functions.netconfig
%{_sbindir}/netconfig
%if !0%{?usrmerged}
/sbin/netconfig
%endif
%{_mandir}/man8/netconfig.8%{ext_man}
%doc %{_docdir}/sysconfig/netconfig.png
%{_libexecdir}/netconfig/ppp/ip-up
%{_libexecdir}/ppp/ip-up.d/10-netconfig
%{_libexecdir}/ppp/ip-down.d/90-netconfig
%{_libexecdir}/ppp/pre-start.d/10-netconfig
%{_libexecdir}/ppp/post-stop.d/90-netconfig
%{_tmpfilesdir}/netconfig.conf
%ghost %dir /run/netconfig
%ghost /run/netconfig/resolv.conf
%ghost /run/netconfig/yp.conf
%ghost /etc/resolv.conf
%ghost %config(noreplace) %{_sysconfdir}/yp.conf

%post -p /bin/bash
%{fillup_only -dns dhcp network network}
%{fillup_only -dns config network network}
/sbin/ldconfig

%postun -p /sbin/ldconfig

%post netconfig -p /bin/bash
%tmpfiles_create %{_tmpfilesdir}/netconfig.conf

%changelog
