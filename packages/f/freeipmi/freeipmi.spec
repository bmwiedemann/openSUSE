#
# spec file for package freeipmi
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2003-2008 FreeIPMI Core Team
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

%define srcversion %{version}
%if %{?_with_debug:1}%{!?_with_debug:0}
%define release 1.debug%{?dist}
%else
%define release 1%{?dist}
%endif

%define libipmiconsole_soname 2
%define libipmidetect_soname 0
%define libipmimonitoring_soname 6
%define libfreeipmi_soname 17

%{!?_initddir: %global _initddir %{_sysconfdir}/init.d}

Name:           freeipmi
Version:        1.6.14
Release:        %{release}
URL:            http://www.gnu.org/software/freeipmi/
Source0:        http://ftp.gnu.org/gnu/freeipmi/%{name}-%{srcversion}.tar.gz
Source1:        http://ftp.gnu.org/gnu/freeipmi/%{name}-%{srcversion}.tar.gz.sig
Source2:        %{name}.keyring
Patch1:         gcc-14.patch
Summary:        IPMI Service Processor, BMC management tool
License:        GPL-3.0-or-later
Group:          System/Management
BuildRequires:  fdupes
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  texinfo
BuildRequires:  pkgconfig(systemd)
%if 0%{?fedora_version} == 20 || 0%{?rhel_version} >= 700
BuildRequires:  perl-Exporter
%endif

Obsoletes:      freeipmi-ipmimonitoring < %{version}
Provides:       freeipmi-ipmimonitoring = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): info
Requires(preun): info

%description
This project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

%package devel
Summary:        Development package for FreeIPMI
Group:          Development/Tools/Other
Requires:       freeipmi = %{version}
Requires:       libfreeipmi%{libfreeipmi_soname} = %{version}
Requires:       libipmiconsole%{libipmiconsole_soname} = %{version}
Requires:       libipmidetect%{libipmidetect_soname} = %{version}
Requires:       libipmimonitoring%{libipmimonitoring_soname} = %{version}

%description devel
Development package for FreeIPMI.  This package includes the FreeIPMI
header files and static libraries.

%package bmc-watchdog
Summary:        FreeIPMI BMC watchdog
Group:          System/Management
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%{?systemd_requires}
%endif
Requires:       freeipmi = %{version}
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
Requires(post): chkconfig
Requires(preun): chkconfig
%endif
Requires:       logrotate

%description bmc-watchdog
Provides a watchdog daemon for OS monitoring and recovery.

%package ipmidetectd
Summary:        IPMI node detection monitoring daemon
Group:          System/Management
Requires:       freeipmi = %{version}
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
Requires(post): chkconfig
Requires(preun): chkconfig
%endif
%{?systemd_requires}

%description ipmidetectd
This service detects and monitors IPMI nodes.

%package ipmiseld
Summary:        Polls system event logs (SEL)
Group:          System/Management
Requires:       freeipmi = %{version}
Provides:       freeipmi:/usr/sbin/ipmiseld
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
Requires(post): chkconfig
Requires(preun): chkconfig
%endif
%{?systemd_requires}

%description ipmiseld
The daemon  polls  the system event log (SEL) of specified hosts and stores the
logs into the local syslog. By default, the daemon can also make best efforts
to manage the remote SEL buffer to ensure events are never lost.
Recent logging data will be cached to disk to ensure that SEL events are
not missed in the event the client or server is rebooted.

%if %{?_with_debug:1}%{!?_with_debug:0}
  %define _enable_debug --enable-debug --enable-trace
%endif

%package -n libipmiconsole%{libipmiconsole_soname}
Summary:        FreeIPMI library
Group:          System/Libraries

%description -n libipmiconsole%{libipmiconsole_soname}
This project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

This package contains the libipmiconsole library.

%package -n libipmidetect%{libipmidetect_soname}
Summary:        FreeIPMI library
Group:          System/Libraries

%description -n libipmidetect%{libipmidetect_soname}
This project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

This package contains the libipmidetect library.

%package -n libipmimonitoring%{libipmimonitoring_soname}
Summary:        FreeIPMI library
Group:          System/Libraries

%description -n libipmimonitoring%{libipmimonitoring_soname}
This project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

This package contains the libipmimonitoring library.

%package -n libfreeipmi%{libfreeipmi_soname}
Summary:        FreeIPMI library
Group:          System/Libraries

%description -n libfreeipmi%{libfreeipmi_soname}
This project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

This package contains the libfreeipmi library.

%prep
%autosetup -p1 -n %{name}-%{srcversion}

%build
# simple .spec expressions for SLE10

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version}
%if 0%{?fedora_version} < 21
%define docpath %{_docdir}/%{name}-%{version}
%else
%define docpath %{_docdir}/%{name}
%endif
%else
%define docpath %{_docdir}/%{name}
%endif

%define configure_systemd --with-systemdsystemunitdir=%{_unitdir}

%configure --program-prefix=%{?_program_prefix:%{_program_prefix}} \
           --docdir=%{docpath} \
           %{?configure_systemd} \
           %{?_enable_debug} --disable-static
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
mkdir -p %{buildroot}

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
# /etc/rc.d/init.d
# 'make install' installs to /etc/init.d
# /etc/init.d -> /etc/rc.d/init.d
mkdir -p %{buildroot}/%{_sysconfdir}/rc.d/init.d
(cd %{buildroot}/%{_sysconfdir}; ln -s rc.d/init.d init.d)
%endif

%if 0%{?suse_version}
%makeinstall
%else
make install DESTDIR=%{buildroot}
%endif

mkdir -p %{buildroot}%{_datadir}/doc/packages/freeipmi-bmc-watchdog
mv %{buildroot}%{_datadir}/doc/packages/freeipmi/*bmc-watchdog* %{buildroot}%{_datadir}/doc/packages/freeipmi-bmc-watchdog
mkdir -p %{buildroot}%{_datadir}/doc/packages/freeipmi-ipmiseld
mv %{buildroot}%{_datadir}/doc/packages/freeipmi/*ipmiseld* %{buildroot}%{_datadir}/doc/packages/freeipmi-ipmiseld

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcbmc-watchdog
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcipmidetectd
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcipmiseld

# Silent build check warning
rm -f %{buildroot}%{_datadir}/doc/packages/freeipmi/INSTALL
rm -rf %{buildroot}%{_datadir}/doc/packages/freeipmi/contrib
rm -rf %{buildroot}%{_datadir}/doc/packages/freeipmi/freeipmi-design.txt
rm -rf %{buildroot}%{_datadir}/doc/packages/freeipmi/freeipmi-testing.txt

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
# remove /etc/init.d -> /etc/rc.d/init.d
(cd %{buildroot}/%{_sysconfdir}; rm init.d)
%endif

# fix coherance problems with associated script filenames
rm -f %{buildroot}%{_infodir}/dir
# Remove .la files
rm -rf %{buildroot}/%{_libdir}/*.la

%if 0%{?suse_version}
mkdir -p %{buildroot}%{_fillupdir}
mv %{buildroot}%{_sysconfdir}/sysconfig/bmc-watchdog %{buildroot}%{_fillupdir}/sysconfig.bmc-watchdog
%endif

%if 0%{?suse_version} > 1010
%fdupes $RPM_BUILD_ROOT
%endif

%post
if [ -x /sbin/install-info ]; then
   /sbin/install-info %{_infodir}/freeipmi-faq.info.gz %{_infodir}/dir
fi
/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
   if [ -x /sbin/install-info ]; then
      /sbin/install-info --delete %{_infodir}/freeipmi-faq.info.gz %{_infodir}/dir
   fi
fi

%postun -p /sbin/ldconfig

%post   -n libipmiconsole%{libipmiconsole_soname} -p /sbin/ldconfig
%postun -n libipmiconsole%{libipmiconsole_soname} -p /sbin/ldconfig

%post   -n libipmidetect%{libipmidetect_soname} -p /sbin/ldconfig
%postun -n libipmidetect%{libipmidetect_soname} -p /sbin/ldconfig

%post   -n libipmimonitoring%{libipmimonitoring_soname} -p /sbin/ldconfig
%postun -n libipmimonitoring%{libipmimonitoring_soname} -p /sbin/ldconfig

%post   -n libfreeipmi%{libfreeipmi_soname} -p /sbin/ldconfig
%postun -n libfreeipmi%{libfreeipmi_soname} -p /sbin/ldconfig

%post bmc-watchdog
%if 0%{?suse_version}
%{fillup_only}
%endif
%service_add_post bmc-watchdog.service

%pre bmc-watchdog
%service_add_pre bmc-watchdog.service

%postun bmc-watchdog
%service_del_postun bmc-watchdog.service

%preun bmc-watchdog
%service_del_preun bmc-watchdog.service

%post ipmidetectd
%service_add_post ipmidetectd.service

%pre ipmidetectd
%service_add_pre ipmidetectd.service

%postun ipmidetectd
%service_del_postun ipmidetectd.service

%preun ipmidetectd
%service_del_preun ipmidetectd.service

%post ipmiseld
%service_add_post ipmiseld.service

%pre ipmiseld
%service_add_pre ipmiseld.service

%preun ipmiseld
%service_del_preun ipmiseld.service
# Could have several files and files with hostname ghost directive
# might not work
rm -rf %{_localstatedir}/cache/ipmiseld/*

%postun ipmiseld
%service_del_postun ipmiseld.service

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/freeipmi/freeipmi.conf
%dir %{_sysconfdir}/freeipmi
%config %{_sysconfdir}/freeipmi/freeipmi_interpret_sel.conf
%config %{_sysconfdir}/freeipmi/freeipmi_interpret_sensor.conf
%config %{_sysconfdir}/freeipmi/ipmidetect.conf
%config %{_sysconfdir}/freeipmi/libipmiconsole.conf
%doc AUTHORS
%license %docpath/COPYING
%doc ChangeLog
%doc ChangeLog.0
%doc NEWS
%doc README
%doc README.argp
%doc README.build
%doc README.openipmi
%doc TODO
%doc %{_infodir}/*
%license %docpath/COPYING.ipmiping
%license %docpath/COPYING.ipmipower
%license %docpath/COPYING.ipmiconsole
%license %docpath/COPYING.ipmimonitoring
%license %docpath/COPYING.pstdout
%license %docpath/COPYING.ipmidetect
%license %docpath/COPYING.ipmi-fru
%license %docpath/COPYING.ZRESEARCH
%license %docpath/COPYING.ipmi-dcmi
%license %docpath/COPYING.sunbmc
%license %docpath/DISCLAIMER.ipmiping
%license %docpath/DISCLAIMER.ipmipower
%license %docpath/DISCLAIMER.ipmiconsole
%license %docpath/DISCLAIMER.ipmidetect
%license %docpath/DISCLAIMER.ipmimonitoring
%license %docpath/DISCLAIMER.pstdout
%license %docpath/DISCLAIMER.ipmi-fru
%license %docpath/DISCLAIMER.ipmiping.UC
%license %docpath/DISCLAIMER.ipmipower.UC
%license %docpath/DISCLAIMER.ipmiconsole.UC
%license %docpath/DISCLAIMER.ipmimonitoring.UC
%license %docpath/DISCLAIMER.pstdout.UC
%license %docpath/DISCLAIMER.ipmidetect.UC
%license %docpath/DISCLAIMER.ipmi-fru.UC
%license %docpath/DISCLAIMER.ipmi-dcmi
%doc doc/freeipmi-coding.txt
%doc doc/freeipmi-hostrange.txt
%doc doc/freeipmi-libraries.txt
%doc doc/freeipmi-bugs-issues-and-workarounds.txt
%doc doc/freeipmi-oem-documentation-requirements.txt

%if 0%{?fedora_version} == 20
%{docpath}
%endif
%dir %{_localstatedir}/lib/freeipmi
%ghost %{_localstatedir}/lib/freeipmi/ipckey
%{_sbindir}/ipmi-config
%{_sbindir}/bmc-config
%{_sbindir}/bmc-info
%{_sbindir}/bmc-device
%{_sbindir}/ipmi-fru
%{_sbindir}/ipmi-locate
%{_sbindir}/ipmi-oem
%{_sbindir}/ipmi-pef-config
%{_sbindir}/pef-config
%{_sbindir}/ipmi-raw
%{_sbindir}/ipmi-sel
%{_sbindir}/ipmi-sensors
%{_sbindir}/ipmi-sensors-config
%{_sbindir}/ipmiping
%{_sbindir}/ipmipower
%{_sbindir}/ipmiconsole
%{_sbindir}/ipmimonitoring
%{_sbindir}/ipmi-chassis
%{_sbindir}/ipmi-chassis-config
%{_sbindir}/ipmi-dcmi
%{_sbindir}/ipmidetect
%{_sbindir}/ipmi-console
%{_sbindir}/ipmi-detect
%{_sbindir}/ipmi-ping
%{_sbindir}/ipmi-power
%{_sbindir}/rmcp-ping
%{_sbindir}/rmcpping
%{_sbindir}/ipmi-pet
%{_mandir}/man8/bmc-config.8*
%{_mandir}/man5/bmc-config.conf.5*
%{_mandir}/man8/bmc-info.8*
%{_mandir}/man8/bmc-device.8*
%{_mandir}/man8/ipmi-fru.8*
%{_mandir}/man8/ipmi-locate.8*
%{_mandir}/man8/ipmi-pef-config.8*
%{_mandir}/man8/ipmi-config.8*
%{_mandir}/man5/ipmi-config.conf.5*
%{_mandir}/man8/pef-config.8*
%{_mandir}/man8/ipmi-oem.8*
%{_mandir}/man8/ipmi-raw.8*
%{_mandir}/man8/ipmi-sel.8*
%{_mandir}/man8/ipmi-sensors.8*
%{_mandir}/man8/ipmi-sensors-config.8*
%{_mandir}/man8/ipmiping.8*
%{_mandir}/man8/ipmipower.8*
%{_mandir}/man5/ipmipower.conf.5*
%{_mandir}/man8/ipmiconsole.8*
%{_mandir}/man5/ipmiconsole.conf.5*
%{_mandir}/man8/ipmimonitoring.8*
%{_mandir}/man5/ipmi_monitoring_sensors.conf.5*
%{_mandir}/man5/ipmimonitoring_sensors.conf.5*
%{_mandir}/man5/ipmimonitoring.conf.5*
%{_mandir}/man5/libipmimonitoring.conf.5*
%{_mandir}/man8/ipmi-chassis.8*
%{_mandir}/man8/ipmi-chassis-config.8*
%{_mandir}/man8/ipmi-dcmi.8*
%{_mandir}/man8/ipmidetect.8*
%{_mandir}/man5/freeipmi.conf.5*
%{_mandir}/man5/ipmidetect.conf.5*
%{_mandir}/man7/freeipmi.7*
%{_mandir}/man8/rmcp-ping.8*
%{_mandir}/man8/rmcpping.8*
%{_mandir}/man5/freeipmi_interpret_sel.conf.5*
%{_mandir}/man5/freeipmi_interpret_sensor.conf.5*
%{_mandir}/man5/libipmiconsole.conf.5*
%{_mandir}/man8/ipmi-console.8*
%{_mandir}/man8/ipmi-detect.8*
%{_mandir}/man8/ipmi-ping.8*
%{_mandir}/man8/ipmi-power.8*
%{_mandir}/man8/ipmi-pet.8*
%dir %{_localstatedir}/cache/ipmimonitoringsdrcache

%files devel
%defattr(-,root,root)
%{_libdir}/libipmiconsole.so
%{_libdir}/libfreeipmi.so
%{_libdir}/libipmidetect.so
%{_libdir}/libipmimonitoring.so
%{_libdir}/pkgconfig/*
%dir %{_includedir}/freeipmi
%dir %{_includedir}/freeipmi/api
%dir %{_includedir}/freeipmi/cmds
%dir %{_includedir}/freeipmi/debug
%dir %{_includedir}/freeipmi/driver
%dir %{_includedir}/freeipmi/fiid
%dir %{_includedir}/freeipmi/fru
%dir %{_includedir}/freeipmi/interface
%dir %{_includedir}/freeipmi/interpret
%dir %{_includedir}/freeipmi/locate
%dir %{_includedir}/freeipmi/payload
%dir %{_includedir}/freeipmi/record-format
%dir %{_includedir}/freeipmi/record-format/oem
%dir %{_includedir}/freeipmi/sdr
%dir %{_includedir}/freeipmi/sdr/oem
%dir %{_includedir}/freeipmi/sel
%dir %{_includedir}/freeipmi/sensor-read
%dir %{_includedir}/freeipmi/spec
%dir %{_includedir}/freeipmi/spec/oem
%dir %{_includedir}/freeipmi/templates
%dir %{_includedir}/freeipmi/templates/oem
%dir %{_includedir}/freeipmi/util

%{_includedir}/ipmiconsole.h
%{_includedir}/ipmidetect.h
%{_includedir}/ipmi_monitoring.h
%{_includedir}/ipmi_monitoring_bitmasks.h
%{_includedir}/ipmi_monitoring_offsets.h
%{_includedir}/freeipmi/*.h
%{_includedir}/freeipmi/api/*.h
%{_includedir}/freeipmi/cmds/*.h
%{_includedir}/freeipmi/debug/*.h
%{_includedir}/freeipmi/driver/*.h
%{_includedir}/freeipmi/fiid/*.h
%{_includedir}/freeipmi/fru/*.h
%{_includedir}/freeipmi/interface/*.h
%{_includedir}/freeipmi/interpret/ipmi-interpret.h
%{_includedir}/freeipmi/locate/*.h
%{_includedir}/freeipmi/payload/ipmi-sol-payload.h
%{_includedir}/freeipmi/record-format/*.h
%{_includedir}/freeipmi/record-format/oem/*.h
%{_includedir}/freeipmi/sdr/*.h
%{_includedir}/freeipmi/sdr/oem/*.h
%{_includedir}/freeipmi/sel/*.h
%{_includedir}/freeipmi/sensor-read/*.h
%{_includedir}/freeipmi/spec/*.h
%{_includedir}/freeipmi/spec/oem/*.h
%{_includedir}/freeipmi/templates/*.h
%{_includedir}/freeipmi/templates/oem/*.h
%{_includedir}/freeipmi/util/*.h
%{_mandir}/man3/*

%files bmc-watchdog
%defattr(-,root,root)
%dir %{_docdir}/freeipmi-bmc-watchdog
%license %{_docdir}/freeipmi-bmc-watchdog/COPYING.bmc-watchdog
%license %{_docdir}/freeipmi-bmc-watchdog/DISCLAIMER.bmc-watchdog
%license %{_docdir}/freeipmi-bmc-watchdog/DISCLAIMER.bmc-watchdog.UC
%{_unitdir}/bmc-watchdog.service
%if 0%{?suse_version}
%attr(0444,root,root) %{_fillupdir}/sysconfig.bmc-watchdog
%else
%attr(0444,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/bmc-watchdog
%endif
%{_sbindir}/bmc-watchdog
%{_sbindir}/rcbmc-watchdog
%{_mandir}/man8/bmc-watchdog.8*

%files ipmidetectd
%defattr(-,root,root)
%{_unitdir}/ipmidetectd.service
%attr(0444,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/ipmidetectd.conf
%{_sbindir}/ipmidetectd
%{_sbindir}/rcipmidetectd
%{_mandir}/man5/ipmidetectd.conf.5*
%{_mandir}/man8/ipmidetectd.8*

%files ipmiseld
%defattr(-,root,root)
%config %{_sysconfdir}/freeipmi/ipmiseld.conf
%dir %{_localstatedir}/cache/ipmiseld
%{_unitdir}/ipmiseld.service
%{_sbindir}/ipmiseld
%{_sbindir}/rcipmiseld
%{_mandir}/man5/ipmiseld.conf.5*
%{_mandir}/man8/ipmiseld.8*
%dir %{_docdir}/freeipmi-ipmiseld
%license %{_docdir}/freeipmi-ipmiseld/COPYING.ipmiseld
%license %{_docdir}/freeipmi-ipmiseld/DISCLAIMER.ipmiseld

%files -n libipmiconsole%{libipmiconsole_soname}
%defattr(-,root,root)
%{_libdir}/libipmiconsole*so.%{libipmiconsole_soname}*

%files -n libipmidetect%{libipmidetect_soname}
%defattr(-,root,root)
%{_libdir}/libipmidetect*so.%{libipmidetect_soname}*

%files -n libipmimonitoring%{libipmimonitoring_soname}
%defattr(-,root,root)
%{_libdir}/libipmimonitoring.so.%{libipmimonitoring_soname}*

%files -n libfreeipmi%{libfreeipmi_soname}
%defattr(-,root,root)
%{_libdir}/libfreeipmi*so.%{libfreeipmi_soname}*

%changelog
