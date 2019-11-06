#
# spec file for package monitoring-plugins-smart
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


Name:           monitoring-plugins-smart
Version:        6.4
Release:        0
Summary:        Check SMART status of a given disk
License:        SUSE-Public-Domain
Group:          System/Monitoring
URL:            https://www.claudiokuenzler.com/nagios-plugins/check_smart.php
Source0:        check_smart.pl
Source1:        usr.lib.nagios.plugins.check_smart
Source3:        monitoring-plugins-smart-README.SUSE
BuildRequires:  nagios-rpm-macros
BuildRequires:  sudo
Requires:       monitoring-plugins-common
Requires:       smartmontools >= 5.39
Requires:       sudo
Requires:       perl(File::Basename)
Requires:       perl(FindBin)
Requires:       perl(Getopt::Long)
Recommends:     apparmor-parser
Provides:       nagios-plugins-smart = %{version}-%{release}
Obsoletes:      nagios-plugins-smart < 1.02
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin does SMART monitoring both ATA and SCSI disks, has an easy usage
syntax, and automatically produces perfdata for all applicable metrics.

Note:
On older distributions you need a line like
  nagios ALL=NOPASSWD: %{_sbindir}/smartctl
in %{_sysconfdir}/sudoers to run this script as non privileged user.

Since SLES 12/openSUSE 12.1, there is a file
  %{_sysconfdir}/sysconfig/sudoers.d/%{name}
which holds the same content and should be used automatically.

%prep
%setup -q -T -c %{name}
install -m755 %{SOURCE0} check_smart
install -m644 %{SOURCE3} README.SUSE

%build

%install
install -D -m755 check_smart %{buildroot}/%{nagios_plugindir}/check_smart
install -D -m644 %{SOURCE1}  %{buildroot}/%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_smart
%if 0%{?suse_version} > 1130
mkdir -p %{buildroot}/%{_sysconfdir}/sudoers.d
cat >> %{buildroot}/%{_sysconfdir}/sudoers.d/%{name} << EOF
# the next line is needed for %%{name} to allow the correct use of smartctl
nagios        ALL=(root) NOPASSWD: %{_sbindir}/smartctl
EOF
%endif

%files
%doc README.SUSE
%dir %{nagios_libdir}
%dir %{_sysconfdir}/apparmor.d
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_smart
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_smart
%if 0%{?suse_version} > 1130
%config(noreplace) %{_sysconfdir}/sudoers.d/%{name}
%endif

%changelog
