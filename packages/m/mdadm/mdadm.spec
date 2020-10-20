#
# spec file for package mdadm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           mdadm
Version:        4.1
Release:        0
BuildRequires:  binutils-devel
BuildRequires:  groff
BuildRequires:  pkgconfig
BuildRequires:  sgmltool
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
PreReq:         %fillup_prereq /sbin/mkinitrd coreutils
Recommends:     smtp_daemon
URL:            http://www.kernel.org/pub/linux/utils/raid/mdadm/
Summary:        Utility for configuring "MD" software RAID devices
License:        GPL-2.0-only
Group:          System/Base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         https://www.kernel.org/pub/linux/utils/raid/mdadm/%{name}-%{version}.tar.xz
Source1:        Software-RAID.HOWTO.tar.bz2
Source2:        sysconfig.mdadm
Patch0:         0000-Makefile-install-mdadm_env.sh-to-usr-lib-mdadm.patch
Patch1:         0001-Assemble-keep-MD_DISK_FAILFAST-and-MD_DISK_WRITEMOST.patch
Patch2:         0002-Document-PART-POLICY-lines.patch
Patch3:         0003-policy-support-devices-with-multiple-paths.patch
Patch4:         0004-mdcheck-add-systemd-unit-files-to-run-mdcheck.patch
Patch5:         0005-Monitor-add-system-timer-to-run-oneshot-periodically.patch
Patch6:         0006-imsm-update-metadata-correctly-while-raid10-double-d.patch
Patch7:         0007-Assemble-mask-FAILFAST-and-WRITEMOSTLY-flags-when-fi.patch
Patch8:         0008-Grow-avoid-overflow-in-compute_backup_blocks.patch
Patch9:         0009-Grow-report-correct-new-chunk-size.patch
Patch10:        0010-policy.c-prevent-NULL-pointer-referencing.patch
Patch11:        0012-policy.c-Fix-for-compiler-error.patch
Patch12:        0013-imsm-finish-recovery-when-drive-with-rebuild-fails.patch
Patch13:        0014-imsm-fix-reshape-for-2TB-drives.patch
Patch14:        0015-Fix-spelling-typos.patch
Patch15:        0016-Detail.c-do-not-skip-first-character-when-calling-xs.patch
Patch16:        0018-Fix-reshape-for-decreasing-data-offset.patch
Patch17:        0019-mdadm-tests-add-one-test-case-for-failfast-of-raid1.patch
Patch18:        0020-mdmon-don-t-attempt-to-manage-new-arrays-when-termin.patch
Patch19:        0021-mdmon-wait-for-previous-mdmon-to-exit-during-takeove.patch
Patch20:        0022-Assemble-Fix-starting-array-with-initial-reshape-che.patch
Patch21:        0023-add-missing-units-to-examine.patch
Patch22:        0024-imsm-fix-spare-activation-for-old-matrix-arrays.patch
Patch23:        0025-Create-Block-rounding-size-to-max.patch
Patch24:        0026-udev-Add-udev-rules-to-create-by-partuuid-for-md-dev.patch
Patch25:        0027-mdmon-fix-wrong-array-state-when-disk-fails-during-m.patch
Patch26:        0028-Enable-probe_roms-to-scan-more-than-6-roms.patch
Patch27:        0029-super-intel-Fix-issue-with-abs-being-irrelevant.patch
Patch28:        0030-mdadm.h-Introduced-unaligned-get-put-_unaligned-16-3.patch
Patch29:        0031-super-intel-Use-put_unaligned-in-split_ull.patch
Patch30:        0032-mdadm-load-default-sysfs-attributes-after-assemblati.patch
Patch31:        0033-mdadm.h-include-sysmacros.h-unconditionally.patch
Patch32:        0034-mdadm-add-no-devices-to-avoid-component-devices-deta.patch
Patch33:        0035-udev-add-no-devices-option-for-calling-mdadm-detail.patch
Patch34:        0036-imsm-close-removed-drive-fd.patch
Patch35:        0037-mdadm-check-value-returned-by-snprintf-against-error.patch
Patch36:        0038-mdadm-Introduce-new-array-state-broken-for-raid0-lin.patch
Patch37:        0039-mdadm-force-a-uuid-swap-on-big-endian.patch
Patch38:        0040-mdadm-md.4-add-the-descriptions-for-bitmap-sysfs-nod.patch
Patch39:        0041-Init-devlist-as-an-array.patch
Patch40:        0042-Don-t-need-to-check-recovery-after-re-add-when-no-I-.patch
Patch41:        0043-udev-allow-for-udev-attribute-reading-bug.patch
Patch42:        0044-imsm-save-current_vol-number.patch
Patch43:        0045-imsm-allow-to-specify-second-volume-size.patch
Patch44:        0046-mdcheck-when-mdcheck_start-is-enabled-enable-mdcheck.patch
Patch45:        0050-mdcheck-use-to-pass-variable-to-mdcheck.patch
Patch46:        0051-SUSE-mdadm_env.sh-handle-MDADM_CHECK_DURATION.patch
Patch47:        0052-super-intel-don-t-mark-structs-packed-unnecessarily.patch
Patch48:        0053-Manage-Remove-the-legacy-code-for-md-driver-prior-to.patch
Patch49:        0054-Remove-last-traces-of-HOT_ADD_DISK.patch
Patch50:        0055-Fix-up-a-few-formatting-issues.patch
Patch51:        0056-Remove-unused-code.patch
Patch52:        0057-imsm-return-correct-uuid-for-volume-in-detail.patch
Patch53:        0058-imsm-Change-the-way-of-printing-nvme-drives-in-detai.patch
Patch54:        0059-Create-add-support-for-RAID0-layouts.patch
Patch55:        0060-Assemble-add-support-for-RAID0-layouts.patch
Patch56:        0061-Respect-CROSS_COMPILE-when-CC-is-the-default.patch
Patch57:        0062-Change-warning-message.patch
Patch58:        0063-mdcheck-service-can-t-start-succesfully-because-of-s.patch
Patch59:        0064-imsm-Update-grow-manual.patch
Patch60:        0065-Add-support-for-Tebibytes.patch
Patch61:        0066-imsm-fill-working_disks-according-to-metadata.patch
Patch62:        0067-mdadm.8-add-note-information-for-raid0-growing-opera.patch
Patch63:        0068-Remove-the-legacy-whitespace.patch
Patch64:        0069-imsm-pass-subarray-id-to-kill_subarray-function.patch
Patch65:        0070-imsm-Remove-dump-restore-implementation.patch
Patch66:        0071-Monitor-improve-check_one_sharer-for-checking-duplic.patch
Patch67:        0072-Detail-adding-sync-status-for-cluster-device.patch
Patch73:        0073-imsm-Correct-minimal-device-size.patch
Patch74:        0074-Detail-show-correct-bitmap-info-for-cluster-raid-dev.patch
Patch75:        0075-imsm-support-the-Array-Creation-Time-field-in-metada.patch
Patch76:        0076-imsm-show-Subarray-and-Volume-ID-in-examine-output.patch
Patch77:        0077-udev-Ignore-change-event-for-imsm.patch
Patch78:        0078-Manage-imsm-Write-metadata-before-add.patch
Patch79:        0079-Assemble-print-error-message-if-mdadm-fails-assembli.patch
Patch80:        0080-clean-up-meaning-of-small-typo.patch
Patch81:        0081-Assemble.c-respect-force-flag.patch
Patch82:        0082-mdcheck-Log-when-done.patch
Patch83:        0083-Makefile-add-EXTRAVERSION-support.patch
Patch84:        0084-uuid.c-split-uuid-stuffs-from-util.c.patch
Patch85:        0085-Include-count-for-0-character-when-using-strncpy-to-.patch
Patch86:        0086-restripe-fix-ignoring-return-value-of-read-and-lseek.patch
Patch87:        0087-Block-overwriting-existing-links-while-manual-assemb.patch
Patch88:        0088-Detect-too-small-device-error-rather-than-underflow-.patch
Patch89:        0089-Use-more-secure-HTTPS-URLs.patch
Patch90:        0090-Update-link-to-Intel-page-for-IMSM.patch
Patch91:        0091-mdadm-Grow-prevent-md-s-fd-from-being-occupied-durin.patch
Patch92:        0092-Specify-nodes-number-when-updating-cluster-nodes.patch
Patch93:        0093-mdadm-md.4-update-path-to-in-kernel-tree-documentati.patch
Patch94:        0094-manual-update-examine-badblocks.patch
Patch1001:      1001-display-timeout-status.patch
Patch1002:      1002-OnCalendar-format-fix-of-mdcheck_start-timer.patch
Patch1003:      1003-mdadm-treat-the-Dell-softraid-array-as-local-array.patch
%define _udevdir %(pkg-config --variable=udevdir udev)
%define _systemdshutdowndir %{_unitdir}/../system-shutdown

%description
mdadm is a program that can be used to control Linux md devices.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch73 -p1
%patch74 -p1
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
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1

%build
make %{?_smp_mflags} CC="%__cc" CXFLAGS="%{optflags} -Wno-error" SUSE=yes
cd Software-RAID.HOWTO
sgml2html Software-RAID.HOWTO.sgml
sgml2txt Software-RAID.HOWTO.sgml

%install
%make_install install-systemd install-udev SYSTEMD_DIR=%{_unitdir} UDEVDIR=%{_udevdir} SUSE=yes
rm -rf %{buildroot}/lib/udev
install -d %{buildroot}%{_fillupdir}
install -d %{buildroot}/usr/share/mdadm
install -m 755 misc/mdcheck %{buildroot}/usr/share/mdadm/mdcheck
install -m 644 %{S:2} %{buildroot}%{_fillupdir}/
install -d %{buildroot}%{_systemdshutdowndir}
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcmdmonitor

%define services mdmonitor.service mdcheck_start.service mdcheck_continue.service mdmonitor-oneshot.service

%pre
%service_add_pre %services

%post
%service_add_post %services
%{?regenerate_initrd_post}
%fillup_only

%preun
%service_del_preun %services

%postun
%service_del_postun %services
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README.initramfs TODO mdadm.conf-example mkinitramfs
%doc Software-RAID.HOWTO/Software-RAID.HOWTO*{.txt,.html}
%doc %{_mandir}/man?/*
/sbin/*
%{_sbindir}/rcmdmonitor
%dir /usr/share/mdadm
/usr/share/mdadm/*
%{_fillupdir}/sysconfig.mdadm
%{_udevdir}/rules.d/01-md-raid-creating.rules
%{_udevdir}/rules.d/63-md-raid-arrays.rules
%{_udevdir}/rules.d/64-md-raid-assembly.rules
%{_udevdir}/rules.d/69-md-clustered-confirm-device.rules
# %%{_systemdshutdowndir}/ is not owned by all versions of systemd-mini.
# But we really do not want to pull in a full systemd, so we rather just own
# that directory by ourselves too. After all, this is allowed.
%dir %{_systemdshutdowndir}
%{_systemdshutdowndir}/mdadm.shutdown
%{_unitdir}/mdmon@.service
%{_unitdir}/mdmonitor.service
%{_unitdir}/mdadm-last-resort@.timer
%{_unitdir}/mdadm-last-resort@.service
%{_unitdir}/mdadm-grow-continue@.service
%{_unitdir}/mdcheck_continue.service
%{_unitdir}/mdcheck_continue.timer
%{_unitdir}/mdcheck_start.service
%{_unitdir}/mdcheck_start.timer
%{_unitdir}/mdmonitor-oneshot.service
%{_unitdir}/mdmonitor-oneshot.timer
%dir %{_prefix}/lib/mdadm
%{_prefix}/lib/mdadm/mdadm_env.sh

%changelog
