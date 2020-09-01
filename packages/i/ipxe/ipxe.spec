#
# spec file for package ipxe
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


Name:           ipxe
Version:        1.20.1+git20200817.ef2c844d
Release:        0
Summary:        A Network Boot Firmware
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://ipxe.org/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  /usr/bin/mkisofs
BuildRequires:  binutils-devel
%ifarch aarch64
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 159999
BuildRequires:  cross-x86_64-gcc7
%else
BuildRequires:  cross-x86_64-gcc10
%endif
%endif
%ifarch x86_64
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 159999
BuildRequires:  cross-aarch64-gcc7
%else
BuildRequires:  cross-aarch64-gcc10
%endif
%endif
BuildRequires:  perl
%ifarch %{ix86} x86_64
BuildRequires:  syslinux
%endif
BuildRequires:  xz-devel
# ix86 does not have a cross-x86_64 gcc available so it can't build
# the x86_64 ipxe code. As a result of which, the support for ix86
# is more limited.
ExclusiveArch:  %{ix86} x86_64 aarch64

%description
iPXE is a network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

%package bootimgs
Summary:        Network boot loader images in bootable USB, CD, floppy and GRUB formats
Group:          Development/Tools/Other
BuildArch:      noarch

%description bootimgs
iPXE is a network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE boot images in USB, CD, floppy, and PXE
UNDI formats. EFI is supported, too.

%prep
%setup -q

%build
cd src

make_ipxe() {
    make %{?_smp_mflags} V=1 \
        VERSION=%{version} "$@"
}

%ifarch %{ix86} x86_64
make_ipxe bin-i386-efi/ipxe.efi
make_ipxe bin-i386-efi/snp.efi
%endif

%ifarch x86_64
# ix86 can't cross-compile
make_ipxe bin-x86_64-efi/ipxe.efi
make_ipxe bin-x86_64-efi/snp.efi
make_ipxe CROSS="aarch64-suse-linux-" bin-arm64-efi/snp.efi
%endif # x86_64

%ifarch aarch64
make_ipxe CROSS="x86_64-suse-linux-" bin-x86_64-efi/ipxe.efi
make_ipxe CROSS="x86_64-suse-linux-" bin-x86_64-efi/snp.efi
make_ipxe bin-arm64-efi/snp.efi
%endif

make_ipxe \
%ifnarch %{ix86} x86_64
  CROSS="x86_64-suse-linux-" \
%endif
  bin/undionly.kpxe bin/ipxe.{dsk,iso,usb,lkrn}

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
mkdir -p %{buildroot}/%{_datadir}/%{name}.efi/

#%ifarch %{ix86} x86_64
install -D -m0644 src/bin/undionly.kpxe %{buildroot}/%{_datadir}/%{name}/
install -D -m0644 src/bin/ipxe.{iso,usb,dsk,lkrn} %{buildroot}/%{_datadir}/%{name}/
#%endif
%ifarch %{ix86} x86_64
install -D -m0644 src/bin-i386-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-i386.efi
install -D -m0644 src/bin-i386-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-i386.efi
%endif
%ifnarch %{ix86}
install -D -m0644 src/bin-x86_64-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-x86_64.efi
install -D -m0644 src/bin-x86_64-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-x86_64.efi
install -D -m0644 src/bin-arm64-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-arm64.efi
%endif

%files bootimgs
%defattr(-,root,root)
%dir %{_datadir}/%{name}
#%ifarch %{ix86} x86_64
%{_datadir}/%{name}/ipxe.iso
%{_datadir}/%{name}/ipxe.usb
%{_datadir}/%{name}/ipxe.dsk
%{_datadir}/%{name}/ipxe.lkrn
#%endif
%ifarch %{ix86} x86_64
%{_datadir}/%{name}/ipxe-i386.efi
%{_datadir}/%{name}/snp-i386.efi
%endif
%ifnarch %{ix86}
%{_datadir}/%{name}/ipxe-x86_64.efi
%{_datadir}/%{name}/snp-x86_64.efi
%{_datadir}/%{name}/snp-arm64.efi
%endif
#%ifarch %{ix86} x86_64
%{_datadir}/%{name}/undionly.kpxe
#%endif
%license COPYING COPYING.GPLv2 COPYING.UBDL

%changelog
