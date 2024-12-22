#
# spec file for package coreboot-utils
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


Name:           coreboot-utils
Version:        24.08
Release:        0
Summary:        A universal flash programming utility
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://coreboot.org/
Source0:        https://www.coreboot.org/releases/coreboot-%{version}.tar.xz
Source1:        https://www.coreboot.org/releases/coreboot-%{version}.tar.xz.sig
Source3:        %{name}.keyring
Patch1:         no-pie.patch
Patch3:         do-explicit-fallthrough.patch
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  pciutils-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
ExclusiveArch:  %ix86 x86_64

%description
coreboot is a Free Software project aimed at replacing the proprietary BIOS
(firmware) found in most computers. This package contains various utilities
used to develop and configure systems with coreboot.

%prep
%autosetup -p1 -n coreboot-%{version}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/ectool
make %{?_smp_mflags} CC="cc %{optflags}" -C util/superiotool
make %{?_smp_mflags} CFLAGS="%{optflags} -DCMOS_HAL=1 -I." -C util/nvramtool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/cbmem
make %{?_smp_mflags} CFLAGS="%{optflags} -I../../src/commonlib/include" -C util/ifdtool
%ifarch x86_64
make %{?_smp_mflags} -C util/cbfstool
%endif
%ifarch %{ix86} x86_64
CXXFLAGS="$CXXFLAGS -fPIC"
CFLAGS="$CFLAGS -fPIC"
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/inteltool
%ifarch x86_64
make %{?_smp_mflags} -C util/cbfstool
make %{?_smp_mflags} HOSTCC="cc %{optflags}"  -C util/amdfwtool
%endif
(cd util/msrtool && %configure && make %{?_smp_mflags} )
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

install util/ifdtool/ifdtool %{buildroot}%{_bindir}
install util/cbmem/cbmem %{buildroot}%{_bindir}
%ifarch %{ix86} x86_64
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/inteltool install
make -C util/msrtool DESTDIR=%{buildroot} PREFIX=%{_prefix} install
%ifarch x86_64
install util/amdfwtool/amdfwtool %{buildroot}%{_sbindir}
install util/cbfstool/cbfstool %{buildroot}%{_bindir}
%endif
%endif

install -pm644 util/superiotool/README README.superiotool
install -pm644 util/superiotool/COPYING COPYING.superiotool
install -pm644 util/nvramtool/README README.nvramtool
install -pm644 util/nvramtool/COPYING COPYING.nvramtool
install -pm644 util/nvramtool/DISCLAIMER DISCLAIMER.nvramtool
%ifarch %{ix86} x86_64
install -pm644 util/msrtool/COPYING COPYING.msrtool
%endif

%files
%defattr(-,root,root)
%license COPYING.superiotool
%doc README.superiotool
%license COPYING.nvramtool
%doc README.nvramtool DISCLAIMER.nvramtool
%ifarch x86_64
%{_bindir}/cbfstool
%{_sbindir}/amdfwtool
%endif
%{_bindir}/cbmem
%{_bindir}/ifdtool
%{_sbindir}/ectool
%{_sbindir}/inteltool
%{_sbindir}/intelmetool
%{_sbindir}/msrtool
%{_sbindir}/nvramtool
%{_sbindir}/superiotool
%{_mandir}/man8/*

%changelog
