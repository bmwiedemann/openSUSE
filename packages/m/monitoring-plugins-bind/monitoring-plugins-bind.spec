#
# spec file for package monitoring-plugins-bind
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


Name:           monitoring-plugins-bind
Version:        1.3
Release:        0
Summary:        Check whether BIND is running and to get the performance data via rndc stats
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://exchange.nagios.org/directory/Plugins/Network-Protocols/DNS/check_bind-2Esh/details
Source0:        check_bind.sh
Source1:        LICENSE
Source2:        check_bind.php
Patch0:         check_bind-fix-bashisms.patch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-bind = %{version}-%{release}
Obsoletes:      nagios-plugins-bind < %{version}-%{release}
Requires:       bind-utils
Requires:       coreutils
Requires:       gawk
Requires:       sudo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
check_bind.sh is a Nagios plugin to check the bind daemon whether it's running
via its pid file and then gets the statistics via rndc stats. The user that run
the script needs the ability to 'sudo rndc stats'! The timeframe in which the
rndc stats output is updated is controlled by the check interval. The output
shows amount of requests of various types occured during the last check
interval. The script itself is written sh-compliant and free software under the
terms of the GPLv2 (or later). 

%prep
%setup -cT
install -m 0644 %{SOURCE0} ./check_bind.sh
%patch0

%build

%install
mkdir -p %{buildroot}/%{nagios_plugindir}
sed -e "s|^version=9.4|version=9.6|g; \
        s|Default is: 9.4|Default is: \$version|g; \
		s|9.5|9.5\|9.6|g" check_bind.sh > %{buildroot}/%{nagios_plugindir}/check_bind
chmod +x %{buildroot}/%{nagios_plugindir}/check_bind
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{pnp4nagios_templatedir}/check_bind.php
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_defaultdocdir}/%{name}/LICENSE

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/LICENSE
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{pnp4nagios_datadir}
%dir %{pnp4nagios_templatedir}
%{nagios_plugindir}/check_bind
%{pnp4nagios_templatedir}/check_bind.php

%changelog
