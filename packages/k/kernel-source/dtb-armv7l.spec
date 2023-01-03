#
# spec file for package dtb-armv7l
#
# Copyright (c) 2023 SUSE LLC
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


%define srcversion 6.1
%define patchversion 6.1.2
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120300 )
%define dtc_symbols 1
%endif

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,mkspec,compute-PATCHVERSION.sh,arch-symbols,log.sh,try-disable-staging-driver,compress-vmlinux.sh,mkspec-dtb,check-module-license,klp-symbols,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

Name:           dtb-armv7l
Version:        6.1.2
%if 0%{?is_kotd}
Release:        <RELEASE>.g7fea150
%else
Release:        0
%endif
Summary:        Device Tree files for $MACHINES
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://www.kernel.org/
ExclusiveArch:  armv7l armv7hl
BuildRequires:  cpp
%if 0%{?dtc_symbols}
BuildRequires:  dtc >= 1.4.3
%else
BuildRequires:  dtc >= 1.4.0
%endif
BuildRequires:  xz
Requires:       kernel = %version
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%srcversion.tar.xz
Source3:        kernel-source.rpmlintrc
Source14:       series.conf
Source16:       guards
Source17:       apply-patches
Source21:       config.conf
Source23:       supported.conf
Source33:       check-for-config-changes
Source35:       group-source-files.pl
Source36:       README.PATCH-POLICY.SUSE
Source37:       README.SUSE
Source38:       README.KSYMS
Source39:       config-options.changes.txt
Source40:       source-timestamp
Source46:       split-modules
Source47:       modversions
Source48:       macros.kernel-source
Source49:       kernel-module-subpackage
Source50:       kabi.pl
Source51:       mkspec
Source52:       kernel-source%variant.changes
Source53:       kernel-source.spec.in
Source54:       kernel-binary.spec.in
Source55:       kernel-syms.spec.in
Source56:       kernel-docs.spec.in
Source57:       kernel-cert-subpackage
Source58:       constraints.in
Source60:       config.sh
Source61:       compute-PATCHVERSION.sh
Source62:       old-flavors
Source63:       arch-symbols
Source64:       package-descriptions
Source65:       kernel-spec-macros
Source67:       log.sh
Source68:       host-memcpy-hack.h
Source69:       try-disable-staging-driver
Source70:       kernel-obs-build.spec.in
Source71:       kernel-obs-qa.spec.in
Source72:       compress-vmlinux.sh
Source73:       dtb.spec.in.in
Source74:       mkspec-dtb
Source75:       release-projects
Source76:       check-module-license
Source77:       klp-symbols
Source78:       modules.fips
Source79:       splitflist
Source80:       mergedep
Source81:       moddep
Source82:       modflist
Source83:       kernel-subpackage-build
Source84:       kernel-subpackage-spec
Source85:       kernel-default-base.spec.txt
Source100:      config.tar.bz2
Source101:      config.addon.tar.bz2
Source102:      patches.arch.tar.bz2
Source103:      patches.drivers.tar.bz2
Source104:      patches.fixes.tar.bz2
Source105:      patches.rpmify.tar.bz2
Source106:      patches.suse.tar.bz2
Source108:      patches.addon.tar.bz2
Source109:      patches.kernel.org.tar.bz2
Source110:      patches.apparmor.tar.bz2
Source111:      patches.rt.tar.bz2
Source113:      patches.kabi.tar.bz2
Source120:      kabi.tar.bz2
Source121:      sysctl.tar.bz2
# These files are found in the kernel-source package:
NoSource:       0
NoSource:       3
NoSource:       14
NoSource:       16
NoSource:       17
NoSource:       21
NoSource:       23
NoSource:       33
NoSource:       35
NoSource:       36
NoSource:       37
NoSource:       38
NoSource:       39
NoSource:       40
NoSource:       46
NoSource:       47
NoSource:       48
NoSource:       49
NoSource:       50
NoSource:       51
NoSource:       52
NoSource:       53
NoSource:       54
NoSource:       55
NoSource:       56
NoSource:       57
NoSource:       58
NoSource:       60
NoSource:       61
NoSource:       62
NoSource:       63
NoSource:       64
NoSource:       65
NoSource:       67
NoSource:       68
NoSource:       69
NoSource:       70
NoSource:       71
NoSource:       72
NoSource:       73
NoSource:       74
NoSource:       75
NoSource:       76
NoSource:       77
NoSource:       78
NoSource:       79
NoSource:       80
NoSource:       81
NoSource:       82
NoSource:       83
NoSource:       84
NoSource:       85
NoSource:       100
NoSource:       101
NoSource:       102
NoSource:       103
NoSource:       104
NoSource:       105
NoSource:       106
NoSource:       108
NoSource:       109
NoSource:       110
NoSource:       111
NoSource:       113
NoSource:       120
NoSource:       121

%description
Device Tree files for $MACHINES.

%package -n dtb-am335x
Summary:        TI AM335x based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-am335x
Device Tree files for TI AM335x based systems.

%package -n dtb-am3517
Summary:        TI AM3517 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-am3517
Device Tree files for TI AM3517 based systems.

%package -n dtb-am57xx
Summary:        TI AM57xx based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-am57xx
Device Tree files for TI AM57xx based systems.

%package -n dtb-armada-370
Summary:        Armada 370 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-370
Device Tree files for Armada 370 based systems.

%package -n dtb-armada-375
Summary:        Armada 375 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-375
Device Tree files for Armada 375 based systems.

%package -n dtb-armada-385
Summary:        Armada 385 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-385
Device Tree files for Armada 385 based systems.

%package -n dtb-armada-388
Summary:        Armada 388 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-388
Device Tree files for Armada 388 based systems.

%package -n dtb-armada-398
Summary:        Armada 398 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-398
Device Tree files for Armada 398 based systems.

%package -n dtb-armada-xp
Summary:        Armada XP based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-xp
Device Tree files for Armada XP based systems.

%package -n dtb-bcm2836
Summary:        Raspberry Pi 2 Model B
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-bcm2836
Device Tree files for Raspberry Pi 2 Model B.

%package -n dtb-dove
Summary:        Marvell dove based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-dove
Device Tree files for Marvell dove based systems.

%package -n dtb-exynos4
Summary:        Samsung Exynos 4 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-exynos4
Device Tree files for Samsung Exynos 4 based systems.

%package -n dtb-exynos5
Summary:        Samsung Exynos 5 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-exynos5
Device Tree files for Samsung Exynos 5 based systems.

%package -n dtb-imx5
Summary:        Freescale i.MX51 and i.MX53 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-imx5
Device Tree files for Freescale i.MX51 and i.MX53 based systems.

%package -n dtb-imx6
Summary:        Freescale i.MX6 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-imx6
Device Tree files for Freescale i.MX6 based systems.

%package -n dtb-imx7
Summary:        Freescale i.MX7 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-imx7
Device Tree files for Freescale i.MX7 based systems.

%package -n dtb-keystone
Summary:        TI Keystone 2 based systems
Group:          System/Boot
Provides:       dtb-k2e = %version
Provides:       dtb-k2l = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-keystone
Device Tree files for TI Keystone 2 based systems.

%package -n dtb-meson6
Summary:        Amlogic Meson 6 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-meson6
Device Tree files for Amlogic Meson 6 based systems.

%package -n dtb-meson8
Summary:        Amlogic Meson 8 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-meson8
Device Tree files for Amlogic Meson 8 based systems.

%package -n dtb-meson8b
Summary:        Amlogic Meson 8b based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-meson8b
Device Tree files for Amlogic Meson 8b based systems.

%package -n dtb-mt76
Summary:        MediaTek mt76 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-mt76
Device Tree files for MediaTek mt76 based systems.

%package -n dtb-omap3
Summary:        TI OMAP3 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-omap3
Device Tree files for TI OMAP3 based systems.

%package -n dtb-omap4
Summary:        TI OMAP4 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-omap4
Device Tree files for TI OMAP4 based systems.

%package -n dtb-omap5
Summary:        TI OMAP5 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-omap5
Device Tree files for TI OMAP5 based systems.

%package -n dtb-qcom
Summary:        Qualcomm Snapdragon based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-qcom
Device Tree files for Qualcomm Snapdragon based systems.

%package -n dtb-rk3
Summary:        Rockchip RK3xxx based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-rk3
Device Tree files for Rockchip RK3xxx based systems.

%package -n dtb-socfpga
Summary:        Altera SoC FPGA based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-socfpga
Device Tree files for Altera SoC FPGA based systems.

%package -n dtb-ste
Summary:        ST Ericsson based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-ste
Device Tree files for ST Ericsson based systems.

%package -n dtb-sun4i
Summary:        Allwinner sun4i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun4i
Device Tree files for Allwinner sun4i based systems.

%package -n dtb-sun5i
Summary:        Allwinner sun5i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun5i
Device Tree files for Allwinner sun5i based systems.

%package -n dtb-sun6i
Summary:        Allwinner sun6i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun6i
Device Tree files for Allwinner sun6i based systems.

%package -n dtb-sun7i
Summary:        Allwinner sun7i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun7i
Device Tree files for Allwinner sun7i based systems.

%package -n dtb-sun8i
Summary:        Allwinner sun8i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun8i
Device Tree files for Allwinner sun8i based systems.

%package -n dtb-sun9i
Summary:        Allwinner sun9i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun9i
Device Tree files for Allwinner sun9i based systems.

%package -n dtb-tegra2
Summary:        NVidia Tegra2 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra2
Device Tree files for NVidia Tegra2 based systems.

%package -n dtb-tegra3
Summary:        NVidia Tegra3 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra3
Device Tree files for NVidia Tegra3 based systems.

%package -n dtb-tegra114
Summary:        NVidia Tegra4 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra114
Device Tree files for NVidia Tegra4 based systems.

%package -n dtb-tegra124
Summary:        NVidia Tegra K1 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra124
Device Tree files for NVidia Tegra K1 based systems.

%package -n dtb-vexpress
Summary:        ARM Versatile Express machines
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-vexpress
Device Tree files for ARM Versatile Express machines.

%package -n dtb-vf500
Summary:        Freescale Vybrid VF500 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-vf500
Device Tree files for Freescale Vybrid VF500 based systems.

%package -n dtb-vf6
Summary:        Freescale Vybrid VF610 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-vf6
Device Tree files for Freescale Vybrid VF610 based systems.

%package -n dtb-xenvm
Summary:        Xen virtual machines
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-xenvm
Device Tree files for Xen virtual machines.

%package -n dtb-zynq
Summary:        Xilinx Zynq based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-zynq
Device Tree files for Xilinx Zynq based systems.



%prep
# Unpack all sources and patches
%setup -q -c -T -a 0 -a 100 -a 101 -a 102 -a 103 -a 104 -a 105 -a 106 -a 108 -a 109 -a 110 -a 111 -a 113 -a 120 -a 121
cd linux-%srcversion
%_sourcedir/apply-patches %_sourcedir/series.conf ..


%build
source=linux-%srcversion
cp $source/COPYING .
SRCDIR=$PWD/$source
mkdir pp
PPDIR=$PWD/pp
export DTC_FLAGS="-R 4 -p 0x1000"
%if 0%{?dtc_symbols}
DTC_FLAGS="$DTC_FLAGS -@"
%endif

cd $source/arch/arm/boot/dts
for dts in am335x-*.dts am3517*.dts am57xx-*.dts armada-370-*.dts armada-375-*.dts armada-385-*.dts armada-388-*.dts armada-398-*.dts armada-xp-*.dts bcm2836*.dts dove-*.dts exynos4*.dts exynos5*.dts imx5*.dts imx6*.dts imx7*.dts keystone-*.dts meson6-*.dts meson8-*.dts meson8b-*.dts mt76*.dts omap3*.dts omap4*.dts omap5*.dts qcom-*.dts rk3*.dts socfpga_*.dts ste-*.dts sun4i-*.dts sun5i-*.dts sun6i-*.dts sun7i-*.dts sun8i-*.dts sun9i-*.dts tegra20-*.dts tegra30-*.dts tegra114-*.dts tegra124-*.dts vexpress-*.dts vf500-*.dts vf610-*.dts xenvm-*.dts zynq-*.dts ; do
    target=${dts%*.dts}
    mkdir -p $PPDIR/$(dirname $target)
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $target.dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $target) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

%define dtbdir /boot/dtb-%kernelrelease

%install

cd pp
for dts in am335x-*.dts am3517*.dts am57xx-*.dts armada-370-*.dts armada-375-*.dts armada-385-*.dts armada-388-*.dts armada-398-*.dts armada-xp-*.dts bcm2836*.dts dove-*.dts exynos4*.dts exynos5*.dts imx5*.dts imx6*.dts imx7*.dts keystone-*.dts meson6-*.dts meson8-*.dts meson8b-*.dts mt76*.dts omap3*.dts omap4*.dts omap5*.dts qcom-*.dts rk3*.dts socfpga_*.dts ste-*.dts sun4i-*.dts sun5i-*.dts sun6i-*.dts sun7i-*.dts sun8i-*.dts sun9i-*.dts tegra20-*.dts tegra30-*.dts tegra114-*.dts tegra124-*.dts vexpress-*.dts vf500-*.dts vf610-*.dts xenvm-*.dts zynq-*.dts ; do
    target=${dts%*.dts}
    install -m 755 -d %{buildroot}%{dtbdir}/$(dirname $target)
    # install -m 644 COPYING %{buildroot}%{dtbdir}/$(dirname $target)
    install -m 644 $target.dtb %{buildroot}%{dtbdir}/$(dirname $target)
%ifarch aarch64 riscv64
    # HACK: work around U-Boot ignoring vendor dir
    baselink=%{dtbdir}/$(basename $target).dtb
    vendordir=$(basename $(dirname $target))
    ln -s $target.dtb %{buildroot}$baselink
    echo $baselink >> ../dtb-$vendordir.list
%endif
done
cd -

%post -n dtb-am335x
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-am3517
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-am57xx
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-armada-370
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-armada-375
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-armada-385
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-armada-388
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-armada-398
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-armada-xp
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-bcm2836
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-dove
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-exynos4
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-exynos5
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-imx5
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-imx6
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-imx7
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-keystone
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-meson6
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-meson8
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-meson8b
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-mt76
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-omap3
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-omap4
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-omap5
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-qcom
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-rk3
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-socfpga
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-ste
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sun4i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sun5i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sun6i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sun7i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sun8i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sun9i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-tegra2
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-tegra3
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-tegra114
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-tegra124
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-vexpress
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-vf500
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-vf6
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-xenvm
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-zynq
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch aarch64 riscv64
%files -n dtb-am335x -f dtb-am335x.list
%else
%files -n dtb-am335x
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/am335x-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-am3517 -f dtb-am3517.list
%else
%files -n dtb-am3517
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/am3517*.dtb

%ifarch aarch64 riscv64
%files -n dtb-am57xx -f dtb-am57xx.list
%else
%files -n dtb-am57xx
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/am57xx-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-armada-370 -f dtb-armada-370.list
%else
%files -n dtb-armada-370
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/armada-370-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-armada-375 -f dtb-armada-375.list
%else
%files -n dtb-armada-375
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/armada-375-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-armada-385 -f dtb-armada-385.list
%else
%files -n dtb-armada-385
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/armada-385-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-armada-388 -f dtb-armada-388.list
%else
%files -n dtb-armada-388
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/armada-388-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-armada-398 -f dtb-armada-398.list
%else
%files -n dtb-armada-398
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/armada-398-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-armada-xp -f dtb-armada-xp.list
%else
%files -n dtb-armada-xp
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/armada-xp-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-bcm2836 -f dtb-bcm2836.list
%else
%files -n dtb-bcm2836
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/bcm2836*.dtb

%ifarch aarch64 riscv64
%files -n dtb-dove -f dtb-dove.list
%else
%files -n dtb-dove
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/dove-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-exynos4 -f dtb-exynos4.list
%else
%files -n dtb-exynos4
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/exynos4*.dtb

%ifarch aarch64 riscv64
%files -n dtb-exynos5 -f dtb-exynos5.list
%else
%files -n dtb-exynos5
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/exynos5*.dtb

%ifarch aarch64 riscv64
%files -n dtb-imx5 -f dtb-imx5.list
%else
%files -n dtb-imx5
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/imx5*.dtb

%ifarch aarch64 riscv64
%files -n dtb-imx6 -f dtb-imx6.list
%else
%files -n dtb-imx6
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/imx6*.dtb

%ifarch aarch64 riscv64
%files -n dtb-imx7 -f dtb-imx7.list
%else
%files -n dtb-imx7
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/imx7*.dtb

%ifarch aarch64 riscv64
%files -n dtb-keystone -f dtb-keystone.list
%else
%files -n dtb-keystone
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/keystone-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-meson6 -f dtb-meson6.list
%else
%files -n dtb-meson6
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/meson6-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-meson8 -f dtb-meson8.list
%else
%files -n dtb-meson8
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/meson8-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-meson8b -f dtb-meson8b.list
%else
%files -n dtb-meson8b
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/meson8b-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-mt76 -f dtb-mt76.list
%else
%files -n dtb-mt76
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/mt76*.dtb

%ifarch aarch64 riscv64
%files -n dtb-omap3 -f dtb-omap3.list
%else
%files -n dtb-omap3
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/omap3*.dtb

%ifarch aarch64 riscv64
%files -n dtb-omap4 -f dtb-omap4.list
%else
%files -n dtb-omap4
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/omap4*.dtb

%ifarch aarch64 riscv64
%files -n dtb-omap5 -f dtb-omap5.list
%else
%files -n dtb-omap5
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/omap5*.dtb

%ifarch aarch64 riscv64
%files -n dtb-qcom -f dtb-qcom.list
%else
%files -n dtb-qcom
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/qcom-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-rk3 -f dtb-rk3.list
%else
%files -n dtb-rk3
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/rk3*.dtb

%ifarch aarch64 riscv64
%files -n dtb-socfpga -f dtb-socfpga.list
%else
%files -n dtb-socfpga
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/socfpga_*.dtb

%ifarch aarch64 riscv64
%files -n dtb-ste -f dtb-ste.list
%else
%files -n dtb-ste
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/ste-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sun4i -f dtb-sun4i.list
%else
%files -n dtb-sun4i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/sun4i-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sun5i -f dtb-sun5i.list
%else
%files -n dtb-sun5i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/sun5i-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sun6i -f dtb-sun6i.list
%else
%files -n dtb-sun6i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/sun6i-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sun7i -f dtb-sun7i.list
%else
%files -n dtb-sun7i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/sun7i-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sun8i -f dtb-sun8i.list
%else
%files -n dtb-sun8i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/sun8i-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sun9i -f dtb-sun9i.list
%else
%files -n dtb-sun9i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/sun9i-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-tegra2 -f dtb-tegra2.list
%else
%files -n dtb-tegra2
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/tegra20-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-tegra3 -f dtb-tegra3.list
%else
%files -n dtb-tegra3
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/tegra30-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-tegra114 -f dtb-tegra114.list
%else
%files -n dtb-tegra114
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/tegra114-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-tegra124 -f dtb-tegra124.list
%else
%files -n dtb-tegra124
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/tegra124-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-vexpress -f dtb-vexpress.list
%else
%files -n dtb-vexpress
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/vexpress-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-vf500 -f dtb-vf500.list
%else
%files -n dtb-vf500
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/vf500-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-vf6 -f dtb-vf6.list
%else
%files -n dtb-vf6
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/vf610-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-xenvm -f dtb-xenvm.list
%else
%files -n dtb-xenvm
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/xenvm-*.dtb

%ifarch aarch64 riscv64
%files -n dtb-zynq -f dtb-zynq.list
%else
%files -n dtb-zynq
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%{dtbdir}/zynq-*.dtb

%changelog
