#
# spec file for package mdadm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           mdadm
Version:        4.2
Release:        0
BuildRequires:  binutils-devel
BuildRequires:  groff
BuildRequires:  pkgconfig
BuildRequires:  sgmltool
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
PreReq:         %fillup_prereq
PreReq:         coreutils
Recommends:     smtp_daemon
URL:            http://www.kernel.org/pub/linux/utils/raid/mdadm/
Summary:        Utility for configuring "MD" software RAID devices
License:        GPL-2.0-only
Group:          System/Base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         https://www.kernel.org/pub/linux/utils/raid/mdadm/%{name}-%{version}.tar.xz
Source1:        Software-RAID.HOWTO.tar.bz2
Source2:        sysconfig.mdadm
Patch1:         0001-Unify-error-message.patch
Patch2:         0002-mdadm-Fix-double-free.patch
Patch3:         0003-Grow_reshape-Add-r0-grow-size-error-message-and-upda.patch
Patch4:         0004-udev-adapt-rules-to-systemd-v247.patch
Patch5:         0005-Replace-error-prone-signal-with-sigaction.patch
Patch6:         0006-mdadm-Respect-config-file-location-in-man.patch
Patch7:         0007-mdadm-Update-ReadMe.patch
Patch8:         0008-mdadm-Update-config-man-regarding-default-files-and-.patch
Patch9:         0009-mdadm-Update-config-manual.patch
Patch10:        0010-Create-Build-use-default_layout.patch
Patch11:        0011-mdadm-add-map_num_s.patch
Patch12:        0012-mdmon-Stop-parsing-duplicate-options.patch
Patch13:        0013-Grow-block-n-on-external-volumes.patch
Patch14:        0014-Incremental-Fix-possible-memory-and-resource-leaks.patch
Patch15:        0015-Mdmonitor-Fix-segfault.patch
Patch16:        0016-Mdmonitor-Improve-logging-method.patch
Patch17:        0017-Fix-possible-NULL-ptr-dereferences-and-memory-leaks.patch
Patch18:        0018-imsm-Remove-possibility-for-get_imsm_dev-to-return-N.patch
Patch19:        0019-Revert-mdadm-fix-coredump-of-mdadm-monitor-r.patch
Patch20:        0020-util-replace-ioctl-use-with-function.patch
Patch21:        0021-mdadm-super1-restore-commit-45a87c2f31335-to-fix-clu.patch
Patch22:        0022-imsm-introduce-get_disk_slot_in_dev.patch
Patch23:        0023-imsm-use-same-slot-across-container.patch
Patch24:        0024-imsm-block-changing-slots-during-creation.patch
Patch25:        0025-mdadm-block-update-ppl-for-non-raid456-levels.patch
Patch26:        0026-mdadm-Fix-array-size-mismatch-after-grow.patch
Patch27:        0027-mdadm-Remove-dead-code-in-imsm_fix_size_mismatch.patch
Patch28:        0028-Monitor-use-devname-as-char-array-instead-of-pointer.patch
Patch29:        0029-Monitor-use-snprintf-to-fill-device-name.patch
Patch30:        0030-Makefile-Don-t-build-static-build-with-everything-an.patch
Patch31:        0031-DDF-Cleanup-validate_geometry_ddf_container.patch
Patch32:        0032-DDF-Fix-NULL-pointer-dereference-in-validate_geometr.patch
Patch33:        0033-mdadm-Grow-Fix-use-after-close-bug-by-closing-after-.patch
Patch34:        0034-monitor-Avoid-segfault-when-calling-NULL-get_bad_blo.patch
Patch35:        0035-mdadm-Fix-mdadm-r-remove-option-regression.patch
Patch36:        0036-mdadm-Fix-optional-write-behind-parameter.patch
Patch37:        0037-mdadm-Replace-obsolete-usleep-with-nanosleep.patch
Patch38:        0038-mdadm-remove-symlink-option.patch
Patch39:        0039-mdadm-move-data_offset-to-struct-shape.patch
Patch40:        0040-mdadm-Don-t-open-md-device-for-CREATE-and-ASSEMBLE.patch
Patch41:        0041-Grow-Split-Grow_reshape-into-helper-function.patch
Patch42:        0042-Assemble-check-if-device-is-container-before-schedul.patch
Patch43:        0043-super1-report-truncated-device.patch
Patch44:        0044-mdadm-Correct-typos-punctuation-and-grammar-in-man.patch
Patch46:        0046-Monitor-Fix-statelist-memory-leaks.patch
Patch47:        0047-mdadm-added-support-for-Intel-Alderlake-RST-on-VMD-p.patch
Patch48:        0048-mdadm-Add-Documentation-entries-to-systemd-services.patch
Patch49:        0049-ReadMe-fix-command-line-help.patch
Patch50:        0050-mdadm-replace-container-level-checking-with-inline.patch
Patch51:        0051-Mdmonitor-Omit-non-md-devices.patch
Patch1001:      1001-display-timeout-status.patch
Patch1002:      1002-OnCalendar-format-fix-of-mdcheck_start-timer.patch
Patch1003:      1003-mdadm-treat-the-Dell-softraid-array-as-local-array.patch
Patch1004:      1004-call-mdadm_env.sh-from-usr-libexec-mdadm.patch
Patch1005:      1005-mdadm-enable-Intel-Alderlake-RSTe-configuration.patch
%define _udevdir %(pkg-config --variable=udevdir udev)
%define _systemdshutdowndir %{_unitdir}/../system-shutdown

%description
mdadm is a program that can be used to control Linux md devices.

%prep
%setup -q -a1
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
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1

%build
make %{?_smp_mflags} CC="%__cc" CXFLAGS="%{optflags} -Wno-error" EXTRAVERSION="%{release}" SUSE=yes BINDIR=%{_sbindir}
cd Software-RAID.HOWTO
sgml2html Software-RAID.HOWTO.sgml
sgml2txt Software-RAID.HOWTO.sgml

%install
%make_install install-systemd install-udev SYSTEMD_DIR=%{_unitdir} UDEVDIR=%{_udevdir} SUSE=yes BINDIR=%{_sbindir}
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
%{_sbindir}/*
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
%dir %{_prefix}/libexec/
%dir %{_prefix}/libexec/mdadm
%{_prefix}/libexec/mdadm/mdadm_env.sh

%changelog
