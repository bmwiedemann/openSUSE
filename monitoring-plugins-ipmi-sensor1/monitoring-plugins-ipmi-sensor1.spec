#
# spec file for package monitoring-plugins-ipmi-sensor1
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


Name:           monitoring-plugins-ipmi-sensor1
Version:        1.3
Release:        0
Summary:        IPMI Sensor 1 Monitoring Plugin
License:        GPL-3.0+
Group:          System/Monitoring
Url:            http://www.thomas-krenn.com/en/oss/ipmi-plugin/
Source0:        check_ipmi_sensor_v%{version}.tar.bz2
Source1:        usr.lib.nagios.plugins.check_ipmi_sensor1
Patch0:         check_ipmi_sensor_v1.3_PowerEdge.patch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-ipmi-sensor1 = %{version}-%{release}
Obsoletes:      nagios-plugins-ipmi-sensor1 < %{version}-%{release}
Requires:       ipmitool
%if 0%{?suse_version}
Recommends:     apparmor-profiles
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This plugin checks all IPMI sensors of a server remotely or locally. It works
with any IPMI-compatible server, so you can use it also in heterogeneous
environments with different server vendors.

This version 1.x is based on ipmitool and can only monitor threshold based
sensors.

%prep
%setup -q -n check_ipmi_sensor_v%{version}
%patch0 -p1

%build

%install
install -D -m755 check_ipmi_sensor  %{buildroot}%{nagios_plugindir}/check_ipmi_sensor1
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_ipmi_sensor1
install -D -m644 changelog.txt %{buildroot}%{_defaultdocdir}/%{name}/changelog.txt
install -m644 gpl.txt %{buildroot}%{_defaultdocdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ipmi_sensor1
%dir %{_sysconfdir}/apparmor.d
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_ipmi_sensor1

%changelog
