#
# spec file for package logwatch
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


Name:           logwatch
Summary:        Analyzes and Reports on system logs
License:        MIT
Group:          System/Monitoring
Version:        7.5.2
Release:        0
Url:            http://www.logwatch.org
BuildArch:      noarch
Source0:        http://sourceforge.net/projects/logwatch/files/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        Logwatch_Dmeventd_Setup_Files.tar.xz
Source3:        ChangeLog
Patch0:         logwatch-firewall.patch
Patch2:         logwatch-timestamp_in_var.patch
Patch3:         logwatch-dmeventd-reduce_frequency.patch
Requires:       cron
Requires:       grep
Requires:       mailx
Requires:       perl
Requires:       perl-Date-Manip
Requires:       sh-utils
Requires:       textutils
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# The main reason for using systemd timers for logwatch is on distros which
# use timers for logrotate, to keep logwatch running before logrotate, as it
# does where both use cron.daily.  We don't need to use systemd timers on all
# distros with systemd, just those with logrotate.timer, which for SUSE is
# SLE 12 SP3/Leap 42.3 and newer (including 15.x).
%if 0%{?sle_version} >= 120300 || 0%{?fedora} >= 30
%bcond_without systemd
%{?systemd_requires}

%if 0%{?suse_version}
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif

%else
%bcond_with systemd
%endif

%description
Logwatch is a customizable, pluggable log-monitoring system. It will go
through your logs for a given period of time and make a report in the
areas that you wish with the detail that you wish.

%prep
%setup -q -a 2
chmod u+w Logwatch_Setup_Files/*
%patch0
%patch2
%patch3
cp %{S:3} .
# fix package doc dir in man page
sed -i -e 's,/usr/share/doc/logwatch-\*,%{_defaultdocdir}/logwatch,' logwatch.8

%build

%install
install -m 0755 -d %{buildroot}%{_var}/cache/logwatch
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/scripts
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf/logfiles
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/logfiles
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/html
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/dist.conf/logfiles
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/dist.conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/scripts/shared
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/lib
install -m 0755 -d %{buildroot}/var/lib/logwatch
install -m 0755 scripts/logwatch.pl %{buildroot}%{_datadir}/logwatch/scripts/logwatch.pl
for i in scripts/logfiles/* ; do
   if [ $(ls $i | wc -l) -ne 0 ] ; then
      install -m 0755 -d %{buildroot}%{_datadir}/logwatch/$i
      install -m 0755 $i/* %{buildroot}%{_datadir}/logwatch/$i
   fi
done
install -m 0755 scripts/services/* %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0755 Logwatch_Setup_Files/dmeventd %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0755 scripts/shared/* %{buildroot}%{_datadir}/logwatch/scripts/shared
install -m 0755 lib/* %{buildroot}%{_datadir}/logwatch/lib
install -m 0644 conf/*.conf %{buildroot}%{_datadir}/logwatch/default.conf
install -m 0644 conf/logfiles/* %{buildroot}%{_datadir}/logwatch/default.conf/logfiles
# these apache log paths are not included in default.conf:
cat > %{buildroot}%{_datadir}/logwatch/dist.conf/logfiles/http.conf << EOF
Archive = apache2/access_log-*.xz
EOF
cat > %{buildroot}%{_datadir}/logwatch/dist.conf/logfiles/http-error.conf << EOF
LogFile = apache2/error_log
Archive = apache2/error_log-*
EOF
install -m 0644 conf/services/* %{buildroot}%{_datadir}/logwatch/default.conf/services
install -m 0644 Logwatch_Setup_Files/dmeventd.conf %{buildroot}%{_datadir}/logwatch/dist.conf/services
install -m 0644 conf/html/* %{buildroot}%{_datadir}/logwatch/default.conf/html
install -m 0755 -d %{buildroot}%{_mandir}/man8
install -m 0644 logwatch.8 %{buildroot}%{_mandir}/man8
install -m 0755 -d %{buildroot}%{_mandir}/man5
install -m 0644 logwatch.conf.5 %{buildroot}%{_mandir}/man5
# replace man page alias files with symlinks
for f in {ignore,override}.conf.5; do
    ln -s logwatch.conf.5 %{buildroot}%{_mandir}/man5/$f
done
rm -f   %{buildroot}%{_sysconfdir}/cron.daily/logwatch \
   %{buildroot}%{_sbindir}/logwatch
%if %{with systemd}
install -D -m 644 scheduler/logwatch.service %{buildroot}%{_unitdir}/logwatch.service
install -D -m 644 scheduler/logwatch.timer %{buildroot}%{_unitdir}/logwatch.timer

%else
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.daily
ln -s %{_datadir}/logwatch/scripts/logwatch.pl %{buildroot}%{_sysconfdir}/cron.daily/0logwatch
%endif
install -m 0755 -d %{buildroot}%{_sbindir}
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.d
install -m 0644 Logwatch_Setup_Files/dmeventd_cronjob.txt %{buildroot}%{_sysconfdir}/cron.d/dmeventd
ln -s %{_datadir}/logwatch/scripts/logwatch.pl %{buildroot}%{_sbindir}/logwatch
echo "###### REGULAR EXPRESSIONS IN THIS FILE WILL BE TRIMMED FROM REPORT OUTPUT #####" > %{buildroot}%{_sysconfdir}/logwatch/conf/ignore.conf
echo "# Local configuration options go here (defaults are in %{_datadir}/logwatch/default.conf/logwatch.conf)" > %{buildroot}%{_sysconfdir}/logwatch/conf/logwatch.conf
echo "# Configuration overrides for specific logfiles/services may be placed here." > %{buildroot}%{_sysconfdir}/logwatch/conf/override.conf
#

%if %{with systemd}
%pre
%service_add_pre %{name}.service %{name}.timer

%post
%service_add_post %{name}.service %{name}.timer
# migration: may need to activate the timer, if enabled but not yet started?

%preun
%service_del_preun %{name}.service %{name}.timer

%postun
%service_del_postun %{name}.service %{name}.timer
%endif

%files
%defattr(-,root,root)
%doc README HOWTO-Customize-LogWatch ChangeLog
%dir %{_var}/cache/logwatch
%dir %{_sysconfdir}/logwatch
%dir %{_sysconfdir}/logwatch/scripts
%dir %{_sysconfdir}/logwatch/conf
%dir %{_sysconfdir}/logwatch/conf/logfiles
%dir %{_sysconfdir}/logwatch/conf/services
%dir %{_datadir}/logwatch
%dir %{_datadir}/logwatch/default.conf
%dir %{_datadir}/logwatch/default.conf/services
%dir %{_datadir}/logwatch/default.conf/logfiles
%dir %{_datadir}/logwatch/default.conf/html
%dir %{_datadir}/logwatch/dist.conf
%dir %{_datadir}/logwatch/dist.conf/services
%dir %{_datadir}/logwatch/dist.conf/logfiles
%dir %{_datadir}/logwatch/scripts
%dir %{_datadir}/logwatch/scripts/logfiles
%dir %{_datadir}/logwatch/scripts/services
%dir %{_datadir}/logwatch/scripts/shared
%dir %{_datadir}/logwatch/scripts/logfiles/*
%dir %{_datadir}/logwatch/lib
%dir /var/lib/logwatch
%config(noreplace) %{_sysconfdir}/cron.d/dmeventd
%{_datadir}/logwatch/scripts/logwatch.pl
%{_sbindir}/logwatch
%{_datadir}/logwatch/scripts/shared/*
%{_datadir}/logwatch/scripts/services/*
%{_datadir}/logwatch/scripts/logfiles/*/*
%{_datadir}/logwatch/lib/Logwatch.pm
%{_datadir}/logwatch/default.conf/*.conf
%{_datadir}/logwatch/default.conf/services/*.conf
%{_datadir}/logwatch/default.conf/logfiles/*.conf
%{_datadir}/logwatch/default.conf/html/*.html
%{_datadir}/logwatch/dist.conf/services/*.conf
%{_datadir}/logwatch/dist.conf/logfiles/*.conf
%if %{with systemd}
%{_unitdir}/logwatch.service
%{_unitdir}/logwatch.timer
%else
%{_sysconfdir}/cron.daily/0logwatch
%endif
%doc %{_mandir}/man8/logwatch.8*
%doc %{_mandir}/man5/*.conf.5*
%config(noreplace) %{_sysconfdir}/logwatch/conf/*.conf

%changelog
