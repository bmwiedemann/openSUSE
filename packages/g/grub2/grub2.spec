#
# spec file for package grub2
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
# needssslcertforbuild


%define _binaries_in_noarch_package_terminate_build 0

Name:           grub2
%ifarch x86_64 ppc64
BuildRequires:  gcc-32bit
BuildRequires:  glibc-32bit
BuildRequires:  glibc-devel-32bit
%else
BuildRequires:  gcc
BuildRequires:  glibc-devel
%endif
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  fuse-devel
%if 0%{?suse_version} >= 1140
BuildRequires:  dejavu-fonts
BuildRequires:  gnu-unifont
%endif
BuildRequires:  help2man
BuildRequires:  xz
%if 0%{?suse_version} >= 1210
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif
%if %{defined pythons}
BuildRequires:  %{pythons}
%else
BuildRequires:  python
%endif
BuildRequires:  xz-devel
%ifarch x86_64 aarch64
%if 0%{?suse_version} >= 1230 || 0%{?suse_version} == 1110
BuildRequires:  openssl >= 0.9.8
BuildRequires:  pesign-obs-integration
%endif
%endif
%if 0%{?suse_version} >= 1210
# Package systemd services files grub2-once.service
BuildRequires:  systemd-rpm-macros
%define has_systemd 1
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  update-bootloader-rpm-macros
%endif

# Modules code is dynamically loaded and collected from a _fixed_ path.
%define _libdir %{_exec_prefix}/lib

# Build grub2-emu everywhere (it may be "required" by 'grub2-once')
%define emu 1

%ifarch ppc ppc64 ppc64le
%define grubcpu powerpc
%define platform ieee1275
# emu does not build here yet... :-(
%define emu 0
%endif

%ifarch %{ix86} x86_64
%define grubcpu i386
%define platform pc
%endif

%ifarch s390x
%define grubcpu s390x
%define platform emu
%endif

%ifarch %{arm}
%define grubcpu arm
%define platform uboot
%endif

%ifarch aarch64
%define grubcpu arm64
%define platform efi
%define only_efi 1
%endif

%ifarch riscv64
%define grubcpu riscv64
%define platform efi
%define only_efi 1
%endif

%define grubarch %{grubcpu}-%{platform}

# build efi bootloader on some platforms only:
%if ! 0%{?efi:1}
%global efi %{ix86} x86_64 ia64 aarch64 %{arm} riscv64
%endif

%ifarch %{efi}
%ifarch %{ix86}
%define grubefiarch i386-efi
%else
%ifarch aarch64
%define grubefiarch arm64-efi
%else
%ifarch %{arm}
%define grubefiarch arm-efi
%else
%define grubefiarch %{_target_cpu}-efi
%endif
%endif
%endif
%endif

%ifarch %{ix86}
%define grubxenarch i386-xen
%endif

%ifarch x86_64
%define grubxenarch x86_64-xen
%endif

%if "%{platform}" == "emu"
# force %%{emu} to 1, e.g. for s390
%define emu 1
%endif

%if 0%{?suse_version} == 1110
%define only_efi %{nil}
%define only_x86_64 %{nil}
%endif

Version:        2.04
Release:        0
Summary:        Bootloader with support for Linux, Multiboot and more
License:        GPL-3.0-or-later
Group:          System/Boot
URL:            http://www.gnu.org/software/grub/
Source0:        https://ftp.gnu.org/gnu/grub/grub-%{version}.tar.xz
Source1:        90_persistent
Source2:        grub.default
Source4:        grub2.rpmlintrc
Source6:        grub2-once
Source7:        20_memtest86+
Source8:        README.ibm3215
Source10:       openSUSE-UEFI-CA-Certificate.crt
Source11:       SLES-UEFI-CA-Certificate.crt
Source12:       grub2-snapper-plugin.sh
Source14:       80_suse_btrfs_snapshot
Source15:       grub2-once.service
Source16:       grub2-xen-pv-firmware.cfg
# required hook for systemd-sleep (bsc#941758)
Source17:       grub2-systemd-sleep.sh
Source18:       grub2-check-default.sh
Source1000:     PATCH_POLICY
Patch1:         rename-grub-info-file-to-grub2.patch
Patch2:         grub2-linux.patch
Patch3:         use-grub2-as-a-package-name.patch
Patch4:         info-dir-entry.patch
Patch6:         grub2-iterate-and-hook-for-extended-partition.patch
Patch8:         grub2-ppc-terminfo.patch
Patch9:         grub2-GRUB_CMDLINE_LINUX_RECOVERY-for-recovery-mode.patch
Patch10:        grub2-fix-error-terminal-gfxterm-isn-t-found.patch
Patch12:        grub2-fix-menu-in-xen-host-server.patch
Patch15:        not-display-menu-when-boot-once.patch
Patch17:        grub2-pass-corret-root-for-nfsroot.patch
Patch19:        grub2-efi-HP-workaround.patch
Patch21:        grub2-secureboot-add-linuxefi.patch
Patch22:        grub2-secureboot-use-linuxefi-on-uefi.patch
Patch23:        grub2-secureboot-no-insmod-on-sb.patch
Patch24:        grub2-secureboot-provide-linuxefi-config.patch
Patch25:        grub2-secureboot-chainloader.patch
Patch26:        grub2-secureboot-use-linuxefi-on-uefi-in-os-prober.patch
Patch27:        grub2-linuxefi-fix-boot-params.patch
Patch35:        grub2-linguas.sh-no-rsync.patch
Patch37:        grub2-use-Unifont-for-starfield-theme-terminal.patch
Patch38:        grub2-s390x-01-Changes-made-and-files-added-in-order-to-allow-s390x.patch
Patch39:        grub2-s390x-02-kexec-module-added-to-emu.patch
Patch40:        grub2-s390x-03-output-7-bit-ascii.patch
Patch41:        grub2-s390x-04-grub2-install.patch
Patch42:        grub2-s390x-05-grub2-mkconfig.patch
Patch43:        grub2-use-rpmsort-for-version-sorting.patch
Patch53:        grub2-getroot-treat-mdadm-ddf-as-simple-device.patch
Patch56:        grub2-setup-try-fs-embed-if-mbr-gap-too-small.patch
Patch58:        grub2-xen-linux16.patch
Patch59:        grub2-efi-disable-video-cirrus-and-bochus.patch
Patch60:        grub2-editenv-add-warning-message.patch
Patch61:        grub2-vbe-blacklist-preferred-1440x900x32.patch
Patch64:        grub2-grubenv-in-btrfs-header.patch
Patch65:        grub2-mkconfig-aarch64.patch
Patch70:        grub2-default-distributor.patch
Patch71:        grub2-menu-unrestricted.patch
Patch72:        grub2-mkconfig-arm.patch
Patch75:        grub2-s390x-06-loadparm.patch
Patch76:        grub2-s390x-07-add-image-param-for-zipl-setup.patch
Patch77:        grub2-s390x-08-workaround-part-to-disk.patch
Patch78:        grub2-commands-introduce-read_file-subcommand.patch
Patch79:        grub2-efi-chainload-harder.patch
Patch80:        grub2-emu-4-all.patch
Patch81:        grub2-lvm-allocate-metadata-buffer-from-raw-contents.patch
Patch82:        grub2-diskfilter-support-pv-without-metadatacopies.patch
Patch83:        grub2-efi-uga-64bit-fb.patch
Patch84:        grub2-s390x-09-improve-zipl-setup.patch
Patch85:        grub2-getroot-scan-disk-pv.patch
Patch92:        grub2-util-30_os-prober-multiple-initrd.patch
Patch93:        grub2-getroot-support-nvdimm.patch
Patch94:        grub2-install-fix-not-a-directory-error.patch
Patch95:        grub2-verifiers-fix-system-freeze-if-verify-failed.patch
Patch96:        grub-install-force-journal-draining-to-ensure-data-i.patch
Patch97:        grub2-s390x-skip-zfcpdump-image.patch
# Btrfs snapshot booting related patches
Patch101:       grub2-btrfs-01-add-ability-to-boot-from-subvolumes.patch
Patch102:       grub2-btrfs-02-export-subvolume-envvars.patch
Patch103:       grub2-btrfs-03-follow_default.patch
Patch104:       grub2-btrfs-04-grub2-install.patch
Patch105:       grub2-btrfs-05-grub2-mkconfig.patch
Patch106:       grub2-btrfs-06-subvol-mount.patch
Patch107:       grub2-btrfs-07-subvol-fallback.patch
Patch108:       grub2-btrfs-08-workaround-snapshot-menu-default-entry.patch
Patch109:       grub2-btrfs-09-get-default-subvolume.patch
Patch110:       grub2-btrfs-10-config-directory.patch
Patch111:       0001-btrfs-disable-zstd-support-for-i386-pc.patch
# Support EFI xen loader
Patch120:       grub2-efi-xen-chainload.patch
Patch121:       grub2-efi-chainloader-root.patch
Patch122:       grub2-efi-xen-cmdline.patch
Patch123:       grub2-efi-xen-cfg-unquote.patch
Patch124:       grub2-efi-xen-removable.patch
# Hidden menu entry and hotkey "t" for text console
Patch140:       grub2-Add-hidden-menu-entries.patch
Patch141:       grub2-SUSE-Add-the-t-hotkey.patch
# Linux root device related patches
Patch163:       grub2-zipl-setup-fix-btrfs-multipledev.patch
Patch164:       grub2-suse-remove-linux-root-param.patch
# PPC64 LE support
Patch205:       grub2-ppc64le-disable-video.patch
Patch207:       grub2-ppc64le-memory-map.patch
# PPC 
Patch211:       grub2-ppc64-cas-reboot-support.patch
Patch212:       grub2-install-remove-useless-check-PReP-partition-is-empty.patch
Patch213:       grub2-Fix-incorrect-netmask-on-ppc64.patch
Patch215:       grub2-ppc64-cas-new-scope.patch
Patch218:       grub2-ppc64-cas-fix-double-free.patch
Patch233:       grub2-use-stat-instead-of-udevadm-for-partition-lookup.patch
Patch234:       fix-grub2-use-stat-instead-of-udevadm-for-partition-lookup-with-new-glibc.patch
Patch236:       grub2-efi_gop-avoid-low-resolution.patch
# Support HTTP Boot IPv4 and IPv6 (fate#320129)
Patch281:       0002-net-read-bracketed-ipv6-addrs-and-port-numbers.patch
Patch282:       0003-bootp-New-net_bootp6-command.patch
Patch283:       0004-efinet-UEFI-IPv6-PXE-support.patch
Patch284:       0005-grub.texi-Add-net_bootp6-doument.patch
Patch285:       0006-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch286:       0007-efinet-Setting-network-from-UEFI-device-path.patch
Patch287:       0008-efinet-Setting-DNS-server-from-UEFI-protocol.patch
# Fix GOP BLT support (FATE#322332)
Patch311:       grub2-efi-gop-add-blt.patch
# TPM Support (FATE#315831)
Patch411:       0012-tpm-Build-tpm-as-module.patch
# UEFI HTTP and related network protocol support (FATE#320130)
Patch420:       0001-add-support-for-UEFI-network-protocols.patch
Patch421:       0002-AUDIT-0-http-boot-tracker-bug.patch
# check if default entry need to be corrected for updated distributor version 
# and/or use fallback entry if default kernel entry removed (bsc#1065349)
Patch430:       grub2-mkconfig-default-entry-correction.patch
Patch431:       grub2-s390x-10-keep-network-at-kexec.patch
Patch432:       grub2-s390x-11-secureboot.patch
# Support for UEFI Secure Boot on AArch64 (FATE#326541)
Patch450:       grub2-secureboot-install-signed-grub.patch
Patch501:       grub2-btrfs-help-on-snapper-rollback.patch
# Improved hiDPI device support (FATE#326680)
Patch510:       grub2-video-limit-the-resolution-for-fixed-bimap-font.patch
# Support long menuentries (FATE#325760)
Patch511:       grub2-gfxmenu-support-scrolling-menu-entry-s-text.patch
# RISC-V fixes
Patch601:       risc-v-fix-computation-of-pc-relative-relocation-offset.patch
Patch602:       risc-v-add-clzdi2-symbol.patch
Patch603:       grub-install-define-default-platform-for-risc-v.patch
# Fix gcc-10 build fail
Patch610:       0001-mdraid1x_linux-Fix-gcc10-error-Werror-array-bounds.patch
Patch611:       0002-zfs-Fix-gcc10-error-Werror-zero-length-bounds.patch
# bsc#1166409 - Grub netbooting does not search for grub.cfg files with mac
# address or ip address in filename
Patch700:       0001-normal-Move-common-datetime-functions-out-of-the-nor.patch
Patch701:       0002-kern-Add-X-option-to-printf-functions.patch
Patch702:       0003-normal-main-Search-for-specific-config-files-for-net.patch
Patch703:       0004-datetime-Enable-the-datetime-module-for-the-emu-plat.patch
# bsc#1168994 VUL-0: EMBARGOED: CVE-2020-10713: grub2: parsing overflows can
# bypass secure boot restrictions
Patch704:       0001-yylex-Make-lexer-fatal-errors-actually-be-fatal.patch
# bsc#1173812 VUL-0: EMBARGOED: CVE-2020-14308, CVE-2020-14309, CVE-2020-14310,
# CVE-2020-14311: grub2: avoid integer overflows
Patch705:       0002-safemath-Add-some-arithmetic-primitives-that-check-f.patch
Patch706:       0003-calloc-Make-sure-we-always-have-an-overflow-checking.patch
Patch707:       0004-calloc-Use-calloc-at-most-places.patch
Patch708:       0005-malloc-Use-overflow-checking-primitives-where-we-do-.patch
Patch709:       0006-iso9660-Don-t-leak-memory-on-realloc-failures.patch
Patch710:       0007-font-Do-not-load-more-than-one-NAME-section.patch
# bsc#1174463 VUL-0: EMBARGOED: CVE-2020-15706: grub2: script: Avoid a
# use-after-free when redefining a function during execution
Patch711:       0008-script-Remove-unused-fields-from-grub_script_functio.patch
Patch712:       0009-script-Avoid-a-use-after-free-when-redefining-a-func.patch
# bsc#1174570 VUL-0: EMBARGOED: CVE-2020-15707: grub2: linux: Fix integer
# overflows in initrd size handling
Patch713:       0010-linux-Fix-integer-overflows-in-initrd-size-handling.patch
Patch714:       0001-kern-mm.c-Make-grub_calloc-inline.patch
# bsc#1174421 VUL-0: CVE-2020-15705: grub2: linuxefi: fail kernel validation
# without shim protocol
Patch715:       0001-linuxefi-fail-kernel-validation-without-shim-protoco.patch
Patch716:       0002-cmdline-Provide-cmdline-functions-as-module.patch
# bsc#1172745 L3: SLES 12 SP4 - Slow boot of system after updated kernel -
# takes 45 minutes after grub to start loading kernel
Patch717:       0001-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch718:       0002-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch719:       0001-Unify-the-check-to-enable-btrfs-relative-path.patch
Patch720:       0001-shim_lock-Disable-GRUB_VERIFY_FLAGS_DEFER_AUTH-if-se.patch
Patch721:       0001-efi-linux-provide-linux-command.patch
# Improve the error handling when grub2-install fails with short mbr gap
# (bsc#1176062)
Patch722:       0001-Warn-if-MBR-gap-is-small-and-user-uses-advanced-modu.patch
Patch723:       0002-grub-install-Avoid-incompleted-install-on-i386-pc.patch

Requires:       gettext-runtime
%if 0%{?suse_version} >= 1140
%ifnarch s390x
Recommends:     os-prober
%endif
# xorriso not available using grub2-mkrescue (bnc#812681)
# downgrade to suggest as minimal system can't afford pulling in tcl/tk and half of the x11 stack (bsc#1102515)
Suggests:       libburnia-tools
Suggests:       mtools
%endif
%if ! 0%{?only_efi:1}
Requires:       grub2-%{grubarch} = %{version}-%{release}
%endif
%ifarch s390x
# required utilities by grub2-s390x-04-grub2-install.patch
# use 'showconsole' to determine console device. (bnc#876743)
Requires:       /sbin/showconsole
Requires:       kexec-tools
# for /sbin/zipl used by grub2-zipl-setup
Requires:       s390-tools
%endif
%ifarch ppc64 ppc64le
Requires:       powerpc-utils
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?only_x86_64:1}
ExclusiveArch:  x86_64
%else
ExclusiveArch:  %{ix86} x86_64 ppc ppc64 ppc64le s390x aarch64 %{arm} riscv64
%endif

%description
This is the second version of the GRUB (Grand Unified Bootloader), a
highly configurable and customizable bootloader with modular
architecture.  It support rich scale of kernel formats, file systems,
computer architectures and hardware devices.

This package includes user space utlities to manage GRUB on your system.


Authors:
--------
    Gordon Matzigkeit
    Yoshinori K. Okuji
    Colin Watson
    Colin D. Bennett
    Vesa Jääskeläinen
    Robert Millan
    Carles Pina

%package branding-upstream

Summary:        Upstream branding for GRUB2's graphical console
Group:          System/Fhs
Requires:       %{name} = %{version}

%description branding-upstream
Upstream branding for GRUB2's graphical console

%if ! 0%{?only_efi:1}
%package %{grubarch}

Summary:        Bootloader with support for Linux, Multiboot and more
Group:          System/Boot
%if "%{platform}" != "emu"
BuildArch:      noarch
%endif
Requires:       %{name} = %{version}
Requires(post):	%{name} = %{version}
%if 0%{?update_bootloader_requires:1}
%update_bootloader_requires
%else
Requires:       perl-Bootloader
Requires(post): perl-Bootloader
%endif

%description %{grubarch}
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It supports rich variety of kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for %{platform} systems.

%package %{grubarch}-debug
Summary:        Debug symbols for %{grubarch}
Group:          System/Boot
%if "%{platform}" != "emu"
BuildArch:      noarch
%endif
Requires:       %{name}-%{grubarch} = %{version}

%description %{grubarch}-debug
Debug information for %{name}-%{grubarch}

Information on how to debug grub can be found online:
https://www.cnblogs.com/coryxie/archive/2013/03/12/2956807.html

%endif

%ifarch %{efi}

%package %{grubefiarch}

Summary:        Bootloader with support for Linux, Multiboot and more
Group:          System/Boot
BuildArch:      noarch
# Require efibootmgr
# Without it grub-install is broken so break the package as well if unavailable
Requires:       efibootmgr
Requires(post): efibootmgr
Requires:       %{name} = %{version}
Requires(post):	%{name} = %{version}
%if 0%{?update_bootloader_requires:1}
%update_bootloader_requires
%else
Requires:       perl-Bootloader >= 0.706
Requires(post): perl-Bootloader >= 0.706
%endif
Provides:       %{name}-efi = %{version}-%{release}
Obsoletes:      %{name}-efi < %{version}-%{release}

%description %{grubefiarch}
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It supports rich variety of kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for EFI systems.

%package %{grubefiarch}-debug
Summary:        Debug symbols for %{grubefiarch}
Group:          System/Boot
%if "%{platform}" != "emu"
BuildArch:      noarch
%endif
Requires:       %{name}-%{grubefiarch} = %{version}

%description %{grubefiarch}-debug
Debug symbols for %{name}-%{grubefiarch}

Information on how to debug grub can be found online:
https://www.cnblogs.com/coryxie/archive/2013/03/12/2956807.html

%endif

%ifarch %{ix86} x86_64

%package %{grubxenarch}

Summary:        Bootloader with support for Linux, Multiboot and more
Group:          System/Boot
Provides:       %{name}-xen = %{version}-%{release}
Obsoletes:      %{name}-xen < %{version}-%{release}
BuildArch:      noarch

%description %{grubxenarch}
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It supports rich variety of kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for XEN systems.

%endif

%package snapper-plugin

Summary:        Grub2's snapper plugin
Group:          System/Fhs
Requires:       %{name} = %{version}
Requires:       libxml2-tools
Supplements:    packageand(snapper:grub2)
BuildArch:      noarch

%description snapper-plugin
Grub2's snapper plugin for advanced btrfs snapshot boot menu management

%if 0%{?has_systemd:1}
%package systemd-sleep-plugin

Summary:        Grub2's systemd-sleep plugin
Group:          System/Fhs
Requires:       grub2
Requires:       util-linux
Supplements:    packageand(systemd:grub2)
BuildArch:      noarch

%description systemd-sleep-plugin
Grub2's systemd-sleep plugin for directly booting hibernated kernel image in
swap partition while in resuming
%endif

%prep
# We create (if we build for efi) two copies of the sources in the Builddir
%setup -q -n grub-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch15 -p1
%patch17 -p1
%patch19 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch35 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch53 -p1
%patch56 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch64 -p1
%patch65 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch140 -p1
%patch141 -p1
%patch163 -p1
%patch164 -p1
%patch205 -p1
%patch207 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch215 -p1
%patch218 -p1
%patch233 -p1
%patch234 -p1
%patch236 -p1
%patch281 -p1
%patch282 -p1
%patch283 -p1
%patch284 -p1
%patch285 -p1
%patch286 -p1
%patch287 -p1
%patch311 -p1
%patch411 -p1
%patch420 -p1
%patch421 -p1
%patch430 -p1
%patch431 -p1
%patch432 -p1
%patch450 -p1
%patch501 -p1
%patch510 -p1
%patch511 -p1
%patch601 -p1
%patch602 -p1
%patch603 -p1
%patch610 -p1
%patch611 -p1
%patch700 -p1
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1
%patch705 -p1
%patch706 -p1
%patch707 -p1
%patch708 -p1
%patch709 -p1
%patch710 -p1
%patch711 -p1
%patch712 -p1
%patch713 -p1
%patch714 -p1
%patch715 -p1
%patch716 -p1
%patch717 -p1
%patch718 -p1
%patch719 -p1
%patch720 -p1
%patch721 -p1
%patch722 -p1
%patch723 -p1

%build
# collect evidence to debug spurious build failure on SLE15
ulimit -a
# patches above may update the timestamp of grub.texi
# and via build-aux/mdate-sh they end up in grub2.info, breaking build-compare
[ -z "$SOURCE_DATE_EPOCH" ] ||\
  [ `stat -c %Y docs/grub.texi` -lt $SOURCE_DATE_EPOCH ] ||\
  touch -d@$SOURCE_DATE_EPOCH docs/grub.texi

# This simplifies patch handling without need to use git to create patch
# that renames file
mv docs/grub.texi docs/grub2.texi

cp %{SOURCE8} .
mkdir build
%ifarch %{efi}
mkdir build-efi
%endif
%ifarch %{ix86} x86_64
mkdir build-xen
%endif
%if %{emu}
mkdir build-emu
%endif

export PYTHON=%{_bindir}/python3
[ -x $PYTHON ] || unset PYTHON   # try 'python', if 'python3' is unavailable
# autogen calls autoreconf -vi
./autogen.sh
# Not yet:
%define common_conf_options TARGET_LDFLAGS=-static --program-transform-name=s,grub,%{name},
# This does NOT work on SLE11:
%define _configure ../configure

# We don't want to let rpm override *FLAGS with default a.k.a bogus values.
CFLAGS="-fno-strict-aliasing -fno-inline-functions-called-once "
CXXFLAGS=" "
FFLAGS=" "
export CFLAGS CXXFLAGS FFLAGS

%if %{emu}
cd build-emu
%define arch_specific --enable-device-mapper --disable-grub-mount
TLFLAGS="-fPIC"

# -static is needed so that autoconf script is able to link
# test that looks for _start symbol on 64 bit platforms
../configure TARGET_LDFLAGS=$TLFLAGS	\
	--prefix=%{_prefix}		\
	--libdir=%{_datadir}		\
	--sysconfdir=%{_sysconfdir}	\
        --target=%{_target_platform}    \
        --with-platform=emu     \
	%{arch_specific}                \
        --program-transform-name=s,grub,%{name},
make %{?_smp_mflags}
cd ..
if [ "%{platform}" = "emu" ]; then
  rmdir build
  mv build-emu build
fi
%endif

%ifarch %{ix86} x86_64
cd build-xen
../configure                           \
        TARGET_LDFLAGS=-static         \
        --prefix=%{_prefix}            \
        --libdir=%{_datadir}           \
        --sysconfdir=%{_sysconfdir}    \
        --target=%{_target_platform}   \
        --with-platform=xen            \
        --program-transform-name=s,grub,%{name},
make %{?_smp_mflags}

./grub-mkstandalone --grub-mkimage=./grub-mkimage -o grub.xen -O %{grubxenarch} -d grub-core/ "/boot/grub/grub.cfg=%{SOURCE16}"

cd ..
%endif

%ifarch %{efi}
cd build-efi
../configure   				                \
        TARGET_LDFLAGS=-static                          \
	--prefix=%{_prefix}				\
	--libdir=%{_datadir}				\
	--sysconfdir=%{_sysconfdir}			\
        --target=%{_target_platform}                    \
        --with-platform=efi                             \
        --program-transform-name=s,grub,%{name},
make %{?_smp_mflags}

#TODO: add efifwsetup module

FS_MODULES="btrfs ext2 xfs jfs reiserfs"
CD_MODULES=" all_video boot cat chain configfile echo true \
		efinet font gfxmenu gfxterm gzio halt iso9660 \
		jpeg minicmd normal part_apple part_msdos part_gpt \
		password_pbkdf2 png reboot search search_fs_uuid \
		search_fs_file search_label sleep test video fat loadenv"
PXE_MODULES="efinet tftp http"
CRYPTO_MODULES="luks gcry_rijndael gcry_sha1 gcry_sha256"

%ifarch x86_64
CD_MODULES="${CD_MODULES} shim_lock linuxefi" 
%else
CD_MODULES="${CD_MODULES} linux" 
%endif

GRUB_MODULES="${CD_MODULES} ${FS_MODULES} ${PXE_MODULES} ${CRYPTO_MODULES} mdraid09 mdraid1x lvm serial"
./grub-mkimage -O %{grubefiarch} -o grub.efi --prefix= \
		-d grub-core ${GRUB_MODULES}
%ifarch x86_64
./grub-mkimage -O %{grubefiarch} -o grub-tpm.efi --prefix= \
		-d grub-core ${GRUB_MODULES} tpm
%endif

%ifarch x86_64 aarch64
%if 0%{?suse_version} >= 1230 || 0%{?suse_version} == 1110
if test -e %{_sourcedir}/_projectcert.crt ; then
    prjsubject=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -noout -subject_hash)
    prjissuer=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -noout -issuer_hash)
    opensusesubject=$(openssl x509 -in %{SOURCE10} -noout -subject_hash)
    slessubject=$(openssl x509 -in %{SOURCE11} -noout -subject_hash)
    if test "$prjissuer" = "$opensusesubject" ; then
        cert=%{SOURCE10}
    fi
    if test "$prjissuer" = "$slessubject" ; then
        cert=%{SOURCE11}
    fi
    if test "$prjsubject" = "$prjissuer" ; then
        cert=%{_sourcedir}/_projectcert.crt
    fi
fi
if test -z "$cert" ; then
    echo "cannot identify project, assuming openSUSE signing"
    cert=%{SOURCE10}
fi

openssl x509 -in $cert -outform DER -out grub.der
%endif
%endif

cd ..
%endif

%if ! 0%{?only_efi:1}
cd build

# 64-bit x86-64 machines use 32-bit boot loader
# (We cannot just redefine _target_cpu, as we'd get i386.rpm packages then)
%ifarch x86_64 
%define _target_platform i386-%{_vendor}-%{_target_os}%{?_gnu}
%endif

%if "%{platform}" != "emu"
%define arch_specific --enable-device-mapper
TLFLAGS="-static"

# -static is needed so that autoconf script is able to link
# test that looks for _start symbol on 64 bit platforms
../configure TARGET_LDFLAGS="$TLFLAGS"	\
	--prefix=%{_prefix}		\
	--libdir=%{_datadir}		\
	--sysconfdir=%{_sysconfdir}	\
        --target=%{_target_platform}    \
        --with-platform=%{platform}     \
	%{arch_specific}                \
        --program-transform-name=s,grub,%{name},
make %{?_smp_mflags}
%endif
cd ..
%endif

%install

%ifarch %{ix86} x86_64
cd build-xen
%make_install
install -m 644 grub.xen %{buildroot}/%{_datadir}/%{name}/%{grubxenarch}/.
# provide compatibility sym-link for VM definitions pointing to old location
install -d %{buildroot}%{_libdir}/%{name}/%{grubxenarch}
ln -srf %{buildroot}%{_datadir}/%{name}/%{grubxenarch}/grub.xen %{buildroot}%{_libdir}/%{name}/%{grubxenarch}/grub.xen
cat <<-EoM >%{buildroot}%{_libdir}/%{name}/%{grubxenarch}/DEPRECATED
	This directory and its contents was moved to %{_datadir}/%{name}/%{grubxenarch}.
	Individual symbolic links are provided for a smooth transition.
	Please update your VM definition files to use the new location!
EoM
cd ..
%endif

%ifarch %{efi}
cd build-efi
%make_install
install -m 644 grub.efi %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/.
%ifarch x86_64
install -m 644 grub-tpm.efi %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/.
%endif

# Create grub.efi link to system efi directory
# This is for tools like kiwi not fiddling with the path
%define sysefibasedir %{_datadir}/efi
%define sysefidir %{sysefibasedir}/%{_target_cpu} 
install -d %{buildroot}/%{sysefidir}
ln -sr %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/grub.efi %{buildroot}%{sysefidir}/grub.efi
%ifarch x86_64
# provide compatibility sym-link for previous shim-install and the like
install -d %{buildroot}/usr/lib64/efi
ln -srf %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/grub.efi %{buildroot}/usr/lib64/efi/grub.efi
cat <<-EoM >%{buildroot}/usr/lib64/efi/DEPRECATED
	This directory and its contents was moved to %{_datadir}/efi/x86_64.
	Individual symbolic links are provided for a smooth transition and
	may vanish at any point in time.  Please use the new location!
EoM
%endif

%ifarch x86_64 aarch64
%if 0%{?suse_version} >= 1230 || 0%{?suse_version} == 1110
export BRP_PESIGN_FILES="%{_datadir}/%{name}/%{grubefiarch}/grub.efi"
%ifarch x86_64
BRP_PESIGN_FILES="${BRP_PESIGN_FILES} %{_datadir}/%{name}/%{grubefiarch}/grub-tpm.efi"
%endif
install -m 444 grub.der %{buildroot}/%{sysefidir}/
%endif
%endif

cd ..
%endif

%if ! 0%{?only_efi:1}
cd build
%make_install
cd ..
%endif

if [ "%{platform}" = "emu" ]; then
  # emu-lite is currently broken (and not needed), don't install!
  rm -f %{buildroot}/%{_bindir}/%{name}-emu-lite
elif [ -d build-emu/grub-core ]; then
  cd build-emu/grub-core
  install -m 755 grub-emu %{buildroot}/%{_bindir}/%{name}-emu
  if false; then
    # this needs to go to '-emu'-package; until that is ready, don't install!
    install -m 755 grub-emu-lite %{buildroot}/%{_bindir}/%{name}-emu-lite
  else
    rm -f %{buildroot}/%{_bindir}/%{name}-emu-lite
  fi
  install -m 644 grub-emu.1 %{buildroot}/%{_mandir}/man1/%{name}-emu.1
  cd ../..
fi

# *.module files are installed with executable bits due to the way grub2 build
# system works. Clear executable bits to not confuse find-debuginfo.sh
find %{buildroot}/%{_datadir}/%{name} \
       \( -name '*.module' -o -name '*.image' -o -name '*.exec' \) -print0 | \
       xargs --no-run-if-empty -0 chmod a-x

# Script that makes part of grub.cfg persist across updates
install -m 755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/grub.d/

# Script to generate memtest86+ menu entry
install -m 755 %{SOURCE7} %{buildroot}/%{_sysconfdir}/grub.d/

# Ghost config file
install -d %{buildroot}/boot/%{name}
touch %{buildroot}/boot/%{name}/grub.cfg

# Remove devel files
rm %{buildroot}/%{_datadir}/%{name}/*/*.h
%if 0%{?suse_version} >= 1140
rm %{buildroot}/%{_datadir}/%{name}/*.h
%endif

# Defaults
install -m 644 -D %{SOURCE2} %{buildroot}/%{_sysconfdir}/default/grub
install -m 755 -D %{SOURCE6} %{buildroot}/%{_sbindir}/grub2-once
install -m 755 -D %{SOURCE12} %{buildroot}/%{_libdir}/snapper/plugins/grub
install -m 755 -D %{SOURCE14} %{buildroot}/%{_sysconfdir}/grub.d/80_suse_btrfs_snapshot
%if 0%{?has_systemd:1}
install -m 644 -D %{SOURCE15} %{buildroot}/%{_unitdir}/grub2-once.service
install -m 755 -D %{SOURCE17} %{buildroot}/%{_libdir}/systemd/system-sleep/grub2.sleep
%endif
install -m 755 -D %{SOURCE18} %{buildroot}/%{_sbindir}/grub2-check-default

R="%{buildroot}"
%ifarch %{ix86} x86_64
%else
rm -f $R%{_sysconfdir}/grub.d/20_memtest86+
%endif

%ifarch ppc ppc64 ppc64le
rm -f $R%{_sysconfdir}/grub.d/95_textmode
%else
rm -f $R%{_sysconfdir}/grub.d/20_ppc_terminfo
%endif

%ifarch s390x
mv $R%{_sysconfdir}/{grub.d,default}/zipl2grub.conf.in
chmod 600 $R%{_sysconfdir}/default/zipl2grub.conf.in

%define dracutlibdir %{_prefix}/lib/dracut
%define dracutgrubmoddir %{dracutlibdir}/modules.d/99grub2
install -m 755 -d $R%{dracutgrubmoddir}
for f in module-setup.sh grub2.sh; do
  mv $R%{_datadir}/%{name}/%{grubarch}/dracut-$f $R%{dracutgrubmoddir}/$f
done
mv $R%{_datadir}/%{name}/%{grubarch}/dracut-zipl-refresh \
   $R%{_datadir}/%{name}/zipl-refresh
rm -f $R%{_sysconfdir}/grub.d/30_os-prober

perl -ni -e '
  sub END() {
    print "\n# on s390x always:\nGRUB_DISABLE_OS_PROBER=true\n";
  }
  if ( s{^#?(GRUB_TERMINAL)=(console|gfxterm)}{$1=console} ) {
    $_ .= "GRUB_GFXPAYLOAD_LINUX=text\n";
  }
  if (	m{^# The resolution used on graphical} ||
	m{^# # note that you can use only modes} ||
	m{^# you can see them in real GRUB} ||
	m{^#?GRUB_GFXMODE=} ) {
    next;
  }
  s{openSUSE}{SUSE Linux Enterprise Server} if (m{^GRUB_DISTRIBUTOR});
  print;
'  %{buildroot}/%{_sysconfdir}/default/grub
%else
%endif

%find_lang %{name}
%fdupes %buildroot%{_bindir}
%fdupes %buildroot%{_libdir}
%fdupes %buildroot%{_datadir}

%pre
%service_add_pre grub2-once.service

%post
%service_add_post grub2-once.service

%if ! 0%{?only_efi:1}

%post %{grubarch}
%if 0%{?update_bootloader_check_type_reinit_post:1} 
%update_bootloader_check_type_reinit_post grub2
%else
# To check by current loader settings
if [ -f %{_sysconfdir}/sysconfig/bootloader ]; then
  . %{_sysconfdir}/sysconfig/bootloader
fi

# If the grub is the current loader, we'll handle the grub2 testing entry
if [ "x${LOADER_TYPE}" = "xgrub" ]; then

  exec >/dev/null 2>&1

  # check if entry for grub2's core.img exists in the config
  # if yes, we will correct obsoleted path and update grub2 stuff and config to make it work
  # if no, do nothing
  if [ -f /boot/grub/menu.lst ]; then

    # If grub config contains obsolete core.img path, remove and use the new one
    if /usr/bin/grep -l "^\s*kernel\s*.*/boot/%{name}/core.img" /boot/grub/menu.lst; then
      /sbin/update-bootloader --remove --image /boot/%{name}/core.img || true
      /sbin/update-bootloader --add --image /boot/%{name}/i386-pc/core.img --name "GNU GRUB 2" || true
    fi

    # Install grub2 stuff and config to make the grub2 testing entry to work with updated version
    if /usr/bin/grep -l "^\s*kernel\s*.*/boot/%{name}/i386-pc/core.img" /boot/grub/menu.lst; then
      # Determine the partition with /boot
      BOOT_PARTITION=$(df -h /boot | sed -n '2s/[[:blank:]].*//p')
      # Generate core.img, but don't let it be installed in boot sector
      %{name}-install --no-bootsector $BOOT_PARTITION || true
      # Create a working grub2 config, otherwise that entry is un-bootable
      /usr/sbin/grub2-mkconfig -o /boot/%{name}/grub.cfg
    fi
  fi

elif [ "x${LOADER_TYPE}" = "xgrub2" ]; then

  # It's enought to call update-bootloader to install grub2 and update it's config
  # Use new --reinit, if not available use --refresh
  # --reinit: install and update bootloader config
  # --refresh: update bootloader config
  /sbin/update-bootloader --reinit 2>&1 | grep -q 'Unknown option: reinit' &&
  /sbin/update-bootloader --refresh || true
fi
%endif

%posttrans %{grubarch}
%{?update_bootloader_posttrans}

%endif

%ifarch %{efi}

%post %{grubefiarch}
%if 0%{?update_bootloader_check_type_reinit_post:1} 
%update_bootloader_check_type_reinit_post grub2-efi
%else
# To check by current loader settings
if [ -f %{_sysconfdir}/sysconfig/bootloader ]; then
  . %{_sysconfdir}/sysconfig/bootloader
fi

if [ "x${LOADER_TYPE}" = "xgrub2-efi" ]; then

  if [ -d /boot/%{name}-efi ]; then
    # Migrate settings to standard prefix /boot/grub2
    for i in custom.cfg grubenv; do
      [ -f /boot/%{name}-efi/$i ] && cp -a /boot/%{name}-efi/$i /boot/%{name} || :
    done

  fi

  # It's enough to call update-bootloader to install grub2 and update it's config
  # Use new --reinit, if not available use --refresh
  # --reinit: install and update bootloader config
  # --refresh: update bootloader config
  /sbin/update-bootloader --reinit 2>&1 | grep -q 'Unknown option: reinit' &&
  /sbin/update-bootloader --refresh || true
fi

if [ -d /boot/%{name}-efi ]; then
  mv /boot/%{name}-efi /boot/%{name}-efi.rpmsave
fi

exit 0
%endif

%posttrans %{grubefiarch}
%{?update_bootloader_posttrans}

%endif

%preun
%service_del_preun grub2-once.service
# We did not add core.img to grub1 menu.lst in new update-bootloader macro as what
# the old %%post ever did, then the %%preun counterpart which removed the added core.img
# entry from old %%post can be skipped entirely if having new macro in use.
%if ! 0%{?update_bootloader_posttrans:1}%{?only_efi:1}
if [ $1 = 0 ]; then
  # To check by current loader settings
  if [ -f %{_sysconfdir}/sysconfig/bootloader ]; then
    . %{_sysconfdir}/sysconfig/bootloader
  fi

  if [ "x${LOADER_TYPE}" = "xgrub" ]; then

    exec >/dev/null 2>&1

    if [ -f /boot/grub/menu.lst ]; then

      # Remove grub2 testing entry in menu.lst if has any
      for i in /boot/%{name}/core.img /boot/%{name}/i386-pc/core.img; do
        if /usr/bin/grep -l "^\s*kernel\s*.*$i" /boot/grub/menu.lst; then
          /sbin/update-bootloader --remove --image "$i" || true
        fi
      done
    fi

    # Cleanup config, to not confuse some tools determining bootloader in use
    rm -f /boot/%{name}/grub.cfg

    # Cleanup installed files
    # Unless grub2 provides grub2-uninstall, we don't remove any file because
    # we have no idea what's been installed. (And a blind remove is dangerous
    # to remove user's or other package's file accidently ..)
  fi
fi
%endif

%postun
%service_del_postun grub2-once.service

%files -f %{name}.lang
%defattr(-,root,root,-)
%if 0%{?suse_version} < 1500
%doc COPYING
%else
%license COPYING
%endif
%doc NEWS README
%doc THANKS TODO ChangeLog
%doc docs/autoiso.cfg docs/osdetect.cfg
%ifarch s390x
%doc README.ibm3215
%endif
%dir /boot/%{name}
%ghost /boot/%{name}/grub.cfg
%{_sysconfdir}/bash_completion.d/grub
%config(noreplace) %{_sysconfdir}/default/grub
%dir %{_sysconfdir}/grub.d
%{_sysconfdir}/grub.d/README
%config(noreplace) %{_sysconfdir}/grub.d/00_header
%config(noreplace) %{_sysconfdir}/grub.d/10_linux
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_xen
%config(noreplace) %{_sysconfdir}/grub.d/40_custom
%config(noreplace) %{_sysconfdir}/grub.d/41_custom
%config(noreplace) %{_sysconfdir}/grub.d/90_persistent
%ifnarch ppc ppc64 ppc64le
%config(noreplace) %{_sysconfdir}/grub.d/95_textmode
%endif
%ifarch %{ix86} x86_64
%config(noreplace) %{_sysconfdir}/grub.d/20_memtest86+
%endif
%ifarch ppc ppc64 ppc64le
%config(noreplace) %{_sysconfdir}/grub.d/20_ppc_terminfo
%endif
%ifarch s390x
%config(noreplace) %{_sysconfdir}/default/zipl2grub.conf.in
%{dracutlibdir}
%{_sbindir}/%{name}-zipl-setup
%{_datadir}/%{name}/zipl-refresh
%endif
%{_sbindir}/%{name}-install
%{_sbindir}/%{name}-mkconfig
%{_sbindir}/%{name}-once
%{_sbindir}/%{name}-probe
%{_sbindir}/%{name}-reboot
%{_sbindir}/%{name}-set-default
%{_sbindir}/%{name}-check-default
%{_bindir}/%{name}-editenv
%{_bindir}/%{name}-file
%{_bindir}/%{name}-fstest
%{_bindir}/%{name}-kbdcomp
%{_bindir}/%{name}-menulst2cfg
%{_bindir}/%{name}-mkfont
%{_bindir}/%{name}-mkimage
%{_bindir}/%{name}-mklayout
%{_bindir}/%{name}-mknetdir
%{_bindir}/%{name}-mkpasswd-pbkdf2
%{_bindir}/%{name}-mkrelpath
%{_bindir}/%{name}-mkrescue
%{_bindir}/%{name}-mkstandalone
%{_bindir}/%{name}-render-label
%{_bindir}/%{name}-script-check
%{_bindir}/%{name}-syslinux2cfg
%if 0%{?has_systemd:1}
%{_unitdir}/grub2-once.service
%endif
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%if 0%{?suse_version} >= 1140
%{_datadir}/%{name}/*.pf2
%endif
%{_datadir}/%{name}/grub-mkconfig_lib
%{_infodir}/grub-dev.info*
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}-editenv.1.*
%{_mandir}/man1/%{name}-file.1.*
%{_mandir}/man1/%{name}-fstest.1.*
%{_mandir}/man1/%{name}-kbdcomp.1.*
%{_mandir}/man1/%{name}-menulst2cfg.1.*
%{_mandir}/man1/%{name}-mkfont.1.*
%{_mandir}/man1/%{name}-mkimage.1.*
%{_mandir}/man1/%{name}-mklayout.1.*
%{_mandir}/man1/%{name}-mknetdir.1.*
%{_mandir}/man1/%{name}-mkpasswd-pbkdf2.1.*
%{_mandir}/man1/%{name}-mkrelpath.1.*
%{_mandir}/man1/%{name}-mkrescue.1.*
%{_mandir}/man1/%{name}-mkstandalone.1.*
%{_mandir}/man1/%{name}-render-label.1.*
%{_mandir}/man1/%{name}-script-check.1.*
%{_mandir}/man1/%{name}-syslinux2cfg.1.*
%{_mandir}/man8/%{name}-install.8.*
%{_mandir}/man8/%{name}-mkconfig.8.*
%{_mandir}/man8/%{name}-probe.8.*
%{_mandir}/man8/%{name}-reboot.8.*
%{_mandir}/man8/%{name}-set-default.8.*
%if %{emu}
%{_bindir}/%{name}-emu
%{_mandir}/man1/%{name}-emu.1.*
%endif
%ifnarch s390x
%config(noreplace) %{_sysconfdir}/grub.d/30_os-prober
%{_bindir}/%{name}-glue-efi
%{_bindir}/%{name}-mount
%{_sbindir}/%{name}-bios-setup
%{_sbindir}/%{name}-macbless
%{_sbindir}/%{name}-ofpathname
%{_sbindir}/%{name}-sparc64-setup
%{_mandir}/man1/%{name}-glue-efi.1.*
%{_mandir}/man1/%{name}-mount.1.*
%{_mandir}/man8/%{name}-bios-setup.8.*
%{_mandir}/man8/%{name}-macbless.8.*
%{_mandir}/man8/%{name}-ofpathname.8.*
%{_mandir}/man8/%{name}-sparc64-setup.8.*
%endif

%files branding-upstream
%defattr(-,root,root,-)
%{_datadir}/%{name}/themes/starfield

%if ! 0%{?only_efi:1}

%files %{grubarch}
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubarch}
%ifarch ppc ppc64 ppc64le
# This is intentionally "grub.chrp" and not "%%{name}.chrp"
%{_datadir}/%{name}/%{grubarch}/grub.chrp
%{_datadir}/%{name}/%{grubarch}/bootinfo.txt
%endif
%ifnarch ppc ppc64 ppc64le s390x %{arm}
%{_datadir}/%{name}/%{grubarch}/*.image
%endif
%{_datadir}/%{name}/%{grubarch}/*.img
%{_datadir}/%{name}/%{grubarch}/*.lst
%{_datadir}/%{name}/%{grubarch}/*.mod
%ifarch x86_64
%{_datadir}/%{name}/%{grubarch}/efiemu*.o
%endif
%{_datadir}/%{name}/%{grubarch}/kernel.exec
%{_datadir}/%{name}/%{grubarch}/modinfo.sh

%files %{grubarch}-debug
%defattr(-,root,root,-)
%{_datadir}/%{name}/%{grubarch}/gdb_grub
%{_datadir}/%{name}/%{grubarch}/gmodule.pl
%{_datadir}/%{name}/%{grubarch}/*.module

%endif

%ifarch %{efi}

%files %{grubefiarch}
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubefiarch}
%{_datadir}/%{name}/%{grubefiarch}/grub.efi
%ifarch x86_64
%{_datadir}/%{name}/%{grubefiarch}/grub-tpm.efi
%endif
%{_datadir}/%{name}/%{grubefiarch}/*.img
%{_datadir}/%{name}/%{grubefiarch}/*.lst
%{_datadir}/%{name}/%{grubefiarch}/*.mod
%{_datadir}/%{name}/%{grubefiarch}/kernel.exec
%{_datadir}/%{name}/%{grubefiarch}/modinfo.sh
%dir %{sysefibasedir}
%dir %{sysefidir}
%{sysefidir}/grub.efi
%if 0%{?suse_version} < 1600
%ifarch x86_64
# provide compatibility sym-link for previous shim-install and kiwi
%dir /usr/lib64/efi
/usr/lib64/efi/DEPRECATED
/usr/lib64/efi/grub.efi
%endif
%endif

%ifarch x86_64 aarch64
%if 0%{?suse_version} >= 1230 || 0%{?suse_version} == 1110
%{sysefidir}/grub.der
%endif
%endif

%files %{grubefiarch}-debug
%defattr(-,root,root,-)
%{_datadir}/%{name}/%{grubefiarch}/gdb_grub
%{_datadir}/%{name}/%{grubefiarch}/gmodule.pl
%{_datadir}/%{name}/%{grubefiarch}/*.module

%endif

%files snapper-plugin
%defattr(-,root,root,-)
%dir %{_libdir}/snapper
%dir %{_libdir}/snapper/plugins
%config(noreplace) %{_sysconfdir}/grub.d/80_suse_btrfs_snapshot
%{_libdir}/snapper/plugins/grub

%ifarch %{ix86} x86_64
%files %{grubxenarch}
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubxenarch}
%{_datadir}/%{name}/%{grubxenarch}/*
# provide compatibility sym-link for VM definitions pointing to old location
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{grubxenarch}
%endif

%if 0%{?has_systemd:1}
%files systemd-sleep-plugin
%defattr(-,root,root,-)
%dir %{_libdir}/systemd/system-sleep
%{_libdir}/systemd/system-sleep/grub2.sleep
%endif

%changelog
