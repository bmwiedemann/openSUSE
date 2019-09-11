#
# spec file for package monitoring-plugins-drbd9
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           monitoring-plugins-drbd9
Version:        0.1
Release:        0
License:        BSD-3-Clause
Summary:        Plugin for monitoring DRBD 9 resources 
Url:            https://github.com/alaskacommunications/nagios_check_drbd9
Group:          System/Monitoring
Source:         nagios_check_drbd9-%{version}.tar.xz 
Patch1:         monitoring-plugins-drbd9-pathnames.patch
Patch2:         monitoring-plugins-drbd9-remove_Data_Dumper_Indent.patch
Requires:       perl(Getopt::Std)
Requires:       perl(Data::Dumper)
BuildRequires:  nagios-rpm-macros
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains monitoring plugins for monitoring DRBD resources. 

The plugins use output from the following sources to determine the state of each resource:
* /proc/drbd
* /usr/sbin/drbdadm sh-resources
* /usr/sbin/drbdetup events2 --now --statistics

The following DRBD kernel modules and DRBD Utilities are supported:
* DRBD 8.4.x with drbd-utils 8.9.6
* DRBD 9.0.x with drbd-utils 8.9.6

%prep
%setup -q -n nagios_check_drbd9-%{version} 
%patch1 -p1
%patch2 -p1
chmod -x *

%build
#

%install
install -Dm755 check_drbd9.pl %{buildroot}%{nagios_plugindir}/check_drbd9.pl
install -m0755 dump_drbd9.pl  %{buildroot}%{nagios_plugindir}/dump_drbd9.pl

%files
%defattr(-,root,root)
%doc ChangeLog* README* COPYING
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/*

%changelog
