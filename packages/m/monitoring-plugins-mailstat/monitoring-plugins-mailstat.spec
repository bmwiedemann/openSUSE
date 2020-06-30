#
# spec file for package monitoring-plugins-mailstat
#
# Copyright (c) 2020 SUSE LLC
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


Name:           monitoring-plugins-mailstat
Version:        0.9.1
Release:        0
Summary:        Monitoring mail server statistics
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            http://linuxplayer.org/2010/12/check_mailstat-pl-a-nagios-plugin-for-monitoring-mail-server-statistics
Source0:        check_mailstat_plugin_v%{version}.zip
Source1:        monitoring-plugins-mailstat-rpmlintrc
Source2:        check_mailstat.cfg
Source3:        gpl-3.0.txt
# PATCH-FIX-UPSTREAM -- allow to configure the path name of the statistics file via -s option
Patch1:         check_mailstat_plugin_v0.9.1-stat_file.patch
# PATCH-FIX-UPSTREAM -- write out the initial values if there is no old file instead of all zero (confuses people)
Patch2:         check_mailstat_plugin_v0.9.1-initial_values.patch
BuildRequires:  nagios-rpm-macros
BuildRequires:  unzip
Requires:       mailgraph
Requires:       monitoring-plugins-common
Requires:       perl(RRDs)
Provides:       nagios-plugins-mailstat = %{version}-%{release}
Obsoletes:      nagios-plugins-mailstat < %{version}-%{release}
BuildArch:      noarch
# nagios can execute the script with embedded perl
Recommends:     perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin includes a patch for mailgraph so that it will also output its
statistics counter to an external file(plus the rra file),and a
check_mailstat.pl which check the stat counter to see if it’s ok, emit
WARN/CRITICAl result if not.It can run on nagios server, or on remote server
via NRPE.

%prep
%setup -q -n check_mailstat_plugin_v%{version}
%patch1 -p1
%patch2 -p1
sed -i "s|||g" README.txt
install -m0644 %{SOURCE3} .

%build

%install
install -D -m755 check_mailstat.pl %{buildroot}/%{nagios_plugindir}/check_mailstat
ln -s %{nagios_plugindir}/check_mailstat %{buildroot}/%{nagios_plugindir}/check_mailstat.pl
install -D -m644 extra/check_mailstat.php %{buildroot}/%{pnp4nagios_templatedir}/check_mailstat.php
install -D -m644 %{SOURCE2} %{buildroot}%{nrpe_sysconfdir}/check_mailstat.cfg

%files
%defattr(-,root,root)
%doc README.txt
%license gpl-3.0.txt
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_mailstat*
%dir %{pnp4nagios_datarootdir}
%dir %{pnp4nagios_templatedir}
%config(noreplace) %{pnp4nagios_templatedir}/check_mailstat.php
%config(noreplace) %{nrpe_sysconfdir}/check_mailstat.cfg

%changelog
