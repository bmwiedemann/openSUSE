#
# spec file for package collectl
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


%if ! %{defined _fillupdir}
%define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           collectl
Version:        4.3.6
Release:        0
Summary:        System status data collection utility
License:        Artistic-1.0 AND GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://collectl.sourceforge.net
Source0:        http://sourceforge.net/projects/collectl/files/collectl/%{name}-%{version}/%{name}-%{version}.src.tar.gz
Source1:        collectl.service
Source2:        collectl.sysconfig
Patch0:         harden_collectl.service.patch
BuildRequires:  fdupes
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch
%{?systemd_requires}

%description
Similar to the "sar" program, collectl does collection of device performance
information. It features:
* Fine-grained non-drifting monitoring
* Aggregates performance numbers or device-individual reports
* Aligned monitoring intervals
* Process and slab monitoring
* Monitoring of process i/o statistics
* IPMI monitoring for fans and temperature sensors
* API for importing additional data

%prep
%setup -q -n %{name}
%patch0 -p1

%build

%install
# Install collectl in /usr/bin and link it in /usr/sbin
install -m 755 -D collectl %{buildroot}%{_bindir}/collectl
install -m 755 -D collectl %{buildroot}%{_bindir}/colmux
mkdir -p %{buildroot}/%{_sbindir}
ln -s  %{_bindir}/collectl %{buildroot}/%{_sbindir}/collectl
install -m 644 -D collectl.conf %{buildroot}/%{_sysconfdir}/collectl.conf
install -m 644 -D formatit.ph %{buildroot}%{_datadir}/%{name}/formatit.ph
install -m 644 -D lexpr.ph %{buildroot}%{_datadir}/%{name}/lexpr.ph
install -m 644 -D gexpr.ph %{buildroot}%{_datadir}/%{name}/gexpr.ph
install -m 644 -D misc.ph %{buildroot}%{_datadir}/%{name}/misc.ph
install -m 644 -D hello.ph %{buildroot}%{_datadir}/%{name}/hello.ph
install -m 644 -D graphite.ph %{buildroot}%{_datadir}/%{name}/graphite.ph
install -m 644 -D vmstat.ph %{buildroot}%{_datadir}/%{name}/vmstat.ph
install -m 644 -D %{SOURCE1} %{buildroot}/%{_unitdir}/collectl.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rccollectl
install -m 644 -D %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.collectl
install -m 644 -D man1/collectl.1 %{buildroot}%{_mandir}/man1/collectl.1
install -m 644 -D man1/colmux.1 %{buildroot}%{_mandir}/man1/colmux.1
install -d -m 0755 %{buildroot}%{_var}/log/%{name}
%fdupes -s %{buildroot}

%post
%fillup_only
%service_add_post %{name}.service

%pre
%fillup_only
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING ARTISTIC GPL
%doc docs/* README RELEASE-collectl
%{_unitdir}/collectl.service
%{_fillupdir}/sysconfig.collectl
%config(noreplace) %{_sysconfdir}/collectl.conf
%{_bindir}/collectl
%{_bindir}/colmux
%{_sbindir}/collectl
%{_sbindir}/rccollectl
%{_datadir}/collectl
%{_mandir}/man1/collectl.1%{?ext_man}
%{_mandir}/man1/colmux.1%{?ext_man}
%dir %{_var}/log/%{name}

%changelog
