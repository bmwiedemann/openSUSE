#
# spec file for package at
#
# Copyright (c) 2020 SUSE LLC
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

Name:           at
Version:        3.2.1
Release:        0
Summary:        A Job Manager
License:        GPL-2.0-or-later
URL:            http://blog.calhariz.com/index.php/tag/at
Source:         http://software.calhariz.com/at/%{name}_%{version}.orig.tar.gz
Source2:        atd.pamd
Source3:        sysconfig.atd
Source5:        atd.service
Patch0:         at-3.1.14.patch
Patch4:         at-3.1.14-joblist.patch
Patch10:        at-3.1.13-massive_batch.patch
Patch11:        at-3.1.13-documentation-dir.patch
# PATCH-FIX-UPSTREAM clean-up opened descriptors (bnc#533454, bnc#523346)
Patch15:        at-3.1.13-leak-fix.patch
#PATCH-FIX-OPENSUSE add proper system users to the deny list
Patch16:        at-3.1.8-denylist.patch
#PATCH-FIX-UPSTREAM plan jobs with past time to tomorrow (bnc#672586)
Patch17:        at-3.1.13-tomorrow.patch
#PATCH-FIX-UPSTREAM wrong mtime handling of jobdir (bnc#680113)
Patch19:        at-3.1.8-jobdir-mtime.patch
Patch20:        at-3.1.14-parse-suse-sysconfig.patch
#PATCH-FIX-UPSTREAM fix makefile dependencies
Patch21:        at-3.1.14-makefile-deps.patch
#PATCH-FIX-OPENSUSE Set pid dir to /run not /var/run
Patch22:        at-piddir.patch
Patch23:        at-secure_getenv.patch
#PATCH-FIX-OPENSUSE backport privs from 3.1.8 (bnc#849720)
Patch24:        at-backport-old-privs.patch
#PATCH-FEATURE-UPSTREAM introduce -o <timeformat> argument for atq (bnc#879402)
Patch25:        at-atq-timeformat.patch
#PATCH-FIX-OPENSUSE use posix timers to avoid the need of suspend/resume hacks.
Patch27:        at-3.1.14-usePOSIXtimers.patch
Patch28:        at-adjust_load_to_cpu_count.patch
# PATCH-FIX-UPSTREAM bnc#945124 kstreitova@suse.com -- don't loop on corrupt files and prevent their creation
Patch29:        at-3.1.16-handle_malformed_jobs.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libHX)
BuildRequires:  pkgconfig(libselinux)
Requires(post): %fillup_prereq
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  permissions
Recommends:     smtp_daemon

%description
This program allows you to run jobs at specified times.

%prep
%autosetup -p1

%build
export SENDMAIL=%{_sbindir}/sendmail

autoreconf -fvi

%configure \
  --with-pam \
  --with-selinux \
  --with-daemon_username=at \
  --with-daemon_groupname=at

%make_build

%install
install -d %{buildroot}{%{_sysconfdir}/pam.d,%{_bindir},%{_sbindir},%{_mandir}/man{1,5,8},%{_fillupdir}}

export CFLAGS="%{?optflags}"
export SENDMAIL=%{_sbindir}/sendmail

make install IROOT=%{buildroot}

# Don't install docs here in this way
mkdir docs
mv %{buildroot}/%{_prefix}/doc/at/* docs/

install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/atd.service
ln -s service %{buildroot}%{_sbindir}/rcatd

install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/atd
install -m644 %{SOURCE3} %{buildroot}%{_fillupdir}

%pre
getent group at >/dev/null || %{_sbindir}/groupadd -g 25 -o -r at
getent passwd at >/dev/null || %{_sbindir}/useradd -r -o -g at -u 25 \
	-s /bin/false -c "Batch jobs daemon" \
	-d %{_localstatedir}/spool/atjobs at
%service_add_pre atd.service

%preun
%service_del_preun atd.service

%post
%{fillup_only -n atd}
%set_permissions %{_bindir}/at
%service_add_post atd.service

%verifyscript
%verify_permissions -e %{_bindir}/at

%postun
%service_del_postun atd.service

%files
%doc Problems README ChangeLog timespec
%license COPYING Copyright
%config(noreplace) %{_sysconfdir}/at.deny
%{_sbindir}/rcatd
%config %attr(644,root,root) %{_sysconfdir}/pam.d/atd
%verify(not mode) %attr(4750,root,trusted) %{_bindir}/at
%{_bindir}/atq
%{_bindir}/atrm
%{_bindir}/batch
%{_mandir}/man?/*
%{_sbindir}/atd
%{_sbindir}/atrun
%attr(700,at,at) %dir %{_localstatedir}/spool/atspool
%attr(1770,at,at) %dir %{_localstatedir}/spool/atjobs
%attr(600,at,at) %{_localstatedir}/spool/atjobs/.SEQ
%{_fillupdir}/sysconfig.atd
%{_unitdir}/atd.service

%changelog
