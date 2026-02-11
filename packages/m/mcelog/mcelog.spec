#
# spec file for package mcelog
#
# Copyright (c) 2026 SUSE LLC
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


%if 0%{?suse_version} > 1600
%bcond_with email_notify
%endif
# Taken over from chrony
%if 0%{?suse_version} > 1500
%bcond_without usr_etc
%endif
Name:           mcelog
Version:        210
Release:        0
Summary:        Log Machine Check Events
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://mcelog.org/
Source:         mcelog-%{version}.tar.gz
Source2:        mcelog.sysconfig
Source3:        mcelog.systemd
Source5:        mcelog.tmpfiles
%if %{with email_notify}
Source6:        README.email_setup
Patch1:         email.patch
%endif
Patch2:         mcelog_invert_prefill_db_warning.patch
Patch3:         Start-consolidating-AMD-specific-stuff.patch
Patch4:         add_new_amd_cpu_defines
Patch5:         patches/add-f10h-support.patch
Patch6:         patches/add-f11h-support.patch
Patch7:         patches/add-f12h-support.patch
Patch8:         patches/add-f14h-support.patch
Patch9:         patches/add-f15h-support.patch
Patch10:        patches/add-f16h-support.patch
Patch11:        mcelog-socket-path.patch
Patch12:        fix_setgroups_missing_call.patch
%if %{with email_notify}
BuildRequires:  libesmtp-devel
Requires(pre):  %fillup_prereq
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Requires:       logrotate
ExclusiveArch:  %{ix86} x86_64
%{?systemd_requires}

%description
mcelog retrieves machine check events from an x86-64 kernel in a cron
job, decodes them, and logs them to %{_localstatedir}/log/mcelog.

A machine check event is a hardware error detected by the CPU.
It should run on any x86-64 system.

In addition, it allows decoding machine check kernel panic messages.

%prep
%autosetup

%build
echo "SUSE VERSION %{?suse_version}"
echo "%{version}" > .os_version
%make_build CFLAGS="%{optflags} -fpie -pie"

%install
export prefix=%{buildroot}%{_prefix}
export etcprefix=%{buildroot}
make -e install
%if %{with usr_etc}
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d/
install -m644 mcelog.logrotate \
	%{buildroot}%{_distconfdir}/logrotate.d/mcelog
%else
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m644 mcelog.logrotate \
	%{buildroot}%{_sysconfdir}/logrotate.d/mcelog
%endif

mkdir -p %{buildroot}/%{_docdir}/%{name}

install -m 644 lk10-mcelog.pdf %{buildroot}/%{_docdir}/%{name}/lk10-mcelog.pdf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/mcelog.service
install -D -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/mcelog.conf

%if %{with email_notify}
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.mcelog
install -m 644 %{SOURCE6} %{buildroot}/%{_docdir}/%{name}/README.email_setup
%else
sed -i '\#EnvironmentFile=-/etc/sysconfig/mcelog#d' %{buildroot}%{_unitdir}/mcelog.service
%endif

%if 0%{?suse_version} < 1600
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcmcelog
%endif

%pre
%service_add_pre %{name}.service
%if %{with usr_etc}
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/mcelog ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if %{with usr_etc}
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/mcelog ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%if %{with email_notify}
%fillup_only
%endif
%tmpfiles_create mcelog.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr (-,root,root,755)
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_sbindir}/mcelog
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/mcelog
%else
%config %{_sysconfdir}/logrotate.d/mcelog
%endif

%if %{with email_notify}
%{_fillupdir}/sysconfig.mcelog
%endif

%dir %{_sysconfdir}/mcelog
%config %{_sysconfdir}/mcelog/mcelog.conf
%{_sysconfdir}/mcelog/*trigger
%{_unitdir}/mcelog.service
%{_tmpfilesdir}/mcelog.conf
%{_docdir}/%{name}
%if 0%{?suse_version} < 1600
%{_sbindir}/rcmcelog
%endif
%ghost %attr(0755,root,root) %{_rundir}/mcelog

%changelog
