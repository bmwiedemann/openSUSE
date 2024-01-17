#
# spec file for package monitoring-plugins-sentry3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           monitoring-plugins-sentry3
Version:        2012
Release:        0
Summary:        Monitor Servertech devices that use the Sentry3 MIB
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://www.linuxhomenetworking.com/
Requires:       perl(Nagios::Plugin) >= 0.36
Requires:       perl(Net::SNMP)
Source0:        check_sentry3
Source1:        gauge_single_rrd_one_chart_per_rra.php
Source2:        LICENSE
Patch0:         check_sentry3-fix_output_with_missing_sensors.patch
BuildArch:      noarch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-sentry3 = %{version}-%{release}
Obsoletes:      nagios-plugins-sentry3 < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This Nagios check monitors Servertech devices that use the Sentry3 MIB.

It checks the following:

1) Environmental temperature (Auto-detects all sensors)
2) Environmental humidity (Auto-detects all sensors)
3) Input power (Auto-detects all input feeds)


%prep
%setup -q -T -c %{name}
install -m755 %{SOURCE0} .
%patch0 -p0
install -m644 %{SOURCE2} .

%build
#
%install
install -Dm755 check_sentry3 %{buildroot}/%{nagios_plugindir}/check_sentry3
install -Dm644 %{SOURCE1} %{buildroot}/%{pnp4nagios_templatedir}/gauge_single_rrd_one_chart_per_rra.php

%files
%defattr(-,root,root)
%doc LICENSE
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{pnp4nagios_datadir}
%dir %{pnp4nagios_templatedir}
%{nagios_plugindir}/check_sentry3
%{pnp4nagios_templatedir}/gauge_single_rrd_one_chart_per_rra.php

%changelog
