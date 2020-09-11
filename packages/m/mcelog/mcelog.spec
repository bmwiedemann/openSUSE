#
# spec file for package mcelog
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           mcelog
Version:        170
Release:        0
Summary:        Log Machine Check Events
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://mcelog.org/
Source:         https://git.kernel.org/pub/scm/utils/cpu/mce/mcelog.git/snapshot/mcelog-%{version}.tar.gz
Source2:        mcelog.sysconfig
Source3:        mcelog.systemd
Source5:        mcelog.tmpfiles
Source6:        README.email_setup
Patch1:         email.patch
Patch2:         mcelog_invert_prefill_db_warning.patch
Patch3:         Start-consolidating-AMD-specific-stuff.patch
Patch4:         patches/add-defines.patch
Patch5:         patches/add-f10h-support.patch
Patch6:         patches/add-f11h-support.patch
Patch7:         patches/add-f12h-support.patch
Patch8:         patches/add-f14h-support.patch
Patch9:         patches/add-f15h-support.patch
Patch10:        patches/add-f16h-support.patch
Patch11:        mcelog-socket-path.patch
Patch12:        fix_setgroups_missing_call.patch
BuildRequires:  libesmtp-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Requires:       logrotate
Requires(pre):  %fillup_prereq
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
echo "%{version}" > .os_version
%make_build CFLAGS="%{optflags} -fpie -pie"

%install
export prefix=%{buildroot}%{_prefix}
export etcprefix=%{buildroot}
make -e install
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m644 mcelog.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/mcelog

mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.mcelog

mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 644 %{SOURCE6} %{buildroot}/%{_docdir}/%{name}/README.email_setup
install -m 644 lk10-mcelog.pdf %{buildroot}/%{_docdir}/%{name}/lk10-mcelog.pdf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/mcelog.service
install -D -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/mcelog.conf
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcmcelog

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service
%{?tmpfiles_create:%tmpfiles_create %{_tmpfilesdir}/mcelog.conf}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr (-,root,root,755)
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_sbindir}/mcelog
%config %{_sysconfdir}/logrotate.d/mcelog
%dir %{_sysconfdir}/mcelog
%config %{_sysconfdir}/mcelog/mcelog.conf
%{_fillupdir}/sysconfig.mcelog
%{_sysconfdir}/mcelog/*trigger
%{_unitdir}/mcelog.service
%{_tmpfilesdir}/mcelog.conf
%{_docdir}/%{name}
%{_sbindir}/rcmcelog
%ghost /run/mcelog

%changelog
