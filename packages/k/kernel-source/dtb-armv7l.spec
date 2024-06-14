#
# spec file for package dtb-armv7l
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


%define srcversion 6.9
%define patchversion 6.9.4
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,mkspec,compute-PATCHVERSION.sh,arch-symbols,log.sh,try-disable-staging-driver,compress-vmlinux.sh,mkspec-dtb,check-module-license,klp-symbols,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

Name:           dtb-armv7l
Version:        6.9.4
%if 0%{?is_kotd}
Release:        <RELEASE>.gad8659c
%else
Release:        0
%endif
Summary:        Device Tree files for $MACHINES
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://www.kernel.org/
BuildRequires:  cpp
BuildRequires:  dtc >= 1.4.3
BuildRequires:  xz
%if ! 0%{?is_kotd} || ! %{?is_kotd_qa}%{!?is_kotd_qa:0}
ExclusiveArch:  armv7l armv7hl
%else
ExclusiveArch:  do_not_build
%endif

%define dtbdir /boot/dtb-%kernelrelease

Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%srcversion.tar.xz
Source3:        kernel-source.rpmlintrc
Source14:       series.conf
Source16:       guards
Source17:       apply-patches
Source19:       kernel-binary-conflicts
Source20:       obsolete-kmps
Source21:       config.conf
Source23:       supported.conf
Source33:       check-for-config-changes
Source35:       group-source-files.pl
Source36:       README.PATCH-POLICY.SUSE
Source37:       README.SUSE
Source38:       README.KSYMS
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
Source86:       old_changelog.txt
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
Source114:      patches.drm.tar.bz2
Source120:      kabi.tar.bz2
Source121:      sysctl.tar.bz2
# These files are found in the kernel-source package:
NoSource:       0
NoSource:       3
NoSource:       14
NoSource:       16
NoSource:       17
NoSource:       19
NoSource:       20
NoSource:       21
NoSource:       23
NoSource:       33
NoSource:       35
NoSource:       36
NoSource:       37
NoSource:       38
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
NoSource:       86
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
NoSource:       114
NoSource:       120
NoSource:       121
Requires:       kernel = %version

%description
Device Tree files for $MACHINES.

%package -n dtb-am335x
Summary:        TI AM335x based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-am335x
Device Tree files for TI AM335x based systems.

%post -n dtb-am335x
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-am335x -f dtb-am335x.list
%else
%files -n dtb-am335x
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/omap
%{dtbdir}/ti/omap/am335x-*.dtb

%package -n dtb-am3517
Summary:        TI AM3517 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-am3517
Device Tree files for TI AM3517 based systems.

%post -n dtb-am3517
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-am3517 -f dtb-am3517.list
%else
%files -n dtb-am3517
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/omap
%{dtbdir}/ti/omap/am3517*.dtb

%package -n dtb-am57xx
Summary:        TI AM57xx based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-am57xx
Device Tree files for TI AM57xx based systems.

%post -n dtb-am57xx
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-am57xx -f dtb-am57xx.list
%else
%files -n dtb-am57xx
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/omap
%{dtbdir}/ti/omap/am57xx-*.dtb

%package -n dtb-armada-370
Summary:        Armada 370 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-370
Device Tree files for Armada 370 based systems.

%post -n dtb-armada-370
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-armada-370 -f dtb-armada-370.list
%else
%files -n dtb-armada-370
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/armada-370-*.dtb

%package -n dtb-armada-375
Summary:        Armada 375 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-375
Device Tree files for Armada 375 based systems.

%post -n dtb-armada-375
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-armada-375 -f dtb-armada-375.list
%else
%files -n dtb-armada-375
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/armada-375-*.dtb

%package -n dtb-armada-385
Summary:        Armada 385 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-385
Device Tree files for Armada 385 based systems.

%post -n dtb-armada-385
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-armada-385 -f dtb-armada-385.list
%else
%files -n dtb-armada-385
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/armada-385-*.dtb

%package -n dtb-armada-388
Summary:        Armada 388 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-388
Device Tree files for Armada 388 based systems.

%post -n dtb-armada-388
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-armada-388 -f dtb-armada-388.list
%else
%files -n dtb-armada-388
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/armada-388-*.dtb

%package -n dtb-armada-398
Summary:        Armada 398 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-398
Device Tree files for Armada 398 based systems.

%post -n dtb-armada-398
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-armada-398 -f dtb-armada-398.list
%else
%files -n dtb-armada-398
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/armada-398-*.dtb

%package -n dtb-armada-xp
Summary:        Armada XP based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-armada-xp
Device Tree files for Armada XP based systems.

%post -n dtb-armada-xp
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-armada-xp -f dtb-armada-xp.list
%else
%files -n dtb-armada-xp
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/armada-xp-*.dtb

%package -n dtb-bcm2836
Summary:        Raspberry Pi 2 Model B
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-bcm2836
Device Tree files for Raspberry Pi 2 Model B.

%post -n dtb-bcm2836
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-bcm2836 -f dtb-bcm2836.list
%else
%files -n dtb-bcm2836
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/broadcom
%{dtbdir}/broadcom/bcm2836*.dtb

%package -n dtb-dove
Summary:        Marvell dove based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-dove
Device Tree files for Marvell dove based systems.

%post -n dtb-dove
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-dove -f dtb-dove.list
%else
%files -n dtb-dove
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/marvell
%{dtbdir}/marvell/dove-*.dtb

%package -n dtb-exynos4
Summary:        Samsung Exynos 4 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-exynos4
Device Tree files for Samsung Exynos 4 based systems.

%post -n dtb-exynos4
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-exynos4 -f dtb-exynos4.list
%else
%files -n dtb-exynos4
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/samsung
%{dtbdir}/samsung/exynos4*.dtb

%package -n dtb-exynos5
Summary:        Samsung Exynos 5 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-exynos5
Device Tree files for Samsung Exynos 5 based systems.

%post -n dtb-exynos5
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-exynos5 -f dtb-exynos5.list
%else
%files -n dtb-exynos5
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/samsung
%{dtbdir}/samsung/exynos5*.dtb

%package -n dtb-imx5
Summary:        Freescale i.MX51 and i.MX53 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-imx5
Device Tree files for Freescale i.MX51 and i.MX53 based systems.

%post -n dtb-imx5
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-imx5 -f dtb-imx5.list
%else
%files -n dtb-imx5
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nxp
%dir %{dtbdir}/nxp/imx
%{dtbdir}/nxp/imx/imx5*.dtb

%package -n dtb-imx6
Summary:        Freescale i.MX6 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-imx6
Device Tree files for Freescale i.MX6 based systems.

%post -n dtb-imx6
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-imx6 -f dtb-imx6.list
%else
%files -n dtb-imx6
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nxp
%dir %{dtbdir}/nxp/imx
%{dtbdir}/nxp/imx/imx6*.dtb

%package -n dtb-imx7
Summary:        Freescale i.MX7 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-imx7
Device Tree files for Freescale i.MX7 based systems.

%post -n dtb-imx7
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-imx7 -f dtb-imx7.list
%else
%files -n dtb-imx7
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nxp
%dir %{dtbdir}/nxp/imx
%{dtbdir}/nxp/imx/imx7*.dtb

%package -n dtb-keystone
Summary:        TI Keystone 2 based systems
Group:          System/Boot
Provides:       dtb-k2e = %version
Provides:       dtb-k2l = %version
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-keystone
Device Tree files for TI Keystone 2 based systems.

%post -n dtb-keystone
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-keystone -f dtb-keystone.list
%else
%files -n dtb-keystone
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/keystone
%{dtbdir}/ti/keystone/keystone-*.dtb

%package -n dtb-meson6
Summary:        Amlogic Meson 6 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-meson6
Device Tree files for Amlogic Meson 6 based systems.

%post -n dtb-meson6
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-meson6 -f dtb-meson6.list
%else
%files -n dtb-meson6
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/amlogic
%{dtbdir}/amlogic/meson6-*.dtb

%package -n dtb-meson8
Summary:        Amlogic Meson 8 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-meson8
Device Tree files for Amlogic Meson 8 based systems.

%post -n dtb-meson8
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-meson8 -f dtb-meson8.list
%else
%files -n dtb-meson8
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/amlogic
%{dtbdir}/amlogic/meson8-*.dtb

%package -n dtb-meson8b
Summary:        Amlogic Meson 8b based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-meson8b
Device Tree files for Amlogic Meson 8b based systems.

%post -n dtb-meson8b
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-meson8b -f dtb-meson8b.list
%else
%files -n dtb-meson8b
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/amlogic
%{dtbdir}/amlogic/meson8b-*.dtb

%package -n dtb-mt76
Summary:        MediaTek mt76 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-mt76
Device Tree files for MediaTek mt76 based systems.

%post -n dtb-mt76
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-mt76 -f dtb-mt76.list
%else
%files -n dtb-mt76
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/mediatek
%{dtbdir}/mediatek/mt76*.dtb

%package -n dtb-omap3
Summary:        TI OMAP3 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-omap3
Device Tree files for TI OMAP3 based systems.

%post -n dtb-omap3
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-omap3 -f dtb-omap3.list
%else
%files -n dtb-omap3
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/omap
%{dtbdir}/ti/omap/omap3*.dtb

%package -n dtb-omap4
Summary:        TI OMAP4 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-omap4
Device Tree files for TI OMAP4 based systems.

%post -n dtb-omap4
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-omap4 -f dtb-omap4.list
%else
%files -n dtb-omap4
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/omap
%{dtbdir}/ti/omap/omap4*.dtb

%package -n dtb-omap5
Summary:        TI OMAP5 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-omap5
Device Tree files for TI OMAP5 based systems.

%post -n dtb-omap5
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-omap5 -f dtb-omap5.list
%else
%files -n dtb-omap5
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/ti
%dir %{dtbdir}/ti/omap
%{dtbdir}/ti/omap/omap5*.dtb

%package -n dtb-qcom
Summary:        Qualcomm Snapdragon based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-qcom
Device Tree files for Qualcomm Snapdragon based systems.

%post -n dtb-qcom
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-qcom -f dtb-qcom.list
%else
%files -n dtb-qcom
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/qcom
%{dtbdir}/qcom/qcom-*.dtb

%package -n dtb-rk3
Summary:        Rockchip RK3xxx based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-rk3
Device Tree files for Rockchip RK3xxx based systems.

%post -n dtb-rk3
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-rk3 -f dtb-rk3.list
%else
%files -n dtb-rk3
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/rockchip
%{dtbdir}/rockchip/rk3*.dtb

%package -n dtb-socfpga
Summary:        Altera SoC FPGA based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-socfpga
Device Tree files for Altera SoC FPGA based systems.

%post -n dtb-socfpga
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-socfpga -f dtb-socfpga.list
%else
%files -n dtb-socfpga
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/intel
%dir %{dtbdir}/intel/socfpga
%{dtbdir}/intel/socfpga/socfpga_*.dtb

%package -n dtb-ste
Summary:        ST Ericsson based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-ste
Device Tree files for ST Ericsson based systems.

%post -n dtb-ste
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-ste -f dtb-ste.list
%else
%files -n dtb-ste
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/st
%{dtbdir}/st/ste-*.dtb

%package -n dtb-sun4i
Summary:        Allwinner sun4i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun4i
Device Tree files for Allwinner sun4i based systems.

%post -n dtb-sun4i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sun4i -f dtb-sun4i.list
%else
%files -n dtb-sun4i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/sun4i-*.dtb

%package -n dtb-sun5i
Summary:        Allwinner sun5i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun5i
Device Tree files for Allwinner sun5i based systems.

%post -n dtb-sun5i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sun5i -f dtb-sun5i.list
%else
%files -n dtb-sun5i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/sun5i-*.dtb

%package -n dtb-sun6i
Summary:        Allwinner sun6i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun6i
Device Tree files for Allwinner sun6i based systems.

%post -n dtb-sun6i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sun6i -f dtb-sun6i.list
%else
%files -n dtb-sun6i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/sun6i-*.dtb

%package -n dtb-sun7i
Summary:        Allwinner sun7i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun7i
Device Tree files for Allwinner sun7i based systems.

%post -n dtb-sun7i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sun7i -f dtb-sun7i.list
%else
%files -n dtb-sun7i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/sun7i-*.dtb

%package -n dtb-sun8i
Summary:        Allwinner sun8i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun8i
Device Tree files for Allwinner sun8i based systems.

%post -n dtb-sun8i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sun8i -f dtb-sun8i.list
%else
%files -n dtb-sun8i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/sun8i-*.dtb

%package -n dtb-sun9i
Summary:        Allwinner sun9i based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sun9i
Device Tree files for Allwinner sun9i based systems.

%post -n dtb-sun9i
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sun9i -f dtb-sun9i.list
%else
%files -n dtb-sun9i
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/sun9i-*.dtb

%package -n dtb-tegra2
Summary:        NVidia Tegra2 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra2
Device Tree files for NVidia Tegra2 based systems.

%post -n dtb-tegra2
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-tegra2 -f dtb-tegra2.list
%else
%files -n dtb-tegra2
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nvidia
%{dtbdir}/nvidia/tegra20-*.dtb

%package -n dtb-tegra3
Summary:        NVidia Tegra3 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra3
Device Tree files for NVidia Tegra3 based systems.

%post -n dtb-tegra3
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-tegra3 -f dtb-tegra3.list
%else
%files -n dtb-tegra3
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nvidia
%{dtbdir}/nvidia/tegra30-*.dtb

%package -n dtb-tegra114
Summary:        NVidia Tegra4 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra114
Device Tree files for NVidia Tegra4 based systems.

%post -n dtb-tegra114
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-tegra114 -f dtb-tegra114.list
%else
%files -n dtb-tegra114
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nvidia
%{dtbdir}/nvidia/tegra114-*.dtb

%package -n dtb-tegra124
Summary:        NVidia Tegra K1 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-tegra124
Device Tree files for NVidia Tegra K1 based systems.

%post -n dtb-tegra124
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-tegra124 -f dtb-tegra124.list
%else
%files -n dtb-tegra124
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nvidia
%{dtbdir}/nvidia/tegra124-*.dtb

%package -n dtb-vexpress
Summary:        ARM Versatile Express machines
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-vexpress
Device Tree files for ARM Versatile Express machines.

%post -n dtb-vexpress
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-vexpress -f dtb-vexpress.list
%else
%files -n dtb-vexpress
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/arm
%{dtbdir}/arm/vexpress-*.dtb

%package -n dtb-vf500
Summary:        Freescale Vybrid VF500 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-vf500
Device Tree files for Freescale Vybrid VF500 based systems.

%post -n dtb-vf500
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-vf500 -f dtb-vf500.list
%else
%files -n dtb-vf500
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nxp
%dir %{dtbdir}/nxp/vf
%{dtbdir}/nxp/vf/vf500-*.dtb

%package -n dtb-vf6
Summary:        Freescale Vybrid VF610 based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-vf6
Device Tree files for Freescale Vybrid VF610 based systems.

%post -n dtb-vf6
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-vf6 -f dtb-vf6.list
%else
%files -n dtb-vf6
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/nxp
%dir %{dtbdir}/nxp/vf
%{dtbdir}/nxp/vf/vf610-*.dtb

%package -n dtb-xenvm
Summary:        Xen virtual machines
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-xenvm
Device Tree files for Xen virtual machines.

%post -n dtb-xenvm
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-xenvm -f dtb-xenvm.list
%else
%files -n dtb-xenvm
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/xen
%{dtbdir}/xen/xenvm-*.dtb

%package -n dtb-zynq
Summary:        Xilinx Zynq based systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-zynq
Device Tree files for Xilinx Zynq based systems.

%post -n dtb-zynq
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-zynq -f dtb-zynq.list
%else
%files -n dtb-zynq
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/xilinx
%{dtbdir}/xilinx/zynq-*.dtb



%prep
# Unpack all sources and patches
%setup -q -c -T -a 0 -a 100 -a 101 -a 102 -a 103 -a 104 -a 105 -a 106 -a 108 -a 109 -a 110 -a 111 -a 113 -a 114 -a 120 -a 121
cd linux-%srcversion
%_sourcedir/apply-patches %_sourcedir/series.conf ..

%build
source=linux-%srcversion
cp $source/COPYING .
SRCDIR=$PWD/$source
mkdir pp
PPDIR=$PWD/pp
export DTC_FLAGS="-R 4 -p 0x1000"
DTC_FLAGS="$DTC_FLAGS -@"

cd $source/arch/arm/boot/dts
for dts in ti/omap/am335x-*.dts ti/omap/am3517*.dts ti/omap/am57xx-*.dts marvell/armada-370-*.dts marvell/armada-375-*.dts marvell/armada-385-*.dts marvell/armada-388-*.dts marvell/armada-398-*.dts marvell/armada-xp-*.dts broadcom/bcm2836*.dts marvell/dove-*.dts samsung/exynos4*.dts samsung/exynos5*.dts nxp/imx/imx5*.dts nxp/imx/imx6*.dts nxp/imx/imx7*.dts ti/keystone/keystone-*.dts amlogic/meson6-*.dts amlogic/meson8-*.dts amlogic/meson8b-*.dts mediatek/mt76*.dts ti/omap/omap3*.dts ti/omap/omap4*.dts ti/omap/omap5*.dts qcom/qcom-*.dts rockchip/rk3*.dts intel/socfpga/socfpga_*.dts st/ste-*.dts allwinner/sun4i-*.dts allwinner/sun5i-*.dts allwinner/sun6i-*.dts allwinner/sun7i-*.dts allwinner/sun8i-*.dts allwinner/sun9i-*.dts nvidia/tegra20-*.dts nvidia/tegra30-*.dts nvidia/tegra114-*.dts nvidia/tegra124-*.dts arm/vexpress-*.dts nxp/vf/vf500-*.dts nxp/vf/vf610-*.dts xen/xenvm-*.dts xilinx/zynq-*.dts ; do
    target=${dts%*.dts}
    mkdir -p $PPDIR/$(dirname $target)
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $target.dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $target) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

%install
cd pp
for dts in ti/omap/am335x-*.dts ti/omap/am3517*.dts ti/omap/am57xx-*.dts marvell/armada-370-*.dts marvell/armada-375-*.dts marvell/armada-385-*.dts marvell/armada-388-*.dts marvell/armada-398-*.dts marvell/armada-xp-*.dts broadcom/bcm2836*.dts marvell/dove-*.dts samsung/exynos4*.dts samsung/exynos5*.dts nxp/imx/imx5*.dts nxp/imx/imx6*.dts nxp/imx/imx7*.dts ti/keystone/keystone-*.dts amlogic/meson6-*.dts amlogic/meson8-*.dts amlogic/meson8b-*.dts mediatek/mt76*.dts ti/omap/omap3*.dts ti/omap/omap4*.dts ti/omap/omap5*.dts qcom/qcom-*.dts rockchip/rk3*.dts intel/socfpga/socfpga_*.dts st/ste-*.dts allwinner/sun4i-*.dts allwinner/sun5i-*.dts allwinner/sun6i-*.dts allwinner/sun7i-*.dts allwinner/sun8i-*.dts allwinner/sun9i-*.dts nvidia/tegra20-*.dts nvidia/tegra30-*.dts nvidia/tegra114-*.dts nvidia/tegra124-*.dts arm/vexpress-*.dts nxp/vf/vf500-*.dts nxp/vf/vf610-*.dts xen/xenvm-*.dts xilinx/zynq-*.dts ; do
    target=${dts%*.dts}
    install -m 755 -d %{buildroot}%{dtbdir}/$(dirname $target)
    # install -m 644 COPYING %{buildroot}%{dtbdir}/$(dirname $target)
    install -m 644 $target.dtb %{buildroot}%{dtbdir}/$(dirname $target)
%ifarch %arm aarch64 riscv64
    # HACK: work around U-Boot ignoring vendor dir
    baselink=%{dtbdir}/$(basename $target).dtb
    ln -s $target.dtb %{buildroot}$baselink
%ifarch %arm
    case $dts in
      ti/omap/am335x-*.dts) pkgname=dtb-am335x;;
      ti/omap/am3517*.dts) pkgname=dtb-am3517;;
      ti/omap/am57xx-*.dts) pkgname=dtb-am57xx;;
      marvell/armada-370-*.dts) pkgname=dtb-armada-370;;
      marvell/armada-375-*.dts) pkgname=dtb-armada-375;;
      marvell/armada-385-*.dts) pkgname=dtb-armada-385;;
      marvell/armada-388-*.dts) pkgname=dtb-armada-388;;
      marvell/armada-398-*.dts) pkgname=dtb-armada-398;;
      marvell/armada-xp-*.dts) pkgname=dtb-armada-xp;;
      broadcom/bcm2836*.dts) pkgname=dtb-bcm2836;;
      marvell/dove-*.dts) pkgname=dtb-dove;;
      samsung/exynos4*.dts) pkgname=dtb-exynos4;;
      samsung/exynos5*.dts) pkgname=dtb-exynos5;;
      nxp/imx/imx5*.dts) pkgname=dtb-imx5;;
      nxp/imx/imx6*.dts) pkgname=dtb-imx6;;
      nxp/imx/imx7*.dts) pkgname=dtb-imx7;;
      ti/keystone/keystone-*.dts) pkgname=dtb-keystone;;
      amlogic/meson6-*.dts) pkgname=dtb-meson6;;
      amlogic/meson8-*.dts) pkgname=dtb-meson8;;
      amlogic/meson8b-*.dts) pkgname=dtb-meson8b;;
      mediatek/mt76*.dts) pkgname=dtb-mt76;;
      ti/omap/omap3*.dts) pkgname=dtb-omap3;;
      ti/omap/omap4*.dts) pkgname=dtb-omap4;;
      ti/omap/omap5*.dts) pkgname=dtb-omap5;;
      qcom/qcom-*.dts) pkgname=dtb-qcom;;
      rockchip/rk3*.dts) pkgname=dtb-rk3;;
      intel/socfpga/socfpga_*.dts) pkgname=dtb-socfpga;;
      st/ste-*.dts) pkgname=dtb-ste;;
      allwinner/sun4i-*.dts) pkgname=dtb-sun4i;;
      allwinner/sun5i-*.dts) pkgname=dtb-sun5i;;
      allwinner/sun6i-*.dts) pkgname=dtb-sun6i;;
      allwinner/sun7i-*.dts) pkgname=dtb-sun7i;;
      allwinner/sun8i-*.dts) pkgname=dtb-sun8i;;
      allwinner/sun9i-*.dts) pkgname=dtb-sun9i;;
      nvidia/tegra20-*.dts) pkgname=dtb-tegra2;;
      nvidia/tegra30-*.dts) pkgname=dtb-tegra3;;
      nvidia/tegra114-*.dts) pkgname=dtb-tegra114;;
      nvidia/tegra124-*.dts) pkgname=dtb-tegra124;;
      arm/vexpress-*.dts) pkgname=dtb-vexpress;;
      nxp/vf/vf500-*.dts) pkgname=dtb-vf500;;
      nxp/vf/vf610-*.dts) pkgname=dtb-vf6;;
      xen/xenvm-*.dts) pkgname=dtb-xenvm;;
      xilinx/zynq-*.dts) pkgname=dtb-zynq;;
    esac
    echo $baselink >> ../$pkgname.list
%else
    vendordir=$(basename $(dirname $target))
    echo $baselink >> ../dtb-$vendordir.list
%endif
%endif
done
cd -

%changelog
