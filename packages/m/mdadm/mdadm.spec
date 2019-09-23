#
# spec file for package mdadm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
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
Url:            http://www.kernel.org/pub/linux/utils/raid/mdadm/
Summary:        Utility for configuring "MD" software RAID devices
License:        GPL-2.0-only
Group:          System/Base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         https://www.kernel.org/pub/linux/utils/raid/mdadm/%{name}-%{version}.tar.xz
Source1:        Software-RAID.HOWTO.tar.bz2
Source2:        sysconfig.mdadm
Patch1:         0001-Makefile-install-mdadm_env.sh-to-usr-lib-mdadm.patch
Patch11:        0001-Document-PART-POLICY-lines.patch
Patch12:        0002-policy-support-devices-with-multiple-paths.patch
Patch13:        0003-mdcheck-add-systemd-unit-files-to-run-mdcheck.patch
Patch14:        0004-Monitor-add-system-timer-to-run-oneshot-periodically.patch
Patch15:        0005-imsm-update-metadata-correctly-while-raid10-double-d.patch
Patch16:        0006-Grow-avoid-overflow-in-compute_backup_blocks.patch
Patch17:        0007-Grow-report-correct-new-chunk-size.patch
Patch18:        0008-policy.c-prevent-NULL-pointer-referencing.patch
Patch19:        0009-Detail.c-do-not-skip-first-character-when-calling-xs.patch
Patch20:        0010-imsm-finish-recovery-when-drive-with-rebuild-fails.patch
Patch21:        0011-mdmon-don-t-attempt-to-manage-new-arrays-when-termin.patch
Patch1001:      1001-display-timeout-status.patch
%define _udevdir %(pkg-config --variable=udevdir udev)
%define _systemdshutdowndir %{_unitdir}/../system-shutdown

%description
mdadm is a program that can be used to control Linux md devices.

%prep
%setup -q -a1
%patch1 -p1
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
%patch1001 -p1

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
%service_del_preun %services mdmon@.service mdadm-last-resort@.service mdadm-grow-continue@.service

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
%dir %{_libexecdir}/mdadm
%{_libexecdir}/mdadm/mdadm_env.sh

%changelog
