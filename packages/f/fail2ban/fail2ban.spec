#
# spec file for package fail2ban
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


%{!?tmpfiles_create:%global tmpfiles_create systemd-tmpfiles --create}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           fail2ban
Version:        1.1.0
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
# Path definitions have been submitted to upstream
Source8:        paths-opensuse.conf
Source200:      fail2ban.keyring
# PATCH-FIX-OPENSUSE fail2ban-opensuse-locations.patch bnc#878028 jweberhofer@weberhofer.at -- update default locations for logfiles
Patch100:       %{name}-opensuse-locations.patch
# PATCH-FIX-OPENSUSE fail2ban-0.10.4-env-script-interpreter.patch jweberhofer@weberhofer.at -- use exact path to define interpretor
Patch201:       %{name}-0.10.4-env-script-interpreter.patch
# PATCH-FEATURE-OPENSUSE harden_fail2ban.service.patch jsegitz@suse.com -- Added hardening to systemd service(s) bsc#1181400
Patch301:       harden_fail2ban.service.patch
# PATCH-FIX-OPENSUSE fail2ban-fix-openssh98.patch meissner@suse.com -- support openssh9.8 bsc#1230101
Patch302:       fail2ban-fix-openssh98.patch
BuildRequires:  fdupes
BuildRequires:  logrotate
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-tools
# timezone package is required to run the tests
BuildRequires:  timezone
Requires:       cron
Requires:       ed
Requires:       iptables
Requires:       logrotate
Requires:       python3 >= 3.5
Requires:       python3-setuptools
Requires:       whois
BuildArch:      noarch
BuildRequires:  python3-systemd
BuildRequires:  pkgconfig(systemd)
Requires:       python3-systemd
Requires:       systemd > 204
%{?systemd_requires}
BuildRequires:  python3-pyinotify >= 0.8.3
Requires:       python3-pyinotify >= 0.8.3
%if 0%{?suse_version} < 1600
Obsoletes:      SuSEfirewall2-%{name}
Provides:       SuSEfirewall2-%{name}
%endif

%description
Fail2ban scans log files like %{_localstatedir}/log/messages and bans IP
addresses that makes too many password failures. It updates firewall rules to
reject the IP address, can send e-mails, or set host.deny entries.  These rules
can be defined by the user. Fail2Ban can read multiple log files such as sshd
or Apache web server ones.

%package -n monitoring-plugins-%{name}
Summary:        Check fail2ban server and how many IPs are currently banned
Group:          System/Monitoring
%if 0%{?suse_version}
BuildRequires:  nagios-rpm-macros
%else
%define         nagios_plugindir %{_libexecdir}/nagios/plugins
%endif
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

%patch -P 100 -p1
%patch -P 201 -p1
%patch -P 301 -p1
%patch -P 302 -p1

rm 	config/paths-arch.conf \
	config/paths-debian.conf \
	config/paths-fedora.conf \
	config/paths-freebsd.conf \
	config/paths-osx.conf

# correct doc-path
sed -i -e 's|%{_datadir}/doc/%{name}|%{_docdir}/%{name}|' setup.py

%build
export CFLAGS="%{optflags}"
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

# use /run directory
install -d -m 755 %{buildroot}/run
touch %{buildroot}/run/%{name}

# systemd
install -d -m 755 %{buildroot}%{_unitdir}
cp -av build/fail2ban.service "%{buildroot}/%{_unitdir}/%{name}.service"

install -d -m 755 %{buildroot}%{_tmpfilesdir}
install -p -m 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

ln -sf service %{buildroot}%{_sbindir}/rc%{name}

echo "# Do all your modifications to the jail's configuration in jail.local!" > %{buildroot}%{_sysconfdir}/%{name}/jail.local

install -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}/

install -d -m 755 %{buildroot}%{_fillupdir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}

install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE3}  %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%if 0%{?suse_version} < 1600
perl -i -lpe 's{(After|PartOf)=(.*)}{$1=$2 SuSEfirewall2.service}' \
	"%{buildroot}/%{_unitdir}/%{name}.service"
%endif
install -D -m 755 files/nagios/check_fail2ban %{buildroot}%{nagios_plugindir}/check_%{name}

# install docs using the macro
rm -r %{buildroot}%{_docdir}/%{name}

# remove duplicates
%fdupes -s %{buildroot}%{python3_sitelib}

%check
# tests require python-pyinotify to be installed, so don't run them on older versions
%if 0%{?suse_version} >= 1500
# Need a UTF-8 locale to work
export LANG=en_US.UTF-8
./fail2ban-testcases-all --no-network || true
%endif

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
# The next line is not workin in Leap 42.1, so keep the old way
#%%tmpfiles_create %%{_tmpfilesdir}/%%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

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
# use /run directory
%ghost /run/%{name}
# systemd
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
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

%files -n monitoring-plugins-%{name}
%license COPYING
%doc files/nagios/README
%if 0%{?suse_version}
%dir %{nagios_libdir}
%else
%dir %{_libexecdir}/nagios
%endif
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_%{name}

%changelog
