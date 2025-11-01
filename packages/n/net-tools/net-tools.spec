#
# spec file for package net-tools
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# The real version is 2.10. But we dropped downstream ether-wake, so bump version to detect this change.
# When an upstream update will appear, return back lines marked with #E#
%define _version 2.10
Version:        2.10+1
Release:        0
Summary:        Important Programs for Networking
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://sourceforge.net/projects/net-tools/
#E#Source:         https://sourceforge.net/projects/net-tools/files/net-tools-%%{version}.tar.xz
Source:         https://sourceforge.net/projects/net-tools/files/net-tools-%{_version}.tar.xz
# PATCH-FEATURE-SUSE: set configure values to our liking as we do not need
# everything here
Patch0:         net-tools-configure.patch
Patch7:         0007-Introduce-T-notrim-option-in-netstat.patch
# PATCH-FIX-SECURITY net-tools-CVE-2025-46836.patch bsc1243581 sbrabec@suse.com -- Perform bound checks when parsing interface labels in /proc/net/dev.
Patch8:         net-tools-CVE-2025-46836.patch
# PATCH-FIX-UPSTREAM net-tools-CVE-2025-46836-regression.patch bsc1243581 sbrabec@suse.com -- Fix regression introduced by net-tools-CVE-2025-46836.patch.
Patch9:         net-tools-CVE-2025-46836-regression.patch
# PATCH-FIX-UPSTREAM net-tools-CVE-2025-46836-error-reporting.patch bsc1243581 sbrabec@suse.com -- Provide more readable error for interface name size checking.
Patch10:        net-tools-CVE-2025-46836-error-reporting.patch
# PATCH-FIX-SECURITY net-tools-parse_hex-stack-overflow.patch bsc1248410 sbrabec@suse.com -- Fix stack buffer overflow in parse_hex.
Patch11:        net-tools-parse_hex-stack-overflow.patch
# PATCH-FIX-SECURITY net-tools-proc_gen_fmt-buffer-overflow.patch bsc1248410 sbrabec@suse.com -- Fix stack-based buffer overflow in proc_gen_fmt.
Patch12:        net-tools-proc_gen_fmt-buffer-overflow.patch
# PATCH-FIX-SECURITY net-tools-ifconfig-avoid-unsafe-memcpy.patch bsc1248410 sbrabec@suse.com -- Avoid unsafe memcpy in ifconfig.
Patch13:        net-tools-ifconfig-avoid-unsafe-memcpy.patch
# PATCH-FIX-SECURITY net-tools-ax25+netrom-overflow-1.patch bsc1248410 sbrabec@suse.com -- Prevent overflow in ax25 and netrom.
Patch14:        net-tools-ax25+netrom-overflow-1.patch
# PATCH-FIX-SECURITY net-tools-ax25+netrom-overflow-2.patch bsc1248410 sbrabec@suse.com -- Prevent overflow in ax25 and netrom.
Patch15:        net-tools-ax25+netrom-overflow-2.patch
# PATCH-FIX-UPSTREAM net-tools-ifconfig-long-name-warning.patch bsc1248410 sbrabec@suse.com -- Allow to enter long interface names again.
Patch16:        net-tools-ifconfig-long-name-warning.patch
BuildRequires:  help2man
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
%setup -q -n %{name}-%{_version}
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
for i in ether-wake nameif plipconfig slattach arp ipmaddr iptunnel; do
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
