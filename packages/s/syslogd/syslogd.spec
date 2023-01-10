#
# spec file for package syslogd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           syslogd
Version:        1.5.1
Release:        0
Summary:        The Syslog daemon
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://www.infodrom.org/projects/sysklogd/
Source:         https://www.infodrom.org/projects/sysklogd/download/sysklogd-%{version}.tar.gz
#Source4:        https://www.infodrom.org/projects/sysklogd/download/sysklogd-%{version}.tar.gz.asc
Source1:        logrotate.syslog
Source2:        sysconfig.syslogd
Source3:        sysconfig.klogd
Source5:        syslog.8
Source6:        klog.service
Source7:        klogd.service
Source8:        syslogd.service
Source9:        syslogd-service-prepare
Source11:       syslogd-rpmlintrc
Source12:       sysconfig.boot
Patch0:         sysklogd-1.4.1.dif
Patch1:         sysklogd-1.4.1-dgram.patch
Patch2:         sysklogd-1.4.1-sparc.patch
Patch3:         sysklogd-1.4.1-forw.patch
Patch5:         sysklogd-ipv6.diff
Patch6:         sysklogd-1.4.1-klogd24.dif
Patch7:         sysklogd-1.4.1-large.patch
Patch8:         sysklogd-1.4.1-dns.patch
Patch9:         sysklogd-1.4.1-reopen.patch
Patch12:        sysklogd-1.4.1-ksyslogsize.diff
Patch13:        sysklogd-1.4.1-unix_sockets.patch
Patch14:        sysklogd-1.4.1-showpri.patch
Patch18:        sysklogd-1.4.1-dontsleep.patch
Patch19:        sysklogd-1.4.1-signal.dif
Patch20:        sysklogd-1.4.1-clearing.patch
Patch21:        sysklogd-1.4.1-nofortify.patch
Patch22:        sysklogd-1.4.1-sysmap-prior-to-2.5.patch
Patch23:        sysklogd-1.4.1-reload.dif
Patch24:        sysklogd-1.4.1-systemd.dif
Patch25:        sysklogd-1.4.1-systemd-multi.dif
Patch26:        sysklogd-1.4.1-systemd-sock-name.patch
# PATCH-FIX-SUSE bsc#897262, CVE-2014-3634 rsyslog/syslogd: remote syslog PRI vulnerability
Patch28:        sysklogd-1.4.1-CVE-2014-3634.patch
BuildRequires:  pkgconfig
BuildRequires:  group(news)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  user(news)
Requires:       klogd
Requires(post): %fillup_prereq
Requires(post): permissions
# Note: this package is for >= 12.3 only
# and does not provide LSB init scripts!
Requires(pre):  syslog-service >= 2.0
Requires(pre):  user(news)
Requires(pre):  group(news)
Conflicts:      syslog
Provides:       sysklogd
Provides:       syslog
Provides:       sysvinit(syslog)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
The syslogd daemon is the general system logging daemon, which is
responsible for handling requests for syslog services.

This version of syslogd is similar to the standard Berkeley product,
but with a number of compatible extensions.

%package -n klogd
Summary:        The kernel log daemon
Group:          System/Daemons
Requires(post): %fillup_prereq

%description -n klogd
The klogd daemon 'listens' to kernel log messages, prioritizes them,
and routes them to either output files or to syslog daemon.

This version of klogd will optionally translate kernel addresses to
their symbolic equivalents if provided with a system map.

%package -n syslog-service
Version:        2.0
Release:        0
Summary:        Syslog service files & scripts
Group:          System/Daemons
Requires:       logrotate
Requires:       syslog
Requires:       sysvinit(network)
Requires(post): %fillup_prereq
BuildArch:      noarch

%description -n syslog-service
The package syslog-service provides the service boot
scripts for SysV and the service unit files for systemd.

%prep
%setup -q -n sysklogd-1.5.1
%patch1   -b .dgram
%patch2   -b .sparc
%patch3   -b .forw
%patch5   -b .ipv6
%patch6   -b .klogd24
%patch7   -b .large
%patch8   -b .dns
%patch9   -b .reopen
%patch12  -b .klsize
%patch13  -b .usock
%patch14  -b .shprio
%patch18  -b .sleep
%patch19  -b .signal
%patch20  -b .clear
%patch21  -b .nofortify
%patch22  -b .sysmap
%patch23  -b .reload
%patch24  -b .sd
%patch25  -b .sd2
%patch26  -b .sd3
%patch28  -b .cve20143634
%patch0 -b .p0

%build
%ifarch s390 s390x
mv sample-s390.conf sample.conf
%endif
# honor the increased LOG_BUF_LEN in kernel/printk.c
make %{?_smp_mflags} BINDIR=%{_sbindir} LOG_BUFFER_SIZE=-DLOG_BUFFER_SIZE=131072

%install
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_mandir}/man{5,8}
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p -m 0755 %{buildroot}/%{_rundir}/syslogd
make install MANDIR=%{_mandir} BINDIR=%{_sbindir} DESTDIR=%{buildroot}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -m 644 %{SOURCE1} %{buildroot}%{_distconfdir}/logrotate.d/syslog
%else
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/syslog
%endif
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE3} %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE5} %{buildroot}/%{_mandir}/man8/syslog.8
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}/
install -m 644 %{SOURCE8} %{buildroot}%{_unitdir}/
install -m 755 %{SOURCE9} %{buildroot}/%{_sbindir}/
ln -s service %{buildroot}/%{_sbindir}/rcsyslogd
install -m 644 %{SOURCE12} %{buildroot}%{_fillupdir}
%if 0%{?suse_version} < 1550
for sbin in klogd syslogd ; do
	ln -sf %{_sbindir}/${sbin} %{buildroot}/sbin/${sbin}
done
%endif
%ifarch s390 s390x
sed -i 's/^KERNEL_LOGLEVEL=1/KERNEL_LOGLEVEL=7/' \
%{buildroot}%{_fillupdir}/sysconfig.klogd
%endif

%if %{defined verify_permissions}
%verifyscript
%verify_permissions -e %{_sysconfdir}/syslog.conf
%endif

%pre
%service_add_pre syslogd.service

%post
%set_permissions %{_sysconfdir}/syslog.conf
#
# add syslog variables provided by syslogd if needed
#
%{remove_and_set -n syslog SYSLOG_DAEMON}
%{remove_and_set -n syslog SYSLOG_REQUIRES_NETWORK}
%{fillup_only -ns syslog syslogd}
#
# create dirs, touch log default files
#
mkdir -p var/log
touch var/log/messages;  chmod 640 var/log/messages
touch var/log/mail;      chmod 640 var/log/mail
touch var/log/mail.info; chmod 640 var/log/mail.info
touch var/log/mail.warn; chmod 640 var/log/mail.warn
touch var/log/mail.err;  chmod 640 var/log/mail.err
test -f var/log/news && mv var/log/news var/log/news.bak
mkdir -p -m 0750 var/log/news
chown news:news  var/log/news
touch var/log/news/news.crit;   chmod 640 var/log/news/news.crit
chown news:news var/log/news/news.crit
touch var/log/news/news.err;    chmod 640 var/log/news/news.err
chown news:news var/log/news/news.err
touch var/log/news/news.notice; chmod 640 var/log/news/news.notice
chown news:news var/log/news/news.notice
#
# Enable the syslogd as service
#
# This macro enables based on a systemctl preset config file only
%service_add_post syslogd.service
# But we want to enable a syslog-daemon regardless of the preset;
# force the creation of a syslog.service alias link (bnc#790805).
# We do not check the obsolete SYSLOG_DAEMON variable as we want
# to switch when installing it and there is a provider conflict.
%{_bindir}/systemctl -f enable syslogd.service >/dev/null 2>&1 || :

%preun
%service_del_preun syslog.socket
%service_del_preun syslogd.service

%postun
%service_del_postun syslogd.service

%preun  -n syslog-service
%service_del_preun klog.service

%post -n syslog-service -p /bin/bash
%{remove_and_set -n syslog SYSLOG_DAEMON}
%{remove_and_set -n syslog SYSLOG_REQUIRES_NETWORK}
%{remove_and_set -n boot KLOGCONSOLE_PARAMS}
%{fillup_only -n boot}
#BEGIN KLOGCONSOLE_PARAMS migration
# KLOGCONSOLE_PARAMS was supported in /etc/sysconfig/boot up to Leap 15 and SLE 15.
# Based on genopts-1.3 options parser.
if test "$KLOGCONSOLE_PARAMS" != "no" ; then
 KLOG_CONSOLE=
 CONSOLE_LOGLEVEL=
 function optarg_parse {
  until [ $# -eq 0 ] ; do
   case "$1" in
   -* )
    OPTTMP="${1:1}"
    until [[ -z "$OPTTMP" ]] ; do
     case "${OPTTMP:0:1}" in
     r )
      KLOG_CONSOLE="${OPTTMP:1}"
      if [[ -z "$KLOG_CONSOLE" ]] ; then
       shift
       KLOG_CONSOLE="$1"
      else
       break
      fi
      ;;
     l )
      CONSOLE_LOGLEVEL="${OPTTMP:1}"
      if [[ -z "$CONSOLE_LOGLEVEL" ]] ; then
       shift
       CONSOLE_LOGLEVEL="$1"
      else
       break
      fi
      ;;
     esac
     OPTTMP="${OPTTMP:1}"
    done
    ;;
   esac
   shift
  done
 }
 optarg_parse $KLOGCONSOLE_PARAMS
 case "$CONSOLE_LOGLEVEL" in
 0) CONSOLE_LOGLEVEL=emerg ;;
 1) CONSOLE_LOGLEVEL=alert ;;
 2) CONSOLE_LOGLEVEL=crit ;;
 3) CONSOLE_LOGLEVEL=err ;;
 4) CONSOLE_LOGLEVEL=warning ;;
 5) CONSOLE_LOGLEVEL=notice ;;
 6) CONSOLE_LOGLEVEL=info ;;
 7) CONSOLE_LOGLEVEL=debug ;;
 esac
 unset OPTTMP
cat >%{_sysconfdir}/sysconfig/boot.update <<EOF
## Path:		System/Logging
## Description:		System logging

## Type:		list(1,2,3,4,5,6,7,8,9,10,11,12)
## Default:		10
#
# Console for logging
#
KLOG_CONSOLE="$KLOG_CONSOLE"

## Type:		list(,0,emerg,1,alert,2,crit,3,err,4,warning,5,notice,6,info,7,debug)
## Default:
#
# Loglevel for log console
#
CONSOLE_LOGLEVEL="$CONSOLE_LOGLEVEL"
EOF
 fillup -m %{_sysconfdir}/sysconfig/boot.update %{_sysconfdir}/sysconfig/boot %{_sysconfdir}/sysconfig/boot
 rm %{_sysconfdir}/sysconfig/boot.update
fi
#END KLOGCONSOLE_PARAMS migration

# when exists, remove the broken link pointing to the
# common syslog.service file, we've provided before...
rm -f %{_sysconfdir}/systemd/system/multi-user.target.wants/syslog.service
%service_add_post klog.service
%{_bindir}/systemctl -f enable klog.service >/dev/null 2>&1 || :

%pre -n syslog-service
%service_add_pre klog.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/syslog ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans  -n syslog-service
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/syslog ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%postun -n syslog-service
%service_del_postun klog.service

%pre -n klogd
%service_add_pre klogd.service

%post -n klogd
#
# add syslog variables provided by klogd if needed
#
%{remove_and_set -n syslog SYSLOG_DAEMON}
%{remove_and_set -n syslog SYSLOG_REQUIRES_NETWORK}
%{fillup_only -ns syslog klogd}
#
# Enable the syslogd as service
#
%service_add_post klogd.service

%preun -n klogd
%service_del_preun klogd.service

%postun -n klogd
%service_del_postun klogd.service

%files
%defattr(-,root,root)
%{_fillupdir}/sysconfig.syslogd
%config %verify(not mode) %attr(0600,root,root) %{_sysconfdir}/syslog.conf
%{_mandir}/man5/syslog.conf.5%{ext_man}
%{_mandir}/man8/syslogd.8%{ext_man}
%{_mandir}/man8/sysklogd.8%{ext_man}
%{_unitdir}/syslogd.service
%{_sbindir}/syslogd-service-prepare
%attr(0755,root,root) %dir %ghost %{_rundir}/syslogd
%{_sbindir}/syslogd
%{_sbindir}/rcsyslogd
%if 0%{?suse_version} < 1550
/sbin/syslogd
%endif

%files -n klogd
%defattr(-,root,root)
%{_fillupdir}/sysconfig.klogd
%{_unitdir}/klogd.service
%{_mandir}/man8/klogd.8%{ext_man}
%{_sbindir}/klogd
%if 0%{?suse_version} < 1550
/sbin/klogd
%endif

%files -n syslog-service
%defattr(-,root,root)
%{_fillupdir}/sysconfig.boot
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/syslog
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/syslog
%endif
%{_unitdir}/klog.service
%{_mandir}/man8/syslog.8%{ext_man}

%changelog
