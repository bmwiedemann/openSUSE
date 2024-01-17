#
# spec file for package at
#
# Copyright (c) 2022 SUSE LLC
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
Name:           at
Version:        3.2.5
Release:        0
Summary:        A Job Manager
License:        GPL-2.0-or-later
URL:            http://blog.calhariz.com/index.php/tag/at
Source:         http://software.calhariz.com/at/%{name}_%{version}.orig.tar.gz
Source2:        atd.pamd
Source3:        sysconfig.atd
Source5:        atd.service
Source6:        system-user-at.conf
Patch0:         at-3.2.2.patch
Patch11:        at-3.1.13-documentation-dir.patch
#PATCH-FIX-OPENSUSE add proper system users to the deny list
Patch16:        at-3.1.8-denylist.patch
#PATCH-FIX-UPSTREAM plan jobs with past time to tomorrow (bnc#672586)
Patch17:        at-3.1.13-tomorrow.patch
Patch20:        at-3.1.14-parse-suse-sysconfig.patch
#PATCH-FIX-UPSTREAM fix makefile dependencies
Patch21:        at-3.1.14-makefile-deps.patch
#PATCH-FIX-OPENSUSE Set pid dir to /run not /var/run
Patch22:        at-piddir.patch
#PATCH-FIX-OPENSUSE backport privs from 3.1.8 (bnc#849720)
Patch24:        at-backport-old-privs.patch
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
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libHX)
BuildRequires:  pkgconfig(libselinux)
Requires(post): %fillup_prereq
Requires(pre):  permissions
%sysusers_requires
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
%sysusers_generate_pre %{SOURCE6} at system-user-at.conf

%install
%if 0%{?suse_version} > 1500
install -d %{buildroot}{%{_pam_vendordir},%{_bindir},%{_sbindir},%{_mandir}/man{1,5,8},%{_fillupdir}}
%else
install -d %{buildroot}{%{_sysconfdir}/pam.d,%{_bindir},%{_sbindir},%{_mandir}/man{1,5,8},%{_fillupdir}}
%endif

export CFLAGS="%{?optflags}"
export SENDMAIL=%{_sbindir}/sendmail

make install IROOT=%{buildroot}

# Don't install docs here in this way
mkdir docs
mv %{buildroot}/%{_prefix}/doc/at/* docs/

install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/atd.service
ln -s service %{buildroot}%{_sbindir}/rcatd

%if 0%{?suse_version} > 1500
install -m644 %{SOURCE2} %{buildroot}%{_pam_vendordir}/atd
%else
install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/atd
%endif
install -m644 %{SOURCE3} %{buildroot}%{_fillupdir}

mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/

%pre -f at.pre
%service_add_pre atd.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/atd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

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

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/atd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%doc Problems README ChangeLog timespec
%license COPYING Copyright
%config(noreplace) %{_sysconfdir}/at.deny
%{_sbindir}/rcatd
%if 0%{?suse_version} > 1500
%attr(644,root,root) %{_pam_vendordir}/atd
%else
%config %attr(644,root,root) %{_sysconfdir}/pam.d/atd
%endif
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
%{_sysusersdir}/system-user-at.conf
%dir %{_datadir}/at
%{_datadir}/at/batch-job

%changelog
