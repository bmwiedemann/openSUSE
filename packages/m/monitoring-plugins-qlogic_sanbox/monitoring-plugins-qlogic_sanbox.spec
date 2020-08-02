#
# spec file for package monitoring-plugins-qlogic_sanbox
#
# Copyright (c) 2013-2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Author: Lars Vogdt
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


Name:           monitoring-plugins-qlogic_sanbox
Summary:        Check QLogic FC Sanboxes
License:        BSD-3-Clause
Group:          System/Monitoring
Version:        1.3
Release:        100
Url:            http://en.opensuse.org/Monitoring-plugins-qlogic_sanbox
Source0:        check_qlogic_sanbox
Requires:       perl(Getopt::Long)
Requires:       perl(Net::Ping)
Requires:       perl(Net::SNMP)
Requires:       perl(Pod::Usage)
Recommends:     perl(Config::IniFiles)
Recommends:     perl(Data::Dumper)
BuildArch:      noarch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-qlogic_sanbox = %{version}-%{release}
Obsoletes:      nagios-plugins-qlogic_sanbox < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nagios plugin, allowing to check QLogic FC Sanboxes.

This plugin has been tested with the following QLogic switches:

SANbox 5200 FC Switch
SANbox 5202 FC Switch
SANbox 5600 FC Switch
SANbox 5602 FC Switch
SANbox 5800 FC Switch


%prep

%build

%install
install -D -m755 %{SOURCE0} %buildroot/%{nagios_plugindir}/check_qlogic_sanbox

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_qlogic_sanbox

%changelog
