#
# spec file for package monitoring-plugins-traffic_limit
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


Name:           monitoring-plugins-traffic_limit
Version:        0.5
Release:        0
Summary:        Checks the traffic on any interface
License:        BSD-4-Clause
Group:          System/Monitoring
URL:            http://exchange.nagios.org/directory/Plugins/Network-Connections%2C-Stats-and-Bandwidth/check_traffic_limit/details
Source0:        https://github.com/localguru/check_traffic_limit/archive/0.4.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/localguru/check_traffic_limit/pull/1
Patch1:         b337c024130437d217d6be53ba58cd0238311200.patch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-traffic_limit = %{version}-%{release}
Obsoletes:      nagios-plugins-traffic_limit < %{version}-%{release}
Requires:       gawk
Requires:       grep
Requires:       vnstat
Requires:       perl(Monitoring::Plugin)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
check_traffic_limit is a Nagios plugin based on vnstat. It checks the traffic
on any interface and sends a warning when defined daily or monthly limits are
reached. The plugin comes with Nagios grapher templates.

Example:
./check_traffic_limit -i eth0 -w 10000 -c 12000 -p d

%prep
%autosetup -p1 -n check_traffic_limit-0.4

%build
sed -i s/Nagios::/Monitoring::/ check_traffic_limit

%install
install -Dm755 check_traffic_limit %{buildroot}/%{nagios_plugindir}/check_traffic_limit

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs README.md
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_traffic_limit

%changelog
