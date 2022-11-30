#
# spec file for package dtb-aarch64
#
# Copyright (c) 2022 SUSE LLC
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


%define srcversion 6.0
%define patchversion 6.0.10
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120300 )
%define dtc_symbols 1
%endif

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,mkspec,compute-PATCHVERSION.sh,arch-symbols,log.sh,try-disable-staging-driver,compress-vmlinux.sh,mkspec-dtb,check-module-license,klp-symbols,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

Name:           dtb-aarch64
Version:        6.0.10
%if 0%{?is_kotd}
Release:        <RELEASE>.g582305b
%else
Release:        0
%endif
Summary:        Device Tree files for $MACHINES
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://www.kernel.org/
ExclusiveArch:  aarch64
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

%package -n dtb-allwinner
Summary:        Allwinner based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-allwinner
Device Tree files for Allwinner based arm64 systems.

%package -n dtb-altera
Summary:        Altera based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-altera
Device Tree files for Altera based arm64 systems.

%package -n dtb-amazon
Summary:        Amazon based arm64 systems
Group:          System/Boot
Provides:       dtb-al = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-amazon
Device Tree files for Amazon based arm64 systems.

%package -n dtb-amd
Summary:        AMD based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-amd
Device Tree files for AMD based arm64 systems.

%package -n dtb-amlogic
Summary:        Amlogic based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-amlogic
Device Tree files for Amlogic based arm64 systems.

%package -n dtb-apm
Summary:        AppliedMicro based arm64 systems
Group:          System/Boot
Provides:       dtb-apm-mustang = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-apm
Device Tree files for AppliedMicro based arm64 systems.

%package -n dtb-apple
Summary:        Apple SOC based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-apple
Device Tree files for Apple SOC based arm64 systems.

%package -n dtb-arm
Summary:        ARM Ltd. based arm64 systems
Group:          System/Boot
Provides:       dtb-foundation-v8 = %version
Provides:       dtb-rtsm_ve-aemv8a = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-arm
Device Tree files for ARM Ltd. based arm64 systems.

%package -n dtb-broadcom
Summary:        Broadcom based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-broadcom
Device Tree files for Broadcom based arm64 systems.

%package -n dtb-cavium
Summary:        Cavium based arm64 systems
Group:          System/Boot
Provides:       dtb-thunder-88xx = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-cavium
Device Tree files for Cavium based arm64 systems.

%package -n dtb-exynos
Summary:        Samsung Exynos based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-exynos
Device Tree files for Samsung Exynos based arm64 systems.

%package -n dtb-freescale
Summary:        NXP (Freescale) based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-freescale
Device Tree files for NXP (Freescale) based arm64 systems.

%package -n dtb-hisilicon
Summary:        HiSilicon based arm64 systems
Group:          System/Boot
Provides:       dtb-hisilicon64 = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-hisilicon
Device Tree files for HiSilicon based arm64 systems.

%package -n dtb-lg
Summary:        LG based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-lg
Device Tree files for LG based arm64 systems.

%package -n dtb-marvell
Summary:        Marvell based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-marvell
Device Tree files for Marvell based arm64 systems.

%package -n dtb-mediatek
Summary:        MediaTek based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-mediatek
Device Tree files for MediaTek based arm64 systems.

%package -n dtb-nvidia
Summary:        Nvidia based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-nvidia
Device Tree files for Nvidia based arm64 systems.

%package -n dtb-qcom
Summary:        Qualcomm based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-qcom
Device Tree files for Qualcomm based arm64 systems.

%package -n dtb-renesas
Summary:        Renesas based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-renesas
Device Tree files for Renesas based arm64 systems.

%package -n dtb-rockchip
Summary:        Rockchip based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-rockchip
Device Tree files for Rockchip based arm64 systems.

%package -n dtb-socionext
Summary:        Socionext based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-socionext
Device Tree files for Socionext based arm64 systems.

%package -n dtb-sprd
Summary:        Spreadtrum based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sprd
Device Tree files for Spreadtrum based arm64 systems.

%package -n dtb-xilinx
Summary:        Xilinx based arm64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-xilinx
Device Tree files for Xilinx based arm64 systems.



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

cd $source/arch/arm64/boot/dts
for dts in allwinner/*.dts altera/*.dts amazon/*.dts amd/*.dts amlogic/*.dts apm/*.dts apple/*.dts arm/*.dts broadcom/*.dts cavium/*.dts exynos/*.dts freescale/*.dts hisilicon/*.dts lg/*.dts marvell/*.dts mediatek/*.dts nvidia/*.dts qcom/*.dts renesas/*.dts rockchip/*.dts socionext/*.dts sprd/*.dts xilinx/*.dts ; do
    target=${dts%*.dts}
    mkdir -p $PPDIR/$(dirname $target)
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $target.dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $target) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

%define dtbdir /boot/dtb-%kernelrelease

%install

cd pp
for dts in allwinner/*.dts altera/*.dts amazon/*.dts amd/*.dts amlogic/*.dts apm/*.dts apple/*.dts arm/*.dts broadcom/*.dts cavium/*.dts exynos/*.dts freescale/*.dts hisilicon/*.dts lg/*.dts marvell/*.dts mediatek/*.dts nvidia/*.dts qcom/*.dts renesas/*.dts rockchip/*.dts socionext/*.dts sprd/*.dts xilinx/*.dts ; do
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

%post -n dtb-allwinner
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-altera
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-amazon
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-amd
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-amlogic
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-apm
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-apple
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-arm
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-broadcom
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-cavium
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-exynos
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-freescale
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-hisilicon
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-lg
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-marvell
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-mediatek
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-nvidia
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

%post -n dtb-renesas
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-rockchip
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-socionext
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sprd
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-xilinx
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch aarch64 riscv64
%files -n dtb-allwinner -f dtb-allwinner.list
%else
%files -n dtb-allwinner
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-altera -f dtb-altera.list
%else
%files -n dtb-altera
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/altera
%{dtbdir}/altera/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-amazon -f dtb-amazon.list
%else
%files -n dtb-amazon
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/amazon
%{dtbdir}/amazon/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-amd -f dtb-amd.list
%else
%files -n dtb-amd
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/amd
%{dtbdir}/amd/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-amlogic -f dtb-amlogic.list
%else
%files -n dtb-amlogic
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/amlogic
%{dtbdir}/amlogic/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-apm -f dtb-apm.list
%else
%files -n dtb-apm
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/apm
%{dtbdir}/apm/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-apple -f dtb-apple.list
%else
%files -n dtb-apple
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/apple
%{dtbdir}/apple/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-arm -f dtb-arm.list
%else
%files -n dtb-arm
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/arm
%{dtbdir}/arm/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-broadcom -f dtb-broadcom.list
%else
%files -n dtb-broadcom
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/broadcom
%{dtbdir}/broadcom/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-cavium -f dtb-cavium.list
%else
%files -n dtb-cavium
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/cavium
%{dtbdir}/cavium/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-exynos -f dtb-exynos.list
%else
%files -n dtb-exynos
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/exynos
%{dtbdir}/exynos/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-freescale -f dtb-freescale.list
%else
%files -n dtb-freescale
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/freescale
%{dtbdir}/freescale/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-hisilicon -f dtb-hisilicon.list
%else
%files -n dtb-hisilicon
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/hisilicon
%{dtbdir}/hisilicon/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-lg -f dtb-lg.list
%else
%files -n dtb-lg
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/lg
%{dtbdir}/lg/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-marvell -f dtb-marvell.list
%else
%files -n dtb-marvell
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-mediatek -f dtb-mediatek.list
%else
%files -n dtb-mediatek
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/mediatek
%{dtbdir}/mediatek/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-nvidia -f dtb-nvidia.list
%else
%files -n dtb-nvidia
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nvidia
%{dtbdir}/nvidia/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-qcom -f dtb-qcom.list
%else
%files -n dtb-qcom
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/qcom
%{dtbdir}/qcom/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-renesas -f dtb-renesas.list
%else
%files -n dtb-renesas
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/renesas
%{dtbdir}/renesas/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-rockchip -f dtb-rockchip.list
%else
%files -n dtb-rockchip
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/rockchip
%{dtbdir}/rockchip/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-socionext -f dtb-socionext.list
%else
%files -n dtb-socionext
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/socionext
%{dtbdir}/socionext/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sprd -f dtb-sprd.list
%else
%files -n dtb-sprd
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/sprd
%{dtbdir}/sprd/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-xilinx -f dtb-xilinx.list
%else
%files -n dtb-xilinx
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/xilinx
%{dtbdir}/xilinx/*.dtb

%changelog
