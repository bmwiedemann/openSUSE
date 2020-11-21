#
# spec file for package u-boot
#
# Copyright (c) 2020 SUSE LLC
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


%define target @BUILD_FLAVOR@
%define mvebu_spl 0
%define x_loader 0
%define rockchip_spl 0
%define rockchip_tpl 0
%define rockchip_idb 0
%define sunxi_spl 0
%define arndale_spl 0
%define origen_spl 0
%define imx6_spl 0
%define socfpga_spl 0
%define binext .bin
%define is_armv6 0
%define is_armv7 0
%define is_armv8 0
%define is_ppc 0
%define is_riscv64 0
%define is_zynq 0
%define is_zynqmp 0
%define tools_only 0
%if "%target" == "rpi" || "%target" == "rpi2" || "%target" == "rpi3" || "%target" == "rpi4" || "%target" == "rpiarm64"
%define is_rpi 1
%if "%target" == "rpi"
%define is_armv6 1
%endif
%if "%target" == "rpi2"
%define is_armv7 1
%endif
%if "%target" == "rpi3" || "%target" == "rpi4" || "%target" == "rpiarm64"
%define is_armv8 1
%endif
%endif
%if "%target" == "firefly-rk3288" || "%target" == "tinker-rk3288"
%define is_armv7 1
%define rockchip_tpl 1
%define soc_name "rk3288"
%if "%target" == "firefly-rk3288"
%define rkimages rksd rkimage
%else
%define rkimages rksd
%endif
%endif
%if "%target" == "rock64-rk3328"
%define is_rk3328 1
%define is_armv8 1
%define rockchip_idb 1
%define rockchip_spl 1
%define rkimages $()
%endif
%if "%target" == "evb-rk3399" || "%target" == "firefly-rk3399" || "%target" == "rock-pi-4-rk3399"
%define is_rk3399 1
%define is_armv8 1
%define rockchip_idb 1
%define rockchip_spl 1
%define rkimages $()
%endif
%if "%target" == "puma-rk3399" || "%target" == "rock960-rk3399"
%define is_rk3399 1
%define is_armv8 1
%endif
%if "%target" == "bananapim64" || "%target" == "nanopia64" || "%target" == "pine64plus" || "%target" == "pinebook"
%define is_a64 1
%define is_armv8 1
%define sunxi_spl 1
%define binext .itb
%endif

%if "%target" == "mt7623nbpir2"
%define is_armv7 1
%endif

%if "%target" == "orangepipc2"
%define is_h5 1
%define is_armv8 1
%define sunxi_spl 1
%define binext .itb
%endif
%if "%target" == "pineh64"
%define is_h6 1
%define is_armv8 1
%define sunxi_spl 1
%define binext .itb
%endif
%if "%target" == "bananapi" || "%target" == "cubieboard" || "%target" == "cubieboard2" || "%target" == "cubietruck" || "%target" == "melea1000" || "%target" == "a10-olinuxino-lime" || "%target" == "a13-olinuxino" || "%target" == "a13-olinuxinom" || "%target" == "a20-olinuxino-lime" || "%target" == "a20-olinuxino-lime2" || "%target" == "a20-olinuxinomicro" || "%target" == "nanopineo" || "%target" == "orangepipc" || "%target" == "hyundaia7hd" || "%target" == "lamobor1" || "%target" == "bananapim2plush3" || "%target" == "orangepizero"
%define is_armv7 1
%define binext .img
%define sunxi_spl 1
%endif
%if "%target" == "clearfog" || "%target" == "turrisomnia"
%define mvebu_spl 1
%define is_armv7 1
%define binext .img
%endif
%if "%target" == "mx53loco"
%define is_armv7 1
%define binext .imx
%endif
%if "%target" == "mx6qsabrelite"
%define is_armv7 1
%define binext -dtb.imx
%endif
%if "%target" == "mx6cuboxi" || "%target" == "udoo" || "%target" == "udooneo"
%define imx6_spl 1
%define is_armv7 1
%define binext .img
%endif
%if "%target" == "omap3beagle" || "%target" == "omap4panda" || "%target" == "am335xevm" || "%target" == "pcm051rev3"
%define x_loader 1
%define is_armv7 1
%define binext .img
%endif
%if "%target" == "colibrit20" || "%target" == "am57xxevm"
%define is_armv7 1
%endif
%if "%target" == "arndale"
%define is_armv7 1
%define arndale_spl 1
%endif
%if  "%target" == "dragonboard410c" || "%target" == "dragonboard820c"
%define is_armv8 1
%endif
%if  "%target" == "geekbox" || "%target" == "hikey" || "%target" == "khadas-vim" || "%target" == "khadas-vim2" || "%target" == "libretech-ac" || "%target" == "libretech-cc" || "%target" == "ls1012afrdmqspi" || "%target" == "mvebudb-88f3720" || "%target" == "mvebudbarmada8k" || "%target" == "mvebuespressobin-88f3720" || "%target" == "mvebumcbin-88f8040" || "%target" == "odroid-c2" || "%target" == "odroid-n2" || "%target" == "p2371-2180" || "%target" == "p2771-0000-500" || "%target" == "p3450-0000" || "%target" == "poplar"
%define is_armv8 1
%endif
%if "%target" == "avnetultra96rev1" || "%target" == "xilinxzynqmpvirt" || "%target" == "xilinxzynqmpzcu102rev10"
%define is_zynqmp 1
%define is_armv8 1
%define binext .elf
%endif
%if "%target" == "highbank" || "%target" == "jetson-tk1" || "%target" == "merriia80optimus" || "%target" == "nanopineoair" || "%target" == "odroid" || "%target" == "odroid-xu3" || "%target" == "paz00" || "%target" == "socfpgade0nanosoc"
%define is_armv7 1
%endif
%if "%target" == "snow" || "%target" == "spring"
%define is_armv7 1
%define binext .img
%endif
%if "%target" == "zynqzturn" || "%target" == "xilinxzynqvirt"
%define is_zynq 1
%define is_armv7 1
%define binext .img
%endif
%if "%target" == "qemu-riscv64" || "%target" == "qemu-riscv64smode" || "%target" == "sifivefu540"
%define is_riscv64 1
%if "%target" == "sifivefu540"
%define binext .itb
%endif
%endif
%if "%target" == "qemu-ppce500"
%define is_ppc 1
%endif
# archive_version differs from version for RC version only
%define archive_version 2020.10
%if "%{target}" == ""
ExclusiveArch:  do_not_build
%else
%if "%{target}" == "tools"
%define tools_only 1
%else
%if %is_armv8
ExclusiveArch:  aarch64
%else
%if %is_armv7
ExclusiveArch:  armv7l armv7hl
%else
%if %is_armv6
ExclusiveArch:  armv6l armv6hl
%else
%if %is_ppc
ExclusiveArch:  ppc
%else
%if %is_riscv64
ExclusiveArch:  riscv64
%else
ExclusiveArch:  do_not_build
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%bcond_with uboot_atf
%bcond_with uboot_atf_pine64
Version:        2020.10
Release:        0
Summary:        The U-Boot firmware for the %target platform
License:        GPL-2.0-only
Group:          System/Boot
URL:            http://www.denx.de/wiki/U-Boot
Source:         http://ftp.denx.de/pub/u-boot/u-boot-%{archive_version}.tar.bz2
Source1:        http://ftp.denx.de/pub/u-boot/u-boot-%{archive_version}.tar.bz2.sig
Source2:        arndale-bl1.img
Source300:      u-boot-rpmlintrc
Source900:      update_git.sh
# Patches: start
Patch0001:      0001-XXX-openSUSE-XXX-Prepend-partition-.patch
Patch0002:      0002-Revert-Revert-omap3-Use-raw-SPL-by-.patch
Patch0003:      0003-rpi-Use-firmware-provided-device-tr.patch
Patch0004:      0004-Temp-workaround-for-Chromebook-snow.patch
Patch0005:      0005-tools-zynqmpbif-Add-support-for-loa.patch
Patch0006:      0006-boo-1123170-Remove-ubifs-support-fr.patch
Patch0007:      0007-boo-1144161-Remove-nand-mtd-spi-dfu.patch
Patch0008:      0008-Kconfig-add-btrfs-to-distro-boot.patch
Patch0009:      0009-configs-Re-sync-with-CONFIG_DISTRO_.patch
Patch0010:      0010-configs-am335x_evm-disable-BTRFS.patch
Patch0011:      0011-sunxi-dts-OrangePi-Zero-Add-SPI-ali.patch
Patch0012:      0012-sunxi-dts-OrangePi-Zero-Enable-SPI-.patch
Patch0013:      0013-sunxi-Enable-SPI-support-on-Orange-.patch
# Patches: end
BuildRequires:  bc
BuildRequires:  bison
# Arndale board needs DTC >= 1.4
BuildRequires:  dtc >= 1.4.0
BuildRequires:  flex
# u-boot-clearfog (tools/kwbimage.c) needs openssl to build
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(sdl)
Conflicts:      u-boot-loader
Provides:       u-boot-loader
%if "%_project" == "hardware:boot" || "%_project" == "hardware:boot:staging" || "%_project" == "openSUSE:Factory" || "%_project" == "openSUSE:Factory:ARM" || "%_project" == "openSUSE:Factory:PowerPC" || "%_project" == "openSUSE:Factory:RISCV" || "%_project" == "openSUSE:Leap:15.2" || "%_project" == "openSUSE:Leap:15.2:ARM" || "%_project" == "openSUSE:Leap:15.2:PowerPC"
# A complete multibuild-flavoured package is only built in above projects.
# In order to build a defined subset in forked projects, add the
# following to the respective project config (without the "#|"):
#|Macros:
#|%prjconf_multibuild_selection patch
#|:Macros
#|BuildFlags: onlybuild:u-boot:my-flavor1 onlybuild:u-boot:my-flavor2
#|BuildFlags: onlybuild:u-boot:my-flavor3 onlybuild:u-boot:my-flavor4
# If you opt to use onlybuild: to select U-Boot flavours and also
# have additional packages in that project, these need to be listed, too:
#|BuildFlags: onlybuild:package onlybuild:otherpackage onlybuild:thirdpackage
# Any packages not included in that list will neither build in that project
# nor in subprojects!
# It is still possible to enable the full multiboot set plus eventual
# additional packages by adding the Macros: [...] :Macros section and
# omitting the "onlybuild:"-lines.
%else
%if "%target" == "tools" || "%target" == ""
# At least build the tools.
%else
BuildRequires:  %prjconf_multibuild_selection
%endif
%endif
%if "%target" == "tools" || "%target" == ""
Name:           u-boot
%else
Name:           u-boot-%target
%endif
%if 0%{?is_rk3328} && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-rk3328
%endif
%if 0%{?is_rk3399} && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-rk3399
%endif
%if (0%{?is_a64} || 0%{?is_h5}) && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-sun50ia64
%endif
%if 0%{?is_h6} && %{with uboot_atf}
BuildRequires:  arm-trusted-firmware-sun50ih6
%endif
%if %{with uboot_atf}
%if "%{name}" == "u-boot-rock64-rk3328" || "%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399" || "%{name}" == "u-boot-rock960-rk3399" || "${name}" == "u-boot-rock-pi-4-rk3399"
# make_fit_atf.py
BuildRequires:  python3-pyelftools
%endif
%endif
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
%if "%{name}" == "u-boot-sifivefu540"
BuildRequires:  opensbi-sifivefu540 >= 0.7
%endif
%if %x_loader == 1
Obsoletes:      x-loader-%target
Provides:       x-loader-%target
%endif
%if "%{name}" == "u-boot-am335xevm"
# http://git.denx.de/?p=u-boot.git;a=commit;h=8fa7f65dd02c176ee6021eaf40114560b8954ba2
Obsoletes:      am335x_boneblack
Provides:       am335x_boneblack
%endif
%if "%{name}" == "u-boot-bananapim2plush3"
# http://git.denx.de/?p=u-boot.git;a=commit;h=268ae6548779ccd8ba38ce39d43f41be7e0bc133
Obsoletes:      Sinovoip_BPI_M2_Plus
Provides:       Sinovoip_BPI_M2_Plus
%endif
%if "%{name}" == "u-boot-rpiarm64"
Supplements:    modalias(of:NfirmwareT*Craspberrypi%2Cbcm2835-firmwareC*)
# Provides one u-boot image for both RPi3 and RPi4
Obsoletes:      u-boot-rpi3 < %{version}
Provides:       u-boot-rpi3 = %{version}
Obsoletes:      u-boot-rpi4 < %{version}
Provides:       u-boot-rpi4 = %{version}
%endif
%if "%{name}" == "u-boot-xilinxzynqmpvirt"
Obsoletes:      u-boot-xilinxzynqmpgeneric < %{version}
Provides:       u-boot-xilinxzynqmpgeneric = %{version}
%endif

%description
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains the firmware for the %target platform.

%if %tools_only
%package tools
Summary:        Tools for the U-Boot Firmware
Group:          System/Boot

%description tools
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains:
mkimage- a tool that creates kernel bootable images for U-Boot.

%else
%package doc
Summary:        Documentation for the U-Boot Firmware
Group:          Documentation/Other

%description doc
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains documentation for U-Boot firmware.

%endif

%prep
%setup -q -n u-boot-%{archive_version}
%autopatch -p1

%build
%if %tools_only
# needed for include/config/auto.conf
make defconfig
make syncconfig
make %{?_smp_mflags} CFLAGS="%{optflags}" tools-only

%else
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/u-boot.changes | tail -n 1 | cut -d- -f1 )" +%s)
%if 0%{?is_a64} || 0%{?is_h5}
export BL31=%{_datadir}/arm-trusted-firmware-sun50ia64/bl31.bin
%endif
%if 0%{?is_h6}
export BL31=%{_datadir}/arm-trusted-firmware-sun50ih6/bl31.bin
%endif
%if "%{name}" == "u-boot-sifivefu540"
export OPENSBI=%{_datadir}/opensbi/opensbi-sifive-fu540.bin
%endif

%if %{with uboot_atf}
%if "%{name}" == "u-boot-rock64-rk3328"
cp %{_datadir}/arm-trusted-firmware-rk3328/bl31.elf .
%endif
%if "%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399" || "%{name}" == "u-boot-rock-pi-4-rk3399"
cp %{_datadir}/arm-trusted-firmware-rk3399/bl31.elf .
%endif
%endif

%if %{is_zynq}
confname="xilinx_zynq_virt_defconfig"
%elif %{is_zynqmp}
confname="xilinx_zynqmp_virt_defconfig"
%else
confname=$(ls configs | perl -ne '$l=lc; $l=~ s,_,,g; $l eq "%{target}defconfig\n" && print;')
%endif

%if "%target" == "avnetultra96rev1"
export DEVICE_TREE=avnet-ultra96-rev1
%endif
%if "%target" == "xilinxzynqmpzcu102rev10"
export DEVICE_TREE=zynqmp-zcu102-rev1.0
%endif
%if "%target" == "zynqzturn"
export DEVICE_TREE=zynq-zturn
%endif

make %{?_smp_mflags} CROSS_COMPILE= HOSTCFLAGS="%{optflags}" $confname
echo "Attempting to enable fdt apply command (.dtbo) support."
echo "CONFIG_OF_LIBFDT_OVERLAY=y" >> .config
%if "%target" == "rpi3"
echo "Tweaking text base for TF-A."
echo "CONFIG_SYS_TEXT_BASE=0x11000000" >> .config
%endif
make %{?_smp_mflags} CROSS_COMPILE= HOSTCFLAGS="%{optflags}" \
%if ("%{name}" == "u-boot-rock64-rk3328" || "%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399" || "%{name}" == "u-boot-rock-pi-4-rk3399") && %{with uboot_atf}
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
for t in %{rkimages}; do
    ./tools/mkimage -n %soc_name -d spl/u-boot-spl.bin -T $t u-boot-spl.$t || exit 1
done
%endif
%if %rockchip_tpl == 1
for t in %{rkimages}; do
    ./tools/mkimage -n %soc_name -d tpl/u-boot-tpl.bin -T $t u-boot-tpl.$t || exit 1
    cat spl/u-boot-spl-dtb.bin >> u-boot-tpl.$t

done
%endif
%endif

%install
%if %tools_only
install -D -m 0755 tools/mkimage %{buildroot}%{_bindir}/mkimage
install -D -m 0644 doc/mkimage.1 %{buildroot}%{_mandir}/man1/mkimage.1

%else
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/u-boot.changes | tail -n 1 | cut -d- -f1 )" +%s)
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
install -D -m 0644 u-boot%{binext} %{buildroot}%{uboot_dir}/u-boot%{binext}
%if ("%{name}" == "u-boot-rock64-rk3328" || "%{name}" == "u-boot-evb-rk3399" || "%{name}" == "u-boot-firefly-rk3399" || "%{name}" == "u-boot-rock-pi-4-rk3399") && %{with uboot_atf}
install -D -m 0644 u-boot.itb %{buildroot}%{uboot_dir}/u-boot.itb
%endif
%if "%{name}" == "u-boot-qemu-ppce500"
mv %{buildroot}%{uboot_dir}/u-boot%{binext} %{buildroot}%{uboot_dir}/u-boot.e500
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
for t in %{rkimages}; do
    install -D -m 0644 u-boot-spl.$t %{buildroot}%{uboot_dir}/u-boot-spl.$t
done
%endif
%if %rockchip_tpl == 1
install -D -m 0644 tpl/u-boot-tpl.bin %{buildroot}%{uboot_dir}/u-boot-tpl.bin
for t in %{rkimages}; do
    install -D -m 0644 u-boot-tpl.$t %{buildroot}%{uboot_dir}/u-boot-tpl.$t
done
%endif
%if %rockchip_idb == 1
install -D -m 0644 idbloader.img %{buildroot}%{uboot_dir}/idbloader.img
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
%if "%{name}" == "u-boot-zynqzturn"
install -D -m 0644 spl/boot.bin %{buildroot}%{uboot_dir}/boot.bin
%endif
%if "%{name}" == "u-boot-rpi3"
echo -e "# Boot in AArch64 mode\narm_64bit=1" > %{buildroot}%{uboot_dir}/ubootconfig.txt
echo -e "\nkernel_address=0x11000000" >> %{buildroot}%{uboot_dir}/ubootconfig.txt
%endif
%if "%{name}" == "u-boot-rpi4" || "%{name}" == "u-boot-rpiarm64"
echo -e "# Boot in AArch64 mode\narm_64bit=1" > %{buildroot}%{uboot_dir}/ubootconfig.txt
%endif
%if "%{name}" == "u-boot-sifivefu540"
install -D -m 0644 spl/u-boot-spl.bin %{buildroot}%{uboot_dir}/u-boot-spl.bin
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
    cp %{uboot_dir}/u-boot%{binext} /boot/efi/
  fi
fi
%endif
%endif

%if %tools_only
%files tools
%else
%files
%endif
%defattr(-,root,root)
%license Licenses/gpl-2.0.txt

%if %tools_only
%{_bindir}/mkimage
%{_mandir}/man1/mkimage.1.gz
%else
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
%endif

%changelog
