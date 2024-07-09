#
# spec file for package grub2
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
# needssslcertforbuild


%define _binaries_in_noarch_package_terminate_build 0

%if %{defined sbat_distro}
# SBAT metadata
%define sbat_generation 1
%define sbat_generation_grub 4
%else
%{error please define sbat_distro, sbat_distro_summary and sbat_distro_url}
%endif

Name:           grub2
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  glibc-devel
%if 0%{?suse_version} >= 1140
BuildRequires:  dejavu-fonts
BuildRequires:  gnu-unifont
%endif
BuildRequires:  help2man
BuildRequires:  libtasn1-devel
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
%ifarch x86_64 aarch64 ppc ppc64 ppc64le
BuildRequires:  openssl >= 0.9.8
BuildRequires:  pesign-obs-integration
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
%define brp_pesign_reservation 65536
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

%ifarch %{efi}
# The branding package requires grub2. It's not necessary here,
# so break the dep to avoid a cycle.
#!BuildIgnore: grub2
BuildRequires:  grub2-branding
BuildRequires:  squashfs
%endif

# For ALP and Tumbleweed
%if 0%{?suse_version} >= 1600
# Only include the macros for the architectures with the newer UEFI and TCG protocol
%ifarch x86_64 aarch64 riscv64
BuildRequires:  fde-tpm-helper-rpm-macros
%endif
%endif

Version:        2.12
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
Source19:       grub2-instdev-fixup.pl
Source1000:     PATCH_POLICY
Patch1:         rename-grub-info-file-to-grub2.patch
Patch2:         grub2-linux.patch
Patch3:         use-grub2-as-a-package-name.patch
Patch4:         info-dir-entry.patch
Patch5:         grub2-simplefb.patch
Patch6:         grub2-iterate-and-hook-for-extended-partition.patch
Patch7:         grub2-ppc-terminfo.patch
Patch8:         grub2-fix-error-terminal-gfxterm-isn-t-found.patch
Patch9:         grub2-fix-menu-in-xen-host-server.patch
Patch10:        not-display-menu-when-boot-once.patch
Patch11:        grub2-pass-corret-root-for-nfsroot.patch
Patch12:        grub2-efi-HP-workaround.patch
Patch13:        grub2-secureboot-add-linuxefi.patch
Patch14:        grub2-secureboot-no-insmod-on-sb.patch
Patch15:        grub2-secureboot-chainloader.patch
Patch16:        grub2-linuxefi-fix-boot-params.patch
Patch17:        grub2-linguas.sh-no-rsync.patch
Patch18:        grub2-use-Unifont-for-starfield-theme-terminal.patch
Patch19:        grub2-s390x-01-Changes-made-and-files-added-in-order-to-allow-s390x.patch
Patch20:        grub2-s390x-03-output-7-bit-ascii.patch
Patch21:        grub2-s390x-04-grub2-install.patch
Patch22:        grub2-s390x-05-grub2-mkconfig.patch
Patch23:        grub2-use-rpmsort-for-version-sorting.patch
Patch24:        grub2-getroot-treat-mdadm-ddf-as-simple-device.patch
Patch25:        grub2-setup-try-fs-embed-if-mbr-gap-too-small.patch
Patch26:        grub2-xen-linux16.patch
Patch27:        grub2-efi-disable-video-cirrus-and-bochus.patch
Patch28:        grub2-vbe-blacklist-preferred-1440x900x32.patch
Patch29:        grub2-grubenv-in-btrfs-header.patch
Patch30:        grub2-mkconfig-aarch64.patch
Patch31:        grub2-default-distributor.patch
Patch32:        grub2-menu-unrestricted.patch
Patch33:        grub2-mkconfig-arm.patch
Patch34:        grub2-s390x-06-loadparm.patch
Patch35:        grub2-s390x-07-add-image-param-for-zipl-setup.patch
Patch36:        grub2-s390x-08-workaround-part-to-disk.patch
Patch37:        grub2-commands-introduce-read_file-subcommand.patch
Patch38:        grub2-efi-chainload-harder.patch
Patch39:        grub2-emu-4-all.patch
Patch40:        grub2-lvm-allocate-metadata-buffer-from-raw-contents.patch
Patch41:        grub2-diskfilter-support-pv-without-metadatacopies.patch
Patch42:        grub2-s390x-09-improve-zipl-setup.patch
Patch43:        grub2-getroot-scan-disk-pv.patch
Patch44:        grub2-util-30_os-prober-multiple-initrd.patch
Patch45:        grub2-getroot-support-nvdimm.patch
Patch46:        grub2-install-fix-not-a-directory-error.patch
Patch47:        grub-install-force-journal-draining-to-ensure-data-i.patch
Patch48:        grub2-s390x-skip-zfcpdump-image.patch
Patch49:        grub2-btrfs-01-add-ability-to-boot-from-subvolumes.patch
Patch50:        grub2-btrfs-02-export-subvolume-envvars.patch
Patch51:        grub2-btrfs-03-follow_default.patch
Patch52:        grub2-btrfs-04-grub2-install.patch
Patch53:        grub2-btrfs-05-grub2-mkconfig.patch
Patch54:        grub2-btrfs-06-subvol-mount.patch
Patch55:        grub2-btrfs-07-subvol-fallback.patch
Patch56:        grub2-btrfs-08-workaround-snapshot-menu-default-entry.patch
Patch57:        grub2-btrfs-09-get-default-subvolume.patch
Patch58:        grub2-btrfs-10-config-directory.patch
Patch59:        grub2-efi-xen-chainload.patch
Patch60:        grub2-efi-xen-cmdline.patch
Patch61:        grub2-efi-xen-cfg-unquote.patch
Patch62:        grub2-efi-xen-removable.patch
Patch63:        grub2-Add-hidden-menu-entries.patch
Patch64:        grub2-SUSE-Add-the-t-hotkey.patch
Patch65:        grub2-zipl-setup-fix-btrfs-multipledev.patch
Patch66:        grub2-suse-remove-linux-root-param.patch
Patch67:        grub2-ppc64le-disable-video.patch
Patch68:        grub2-ppc64le-memory-map.patch
Patch69:        grub2-ppc64-cas-reboot-support.patch
Patch70:        grub2-install-remove-useless-check-PReP-partition-is-empty.patch
Patch71:        grub2-ppc64-cas-new-scope.patch
Patch72:        grub2-ppc64-cas-fix-double-free.patch
Patch73:        grub2-efi_gop-avoid-low-resolution.patch
Patch74:        0003-bootp-New-net_bootp6-command.patch
Patch75:        0004-efinet-UEFI-IPv6-PXE-support.patch
Patch76:        0005-grub.texi-Add-net_bootp6-doument.patch
Patch77:        0006-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch78:        0007-efinet-Setting-network-from-UEFI-device-path.patch
Patch79:        0008-efinet-Setting-DNS-server-from-UEFI-protocol.patch
Patch80:        0012-tpm-Build-tpm-as-module.patch
Patch81:        0001-add-support-for-UEFI-network-protocols.patch
Patch82:        0002-AUDIT-0-http-boot-tracker-bug.patch
Patch83:        grub2-mkconfig-default-entry-correction.patch
Patch84:        grub2-s390x-11-secureboot.patch
Patch85:        grub2-s390x-12-zipl-setup-usrmerge.patch
Patch86:        grub2-secureboot-install-signed-grub.patch
Patch87:        grub2-btrfs-help-on-snapper-rollback.patch
Patch88:        grub2-video-limit-the-resolution-for-fixed-bimap-font.patch
Patch89:        grub2-gfxmenu-support-scrolling-menu-entry-s-text.patch
Patch90:        0001-kern-mm.c-Make-grub_calloc-inline.patch
Patch91:        0002-cmdline-Provide-cmdline-functions-as-module.patch
Patch92:        0001-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch93:        0002-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch94:        0001-Unify-the-check-to-enable-btrfs-relative-path.patch
Patch95:        0001-efi-linux-provide-linux-command.patch
Patch96:        0001-Add-support-for-Linux-EFI-stub-loading-on-aarch64.patch
Patch97:        0002-arm64-make-sure-fdt-has-address-cells-and-size-cells.patch
Patch98:        0003-Make-grub_error-more-verbose.patch
Patch99:        0004-arm-arm64-loader-Better-memory-allocation-and-error-.patch
Patch100:       0006-efi-Set-image-base-address-before-jumping-to-the-PE-.patch
Patch101:       0044-squash-kern-Add-lockdown-support.patch
Patch102:       0001-ieee1275-Avoiding-many-unecessary-open-close.patch
Patch103:       0001-Workaround-volatile-efi-boot-variable.patch
Patch104:       0001-templates-Follow-the-path-of-usr-merged-kernel-confi.patch
Patch105:       0001-ieee1275-implement-FCP-methods-for-WWPN-and-LUNs.patch
Patch106:       0001-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch107:       0002-Arm-check-for-the-PE-magic-for-the-compiled-arch.patch
Patch108:       0001-Factor-out-grub_efi_linux_boot.patch
Patch109:       0002-Fix-race-in-EFI-validation.patch
Patch110:       0003-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
Patch111:       0004-Try-to-pick-better-locations-for-kernel-and-initrd.patch
Patch112:       0005-x86-efi-Use-bounce-buffers-for-reading-to-addresses-.patch
Patch113:       0006-x86-efi-Re-arrange-grub_cmd_linux-a-little-bit.patch
Patch114:       0007-x86-efi-Make-our-own-allocator-for-kernel-stuff.patch
Patch115:       0008-x86-efi-Allow-initrd-params-cmdline-allocations-abov.patch
Patch116:       0009-x86-efi-Reduce-maximum-bounce-buffer-size-to-16-MiB.patch
Patch117:       0010-efilinux-Fix-integer-overflows-in-grub_cmd_initrd.patch
Patch118:       0011-Also-define-GRUB_EFI_MAX_ALLOCATION_ADDRESS-for-RISC.patch
Patch119:       0004-Add-suport-for-signing-grub-with-an-appended-signatu.patch
Patch120:       0005-docs-grub-Document-signing-grub-under-UEFI.patch
Patch121:       0006-docs-grub-Document-signing-grub-with-an-appended-sig.patch
Patch122:       0007-dl-provide-a-fake-grub_dl_set_persistent-for-the-emu.patch
Patch123:       0008-pgp-factor-out-rsa_pad.patch
Patch124:       0009-crypto-move-storage-for-grub_crypto_pk_-to-crypto.c.patch
Patch125:       0010-posix_wrap-tweaks-in-preparation-for-libtasn1.patch
Patch126:       0011-libtasn1-import-libtasn1-4.18.0.patch
Patch127:       0012-libtasn1-disable-code-not-needed-in-grub.patch
Patch128:       0013-libtasn1-changes-for-grub-compatibility.patch
Patch129:       0014-libtasn1-compile-into-asn1-module.patch
Patch130:       0015-test_asn1-test-module-for-libtasn1.patch
Patch131:       0016-grub-install-support-embedding-x509-certificates.patch
Patch132:       0017-appended-signatures-import-GNUTLS-s-ASN.1-descriptio.patch
Patch133:       0018-appended-signatures-parse-PKCS-7-signedData-and-X.50.patch
Patch134:       0019-appended-signatures-support-verifying-appended-signa.patch
Patch135:       0020-appended-signatures-verification-tests.patch
Patch136:       0021-appended-signatures-documentation.patch
Patch137:       0022-ieee1275-enter-lockdown-based-on-ibm-secure-boot.patch
Patch138:       0023-x509-allow-Digitial-Signature-plus-other-Key-Usages.patch
Patch139:       0001-grub-install-Add-SUSE-signed-image-support-for-power.patch
Patch140:       0001-Add-grub_envblk_buf-helper-function.patch
Patch141:       0002-Add-grub_disk_write_tail-helper-function.patch
Patch142:       0003-grub-install-support-prep-environment-block.patch
Patch143:       0004-Introduce-prep_load_env-command.patch
Patch144:       0005-export-environment-at-start-up.patch
Patch145:       0001-grub-install-bailout-root-device-probing.patch
Patch146:       0001-install-fix-software-raid1-on-esp.patch
Patch147:       0001-grub-probe-Deduplicate-probed-partmap-output.patch
Patch148:       0001-Fix-infinite-boot-loop-on-headless-system-in-qemu.patch
Patch149:       0001-ofdisk-improve-boot-time-by-lookup-boot-disk-first.patch
Patch150:       0001-key_protector-Add-key-protectors-framework.patch
Patch151:       0002-tpm2-Add-TPM-Software-Stack-TSS.patch
Patch152:       0003-key_protector-Add-TPM2-Key-Protector.patch
Patch153:       0004-cryptodisk-Support-key-protectors.patch
Patch154:       0005-util-grub-protect-Add-new-tool.patch
Patch155:       0008-linuxefi-Use-common-grub_initrd_load.patch
Patch156:       0009-Add-crypttab_entry-to-obviate-the-need-to-input-pass.patch
Patch157:       0010-templates-import-etc-crypttab-to-grub.cfg.patch
Patch158:       grub-read-pcr.patch
Patch159:       tpm-record-pcrs.patch
Patch160:       grub-install-record-pcrs.patch
Patch161:       safe_tpm_pcr_snapshot.patch
Patch162:       0001-ieee1275-add-support-for-NVMeoFC.patch
Patch163:       0002-ieee1275-ofpath-enable-NVMeoF-logical-device-transla.patch
Patch164:       0003-ieee1275-change-the-logic-of-ieee1275_get_devargs.patch
Patch165:       0004-ofpath-controller-name-update.patch
Patch166:       0002-Mark-environmet-blocks-as-used-for-image-embedding.patch
Patch167:       grub2-increase-crypttab-path-buffer.patch
Patch168:       0001-grub2-Set-multiple-device-path-for-a-nvmf-boot-devic.patch
Patch169:       0001-grub2-Can-t-setup-a-default-boot-device-correctly-on.patch
Patch170:       0001-tpm2-Support-authorized-policy.patch
Patch171:       0001-tpm2-Add-extra-RSA-SRK-types.patch
Patch174:       0001-clean-up-crypttab-and-linux-modules-dependency.patch
Patch175:       0002-discard-cached-key-before-entering-grub-shell-and-ed.patch
Patch176:       0001-ieee1275-ofdisk-retry-on-open-and-read-failure.patch
Patch177:       0002-Restrict-cryptsetup-key-file-permission-for-better-s.patch
Patch178:       0001-openfw-Ensure-get_devargs-and-get_devname-functions-.patch
Patch179:       0002-prep_loadenv-Fix-regex-for-Open-Firmware-device-spec.patch
Patch180:       0001-xen_boot-add-missing-grub_arch_efi_linux_load_image_.patch
Patch181:       0001-font-Try-memdisk-fonts-with-the-same-name.patch
Patch182:       0001-Make-grub.cfg-compatible-to-old-binaries.patch
Patch183:       grub2-change-bash-completion-dir.patch
Patch184:       0001-tpm2-Implement-NV-index.patch
Patch185:       0002-cryptodisk-Fallback-to-passphrase.patch
Patch186:       0003-cryptodisk-wipe-out-the-cached-keys-from-protectors.patch
Patch187:       0004-diskfilter-look-up-cryptodisk-devices-first.patch
Patch188:       grub2-mkconfig-riscv64.patch
Patch189:       arm64-Use-proper-memory-type-for-kernel-allocation.patch
Patch190:       0001-luks2-Use-grub-tpm2-token-for-TPM2-protected-volume-.patch
Patch191:       Fix-the-size-calculation-for-the-synthesized-initrd.patch
Patch192:       0001-Improve-TPM-key-protection-on-boot-interruptions.patch
Patch193:       0002-Restrict-file-access-on-cryptodisk-print.patch
Patch194:       0003-Restrict-ls-and-auto-file-completion-on-cryptodisk-p.patch
Patch195:       0004-Key-revocation-on-out-of-bound-file-access.patch
# Workaround for 2.12 tarball
Patch196:       fix_no_extra_deps_in_release_tarball.patch
Patch197:       0001-fs-xfs-always-verify-the-total-number-of-entries-is-.patch
Patch198:       0001-loader-arm64-efi-linux-Remove-magic-number-header-fi.patch
Patch199:       0001-squash-ieee1275-ofpath-enable-NVMeoF-logical-device-.patch
Patch200:       0001-ofdisk-enhance-boot-time-by-focusing-on-boot-disk-re.patch
Patch201:       0002-ofdisk-add-early_log-support.patch
Patch202:       0001-disk-Optimize-disk-iteration-by-moving-memdisk-to-th.patch
Patch203:       grub2-bsc1220338-key_protector-implement-the-blocklist.patch
Patch204:       0001-ofdisk-Enhance-canonical-path-handling-for-bootpath.patch
Patch205:       0001-10_linux-Ensure-persistence-of-root-file-system-moun.patch
Patch206:       0001-util-bash-completion-Fix-for-bash-completion-2.12.patch
Patch207:       0001-util-enable-grub-protect-only-for-EFI-systems.patch
Patch208:       0001-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch
Patch209:       0002-Add-BLS-support-to-grub-mkconfig.patch
Patch210:       0003-Add-grub2-switch-to-blscfg.patch
Patch211:       0004-blscfg-Don-t-root-device-in-emu-builds.patch
Patch212:       0005-blscfg-check-for-mounted-boot-in-emu.patch
Patch213:       0006-Follow-the-device-where-blscfg-is-discovered.patch
Patch214:       0007-grub-switch-to-blscfg-adapt-to-openSUSE.patch
Patch215:       0008-blscfg-reading-bls-fragments-if-boot-present.patch
Patch216:       0009-10_linux-Some-refinement-for-BLS.patch
Patch217:       0001-net-drivers-ieee1275-ofnet-Remove-200-ms-timeout-in-.patch

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
Requires:       kexec-tools
Requires:       (/sbin/showconsole or /usr/sbin/showconsole)
# for /sbin/zipl used by grub2-zipl-setup
Requires:       s390-tools
%endif
%ifarch ppc64 ppc64le
Requires:       powerpc-utils
%endif
%ifarch %{ix86}
# meanwhile, memtest is available as EFI executable
Recommends:     memtest86+
%endif

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
Requires(post): %{name} = %{version}
%{?update_bootloader_requires}

%description %{grubarch}
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It supports rich variety of kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for %{platform} systems.

%package %{grubarch}-extras
Summary:        Unsupported modules for %{grubarch}
Group:          System/Boot
BuildArch:      noarch
Requires:       %{name}-%{grubarch} = %{version}
Provides:       %{name}-%{grubarch}:%{_datadir}/%{name}/%{grubarch}/zfs.mod
Provides:       %{name}-%{grubarch}:%{_datadir}/%{name}/%{grubarch}/zfscrypt.mod
Provides:       %{name}-%{grubarch}:%{_datadir}/%{name}/%{grubarch}/zfsinfo.mod

%description %{grubarch}-extras
Unsupported modules for %{name}-%{grubarch}

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
Requires(post): %{name} = %{version}
%{?update_bootloader_requires}
%{?fde_tpm_update_requires}
Provides:       %{name}-efi = %{version}-%{release}
Obsoletes:      %{name}-efi < %{version}-%{release}

%description %{grubefiarch}
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It supports rich variety of kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for EFI systems.

%package %{grubefiarch}-extras

Summary:        Unsupported modules for %{grubefiarch}
Group:          System/Boot
BuildArch:      noarch
Requires:       %{name}-%{grubefiarch} = %{version}
Provides:       %{name}-%{grubefiarch}:%{_datadir}/%{name}/%{grubefiarch}/zfs.mod
Provides:       %{name}-%{grubefiarch}:%{_datadir}/%{name}/%{grubefiarch}/zfscrypt.mod
Provides:       %{name}-%{grubefiarch}:%{_datadir}/%{name}/%{grubefiarch}/zfsinfo.mod

%description %{grubefiarch}-extras
Unsupported modules for %{name}-%{grubefiarch}

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

%package %{grubxenarch}-extras
Summary:        Unsupported modules for %{grubxenarch}
Group:          System/Boot
BuildArch:      noarch
Requires:       %{name}-%{grubxenarch} = %{version}
Provides:       %{name}-%{grubxenarch}:%{_datadir}/%{name}/%{grubxenarch}/zfs.mod
Provides:       %{name}-%{grubxenarch}:%{_datadir}/%{name}/%{grubxenarch}/zfscrypt.mod
Provides:       %{name}-%{grubxenarch}:%{_datadir}/%{name}/%{grubxenarch}/zfsinfo.mod

%description %{grubxenarch}-extras
Unsupported modules for %{name}-%{grubxenarch}

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
%autosetup -p1 -n grub-%{version}

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

FS_MODULES="btrfs ext2 xfs jfs reiserfs"
CD_MODULES="all_video boot cat configfile echo true \
		font gfxmenu gfxterm gzio halt iso9660 \
		jpeg minicmd normal part_apple part_msdos part_gpt \
		password password_pbkdf2 png reboot search search_fs_uuid \
		search_fs_file search_label sleep test video fat loadenv loopback"
PXE_MODULES="tftp http"
CRYPTO_MODULES="luks luks2 gcry_rijndael gcry_sha1 gcry_sha256 gcry_sha512 crypttab"
%ifarch %{efi}
CD_MODULES="${CD_MODULES} chain efifwsetup efinet read tpm tpm2 memdisk tar squash4 xzio blscfg"
PXE_MODULES="${PXE_MODULES} efinet"
%else
CD_MODULES="${CD_MODULES} net ofnet"
PXE_MODULES="${PXE_MODULES} net ofnet"
%endif

%ifarch x86_64
CD_MODULES="${CD_MODULES} linuxefi"
%else
CD_MODULES="${CD_MODULES} linux"
%endif

GRUB_MODULES="${CD_MODULES} ${FS_MODULES} ${PXE_MODULES} ${CRYPTO_MODULES} mdraid09 mdraid1x lvm serial"
%ifarch ppc ppc64 ppc64le
GRUB_MODULES="${GRUB_MODULES} appendedsig memdisk tar regexp prep_loadenv tpm"
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

%if 0%{?sbat_generation}
echo "sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md" > sbat.csv
echo "grub,%{sbat_generation_grub},Free Software Foundation,grub,%{version},https://www.gnu.org/software/grub/" >> sbat.csv
echo "grub.%{sbat_distro},%{sbat_generation},%{sbat_distro_summary},%{name},%{version},%{sbat_distro_url}" >> sbat.csv
%endif

mkdir -p ./fonts
cp %{_datadir}/%{name}/themes/*/*.pf2 ./fonts
cp ./unicode.pf2 ./fonts
%if 0%{?suse_version} > 1500
tar --sort=name -cf - ./fonts | mksquashfs - memdisk.sqsh -tar -comp xz -quiet -no-progress
%else
mksquashfs ./fonts memdisk.sqsh -keep-as-directory -comp xz -quiet -no-progress
%endif

./grub-mkimage -O %{grubefiarch} -o grub.efi --memdisk=./memdisk.sqsh --prefix= %{?sbat_generation:--sbat sbat.csv} \
		-d grub-core ${GRUB_MODULES}

%ifarch x86_64 aarch64
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

if [ "%{platform}" = "ieee1275" ]; then
        # So far neither OpenFirmware nor grub support CA chain, only certificate pinning
        # Use project certificate always in the shipped informational file and
        # for kernel verification
        projectcert="%{_sourcedir}/_projectcert.crt"
        openssl x509 -in "$projectcert" -outform DER -out grub.der
        cat > %{platform}-config <<'EOF'
set root=memdisk
set prefix=($root)/
echo "earlycfg: root=$root prefix=$prefix"
EOF
        cat > ./grub.cfg <<'EOF'

regexp --set 1:bdev --set 2:bpath '\((.*)\)(.*)' "$cmdpath"
regexp --set 1:bdev --set 2:bpart '(.*[^\])(,.*)' "$bdev"

echo "bdev=$bdev"
echo "bpart=$bpart"
echo "bpath=$bpath"

if regexp '^(tftp|http)$' "$bdev"; then
  if [ -z "$bpath" ]; then
    echo "network booting via $bdev but firmware didn't provide loaded path from sever root"
    bpath="/boot/grub2/powerpc-ieee1275"
    echo "using bpath=$bpath as fallback path"
  fi
elif [ -z "$ENV_FS_UUID" ]; then
  echo "Reading vars from ($bdev)"
  prep_load_env "($bdev)"
fi

echo "ENV_HINT=$ENV_HINT"
echo "ENV_GRUB_DIR=$ENV_GRUB_DIR"
echo "ENV_FS_UUID=$ENV_FS_UUID"
echo "ENV_CRYPTO_UUID=$ENV_CRYPTO_UUID"

if [ "$btrfs_relative_path" = xy ]; then
  btrfs_relative_path=1
fi

if [ "$bdev" -a "$bpart" -a "$bpath" ]; then
  set hints="--hint $bdev$bpart"
  set cfg_dir="$bpath"
elif [ "$bdev" -a "$bpart" ]; then
  set hints="--hint $bdev$bpart"
  set cfg_dir="/boot/grub2 /grub2"
  set btrfs_relative_path=1
elif [ "$bdev" ]; then
  if [ "$ENV_HINT" ]; then
    set hints="--hint $ENV_HINT"
  else
    set hints="--hint ${bdev},"
  fi
  if [ "$ENV_GRUB_DIR" ]; then
    set cfg_dir="$ENV_GRUB_DIR"
  else
    set cfg_dir="/boot/grub2 /grub2"
    set btrfs_relative_path=1
  fi
else
  set hints=""
  set cfg_dir="/boot/grub2 /grub2"
  set btrfs_relative_path=1
fi

set prefix=""
set root=""
set cfg="grub.cfg"

for uuid in $ENV_CRYPTO_UUID; do
  cryptomount -u $uuid
done

if [ "$ENV_FS_UUID" ]; then
  echo "searching for $ENV_FS_UUID with $hints"
  if search --fs-uuid --set=root "$ENV_FS_UUID" $hints; then
    echo "$ENV_FS_UUID is on $root"
  fi
fi

for d in ${cfg_dir}; do
  if [ -z "$root" ]; then
    echo "searching for ${d}/${cfg}"
    if search --file --set=root "${d}/${cfg}" $hints; then
      echo "${d}/${cfg} is on $root"
      prefix="($root)${d}"
    fi
  elif [ -f "${d}/${cfg}" ]; then
    echo "${d}/${cfg} is on $root"
    prefix="($root)${d}"
  else
    echo "${d}/${cfg} not found in $root"
  fi

  if [ "$prefix" -a x"$btrfs_relative_path" = x1 ]; then
    btrfs_relative_path=0
    if [ -f /@"${d}"/powerpc-ieee1275/command.lst ]; then
      btrfs_relative_path=1
      echo "mounting subvolume @${d}/powerpc-ieee1275 on ${d}/powerpc-ieee1275"
      btrfs-mount-subvol ($root) "${d}"/powerpc-ieee1275 @"${d}"/powerpc-ieee1275
    fi
    btrfs_relative_path=1
    break
  fi
done

echo "prefix=$prefix root=$root"
if [ -n "$prefix" ]; then
  source "${prefix}/${cfg}"
fi
EOF
        %{__tar} cvf memdisk.tar ./grub.cfg
        ./grub-mkimage -O %{grubarch} -o grub.elf -d grub-core -x grub.der -m memdisk.tar \
            -c %{platform}-config --appended-signature-size %brp_pesign_reservation ${GRUB_MODULES}
        ls -l "grub.elf"
        truncate -s -%brp_pesign_reservation "grub.elf"
fi
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
ln -srf %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/grub.efi %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/grub-tpm.efi
%endif

# Create grub.efi link to system efi directory
# This is for tools like kiwi not fiddling with the path
%define sysefibasedir %{_datadir}/efi
%define sysefidir %{sysefibasedir}/%{_target_cpu}
install -d %{buildroot}/%{sysefidir}
ln -sr %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/grub.efi %{buildroot}%{sysefidir}/grub.efi
%if 0%{?suse_version} < 1600
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
%endif

%ifarch x86_64 aarch64
export BRP_PESIGN_FILES="%{_datadir}/%{name}/%{grubefiarch}/grub.efi"
install -m 444 grub.der %{buildroot}/%{sysefidir}/
%endif

cd ..
%endif

%if ! 0%{?only_efi:1}
cd build
%make_install
if [ "%{platform}" = "ieee1275" ]; then
        export BRP_PESIGN_FILES="%{_datadir}/%{name}/%{grubarch}/grub.elf"
        export BRP_PESIGN_GRUB_RESERVATION=%brp_pesign_reservation
        install -m 444 grub.der %{buildroot}%{_datadir}/%{name}/%{grubarch}/
        install -m 644 grub.elf %{buildroot}%{_datadir}/%{name}/%{grubarch}/
fi
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
%ifarch  %{ix86} x86_64
install -m 755 -D %{SOURCE19} %{buildroot}/%{_libexecdir}/grub2-instdev-fixup.pl
%endif

R="%{buildroot}"

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

# bsc#1205554 move the zfs modules into extras packages
# EXTRA_PATTERN='pattern1|pattern2|pattern3|...'
EXTRA_PATTERN="zfs"
%ifarch %{ix86} x86_64
find %{buildroot}/%{_datadir}/%{name}/%{grubxenarch}/ -type f | sed 's,%{buildroot},,' > %{grubxenarch}-all.lst
grep -v -E ${EXTRA_PATTERN} %{grubxenarch}-all.lst > %{grubxenarch}.lst
grep -E ${EXTRA_PATTERN} %{grubxenarch}-all.lst > %{grubxenarch}-extras.lst
%endif

%ifarch %{efi}
find %{buildroot}/%{_datadir}/%{name}/%{grubefiarch}/ -name '*.mod' | sed 's,%{buildroot},,' > %{grubefiarch}-mod-all.lst
grep -v -E ${EXTRA_PATTERN} %{grubefiarch}-mod-all.lst > %{grubefiarch}-mod.lst
grep -E ${EXTRA_PATTERN} %{grubefiarch}-mod-all.lst > %{grubefiarch}-mod-extras.lst
%endif

find %{buildroot}/%{_datadir}/%{name}/%{grubarch}/ -name '*.mod' | sed 's,%{buildroot},,' > %{grubarch}-mod-all.lst
grep -v -E ${EXTRA_PATTERN} %{grubarch}-mod-all.lst > %{grubarch}-mod.lst
grep -E ${EXTRA_PATTERN} %{grubarch}-mod-all.lst > %{grubarch}-mod-extras.lst

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
%{?update_bootloader_check_type_reinit_post:%update_bootloader_check_type_reinit_post grub2}

%posttrans %{grubarch}
%{?update_bootloader_posttrans}

%endif

%ifarch %{efi}

%post %{grubefiarch}
%if 0%{?fde_tpm_update_post:1}
%fde_tpm_update_post grub2-efi
%endif

%{?update_bootloader_check_type_reinit_post:%update_bootloader_check_type_reinit_post grub2-efi}

%posttrans %{grubefiarch}
%{?update_bootloader_posttrans}
%{?fde_tpm_update_posttrans}

%endif

%preun
%service_del_preun grub2-once.service

%postun
%service_del_postun grub2-once.service

%files -f %{name}.lang
%defattr(-,root,root,-)
%if 0%{?suse_version} < 1500
%doc COPYING
%else
%license COPYING
%endif
%doc AUTHORS
%doc NEWS README
%doc THANKS TODO ChangeLog
%doc docs/autoiso.cfg docs/osdetect.cfg
%ifarch s390x
%doc README.ibm3215
%endif
%dir /boot/%{name}
%ghost %attr(600, root, root) /boot/%{name}/grub.cfg
%{_datadir}/bash-completion/completions/grub*
%config(noreplace) %{_sysconfdir}/default/grub
%dir %{_sysconfdir}/grub.d
%{_sysconfdir}/grub.d/README
%config(noreplace) %{_sysconfdir}/grub.d/00_header
%config(noreplace) %{_sysconfdir}/grub.d/05_crypttab
%config(noreplace) %{_sysconfdir}/grub.d/10_linux
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_xen
%config(noreplace) %{_sysconfdir}/grub.d/25_bli
%config(noreplace) %{_sysconfdir}/grub.d/30_uefi-firmware
%config(noreplace) %{_sysconfdir}/grub.d/40_custom
%config(noreplace) %{_sysconfdir}/grub.d/41_custom
%config(noreplace) %{_sysconfdir}/grub.d/90_persistent
%ifnarch ppc ppc64 ppc64le
%config(noreplace) %{_sysconfdir}/grub.d/95_textmode
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
%{_sbindir}/%{name}-switch-to-blscfg
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
%ifarch %{efi}
%{_bindir}/%{name}-protect
%endif
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
%{_mandir}/man8/%{name}-switch-to-blscfg.8.*
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
%ifarch %{efi}
%{_mandir}/man1/%{name}-protect.1.*
%endif

%files branding-upstream
%defattr(-,root,root,-)
%{_datadir}/%{name}/themes/starfield

%if ! 0%{?only_efi:1}

%files %{grubarch} -f %{grubarch}-mod.lst
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubarch}
%ifarch ppc ppc64 ppc64le
# This is intentionally "grub.chrp" and not "%%{name}.chrp"
%{_datadir}/%{name}/%{grubarch}/grub.chrp
%{_datadir}/%{name}/%{grubarch}/grub.elf
%{_datadir}/%{name}/%{grubarch}/grub.der
%{_datadir}/%{name}/%{grubarch}/bootinfo.txt
%endif
%ifnarch ppc ppc64 ppc64le s390x %{arm}
%{_datadir}/%{name}/%{grubarch}/*.image
%endif
%{_datadir}/%{name}/%{grubarch}/*.img
%{_datadir}/%{name}/%{grubarch}/*.lst
%ifarch x86_64
%{_datadir}/%{name}/%{grubarch}/efiemu*.o
%endif
%{_datadir}/%{name}/%{grubarch}/kernel.exec
%{_datadir}/%{name}/%{grubarch}/modinfo.sh
%ifarch %{ix86} x86_64
%{_libexecdir}/%{name}-instdev-fixup.pl
%endif

%files %{grubarch}-extras -f %{grubarch}-mod-extras.lst
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubarch}

%files %{grubarch}-debug
%defattr(-,root,root,-)
%{_datadir}/%{name}/%{grubarch}/gdb_grub
%{_datadir}/%{name}/%{grubarch}/gdb_helper.py
%{_datadir}/%{name}/%{grubarch}/*.module

%endif

%ifarch %{efi}

%files %{grubefiarch} -f %{grubefiarch}-mod.lst
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubefiarch}
%{_datadir}/%{name}/%{grubefiarch}/grub.efi
%ifarch x86_64
%{_datadir}/%{name}/%{grubefiarch}/grub-tpm.efi
%endif
%{_datadir}/%{name}/%{grubefiarch}/*.img
%{_datadir}/%{name}/%{grubefiarch}/*.lst
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
%{sysefidir}/grub.der
%endif

%files %{grubefiarch}-extras -f %{grubefiarch}-mod-extras.lst
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubefiarch}

%files %{grubefiarch}-debug
%defattr(-,root,root,-)
%{_datadir}/%{name}/%{grubefiarch}/gdb_grub
%{_datadir}/%{name}/%{grubefiarch}/gdb_helper.py
%{_datadir}/%{name}/%{grubefiarch}/*.module

%endif

%files snapper-plugin
%defattr(-,root,root,-)
%dir %{_libdir}/snapper
%dir %{_libdir}/snapper/plugins
%config(noreplace) %{_sysconfdir}/grub.d/80_suse_btrfs_snapshot
%{_libdir}/snapper/plugins/grub

%ifarch %{ix86} x86_64
%files %{grubxenarch} -f %{grubxenarch}.lst
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubxenarch}
# provide compatibility sym-link for VM definitions pointing to old location
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{grubxenarch}

%files %{grubxenarch}-extras -f %{grubxenarch}-extras.lst
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/%{grubxenarch}
%endif

%if 0%{?has_systemd:1}
%files systemd-sleep-plugin
%defattr(-,root,root,-)
%dir %{_libdir}/systemd/system-sleep
%{_libdir}/systemd/system-sleep/grub2.sleep
%endif

%changelog
