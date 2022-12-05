#
# spec file for package fail2ban
#
# Copyright (c) 2022 SUSE LLC
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


%{!?tmpfiles_create:%global tmpfiles_create systemd-tmpfiles --create}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           fail2ban
Version:        1.0.2
Release:        0
Summary:        Bans IP addresses that make too many authentication failures
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.fail2ban.org/
Source0:        https://github.com/fail2ban/fail2ban/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/fail2ban/fail2ban/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.sysconfig
Source3:        %{name}.logrotate
Source5:        %{name}.tmpfiles
Source6:        sfw-fail2ban.conf
Source7:        f2b-restart.conf
# Path definitions have been submitted to upstream
Source8:        paths-opensuse.conf
Source200:      fail2ban.keyring
# PATCH-FIX-OPENSUSE fail2ban-opensuse-locations.patch bnc#878028 jweberhofer@weberhofer.at -- update default locations for logfiles
Patch100:       %{name}-opensuse-locations.patch
# PATCH-FIX-OPENSUSE fail2ban-opensuse-service.patch jweberhofer@weberhofer.at -- openSUSE modifications to the service file
Patch101:       %{name}-opensuse-service.patch
# PATCH-FIX-OPENSUSE fail2ban-disable-iptables-w-option.patch jweberhofer@weberhofer.at -- disable iptables "-w" option for older releases
Patch200:       %{name}-disable-iptables-w-option.patch
# PATCH-FIX-OPENSUSE fail2ban-0.10.4-env-script-interpreter.patch jweberhofer@weberhofer.at -- use exact path to define interpretor
Patch201:       %{name}-0.10.4-env-script-interpreter.patch
# PATCH-FEATURE-OPENSUSE fail2ban-opensuse-service-sfw.patch jweberhofer@weberhofer.at -- start after SuSEfirewall2 only for older distributions
Patch300:       fail2ban-opensuse-service-sfw.patch
# PATCH-FEATURE-OPENSUSE harden_fail2ban.service.patch jsegitz@suse.com -- Added hardening to systemd service(s) bsc#1181400
Patch301:       harden_fail2ban.service.patch
BuildRequires:  fdupes
BuildRequires:  logrotate
BuildRequires:  python-rpm-macros
BuildRequires:  python3-tools
# timezone package is required to run the tests
BuildRequires:  timezone
Requires:       cron
Requires:       ed
Requires:       iptables
Requires:       logrotate
Requires:       python3 >= 3.2
Requires:       whois
%if 0%{?suse_version} != 1110
BuildArch:      noarch
%endif
%if 0%{?suse_version} >= 1230
# systemd
BuildRequires:  python3-systemd
BuildRequires:  pkgconfig(systemd)
Requires:       python3-systemd
Requires:       systemd > 204
%{?systemd_requires}
%else
# no systemd (the init-script requires lsof)
Requires:       lsof
Requires:       syslog
%endif
%if 0%{?suse_version} >= 1140 && 0%{?suse_version} != 1010  && 0%{?suse_version} != 1110 && 0%{?suse_version} != 1315
BuildRequires:  python3-pyinotify >= 0.8.3
Requires:       python3-pyinotify >= 0.8.3
%endif

%description
Fail2ban scans log files like %{_localstatedir}/log/messages and bans IP
addresses that makes too many password failures. It updates firewall rules to
reject the IP address, can send e-mails, or set host.deny entries.  These rules
can be defined by the user. Fail2Ban can read multiple log files such as sshd
or Apache web server ones.

%if !0%{?suse_version} > 1500
%package -n SuSEfirewall2-%{name}
Summary:        Files for integrating fail2ban into SuSEfirewall2 via systemd
Group:          Productivity/Networking/Security
Requires:       SuSEfirewall2
Requires:       fail2ban

%description -n SuSEfirewall2-%{name}
This package ships systemd files which will cause fail2ban to be ordered in
relation to SuSEfirewall2 such that the two can be run concurrently within
reason, i.e. SFW will always run first because it does a table flush.
%endif

%package -n monitoring-plugins-%{name}
%define         nagios_plugindir %{_libexecdir}/nagios/plugins
Summary:        Check fail2ban server and how many IPs are currently banned
Group:          System/Monitoring
Provides:       nagios-plugins-%{name} = %{version}
Obsoletes:      nagios-plugins-%{name} < %{version}

%description -n monitoring-plugins-%{name}
This plugin checks if the fail2ban server is running and how many IPs are
currently banned.  You can use this plugin to monitor all the jails or just a
specific jail.

How to use
----------
Just have to run the following command:
  $ ./check_fail2ban --help

%prep
%setup -q
install -m644 %{SOURCE8} config/paths-opensuse.conf

# Use openSUSE paths
sed -i -e 's/^before = paths-.*/before = paths-opensuse.conf/' config/jail.conf

%patch100 -p1
%patch101 -p1
%if 0%{?suse_version} < 1310
%patch200 -p1
%endif
%patch201 -p1
%if !0%{?suse_version} > 1500
%patch300 -p1
%endif
%patch301 -p1

rm 	config/paths-arch.conf \
	config/paths-debian.conf \
	config/paths-fedora.conf \
	config/paths-freebsd.conf \
	config/paths-osx.conf

# correct doc-path
sed -i -e 's|%{_datadir}/doc/%{name}|%{_docdir}/%{name}|' setup.py

# remove syslogd-logger settings for older distributions
%if 0%{?suse_version} < 1230
sed -i -e 's|^\([^_]*_backend = systemd\)|#\1|' config/paths-opensuse.conf
%endif

%build
export CFLAGS="%{optflags}"
./fail2ban-2to3
python3 setup.py build
gzip man/*.{1,5}

%install
python3 setup.py install \
	--root=%{buildroot} \
	--prefix=%{_prefix}

install -d -m 755 %{buildroot}%{_mandir}/man{1,5}
install -p -m 644 man/fail2ban-*.1.gz %{buildroot}%{_mandir}/man1
install -p -m 644 man/jail.conf.5.gz %{buildroot}%{_mandir}/man5

install -d -m 755 %{buildroot}%{_initddir}
install -d -m 755 %{buildroot}%{_sbindir}

%if 0%{?suse_version} > 1310
# use /run directory
install -d -m 755 %{buildroot}/run
touch %{buildroot}/run/%{name}
%else
#use /var/run directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/%{name}
%endif

%if 0%{?suse_version} >= 1230
# systemd
install -d -m 755 %{buildroot}%{_unitdir}
install -p -m 644 files/%{name}.service.in %{buildroot}%{_unitdir}/%{name}.service

install -d -m 755 %{buildroot}%{_tmpfilesdir}
install -p -m 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

ln -sf service %{buildroot}%{_sbindir}/rc%{name}

%else
# without systemd
install -d -m 755 %{buildroot}%{_initddir}
install -m 755 files/suse-initd %{buildroot}%{_initddir}/%{name}
ln -sf %{_initddir}/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif

echo "# Do all your modifications to the jail's configuration in jail.local!" > %{buildroot}%{_sysconfdir}/%{name}/jail.local

install -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}/

install -d -m 755 %{buildroot}%{_fillupdir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}

install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE3}  %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%if !0%{?suse_version} > 1500
%if 0%{?_unitdir:1}
install -Dm 0644 "%{_sourcedir}/sfw-fail2ban.conf" \
	"%{buildroot}%{_unitdir}/SuSEfirewall2.service.d/fail2ban.conf"
install -D -m 0644 "%{_sourcedir}/f2b-restart.conf" \
	"%{buildroot}%{_unitdir}/fail2ban.service.d/SuSEfirewall2.conf"
%endif
%endif
install -D -m 755 files/nagios/check_fail2ban %{buildroot}%{nagios_plugindir}/check_%{name}

# install docs using the macro
rm -r %{buildroot}%{_docdir}/%{name}

# remove duplicates
%fdupes -s %{buildroot}%{python3_sitelib}

%check
#stat /dev/log
#python -c "import platform; print(platform.system())"
# tests require python-pyinotify to be installed, so don't run them on older versions
%if 0%{?suse_version} >= 1140 && 0%{?suse_version} != 1010  && 0%{?suse_version} != 1110 && 0%{?suse_version} != 1315
# Need a UTF-8 locale to work
export LANG=en_US.UTF-8
./fail2ban-testcases-all --no-network || true
%endif

%pre
%if 0%{?suse_version} >= 1230
%service_add_pre %{name}.service
%endif

%post
%fillup_only
%if 0%{?suse_version} >= 1230
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
# The next line is not workin in Leap 42.1, so keep the old way
#%%tmpfiles_create %%{_tmpfilesdir}/%%{name}.conf
%service_add_post %{name}.service
%endif

%preun
%if 0%{?suse_version} >= 1230
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%postun
%if 0%{?suse_version} >= 1230
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%if !0%{?suse_version} > 1500
%if 0%{?_unitdir:1}
%post -n SuSEfirewall2-%{name}
%{_bindir}/systemctl daemon-reload >/dev/null 2>&1 || :

%postun -n SuSEfirewall2-%{name}
%{_bindir}/systemctl daemon-reload >/dev/null 2>&1 || :
%endif
%endif

%files
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/action.d
%dir %{_sysconfdir}/%{name}/%{name}.d
%dir %{_sysconfdir}/%{name}/filter.d
%dir %{_sysconfdir}/%{name}/jail.d
#
%config %{_sysconfdir}/%{name}/action.d/*
%config %{_sysconfdir}/%{name}/filter.d/*
#
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config %{_sysconfdir}/%{name}/jail.conf
%config %{_sysconfdir}/%{name}/paths-common.conf
%config %{_sysconfdir}/%{name}/paths-opensuse.conf
#
%config(noreplace) %{_sysconfdir}/%{name}/jail.local
#
%config %{_sysconfdir}/logrotate.d/%{name}
%dir %{_localstatedir}/lib/%{name}/
%if 0%{?suse_version} > 1310
# use /run directory
%ghost /run/%{name}
%else
# use /var/run directory
%dir %ghost %{_localstatedir}/run/%{name}
%endif
%if 0%{?suse_version} >= 1230
# systemd
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%else
# without-systemd
%{_initddir}/%{name}
%endif
%{_sbindir}/rc%{name}
%{_bindir}/%{name}-server
%{_bindir}/%{name}-client
%{_bindir}/%{name}-python
%{_bindir}/%{name}-regex
%{python3_sitelib}/%{name}
%exclude %{python3_sitelib}/%{name}/tests
%{python3_sitelib}/%{name}-*
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%license COPYING
%doc README.md TODO ChangeLog doc/*.txt

# do not include tests as they are executed during the build process
%exclude %{_bindir}/%{name}-testcases
%exclude %{python3_sitelib}/%{name}/tests

%if !0%{?suse_version} > 1500
%if 0%{?_unitdir:1}
%files -n SuSEfirewall2-%{name}
%{_unitdir}/SuSEfirewall2.service.d
%{_unitdir}/%{name}.service.d
%endif
%endif

%files -n monitoring-plugins-%{name}
%license COPYING
%doc files/nagios/README
%dir %{_libexecdir}/nagios
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_%{name}

%changelog
