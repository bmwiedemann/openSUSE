#
# spec file for package ipmiutil
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ipmiutil
Version:        3.0.7
Release:        1%{?dist}
Summary:        Easy-to-use IPMI server management utilities
License:        BSD-3-Clause
Group:          System/Management
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Url:            http://ipmiutil.sourceforge.net
Patch0:         warnings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?sles_version} > 10
%define bldreq0 libopenssl-devel 
%else
%define bldreq0 openssl-devel 
%endif
%if 0%{?suse_version} >= 1210
%define req_systemd 1
%endif
%{!?_unitdir: %define _unitdir  /usr/lib/systemd/system}
%define unit_dir  %{_unitdir}
%if 0%{?req_systemd}
BuildRequires:  systemd
%define systemd_fls %{_unitdir}
%else
%define systemd_fls %{_datadir}/%{name}
%endif
BuildRequires:  autoconf automake %{bldreq0} 
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl(Exporter)

%define init_dir  %{_initrddir}

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

%build
autoreconf -fiv
%if 0%{?req_systemd}
%configure --enable-systemd
%else
%configure
%endif
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
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
%{systemd_fls}/ipmiutil_evt.service
%{systemd_fls}/ipmiutil_asy.service
%{systemd_fls}/ipmiutil_wdt.service
%{systemd_fls}/ipmi_port.service
%{_datadir}/%{name}/ipmiutil.env
%{_datadir}/%{name}/ipmiutil.pre
%{_datadir}/%{name}/ipmiutil.setup
%{_datadir}/%{name}/ipmi_if.sh
%{_datadir}/%{name}/evt.sh
%{_datadir}/%{name}/ipmi.init.basic
%{_datadir}/%{name}/bmclanpet.mib
%{_mandir}/man8/isel.8*
%{_mandir}/man8/isensor.8*
%{_mandir}/man8/ireset.8*
%{_mandir}/man8/igetevent.8*
%{_mandir}/man8/ihealth.8*
%{_mandir}/man8/iconfig.8*
%{_mandir}/man8/ialarms.8*
%{_mandir}/man8/iwdt.8*
%{_mandir}/man8/ilan.8*
%{_mandir}/man8/iserial.8*
%{_mandir}/man8/ifru.8*
%{_mandir}/man8/icmd.8*
%{_mandir}/man8/isol.8*
%{_mandir}/man8/ipmiutil.8*
%{_mandir}/man8/idiscover.8*
%{_mandir}/man8/ievents.8*
%{_mandir}/man8/ipmi_port.8*
%{_mandir}/man8/ipicmg.8*
%{_mandir}/man8/ifirewall.8*
%{_mandir}/man8/ifwum.8*
%{_mandir}/man8/ihpm.8*
%{_mandir}/man8/isunoem.8*
%{_mandir}/man8/idelloem.8*
%{_mandir}/man8/ismcoem.8*
%{_mandir}/man8/iekanalyzer.8*
%{_mandir}/man8/itsol.8*
%{_mandir}/man8/idcmi.8*
%{_mandir}/man8/iuser.8*
%doc AUTHORS ChangeLog COPYING NEWS README TODO 
%doc doc/UserGuide

%files devel
%defattr(-,root,root)
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
%defattr(-,root,root)
%{_libdir}/libipmiutil.a

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%pre
%if 0%{?req_systemd}
%service_add_pre ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%endif

%post
# POST_INSTALL, $1 = 1 if rpm -i, $1 = 2 if rpm -U
/sbin/ldconfig
if [ "$1" = "1" ]
then
   # doing rpm -i, first time
   vardir=%{_var}/lib/%{name}
   scr_dir=%{_datadir}/%{name}

%if 0%{?req_systemd}
%service_add_post ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%else
   if [ -x /bin/systemctl ] && [ -d %{unit_dir} ]; then
      echo "IINITDIR=%{init_dir}" >>%{_datadir}/%{name}/ipmiutil.env
      cp -f ${scr_dir}/ipmiutil_evt.service %{unit_dir}
      cp -f ${scr_dir}/ipmiutil_asy.service %{unit_dir}
      cp -f ${scr_dir}/ipmiutil_wdt.service %{unit_dir}
      cp -f ${scr_dir}/ipmi_port.service    %{unit_dir}
      # systemctl enable ipmi_port.service >/dev/null 2>&1 || :
   else 
      cp -f ${scr_dir}/ipmiutil_wdt %{init_dir}
      cp -f ${scr_dir}/ipmiutil_asy %{init_dir}
      cp -f ${scr_dir}/ipmiutil_evt %{init_dir}
      cp -f ${scr_dir}/ipmi_port    %{init_dir}
      cp -f ${scr_dir}/ipmi_info    %{init_dir}
   fi
%endif

   # Test whether an IPMI interface is known to the motherboard
   IPMIret=1
   which dmidecode >/dev/null 2>&1 && IPMIret=0
   if [ $IPMIret -eq 0 ]; then
    %{_sbindir}/dmidecode |grep -q IPMI && IPMIret=0
    if [ $IPMIret -eq 0 ]; then
     # Run some ipmiutil command to see if any IPMI interface works.
     # Some may not have IPMI on the motherboard, so need to check, but
     # some kernels may have IPMI driver partially loaded, which breaks this
     %{_bindir}/ipmiutil sel -v >/dev/null 2>&1 && IPMIret=0
     if [ $IPMIret -eq 0 ]; then
      if [ ! -x %{init_dir}/ipmi ]; then
         cp -f %{scr_dir}/ipmi.init.basic  %{init_dir}/ipmi
      fi
      # If IPMI is enabled, automate managing the IPMI SEL
      if [ -d %{_sysconfdir}/cron.daily ]; then
         cp -f %{_datadir}/%{name}/checksel %{_sysconfdir}/cron.daily
      fi
      # IPMI_IS_ENABLED, so enable services, but only if Red Hat
      if [ -f /etc/redhat-release ]; then
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
%if 0%{?req_systemd}
%service_del_preun ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%else
   if [ -x /bin/systemctl ]; then
     if [ -f %{unit_dir}/ipmiutil_evt.service ]; then
        systemctl disable ipmi_port.service >/dev/null 2>&1 || :
        systemctl disable ipmiutil_evt.service >/dev/null 2>&1 || :
        systemctl disable ipmiutil_asy.service >/dev/null 2>&1 || :
        systemctl disable ipmiutil_wdt.service >/dev/null 2>&1 || :
        systemctl stop ipmiutil_evt.service >/dev/null 2>&1 || :
        systemctl stop ipmiutil_asy.service >/dev/null 2>&1 || :
        systemctl stop ipmiutil_wdt.service >/dev/null 2>&1 || :
        systemctl stop ipmi_port.service    >/dev/null 2>&1 || :
     fi
   else 
     if [ -x /sbin/service ]; then
        /sbin/service ipmi_port stop       >/dev/null 2>&1 || :
        /sbin/service ipmiutil_wdt stop    >/dev/null 2>&1 || :
        /sbin/service ipmiutil_asy stop    >/dev/null 2>&1 || :
        /sbin/service ipmiutil_evt stop    >/dev/null 2>&1 || :
     fi
     if [ -x /sbin/chkconfig ]; then
        /sbin/chkconfig --del ipmi_port    >/dev/null 2>&1 || :
        /sbin/chkconfig --del ipmiutil_wdt >/dev/null 2>&1 || :
        /sbin/chkconfig --del ipmiutil_asy >/dev/null 2>&1 || :
        /sbin/chkconfig --del ipmiutil_evt >/dev/null 2>&1 || :
     fi
   fi
%endif
   if [ -f %{_sysconfdir}/cron.daily/checksel ]; then
	rm -f %{_sysconfdir}/cron.daily/checksel
   fi
fi

%postun
# after uninstall,  $1 = 1 if update, $1 = 0 if rpm -e
/sbin/ldconfig
%if 0%{?req_systemd}
%service_del_postun ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%else
if [ -x /bin/systemctl ]; then
   systemctl daemon-reload  || :
   if [ $1 -ge 1 ] ; then
	# Package upgrade, not uninstall
	systemctl try-restart ipmi_port.service  || :
   fi
   if [ -f %{unit_dir}/ipmiutil_evt.service ]; then
      rm -f %{unit_dir}/ipmiutil_evt.service  2>/dev/null || :
      rm -f %{unit_dir}/ipmiutil_asy.service  2>/dev/null || :
      rm -f %{unit_dir}/ipmiutil_wdt.service  2>/dev/null || :
      rm -f %{unit_dir}/ipmi_port.service     2>/dev/null || :
   fi
else
   if [ -f %{init_dir}/ipmiutil_evt.service ]; then
      rm -f %{init_dir}/ipmiutil_wdt 2>/dev/null || :
      rm -f %{init_dir}/ipmiutil_asy 2>/dev/null || :
      rm -f %{init_dir}/ipmiutil_evt 2>/dev/null || :
      rm -f %{init_dir}/ipmi_port    2>/dev/null || :
   fi
fi
%endif

%changelog
