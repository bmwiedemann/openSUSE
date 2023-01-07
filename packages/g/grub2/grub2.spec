#
# spec file for package grub2
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
# needssslcertforbuild


%define _binaries_in_noarch_package_terminate_build 0

%if %{defined sbat_distro}
# SBAT metadata
%define sbat_generation 1
%define sbat_generation_grub 3
%else
%{error please define sbat_distro, sbat_distro_summary and sbat_distro_url}
%endif

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

Version:        2.06
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
Source19:       grub2-instdev-fixup.pl
Source1000:     PATCH_POLICY
Patch1:         rename-grub-info-file-to-grub2.patch
Patch2:         grub2-linux.patch
Patch3:         use-grub2-as-a-package-name.patch
Patch4:         info-dir-entry.patch
Patch5:         grub2-simplefb.patch
Patch6:         grub2-iterate-and-hook-for-extended-partition.patch
Patch8:         grub2-ppc-terminfo.patch
Patch9:         grub2-GRUB_CMDLINE_LINUX_RECOVERY-for-recovery-mode.patch
Patch10:        grub2-fix-error-terminal-gfxterm-isn-t-found.patch
Patch12:        grub2-fix-menu-in-xen-host-server.patch
Patch15:        not-display-menu-when-boot-once.patch
Patch17:        grub2-pass-corret-root-for-nfsroot.patch
Patch19:        grub2-efi-HP-workaround.patch
Patch21:        grub2-secureboot-add-linuxefi.patch
Patch23:        grub2-secureboot-no-insmod-on-sb.patch
Patch25:        grub2-secureboot-chainloader.patch
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
Patch84:        grub2-s390x-09-improve-zipl-setup.patch
Patch85:        grub2-getroot-scan-disk-pv.patch
Patch92:        grub2-util-30_os-prober-multiple-initrd.patch
Patch93:        grub2-getroot-support-nvdimm.patch
Patch94:        grub2-install-fix-not-a-directory-error.patch
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
Patch233:       0001-osdep-Introduce-include-grub-osdep-major.h-and-use-i.patch
Patch234:       0002-osdep-linux-hostdisk-Use-stat-instead-of-udevadm-for.patch
Patch236:       grub2-efi_gop-avoid-low-resolution.patch
# Support HTTP Boot IPv4 and IPv6 (fate#320129)
Patch281:       0002-net-read-bracketed-ipv6-addrs-and-port-numbers.patch
Patch282:       0003-bootp-New-net_bootp6-command.patch
Patch283:       0004-efinet-UEFI-IPv6-PXE-support.patch
Patch284:       0005-grub.texi-Add-net_bootp6-doument.patch
Patch285:       0006-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch286:       0007-efinet-Setting-network-from-UEFI-device-path.patch
Patch287:       0008-efinet-Setting-DNS-server-from-UEFI-protocol.patch
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
Patch714:       0001-kern-mm.c-Make-grub_calloc-inline.patch
Patch716:       0002-cmdline-Provide-cmdline-functions-as-module.patch
# bsc#1172745 L3: SLES 12 SP4 - Slow boot of system after updated kernel -
# takes 45 minutes after grub to start loading kernel
Patch717:       0001-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch718:       0002-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch719:       0001-Unify-the-check-to-enable-btrfs-relative-path.patch
Patch721:       0001-efi-linux-provide-linux-command.patch
# Secure Boot support in GRUB on aarch64 (jsc#SLE-15864)
Patch730:       0001-Add-support-for-Linux-EFI-stub-loading-on-aarch64.patch
Patch731:       0002-arm64-make-sure-fdt-has-address-cells-and-size-cells.patch
Patch732:       0003-Make-grub_error-more-verbose.patch
Patch733:       0004-arm-arm64-loader-Better-memory-allocation-and-error-.patch
Patch735:       0006-efi-Set-image-base-address-before-jumping-to-the-PE-.patch
Patch739:       0001-Fix-build-error-in-binutils-2.36.patch
Patch740:       0001-emu-fix-executable-stack-marking.patch
Patch784:       0044-squash-kern-Add-lockdown-support.patch
Patch786:       0046-squash-verifiers-Move-verifiers-API-to-kernel-image.patch
Patch788:       0001-ieee1275-Avoiding-many-unecessary-open-close.patch
Patch789:       0001-Workaround-volatile-efi-boot-variable.patch
Patch790:       0001-30_uefi-firmware-fix-printf-format-with-null-byte.patch
Patch792:       0001-templates-Follow-the-path-of-usr-merged-kernel-confi.patch
Patch793:       0001-tpm-Pass-unknown-error-as-non-fatal-but-debug-print-.patch
Patch794:       0001-Filter-out-POSIX-locale-for-translation.patch
Patch795:       0001-ieee1275-implement-FCP-methods-for-WWPN-and-LUNs.patch
Patch796:       0001-disk-diskfilter-Use-nodes-in-logical-volume-s-segmen.patch
Patch797:       0001-fs-xfs-Fix-unreadable-filesystem-with-v4-superblock.patch
Patch798:       0001-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch799:       0002-Arm-check-for-the-PE-magic-for-the-compiled-arch.patch
Patch800:       0001-fs-btrfs-Make-extent-item-iteration-to-handle-gaps.patch
Patch801:       0001-Factor-out-grub_efi_linux_boot.patch
Patch802:       0002-Fix-race-in-EFI-validation.patch
Patch803:       0003-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
Patch804:       0004-Try-to-pick-better-locations-for-kernel-and-initrd.patch
Patch805:       0005-x86-efi-Use-bounce-buffers-for-reading-to-addresses-.patch
Patch806:       0006-x86-efi-Re-arrange-grub_cmd_linux-a-little-bit.patch
Patch807:       0007-x86-efi-Make-our-own-allocator-for-kernel-stuff.patch
Patch808:       0008-x86-efi-Allow-initrd-params-cmdline-allocations-abov.patch
Patch809:       0009-x86-efi-Reduce-maximum-bounce-buffer-size-to-16-MiB.patch
Patch810:       0010-efilinux-Fix-integer-overflows-in-grub_cmd_initrd.patch
Patch811:       0011-Also-define-GRUB_EFI_MAX_ALLOCATION_ADDRESS-for-RISC.patch
Patch812:       0001-grub-mkconfig-restore-umask-for-grub.cfg.patch
Patch813:       0001-ieee1275-Drop-HEAP_MAX_ADDR-and-HEAP_MIN_SIZE-consta.patch
Patch814:       0002-ieee1275-claim-more-memory.patch
Patch815:       0003-ieee1275-request-memory-with-ibm-client-architecture.patch
Patch816:       0004-Add-suport-for-signing-grub-with-an-appended-signatu.patch
Patch817:       0005-docs-grub-Document-signing-grub-under-UEFI.patch
Patch818:       0006-docs-grub-Document-signing-grub-with-an-appended-sig.patch
Patch819:       0007-dl-provide-a-fake-grub_dl_set_persistent-for-the-emu.patch
Patch820:       0008-pgp-factor-out-rsa_pad.patch
Patch821:       0009-crypto-move-storage-for-grub_crypto_pk_-to-crypto.c.patch
Patch822:       0010-posix_wrap-tweaks-in-preparation-for-libtasn1.patch
Patch823:       0011-libtasn1-import-libtasn1-4.18.0.patch
Patch824:       0012-libtasn1-disable-code-not-needed-in-grub.patch
Patch825:       0013-libtasn1-changes-for-grub-compatibility.patch
Patch826:       0014-libtasn1-compile-into-asn1-module.patch
Patch827:       0015-test_asn1-test-module-for-libtasn1.patch
Patch828:       0016-grub-install-support-embedding-x509-certificates.patch
Patch829:       0017-appended-signatures-import-GNUTLS-s-ASN.1-descriptio.patch
Patch830:       0018-appended-signatures-parse-PKCS-7-signedData-and-X.50.patch
Patch831:       0019-appended-signatures-support-verifying-appended-signa.patch
Patch832:       0020-appended-signatures-verification-tests.patch
Patch833:       0021-appended-signatures-documentation.patch
Patch834:       0022-ieee1275-enter-lockdown-based-on-ibm-secure-boot.patch
Patch835:       0023-x509-allow-Digitial-Signature-plus-other-Key-Usages.patch
Patch836:       0001-grub-install-Add-SUSE-signed-image-support-for-power.patch
Patch837:       0001-Add-grub_envblk_buf-helper-function.patch
Patch838:       0002-Add-grub_disk_write_tail-helper-function.patch
Patch839:       0003-grub-install-support-prep-environment-block.patch
Patch840:       0004-Introduce-prep_load_env-command.patch
Patch841:       0005-export-environment-at-start-up.patch
Patch842:       0001-grub-install-bailout-root-device-probing.patch
Patch843:       0001-RISC-V-Adjust-march-flags-for-binutils-2.38.patch
Patch844:       0001-install-fix-software-raid1-on-esp.patch
Patch845:       0001-mkimage-Fix-dangling-pointer-may-be-used-error.patch
Patch846:       0002-Fix-Werror-array-bounds-array-subscript-0-is-outside.patch
Patch847:       0003-reed_solomon-Fix-array-subscript-0-is-outside-array-.patch
Patch848:       0001-grub-probe-Deduplicate-probed-partmap-output.patch
Patch849:       0001-powerpc-do-CAS-in-a-more-compatible-way.patch
Patch850:       0001-Fix-infinite-boot-loop-on-headless-system-in-qemu.patch
Patch851:       0001-libc-config-merge-from-glibc.patch
Patch852:       0001-ofdisk-improve-boot-time-by-lookup-boot-disk-first.patch
Patch853:       0001-video-Remove-trailing-whitespaces.patch
Patch854:       0002-loader-efi-chainloader-Simplify-the-loader-state.patch
Patch855:       0003-commands-boot-Add-API-to-pass-context-to-loader.patch
Patch856:       0004-loader-efi-chainloader-Use-grub_loader_set_ex.patch
Patch857:       0005-kern-efi-sb-Reject-non-kernel-files-in-the-shim_lock.patch
Patch858:       0006-kern-file-Do-not-leak-device_name-on-error-in-grub_f.patch
Patch859:       0007-video-readers-png-Abort-sooner-if-a-read-operation-f.patch
Patch860:       0008-video-readers-png-Refuse-to-handle-multiple-image-he.patch
Patch861:       0009-video-readers-png-Drop-greyscale-support-to-fix-heap.patch
Patch862:       0010-video-readers-png-Avoid-heap-OOB-R-W-inserting-huff-.patch
Patch863:       0011-video-readers-png-Sanity-check-some-huffman-codes.patch
Patch864:       0012-video-readers-jpeg-Abort-sooner-if-a-read-operation-.patch
Patch865:       0013-video-readers-jpeg-Do-not-reallocate-a-given-huff-ta.patch
Patch866:       0014-video-readers-jpeg-Refuse-to-handle-multiple-start-o.patch
Patch867:       0015-video-readers-jpeg-Block-int-underflow-wild-pointer-.patch
Patch868:       0016-normal-charset-Fix-array-out-of-bounds-formatting-un.patch
Patch869:       0017-net-ip-Do-IP-fragment-maths-safely.patch
Patch870:       0018-net-netbuff-Block-overly-large-netbuff-allocs.patch
Patch871:       0019-net-dns-Fix-double-free-addresses-on-corrupt-DNS-res.patch
Patch872:       0020-net-dns-Don-t-read-past-the-end-of-the-string-we-re-.patch
Patch873:       0021-net-tftp-Prevent-a-UAF-and-double-free-from-a-failed.patch
Patch874:       0022-net-tftp-Avoid-a-trivial-UAF.patch
Patch875:       0023-net-http-Do-not-tear-down-socket-if-it-s-already-bee.patch
Patch876:       0024-net-http-Fix-OOB-write-for-split-http-headers.patch
Patch877:       0025-net-http-Error-out-on-headers-with-LF-without-CR.patch
Patch878:       0026-fs-f2fs-Do-not-read-past-the-end-of-nat-journal-entr.patch
Patch879:       0027-fs-f2fs-Do-not-read-past-the-end-of-nat-bitmap.patch
Patch880:       0028-fs-f2fs-Do-not-copy-file-names-that-are-too-long.patch
Patch881:       0029-fs-btrfs-Fix-several-fuzz-issues-with-invalid-dir-it.patch
Patch882:       0030-fs-btrfs-Fix-more-ASAN-and-SEGV-issues-found-with-fu.patch
Patch883:       0031-fs-btrfs-Fix-more-fuzz-issues-related-to-chunks.patch
Patch884:       0032-Use-grub_loader_set_ex-for-secureboot-chainloader.patch
Patch885:       0001-luks2-Add-debug-message-to-align-with-luks-and-geli-.patch
Patch886:       0002-cryptodisk-Refactor-to-discard-have_it-global.patch
Patch887:       0003-cryptodisk-Return-failure-in-cryptomount-when-no-cry.patch
Patch888:       0004-cryptodisk-Improve-error-messaging-in-cryptomount-in.patch
Patch889:       0005-cryptodisk-Improve-cryptomount-u-error-message.patch
Patch890:       0006-cryptodisk-Add-infrastructure-to-pass-data-from-cryp.patch
Patch891:       0007-cryptodisk-Refactor-password-input-out-of-crypto-dev.patch
Patch892:       0008-cryptodisk-Move-global-variables-into-grub_cryptomou.patch
Patch893:       0009-cryptodisk-Improve-handling-of-partition-name-in-cry.patch
Patch894:       0010-protectors-Add-key-protectors-framework.patch
Patch895:       0011-tpm2-Add-TPM-Software-Stack-TSS.patch
Patch896:       0012-protectors-Add-TPM2-Key-Protector.patch
Patch897:       0013-cryptodisk-Support-key-protectors.patch
Patch898:       0014-util-grub-protect-Add-new-tool.patch
Patch899:       fix-tpm2-build.patch
Patch900:       0001-crytodisk-fix-cryptodisk-module-looking-up.patch
# fde
Patch901:       0001-devmapper-getroot-Have-devmapper-recognize-LUKS2.patch
Patch902:       0002-devmapper-getroot-Set-up-cheated-LUKS2-cryptodisk-mo.patch
Patch903:       0003-disk-cryptodisk-When-cheatmounting-use-the-sector-in.patch
Patch904:       0004-normal-menu-Don-t-show-Booting-s-msg-when-auto-booti.patch
Patch905:       0005-EFI-suppress-the-Welcome-to-GRUB-message-in-EFI-buil.patch
Patch906:       0006-EFI-console-Do-not-set-colorstate-until-the-first-te.patch
Patch907:       0007-EFI-console-Do-not-set-cursor-until-the-first-text-o.patch
Patch908:       0008-linuxefi-Use-common-grub_initrd_load.patch
Patch909:       0009-Add-crypttab_entry-to-obviate-the-need-to-input-pass.patch
Patch910:       0010-templates-import-etc-crypttab-to-grub.cfg.patch
Patch911:       grub-read-pcr.patch
Patch912:       efi-set-variable-with-attrs.patch
Patch913:       tpm-record-pcrs.patch
Patch914:       tpm-protector-dont-measure-sealed-key.patch
Patch915:       tpm-protector-export-secret-key.patch
Patch916:       grub-install-record-pcrs.patch
Patch917:       grub-unseal-debug.patch
# efi mm
Patch918:       0001-tpm-Disable-tpm-verifier-if-tpm-is-not-present.patch
Patch919:       0001-mm-Allow-dynamically-requesting-additional-memory-re.patch
Patch920:       0002-kern-efi-mm-Always-request-a-fixed-number-of-pages-o.patch
Patch921:       0003-kern-efi-mm-Extract-function-to-add-memory-regions.patch
Patch922:       0004-kern-efi-mm-Pass-up-errors-from-add_memory_regions.patch
Patch923:       0005-kern-efi-mm-Implement-runtime-addition-of-pages.patch
Patch924:       0001-kern-efi-mm-Enlarge-the-default-heap-size.patch
Patch925:       0002-mm-Defer-the-disk-cache-invalidation.patch
# powerpc-ieee1275
Patch926:       0001-grub-install-set-point-of-no-return-for-powerpc-ieee1275.patch
Patch927:       safe_tpm_pcr_snapshot.patch
# (PED-996) NVMeoFC support on Grub (grub2)
Patch929:       0001-ieee1275-add-support-for-NVMeoFC.patch
Patch930:       0002-ieee1275-ofpath-enable-NVMeoF-logical-device-transla.patch
Patch931:       0003-ieee1275-change-the-logic-of-ieee1275_get_devargs.patch
Patch932:       0004-ofpath-controller-name-update.patch
# (PED-1265) TDX: Enhance grub2 measurement to TD RTMR
Patch933:       0001-commands-efi-tpm-Refine-the-status-of-log-event.patch
Patch934:       0002-commands-efi-tpm-Use-grub_strcpy-instead-of-grub_mem.patch
Patch935:       0003-efi-tpm-Add-EFI_CC_MEASUREMENT_PROTOCOL-support.patch
# (PED-1990) GRUB2: Measure the kernel on POWER10 and extend TPM PCRs
Patch936:       0001-ibmvtpm-Add-support-for-trusted-boot-using-a-vTPM-2..patch
Patch937:       0002-ieee1275-implement-vec5-for-cas-negotiation.patch
Patch938:       0001-font-Reject-glyphs-exceeds-font-max_glyph_width-or-f.patch
Patch939:       0002-font-Fix-size-overflow-in-grub_font_get_glyph_intern.patch
Patch940:       0003-font-Fix-several-integer-overflows-in-grub_font_cons.patch
Patch941:       0004-font-Remove-grub_font_dup_glyph.patch
Patch942:       0005-font-Fix-integer-overflow-in-ensure_comb_space.patch
Patch943:       0006-font-Fix-integer-overflow-in-BMP-index.patch
Patch944:       0007-font-Fix-integer-underflow-in-binary-search-of-char-.patch
Patch945:       0008-fbutil-Fix-integer-overflow.patch
Patch946:       0009-font-Fix-an-integer-underflow-in-blit_comb.patch
Patch947:       0010-font-Harden-grub_font_blit_glyph-and-grub_font_blit_.patch
Patch948:       0011-font-Assign-null_font-to-glyphs-in-ascii_font_glyph.patch
Patch949:       0012-normal-charset-Fix-an-integer-overflow-in-grub_unico.patch
Patch950:       0001-fs-btrfs-Use-full-btrfs-bootloader-area.patch
Patch951:       0002-Mark-environmet-blocks-as-used-for-image-embedding.patch
Patch952:       0001-ieee1275-Increase-initially-allocated-heap-from-1-4-.patch
Patch953:       grub2-increase-crypttab-path-buffer.patch
Patch954:       0001-grub2-Set-multiple-device-path-for-a-nvmf-boot-devic.patch

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
CD_MODULES="${CD_MODULES} chain efifwsetup efinet read tpm tpm2"
PXE_MODULES="${PXE_MODULES} efinet"
%else
CD_MODULES="${CD_MODULES} net"
PXE_MODULES="${PXE_MODULES} net"
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

./grub-mkimage -O %{grubefiarch} -o grub.efi --prefix= %{?sbat_generation:--sbat sbat.csv} \
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

regexp --set 1:bdev --set 2:bpart --set 3:bpath '\(([^,]+)(,?.*)?\)(.*)' "$cmdpath"

echo "bdev=$bdev"
echo "bpart=$bpart"
echo "bpath=$bpath"

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

if [ "$ENV_CRYPTO_UUID" ]; then
  cryptomount -u "$ENV_CRYPTO_UUID"
fi

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
%ifarch  %{ix86} x86_64
install -m 755 -D %{SOURCE19} %{buildroot}/%{_libexecdir}/grub2-instdev-fixup.pl
%endif

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
%doc AUTHORS
%doc NEWS README
%doc THANKS TODO ChangeLog
%doc docs/autoiso.cfg docs/osdetect.cfg
%ifarch s390x
%doc README.ibm3215
%endif
%dir /boot/%{name}
%ghost %attr(600, root, root) /boot/%{name}/grub.cfg
%{_sysconfdir}/bash_completion.d/grub
%config(noreplace) %{_sysconfdir}/default/grub
%dir %{_sysconfdir}/grub.d
%{_sysconfdir}/grub.d/README
%config(noreplace) %{_sysconfdir}/grub.d/00_header
%config(noreplace) %{_sysconfdir}/grub.d/05_crypttab
%config(noreplace) %{_sysconfdir}/grub.d/10_linux
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_xen
%config(noreplace) %{_sysconfdir}/grub.d/30_uefi-firmware
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
%{_bindir}/%{name}-protect
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
%{_datadir}/%{name}/%{grubarch}/gmodule.pl
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
