#
# spec file for package u-boot-orangepipc2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Texas Instruments Inc by Nishanth Menon
# Copyright (c) 2007-2010 by Silvan Calarco <silvan.calarco@mambasoft.it>
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


%bcond_with uboot_atf
%bcond_with uboot_atf_pine64

%define mvebu_spl 0
%define x_loader 0
%define rockchip_spl 0
%define sunxi_spl 1
%define arndale_spl 0
%define origen_spl 0
%define imx6_spl 0
%define socfpga_spl 0

%if "orangepipc2" == "rpi" || "orangepipc2" == "rpi2" || "orangepipc2" == "rpi3"
%define is_rpi 1
%endif
%if "orangepipc2" == "evb-rk3399" || "orangepipc2" == "firefly-rk3399" || "orangepipc2" == "puma-rk3399" || "orangepipc2" == "rock960-rk3399"
%define is_rk3399 1
%endif
%if "orangepipc2" == "bananapim64" || "orangepipc2" == "nanopia64" || "orangepipc2" == "pine64plus" || "orangepipc2" == "pinebook"
%define is_a64 1
%endif
%if "orangepipc2" == "orangepipc2"
%define is_h5 1
%endif
%if "orangepipc2" == "pineh64"
%define is_h6 1
%endif

# archive_version differs from version for RC version only
%define archive_version 2019.04

Name:           u-boot-orangepipc2
Version:        2019.04
Release:        0
Summary:        The U-Boot firmware for the orangepipc2 platform
License:        GPL-2.0-only
Group:          System/Boot
Url:            http://www.denx.de/wiki/U-Boot
Source:         ftp://ftp.denx.de/pub/u-boot/u-boot-%{archive_version}.tar.bz2
Source1:        ftp://ftp.denx.de/pub/u-boot/u-boot-%{archive_version}.tar.bz2.sig
Source2:        arndale-bl1.img
Source3:        update_git.sh
Source300:      u-boot-rpmlintrc
Patch0001:      0001-XXX-openSUSE-XXX-Prepend-partition-.patch
Patch0002:      0002-Revert-Revert-omap3-Use-raw-SPL-by-.patch
Patch0003:      0003-rpi-Use-firmware-provided-device-tr.patch
Patch0004:      0004-Temp-workaround-for-Chromebook-snow.patch
Patch0005:      0005-zynqmp-Add-generic-target.patch
Patch0006:      0006-tools-zynqmpbif-Add-support-for-loa.patch
Patch0007:      0007-boo-1123170-Remove-ubifs-support-fr.patch
Patch0008:      0008-zynqmp-generic-fix-compilation.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?is_rk3399} && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-rk3399
%endif
%if (0%{?is_a64} || 0%{?is_h5}) && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-sun50ia64
%endif
%if 0%{?is_h6} && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-sun50ih6
%endif
BuildRequires:  bc
BuildRequires:  bison
# Arndale board needs DTC >= 1.4
BuildRequires:  dtc >= 1.4.0
BuildRequires:  flex
# u-boot-clearfog (tools/kwbimage.c) needs openssl to build
BuildRequires:  libopenssl-devel
BuildRequires:  python-devel
%if %{with uboot_atf}
%if "%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399"
# make_fit_atf.py
BuildRequires:  python-pyelftools
%endif
%endif
BuildRequires:  swig
%if "%{name}" == "u-boot-qemu-ppce500"
# Owns /usr/share/qemu directory
BuildRequires:  qemu
Provides:       qemu-ppc:%{_datadir}/qemu/u-boot.e500
%endif
%if 0%{?is_rpi}
# Owns /boot/vc directory
BuildRequires:  raspberrypi-firmware
%endif
%if "%{name}" == "u-boot-zynqmp"
BuildRequires:  zynqmp-dts
%endif
%if 0%{?is_rpi}
# For mountpoint
Requires(post): util-linux
%endif
Provides:       u-boot-loader
Conflicts:      otherproviders(u-boot-loader)
%if %x_loader == 1
Obsoletes:      x-loader-orangepipc2
Provides:       x-loader-orangepipc2
%endif
%if "%{name}" == "u-boot-am335xevm"
# http://git.denx.de/?p=u-boot.git;a=commit;h=8fa7f65dd02c176ee6021eaf40114560b8954ba2
Obsoletes:      am335x_boneblack
Provides:       am335x_boneblack
%endif
%if "%{name}" == "bananapi_m2_plus_h3"
# http://git.denx.de/?p=u-boot.git;a=commit;h=268ae6548779ccd8ba38ce39d43f41be7e0bc133
Obsoletes:      Sinovoip_BPI_M2_Plus
Provides:       Sinovoip_BPI_M2_Plus
%endif
ExclusiveArch:  aarch64

%description
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains the firmware for the orangepipc2 platform.

%package doc
Summary:        Documentation for the U-Boot Firmware
Group:          Documentation/Other

%description doc
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains documentation for U-Boot firmware.

%prep
%setup -q -n u-boot-%{archive_version}
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1

%build
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/%{name}.changes | tail -n 1 | cut -d- -f1 )" +%s)
%if 0%{?is_a64} || 0%{?is_h5}
export BL31=/usr/share/arm-trusted-firmware-sun50ia64/bl31.bin
%endif
%if 0%{?is_h6}
export BL31=/usr/share/arm-trusted-firmware-sun50ih6/bl31.bin
%endif

%if %{with uboot_atf}
%if "%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399"
cp /usr/share/arm-trusted-firmware-rk3399/bl31.elf .
%endif
%endif

make %{?_smp_mflags} CROSS_COMPILE= HOSTCFLAGS="$RPM_OPT_FLAGS" orangepi_pc2_defconfig
echo "Attempting to enable fdt apply command (.dtbo) support."
echo "CONFIG_OF_LIBFDT_OVERLAY=y" >> .config
make %{?_smp_mflags} CROSS_COMPILE= HOSTCFLAGS="$RPM_OPT_FLAGS" \
%if ("%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399") && %{with uboot_atf}
     all u-boot.itb
%else
     all
%endif

%ifarch aarch64
%if %sunxi_spl == 1
cat spl/sunxi-spl.bin u-boot.itb > u-boot-sunxi-with-spl.bin
%endif
%endif

%if "%{name}" == "u-boot-snow" || "%{name}" == "u-boot-spring"
# Chromebook ARM (snow) and HP Chromebook 11 (spring) need a uImage format
export TEXT_START=$(awk '$NF == "_start" { printf "0x"$1 }' System.map)
./tools/mkimage -A arm -O linux -T kernel -C none -a $TEXT_START -e $TEXT_START -n uboot -d u-boot-dtb.bin u-boot.img
%endif

%if %rockchip_spl == 1
for t in ; do
    ./tools/mkimage -n  -d spl/u-boot-spl.bin -T $t u-boot-spl.$t
done
%endif

%install
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/%{name}.changes | tail -n 1 | cut -d- -f1 )" +%s)
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define uboot_dir /boot
%if 0%{?is_rpi}
%define uboot_dir /boot/vc
%endif
%if "%{name}" == "u-boot-qemu-ppce500"
%define uboot_dir %{_datadir}/qemu
%endif
%if "%{name}" == "u-boot-jetson-tk1"
# tegra-uboot-flasher needs several intermediate files, under their original name.
for f in u-boot u-boot.dtb u-boot-dtb-tegra.bin u-boot-nodtb-tegra.bin spl/u-boot-spl; do
    install -D -m 0644 $f %{buildroot}%{uboot_dir}/$f
done
%else
%if "%{name}" == "u-boot-p2371-2180"
# Jetson TX1 Driver Pack flash.sh needs several intermediate files, under their original name.
for f in u-boot u-boot.bin u-boot.dtb u-boot-dtb.bin; do
    install -D -m 0644 $f %{buildroot}%{uboot_dir}/$f
done
%else
install -D -m 0644 u-boot.itb %{buildroot}%{uboot_dir}/u-boot.itb
%if ("%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399") && %{with uboot_atf}
install -D -m 0644 u-boot.itb %{buildroot}%{uboot_dir}/u-boot.itb
%endif
%if "%{name}" == "u-boot-qemu-ppce500"
mv %{buildroot}%{uboot_dir}/u-boot.itb %{buildroot}%{uboot_dir}/u-boot.e500
%endif
%endif
%endif
%if %x_loader == 1
install -D -m 0644 MLO %{buildroot}%{uboot_dir}/MLO
%endif
%if %origen_spl == 1
install -D -m 0644 spl/origen-spl.bin %{buildroot}%{uboot_dir}/origen-spl.bin
%endif
%if %arndale_spl == 1
install -D -m 0644 spl/arndale-spl.bin %{buildroot}%{uboot_dir}/arndale-spl.bin
install -D -m 0644 %{SOURCE2} %{buildroot}%{uboot_dir}/arndale-bl1.img
%endif
%if %mvebu_spl == 1
install -D -m 0644 u-boot-spl.kwb %{buildroot}%{uboot_dir}/u-boot-spl.kwb
%endif
%if %rockchip_spl == 1
install -D -m 0644 spl/u-boot-spl.bin %{buildroot}%{uboot_dir}/u-boot-spl.bin
for t in ; do
    install -D -m 0644 u-boot-spl.$t %{buildroot}%{uboot_dir}/u-boot-spl.$t
done
%endif
%if %sunxi_spl == 1
install -D -m 0644 spl/sunxi-spl.bin %{buildroot}%{uboot_dir}/sunxi-spl.bin
install -D -m 0644 u-boot-sunxi-with-spl.bin %{buildroot}%{uboot_dir}/u-boot-sunxi-with-spl.bin
%endif
%if %imx6_spl == 1
install -D -m 0644 SPL %{buildroot}%{uboot_dir}/imx6-spl.bin
%endif
%if %socfpga_spl == 1
install -D -m 0644 u-boot-with-spl.sfp %{buildroot}%{uboot_dir}/u-boot-with-spl.sfp
%endif
%if "%{name}" == "u-boot-rpi3"
echo -e "# Boot in AArch64 mode\narm_control=0x200" > %{buildroot}%{uboot_dir}/ubootconfig.txt
%endif

%if 0%{?is_rpi}
%post
# On the Raspberry Pi we chain-load u-boot.bin from bootcode.bin via config.txt.
# It needs to be on the first FAT partition, wherever we mounted it.
# a) Unmounted, then do nothing.
# b) Mounted as /boot/vc, then they're in the right place already.
# c) Mounted as /boot/efi, with /boot/vc as symlink, then nothing to be done.
# d) Mounted as /boot/efi, with /boot/vc a directory, then copy files over.
if mountpoint -q /boot/efi; then
  if ! [[ "$(readlink -f /boot/efi)" -ef "$(readlink -f %{uboot_dir})" ]]; then
    [ -f %{uboot_dir}/ubootconfig.txt ] && cp %{uboot_dir}/ubootconfig.txt /boot/efi
    cp %{uboot_dir}/u-boot.itb /boot/efi/
  fi
fi
%endif

%files
%defattr(-,root,root)
%license Licenses/gpl-2.0.txt
%doc README
%{uboot_dir}/*

%files doc
%defattr(-,root,root)
# Generic documents
%doc doc/README.JFFS2 doc/README.JFFS2_NAND doc/README.commands
%doc doc/README.autoboot doc/README.commands doc/README.console doc/README.dns
%doc doc/README.hwconfig doc/README.nand doc/README.NetConsole doc/README.serial_multi
%doc doc/README.SNTP doc/README.standalone doc/README.update doc/README.usb
%doc doc/README.video doc/README.VLAN doc/README.silent doc/README.POST
# Copy some useful kermit scripts as well
%doc tools/kermit/dot.kermrc tools/kermit/flash_param tools/kermit/send_cmd tools/kermit/send_image
# Now any h/w dependent Documentation
%doc doc/README.ARM-memory-map

%changelog
