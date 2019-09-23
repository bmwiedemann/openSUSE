#
# spec file for package monitoring-plugins-contentage
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           monitoring-plugins-contentage
Version:        0.6
Release:        1
License:        BSD-3-Clause
Summary:        Check age of files in a directory
Url:            http://en.opensuse.org/Monitoring-plugins-contentage
Group:          System/Monitoring
Source0:        check_contentage
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-contentage = %{version}-%{release}
Obsoletes:      nagios-plugins-contentage < %{version}-%{release}
Requires:       perl(File::Basename)
Requires:       perl(File::stat)
Requires:       perl(Getopt::Long)
Requires:       perl(POSIX)
Requires:       perl(Time::HiRes)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This plugin checks one or more directory for files older than a specified age.
You can define the age of files for warning and critical states.

Note: the plugin checks the mtime of files, not the ctime.

Usage: check_dircontent.pl -w 24 -c 48 -p /tmp
Options:
       -w|--warning   : time for warnings (minutes)
       -c|--critical  : time for critical warnings (minutes)
       -p|--pathnames : absolute path to the folders, split mutliple pathnames with commata
       -t|--timeout   : timeout (default: 15)

%prep
#
%build
#
%install
install -D -m755 %{SOURCE0} %{buildroot}%{nagios_plugindir}/check_contentage

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_contentage

%changelog
