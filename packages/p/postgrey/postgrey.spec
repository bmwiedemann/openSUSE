#
# spec file for package postgrey
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           postgrey
Version:        1.37
Release:        0
Summary:        Postfix greylisting policy server
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Utilities
Url:            http://postgrey.schweikert.ch/
Source0:        http://postgrey.schweikert.ch/pub/%{name}-%{version}.tar.gz
Source1:        %{name}.init
Source2:        %{name}.sysconfig
Source3:        %{name}.README.SUSE
Source4:        %{name}_daily_greylist.crontab
# http://hg.schweikert.ch/dispatch.fcgi/postgrey-1.x/raw-file/ca06ef218498/postgrey_clients_dump
Source5:        postgrey_clients_dump
Source6:        %{name}.service
# PATCH-FIX-OPENSUSE -- Adapt default config and documentation to pathnames for openSUSE
# /etc/postfix => /etc/postgrey
# /var/spool/postfix/postgrey => /var/lib/postgrey
Patch0:         %{name}-%{version}-config.patch
# PATCH-FIX-OPENSUSE -- run postgrey under the same groupid as postfix: postfix
Patch1:         %{name}-groupid.patch
# PATCH-FIX-OPENSUSE -- patch SOURCE5 to run under openSUSE
Patch2:         postgrey_clients_dump.patch
%if 0%{?suse_version} < 1210
# PATCH-FIX-OPENSUSE -- revert process name changes from 1.35
# startproc will return 7 without
Patch3:         postgrey_process_name.patch
%endif
BuildRequires:  postfix
Requires:       perl >= 5.6.0
Requires:       perl-BerkeleyDB
Requires:       perl-IO-Multiplex
Requires:       perl-Net-DNS
Requires:       perl-Net-Server
Requires:       perl-NetAddr-IP
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version}
Suggests:       cron
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd
%systemd_requires
%endif
Requires(post): %fillup_prereq
%endif
%if 0%{?suse_version} >= 1330
Requires(pre):  group(nogroup)
%endif

%description
Postgrey is a Postfix policy server implementing greylisting. When a
request for delivery of a mail is received by Postfix via SMTP, the
triplet CLIENT_IP / SENDER / RECIPIENT is built. If it is the first
time that this triplet is seen, or if the triplet was first seen less
than 5 minutes, then the mail gets rejected with a temporary error.
Hopefully spammers or viruses will not try again later, as it is
however required per RFC.

The following features compared with greylist.pl from Postfix 2.1.1 are
new: Safe database, automatic maintenance, whitelists, lookup by
subnet, auto-whitelisting of clients, only Berkeley DB and no large
mysql nor postgresql DB needed.

%prep
%setup -q
test -d examples || mkdir examples
cp %{SOURCE5} examples/
%patch0
%patch1
%patch2
%if 0%{?suse_version} < 1210
%patch3
%endif
cp %{SOURCE3} README.SUSE

%build
pod2man -s 8 postgrey > postgrey.8
pod2man -s 8 contrib/postgreyreport > postgreyreport.8

%install
# the binaries
install -d %{buildroot}/%{_sbindir}
install -m 0755 postgrey %{buildroot}/%{_sbindir}/%{name}
install -m 0755 contrib/postgreyreport %{buildroot}/%{_sbindir}/postgreyreport
# manual
install -d %{buildroot}/%{_mandir}/man8
install -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
install -m 0644 postgreyreport.8 %{buildroot}%{_mandir}/man8/postgreyreport.8
# configuration
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -m 0644 postgrey_whitelist_clients %{buildroot}/%{_sysconfdir}/%{name}/whitelist_clients
install -m 0644 postgrey_whitelist_recipients %{buildroot}/%{_sysconfdir}/%{name}/whitelist_recipients
touch whitelist_clients.local
install -m 0644 whitelist_clients.local %{buildroot}/%{_sysconfdir}/%{name}
# configuration
install -D -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
# systemd service file or init file
%if 0%{?suse_version} > 1210
install -D -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
ln -s  	%{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -D %{SOURCE1} %{buildroot}%{_initddir}/%{name}
ln -sf %{_initddir}/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif
# queue directory
install -d %{buildroot}/%{_localstatedir}/lib/%{name}
# directory for socket
install -d -m 0775 %{buildroot}/%{_localstatedir}/spool/postfix/%{name}
# some helper tools
install -m 0644 %{SOURCE4} .

%pre
getent passwd %{name} >/dev/null || useradd -r -g nogroup -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "Postgrey Daemon" %{name}
%if 0%{?suse_version} > 1210
%service_add_pre %{name}.service
%endif

%preun
%if 0%{?suse_version} > 1210
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%post
%if 0%{?suse_version} > 1210
%service_add_post %{name}.service
%fillup_only
%else
%{fillup_and_insserv %{name}}
%endif

%postun
%if 0%{?suse_version} > 1210
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/whitelist_recipients
%config(noreplace) %{_sysconfdir}/%{name}/whitelist_clients
%config(noreplace) %{_sysconfdir}/%{name}/whitelist_clients.local
%{_sbindir}/%{name}
%{_sbindir}/postgreyreport
%{_sbindir}/rc%{name}
%dir %attr(0755,postgrey,postfix) %{_localstatedir}/lib/%{name}
%{_fillupdir}/sysconfig.%{name}
%dir %attr(0770,postgrey,postfix) %{_localstatedir}/spool/postfix/%{name}
%doc %{_mandir}/man?/*
%doc Changes COPYING README README.SUSE examples %{name}_daily_greylist.crontab
%if 0%{?suse_version} > 1210
%{_unitdir}/%{name}.service
%else
%config %attr(0755,root,root) %{_initddir}/%{name}
%endif

%changelog
