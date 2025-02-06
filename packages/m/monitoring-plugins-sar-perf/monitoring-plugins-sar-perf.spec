#
# spec file for package monitoring-plugins-sar-perf
#
# Copyright (c) 2025 SUSE LLC
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


Name:           monitoring-plugins-sar-perf
Summary:        Get performance data from sar
License:        BSD-2-Clause
Group:          System/Monitoring
Version:        0.1+git.1272298931.4878d0c
Release:        0
URL:            https://github.com/nickanderson/check-sar-perf
Source0:        check-sar-perf-%{version}.tar.xz
Source1:        check_iostat
Source2:        usr.lib.nagios.plugins.check_iostat
Patch0:         monitoring-plugins-sar-perf-output.patch
Patch1:         monitoring-plugins-sar-perf-stdout.patch
# PATCH-FIX-UPSTREAM no-python2.patch gh#nickanderson/check-sar-perf!3 mcepl@suse.com
# make the script Python 3 compatible
Patch2:         no-python2.patch
BuildRequires:  nagios-rpm-macros
%if 0%{?suse_version}
Recommends:     apparmor-profiles
%endif
Provides:       nagios-plugins-sar-perf = %{version}-%{release}
Obsoletes:      nagios-plugins-sar-perf < %{version}-%{release}
Requires:       python3
Requires:       sysstat
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plug-in was written to get performance data from sar. It was developed for
use with Zenoss but should work with other NRPE compatible NMS.

Example output:

check_sar_perf cpu
sar OK| CPU=all user=59.90 nice=0.00 system=4.46 iowait=0.00 steal=0.00
  idle=35.64

check_sar_perf disk sda
sar OK| DEV=sda tps=0.00 rd_sec/s=0.00 wr_sec/s=0.00 avgrq-sz=0.00
  avgqu-sz=0.00 await=0.00 svctm=0.00 util=0.00

%prep
%autosetup -p1 -n check-sar-perf-%{version}

%build

%install
install -D -m755 check_sar_perf.py %{buildroot}/%{nagios_plugindir}/check_sar_perf
install -m755 %{SOURCE1} %{buildroot}/%{nagios_plugindir}/check_iostat
install -Dm0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_iostat

%postun
if [ "$YAST_IS_RUNNING" != "instsys" ]; then
     if [ -x /sbin/apparmor_parser ]; then
         if /usr/bin/systemctl is-active --quiet apparmor.service; then
             /sbin/apparmor_parser -r -T -W  %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_iostat &> /dev/null || :
         fi
     else
         echo "Could not reload the Apparmor profile: /sbin/apparmor_parser is missing or not executable."
     fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{_sysconfdir}/apparmor.d
%{nagios_plugindir}/check_sar_perf
%{nagios_plugindir}/check_iostat
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_iostat

%changelog
