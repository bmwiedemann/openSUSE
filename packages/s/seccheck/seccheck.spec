#
# spec file for package seccheck
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           seccheck
Version:        3.0
Release:        0
Summary:        Security-Check Scripts
License:        GPL-2.0-or-later
Group:          Productivity/Security
Url:            https://github.com/openSUSE/seccheck
Source0:        https://github.com/openSUSE/seccheck/archive/master.zip
Source1:        sysconfig.seccheck
BuildRequires:  unzip
Requires:       bash
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
Provides:       suse-security-check-3.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# Standard systemd requirements
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
Regularly executable scripts (via cron) for checking the security of
your system.

%prep
%setup -q -n seccheck-master

%build

%install
install -d -m 700 %{buildroot}%{_localstatedir}/lib/secchk
install -d -m 700 %{buildroot}%{_localstatedir}/lib/secchk/data
install -d -m 750 %{buildroot}%{_libexecdir}/secchk
install -d -m 755 %{buildroot}%{_libexecdir}/secchk/blurbs
install -d -m 755 %{buildroot}%{_prefix}/doc/packages/secchk
install -d -m 755 %{buildroot}%{_sysconfdir}/cron.d
install -D -m 0644 %{name}-daily.service %{buildroot}%{_unitdir}/%{name}-daily.service
install -D -m 0644 %{name}-daily.timer %{buildroot}%{_unitdir}/%{name}-daily.timer
install -D -m 0644 %{name}-weekly.service %{buildroot}%{_unitdir}/%{name}-weekly.service
install -D -m 0644 %{name}-weekly.timer %{buildroot}%{_unitdir}/%{name}-weekly.timer
install -D -m 0644 %{name}-monthly.service %{buildroot}%{_unitdir}/%{name}-monthly.service
install -D -m 0644 %{name}-monthly.timer %{buildroot}%{_unitdir}/%{name}-monthly.timer
install -D -m 0644 %{name}-autologout.service %{buildroot}%{_unitdir}/%{name}-autologout.service
install -D -m 0644 %{name}-autologout.timer %{buildroot}%{_unitdir}/%{name}-autologout.timer
install -m 740 *.sh %{buildroot}%{_libexecdir}/secchk/
install -m 640 *.inc %{buildroot}%{_libexecdir}/secchk/
install -m 640 blurbs/*.txt %{buildroot}%{_libexecdir}/secchk/blurbs
install -m 740 checkneverlogin %{buildroot}%{_libexecdir}/secchk/
install -d %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE1} %{buildroot}%{_fillupdir}/
install -d -m 755 %{buildroot}%{_sysconfdir}/security
install -m 644 autologout.conf %{buildroot}%{_sysconfdir}/security/

%pre
%service_add_pre seccheck-daily.timer seccheck-weekly.timer seccheck-monthly.timer

%post
%fillup_only
%service_add_post %{name}-daily.timer %{name}-weekly.timer %{name}-monthly.timer

%preun
%service_del_preun %{name}-daily.timer %{name}-weekly.timer %{name}-monthly.timer

%postun
%service_del_postun %{name}-daily.timer %{name}-weekly.timer %{name}-monthly.timer

%files
%defattr(-,root,root)
%doc TODO CHANGES README LICENCE
%{_libexecdir}/secchk
%{_unitdir}/%{name}-daily.service
%{_unitdir}/%{name}-daily.timer
%{_unitdir}/%{name}-weekly.service
%{_unitdir}/%{name}-weekly.timer
%{_unitdir}/%{name}-monthly.service
%{_unitdir}/%{name}-monthly.timer
%{_unitdir}/%{name}-autologout.service
%{_unitdir}/%{name}-autologout.timer
%dir %{_localstatedir}/lib/secchk
%dir %{_localstatedir}/lib/secchk/data
%{_fillupdir}/sysconfig.seccheck
%config %{_sysconfdir}/security/autologout.conf

%changelog
