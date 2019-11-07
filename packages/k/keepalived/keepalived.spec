#
# spec file for package keepalived
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} > 1210
%bcond_without systemd
%else
%bcond_with    systemd
%endif

%if 0%{?suse_version} > 1500
%bcond_without dbus
%bcond_without keepalived_nftables
%else
%bcond_with    dbus
%bcond_with    keepalived_nftables
%endif

%if 0%{?suse_version} >= 1500
%bcond_without keepalived_regex
%else
%bcond_with    keepalived_regex
%endif
%bcond_without json

Name:           keepalived
Version:        2.0.19
Release:        0
Summary:        A keepalive facility for Linux
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Routing
Url:            http://www.keepalived.org/
Source:         http://www.keepalived.org/software/%{name}-%{version}.tar.gz
Source2:        keepalive-rpmlintrc
Patch1:         keepalive-init.patch
# PATCH-FIX-UPSTREAM: https://github.com/acassen/keepalived/commit/947248af144bcab6376ccddab8dc40f313b14281.patch
Patch2:         linux-4.15.patch
BuildRequires:  file-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
BuildRequires:  snmp-mibs
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(openssl)
%if %{with json}
BuildRequires:  pkgconfig(json-c)
%endif
BuildRequires:  pkgconfig(libipset)
BuildRequires:  pkgconfig(libiptc)
BuildRequires:  pkgconfig(libnl-3.0)
%if %{with keepalived_regex}
BuildRequires:  pkgconfig(libpcre2-8)
%endif
BuildRequires:  pkgconfig(libnfnetlink)
%if %{with keepalived_nftables}
BuildRequires:  pkgconfig(libnftables)
BuildRequires:  pkgconfig(libnftnl)
%endif
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(xtables)
Requires(pre):  pwdutils
Requires(pre):  %fillup_prereq
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
Requires(pre):  %insserv_prereq
%endif

%description
This project provides facilities for load balancing and high-availability to
Linux system and Linux-based infrastructures. The load-balancing framework
relies on the Linux Virtual Server (IPVS) kernel module providing Layer4 load
balancing.  Keepalived implements a set of checkers to dynamically and
adaptively maintain and manage loadbalanced server pool according their health.
High-availability is achieved by the VRRP protocol, a fundamental brick for
router failover. In addition, Keepalived implements a set of hooks to the VRRP
finite state machine, providing low-level and high-speed protocol interactions.
Keepalived frameworks can be used independently or all together to provide
resilient infrastructures.

%prep
%setup -q
%patch1 -p1
%patch2 -p0
chmod 644 doc/samples/*

%build
export STRIP=true
export CPPFLAGS="$(pkg-config --cflags libnfnetlink libiptc libipset xtables)"
export CFLAGS="%optflags -DOPENSSL_NO_SSL_INTERN"
#  --enable-dbus-create-instance \
%configure \
  --disable-silent-rules \
  --enable-bfd \
  %if %{with json}
  --enable-json \
  %endif
  --enable-snmp \
  --enable-snmp-checker \
  --enable-snmp-vrrp \
  --enable-snmp-rfc \
  --enable-snmp-rfcv2 \
  --enable-snmp-rfcv3 \
  %if %{with dbus}
  --enable-dbus \
  %endif
  %if %{with keepalived_regex}
  --enable-regex \
  --enable-regex-timers \
  %endif
  %if %{with keepalived_nftables}
  --enable-nftables \
  %endif
  %if %{with systemd}
  --with-init=systemd \
  --with-systemdsystemunitdir="%{_unitdir}" \
  %endif
  --enable-sha1 \
  --enable-routes \
  --enable-iptables \
  --enable-dynamic-linking \
  --enable-libiptc \
  --enable-libiptc-dynamic \
  --enable-libipset \
  --enable-libipset-dynamic \
  --enable-libnl \
  --enable-libnl-dynamic \
  --enable-stacktrace \
  --enable-json
make %{?_smp_mflags}

%install
%make_install
install -dD -m 0750 %{buildroot}%{_var}/lib/%{name}
install -D  -m 0644 %{buildroot}/etc/sysconfig/keepalived %{buildroot}%{_fillupdir}/sysconfig.%{name}

%if %{with systemd}
ln -s /sbin/service %{buildroot}%{_sbindir}/rckeepalived
%else
install -D -m 0750 keepalived/etc/init.d/keepalived.suse.init %{buildroot}/etc/init.d/keepalived
ln -s /etc/init.d/keepalived %{buildroot}%{_sbindir}/rckeepalived
%endif

chmod -R o= %{buildroot}/etc/keepalived
rm -rv %{buildroot}/etc/keepalived/samples/ %{buildroot}/etc/sysconfig/keepalived

%check
# A build could silently have LVS support disabled if the kernel includes can't
# be properly found, we need to avoid that.
if ! grep -q "#define _WITH_LVS_ *1" lib/config.h; then
    %{__echo} "ERROR: We do not want keepalived lacking LVS support." >&2
    exit 1
fi

%pre
getent group %{name} >/dev/null || /usr/sbin/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	/usr/sbin/useradd -g %{name} -s /bin/false -r -c "Keepalived" \
	-d %{_var}/lib/%{name} %{name}
%if %{with systemd}
%service_add_pre %{name}.service
%endif

%preun
%if %{with systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%post
%fillup_only %{name}
%if %{with systemd}
%service_add_post %{name}.service
%endif

%postun
%if %{with systemd}
%service_del_postun %{name}.service
%else
%insserv_cleanup
%restart_on_update %{name}
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHOR ChangeLog CONTRIBUTORS README
%doc %{_datadir}/doc/keepalived/
%doc doc/samples/
%doc doc/keepalived.conf.SYNOPSIS doc/NOTE_vrrp_vmac.txt
%dir  %{_sysconfdir}/keepalived
%dir %attr(-,keepalived,keepalived) %{_var}/lib/%{name}
%{_fillupdir}/sysconfig.%{name}
%config(noreplace)  %{_sysconfdir}/keepalived/*conf
%{_bindir}/genhash
%{_sbindir}/rckeepalived
%{_sbindir}/keepalived
%{_mandir}/man1/genhash.1*
%{_mandir}/man5/keepalived.conf.5*
%{_mandir}/man8/keepalived.8*
%{_datadir}/snmp/mibs/KEEPALIVED-MIB.txt
%{_datadir}/snmp/mibs/VRRP-MIB.txt
%{_datadir}/snmp/mibs/VRRPv3-MIB.txt
#
%if %{with dbus}
%config /etc/dbus-1/system.d/org.keepalived.Vrrp1.conf
%{_datadir}/dbus-1/interfaces/org.keepalived.Vrrp1.Instance.xml
%{_datadir}/dbus-1/interfaces/org.keepalived.Vrrp1.Vrrp.xml
%endif
#
%if %{with systemd}
%{_unitdir}/%name.service
%else
/etc/init.d/keepalived
%endif

%changelog
