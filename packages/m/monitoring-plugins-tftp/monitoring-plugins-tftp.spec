#
# spec file for package monitoring-plugins-tftp
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
#

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           monitoring-plugins-tftp
Version:        0.11
Release:        100
License:        GPL-2.0+
Summary:        Check a remote tftp server
Url:            http://isle.wumpus.org/nagios/
Group:          System/Monitoring
Source0:        check_tftp.pl
%if 0%{?suse_version} > 1010
# nagios can execute the script with embedded perl
Recommends:     perl
%endif
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-tftp = %{version}-%{release}
Obsoletes:      nagios-plugins-tftp < %{version}-%{release}
Requires:       perl(FileHandle)
Requires:       perl(Net::TFTP)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This plugin checks for availability of a TFTP Server,
which is normaly used for booting clients over the network.

It downloads a test file from the TFTP server and checks its size against a
given value.

%prep

%build

%install
mkdir -p %{buildroot}/%{nagios_plugindir}
sed -e "s|/usr/local/libexec/nagios|%{nagios_plugindir}|g; \
        s|/usr/local/bin/perl|%{_bindir}/perl|g" %{SOURCE0} > %{buildroot}/%{nagios_plugindir}/check_tftp
chmod +x %{buildroot}/%{nagios_plugindir}/check_tftp

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_tftp

%changelog
