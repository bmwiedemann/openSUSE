#
# spec file for package vpcs
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


Name:           vpcs
Version:        0.8
Release:        0
Summary:        Virtual PC Simulator
License:        BSD-2-Clause
Group:          System/Emulators/Other
Url:            http://sourceforge.net/projects/vpcs/
Source0:        %{name}-%{version}-src.tbz
Patch0:         %{name}-0.8-no-static.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
cd src
rm getopt.*
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fno-strict-aliasing"
make -f Makefile.linux CPUTYPE=%_target_cpu

%install
%__mkdir -p %buildroot/%_bindir
%__mkdir -p %buildroot/%_mandir/man1
%__cp src/vpcs %buildroot/%_bindir/
%__cp man/vpcs.1 %buildroot/%_mandir/man1/

%files
%defattr(-,root,root)
%doc readme.txt COPYING
%_bindir/vpcs
%_mandir/man1/*

%changelog
