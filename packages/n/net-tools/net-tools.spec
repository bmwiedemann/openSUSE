#
# spec file for package net-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           net-tools
Version:        2.0+git20180626.aebd88e
Release:        0
Summary:        Important Programs for Networking
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://sourceforge.net/projects/net-tools/
# Repacked by the service file from git
Source:         %{name}-%{version}.tar.xz
# PATCH-FEATURE-SUSE: set configure values to our liking as we do not need
# everything here
Patch0:         net-tools-configure.patch
# Git formatted patches described in each patch
Patch1:         0001-Add-ether-wake-binary.patch
Patch2:         0002-Do-not-warn-about-interface-socket-not-binded.patch
Patch3:         0003-Add-support-for-EiB-in-interface.c.patch
Patch4:         0004-By-default-do-not-fopen-anything-in-netrom_gr.patch
Patch5:         0005-Add-support-for-interface-rename-in-nameif.patch
Patch6:         0006-Allow-interface-stacking.patch
Patch7:         0007-Introduce-T-notrim-option-in-netstat.patch
BuildRequires:  help2man
Requires:       hostname
Recommends:     %{name}-lang = %{version}
Recommends:     traceroute >= 2.0.0
Provides:       net_tool = %{version}
Obsoletes:      net_tool < %{version}

%description
This package contains programs for network administration and maintenance.
Most of the utilities formerly contained in this package (netstat, arp,
ifconfig, rarp, route) are obsoleted by the tools from iproute2 package (ip, ss)
and have been moved to net-tools-deprecated.

%package deprecated
Summary:        Deprecated Networking Utilities
Group:          Productivity/Networking/Other
Recommends:     %{name}-lang = %{version}

%description deprecated
This package contains the deprecated network utilities arp, ifconfig, netstat and route,
which have been replaced by tools from the iproute2 package:
  * arp -> ip [-r] neigh
  * ifconfig -> ip a
  * netstat -> ss [-r]
  * route -> ip r

%lang_package

%prep
%setup -q
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
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}/bin
for i in ether-wake nameif plipconfig slattach arp ipmaddr iptunnel; do
ln -s %{_sbindir}/$i %{buildroot}/sbin/$i
done
for i in netstat ifconfig route; do
ln -s %{_bindir}/$i %{buildroot}/bin/$i
done
%find_lang %{name} --all-name

%files
%license COPYING
%doc README ABOUT-NLS
%{_sbindir}/ether-wake
/sbin/ether-wake
%{_sbindir}/nameif
/sbin/nameif
%{_sbindir}/plipconfig
/sbin/plipconfig
%{_sbindir}/slattach
/sbin/slattach
%{_mandir}/de/man5/ethers.5%{?ext_man}
%{_mandir}/de/man8/plipconfig.8%{?ext_man}
%{_mandir}/de/man8/slattach.8%{?ext_man}
%{_mandir}/fr/man5/ethers.5%{?ext_man}
%{_mandir}/fr/man8/plipconfig.8%{?ext_man}
%{_mandir}/fr/man8/slattach.8%{?ext_man}
%{_mandir}/man5/ethers.5%{?ext_man}
%{_mandir}/man8/ether-wake.8%{?ext_man}
%{_mandir}/man8/nameif.8%{?ext_man}
%{_mandir}/man8/plipconfig.8%{?ext_man}
%{_mandir}/man8/slattach.8%{?ext_man}

%files deprecated
%license COPYING
%{_bindir}/netstat
/bin/netstat
%{_sbindir}/arp
/sbin/arp
%{_bindir}/ifconfig
/bin/ifconfig
%{_sbindir}/ipmaddr
/sbin/ipmaddr
%{_sbindir}/iptunnel
/sbin/iptunnel
%{_bindir}/route
/bin/route
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
