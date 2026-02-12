#
# spec file for package keepalived
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.3.4+git23.b3631012
Release:        0
Summary:        A keepalive facility for Linux
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Routing
URL:            https://www.keepalived.org/
Source:         %{name}-%{version}.tar.xz
Source3:        tmpfile.conf
Source4:        users.conf
Patch1:         harden_keepalived.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file-devel
BuildRequires:  libtool
BuildRequires:  make
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
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libsystemd)
%{?systemd_ordering}
%sysusers_requires

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
%autosetup -p1  -n %{name}-%{version}
chmod 644 doc/samples/*

%build
export STRIP=true
export CPPFLAGS="$(pkg-config --cflags libnfnetlink libiptc libipset xtables)"
export CFLAGS="%optflags -DOPENSSL_NO_SSL_INTERN"
./autogen.sh
#  --enable-dbus-create-instance \
%configure \
  --disable-silent-rules \
  --docdir=%{_defaultdocdir}/%{name}/ \
  --enable-bfd \
  %if %{with json}
  --enable-json \
  %endif
  --enable-snmp \
  --enable-snmp-rfc \
  %if %{with dbus}
  --enable-dbus \
  %endif
  %if %{with keepalived_regex}
  --enable-regex \
  %endif
  %if %{with keepalived_nftables}
  --enable-nftables \
  --disable-iptables \
  %else
  --enable-iptables \
  --enable-libipset \
  %endif
  --enable-systemd \
  --with-init=systemd \
  --with-systemdsystemunitdir="%{_unitdir}" \
  --enable-sha1 \
  --enable-gnu-std-paths \
  --enable-hardening \
  --enable-log-file \
  --enable-routes \
  --disable-dynamic-linking \
  --disable-libiptc-dynamic \
  --disable-libipset-dynamic \
  --disable-libnl-dynamic \
  --enable-libnl \
  --enable-json
make %{?_smp_mflags}
%sysusers_generate_pre %{SOURCE12} %{name} %{S:4}

%install
%make_install
install -dD -m 0750 %{buildroot}%{_var}/lib/%{name}
install -D  -m 0644 %{buildroot}/etc/sysconfig/%{name} %{buildroot}%{_fillupdir}/sysconfig.%{name}

ln -s /sbin/service %{buildroot}%{_sbindir}/rckeepalived

chmod -R o= %{buildroot}/etc/%{name}
rm -rv %{buildroot}/etc/%{name}/samples/ %{buildroot}/etc/sysconfig/%{name}
cp -rv \
  AUTHOR ChangeLog CONTRIBUTORS README doc/samples/ doc/%{name}.conf.SYNOPSIS doc/NOTE_vrrp_vmac.txt \
  %{buildroot}%{_defaultdocdir}/%{name}/

mkdir -p %{buildroot}%{_tmpfilesdir}/
install -D -m 0644 %{S:3} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%check
# A build could silently have LVS support disabled if the kernel includes can't
# be properly found, we need to avoid that.
if ! grep -q "#define _WITH_LVS_ *1" lib/config.h; then
    %{__echo} "ERROR: We do not want keepalived lacking LVS support." >&2
    exit 1
fi

%pre  -f %{name}.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%fillup_only %{name}
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%license COPYING
%doc %{_defaultdocdir}/%{name}/
%dir  %{_sysconfdir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%ghost %dir /var/lib/%{name}
%config(noreplace) %ghost %attr(0640,root,root) %{_sysconfdir}/%{name}/%{name}.conf
%config %attr(0640,root,root) %{_sysconfdir}/%{name}/%{name}.conf.sample
%{_fillupdir}/sysconfig.%{name}
%{_bindir}/genhash
%{_sbindir}/rckeepalived
%{_sbindir}/%{name}
%{_mandir}/man1/genhash.1*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%{_datadir}/snmp/mibs/KEEPALIVED-MIB.txt
%{_datadir}/snmp/mibs/VRRP-MIB.txt
%{_datadir}/snmp/mibs/VRRPv3-MIB.txt
#
%if %{with dbus}
%config /etc/dbus-1/system.d/org.%{name}.Vrrp1.conf
%{_datadir}/dbus-1/interfaces/org.%{name}.Vrrp1.Instance.xml
%{_datadir}/dbus-1/interfaces/org.%{name}.Vrrp1.Vrrp.xml
%endif
#
%{_unitdir}/%name.service

%changelog
