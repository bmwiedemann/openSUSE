#
# spec file for package sysstat
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


Name:           sysstat
Version:        12.7.5
Release:        0
Summary:        Sar and Iostat Commands for Linux
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/sysstat/sysstat
Source:         https://github.com/sysstat/sysstat/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        isag.desktop
# PATCH-FIX-OPENSUSE should be upstreamed
# add locking to scripts sa1 and sa2 (bnc#7861)
Patch0:         sysstat-8.1.6-sa1sa2lock.diff
# PATCH-FIX-OPENSUSE should be upstreamed
# use getpagesize() instead of kb_shift for hugetable archs
Patch2:         sysstat-8.0.4-pagesize.diff
# PATCH-FIX-OPENSUSE bsc#1151453
Patch3:         sysstat-service.patch
Patch4:         harden_sysstat.service.patch
BuildRequires:  findutils
BuildRequires:  gettext-runtime
BuildRequires:  libpcp-devel
BuildRequires:  libpcp_import1
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
Requires:       procmail
Requires:       xz
%{?systemd_ordering}
%ifnarch s390 s390x
BuildRequires:  libsensors4-devel
%endif

%description
Sar and Iostat commands for Linux. The sar command collects and reports
system activity information. The iostat command reports CPU statistics
and I/O statistics for TTY devices and disks.  The information
collected by sar and iostat can be saved in a binary file for future
inspection. Both commands now support SMP machines when displaying CPU
utilization.

%package isag
Summary:        Interactive System Activity Grapher for sysstat
Group:          System/Monitoring
Requires:       gnuplot
Requires:       sysstat = %{version}
Requires:       tk

%description isag
This package includes the isag command, which graphically displays the
system activity data stored in a binary data produced by a sar command
from a sysstat package.

%prep
%autosetup -p1
cp %{SOURCE1} .
# remove date and time from objects
find ./ -name \*.c -exec sed -i -e 's: " compiled " __DATE__ " " __TIME__::g' {} \;

%build
export conf_dir="%{_sysconfdir}/sysstat"
export sa_lib_dir="%{_libdir}/sa"
export cron_owner=root
export LFLAGS="-L. -lsyscom"
export history="60"
export sadc_options="-S ALL"
%configure \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemdsleepdir=%{_systemd_util_dir}/system-sleep \
           --enable-install-cron \
           --disable-silent-rules \
           --enable-nls \
           --disable-man-group \
           --enable-copy-only \
           --disable-file-attr \
           --enable-debug-info \
           --enable-pcp \
%ifnarch s390 s390x
           --enable-sensors \
%endif
           --disable-stripping
%make_build

%install
mkdir -p %{buildroot}%{_localstatedir}/log/sa %{buildroot}%{_sbindir}
%make_install
install -D -m 0644 isag.desktop %{buildroot}%{_datadir}/applications/isag.desktop
%suse_update_desktop_file isag
cp contrib/isag/isag %{buildroot}%{_bindir}
cp contrib/isag/isag.1 %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}%{_datadir}/doc/sysstat*
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcsysstat
%find_lang %{name}

%check
# Newer versions only have simulation tests
# make %%{?_smp_mflags} test

%pre
%service_add_pre sysstat.service sysstat-collect.service sysstat-collect.timer sysstat-summary.service sysstat-summary.timer sysstat-rotate.service syssstat-rotate.timer

%post
%service_add_post sysstat.service sysstat-collect.service sysstat-collect.timer sysstat-summary.service sysstat-summary.timer sysstat-rotate.service syssstat-rotate.timer
# Earlier versions used cron, remove leftover
rm -f /etc/cron.d/sysstat || :

%preun
%service_del_preun sysstat.service sysstat-collect.service sysstat-collect.timer sysstat-summary.service sysstat-summary.timer sysstat-rotate.service syssstat-rotate.timer
[ "$1" -gt 0 ] || rm -rf %{_localstatedir}/log/sa/*

%postun
%service_del_postun sysstat.service sysstat-collect.service sysstat-collect.timer sysstat-summary.service sysstat-summary.timer sysstat-rotate.service syssstat-rotate.timer

%files -f "%{name}.lang"
%license COPYING
%doc CHANGES CREDITS FAQ.md README.md
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%exclude %{_mandir}/man1/isag*
%dir %{_sysconfdir}/sysstat
%dir %{_systemd_util_dir}/system-sleep
%config(noreplace) %{_sysconfdir}/sysstat/sysstat
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/sysstat/sysstat.ioconf
%{_bindir}/cifsiostat
%{_bindir}/iostat
%{_bindir}/mpstat
%{_bindir}/pidstat
%{_bindir}/sadf
%{_bindir}/sar
%{_bindir}/tapestat
%exclude %{_bindir}/isag
%{_libdir}/sa
%{_unitdir}/sysstat.service
%{_unitdir}/sysstat-collect.service
%{_unitdir}/sysstat-collect.timer
%{_unitdir}/sysstat-summary.service
%{_unitdir}/sysstat-summary.timer
%{_unitdir}/sysstat-rotate.service
%{_unitdir}/sysstat-rotate.timer
%{_systemd_util_dir}/system-sleep/sysstat.sleep
%dir %{_localstatedir}/log/sa
%{_sbindir}/rcsysstat

%files isag
%doc contrib/isag/README-isag
%{_mandir}/man1/isag*
%{_bindir}/isag
%{_datadir}/applications/isag.desktop

%changelog
