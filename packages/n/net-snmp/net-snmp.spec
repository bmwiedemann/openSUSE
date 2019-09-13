#
# spec file for package net-snmp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define netsnmp_logfile %{_localstatedir}/log/net-snmpd.log
%define netsnmp_agentx_socket_dir_fhs %{_rundir}/agentx
%define netsnmp_agentx_socket_dir_rfc %{_localstatedir}/agentx
# Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%ifnarch s390 s390x
%define netsnmp_with_sensors 1
%endif
%define libname libsnmp30
%bcond_without python2
Name:           net-snmp
Version:        5.8
Release:        0
Summary:        SNMP Daemon
License:        BSD-3-Clause AND MIT
Group:          Productivity/Networking/Other
Url:            http://sourceforge.net/projects/net-snmp
Source:         http://sourceforge.net/projects/net-snmp/files/net-snmp/%{version}/%{name}-%{version}.tar.gz
Source1:        snmpd.service
Source2:        snmpd.conf
Source3:        README.SUSE
Source4:        snmptrapd.service
Source5:        net-snmp.logrotate
Source6:        test_installed
Source10:       snmpd.sysconfig
Source11:       snmptrapd.sysconfig
Source20:       net-snmp-tmpfs.conf
Source98:       net-snmp-rpmlintrc
Source99:       baselibs.conf
Patch1:         net-snmp-5.8-socket-path.patch
Patch2:         net-snmp-5.8-testing-empty-arptable.patch
Patch3:         net-snmp-5.8-pie.patch
Patch4:         net-snmp-5.8-net-snmp-config-headercheck.patch
Patch5:         net-snmp-5.8-perl-tk-warning.patch
Patch6:         net-snmp-5.8-velocity-mib.patch
Patch7:         net-snmp-5.8-netgroups.patch
Patch8:         net-snmp-5.8-snmpstatus-suppress-output.patch
Patch9:         net-snmp-5.8-fix-Makefile.PL.patch
Patch10:        net-snmp-5.8-modern-rpm-api.patch
Patch11:        net-snmp-5.8-fix-python3.patch
Patch12:        net-snmp-5.8-add-lustre-fs-support.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  rpm-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
Requires:       logrotate
Requires:       perl-SNMP = %{version}
Requires:       perl-TermReadKey
Requires(post): %fillup_prereq
%{?systemd_requires}
%if 0%{?netsnmp_with_sensors}
BuildRequires:  libsensors4-devel
%endif

%description
Net-SNMP is a suite of applications used to implement SNMP v1, SNMP v2c
and SNMP v3 using both IPv4 and IPv6. The suite includes:

- An extensible agent for responding to SNMP queries including built-in
  support for a wide range of MIB information modules
- Command-line applications to retrieve and manipulate information from
  SNMP-capable devices
- A daemon application for receiving SNMP notifications
- A library for developing new SNMP applications, with C and Perl APIs
- A graphical MIB browser.

This package was originally based on the CMU 2.1.2.1 snmp code. It was
renamed from cmu-snmp to ucd-snmp in 1995 and later renamed from ucd-snmp
to net-snmp in November 2000.

%package     -n %{libname}
Summary:        Shared Libraries from net-snmp
License:        BSD-3-Clause AND MIT
Group:          System/Libraries
Requires:       perl-base = %{perl_version}
Requires:       snmp-mibs = %{version}

%description -n %{libname}
Net-SNMP is a suite of applications used to implement SNMP v1, SNMP v2c
and SNMP v3 using both IPv4 and IPv6. The suite includes:

* An extensible agent for responding to SNMP queries including built-in
  support for a wide range of MIB information modules
* Command-line applications to retrieve and manipulate information from
  SNMP-capable devices
* A daemon application for receiving SNMP notifications
* A library for developing new SNMP applications, with C and Perl APIs
* A graphical MIB browser.

This package holds the shared libraries from the net-snmp package.

%package devel
Summary:        Development files from net-snmp
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
# for mib2c
Requires:       perl
Requires:       perl-SNMP = %{version}
Requires:       rpm-devel
Requires:       tcpd-devel
Requires:       zlib-devel
Requires:       pkgconfig(libssl)
%if 0%{?netsnmp_with_sensors}
Requires:       libsensors4-devel
%endif

%description devel
Net-SNMP is a suite of applications used to implement SNMP v1, SNMP v2c
and SNMP v3 using both IPv4 and IPv6. The suite includes:

* An extensible agent for responding to SNMP queries including built-in
  support for a wide range of MIB information modules
* Command-line applications to retrieve and manipulate information from
  SNMP-capable devices
* A daemon application for receiving SNMP notifications
* A library for developing new SNMP applications, with C and Perl APIs
* A graphical MIB browser.

This package holds the development headers, libraries and API documentation
from the net-snmp package.

%package     -n snmp-mibs
Summary:        MIB files from net-snmp
License:        BSD-3-Clause AND MIT
Group:          Productivity/Networking/Other

%description -n snmp-mibs
Net-SNMP is a suite of applications used to implement SNMP v1, SNMP v2c
and SNMP v3 using both IPv4 and IPv6. The suite includes:

- An extensible agent for responding to SNMP queries including built-in
  support for a wide range of MIB information modules
- Command-line applications to retrieve and manipulate information from
  SNMP-capable devices
- A daemon application for receiving SNMP notifications
- A library for developing new SNMP applications, with C and Perl APIs
- A graphical MIB browser.

This package holds the MIB files from the net-snmp package.

%package     -n perl-SNMP
Summary:        Perl5 SNMP Extension Module
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}
Requires:       perl-base = %{perl_version}

%description -n perl-SNMP
The Perl5 'SNMP' Extension Module v3.1.0 for the UCD SNMPv3 library.

%package -n python2-%{name}
Summary:        The Python 'netsnmp' module for the Net-SNMP
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/Python
Requires:       %{libname} = %{version}
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < %{version}
Provides:       python-%{name} = %{version}

%description -n python2-%{name}
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3,
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%package -n python3-%{name}
Summary:        The Python 3 'netsnmp' module for the Net-SNMP
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/Python
Requires:       %{libname} = %{version}

%description -n python3-%{name}
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3,
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%prep
%setup -q
%autopatch -p1

%build
MIBS="misc/ipfwacc ucd-snmp/diskio etherlike-mib rmon-mib velocity smux \
      ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
      ip-mib/ipDefaultRouterTable ip-mib/ipAddressPrefixTable \
      ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
      tsm-mib tlstm-mib"

%if 0%{?netsnmp_with_sensors}
MIBS="$MIBS ucd-snmp/lmsensorsMib"
%endif

autoreconf -fvi
%configure \
	--with-sys-contact="root@localhost" \
	--with-sys-location="unknown" \
	--with-mib-modules="$MIBS" \
	--with-cflags="%{optflags}" \
        --with-ldflags="-Wl,-z,relro -Wl,-z,now" \
	--with-persistent-directory="%{_localstatedir}/lib/net-snmp" \
	--with-agentx-socket="%{netsnmp_agentx_socket_dir_fhs}/master" \
        --with-temp-file-pattern=%{_localstatedir}/run/net-snmp/snmp-tmp-XXXXXX \
	--with-logfile="%{netsnmp_logfile}" \
	--with-libwrap="%{_prefix}" \
	--with-perl-modules="INSTALLDIRS=vendor" \
	--with-defaults \
	--enable-shared \
	--disable-static \
	--enable-as-needed \
	--without-root-access \
	--enable-local-smux \
	--enable-ipv6 \
	--enable-ucd-snmp-compatibility \
	--with-security-modules=tsm,usm \
	--with-transports=TLSTCP,DTLSUDP \
        --with-systemd

# Parallel build deps not properly stated
make -j1

pushd python
%python_exec setup.py build --basedir="../"
popd

%install
%make_install INSTALL_PREFIX=%{buildroot}
install -Dd %{buildroot}%{_localstatedir}/log %{buildroot}%{_localstatedir}/lib/net-snmp %{buildroot}%{_libexecdir}/net-snmp/agents %{buildroot}%{netsnmp_agentx_socket_dir_fhs}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/snmpd.service
install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/snmptrapd.service
install -D -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/snmp/snmpd.conf
install -m 0644 %{SOURCE3} .
install -m 0644 %{SOURCE4} .
install -D -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/net-snmp
install -m 0744 %{SOURCE6} testing/
ln -sf service %{buildroot}%{_sbindir}/rcsnmpd
ln -sf service %{buildroot}%{_sbindir}/rcsnmptrapd
install -m 0644 /dev/null  %{buildroot}%{netsnmp_logfile}
pushd perl
    %perl_make_install
    %perl_process_packlist
    rm -f %{buildroot}/%{perl_vendorarch}/Bundle/Makefile.subs.pl
popd
pushd python
%python_install
popd
grep -a -v "^#define PACKAGE" %{buildroot}%{_includedir}/net-snmp/net-snmp-config.h > \
    %{buildroot}%{_includedir}/net-snmp/net-snmp-config.h.new
mv  %{buildroot}%{_includedir}/net-snmp/net-snmp-config.h{.new,}
install -D -m 0644 %{SOURCE10} %{buildroot}%{_fillupdir}/sysconfig.snmpd
install -D -m 0644 %{SOURCE11} %{buildroot}%{_fillupdir}/sysconfig.snmptrapd
# tmpfiles
install -m 755 -d %{buildroot}/%{_tmpfilesdir}
install -m 644 %SOURCE20 %{buildroot}/%{_tmpfilesdir}/net-snmp.conf
#
ln -s -f %{netsnmp_agentx_socket_dir_fhs} %{buildroot}%{netsnmp_agentx_socket_dir_rfc}
#
find %{buildroot} -type f -name "*.la" -delete -print

%pre
%service_add_pre snmpd.service snmptrapd.service

%post
%fillup_only snmpd
%fillup_only snmptrapd
%tmpfiles_create %{_tmpfilesdir}/net-snmp.conf
%service_add_post snmpd.service snmptrapd.service

%preun
%service_del_preun snmpd.service snmptrapd.service

%postun
%service_del_postun snmpd.service snmptrapd.service

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING
%doc AGENT.txt EXAMPLE.conf EXAMPLE.conf.def
%doc FAQ NEWS TODO CHANGES
%doc README README.agent-mibs README.agentx README.krb5 README.snmpv3 README.thread
%dir %{_sysconfdir}/snmp
%config(noreplace) %{_sysconfdir}/snmp/snmpd.conf
%{_unitdir}/snmpd.service
%{_unitdir}/snmptrapd.service
%{_tmpfilesdir}/net-snmp.conf
%{_bindir}/encode_keychange
%{_bindir}/fixproc
%{_bindir}/ipf-mod.pl
%{_bindir}/net-snmp-config
%{_bindir}/snmpbulkget
%{_bindir}/snmpbulkwalk
%{_bindir}/snmpcheck
%{_bindir}/snmpconf
%{_bindir}/snmpdelta
%{_bindir}/snmpdf
%{_bindir}/snmpget
%{_bindir}/snmpgetnext
%{_bindir}/snmpinform
%{_bindir}/snmpnetstat
%{_bindir}/snmpset
%{_bindir}/snmpstatus
%{_bindir}/snmptable
%{_bindir}/snmptest
%{_bindir}/snmptls
%{_bindir}/snmptranslate
%{_bindir}/snmptrap
%{_bindir}/snmpusm
%{_bindir}/snmpvacm
%{_bindir}/snmpwalk
%{_bindir}/traptoemail
%{_bindir}/net-snmp-create-v3-user
%{_bindir}/net-snmp-cert
%{_bindir}/agentxtrap
%{_bindir}/snmp-bridge-mib
%{_bindir}/checkbandwidth
%{_bindir}/snmpping
%{_bindir}/snmpps
%{_bindir}/snmptop
%dir %{_libexecdir}/net-snmp
%dir %{_libexecdir}/net-snmp/agents
%{_mandir}/man[158]/*
%{_sbindir}/*
%{_localstatedir}/lib/net-snmp
%dir %ghost %attr(700,root,root) %{netsnmp_agentx_socket_dir_fhs}
%ghost %{netsnmp_logfile}
%config(noreplace) %{_sysconfdir}/logrotate.d/net-snmp
%{_fillupdir}/sysconfig.snmpd
%{_fillupdir}/sysconfig.snmptrapd
%{netsnmp_agentx_socket_dir_rfc}
%{_datadir}/snmp/snmpconf-data/
%{_datadir}/snmp/snmp_perl.pl
%{_datadir}/snmp/snmp_perl_trapd.pl

%files -n snmp-mibs
%dir %{_datadir}/snmp
%{_datadir}/snmp/mibs/

%files -n %{libname}
%license COPYING
%{_libdir}/libsnmp*.so.*
%{_libdir}/libnetsnmp*.so.*

%files devel
%doc ChangeLog PORTING
%{_mandir}/man3/*
%{_includedir}/ucd-snmp
%{_includedir}/net-snmp
%{_libdir}/libsnmp*.so
%{_libdir}/libnetsnmp*.so
%{_bindir}/mib2c
%{_bindir}/mib2c-update
%{_datadir}/snmp/mib2c*

%files -n perl-SNMP
%{perl_vendorarch}/auto/SNMP
%{perl_vendorarch}/auto/NetSNMP
%{perl_vendorarch}/Bundle
%{perl_vendorarch}/SNMP.pm
%{perl_vendorarch}/NetSNMP
%{_bindir}/tkmib

%if %{with python2}
%files -n python2-%{name}
%doc README
%{python2_sitearch}/*
%endif

%files -n python3-%{name}
%doc README
%{python3_sitearch}/*

%changelog
