#
# spec file for package pciutils
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover   3
%define lname   libpci%{sover}
Name:           pciutils
Version:        3.13.0
Release:        0
Summary:        PCI utilities for the Linux Kernel
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://mj.ucw.cz/sw/pciutils/
Source:         https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.sign
Source2:        baselibs.conf
# https://mj.ucw.cz/pgp.html
Source3:        https://mj.ucw.cz/pgpkey.txt#/%{name}.keyring
Patch0:         pciutils-3.1.9_pkgconfig.patch
Patch1:         pciutils-endianh.patch
Patch2:         pciutils-ocloexec.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(zlib)
Requires:       hwdata

%description
lspci: This program displays detailed information about all PCI busses
and devices in the system, replacing the original /proc/pci interface.

setpci: This program allows reading from and writing to PCI device
configuration registers. For example, you can adjust the latency timers
with it.

update-pciids: This program downloads the current version of the
pci.ids file.

%package -n %{lname}
Summary:        PCI utility library
Group:          System/Libraries

%description -n %{lname}
libpci offers access to the PCI configuration space.

%package devel
Summary:        Library and Include Files of the PCI utilities
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package contains the files that are necessary for software
development using the PCI utilities.

%prep
%autosetup -p1

%build
%make_build OPT="%{optflags}" PREFIX=%{_prefix} LIBDIR=%{_libdir} SBINDIR=%{_bindir} STRIP="" SHARED="yes"

%install
make install PREFIX=%{buildroot}%{_prefix} SBINDIR=%{buildroot}%{_bindir} \
             ROOT=%{buildroot} MANDIR=%{buildroot}%{_mandir} STRIP="" \
	     SHARED="yes" LIBDIR=%{buildroot}%{_libdir}
chmod 0755 %{buildroot}%{_libdir}/libpci.so.%{sover}
mkdir -p %{buildroot}%{_includedir}/pci
cp -p lib/{pci,header,config,types}.h %{buildroot}%{_includedir}/pci
rm -rf %{buildroot}%{_datadir}/pci.ids*
install -D -m 0644 lib/libpci.pc %{buildroot}%{_libdir}/pkgconfig/libpci.pc
ln -sf %{_libdir}/libpci.so.3 %{buildroot}%{_libdir}/libpci.so

%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
ln -s %{_bindir}/{lspci,setpci,pcilmr} %{buildroot}/sbin
%endif

mkdir %{buildroot}%{_sbindir}
ln -s %{_bindir}/{lspci,setpci,pcilmr} %{buildroot}%{_sbindir}

rm %{buildroot}%{_bindir}/update-pciids
rm %{buildroot}%{_mandir}/man8/update-pciids.8

%check
%make_build tests

%ldconfig_scriptlets -n %{lname}

%files
%license COPYING
%doc README
%if 0%{?suse_version} < 1550
/sbin/lspci
/sbin/pcilmr
/sbin/setpci
%endif
%{_bindir}/lspci
%{_bindir}/pcilmr
%{_bindir}/setpci
%{_sbindir}/lspci
%{_sbindir}/pcilmr
%{_sbindir}/setpci
%{_mandir}/man7/pcilib.7%{?ext_man}
%{_mandir}/man8/lspci.8%{?ext_man}
%{_mandir}/man8/pcilmr.8%{?ext_man}
%{_mandir}/man8/setpci.8%{?ext_man}
%{_mandir}/man5/pci.ids.5%{?ext_man}

%files -n %{lname}
%license COPYING
%{_libdir}/libpci.so.%{sover}
%{_libdir}/libpci.so.%{sover}.*

%files devel
%license COPYING
%{_includedir}/pci
%{_libdir}/libpci.so
%{_libdir}/pkgconfig/libpci.pc

%changelog
