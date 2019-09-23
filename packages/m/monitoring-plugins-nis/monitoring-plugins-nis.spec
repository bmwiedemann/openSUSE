#
# spec file for package monitoring-plugins-nis
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


Name:           monitoring-plugins-nis
Version:        1.2
Release:        0
Summary:        Check the status of a NIS server on a specified host and NIS domain
License:        GPL-3.0+
Group:          System/Monitoring
Url:            https://www.monitoringexchange.org/inventory/Check-Plugins/Operating-Systems/Linux/check_nis
Provides:       nagios-plugins-nis = %{version}-%{release}
Obsoletes:      nagios-plugins-nis <= 1.2
Source0:        check_nis_%{version}
BuildRequires:  nagios-rpm-macros
Requires:       yp-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Check the status of a NIS server on a specified host and NIS domain by asking
NIS server for "passwd.byname".

As an additional check, a username may be specified which will then be
"looked up" on the NIS server, note that this is optional and only
introduced in v1.1

Script returns OK if it gets an acceptable answer, CRITICAL if not.

This *nix script has been designed and written for the lowest common
denominator of shells (sh), uses yppoll, ypcat and grep as external
commands.

%prep

%build

%install
mkdir -p %{buildroot}/%{nagios_plugindir}
sed -e "s|/usr/local/nagios/libexec|%{nagios_plugindir}|g; \
		s|FLAG_VERBOSE=FALSE|unset LANG;\n\nFLAG_VERBOSE=FALSE|g" %{SOURCE0} > %{buildroot}/%{nagios_plugindir}/check_nis
chmod +x %{buildroot}/%{nagios_plugindir}/check_nis

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_nis

%changelog
