#
# spec file for package net-snmp
#
# Copyright (c) 2023 SUSE LLC
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
%define libname libsnmp40
%bcond_without python2
Name:           net-snmp
Version:        5.9.3
Release:        0
Summary:        SNMP Daemon
License:        BSD-3-Clause AND MIT
Group:          Productivity/Networking/Other
URL:            https://sourceforge.net/projects/net-snmp
Source:         https://sourceforge.net/projects/net-snmp/files/net-snmp/%{version}/%{name}-%{version}.tar.gz
Source1:        snmpd.conf
Source2:        README.SUSE
Source3:        net-snmp.logrotate
Source4:        test_installed
Source7:        https://sourceforge.net/projects/net-snmp/files/net-snmp/%{version}/%{name}-%{version}.tar.gz.asc
Source8:        http://www.net-snmp.org/net-snmp-admin.asc#/%{name}.keyring
Source10:       snmpd.sysconfig
Source11:       snmptrapd.sysconfig
Source20:       net-snmp-tmpfs.conf
Source98:       net-snmp-rpmlintrc
Source99:       baselibs.conf
Patch1:         net-snmp-5.9.1-socket-path.patch
Patch2:         net-snmp-5.9.1-testing-empty-arptable.patch
Patch3:         net-snmp-5.9.2-pie.patch
Patch4:         net-snmp-5.9.1-net-snmp-config-headercheck.patch
Patch5:         net-snmp-5.9.1-perl-tk-warning.patch
Patch6:         net-snmp-5.9.1-velocity-mib.patch
Patch7:         net-snmp-5.9.1-snmpstatus-suppress-output.patch
Patch8:         net-snmp-5.9.1-fix-Makefile.PL.patch
Patch9:         net-snmp-5.9.1-modern-rpm-api.patch
Patch10:        net-snmp-5.9.1-add-lustre-fs-support.patch
Patch11:        net-snmp-5.9.1-harden_snmpd.service.patch
Patch12:        net-snmp-5.9.1-harden_snmptrapd.service.patch
Patch13:        net-snmp-5.9.1-suse-systemd-service-files.patch
Patch14:        net-snmp-5.9.2-fix-create-v3-user-outfile.patch
Patch15:        net-snmp-5.9.1-subagent-set-response.patch
Patch16:        net-snmp-5.9.3-fixed-python2-bindings.patch
Patch17:        net-snmp-5.9.3-grep.patch
Patch18:        net-snmp-5.9.3-disallow_SET_requests_with_NULL_varbind.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  ncurses-devel
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

%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
# same "defaults" for all distributions, used in files section
%define python_files() -n python3-%{**}
%define python_sitearch %{python3_sitearch}
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
Requires:       snmp-mibs >= %{version}
# Version 5.9.2 was wrongly packaging .so.39 in libsnmp40
Conflicts:      libsnmp40 <= 5.9.2

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

%if 0%{?python_subpackage_only}
%package -n python-%{name}
Summary:        The Python 3 'netsnmp' module for the Net-SNMP
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/Python
Requires:       %{libname} = %{version}

%description -n python-%{name}
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3,
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%else

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
%endif

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
	--with-cflags="%{optflags} -fcommon" \
	--with-ldflags="-Wl,-z,relro -Wl,-z,now" \
	--with-persistent-directory="%{_localstatedir}/lib/net-snmp" \
	--with-agentx-socket="%{netsnmp_agentx_socket_dir_fhs}/master" \
	--with-temp-file-pattern=%{_localstatedir}/run/net-snmp/snmp-tmp-XXXXXX \
	--with-logfile="%{netsnmp_logfile}" \
	--with-libwrap="%{_prefix}" \
	--with-perl-modules="INSTALLDIRS=vendor" \
	--with-defaults \
	--with-pic \
	--sysconfdir=%{_sysconfdir} \
	--enable-shared \
	--disable-static \
	--enable-as-needed \
	--without-root-access \
	--enable-local-smux \
	--enable-ipv6 \
	--enable-ucd-snmp-compatibility \
	--enable-mfd-rewrites \
	--with-security-modules=tsm,usm \
	--with-transports=TLSTCP,DTLSUDP \
	--with-systemd \
	--with-openssl \
	--enable-blumenthal-aes \
	--disable-des \
	--disable-md5

# Parallel build deps not properly stated
%make_build -j1

pushd python
%python_exec setup.py build --basedir="../"
popd

%install
%make_install INSTALL_PREFIX=%{buildroot}
install -Dd %{buildroot}%{_localstatedir}/log %{buildroot}%{_localstatedir}/lib/net-snmp %{buildroot}%{_libexecdir}/net-snmp/agents %{buildroot}%{netsnmp_agentx_socket_dir_fhs}
install -D -m 0644 dist/snmpd.service %{buildroot}%{_unitdir}/snmpd.service
install -D -m 0644 dist/snmptrapd.service %{buildroot}%{_unitdir}/snmptrapd.service
install -D -m 0600 %{SOURCE1} %{buildroot}%{_sysconfdir}/snmp/snmpd.conf
install -m 0644 %{SOURCE2} .
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -D -m 0644 %{SOURCE3} %{buildroot}%{_distconfdir}/logrotate.d/net-snmp
%else
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/net-snmp
%endif
install -m 0744 %{SOURCE4} testing/
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
install -m 644 %{SOURCE20} %{buildroot}/%{_tmpfilesdir}/net-snmp.conf
#
ln -s -f %{netsnmp_agentx_socket_dir_fhs} %{buildroot}%{netsnmp_agentx_socket_dir_rfc}
#
find %{buildroot} -type f -name "*.la" -delete -print

%pre
%service_add_pre snmpd.service snmptrapd.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/net-snmp ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/net-snmp ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%fillup_only -n snmpd
%fillup_only -n snmptrapd
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
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/net-snmp
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/net-snmp
%endif
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
%{_libdir}/pkgconfig/netsnmp-agent.pc
%{_libdir}/pkgconfig/netsnmp.pc
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

%if %{with python2} && ! 0%{?python_subpackage_only}
%files -n python2-%{name}
%doc README
%{python2_sitearch}/*
%endif

%files %{python_files %{name}}
%doc README
%{python_sitearch}/*

%changelog
