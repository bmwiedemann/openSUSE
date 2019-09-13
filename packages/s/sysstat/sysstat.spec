#
# spec file for package sysstat
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           sysstat
Version:        12.0.6
Release:        0
Summary:        Sar and Iostat Commands for Linux
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://pagesperso-orange.fr/sebastien.godard/
Source:         http://pagesperso-orange.fr/sebastien.godard/%{name}-%{version}.tar.xz
Source1:        isag.desktop
Source2:        sysstat.cron.suse
Source4:        sysstat.service
# PATCH-FIX-OPENSUSE should be upstreamed
# add locking to scripts sa1 and sa2 (bnc#7861)
Patch0:         sysstat-8.1.6-sa1sa2lock.diff
# PATCH-FIX-OPENSUSE should be upstreamed
# use getpagesize() instead of kb_shift for hugetable archs
Patch2:         sysstat-8.0.4-pagesize.diff
BuildRequires:  findutils
BuildRequires:  gettext-runtime
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(systemd)
Requires:       procmail
Requires:       xz
%{?systemd_requires}
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
%setup -q
%patch0 -p1
%patch2 -p1
cp %{SOURCE1} %{SOURCE2} %{SOURCE4} .
# remove date and time from objects
find ./ -name \*.c -exec sed -i -e 's: " compiled " __DATE__ " " __TIME__::g' {} \;

%build
export conf_dir="%{_sysconfdir}/sysstat"
export sa_lib_dir="%{_libdir}/sa"
export cron_owner=root
export LFLAGS="-L. -lsyscom"
export history="60"
%configure \
	--disable-silent-rules \
	--enable-nls \
	--disable-man-group \
	--enable-copy-only \
	--disable-file-attr \
	--enable-debug-info \
%ifnarch s390 s390x
	--enable-sensors \
%endif
	--disable-stripping
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_localstatedir}/log/sa %{buildroot}%{_sbindir}
%make_install
install -D -m 0644 isag.desktop %{buildroot}%{_datadir}/applications/isag.desktop
%suse_update_desktop_file isag
cp contrib/isag/isag %{buildroot}%{_bindir}
cp contrib/isag/isag.1 %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}%{_datadir}/doc/sysstat*
install -D -m 0755 sysstat.cron.suse %{buildroot}%{_sysconfdir}/sysstat/sysstat.cron
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcsysstat
%find_lang %{name}
install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/sysstat.service
# change /usr/lib to /usr/lib64 or something else when needed
if [ "%{_libdir}" != "%{_libexecdir}" ]; then
    sed -i 's:%{_libexecdir}/:%{_libdir}/:g' \
           %{buildroot}%{_sysconfdir}/sysstat/sysstat.cron \
           %{buildroot}%{_unitdir}/sysstat.service
fi

%check
make %{?_smp_mflags} test

%pre
%service_add_pre sysstat.service

%preun
%service_del_preun sysstat.service
[ "$1" -gt 0 ] || rm -rf %{_localstatedir}/log/sa/*

%post
%service_add_post sysstat.service

%postun
%service_del_postun sysstat.service

%if 0%{?suse_version} < 1500
%post isag
%desktop_database_post

%postun isag
%desktop_database_postun
%endif

%files -f "%{name}.lang"
%license COPYING
%doc CHANGES CREDITS FAQ.md README.md
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%exclude %{_mandir}/man1/isag*
%dir %{_sysconfdir}/sysstat
%config(noreplace) %{_sysconfdir}/sysstat/sysstat
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/sysstat/sysstat.cron
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
%dir %{_localstatedir}/log/sa
%{_sbindir}/rcsysstat

%files isag
%doc contrib/isag/README-isag
%{_mandir}/man1/isag*
%{_bindir}/isag
%{_datadir}/applications/isag.desktop

%changelog
