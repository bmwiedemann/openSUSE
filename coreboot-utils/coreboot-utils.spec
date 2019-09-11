#
# spec file for package coreboot-utils
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


Name:           coreboot-utils
Version:        4.9
Release:        0
Summary:        A universal flash programming utility
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://coreboot.org/
Source0:        https://www.coreboot.org/releases/coreboot-%{version}.tar.xz
Source1:        https://www.coreboot.org/releases/coreboot-%{version}.tar.xz.sig
#http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x269C04E1#/%%{name}.keyring
Source3:        %{name}.keyring
Patch1:         no-pie.patch
Patch2:         k8resdump.diff
Patch3:         do-explicit-fallthrough.patch
BuildRequires:  gcc-c++
BuildRequires:  pciutils-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
ExclusiveArch:  %ix86 x86_64

%description
coreboot is a Free Software project aimed at replacing the proprietary BIOS
(firmware) found in most computers. This package contains various utilities
used to develop and configure systems with coreboot.

%prep
%setup -q -n coreboot-%{version}
%if 0%{?suse_version} > 1320
%patch1 -p1
%endif
%patch2 -p1
%if 0%{?suse_version} > 1320
%patch3 -p1
%endif

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/ectool
make %{?_smp_mflags} CC="cc %{optflags}" -C util/superiotool
make %{?_smp_mflags} CFLAGS="%{optflags} -DCMOS_HAL=1 -I." -C util/nvramtool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/romcc romcc
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/cbmem
make %{?_smp_mflags} CFLAGS="%{optflags} -I../../src/commonlib/include" -C util/ifdtool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/cbfstool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/k8resdump
%ifarch %{ix86} x86_64
CXXFLAGS="$CXXFLAGS -fPIC"
CFLAGS="$CFLAGS -fPIC"
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/inteltool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/intelmetool
make %{?_smp_mflags} HOSTCC="cc %{optflags}"  -C util/amdfwtool
make %{?_smp_mflags} CFLAGS="%{optflags} -I." -C util/viatool
(cd util/msrtool && %configure && make %{?_smp_mflags})
%endif

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_mandir}/man1

make %{?_smp_mflags} PREFIX=%{buildroot}/%{_prefix} -C util/ectool install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/superiotool install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/nvramtool install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/intelmetool install
# ifdtool & viatool install targets try to install a nonexistent manpage...
install util/ifdtool/ifdtool %{buildroot}%{_bindir}
install util/cbfstool/cbfstool %{buildroot}%{_bindir}
install util/cbmem/cbmem %{buildroot}%{_bindir}
install util/romcc/romcc %{buildroot}%{_bindir}
install -pm644 util/romcc/romcc.1 %{buildroot}%{_mandir}/man1/
install util/k8resdump/k8resdump %{buildroot}%{_sbindir}
install util/amdtools/*.pl %{buildroot}%{_sbindir}
install util/amdtools/k8-read-mem-settings.sh %{buildroot}%{_sbindir}
%ifarch %{ix86} x86_64
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/inteltool install
install util/viatool/viatool %{buildroot}%{_bindir}
install util/amdfwtool/amdfwtool %{buildroot}%{_sbindir}
make -C util/msrtool DESTDIR=%{buildroot} PREFIX=%{_prefix} install
%endif

install -pm644 util/superiotool/README README.superiotool
install -pm644 util/superiotool/COPYING COPYING.superiotool
install -pm644 util/nvramtool/README README.nvramtool
install -pm644 util/nvramtool/COPYING COPYING.nvramtool
install -pm644 util/nvramtool/DISCLAIMER DISCLAIMER.nvramtool
install -pm644 util/romcc/COPYING COPYING.romcc
install -pm644 util/amdtools/README README.amdtools
cp -a util/amdtools/example_input example_input.amdtools
%ifarch %{ix86} x86_64
install -pm644 util/viatool/README README.viatool
install -pm644 util/msrtool/COPYING COPYING.msrtool
%endif

%files
%defattr(-,root,root)
%license COPYING.superiotool
%doc README.superiotool
%license COPYING.nvramtool
%doc README.nvramtool DISCLAIMER.nvramtool
%doc README.amdtools example_input.amdtools
%{_bindir}/cbfstool
%{_bindir}/cbmem
%{_bindir}/ifdtool
%{_bindir}/romcc
%{_bindir}/viatool
%{_sbindir}/ectool
%{_sbindir}/inteltool
%{_sbindir}/intelmetool
%{_sbindir}/amdfwtool
%{_sbindir}/k8-compare-pci-space.pl
%{_sbindir}/k8-interpret-extended-memory-settings.pl
%{_sbindir}/k8-read-mem-settings.sh
%{_sbindir}/k8resdump
%{_sbindir}/msrtool
%{_sbindir}/nvramtool
%{_sbindir}/parse-bkdg.pl
%{_sbindir}/superiotool
%{_mandir}/man1/*
%{_mandir}/man8/*

%changelog
