#
# spec file for package monitoring-plugins-zypper
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


%if 0%{?suse_version} >= 1230
%bcond_without systemd
%else
%bcond_with systemd
%endif

Name:           monitoring-plugins-zypper
Summary:        Check for software updates via zypper
License:        BSD-3-Clause
Group:          System/Monitoring
Version:        1.98.11
Release:        0
URL:            https://github.com/lrupp/monitoring-plugins-zypper
Source0:        %{name}-%{version}.tar.xz
Requires:       gawk
Requires:       grep
Requires:       rpm
Requires:       perl(Getopt::Long)
Requires:       perl(POSIX)
Requires:       perl(Time::Local)
%if 0%{?suse_version} < 1200
BuildRequires:  xz
%endif
%if 0%{?suse_version} > 1310
BuildRequires:  sudo
Requires:       sudo
%endif
%if 0%{?suse_version}
# nagios can execute the script with embedded perl
Recommends:     perl 
Recommends:     apparmor-parser
BuildRequires:  apparmor-parser
%endif
%if 0%{?suse_version} > 1320
Requires:       apparmor-abstractions
%else
Requires:       apparmor-profiles
%endif
Requires:       zypper
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  distribution-release
%endif
%if %{with systemd}
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd-rpm-macros
%endif
%{?systemd_requires}
%endif
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-zypper = %{version}-%{release}
Obsoletes:      nagios-plugins-zypper < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin checks for software updates on systems that use package
management systems based on the zypper command found in (open)SUSE.

It checks for security, recommended and optional patches and also for
optional package updates.

You can define the status by patch category. Use a commata to list more
than one category to a state.

If you like to know the names of available patches and packages, use
the "-v" option.


%prep
%setup -q

%build

%install
install -D -m755 check_zypper.pl                     %buildroot/%{nagios_plugindir}/check_zypper
install -D -m644 usr.lib.nagios.plugins.check_zypper %{buildroot}%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_zypper
install -D -m644 apparmor-abstractions-rpm           %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/rpm
install -D -m644 apparmor-abstractions-ssl           %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/ssl
install -D -m644 apparmor-abstractions-zypp          %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/zypp
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/local
for file in usr.lib.nagios.plugins.check_zypper.zypp_refresh usr.lib.nagios.plugins.check_zypper ; do
cat > %{buildroot}%{_sysconfdir}/apparmor.d/local/$file << EOF
# Site-specific additions and overrides for usr.lib.nagios.plugins.check_zypper
# See /etc/apparmor.d/local/README for details.
EOF
done
%if 0%{?suse_version} > 1310
install -Dm400 sudo-profile-check_zypper             %{buildroot}%{_sysconfdir}/sudoers.d/check_zypper
%endif

%check
# generic test if check_zypper is working at all
%buildroot/%{nagios_plugindir}/check_zypper --help
if [ "$?" != "0" ]; then
    echo "Test failed: check_zypper can not print help text" >&2
    exit 1
fi

%clean
rm -rf %buildroot

%postun
if [ "$YAST_IS_RUNNING" != "instsys" ]; then
     if [ -x /sbin/apparmor_parser ]; then
       %if %{with systemd}
         if /usr/bin/systemctl is-active --quiet apparmor.service; then
             /sbin/apparmor_parser -r -T -W  %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_zypper &> /dev/null || :
         fi
       %else
         if /etc/init.d/boot.apparmor status >/dev/null ; then 
             /sbin/apparmor_parser -r -T -W  %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_zypper &> /dev/null || :
         fi
       %endif
     else
         echo "Could not reload the Apparmor profile: /sbin/apparmor_parser is missing or not executable."
     fi
fi

%files 
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/rpm
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/ssl
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/zypp
%dir %{_sysconfdir}/apparmor.d/local
%config %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_zypper
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.lib.nagios.plugins.check_zypper
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.lib.nagios.plugins.check_zypper.zypp_refresh
%{nagios_plugindir}/check_zypper
%if 0%{?suse_version} > 1310
%config(noreplace) %{_sysconfdir}/sudoers.d/check_zypper
%endif

%changelog
