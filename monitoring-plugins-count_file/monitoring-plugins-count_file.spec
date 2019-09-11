#
# spec file for package monitoring-plugins-count_file
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

Name:           monitoring-plugins-count_file
Version:        232
Release:        0
License:        BSD-4-Clause
Summary:        Counts the number of files in a directory
Url:            https://www.monitoringexchange.org/inventory/Check-Plugins/Operating-Systems/Linux/count_file
Group:          System/Monitoring
Source0:        count_file.pl
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-count_file = %{version}-%{release}
Obsoletes:      nagios-plugins-count_file < %{version}-%{release}
Requires:       perl
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Use this plugin to count the number of files in a directory and 
issue a warning or critical state if the number exceeds a limit.

Useful if you want to monitor for example:
* a directory which contains error files and must stay empty
* a tmp dir which have to stay under a practical limit

%prep
#
%build
#
%install
install -Dm755 %{SOURCE0} %buildroot/%{nagios_plugindir}/count_file.pl

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/count_file.pl

%changelog
