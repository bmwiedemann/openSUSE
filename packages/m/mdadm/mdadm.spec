#
# spec file for package mdadm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           mdadm
Version:        4.3
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
URL:            http://www.kernel.org/pub/linux/utils/raid/mdadm/
Summary:        Utility for configuring "MD" software RAID devices
License:        GPL-2.0-only
Group:          System/Base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         https://www.kernel.org/pub/linux/utils/raid/mdadm/%{name}-%{version}.tar.xz
Source1:        Software-RAID.HOWTO.tar.bz2
Source2:        sysconfig.mdadm
Patch1:         0001-Remove-hardcoded-checkpoint-interval-checking.patch
Patch2:         0002-monitor-refactor-checkpoint-update.patch
Patch3:         0003-Super-intel-Fix-first-checkpoint-restart.patch
Patch4:         0004-Grow-Move-update_tail-assign-to-Grow_reshape.patch
Patch5:         0005-Add-understanding-output-section-in-man.patch
Patch6:         0006-util.c-change-devnm-to-const-in-mdmon-functions.patch
Patch7:         0007-Wait-for-mdmon-when-it-is-stared-via-systemd.patch
Patch8:         0008-Detail-remove-duplicated-code.patch
Patch9:         0009-mdadm-Fix-native-detail-export.patch
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
%autosetup -p1 -a1

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
%if 0%{?suse_version} < 1600
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcmdmonitor
%endif
%if 0%{?suse_version} < 1550
	mkdir -p %{buildroot}/sbin
	ln -s %{_sbindir}/mdadm %{buildroot}/sbin/mdadm
	ln -s %{_sbindir}/mdmon %{buildroot}/sbin/mdmon
%endif

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
%if 0%{?suse_version} < 1550
/sbin/mdadm
/sbin/mdmon
%endif
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
