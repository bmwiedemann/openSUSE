#
# spec file for package monitoring-plugins-keepalived
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           monitoring-plugins-keepalived
Summary:        Check keepalived
License:        BSD-3-Clause
Group:          System/Monitoring
Version:        0.1.5
Release:        1
Url:            https://en.opensuse.org/Monitoring-plugins-keepalived
Source0:        check_keepalived
Source1:        keepalived_notify_monitoring.sh
Source2:        monitoring-plugins-keepalived-rpmlintrc
BuildRequires:  keepalived
Requires:       awk
Requires:       bash
Requires:       coreutils 
Requires:       grep
Requires:       keepalived
Requires:       logrotate
Requires:       monitoring-plugins-common
Requires:       procps
Requires(pre):  keepalived
Recommends:     net-snmp
BuildArch:      noarch
BuildRequires:  nagios-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This script either uses the 'notify' or snmp functionality of keepalived 
to inform an administrator about the current state of keepalived masters and
slaves.

While the SNMP part is simply querying a SNMP server for the keepalived 
part (via agentx), the 'notify' part needs some adaptions in the keepalived.conf
to: 
* execute a script on changes during keepalived runtime, which writes
  the state change into a temporary file
* read the file each time the monitoring server asks for the state if
  there is a keepalived up and running

%prep

%build

%install
#
# "binaries"
#
install -D -m755 %{SOURCE0} %buildroot/%{nagios_plugindir}/check_keepalived
install -D -m755 %{SOURCE1} %buildroot/%{_bindir}/keepalived_notify_monitoring.sh
#
# extra configuration file
#
mkdir -p %buildroot/%{_sysconfdir}/keepalived
cat >> %buildroot/%{_sysconfdir}/keepalived/keepalived_notify_monitoring.conf << EOF
#
# Where to store the logs
#
LOGFILE='/var/log/keepalived_notify.log'
#
# The file with the current status information
# Checked by %{nagios_plugindir}/check_keepalived
#
STATEFILE='/var/run/keepalived.state'
#
# Any additional script that should be executed.
# Arguments given to the script:
# $1 = "GROUP"|"INSTANCE"
# $2 = name of the group or instance
# $3 = target state of transition (stop only applies to instances)
#     ("MASTER"|"BACKUP"|"FAULT"|"STOP")
# $4 = priority value
#
# Please uncomment the following line to activate...
# EXEC_SCRIPT=''
EOF
#
# logrotate
#
mkdir -p %buildroot/%{nrpe_sysconfdir} %buildroot/%{_sysconfdir}/logrotate.d
cat >> %buildroot/%{_sysconfdir}/logrotate.d/%{name}  << EOF
/var/log/keepalived_notify.log {
    compress
    dateext
    maxage 365
    rotate 99
    missingok
    notifempty
    size +4096k
    create 640 root root
    sharedscripts
}
EOF

#
# nrpe config
#
cat >> %buildroot/%{nrpe_sysconfdir}/check_keepalived.cfg  <<EOF
# example command definition for check_keepalived
# please run 
#   %{nagios_plugindir}/check_keepalived -h
# for a complete list of options
command[check_keepalived]=%{nagios_plugindir}/check_keepalived
EOF

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%config(noreplace) %{_sysconfdir}/keepalived/keepalived_notify_monitoring.conf
%config(noreplace) %{nrpe_sysconfdir}/check_keepalived.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{nagios_plugindir}/check_keepalived
%{_bindir}/keepalived_notify_monitoring.sh

%changelog
