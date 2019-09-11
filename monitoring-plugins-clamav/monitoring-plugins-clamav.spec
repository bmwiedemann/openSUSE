#
# spec file for package monitoring-plugins-clamav
#
# Copyright (c) 2012-2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           monitoring-plugins-clamav
Version:        1.2
Release:        1
License:        ISC
Summary:        Check to see if your ClamAV signatures are current
Url:            http://exchange.nagios.org/directory/Plugins/Anti-2DVirus/ClamAV/ClamAV-check-plugin/details
Group:          System/Monitoring
Source0:        check_clamav
%if 0%{?suse_version} > 1010
# nagios can execute the script with embedded perl
Recommends:     perl
%endif
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-clamav = %{version}-%{release}
Obsoletes:      nagios-plugins-clamav < %{version}-%{release}
Requires:       clamav
Requires:       monitoring-plugins-common
Requires:       perl(File::Basename)
Requires:       perl(Net::DNS)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This check plugin is a Perl script which compares your local signature database
(daily.cvd) version to the version advertised from the ClamAV site. It verifies
the latest ClamAV revision using a DNS TXT query against
current.cvd.clamav.net.

%prep
%setup -q -T -c %{name}
install -m644 %{SOURCE0} .
sed -i "s|/usr/local/libexec/nagios|%{nagios_plugindir}|g;
		s|/usr/local/sbin/clamd|%{_sbindir}/clamd|g;" check_clamav

%build

%install
install -D -m755 check_clamav %{buildroot}%{nagios_plugindir}/check_clamav

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_clamav

%changelog
