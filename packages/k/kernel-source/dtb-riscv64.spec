#
# spec file for package dtb-riscv64
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
%define patchversion 6.0.12
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120300 )
%define dtc_symbols 1
%endif

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,mkspec,compute-PATCHVERSION.sh,arch-symbols,log.sh,try-disable-staging-driver,compress-vmlinux.sh,mkspec-dtb,check-module-license,klp-symbols,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

Name:           dtb-riscv64
Version:        6.0.12
%if 0%{?is_kotd}
Release:        <RELEASE>.g523a283
%else
Release:        0
%endif
Summary:        Device Tree files for $MACHINES
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://www.kernel.org/
ExclusiveArch:  riscv64
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

%package -n dtb-microchip
Summary:        Microchip based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-microchip
Device Tree files for Microchip based riscv64 systems.

%package -n dtb-sifive
Summary:        SiFive based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sifive
Device Tree files for SiFive based riscv64 systems.

%package -n dtb-starfive
Summary:        StarFive based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-starfive
Device Tree files for StarFive based riscv64 systems.



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

cd $source/arch/riscv/boot/dts
for dts in microchip/*.dts sifive/*.dts starfive/*.dts ; do
    target=${dts%*.dts}
    mkdir -p $PPDIR/$(dirname $target)
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $target.dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $target) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

%define dtbdir /boot/dtb-%kernelrelease

%install

cd pp
for dts in microchip/*.dts sifive/*.dts starfive/*.dts ; do
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

%post -n dtb-microchip
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-sifive
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%post -n dtb-starfive
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch aarch64 riscv64
%files -n dtb-microchip -f dtb-microchip.list
%else
%files -n dtb-microchip
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/microchip
%{dtbdir}/microchip/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-sifive -f dtb-sifive.list
%else
%files -n dtb-sifive
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/sifive
%{dtbdir}/sifive/*.dtb

%ifarch aarch64 riscv64
%files -n dtb-starfive -f dtb-starfive.list
%else
%files -n dtb-starfive
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/starfive
%{dtbdir}/starfive/*.dtb

%changelog
