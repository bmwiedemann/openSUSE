#
# spec file for package monitoring-plugins-haproxy
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# 
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.




Name:           monitoring-plugins-haproxy
Version:        1.0
Release:        100
License:        GPL-2.0+
Summary:        Plugin to check HAProxy (csv) stats url
Url:            http://cvs.orion.education.fr/viewvc/viewvc.cgi/monitoring-plugins-perl/trunk/plugins/
Group:          System/Monitoring
Source0:        check_haproxy.pl
Source1:        gpl-2.0.txt
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-haproxy = %{version}-%{release}
Obsoletes:      nagios-plugins-haproxy < %{version}-%{release}
Requires:       perl(Nagios::Plugin)
Requires:       perl(Locale::gettext)
Requires:       perl(File::Basename)
Requires:       perl(Time::HiRes)
Requires:       perl(LWP::UserAgent)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Status)
Requires:       perl(Data::Dumper)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The plugin checks HAProxy statistic url (csv) and gets UP and DOWN services.

%prep
%setup -q -T -c %{name}
install -m644 %{SOURCE1} LICENSE

%build
#
%install
%{__mkdir} -p %{buildroot}%{nagios_plugindir}
%{__install} -D -m755 %{SOURCE0} %{buildroot}%{nagios_plugindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{nagios_libdir}
%{nagios_plugindir}/

%changelog
