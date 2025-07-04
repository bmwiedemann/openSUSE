#
# spec file for package dtb-riscv64
#
# Copyright (c) 2025 SUSE LLC
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


%define srcversion 6.15
%define patchversion 6.15.4
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,mkspec,compute-PATCHVERSION.sh,arch-symbols,mkspec-dtb,check-module-license,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

Name:           dtb-riscv64
Version:        6.15.4
%if 0%{?is_kotd}
Release:        <RELEASE>.g55e70a8
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
ExclusiveArch:  riscv64

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
Source70:       kernel-obs-build.spec.in
Source71:       kernel-obs-qa.spec.in
Source73:       dtb.spec.in.in
Source74:       mkspec-dtb
Source75:       release-projects
Source76:       check-module-license
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
NoSource:       70
NoSource:       71
NoSource:       73
NoSource:       74
NoSource:       75
NoSource:       76
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

%package -n dtb-allwinner
Summary:        Allwinner based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-allwinner
Device Tree files for Allwinner based riscv64 systems.

%post -n dtb-allwinner
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-allwinner -f dtb-allwinner.list
%else
%files -n dtb-allwinner
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/allwinner
%{dtbdir}/allwinner/*.dtb

%package -n dtb-microchip
Summary:        Microchip based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-microchip
Device Tree files for Microchip based riscv64 systems.

%post -n dtb-microchip
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-microchip -f dtb-microchip.list
%else
%files -n dtb-microchip
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/microchip
%{dtbdir}/microchip/*.dtb

%package -n dtb-renesas
Summary:        Renesas based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-renesas
Device Tree files for Renesas based riscv64 systems.

%post -n dtb-renesas
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-renesas -f dtb-renesas.list
%else
%files -n dtb-renesas
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/renesas
%{dtbdir}/renesas/*.dtb

%package -n dtb-sifive
Summary:        SiFive based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sifive
Device Tree files for SiFive based riscv64 systems.

%post -n dtb-sifive
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sifive -f dtb-sifive.list
%else
%files -n dtb-sifive
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/sifive
%{dtbdir}/sifive/*.dtb

%package -n dtb-sophgo
Summary:        Sophgo based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-sophgo
Device Tree files for Sophgo based riscv64 systems.

%post -n dtb-sophgo
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-sophgo -f dtb-sophgo.list
%else
%files -n dtb-sophgo
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/sophgo
%{dtbdir}/sophgo/*.dtb

%package -n dtb-starfive
Summary:        StarFive based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-starfive
Device Tree files for StarFive based riscv64 systems.

%post -n dtb-starfive
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-starfive -f dtb-starfive.list
%else
%files -n dtb-starfive
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/starfive
%{dtbdir}/starfive/*.dtb

%package -n dtb-thead
Summary:        T-HEAD based riscv64 systems
Group:          System/Boot
Provides:       multiversion(dtb)
Requires(post): coreutils

%description -n dtb-thead
Device Tree files for T-HEAD based riscv64 systems.

%post -n dtb-thead
cd /boot
# If /boot/dtb is a symlink, remove it, so that we can replace it.
[ -d dtb ] && [ -L dtb ] && rm -f dtb
# Unless /boot/dtb exists as real directory, create a symlink.
[ -d dtb ] || ln -sf dtb-%kernelrelease dtb

%ifarch %arm aarch64 riscv64
%files -n dtb-thead -f dtb-thead.list
%else
%files -n dtb-thead
%endif
%defattr(-,root,root)
%ghost /boot/dtb
%dir %{dtbdir}
%dir %{dtbdir}/thead
%{dtbdir}/thead/*.dtb



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

cd $source/arch/riscv/boot/dts
for dts in allwinner/*.dts microchip/*.dts renesas/*.dts sifive/*.dts sophgo/*.dts starfive/*.dts thead/*.dts ; do
    target=${dts%*.dts}
    mkdir -p $PPDIR/$(dirname $target)
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $target.dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $target) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

%install
cd pp
for dts in allwinner/*.dts microchip/*.dts renesas/*.dts sifive/*.dts sophgo/*.dts starfive/*.dts thead/*.dts ; do
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
