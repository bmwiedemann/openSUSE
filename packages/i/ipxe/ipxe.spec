#
# spec file for package ipxe
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


%ifnarch %{ix86} x86_64
%define buildtargets dsk,usb,lkrn
%else
%define buildtargets sdsk,dsk,iso,usb,lkrn
%define do_floppy 1
%endif

Name:           ipxe
Version:        1.21.1+git20250827.61b4585e2
Release:        0
Summary:        A Network Boot Firmware
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://ipxe.org/
Source:         %{name}-%{version}.tar.xz
Patch0:         syslinux-mtools.patch
Patch9:         fix-i586.patch
BuildRequires:  binutils-devel
# Do not build i586 for Leap/SLE: no such port available
%ifarch i586
%if 0%{?sle_version}
%define no_aarch64_cc 1
%endif
%endif
%ifnarch %{ix86} x86_64
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 159999
BuildRequires:  cross-x86_64-gcc7
%else
BuildRequires:  cross-x86_64-gcc%{gcc_version}
%endif
%endif
%if !0%{?no_aarch64_cc}
%ifnarch aarch64
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 159999
BuildRequires:  cross-aarch64-gcc7
%else
BuildRequires:  cross-aarch64-gcc%{gcc_version}
%endif
%endif
%endif
BuildRequires:  perl
%ifarch %{ix86} x86_64
BuildRequires:  mtools
BuildRequires:  syslinux
BuildRequires:  xorriso
%endif
BuildRequires:  xz-devel
# For QEMU ROMs
BuildRequires:  ovmf-tools

# iPXE provide ROMs only for x86 (Legacy BIOS/UEFI) and ARM (UEFI) targets.
# However, it depends on ovmf-tools (for building) and:
# - ovmf-tools is only available on x86_64, aarch64 and riscv64.
# Furthermore, it does not build on bigendian arch-es (s390, s390x, ppc,
# ppc64) while, for ppc64le:
# - on Baremetal: ppc64le uses Petitboot/OPAL;
# - for KVM/QEMU: pseries machines use SLOF (Open Firmware).
# We can, therefore, restrict the to only x86_64 and ARM64, which is also
# where the binaries are necessary and are actually executable.
ExclusiveArch:  x86_64 aarch64

%description
iPXE is a network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

%package bootimgs
Summary:        Network boot loader images in bootable USB, CD, floppy and GRUB formats
Group:          Development/Tools/Other

%description bootimgs
iPXE is a network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE boot images in USB, CD, floppy, and PXE
UNDI formats. EFI is supported, too.

%package qemu
Summary:        PXE and EFI ROMs for QEMU network devices
Group:          System/Emulators/PC
Provides:       qemu-ipxe
Obsoletes:      qemu-ipxe
Provides:       ipxe-qemu-roms = %{version}

%description qemu
This package contains the iPXE ROMs (legacy PXE and EFI) compiled specifically
for QEMU emulated network devices.

%prep
%autosetup -N
%autopatch -p1 -M 8
%ifarch %{ix86}
%autopatch -p1 -m 9
%endif
cd src

# enable compressed images
sed -i.bak \
    -e 's,//\(#define.*IMAGE_ZLIB.*\),\1,' \
    -e 's,//\(#define.*IMAGE_GZIP.*\),\1,' \
    config/general.h

# enable HTTPS downloads
sed -i.bak \
    -e 's,#undef\(.*DOWNLOAD_PROTO_HTTPS.*\),#define\1,' \
    config/general.h

%build
cd src

make_ipxe() {
    # https://github.com/ipxe/ipxe/issues/620 ; and gcc-7 now also fails from -Werror
    TAG="NO_WERROR=1"
    make -O %{?_smp_mflags} V=1 \
        VERSION=%{version} $TAG "$@"
}

# Building QEMU ROMs

# QEMU's legacy virtio ROM must fit in 64KB. For that to happen, let's get
# rid of HTTPS, ZLIB, GZIP and all the SAN features (just for the QEMU ROMs
# of course, using iPXE's local config mechanism).
cat <<EOF > config/local/general.h
#undef DOWNLOAD_PROTO_HTTPS
#undef IMAGE_ZLIB
#undef IMAGE_GZIP
#undef SANBOOT_PROTO_ISCSI
#undef SANBOOT_PROTO_AOE
#undef SANBOOT_PROTO_IB_SRP
#undef SANBOOT_PROTO_FCP
EOF

# Enable serial output (so, e.g., -nographic, works).
cat <<EOF > config/local/console.h
#define CONSOLE_SERIAL
EOF

QEMU_NICS="e1000:8086:100e eepro100:8086:1209 ne2k_pci:10ec:8029 pcnet:1022:2000 rtl8139:10ec:8139 virtio:1af4:1000 e1000e:8086:10d3 vmxnet3:15ad:07b0"

CROSS_PREFIX=""
%ifnarch %{ix86} x86_64
CROSS_PREFIX="CROSS=x86_64-suse-linux-"
%endif

for nic in $QEMU_NICS; do
    name=$(echo "$nic" | cut -d: -f1)
    vid=$(echo "$nic" | cut -d: -f2)
    did=$(echo "$nic" | cut -d: -f3)
    # for EfiRom: -f Vendor ID, -i Device ID, -l 0x02 (Network Controller PCI Class)
    EFI_ARGS="-f 0x${vid} -i 0x${did} -l 0x02"

    # Build legacy ROMs
    if [ "$name" != "e1000e" ] && [ "$name" != "vmxnet3" ]; then
        make_ipxe $CROSS_PREFIX bin/${vid}${did}.rom
        cp bin/${vid}${did}.rom pxe-${name}.rom
        EFI_ARGS="$EFI_ARGS -b bin/${vid}${did}.rom"
    fi

    # Build EFI drivers
    %ifnarch %{ix86}
    make_ipxe $CROSS_PREFIX bin-x86_64-efi/${vid}${did}.efidrv
    EFI_ARGS="$EFI_ARGS -ec bin-x86_64-efi/${vid}${did}.efidrv"
    %endif

    # Combine them into FAT EFI ROMs using EfiRom
    EfiRom $EFI_ARGS -o efi-${name}.rom
done

# QEMU's padding logic (for legacy and EFI ROMs)
for name in e1000 eepro100 ne2k_pci pcnet rtl8139 virtio; do
    size=$(stat -c '%s' pxe-${name}.rom)
    if [ "$name" = "virtio" ]; then
        if [ $size -gt 65536 ]; then echo "virtio rom too large"; exit 1; fi
    else
        if [ $size -gt 131072 ]; then echo "pxe rom $name too large"; exit 1; fi
        if [ $size -le 65536 ]; then
            perl util/padimg.pl pxe-${name}.rom -s 65536 -b 255
            echo -ne "SEGMENT OVERAGE\0" >> pxe-${name}.rom
        fi
    fi
done
for name in e1000 eepro100 ne2k_pci pcnet rtl8139 virtio e1000e vmxnet3; do
    size=$(stat -c '%s' efi-${name}.rom)
    # This is the size of the ROMs provided by the old qemu-ipxe package.
    # If this one is larger, we'll have live migration issues (bsc#1269260).
    if [ $size -gt 262144 ]; then echo "EFI rom $name too large"; exit 1; fi
    truncate -s 262144 efi-${name}.rom
done

rm config/local/general.h
rm config/local/console.h
rm -rf bin bin-i386-efi bin-x86_64-efi bin-arm64-efi
# End of building QEMU ROMs

%ifarch %{ix86} x86_64
make_ipxe bin-i386-efi/ipxe.efi
make_ipxe bin-i386-efi/snp.efi
%else
make_ipxe CROSS="x86_64-suse-linux-" bin-i386-efi/ipxe.efi
make_ipxe CROSS="x86_64-suse-linux-" bin-i386-efi/snp.efi
%endif

%ifarch x86_64
make_ipxe bin-x86_64-efi/ipxe.efi
make_ipxe bin-x86_64-efi/snp.efi
%else
# ix86 can't cross-compile
%ifnarch %{ix86}
make_ipxe CROSS="x86_64-suse-linux-" bin-x86_64-efi/ipxe.efi
make_ipxe CROSS="x86_64-suse-linux-" bin-x86_64-efi/snp.efi
%endif
%endif # x86_64

%ifarch aarch64
make_ipxe bin-arm64-efi/snp.efi
%else
%{!?no_aarch64_cc:make_ipxe CROSS="aarch64-suse-linux-" bin-arm64-efi/snp.efi}
%endif

make_ipxe \
%ifnarch %{ix86} x86_64
  CROSS="x86_64-suse-linux-" \
%endif
  bin/undionly.kpxe bin/ipxe.{%{buildtargets}}

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
mkdir -p %{buildroot}/%{_datadir}/%{name}.efi/

install -D -m0644 src/bin/undionly.kpxe %{buildroot}/%{_datadir}/%{name}/
install -D -m0644 src/bin/ipxe.{%{buildtargets}} %{buildroot}/%{_datadir}/%{name}/
install -D -m0644 src/bin-i386-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-i386.efi
install -D -m0644 src/bin-i386-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-i386.efi
%ifnarch %{ix86}
install -D -m0644 src/bin-x86_64-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-x86_64.efi
install -D -m0644 src/bin-x86_64-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-x86_64.efi
%endif
%{!?no_aarch64_cc:install -D -m0644 src/bin-arm64-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-arm64.efi}
%if 0%{?do_floppy}
ln -s ipxe.sdsk %{buildroot}/%{_datadir}/%{name}/floppy.img
%endif

mkdir -p %{buildroot}/%{_datadir}/qemu/
install -m0644 src/pxe-*.rom %{buildroot}/%{_datadir}/qemu/
install -m0644 src/efi-*.rom %{buildroot}/%{_datadir}/qemu/

%files bootimgs
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ipxe.{%{buildtargets}}
%if 0%{?do_floppy}
%{_datadir}/%{name}/floppy.img
%endif
%{_datadir}/%{name}/ipxe-i386.efi
%{_datadir}/%{name}/snp-i386.efi
%ifnarch %{ix86}
%{_datadir}/%{name}/ipxe-x86_64.efi
%{_datadir}/%{name}/snp-x86_64.efi
%endif
%{!?no_aarch64_cc:%{_datadir}/%{name}/snp-arm64.efi}
%{_datadir}/%{name}/undionly.kpxe
%license COPYING COPYING.GPLv2 COPYING.UBDL

%files qemu
%defattr(-,root,root)
%dir %{_datadir}/qemu
%{_datadir}/qemu/pxe-*.rom
%{_datadir}/qemu/efi-*.rom

%changelog
