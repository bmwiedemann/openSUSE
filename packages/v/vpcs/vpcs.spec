#
# spec file for package vpcs
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


Name:           vpcs
Version:        0.8
Release:        0
Summary:        Virtual PC Simulator
License:        BSD-2-Clause
Group:          System/Emulators/Other
URL:            https://sourceforge.net/projects/vpcs/
Source0:        %{name}-%{version}-src.tbz
Patch0:         %{name}-0.8-no-static.patch
Patch1:         0001-revert-from-r124.patch

%description
The VPCS can simulate up to 9 PCs. You can ping/traceroute them, or ping/traceroute
the other hosts/routers from the virtual PCs when you study the Cisco routers in
the Dynamips. VPCS is not the traditional PC, it is just a program running on the
Linux or Windows, and only few network commands can be used in it. But VPCS can
give you a big hand when you study the Cisco devices in the Dynamips. VPCS can
replace the routers or VMware boxes which are used as PCs in the Dynamips network.

Try VPCS, it can save your CPU/Memory. It is very small.

Now, VPCS can be run in udp or ether mode. In the udp mode, VPCS sends or receives
the packets via udp. In the ether mode, via /dev/tap, not support on the Windows.

%prep
%autosetup -p1

%build
cd src
rm getopt.*
export CFLAGS="%{optflags} -D_GNU_SOURCE -fno-strict-aliasing -fcommon"
%make_build -f Makefile.linux CPUTYPE=%_target_cpu

%install
install -D -m0755 src/vpcs %{buildroot}%{_bindir}/vpcs
install -D -m0644 man/vpcs.1 %{buildroot}%{_mandir}/man1/vpcs.1

%files
%license COPYING
%doc readme.txt
%{_bindir}/vpcs
%{_mandir}/man1/vpcs.1%{ext_man}

%changelog
