#
# spec file for package monitoring-plugins-sip
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         realname nagios-check_sip
Name:           monitoring-plugins-sip
Version:        1.3
Release:        100
Summary:        Test a SIP server/device for availability and response time
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://bashton.com/osprojects/nagiosplugins/
Source:         %{realname}-%{version}.tar.bz2
Patch0:         nagios-check_sip-1.3-utils.patch
# PATCH-FIX-UPSTREAM - use of uninitialized variables if running in timeout
Patch1:         nagios-check_sip-1.3-uninitialized_problem.patch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-sip = %{version}-%{release}
Obsoletes:      nagios-plugins-sip < %{version}-%{release}
Requires:       perl(IO::Socket::INET)
Requires:       perl(Net::Domain)
Requires:       perl(Switch)
Requires:       perl(Time::HiRes)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Test SIP servers.

check_sip requires the following variable:
  -u  Full SIP uri, eg sip:uri@example.com

The following optional variables are also available:
  -f From SIP uri
  -H Host to connect to
  -p Port to connect to
  -w Seconds after which to respond with a warning
  -s Switch off standard behavior: after this, all SIP-responses are counted
      as success

%prep
%setup -q -n %{realname}-%{version}
%patch0
%patch1 -p1

%build

%install
install -D -m0755 check_sip %{buildroot}%{nagios_plugindir}/check_sip

%files
%defattr(-,root,root)
%doc CHANGES COPYING README
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_sip

%changelog
