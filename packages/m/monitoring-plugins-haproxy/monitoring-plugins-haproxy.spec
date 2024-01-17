#
# spec file for package monitoring-plugins-haproxy
#
# Copyright (c) 2021 SUSE LLC
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


Name:           monitoring-plugins-haproxy
Version:        1.1g6790d7f
Release:        0
Summary:        Plugin to check HAProxy (csv) stats url
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/Napsty/check_haproxy
Source0:        check_haproxy-%{version}.tar.gz
Source1:        gpl-2.0.txt
BuildRequires:  nagios-rpm-macros
# For directory ownership:
BuildRequires:  icinga2-bin
BuildRequires:  icinga2-common
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Status)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Locale::gettext)
Requires:       perl(Nagios::Plugin)
Requires:       perl(Time::HiRes)
Provides:       nagios-plugins-haproxy = %{version}-%{release}
Obsoletes:      nagios-plugins-haproxy < %{version}-%{release}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The plugin checks HAProxy statistic url (csv) and gets UP and DOWN services.

%prep
%setup -q -n check_haproxy-%{version}
install -m644 %{SOURCE1} LICENSE

%build
#
%install
install -D -m755 check_haproxy.pl %{buildroot}%{nagios_plugindir}/check_haproxy.pl
# icinga2 check_command template
install -D -m0644 icinga2/CheckCommand.conf %{buildroot}%{icinga2_datadir}/include/plugins-contrib.d/%{name}.conf
# NRPE configuration check_connections
mkdir -p %{buildroot}%{nrpe_sysconfdir}
cat > %{buildroot}%{nrpe_sysconfdir}/check_haproxy.cfg << EOF
# default check, please adjust the URL, User and Password
command[check_haproxy]=/usr/lib/nagios/plugins/check_haproxy.pl -u 'https://proxy.example.com/;csv;norefresh' -U admin -P 's3cr3t'
# define backends, that will immediately turn the check critical. Other backends will only result in a warning
#command[check_haproxy]=/usr/lib/nagios/plugins/check_haproxy.pl -u 'https://proxy.example.com/;csv;norefresh' -U admin -P 's3cr3t' --critical-backends=www,galera
# ignore backends
#command[check_haproxy]=/usr/lib/nagios/plugins/check_haproxy.pl -u 'https://proxy.example.com/;csv;norefresh' -U admin -P 's3cr3t' --ignore-backends=test
EOF

%files
%license LICENSE
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_haproxy.pl
%{icinga2_datadir}/include/plugins-contrib.d/%{name}.conf
%dir %{nrpe_sysconfdir}
%config(noreplace) %{nrpe_sysconfdir}/check_haproxy.cfg

%changelog
