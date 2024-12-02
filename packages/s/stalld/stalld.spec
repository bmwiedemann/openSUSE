#
# spec file for package stalld
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


Name:           stalld
Version:        1.19.3
Release:        0
Summary:        Daemon that finds starving tasks and gives them a temporary boost
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://gitlab.com/rt-linux-tools/%{name}/%{name}.git
Source0:        https://gitlab.com/rt-linux-tools/stalld/-/archive/v%{version}/stalld-v%{version}.tar.bz2
Patch0:         pid-dir.patch
Patch1:         fixed-tmpfile-fix.patch
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Requires(post): %fillup_prereq

%description
The stalld program monitors the set of system threads,
looking for threads that are ready-to-run but have not
been given processor time for some threshold period.
When a starving thread is found, it is given a temporary
boost using the SCHED_DEADLINE policy. The default is to
allow 10 microseconds of runtime for 1 second of clock time.

%prep
%autosetup -v -p1 -n %{name}-v%{version}

%build
%make_build USE_BPF=0 SOPTS="" CFLAGS="%{optflags} %{build_cflags} -DVERSION="\\\"%{version}\\\""" stalld

%install
%make_install DOCDIR=%{_docdir} MANDIR=%{_mandir} BINDIR=%{_bindir} DATADIR=%{_datadir} VERSION=%{version}
%make_install -C systemd UNITDIR=%{_unitdir}
mkdir -p %{buildroot}%{_fillupdir}
mv %{buildroot}%{_sysconfdir}/sysconfig/%{name} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%files
%{_bindir}/%{name}
%{_bindir}/throttlectl
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}
%doc %{_docdir}/README.md
%doc %{_mandir}/man8/stalld.8*
%license gpl-2.0.txt

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%changelog
