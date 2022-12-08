#
# spec file for package ipmiutil
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Andy Cress
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


%{!?_unitdir: %define _unitdir  %{_prefix}/lib/systemd/system}
Name:           ipmiutil
Version:        3.1.8
Release:        0
Summary:        Easy-to-use IPMI server management utilities
License:        BSD-3-Clause
Group:          System/Management
URL:            http://ipmiutil.sourceforge.net
Source:         https://sourceforge.net/projects/ipmiutil/files/%{name}-%{version}.tar.gz
Patch0:         harden_ipmi_port.service.patch
Patch1:         harden_ipmiutil_asy.service.patch
Patch2:         harden_ipmiutil_evt.service.patch
Patch3:         harden_ipmiutil_wdt.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  perl(Exporter)
BuildRequires:  pkgconfig(systemd)

%description
The ipmiutil package provides easy-to-use utilities to view the SEL,
perform an IPMI chassis reset, set up the IPMI LAN and Platform Event Filter
entries to allow SNMP alerts, Serial-Over-LAN console, event daemon, and
other IPMI tasks.
These can be invoked with the metacommand ipmiutil, or via subcommand
shortcuts as well.  IPMIUTIL can also write sensor thresholds, FRU asset tags,
and has a full IPMI configuration save/restore.
An IPMI driver can be provided by either the OpenIPMI driver (/dev/ipmi0)
or the Intel IPMI driver (/dev/imb), etc.  If used locally and no driver is
detected, ipmiutil will use user-space direct I/Os instead.

%package devel
Summary:        Includes libraries and headers for the ipmiutil package
Group:          Development/Libraries/C and C++
Requires:       ipmiutil >= %{version}

%description devel
The ipmiutil-devel package contains headers and libraries which are
useful for building custom IPMI applications.

%package static
Summary:        Includes static libraries for the ipmiutil package
Group:          Development/Libraries/C and C++
Requires:       ipmiutil >= %{version}

%description static
The ipmiutil-static package contains static libraries which are
useful for building custom IPMI applications.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure --enable-systemd
%make_build

%install
%make_install

%files
%dir %{_datadir}/%{name}
%dir %{_var}/lib/%{name}
%{_bindir}/ipmiutil
%{_bindir}/idiscover
%{_bindir}/ievents
%{_sbindir}/iseltime
%{_sbindir}/ipmi_port
%{_sbindir}/ialarms
%{_sbindir}/iconfig
%{_sbindir}/icmd
%{_sbindir}/ifru
%{_sbindir}/igetevent
%{_sbindir}/ihealth
%{_sbindir}/ilan
%{_sbindir}/ireset
%{_sbindir}/isel
%{_sbindir}/isensor
%{_sbindir}/iserial
%{_sbindir}/isol
%{_sbindir}/iwdt
%{_sbindir}/ipicmg
%{_sbindir}/ifirewall
%{_sbindir}/ifwum
%{_sbindir}/ihpm
%{_sbindir}/iuser
%{_datadir}/%{name}/ipmiutil_evt
%{_datadir}/%{name}/ipmiutil_asy
%{_datadir}/%{name}/ipmiutil_wdt
%{_datadir}/%{name}/ipmi_port
%{_datadir}/%{name}/ipmi_info
%{_datadir}/%{name}/checksel
%{_unitdir}/ipmiutil_evt.service
%{_unitdir}/ipmiutil_asy.service
%{_unitdir}/ipmiutil_wdt.service
%{_unitdir}/ipmi_port.service
%{_datadir}/%{name}/ipmiutil.pre
%{_datadir}/%{name}/ipmiutil.setup
%{_datadir}/%{name}/ipmi_if.sh
%{_datadir}/%{name}/evt.sh
%{_datadir}/%{name}/ipmi.init.basic
%{_datadir}/%{name}/bmclanpet.mib
%{_datadir}/%{name}/ipmiutil.env.template
%{_mandir}/man8/isel.8%{?ext_man}
%{_mandir}/man8/isensor.8%{?ext_man}
%{_mandir}/man8/ireset.8%{?ext_man}
%{_mandir}/man8/igetevent.8%{?ext_man}
%{_mandir}/man8/ihealth.8%{?ext_man}
%{_mandir}/man8/iconfig.8%{?ext_man}
%{_mandir}/man8/ialarms.8%{?ext_man}
%{_mandir}/man8/iwdt.8%{?ext_man}
%{_mandir}/man8/ilan.8%{?ext_man}
%{_mandir}/man8/iserial.8%{?ext_man}
%{_mandir}/man8/ifru.8%{?ext_man}
%{_mandir}/man8/icmd.8%{?ext_man}
%{_mandir}/man8/isol.8%{?ext_man}
%{_mandir}/man8/ipmiutil.8%{?ext_man}
%{_mandir}/man8/idiscover.8%{?ext_man}
%{_mandir}/man8/ievents.8%{?ext_man}
%{_mandir}/man8/ipmi_port.8%{?ext_man}
%{_mandir}/man8/ipicmg.8%{?ext_man}
%{_mandir}/man8/ifirewall.8%{?ext_man}
%{_mandir}/man8/ifwum.8%{?ext_man}
%{_mandir}/man8/ihpm.8%{?ext_man}
%{_mandir}/man8/isunoem.8%{?ext_man}
%{_mandir}/man8/idelloem.8%{?ext_man}
%{_mandir}/man8/ismcoem.8%{?ext_man}
%{_mandir}/man8/iseltime.8%{?ext_man}
%{_mandir}/man8/iekanalyzer.8%{?ext_man}
%{_mandir}/man8/itsol.8%{?ext_man}
%{_mandir}/man8/idcmi.8%{?ext_man}
%{_mandir}/man8/iuser.8%{?ext_man}
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/UserGuide

%files devel
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ipmi_sample.c
%{_datadir}/%{name}/ipmi_sample_evt.c
%{_datadir}/%{name}/isensor.c
%{_datadir}/%{name}/ievents.c
%{_datadir}/%{name}/isensor.h
%{_datadir}/%{name}/ievents.h
%{_datadir}/%{name}/Makefile
%{_libdir}/libipmiutil.so.1
%{_libdir}/libipmiutil.so
%{_includedir}/ipmicmd.h

%files static
%{_libdir}/libipmiutil.a

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%pre
%service_add_pre ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service

%post
# POST_INSTALL, $1 = 1 if rpm -i, $1 = 2 if rpm -U
/sbin/ldconfig
if [ "$1" = "1" ]
then
   # doing rpm -i, first time
   vardir=%{_var}/lib/%{name}
   scr_dir=%{_datadir}/%{name}

%service_add_post ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service

   # Test whether an IPMI interface is known to the motherboard
   IPMIret=1
   which dmidecode >/dev/null 2>&1 && IPMIret=0
   if [ $IPMIret -eq 0 ]; then
    IPMIret=1
    %{_sbindir}/dmidecode |grep -q IPMI && IPMIret=0
    if [ $IPMIret -eq 0 ]; then
     IPMIret=1
     # Run some ipmiutil command to see if any IPMI interface works.
     # Some may not have IPMI on the motherboard, so need to check, but
     # some kernels may have IPMI driver partially loaded, which breaks this
     %{_bindir}/ipmiutil sel -v >/dev/null 2>&1 && IPMIret=0
     if [ $IPMIret -eq 0 ]; then
      if [ ! -x %{_initddir}/ipmi ]; then
         cp -f %{scr_dir}/ipmi.init.basic  %{_initddir}/ipmi
      fi
      # If IPMI is enabled, automate managing the IPMI SEL
      if [ -d %{_sysconfdir}/cron.daily ]; then
         cp -f %{_datadir}/%{name}/checksel %{_sysconfdir}/cron.daily
      fi
      # IPMI_IS_ENABLED, so enable services, but only if Red Hat
      if [ -f %{_sysconfdir}/redhat-release ]; then
         if [ -x /bin/systemctl ]; then
            touch ${scr_dir}/ipmi_port.service
         elif [ -x /sbin/chkconfig ]; then
            /sbin/chkconfig --add ipmi_port
            /sbin/chkconfig --add ipmi_info
            # /sbin/chkconfig --add ipmiutil_wdt
            # /sbin/chkconfig --add ipmiutil_evt
         fi
      fi

      # Capture a snapshot of IPMI sensor data once now for later reuse.
      sensorout=$vardir/sensor_out.txt
      if [ ! -f $sensorout ]; then
         %{_bindir}/ipmiutil sensor -q >$sensorout || :
         if [ $? -ne 0 ]; then
           # remove file if error, try again in ipmi_port on reboot.
           rm -f $sensorout
         fi
      fi
     fi
    fi
   fi
else
   # postinstall, doing rpm update
   IPMIret=1
   which dmidecode >/dev/null 2>&1 && IPMIret=0
   if [ $IPMIret -eq 0 ]; then
    IPMIret=1
    %{_sbindir}/dmidecode |grep -q IPMI && IPMIret=0
    if [ $IPMIret -eq 0 ]; then
      if [ -d %{_sysconfdir}/cron.daily ]; then
         cp -f %{_datadir}/%{name}/checksel %{_sysconfdir}/cron.daily
      fi
    fi
   fi
fi

%preun
# before uninstall,  $1 = 1 if rpm -U, $1 = 0 if rpm -e
if [ "$1" = "0" ]
then
%service_del_preun ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
   if [ -f %{_sysconfdir}/cron.daily/checksel ]; then
	rm -f %{_sysconfdir}/cron.daily/checksel
   fi
fi

%postun
# after uninstall,  $1 = 1 if update, $1 = 0 if rpm -e
/sbin/ldconfig
%service_del_postun ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service

%changelog
