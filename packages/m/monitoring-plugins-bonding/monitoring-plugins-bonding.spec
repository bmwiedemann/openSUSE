#
# spec file for package monitoring-plugins-bonding
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           monitoring-plugins-bonding
Version:        0.002
Release:        0
Summary:        Nagios Network Bonding Check
License:        GPL-2.0-or-later OR Artistic-1.0
Group:          System/Monitoring
Url:            http://www.monitoringexchange.org/inventory/Check-Plugins/Operating-Systems/Linux/Network-Bonding
Source0:        check_bonding.pl
Source1:        usr.lib.nagios.plugins.check_bonding
Source2:        nrpe-check_bonding
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-bonding = %{version}-%{release}
Obsoletes:      nagios-plugins-bonding < %{version}-%{release}
%if 0%{?suse_version}
Recommends:     apparmor-profiles
# nagios can execute the script with embedded perl
Recommends:     perl
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This script attempts to read the proc interface to the Linux kernel bonding
driver, and determine if the bonded interfaces are optimal. It will warn if any
of the enslaved devices are not 'up' (exit 1), and if any bonded interfaces are
not active at all (exit 2). This script is suitable for feeding to NRPE for
Nagios (or similar) to check.

%prep

%build

%install
install -D -m755 %{SOURCE0} %{buildroot}%{nagios_plugindir}/check_bonding
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_bonding
install -D -m644 %{SOURCE2} %{buildroot}%{nrpe_sysconfdir}/check_bonding.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_bonding
%dir %{_sysconfdir}/apparmor.d
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_bonding
%config(noreplace) %{nrpe_sysconfdir}/check_bonding.cfg

%changelog
