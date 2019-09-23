#
# spec file for package monitoring-plugins-apcupsd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           monitoring-plugins-apcupsd
Version:        1.3
Release:        0
Summary:        Monitoring plugin for APC Smart-UPSes using apcupsd
License:        BSD-3-Clause
Group:          System/Monitoring
Url:            https://github.com/jkramarz/check_apcupsd/blob/master/check_apcupsd
Source0:        check_apcupsd
Patch1:         monitoring-plugins-apcupsd-power_status.patch
BuildRequires:  nagios-rpm-macros
Requires:       apcupsd
Requires:       bash
Requires:       grep
Provides:       nagios-plugins-apcupsd = %{version}-%{release}
Obsoletes:      nagios-plugins-apcupsd < %{version}-%{release}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nagios plugin to monitor APC Smart-UPSes using apcupsd.

%prep
%setup -q -T -c %{name}
install -m755 %{SOURCE0} .
%patch1 -p1

%build
#
%install
install -D -m755 check_apcupsd %{buildroot}/%{nagios_plugindir}/check_apcupsd

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_apcupsd

%changelog
