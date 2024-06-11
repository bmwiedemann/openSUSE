#
# spec file for package monitoring-plugins-bind9
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


Name:           monitoring-plugins-bind9
Version:        1.0.0
Release:        0
Summary:        BIND9 Monitoring Plugin
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            https://github.com/thorfi/nagios-bind9-plugin
Source0:        nagios-bind9-plugin-1.0.0.tar.bz2
Source1:        monitoring-plugins-bind9-sudoers
Source2:        monitoring-plugins-bind9-nrpe
# PATCH-FIX-UPSTREAM: increase the amount of lines to read backwards - to allow this check to succeed even with huge amount of DNS zones
Patch0:         monitoring-plugins-bind9-increase_stats-seek.patch
BuildRequires:  nagios-rpm-macros
BuildRequires:  sudo
Requires:       bind-utils
Requires:       sudo
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Provides:       nagios-plugins-bind9 = %{version}-%{release}
Obsoletes:      nagios-plugins-bind9 < %{version}-%{release}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Plugins for BIND9 and DNS resolver monitoring. The check_bind9.pl plugin
expects to run on the host running BIND.

Please run it with --help to see where it expects to find a variety of files
and commands, and the options you are likely to require to provide.

%package -n monitoring-plugins-dns.pl
Summary:        Monitor a DNS server
Group:          System/Monitoring
Requires:       perl(Getopt::Long)
Requires:       perl(IO::Select)
Requires:       perl(IO::Socket)
Requires:       perl(Socket)
Provides:       nagios-plugins-dns.pl = %{version}-%{release}
Obsoletes:      nagios-plugins-dns.pl < %{version}-%{release}

%description -n monitoring-plugins-dns.pl
A Perl based monitoring plugin which can be used to monitor a DNS server. It
forms DNS queries of specific QTYPE and QNAME and sends them directly to the
DNS server.

%prep
%autosetup -p1 -n nagios-bind9-plugin-%{version}
cp %{SOURCE1} .

%build
#

%install
mkdir -p %{buildroot}/%{nagios_plugindir} %{buildroot}/%{pnp4nagios_templatedir}
install -m755 check_bind9.pl %{buildroot}/%{nagios_plugindir}/check_bind9.pl
install -m644 pnp4nagios/check_bind9.php %{buildroot}/%{pnp4nagios_templatedir}/check_bind9.php
install -m755 check_dns.pl %{buildroot}/%{nagios_plugindir}/check_dns.pl
install -m644 pnp4nagios/check_dns.php %{buildroot}/%{pnp4nagios_templatedir}/check_dns.php
install -Dm0644 %{SOURCE1} %{buildroot}%{nrpe_sysconfdir}/check_bind9.cfg

%files
%defattr(-,root,root)
%license LICENSE
%doc README monitoring-plugins-bind9-sudoers
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{pnp4nagios_datadir}
%dir %{pnp4nagios_templatedir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_bind9.pl
%{pnp4nagios_templatedir}/check_bind9.php
%config(noreplace) %{nrpe_sysconfdir}/check_bind9.cfg

%files -n monitoring-plugins-dns.pl
%defattr(-,root,root)
%license LICENSE
%doc README
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_dns.pl
%{pnp4nagios_templatedir}/check_dns.php

%changelog
