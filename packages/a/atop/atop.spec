# vim: set ts=4 sw=4 et:
#
# spec file for package atop
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.8.0
Release:        0
Summary:        Monitor for System Resources and Process Activity
License:        GPL-2.0-only
URL:            https://www.atoptool.nl/
Source0:        https://www.atoptool.nl/download/atop-%{version}.tar.gz
Source1:        atop.desktop
Source2:        atop.default
#Source99:       atop-rpmlintrc
Patch0:         atop-makefile.patch
Patch1:         harden_atop-rotate.service.patch
Patch2:         harden_atop.service.patch
Patch3:         harden_atopacct.service.patch
Patch4:         harden_atopgpu.service.patch
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
Requires:       %{name} = %{version}-%{release}

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
%autosetup -p1

%build
%make_build \
    	  OPTFLAGS="%{optflags} -fstack-protector" \
    	  CC="gcc"

%install
install -d "%{buildroot}%{_sbindir}"
install -d "%{buildroot}%{_sysconfdir}/default"
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/atop

make install DESTDIR=%{buildroot} SYSDPATH=%{_unitdir}

rm -f "%{buildroot}%{_localstatedir}/log/atop"/*

install -D -m0644 "atop.service" "%{buildroot}%{_usr}/lib/systemd/system/%{name}.service"
install -D -m0644 "atopgpu.service" "%{buildroot}%{_usr}/lib/systemd/system/atopgpu.service"
install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%if 0%{?suse_update_desktop_file:1}
%suse_update_desktop_file -r "%{name}" System Monitor
%endif

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatopacct
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatopgpu
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcatop-rotate

%pre daemon
%service_add_pre atop.service atopgpu.service atopacct.service atop-rotate.service

%post daemon
%service_add_post atop.service atopgpu.service atopacct.service atop-rotate.service

%postun daemon
%service_del_postun atop.service atopgpu.service atopacct.service atop-rotate.service

%preun daemon
%service_del_preun atop.service atopgpu.service atopacct.service atop-rotate.service

%files
%license COPYING
%doc README
%attr(0755,root,root) %{_bindir}/atop
%{_bindir}/atopcat
%{_bindir}/atopsar
%{_bindir}/atopconvert
%{_bindir}/atop-%{version}
%{_bindir}/atopsar-%{version}
%{_mandir}/man1/atop.1%{?ext_man}
%{_mandir}/man1/atopcat.1%{?ext_man}
%{_mandir}/man1/atopsar.1%{?ext_man}
%{_mandir}/man1/atopconvert.1%{?ext_man}
%{_mandir}/man5/atoprc.5%{?ext_man}
%{_datadir}/applications/%{name}.desktop

%files daemon
%license COPYING
%doc README
%{_sbindir}/atopgpud
%{_sbindir}/atopacctd
%{_sbindir}/rcatopacct
%{_sbindir}/rcatop-rotate
%{_sbindir}/rc%{name}
%{_sbindir}/rcatopgpu
%{_localstatedir}/log/atop
%{_mandir}/man8/atopgpud.8%{?ext_man}
%{_mandir}/man8/atopacctd.8%{?ext_man}
%{_unitdir}/atop.service
%{_unitdir}/atopgpu.service
%{_unitdir}/atopacct.service
%{_unitdir}/atop-rotate.timer
%{_unitdir}/atop-rotate.service
%dir %{_prefix}/lib/systemd/system-sleep
%{_prefix}/lib/systemd/system-sleep/atop-pm.sh
%config(noreplace)%{_sysconfdir}/default/atop

%changelog
