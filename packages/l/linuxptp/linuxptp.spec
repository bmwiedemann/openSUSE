#
# spec file for package linuxptp
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           linuxptp
Version:        4.4
Release:        0
Summary:        Precision Time Protocol v2 daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://linuxptp.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
Source1:        ptp4l.service
Source2:        sysconfig.ptp4l
Source4:        linuxptp-howto.txt
Source5:        phc2sys.service
Source6:        sysconfig.phc2sys
BuildRequires:  kernel-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  %fillup_prereq
Provides:       ptp-timekeeping
%{?systemd_requires}

%description
This software is an implementation of the Precision Time Protocol (PTP)
according to the IEEE1588 standard for Linux.

%prep
%setup -q

%build
export EXTRA_CFLAGS="%{optflags} -Iusr/include"
make %{?_smp_mflags}

cp %{SOURCE4} .

%install
make prefix=%{buildroot}%{_prefix} mandir=%{buildroot}/%{_mandir} install

install -Dpm 644 %{SOURCE1} %{buildroot}/%{_unitdir}/ptp4l.service
install -Dpm 644 %{SOURCE5} %{buildroot}/%{_unitdir}/phc2sys.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcptp4l
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcphc2sys

install -Dpm 644 configs/default.cfg %{buildroot}/%{_sysconfdir}/ptp4l.conf

install -Dpm 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.ptp4l
install -Dpm 644 %{SOURCE6} %{buildroot}%{_fillupdir}/sysconfig.phc2sys

%pre
%service_add_pre ptp4l.service phc2sys.service

%post
%{fillup_only -n ptp4l}
%{fillup_only -n phc2sys}
%service_add_post ptp4l.service phc2sys.service

%preun
%service_del_preun ptp4l.service phc2sys.service

%postun
%service_del_postun ptp4l.service phc2sys.service

%files
%license COPYING
%doc README.org linuxptp-howto.txt configs
%{_unitdir}/ptp4l.service
%{_unitdir}/phc2sys.service
%{_sbindir}/rcptp4l
%{_sbindir}/rcphc2sys
%config %{_sysconfdir}/ptp4l.conf
%{_sbindir}/hwstamp_ctl
%{_sbindir}/phc2sys
%{_sbindir}/phc_ctl
%{_sbindir}/pmc
%{_sbindir}/ptp4l
%{_sbindir}/nsm
%{_sbindir}/timemaster
%{_sbindir}/ts2phc
%{_sbindir}/tz2alt
%{_mandir}/man8/hwstamp_ctl.8%{?ext_man}
%{_mandir}/man8/nsm.8%{?ext_man}
%{_mandir}/man8/phc2sys.8%{?ext_man}
%{_mandir}/man8/phc_ctl.8%{?ext_man}
%{_mandir}/man8/pmc.8%{?ext_man}
%{_mandir}/man8/ptp4l.8%{?ext_man}
%{_mandir}/man8/timemaster.8%{?ext_man}
%{_mandir}/man8/ts2phc.8%{?ext_man}
%{_mandir}/man8/tz2alt.8%{?ext_man}
%{_fillupdir}/sysconfig.ptp4l
%{_fillupdir}/sysconfig.phc2sys

%changelog
