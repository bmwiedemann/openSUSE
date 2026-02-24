#
# spec file for package mdadm
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        4.5+43.gdc69a22f
Release:        0
BuildRequires:  binutils-devel
BuildRequires:  groff
BuildRequires:  pkgconfig
BuildRequires:  sgmltool
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%if 0%{?suse_version} < 1550
BuildRequires:  suse-module-tools
%endif
PreReq:         %fillup_prereq
PreReq:         coreutils
URL:            http://www.kernel.org/pub/linux/utils/raid/mdadm/
Summary:        Utility for configuring "MD" software RAID devices
License:        GPL-2.0-only
Group:          System/Base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.xz
Source1:        Software-RAID.HOWTO.tar.bz2
Source2:        sysconfig.mdadm

%define _udevdir %(pkg-config --variable=udevdir udev)
%define _systemdshutdowndir %{_unitdir}/../system-shutdown

%description
mdadm is a program that can be used to control Linux Software RAID (md) devices.

%package doc
Summary:        Linux Software RAID HOWTO
Group:          Documentation/HTML

%description doc
This package contains the Linux Software RAID HOWTO.

%prep
%autosetup -p1 -a1

%build
%make_build CC="%{__cc}" CXFLAGS="%{optflags}" SUSE=yes BINDIR="%{_sbindir}"
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

# We need to register all (non-instiatated) systemd units with systemd.
# The services (except mdmonitor) just wait for the kernel-side check to
# finish and need not be restarted.
# Restarting the timers isn't problematic because they all use OnCalendar.
%define timers mdcheck_start.timer mdcheck_continue.timer mdmonitor-oneshot.timer
%define norestart_services mdcheck_start.service mdcheck_continue.service mdmonitor-oneshot.service
%define restart_services mdmonitor.service

%pre
%service_add_pre %restart_services %norestart_services %timers

%post
%service_add_post %restart_services %norestart_services %timers
%{?regenerate_initrd_post}
%fillup_only

%preun
%service_del_preun %restart_services %norestart_services %timers

%postun
%service_del_postun_without_restart %norestart_services
%service_del_postun %timers %restart_services

%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%defattr(-,root,root)
%license COPYING
%doc documentation/mdadm.conf-example
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

%files doc
%doc CHANGELOG.md
%doc documentation/external-reshape-design.txt documentation/mdmon-design.txt
%doc Software-RAID.HOWTO/Software-RAID.HOWTO*{.txt,.html}

%changelog
