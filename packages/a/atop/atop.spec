# vim: set ts=4 sw=4 et:
#
# spec file for package atop
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 The openSUSE Project.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           atop
Version:        2.4.0
Release:        0
Summary:        Monitor for System Resources and Process Activity
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://www.atoptool.nl/
Source:         http://www.atoptool.nl/download/atop-%{version}.tar.gz
Source1:        atop.desktop
Source99:       atop-rpmlintrc
Patch1:         atop-makefile.patch
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
%{?systemd_requires}
%if 0%{?suse_version:1}
BuildRequires:  update-desktop-files
%endif

%description
Atop is an ASCII full-screen performance monitor, similar to the top
command. At regular intervals, it shows system-level activity related to
the CPU, memory, swap, disks and network layers, and it shows for every
active process the CPU utilization in system and user mode, the virtual
and resident memory growth, priority, username, state, and exit code. The
process level activity is also shown for processes which finished during
the last interval, to get a complete overview about the consumers of things
such as CPU time. Atop only shows the active system-resources and processes,
and only shows the deviations since the previous interval.

%package daemon
Summary:        System Resource and Process Monitoring History Daemon
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires(post): permissions
Recommends:     cron
Recommends:     logrotate

%description daemon
Atop is an ASCII full-screen performance monitor, similar to the top
command. At regular intervals, it shows system-level activity related to
the CPU, memory, swap, disks and network layers, and it shows for every
active process the CPU utilization in system and user mode, the virtual
and resident memory growth, priority, username, state, and exit code. The
process level activity is also shown for processes which finished during
the last interval, to get a complete overview about the consumers of things
such as CPU time. Atop only shows the active system-resources and processes,
and only shows the deviations since the previous interval.

This subpackage contains the permanent monitoring daemon, to store history
information about processes and system resources.

%prep
%setup -q
%patch1

%build
make %{?_smp_mflags} \
    	  OPTFLAGS="%{optflags} -fstack-protector" \
    	  CC="gcc"

%install
install -d "%{buildroot}%{_sbindir}"
make systemdinstall DESTDIR=%{buildroot}

rm -f "%{buildroot}%{_localstatedir}/log/atop"/*

install -D -m0644 "atop.service" "%{buildroot}%{_usr}/lib/systemd/system/%{name}.service"
install -D -m0644 "atopgpu.service" "%{buildroot}%{_usr}/lib/systemd/system/atopgpu.service"

install -D -m 0644 atop.cronsystemd "%{buildroot}%{_sysconfdir}/cron.d/%{name}"

install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%if 0%{?suse_update_desktop_file:1}
%suse_update_desktop_file -r "%{name}" System Monitor
%endif

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatopacct
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatopgpu

%pre daemon
%service_add_pre atop.service atopgpu.service atopacct.service

%post daemon
%service_add_post atop.service atopgpu.service atopacct.service
%set_permissions /etc/cron.d

%postun daemon
%service_del_postun atop.service atopgpu.service atopacct.service

%preun daemon
%service_del_preun atop.service atopgpu.service atopacct.service

%verifyscript daemon
%verify_permissions -e /etc/cron.d

%files
%license COPYING
%doc README
%attr(0755,root,root) %{_bindir}/atop
%dir %{_datadir}/%{name}
%{_bindir}/atopsar
%{_bindir}/atopconvert
%{_bindir}/atop-%{version}
%{_bindir}/atopsar-%{version}
%{_mandir}/man1/atop.1%{?ext_man}
%{_mandir}/man1/atopconvert.1%{?ext_man}
%{_mandir}/man1/atopsar.1%{?ext_man}
%{_mandir}/man5/atoprc.5%{?ext_man}
%{_datadir}/applications/%{name}.desktop

%files daemon
%license COPYING
%doc README
%config(noreplace) %{_sysconfdir}/logrotate.d/psaccs_atop
%config(noreplace) %{_sysconfdir}/logrotate.d/psaccu_atop
%dir %{_sysconfdir}/cron.d
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_datadir}/%{name}/atop.daily
%{_localstatedir}/log/atop
%{_usr}/lib/systemd/system/%{name}.service
%{_mandir}/man8/atopacctd.8%{?ext_man}
%{_mandir}/man8/atopgpud.8%{?ext_man}
%{_usr}/lib/systemd/system/atopacct.service
%{_usr}/lib/systemd/system/atopgpu.service
%dir %{_usr}/lib/systemd/system-sleep
%{_usr}/lib/systemd/system-sleep/atop-pm.sh
%{_sbindir}/atopacctd
%{_sbindir}/atopgpud
%{_sbindir}/rcatopacct
%{_sbindir}/rc%{name}
%{_sbindir}/rcatopgpu

%changelog
