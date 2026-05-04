#
# spec file for package net-tools
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


Name:           net-tools
Version:        3.14~alpha~git.20251212.7011617
Release:        0
Summary:        Important Programs for Networking
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/ecki/net-tools
Source:         net-tools-%{version}.tar.xz
# PATCH-FEATURE-SUSE net-tools-configure.patch -- Set configure values to our liking as we do not need everything here.
Patch0:         net-tools-configure.patch
# PATCH-FIX-SECURITY net-tools-netstat-ansi-injection.patch bsc1254323 gh#ecki/net-tools#2109 CVE-2024-58251 sbrabec@suse.com -- Prevent denial of service via terminal escape sequences injection.
Patch1:         net-tools-netstat-ansi-injection.patch
BuildRequires:  bluez-devel
BuildRequires:  help2man
BuildRequires:  libselinux-devel
Recommends:     traceroute >= 2.0.0

%description
This package contains programs for network administration and maintenance.
Most of the utilities formerly contained in this package (netstat, arp,
ifconfig, rarp, route, ether-wake) are obsoleted by the tools from iproute2
package (ip, ss) and have been moved to net-tools-deprecated.

%package deprecated
Summary:        Deprecated Networking Utilities
Group:          Productivity/Networking/Other
Obsoletes:      %{name}-dummy

%description deprecated
This package contains the deprecated network utilities arp, ifconfig,
netstat and route, which have been replaced by tools from the iproute2
package:
  * arp -> ip [-r] neigh
  * ether-wake -> wol
    or use busybox-ether-wake
  * ifconfig -> ip addr
  * ipmaddr -> ip maddress
  * iptunnel -> ip tunnel
  * netstat -> ss [-r]
  * route -> ip route

%lang_package

%prep
#E#%%setup -q
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} config
make %{?_smp_mflags}

%install
%make_install BINDIR=%{_bindir} SBINDIR=%{_sbindir}
# remove rarp as it is not usefull with our kernel
rm -fv %{buildroot}%{_prefix}/*bin/rarp
rm -fv %{buildroot}/%{_mandir}/man*/rarp.*
rm -fv %{buildroot}/%{_mandir}/*/man*/rarp.*
# Fix manpage locations
mv %{buildroot}/%{_mandir}/de_DE %{buildroot}/%{_mandir}/de
mv %{buildroot}/%{_mandir}/fr_FR %{buildroot}/%{_mandir}/fr
# Generate missing manpages
for tool in iptunnel ipmaddr; do
  t="%{buildroot}/%{_mandir}/man8/${tool}.8"
  help2man -s8 "%{buildroot}%{_sbindir}/${tool}" --no-discard-stderr >"${t}"
done
# generate bin/sbin compat symlinks
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}/bin
for i in nameif plipconfig slattach arp ipmaddr iptunnel; do
ln -s %{_sbindir}/$i %{buildroot}/sbin/$i
done
for i in netstat ifconfig route; do
ln -s %{_bindir}/$i %{buildroot}/bin/$i
done
%endif
%find_lang %{name} --all-name

%files
%license COPYING
%doc README ABOUT-NLS
%{_sbindir}/nameif
%{_sbindir}/plipconfig
%{_sbindir}/slattach
%if 0%{?suse_version} < 1550
/sbin/nameif
/sbin/plipconfig
/sbin/slattach
%endif
%{_mandir}/de/man5/ethers.5%{?ext_man}
%{_mandir}/de/man8/plipconfig.8%{?ext_man}
%{_mandir}/de/man8/slattach.8%{?ext_man}
%{_mandir}/fr/man5/ethers.5%{?ext_man}
%{_mandir}/fr/man8/plipconfig.8%{?ext_man}
%{_mandir}/fr/man8/slattach.8%{?ext_man}
%{_mandir}/man5/ethers.5%{?ext_man}
%{_mandir}/man8/nameif.8%{?ext_man}
%{_mandir}/man8/plipconfig.8%{?ext_man}
%{_mandir}/man8/slattach.8%{?ext_man}

%files deprecated
%license COPYING
%{_bindir}/ifconfig
%{_bindir}/netstat
%{_bindir}/route
%if 0%{?suse_version} < 1550
/bin/ifconfig
/bin/netstat
/bin/route
/sbin/arp
/sbin/ipmaddr
/sbin/iptunnel
%endif
%{_sbindir}/arp
%{_sbindir}/ipmaddr
%{_sbindir}/iptunnel
%{_mandir}/de/man8/arp.8%{?ext_man}
%{_mandir}/de/man8/ifconfig.8%{?ext_man}
%{_mandir}/de/man8/netstat.8%{?ext_man}
%{_mandir}/de/man8/route.8%{?ext_man}
%{_mandir}/fr/man8/arp.8%{?ext_man}
%{_mandir}/fr/man8/ifconfig.8%{?ext_man}
%{_mandir}/fr/man8/netstat.8%{?ext_man}
%{_mandir}/fr/man8/route.8%{?ext_man}
%{_mandir}/man8/arp.8%{?ext_man}
%{_mandir}/man8/ifconfig.8%{?ext_man}
%{_mandir}/man8/netstat.8%{?ext_man}
%{_mandir}/man8/route.8%{?ext_man}
%{_mandir}/man8/ipmaddr.8%{?ext_man}
%{_mandir}/man8/iptunnel.8%{?ext_man}
%{_mandir}/pt_BR/man8/arp.8%{?ext_man}
%{_mandir}/pt_BR/man8/ifconfig.8%{?ext_man}
%{_mandir}/pt_BR/man8/netstat.8%{?ext_man}
%{_mandir}/pt_BR/man8/route.8%{?ext_man}

%files lang -f %{name}.lang

%changelog
