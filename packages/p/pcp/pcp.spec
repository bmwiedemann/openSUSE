#
# spec file for package pcp
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} > 1140 || 0%{?fedora_version} > 14
%global has_systemd 1
%else
%global has_systemd 0
%endif

%if 0%{?suse_version}
%global pcp_gr			System/Monitoring
%global lib_pkg			libpcp3
%global lib_pkg_conflict	pcp-libs
%global lib_gr			System/Libraries
%global lib_devel_pkg		libpcp-devel
%global lib_devel_pkg_conflict	pcp-libs-devel
%global lib_devel_gr		Development/Libraries/Other
%global license_apache2         Apache-2.0
%global license_cc_by           CC-BY-SA-3.0
%global license_gplv2		GPL-2.0
%global license_gplv2plus	GPL-2.0+
%global license_lgplv2		LGPL-2.0
%global license_lgplv2plus	LGPL-2.0+
%global license_lgplv21plus	LGPL-2.1+
%global license_mit	        MIT
%global _libexecdir             %{_libdir}
%else
%global pcp_gr			Applications/System
%global lib_pkg			pcp-libs
%global lib_pkg_conflict	libpcp3
%global lib_gr			System Environment/Libraries
%global lib_devel_pkg		pcp-libs-devel
%global lib_devel_pkg_conflict	libpcp-devel
%global lib_devel_gr		Development/Libraries
%global license_apache2         ASL2.0
%global license_cc_by           CC-BY
%global license_gplv2		GPLv2
%global license_gplv2plus	GPLv2+
%global license_lgplv2		LGPLv2
%global license_lgplv2plus	LGPLv2+
%global license_lgplv21plus	LGPLv2.1+
%global license_mit	        MIT
%endif

%global libpcp_pmda_sover 3
%global libpcp_gui_sover 2
%global libpcp_mmv_sover 1
%global libpcp_trace_sover 2
%global libpcp_import_sover 1
%global libpcp_web_sover 1

Summary:        System-level performance monitoring and performance management
License:        %{license_gplv2plus} AND %{license_lgplv2plus} AND %{license_cc_by}
Group:          %{pcp_gr}
Name:           pcp
Version:        4.3.4
Release:        0
%global buildversion 1

Url:            https://pcp.io
Source0:        pcp-%{version}.tar.bz2
%if 0%{?suse_version}
Source2:        pcp-rpmlintrc
%endif

# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch1:         0001-Install-libraries-without-exec-permission.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch2:         0002-Remove-CPAN-rpaths.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch3:         0003-Remove-runlevel-4-from-init-scripts.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch5:         0005-SUSE-fy-pmsnap-control-path.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch6:         0006-pmsnap-control-var-www-srv-www.patch 

%if 0%{?fedora} || 0%{?rhel}
%global disable_selinux 0
%else
%global disable_selinux 1
%endif

%global disable_snmp 0

# No libpfm devel packages for s390, armv7hl nor for some rhels, disable
%ifarch s390 s390x armv7hl
%global disable_perfevent 1
%else
%if 0%{?fedora} >= 20 || 0%{?rhel} > 6 || 0%{?suse_version}
%global disable_perfevent 0
%else
%global disable_perfevent 1
%endif
%endif

%global disable_sheet2pcp 1
%global disable_microhttpd 0
%global disable_cairo 0

%global disable_python2 0
# No python3 development environment before el8
%if 0%{?rhel} == 0 || 0%{?rhel} > 7
%global disable_python3 0
# Do we wish to mandate python3 use in pcp?  (f22+ and el8+)
%else
%global disable_python3 1
%endif

# some Python3 deps missing for SLE <= 12SP2
%if 0%{?sle_version} && 0%{?sle_version} <= 120200
%global disable_python3 1
%endif

# drop python2 packages on Tumbleweed and SLE15
%if 0%{?fedora} >= 26 || 0%{?rhel} > 7 || 0%{?suse_version} >= 1500
%global _with_python2 --with-python=no
%global disable_python2 1
%global __python2 python2
%else
%global __python2 python
%endif

# support for pmdajson
%if 0%{?rhel} == 0 || 0%{?rhel} > 6
%if !%{disable_python2} || !%{disable_python3}
%global disable_json 0
%else
%global disable_json 1
%endif
%else
%global disable_json 1
%endif

# support for pmdanutcracker (perl deps missing on rhel)
%if 0%{?rhel} == 0
%global disable_nutcracker 0
%else
%global disable_nutcracker 1
%endif

# support for pmdarpm
%if 0%{?rhel} == 0 || 0%{?rhel} > 5
%global disable_rpm 0
%else
%global disable_rpm 1
%endif

# Qt development and runtime environment missing components before el6
%if 0%{?rhel} == 0 || 0%{?rhel} > 5
%global disable_qt 0
# We need qt5 for fedora and openSUSE / SLE factory
%if 0%{?fedora} != 0 || 0%{?suse_version} > 1320
%global default_qt 5
%endif
%else
%global disable_qt 1
%endif

# systemd services and pmdasystemd
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7 || 0%{?suse_version}
%global disable_systemd 0
%else
%global disable_systemd 1
%endif

# systemtap static probing, missing before el6 and on some architectures
%if 0%{?rhel} == 0 || 0%{?rhel} > 5
%global disable_sdt 0
%else
%ifnarch ppc ppc64
%global disable_sdt 0
%else
%global disable_sdt 1
%endif
%endif

%if 0%{?suse_version} && !%{disable_python3}
# SUSE doesn't currently ship the libvirt-python3 dependency
%global disable_libvirt 1
%else
%global disable_libvirt 0
%endif

%if 0%{?suse_version}
# SUSE doesn't currently ship the python psycopg2 dependency
%global disable_postgresql 1
%else
%global disable_postgresql 0
%endif

# rpm producing "noarch" packages
%if 0%{?rhel} == 0 || 0%{?rhel} > 5 || 0%{?suse_version} >= 1315
%global disable_noarch 0
%else
%global disable_noarch 1
%endif

%if 0%{?fedora} >= 24
%global disable_xlsx 0
%else
%global disable_xlsx 1
%endif

# python3-rtslib-fb not yet available on SUSE, see boo#1045332
%if 0%{?suse_version} && !%{disable_python3}
%global disable_lio 1
%else
%global disable_lio 0
%endif

# KVM PMDA moved into pcp (no longer using Perl, default on)
Obsoletes:      pcp-pmda-kvm < %{version}
Provides:       pcp-pmda-kvm

%if 0%{?suse_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%else
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
BuildRequires:  autoconf
BuildRequires:  avahi-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  mozilla-nss-devel
%else	# suse_version
BuildRequires:  nss-devel
%endif	# suse_version
BuildRequires:  perl
BuildRequires:  procps
BuildRequires:  rpm-devel
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
%if !%{disable_python3}
BuildRequires:  python3-devel
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
%if !%{disable_perfevent}
BuildRequires:  libpfm-devel >= 4.4
%endif
%if !%{disable_microhttpd}
BuildRequires:  libmicrohttpd-devel
%endif
%if !%{disable_cairo}
BuildRequires:  cairo-devel
%endif
%if !%{disable_sdt}
BuildRequires:  systemtap-sdt-devel
%endif
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  perl-ExtUtils-MakeMaker
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%else
BuildRequires:  initscripts
%endif
BuildRequires:  man
%if !%{disable_systemd}
BuildRequires:  systemd-devel
%{?systemd_requires}
%endif
%if !%{disable_qt}
BuildRequires:  desktop-file-utils
%if 0%{?default_qt} != 5
%if 0%{?suse_version}
BuildRequires:  libqt4-devel >= 4.4
%else	# suse_version
BuildRequires:  qt4-devel >= 4.4
%endif	# suse_version
%else	# default_qt
%if 0%{?suse_version}
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtsvg-devel
%else	# suse_version
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
%endif	# suse_version
%endif	# default_qt
%endif	# !disable_qt
%if !%{disable_selinux}
Requires:       pcp-selinux = %{version}-%{release}
%endif

# for set_permissions
%if 0%{?suse_version} >= 1131
PreReq:         permissions
%endif
Requires:       bash
%if %{disable_systemd}
Requires:       cron
%endif
Requires:       fileutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       perl
Requires:       sed
Requires:       which
%if 0%{?suse_version}
Requires:       cpp
Requires:       cyrus-sasl
Requires:       sysconfig
%if !%{disable_python2}
# pmatop needs curses.py
Requires:       %{__python2}-curses
%endif
%else
Requires:       initscripts
%endif

Requires:       %{lib_pkg} = %{version}-%{release}
Obsoletes:      pcp-pmda-nvidia < %{version}

%global tapsetdir      %{_datadir}/systemtap/tapset

%global _confdir  %{_sysconfdir}/pcp
%global _logsdir  %{_localstatedir}/log/pcp
%global _pmnsdir  %{_localstatedir}/lib/pcp/pmns
%global _tempsdir %{_localstatedir}/lib/pcp/tmp
%global _pmdasdir %{_localstatedir}/lib/pcp/pmdas
%global _testsdir %{_localstatedir}/lib/pcp/testsuite
%global _selinuxdir %{_localstatedir}/lib/pcp/selinux
%global _logconfdir %{_localstatedir}/lib/pcp/config/pmlogconf
%if 0%{?suse_version}
%global _pixmapdir %{_datadir}/pixmaps
%global _booksdir %{_docdir}/pcp-doc
%else
%global _pixmapdir %{_datadir}/pcp-gui/pixmaps
%global _booksdir %{_datadir}/doc/pcp-doc
%endif

%if 0%{?fedora} >= 20 || 0%{?rhel} >= 8 || 0%{?suse_version}
# FIXME: PCP defaults to using %{_datadir}/doc/pcp-doc
%global _with_doc --with-docdir=%{_docdir}/%{name}
%endif
%if !%{disable_systemd}
%global _initddir %{_datadir}/pcp/lib
%else
%if 0%{?suse_version}
%global _initddir %{_sysconfdir}/init.d
%else
%global _initddir %{_sysconfdir}/rc.d/init.d
%endif
%global _with_initd --with-rcdir=%{_initddir}
%endif

# we never want Infiniband on s390 platforms
%ifarch s390 s390x
%global disable_infiniband 1
%else

# we never want Infiniband on RHEL5 or earlier
%if 0%{?rhel} != 0 && 0%{?rhel} < 6
%global disable_infiniband 1
%else
%global disable_infiniband 0
%endif

%endif

%if %{disable_infiniband}
%global _with_ib --with-infiniband=no
%endif

%if !%{disable_perfevent}
%global _with_perfevent --with-perfevent=yes
%endif

%if %{disable_json}
%global _with_json --with-pmdajson=no
%else
%global _with_json --with-pmdajson=yes
%endif

%if %{disable_nutcracker}
%global _with_nutcracker --with-pmdanutcracker=no
%else
%global _with_nutcracker --with-pmdanutcracker=yes
%endif

%if %{disable_snmp}
%global _with_snmp --with-pmdasnmp=no
%else
%global _with_snmp --with-pmdasnmp=yes
%endif

%description
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management. 

The PCP open source release provides a unifying abstraction for all of
the interesting performance data in a system, and allows client
applications to easily retrieve and process any subset of that data.

#
# pcp-conf
#
%package conf
Summary:        Performance Co-Pilot run-time configuration
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io
# http://fedoraproject.org/wiki/Packaging:Conflicts "Splitting Packages"
Conflicts:      pcp-libs < 3.9

%description conf
Performance Co-Pilot (PCP) run-time configuration

#
# pcp-libs
#

%package -n %{lib_pkg}
Summary:        Performance Co-Pilot run-time libraries
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io
Conflicts:      %{lib_pkg_conflict}
Requires:       pcp-conf >= %{version}-%{release}

%description -n %{lib_pkg}
Performance Co-Pilot (PCP) run-time libraries

%if 0%{?suse_version}
%package -n libpcp_gui%{libpcp_gui_sover}
Summary:        Performance Co-Pilot run-time GUI library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io

%description -n libpcp_gui%{libpcp_gui_sover}
Performance Co-Pilot (PCP) run-time graphical user interface library

%package -n libpcp_mmv%{libpcp_mmv_sover}
Summary:        Performance Co-Pilot run-time MMV library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io

%description -n libpcp_mmv%{libpcp_mmv_sover}
Performance Co-Pilot (PCP) run-time Memory Mapped Values library

%package -n libpcp_trace%{libpcp_trace_sover}
Summary:        Performance Co-Pilot run-time tracing library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io

%description -n libpcp_trace%{libpcp_trace_sover}
Performance Co-Pilot (PCP) run-time tracing library

%package -n libpcp_import%{libpcp_import_sover}
Summary:        Performance Co-Pilot run-time import library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io

%description -n libpcp_import%{libpcp_import_sover}
Performance Co-Pilot (PCP) run-time import library

%package -n libpcp_web%{libpcp_web_sover}
Summary:        Performance Co-Pilot run-time web library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
Url:            https://pcp.io

%description -n libpcp_web%{libpcp_web_sover}
Performance Co-Pilot (PCP) run-time web library
%endif

#
# pcp-libs-devel
# SLE uses the legacy libpcp-devel package name.
#
%package -n %{lib_devel_pkg}
Summary:        Performance Co-Pilot (PCP) development headers
License:        %{license_gplv2plus} AND %{license_lgplv21plus}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
Requires:       %{lib_pkg} = %{version}-%{release}
Conflicts:      %{lib_devel_pkg_conflict}
%if (0%{?suse_version} > 0)
Provides:       pcp-devel = %{version}
Obsoletes:      pcp-devel < %{version}
%endif

%description -n %{lib_devel_pkg}
Performance Co-Pilot (PCP) headers for development.

#
# pcp-devel
#
%package devel
Summary:        Performance Co-Pilot (PCP) development tools and documentation
License:        %{license_gplv2plus} AND %{license_lgplv21plus}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_devel_pkg} = %{version}-%{release}
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       pcp = %{version}-%{release}
%endif

%description devel
Performance Co-Pilot (PCP) documentation and tools for development.

#
# pcp-testsuite
#
%package testsuite
Summary:        Performance Co-Pilot (PCP) test suite
License:        %{license_gplv2plus} AND %{license_mit}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_devel_pkg} = %{version}-%{release}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}
Requires:       pcp-devel = %{version}-%{release}
Obsoletes:      pcp-gui-testsuite

%description testsuite
Quality assurance test suite for Performance Co-Pilot (PCP).

#
# pcp-manager
#
%package manager
Summary:        Performance Co-Pilot (PCP) manager daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}

%description manager
An optional daemon (pmmgr) that manages a collection of pmlogger and
pmie daemons, for a set of discovered local and remote hosts running
the performance metrics collection daemon (pmcd).  It ensures these
daemons are running when appropriate, and manages their log rotation
needs.  It is an alternative to the cron-based pmlogger/pmie service
scripts.

%if !%{disable_microhttpd}
#
# pcp-webapi
#
%package webapi
Summary:        Performance Co-Pilot (PCP) web API service
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}

%description webapi
Provides a daemon (pmwebd) that binds a large subset of the Performance
Co-Pilot (PCP) client API (PMAPI) to RESTful web applications using the
HTTP (PMWEBAPI) protocol.
%endif

#
# perl-PCP-PMDA. This is the PCP agent perl binding.
#
%package -n perl-PCP-PMDA
Summary:        Performance Co-Pilot (PCP) Perl bindings and documentation
License:        %{license_gplv2plus}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
%if 0%{?suse_version}
%perl_requires
%endif
Requires:       %{lib_pkg} = %{version}-%{release}

%description -n perl-PCP-PMDA
The PCP::PMDA Perl module contains the language bindings for
building Performance Metric Domain Agents (PMDAs) using Perl.
Each PMDA exports performance data for one specific domain, for
example the operating system kernel, Cisco routers, a database,
an application, etc.

#
# perl-PCP-MMV
#
%package -n perl-PCP-MMV
Summary:        Performance Co-Pilot (PCP) Perl bindings for PCP Memory Mapped Values
License:        %{license_gplv2plus}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
%if 0%{?suse_version}
%perl_requires
%endif
Requires:       %{lib_pkg} = %{version}-%{release}

%description -n perl-PCP-MMV
The PCP::MMV module contains the Perl language bindings for
building scripts instrumented with the Performance Co-Pilot
(PCP) Memory Mapped Value (MMV) mechanism.
This mechanism allows arbitrary values to be exported from an
instrumented script into the PCP infrastructure for monitoring
and analysis with pmchart, pmie, pmlogger and other PCP tools.

#
# perl-PCP-LogImport
#
%package -n perl-PCP-LogImport
Summary:        Performance Co-Pilot Perl bindings for importing external archive data
License:        %{license_gplv2plus}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
%if 0%{?suse_version}
%perl_requires
%endif
Requires:       %{lib_pkg} = %{version}-%{release}

%description -n perl-PCP-LogImport
The PCP::LogImport module contains the Perl language bindings for
importing data in various 3rd party formats into PCP archives so
they can be replayed with standard PCP monitoring tools.

 #
# perl-PCP-LogSummary
#
%package -n perl-PCP-LogSummary
Summary:        Performance Co-Pilot Perl bindings for processing pmlogsummary output
License:        %{license_gplv2plus}
Group:          %{lib_devel_gr}
Url:            https://pcp.io
%if 0%{?suse_version}
%perl_requires
%endif
Requires:       %{lib_pkg} = %{version}-%{release}

%description -n perl-PCP-LogSummary
The PCP::LogSummary module provides a Perl module for using the
statistical summary data produced by the Performance Co-Pilot
pmlogsummary utility.  This utility produces various averages,
minima, maxima, and other calculations based on the performance
data stored in a PCP archive.  The Perl interface is ideal for
exporting this data into third-party tools (e.g. spreadsheets).

#
# pcp-import-sar2pcp
#
%package import-sar2pcp
Summary:        Performance Co-Pilot archive tools for importing sar data
License:        %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       perl-PCP-LogImport = %{version}-%{release}
Requires:       sysstat

%description import-sar2pcp
Performance Co-Pilot (PCP) front-end tools for importing sar data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# pcp-import-iostat2pcp
#
%package import-iostat2pcp
Summary:        Performance Co-Pilot archive tools for importing iostat data
License:        %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       perl-PCP-LogImport = %{version}-%{release}
Requires:       sysstat

%description import-iostat2pcp
Performance Co-Pilot (PCP) front-end tools for importing iostat data
into standard PCP archive logs for replay with any PCP monitoring tool.

%if !%{disable_sheet2pcp}
#
# pcp-import-sheet2pcp
#
%package import-sheet2pcp
Summary:        Performance Co-Pilot archive tools for importing spreadsheet data
License:        %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       perl-PCP-LogImport = %{version}-%{release}
Requires:       sysstat

%description import-sheet2pcp
Performance Co-Pilot (PCP) front-end tools for importing spreadsheet data
into standard PCP archive logs for replay with any PCP monitoring tool.

%endif

#
# pcp-import-mrtg2pcp
#
%package import-mrtg2pcp
Summary:        Performance Co-Pilot archive tools for importing MTRG data
License:        %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       perl-PCP-LogImport = %{version}-%{release}

%description import-mrtg2pcp
Performance Co-Pilot (PCP) front-end tools for importing MTRG data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# pcp-import-ganglia2pcp
#
%package import-ganglia2pcp
Summary:        Performance Co-Pilot archive tools for importing ganglia data
License:        %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       perl-PCP-LogImport = %{version}-%{release}

%description import-ganglia2pcp
Performance Co-Pilot (PCP) front-end tools for importing ganglia data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# pcp-import-collectl2pcp
#
%package import-collectl2pcp
Summary:        Performance Co-Pilot archive tools for importing collectl data
License:        %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description import-collectl2pcp
Performance Co-Pilot (PCP) front-end tools for importing collectl data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# pcp-export-zabbix-agent
#
%package export-zabbix-agent
Summary:        Module for exporting from PCP into a Zabbix agent daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} >= %{version}-%{release}
%endif

%description export-zabbix-agent
Performance Co-Pilot (PCP) module for exporting metrics from PCP to
Zabbix via the Zabbix agent - see zbxpcp(3) for further details.

%if !%{disable_python2} || !%{disable_python3}
#
# pcp-export-pcp2elasticsearch
#
%package export-pcp2elasticsearch
Summary:        Performance Co-Pilot tools for exporting PCP metrics to ElasticSearch
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       %{lib_pkg} >= %{version}-%{release}
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
Requires:       python3-requests
BuildRequires:  python3-requests
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
Requires:       %{__python2}-requests
BuildRequires:  %{__python2}-requests
%endif

%description export-pcp2elasticsearch
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to Elasticsearch - a distributed, RESTful search and analytics engine.
See https://www.elastic.co/community for further details.

#
# pcp-export-pcp2graphite
#
%package export-pcp2graphite
Summary:        Performance Co-Pilot tools for exporting PCP metrics to Graphite
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
%endif

%description export-pcp2graphite
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to graphite (http://graphite.readthedocs.org).

# pcp-export-pcp2influxdb
#
%package export-pcp2influxdb
Summary:        Performance Co-Pilot tools for exporting PCP metrics to InfluxDB
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} >= %{version}-%{release}
%endif
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
Requires:       python3-requests
BuildRequires:  python3-requests
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
Requires:       %{__python2}-requests
BuildRequires:  %{__python2}-requests
%endif

%description export-pcp2influxdb
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to InfluxDB (https://influxdata.com/time-series-platform/influxdb).

#
# pcp-export-pcp2json
#
%package export-pcp2json
Url:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics in JSON format
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
%endif

%description export-pcp2json
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in JSON format.

#
# pcp-export-pcp2spark
#
%package export-pcp2spark
Url:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics to Apache Spark
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
%endif

%description export-pcp2spark
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in JSON format to Apache Spark. See https://spark.apache.org/ for
further details on Apache Spark.

#
# pcp-export-pcp2xlsx
#
%if !%{disable_xlsx}
%package export-pcp2xlsx
Url:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics to Excel
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
%if !%{disable_python3}
Requires:       python3-openpyxl
Requires:       python3-pcp = %{version}-%{release}
BuildRequires:  python3-openpyxl
%else
Requires:       %{__python2}-openpyxl
Requires:       %{__python2}-pcp = %{version}-%{release}
BuildRequires:  %{__python2}-openpyxl
%endif

%description export-pcp2xlsx
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in Excel spreadsheet format.
%endif
#
# pcp-export-pcp2xml
#
%package export-pcp2xml
Url:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics in XML format
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
%endif

%description export-pcp2xml
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in XML format.

#
# pcp-export-pcp2zabbix
#
%package export-pcp2zabbix
Summary:        Performance Co-Pilot tools for exporting PCP metrics to Zabbix
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
%else
Requires:       %{__python2}-pcp = %{version}-%{release}
%endif

%description export-pcp2zabbix
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to the Zabbix (https://www.zabbix.org/) monitoring software.
%endif

%if !%{disable_perfevent}
#
# pcp-pmda-perfevent
#
%package pmda-perfevent
Summary:        Performance Co-Pilot (PCP) metrics for hardware counters
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       libpfm >= 4.4
%endif
BuildRequires:  libpfm-devel >= 4.4
Obsoletes:      pcp-pmda-papi
Obsoletes:      pcp-pmda-papi-debuginfo

%description pmda-perfevent
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting hardware counters statistics through libpfm.
%endif

%if !%{disable_infiniband}
#
# pcp-pmda-infiniband
#
%package pmda-infiniband
Summary:        Performance Co-Pilot (PCP) metrics for Infiniband HCAs and switches
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       libibmad >= 1.3.7
Requires:       libibumad >= 1.3.7
%endif
BuildRequires:  libibmad-devel >= 1.3.7
BuildRequires:  libibumad-devel >= 1.3.7

%description pmda-infiniband
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting Infiniband statistics.  By default, it monitors the local HCAs
but can also be configured to monitor remote GUIDs such as IB switches.
%endif

#
# pcp-pmda-activemq
#
%package pmda-activemq
Summary:        Performance Co-Pilot (PCP) metrics for ActiveMQ
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(LWP::UserAgent)

%description pmda-activemq
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the ActiveMQ message broker.
#end pcp-pmda-activemq

#
# pcp-pmda-bind2
#
%package pmda-bind2
Summary:        Performance Co-Pilot (PCP) metrics for BIND servers
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(File::Slurp)
Requires:       perl(LWP::UserAgent)
Requires:       perl(XML::LibXML)

%description pmda-bind2
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from BIND (Berkeley Internet Name Domain).
#end pcp-pmda-bind2

#
# pcp-pmda-redis
#
%package pmda-redis
Summary:        Performance Co-Pilot (PCP) metrics for Redis
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-redis
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from Redis servers (redis.io).
#end pcp-pmda-redis

%if !%{disable_nutcracker}
#
# pcp-pmda-nutcracker
#
%package pmda-nutcracker
Summary:        Performance Co-Pilot (PCP) metrics for NutCracker (TwemCache)
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(JSON)
Requires:       perl(YAML::XS::LibYAML)

%description pmda-nutcracker
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from NutCracker (TwemCache).
#end pcp-pmda-nutcracker
%endif

#
# pcp-pmda-bonding
#
%package pmda-bonding
Summary:        Performance Co-Pilot (PCP) metrics for Bonded network interfaces
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-bonding
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about bonded network interfaces.
#end pcp-pmda-bonding

#
# pcp-pmda-dbping
#
%package pmda-dbping
Summary:        Performance Co-Pilot (PCP) metrics for Database responsiveness
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-dbping
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Database response times and Availablility.
#end pcp-pmda-dbping

#
# pcp-pmda-ds389
#
%package pmda-ds389
Summary:        Performance Co-Pilot (PCP) metrics for 389 Directory Servers
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if 0%{?suse_version}
Requires:       perl-ldap
%else
Requires:       perl-LDAP
%endif
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-ds389
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about a 389 Directory Server.
#end pcp-pmda-ds389

#
# pcp-pmda-ds389log
#
%package pmda-ds389log
Summary:        Performance Co-Pilot (PCP) metrics for 389 Directory Server Loggers
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-Date-Manip
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-ds389log
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from a 389 Directory Server log.
#end pcp-pmda-ds389log

#
# pcp-pmda-gpfs
#
%package pmda-gpfs
Summary:        Performance Co-Pilot (PCP) metrics for GPFS Filesystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-gpfs
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the GPFS filesystem.
#end pcp-pmda-gpfs

#
# pcp-pmda-gpsd
#
%package pmda-gpsd
Summary:        Performance Co-Pilot (PCP) metrics for a GPS Daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-gpsd
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about a GPS Daemon.
#end pcp-pmda-gpsd

#
# pcp-pmda-docker
#
%package pmda-docker
Summary:        Performance Co-Pilot (PCP) metrics from the Docker daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io

%description pmda-docker
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics using the Docker daemon REST API.
#end pcp-pmda-docker

#
# pcp-pmda-lustre
#
%package pmda-lustre
Summary:        Performance Co-Pilot (PCP) metrics for the Lustre Filesytem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-lustre
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Lustre Filesystem.
#end pcp-pmda-lustre
   
#
# pcp-pmda-lustrecomm
#
%package pmda-lustrecomm
Summary:        Performance Co-Pilot (PCP) metrics for the Lustre Filesytem Comms
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}
Supplements:    pcp

%description pmda-lustrecomm
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Lustre Filesystem Comms.
#end pcp-pmda-lustrecomm

#
# pcp-pmda-memcache
#
%package pmda-memcache
Summary:        Performance Co-Pilot (PCP) metrics for Memcached
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-memcache
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Memcached.
#end pcp-pmda-memcache

#
# pcp-pmda-mysql
#
%package pmda-mysql
Summary:        Performance Co-Pilot (PCP) metrics for MySQL
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(DBD::mysql)
Requires:       perl(DBI)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
Supplements:    pcp

%description pmda-mysql
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the MySQL database.
#end pcp-pmda-mysql

#
# pcp-pmda-named
#
%package pmda-named
Summary:        Performance Co-Pilot (PCP) metrics for Named
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-named
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Named nameserver.
#end pcp-pmda-named

# pcp-pmda-netfilter
#
%package pmda-netfilter
Summary:        Performance Co-Pilot (PCP) metrics for Netfilter framework
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-netfilter
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Netfilter packet filtering framework.
#end pcp-pmda-netfilter

#
# pcp-pmda-news
#
%package pmda-news
Summary:        Performance Co-Pilot (PCP) metrics for Usenet News
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-news
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Usenet News.
#end pcp-pmda-news

#
# pcp-pmda-nginx
#
%package pmda-nginx
Summary:        Performance Co-Pilot (PCP) metrics for the Nginx Webserver
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(LWP::UserAgent)
BuildRequires:  perl(LWP::UserAgent)

%description pmda-nginx
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Nginx Webserver.
#end pcp-pmda-nginx

#
# pcp-pmda-oracle
#
%package pmda-oracle
Summary:        Performance Co-Pilot (PCP) metrics for the Oracle database
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(DBI)
BuildRequires:  perl(DBI)

%description pmda-oracle
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Oracle database.
#end pcp-pmda-oracle

#
# pcp-pmda-pdns
#
%package pmda-pdns
Summary:        Performance Co-Pilot (PCP) metrics for PowerDNS
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-pdns
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the PowerDNS.
#end pcp-pmda-pdns

#
# pcp-pmda-postfix
#
%package pmda-postfix
Summary:        Performance Co-Pilot (PCP) metrics for the Postfix (MTA)
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
%if 0%{?fedora} > 16 || 0%{?rhel} > 5
Requires:       postfix-perl-scripts
BuildRequires:  postfix-perl-scripts
%endif
%if 0%{?rhel} <= 5
Requires:       postfix
BuildRequires:  postfix
%endif
%if "%{_vendor}" == "suse"
Requires:       postfix-doc
BuildRequires:  postfix-doc
%endif
Supplements:    pcp

%description pmda-postfix
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Postfix (MTA).
#end pcp-pmda-postfix

#
# pcp-pmda-rsyslog
#
%package pmda-rsyslog
Summary:        Performance Co-Pilot (PCP) metrics for Rsyslog
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-rsyslog
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Rsyslog.
#end pcp-pmda-rsyslog

#
# pcp-pmda-samba
#
%package pmda-samba
Summary:        Performance Co-Pilot (PCP) metrics for Samba
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-samba
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Samba.
#end pcp-pmda-samba

#
# pcp-pmda-slurm
#
%package pmda-slurm
Summary:        Performance Co-Pilot (PCP) metrics for NFS Clients
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-slurm
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from the SLURM Workload Manager.
#end pcp-pmda-slurm

%if !%{disable_snmp}
#
# pcp-pmda-snmp
#
%package pmda-snmp
Summary:        Performance Co-Pilot (PCP) metrics for Simple Network Management Protocol
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
# There are no perl-Net-SNMP packages in rhel, disable unless non-rhel or epel5
%if 0%{?rhel} == 0 || 0%{?rhel} < 6
Requires:       perl(Net::SNMP)
%endif
Supplements:    pcp

%description pmda-snmp
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about SNMP.
#end pcp-pmda-snmp
%endif

#
# pcp-pmda-vmware
#
%package pmda-vmware
Summary:        Performance Co-Pilot (PCP) metrics for VMware
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-vmware
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics for VMware.
#end pcp-pmda-vmware

#
# pcp-pmda-zimbra
#
%package pmda-zimbra
Summary:        Performance Co-Pilot (PCP) metrics for Zimbra
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-zimbra
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Zimbra.
#end pcp-pmda-zimbra

#
# pcp-pmda-dm
#
%package pmda-dm
Summary:        Performance Co-Pilot (PCP) metrics for the Device Mapper Cache and Thin Client
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-dm
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Device Mapper Cache and Thin Client.
# end pcp-pmda-dm
   

%if !%{disable_python2} || !%{disable_python3}
#
# pcp-pmda-gluster
#
%package pmda-gluster
Summary:        Performance Co-Pilot (PCP) metrics for the Gluster filesystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-gluster
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the gluster filesystem.
# end pcp-pmda-gluster

#
# pcp-pmda-nfsclient
#
%package pmda-nfsclient
Summary:        Performance Co-Pilot (PCP) metrics for NFS Clients
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-nfsclient
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics for NFS Clients.
#end pcp-pmda-nfsclient

%if !%{disable_postgresql}
#
# pcp-pmda-postgresql
#
%package pmda-postgresql
Summary:        Performance Co-Pilot (PCP) metrics for PostgreSQL
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
Requires:       python3-psycopg2
BuildRequires:  python3-psycopg2
%else
Requires:       %{__python2}-pcp
Requires:       %{__python2}-psycopg2
BuildRequires:  %{__python2}-psycopg2
%endif
%description pmda-postgresql
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the PostgreSQL database.
#end pcp-pmda-postgresql
%endif

#
# pcp-pmda-zswap
#
%package pmda-zswap
Summary:        Performance Co-Pilot (PCP) metrics for compressed swap
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-zswap
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about compressed swap.
# end pcp-pmda-zswap

#
# pcp-pmda-unbound
#
%package pmda-unbound
Summary:        Performance Co-Pilot (PCP) metrics for the Unbound DNS Resolver
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-unbound
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Unbound DNS Resolver.
# end pcp-pmda-unbound

#
# pcp-pmda-mic
#
%package pmda-mic
Summary:        Performance Co-Pilot (PCP) metrics for Intel MIC cards
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-mic
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Intel MIC cards.
# end pcp-pmda-mic

#
# pcp-pmda-haproxy
#
%package pmda-haproxy
Summary:        Performance Co-Pilot (PCP) metrics for HAProxy
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-haproxy
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
extracting performance metrics from HAProxy over the HAProxy stats socket.
# end pcp-pmda-haproxy

%if !%{disable_libvirt}
#
# pcp-pmda-libvirt
#
%package pmda-libvirt
Summary:        Performance Co-Pilot (PCP) metrics for virtual machines
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       libvirt-python3
Requires:       python3-lxml
Requires:       python3-pcp
BuildRequires:  libvirt-python3
%else
Requires:       %{__python2}-lxml
Requires:       %{__python2}-pcp
Requires:       libvirt-python
%if 0%{?rhel} == 0 || 0%{?rhel} > 5
BuildRequires:  libvirt-python
%endif
%endif
%description pmda-libvirt
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
extracting virtualisation statistics from libvirt about behaviour of guest
and hypervisor machines.
# end pcp-pmda-libvirt
%endif

#
# pcp-pmda-elasticsearch
#
%package pmda-elasticsearch
Summary:        Performance Co-Pilot (PCP) metrics for Elasticsearch
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
%description pmda-elasticsearch
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Elasticsearch.
#end pcp-pmda-elasticsearch

%if !%{disable_lio}
#
# pcp-pmda-lio
#
%package pmda-lio
Summary:        Performance Co-Pilot (PCP) metrics for the LIO subsystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%if 0%{?suse_version}
Requires:       python3-rtslib-fb
%else
Requires:       python3-rtslib
%endif
%else # !%{disable_python3}
Requires:       %{__python2}-pcp
%if 0%{?suse_version}
Requires:       %{__python2}-rtslib-fb
%else
Requires:       %{__python2}-rtslib
%endif
%endif # !%{disable_python3}
%description pmda-lio
This package provides a PMDA to gather performance metrics from the kernels
iSCSI target interface (LIO). The metrics are stored by LIO within the Linux
kernels configfs filesystem. The PMDA provides per LUN level stats, and a
summary instance per iSCSI target, which aggregates all LUN metrics within the
target.
#end pcp-pmda-lio
%endif # !%{disable_lio}

#
# pcp-pmda-prometheus
#
%package pmda-prometheus
Summary:        Performance Co-Pilot (PCP) metrics from Prometheus endpoints
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
Requires:       python3-requests
BuildRequires:  python3-requests
%else
Requires:       %{__python2}-pcp
Requires:       %{__python2}-requests
BuildRequires:  %{__python2}-requests
%endif

%description pmda-prometheus
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
extracting statistics from programs instrumented as Prometheus endpoints.
#end pcp-pmda-prometheus

#
# pcp-pmda-lmsensors
#
%package pmda-lmsensors
Summary:        Performance Co-Pilot (PCP) metrics for hardware sensors
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
%else
Requires:       %{__python2}-pcp
%endif
# rewritten in python, so there is no longer a debuginfo package
Obsoletes:      pcp-pmda-lmsensors-debuginfo

%description pmda-lmsensors
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Linux hardware monitoring sensors.
# end pcp-pmda-lmsensors

%endif # !%{disable_python2} || !%{disable_python3}

%if !%{disable_json}
#
# pcp-pmda-json
#
%package pmda-json
Summary:        Performance Co-Pilot (PCP) metrics for JSON data
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp
Requires:       python3-six
BuildRequires:  python3-six
Requires:       python3-jsonpointer
BuildRequires:  python3-jsonpointer
%else
Requires:       %{__python2}-jsonpointer
Requires:       %{__python2}-pcp
Requires:       %{__python2}-six
BuildRequires:  %{__python2}-jsonpointer
BuildRequires:  %{__python2}-six
%endif
%description pmda-json
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics output in JSON.
# end pcp-pmda-json
%endif # !%{disable_json}

#
# C pmdas
# pcp-pmda-apache
#
%package pmda-apache
Summary:        Performance Co-Pilot (PCP) metrics for the Apache webserver
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-apache
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Apache webserver.
# end pcp-pmda-apache

#
# pcp-pmda-bash
#
%package pmda-bash
Summary:        Performance Co-Pilot (PCP) metrics for the Bash shell
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-bash
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Bash shell.
# end pcp-pmda-bash

#
# pcp-pmda-cifs
#
%package pmda-cifs
Summary:        Performance Co-Pilot (PCP) metrics for the CIFS protocol
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-cifs
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Common Internet Filesytem.
# end pcp-pmda-cifs

#
# pcp-pmda-cisco
#
%package pmda-cisco
Summary:        Performance Co-Pilot (PCP) metrics for Cisco routers
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-cisco
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Cisco routers.
# end pcp-pmda-cisco

#
# pcp-pmda-gfs2
#
%package pmda-gfs2
Summary:        Performance Co-Pilot (PCP) metrics for the GFS2 filesystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-gfs2
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Global Filesystem v2.
# end pcp-pmda-gfs2

#
# pcp-pmda-logger
#
%package pmda-logger
Summary:        Performance Co-Pilot (PCP) metrics from arbitrary log files
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-logger
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from a specified set of log files (or pipes).  The PMDA
supports both sampled and event-style metrics.
# end pcp-pmda-logger

#
# pcp-pmda-mailq
#
%package pmda-mailq
Summary:        Performance Co-Pilot (PCP) metrics for the sendmail queue
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-mailq
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about email queues managed by sendmail.
# end pcp-pmda-mailq

#
# pcp-pmda-mounts
#
%package pmda-mounts
Summary:        Performance Co-Pilot (PCP) metrics for filesystem mounts
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-mounts
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about filesystem mounts.
# end pcp-pmda-mounts

#
# pcp-pmda-nvidia-gpu
#
%package pmda-nvidia-gpu
Summary:        Performance Co-Pilot (PCP) metrics for the Nvidia GPU
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-nvidia-gpu
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Nvidia GPUs.
# end pcp-pmda-nvidia-gpu

#
# pcp-pmda-roomtemp
#
%package pmda-roomtemp
Summary:        Performance Co-Pilot (PCP) metrics for the room temperature
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}
Supplements:    pcp

%description pmda-roomtemp
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the room temperature.
# end pcp-pmda-roomtemp

%if !%{disable_rpm}
#
# pcp-pmda-rpm
#
%package pmda-rpm
Summary:        Performance Co-Pilot (PCP) metrics for the RPM package manager
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}

%description pmda-rpm
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the installed RPM packages.
%endif
# end pcp-pmda-rpm

#
# pcp-pmda-sendmail
#
%package pmda-sendmail
Summary:        Performance Co-Pilot (PCP) metrics for Sendmail
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}
Supplements:    pcp

%description pmda-sendmail
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Sendmail traffic.
# end pcp-pmda-sendmail

#
# pcp-pmda-shping
#
%package pmda-shping
Summary:        Performance Co-Pilot (PCP) metrics for shell command responses
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-shping
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about quality of service and response time measurements of
arbitrary shell commands.
# end pcp-pmda-shping

#
# pcp-pmda-smart
#
%package pmda-smart
Summary:        Performance Co-Pilot (PCP) metrics for S.M.A.R.T values
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
Requires:       %{lib_pkg} = %{version}-%{release}

%description pmda-smart
This package contains the PCP Performance Metric Domain Agent (PMDA) for
collecting metrics of disk S.M.A.R.T values making use of data from the
smartmontools package.
#end pcp-pmda-smart

#
# pcp-pmda-summary
#
%package pmda-summary
Summary:        Performance Co-Pilot (PCP) summary metrics from pmie
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}
Supplements:    pcp

%description pmda-summary
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about other installed pmdas.
# end pcp-pmda-summary

%if !%{disable_systemd}
#
# pcp-pmda-systemd
#
%package pmda-systemd
Summary:        Performance Co-Pilot (PCP) metrics from the Systemd journal
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-systemd
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from the Systemd journal.
# end pcp-pmda-systemd
%endif

#
# pcp-pmda-trace
#
%package pmda-trace
Summary:        Performance Co-Pilot (PCP) metrics for application tracing
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Supplements:    pcp

%description pmda-trace
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about trace performance data in applications.
# end pcp-pmda-trace

#
# pcp-pmda-weblog
#
%package pmda-weblog
Summary:        Performance Co-Pilot (PCP) metrics from web server logs
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       pcp = %{version}-%{release}
Supplements:    pcp

%description pmda-weblog
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about web server logs.
# end pcp-pmda-weblog
# end C pmdas

%package zeroconf
Summary:        Performance Co-Pilot (PCP) Zeroconf Package
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       pcp
Requires:       pcp-doc
Requires:       pcp-pmda-dm
Requires:       pcp-pmda-nfsclient
Requires:       pcp-system-tools
# to make pcp-zeroconf replace sysstat, uncomment the next line
# Obsoletes: sysstat
%description zeroconf
This package contains configuration tweaks and files to increase metrics
gathering frequency, several extended pmlogger configurations, as well as
automated pmie diagnosis, alerting and self-healing for the localhost.
A timer script also writes daily performance summary reports similar to
those written by sysstat.

%if !%{disable_python2}
#
# python-pcp. This is the PCP library bindings for python.
#
%package -n %{__python2}-pcp
Summary:        Performance Co-Pilot (PCP) Python bindings and documentation
License:        %{license_gplv2plus}
Group:          %{lib_gr}
Url:            https://pcp.io
BuildRequires:  %{__python2}-devel
Requires:       %{lib_pkg} = %{version}-%{release}
%if 0%{?suse_version}
Requires:       libpcp_gui%{libpcp_gui_sover} = %{version}-%{release}
Requires:       libpcp_import%{libpcp_import_sover} = %{version}-%{release}
Requires:       libpcp_mmv%{libpcp_mmv_sover} = %{version}-%{release}
%endif
Requires:       %{__python2}
Requires:       pcp = %{version}-%{release}
BuildRequires:  %{__python2}-setuptools
%if 0%{?fedora} >= 26 || 0%{?rhel} > 7 || 0%{?sle_version} > 150000
# on these platforms, python2-pcp replaces python-pcp
Obsoletes:      python-pcp
%endif

%description -n %{__python2}-pcp
This python PCP module contains the language bindings for
Performance Metric API (PMAPI) monitor tools and Performance
Metric Domain Agent (PMDA) collector tools written in Python.
%endif	# !%{disable_python2}

%if !%{disable_python3}
#
# python3-pcp. This is the PCP library bindings for python3.
#
%package -n python3-pcp
Summary:        Performance Co-Pilot (PCP) Python3 bindings and documentation
License:        %{license_gplv2plus}
Group:          %{lib_gr}
Url:            https://pcp.io
Requires:       %{lib_pkg} = %{version}-%{release}
%if 0%{?suse_version}
Requires:       libpcp_gui%{libpcp_gui_sover} = %{version}-%{release}
Requires:       libpcp_import%{libpcp_import_sover} = %{version}-%{release}
Requires:       libpcp_mmv%{libpcp_mmv_sover} = %{version}-%{release}
%endif
Requires:       python3
BuildRequires:  python3-setuptools

%description -n python3-pcp
This python PCP module contains the language bindings for
Performance Metric API (PMAPI) monitor tools and Performance
Metric Domain Agent (PMDA) collector tools written in Python3.
%endif

%if !%{disable_python2} || !%{disable_python3}
#
# pcp-system-tools
#
%package system-tools
Summary:        Performance Co-Pilot (PCP) System and Monitoring Tools
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !%{disable_python3}
Requires:       python3-pcp = %{version}-%{release}
%endif
%if !%{disable_python2}
Requires:       %{__python2}-pcp = %{version}-%{release}
%endif
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description system-tools
This PCP module contains additional system monitoring tools written
in python.
%endif #end pcp-system-tools
%if !%{disable_qt}
#
# pcp-gui package for Qt tools
#
%package gui
Summary:        Visualization tools for the Performance Co-Pilot toolkit
License:        %{license_gplv2plus} AND %{license_lgplv2plus}
Group:          %{pcp_gr}
Url:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description gui
Visualization tools for the Performance Co-Pilot toolkit.
The pcp-gui package primarily includes visualization tools for
monitoring systems using live and archived Performance Co-Pilot
(PCP) sources.
%endif

#
# pcp-doc package
#
%package doc
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Documentation and tutorial for the Performance Co-Pilot
License:        %{license_gplv2plus} AND %{license_cc_by}
Group:          Documentation/Other
Url:            https://pcp.io
# http://fedoraproject.org/wiki/Packaging:Conflicts "Splitting Packages"
# (all man pages migrated to pcp-doc during great package split of '15)
Conflicts:      pcp-pmda-pmda < 3.10.5
Conflicts:      pcp-pmda-infiniband < 3.10.5

%description doc
Documentation and tutorial for the Performance Co-Pilot
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management.

The pcp-doc package provides useful information on using and
configuring the Performance Co-Pilot (PCP) toolkit for system
level performance management.  It includes tutorials, HOWTOs,
and other detailed documentation about the internals of core
PCP utilities and daemons, and the PCP graphical tools.

#
# pcp-selinux package
#
%if !%{disable_selinux}
%package selinux
Summary:        Selinux policy package
License:        %{license_gplv2plus} AND %{license_cc_by}
Group:          Applications/System
Url:            https://pcp.io
BuildRequires:  selinux-policy-devel
%if 0%{?rhel} == 5
BuildRequires:  setools
%else
BuildRequires:  setools-console
%endif
Requires:       pcp = %{version}-%{release}
Requires:       policycoreutils

%description selinux
This package contains SELinux support for PCP.  The package contains
interface rules, type enforcement and file context adjustments for an
updated policy package.
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1

autoconf

%clean
rm -Rf $RPM_BUILD_ROOT

%build
%define _lto_cflags %{nil}
%if 0%{?suse_version}
# in case we're building without os-release (bsc#1123311)...
export PACKAGE_DISTRIBUTION="suse"
%endif
export PACKAGE_BUILD_DATE=`date -u -r CHANGELOG +%Y-%m-%d`
PCP_CFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" CCFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" %configure \
   --with-tmpdir=%{_tempsdir} \
   --datarootdir=%{_datadir} \
   --docdir=%{_docdir} \
   --with-dstat-symlink=no \
   %{?_with_initd} \
   %{?_with_doc} \
   %{?_with_ib} \
   %{?_with_perfevent} \
   %{?_with_json} \
   %{?_with_snmp} \
   %{?_with_nutcracker} \
   %{?_with_python2}
PCP_CFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" CCFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" make default_pcp

###############################################################################

%install
export NO_CHOWN=true DIST_ROOT=$RPM_BUILD_ROOT
make install_pcp

PCP_GUI='pmchart|pmconfirm|pmdumptext|pmmessage|pmquery|pmsnap|pmtime'

# Fix stuff we do/don't want to ship
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a

%if %{disable_sheet2pcp}
# remove sheet2pcp until BZ 830923 and BZ 754678 are resolved.
rm -f $RPM_BUILD_ROOT/%{_bindir}/sheet2pcp $RPM_BUILD_ROOT/%{_mandir}/man1/sheet2pcp.1*
%endif

%if %{disable_libvirt}
rm -fr $RPM_BUILD_ROOT/%{_pmdasdir}/libvirt
%endif

%if %{disable_postgresql}
rm -fr $RPM_BUILD_ROOT/%{_pmdasdir}/postgresql
%endif

# remove {config,platform}sz.h as these are not multilib friendly.
rm -f $RPM_BUILD_ROOT/%{_includedir}/pcp/configsz.h
rm -f $RPM_BUILD_ROOT/%{_includedir}/pcp/platformsz.h

%if %{disable_microhttpd}
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/pmwebd.*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man3/PMWEBAPI.*
rm -fr $RPM_BUILD_ROOT/%{_confdir}/pmwebd
rm -fr $RPM_BUILD_ROOT/%{_initddir}/pmwebd
rm -fr $RPM_BUILD_ROOT/%{_unitdir}/pmwebd.service
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/pcp/bin/pmwebd
%endif

%if %{disable_infiniband}
# remove pmdainfiniband on platforms lacking IB devel packages.
rm -f $RPM_BUILD_ROOT/%{_pmdasdir}/ib
rm -fr $RPM_BUILD_ROOT/%{_pmdasdir}/infiniband
%endif

%if %{disable_selinux}
rm -fr $RPM_BUILD_ROOT/%{_selinuxdir}
%endif

%if %{disable_qt}
%if !0%{?suse_version}
rm -fr $RPM_BUILD_ROOT/%{_pixmapdir}
%endif
rm -fr $RPM_BUILD_ROOT/%{_confdir}/pmsnap
rm -fr $RPM_BUILD_ROOT/%{_localstatedir}/lib/pcp/config/pmsnap
rm -fr $RPM_BUILD_ROOT/%{_localstatedir}/lib/pcp/config/pmchart
rm -f $RPM_BUILD_ROOT/%{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
rm -f $RPM_BUILD_ROOT/%{_datadir}/applications/pmchart.desktop
rm -f `find $RPM_BUILD_ROOT/%{_mandir}/man1 | grep -E "$PCP_GUI"`
%else
rm -rf $RPM_BUILD_ROOT/usr/share/doc/pcp-gui
%if 0%{?suse_version}
mkdir -p $RPM_BUILD_ROOT/%{_pixmapdir}
mv $RPM_BUILD_ROOT/%{_datadir}/pcp-gui/pixmaps/*.png $RPM_BUILD_ROOT/%{_pixmapdir}
rm -rf $RPM_BUILD_ROOT/%{_datadir}/pcp-gui/pixmaps
%suse_update_desktop_file -r -G 'Performance Copilot Chart' $RPM_BUILD_ROOT/%{_datadir}/applications/pmchart.desktop System Monitor
%else
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pmchart.desktop
%endif
%endif

%if %{disable_lio}
rm -fr $RPM_BUILD_ROOT/%{_pmdasdir}/lio
%endif

rm -f $RPM_BUILD_ROOT/%{_localstatedir}/lib/pcp/testsuite/perfevent/perfevent_coverage # drop unreproducible file (boo#1040589)

%if 0%{?suse_version}
rm -rf $RPM_BUILD_ROOT/%{_datadir}/pcp/webapps

mkdir -p $RPM_BUILD_ROOT/%{_tempsdir}

%__install -d -m 0755 ${RPM_BUILD_ROOT}/%{_sbindir}

%if !0%{?has_systemd}
# add /etc/init.d/X symlinks at /usr/sbin/rcX
for script in pcp pmie pmproxy pmlogger pmcd; do
	ln -s "%{_sysconfdir}/init.d/${script}" \
	      "${RPM_BUILD_ROOT}/%{_sbindir}/rc${script}"
done
%else
ln -sf /sbin/service $RPM_BUILD_ROOT/%{_sbindir}/rcpmcd
ln -sf /sbin/service $RPM_BUILD_ROOT/%{_sbindir}/rcpmie
ln -sf /sbin/service $RPM_BUILD_ROOT/%{_sbindir}/rcpmlogger
ln -sf /sbin/service $RPM_BUILD_ROOT/%{_sbindir}/rcpmproxy
ln -sf /sbin/service $RPM_BUILD_ROOT/%{_sbindir}/rcpmmgr
ln -sf /sbin/service $RPM_BUILD_ROOT/%{_sbindir}/rcpmwebd
%endif

# SUSE requires use of %fillup_and_insserv
mkdir -p $RPM_BUILD_ROOT/%{_fillupdir}
for f in pmlogger pmproxy pmcd pmie_timers pmlogger_timers; do
	mv $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/${f} \
		$RPM_BUILD_ROOT/%{_fillupdir}/sysconfig.${f}
done

%else
# default chkconfig off for Fedora and RHEL
for f in $RPM_BUILD_ROOT/%{_initddir}/{pcp,pmcd,pmlogger,pmie,pmwebd,pmmgr,pmproxy}; do
	test -f "$f" || continue
	sed -i -e '/^# chkconfig/s/:.*$/: - 95 05/' -e '/^# Default-Start:/s/:.*$/:/' $f
done
%endif

# list of PMDAs in the base pkg
ls -1 $RPM_BUILD_ROOT/%{_pmdasdir} |\
  grep -E -v '^simple|sample|trivial|txmon' |\
  grep -E -v '^perfevent|perfalloc.1' |\
  grep -E -v '^ib$|^infiniband' |\
  grep -E -v '^activemq' |\
  grep -E -v '^bonding' |\
  grep -E -v '^bind2' |\
  grep -E -v '^dbping' |\
  grep -E -v '^docker' |\
  grep -E -v '^ds389log'|\
  grep -E -v '^ds389' |\
  grep -E -v '^elasticsearch' |\
  grep -E -v '^gpfs' |\
  grep -E -v '^gpsd' |\
  grep -E -v '^lio' |\
  grep -E -v '^lustre' |\
  grep -E -v '^lustrecomm' |\
  grep -E -v '^memcache' |\
  grep -E -v '^mysql' |\
  grep -E -v '^named' |\
  grep -E -v '^netfilter' |\
  grep -E -v '^news' |\
  grep -E -v '^nfsclient' |\
  grep -E -v '^nginx' |\
  grep -E -v '^nutcracker' |\
  grep -E -v '^oracle' |\
  grep -E -v '^pdns' |\
  grep -E -v '^postfix' |\
  grep -E -v '^postgresql' |\
  grep -E -v '^prometheus' |\
  grep -E -v '^redis' |\
  grep -E -v '^rsyslog' |\
  grep -E -v '^samba' |\
  grep -E -v '^slurm' |\
  grep -E -v '^snmp' |\
  grep -E -v '^vmware' |\
  grep -E -v '^zimbra' |\
  grep -E -v '^dm' |\
  grep -E -v '^apache' |\
  grep -E -v '^bash' |\
  grep -E -v '^cifs' |\
  grep -E -v '^cisco' |\
  grep -E -v '^gfs2' |\
  grep -E -v '^libvirt' |\
  grep -E -v '^lmsensors' |\
  grep -E -v '^logger' |\
  grep -E -v '^mailq' |\
  grep -E -v '^mounts' |\
  grep -E -v '^nvidia' |\
  grep -E -v '^roomtemp' |\
  grep -E -v '^sendmail' |\
  grep -E -v '^shping' |\
  grep -E -v '^smart' |\
  grep -E -v '^summary' |\
  grep -E -v '^trace' |\
  grep -E -v '^weblog' |\
  grep -E -v '^rpm' |\
  grep -E -v '^json' |\
  grep -E -v '^mic' |\
  grep -E -v '^gluster' |\
  grep -E -v '^zswap' |\
  grep -E -v '^unbound' |\
  grep -E -v '^haproxy' |\
  sed -e 's#^#'%{_pmdasdir}'\/#' >base_pmdas.list

# all base pcp package files except those split out into sub packages
ls -1 $RPM_BUILD_ROOT/%{_bindir} |\
  grep -E -v 'pmiostat|pmcollectl|zabbix|zbxpcp|dstat' |\
  grep -E -v 'pmrep|pcp2csv|pcp2graphite|pcp2influxdb|pcp2zabbix' |\
  grep -E -v 'pcp2elasticsearch|pcp2json|pcp2xlsx|pcp2xml' |\
  grep -E -v 'pcp2spark' |\
  grep -E -v 'pmdbg|pmclient|pmerr|genpmda' |\
sed -e 's#^#'%{_bindir}'\/#' >base_bin.list
#
# Separate the pcp-system-tools package files.
# pmcollectl and pmiostat are back-compat symlinks to their
# pcp(1) sub-command variants so are also in pcp-system-tools.
%if !%{disable_python2} || !%{disable_python3}
ls -1 $RPM_BUILD_ROOT/%{_bindir} |\
  egrep -e 'pmiostat|pmcollectl|pmrep|pcp2csv|dstat' |\
  sed -e 's#^#'%{_bindir}'\/#' >pcp-system-tools.list
ls -1 $RPM_BUILD_ROOT/%{_libexecdir}/pcp/bin |\
  egrep -e 'atop|collectl|dmcache|dstat|free|iostat|ipcs|lvmcache|mpstat' \
        -e 'numastat|pidstat|shping|tapestat|uptime|verify' |\
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >>pcp-system-tools.list
%endif
# Separate the pcp-selinux package files.
%if !%{disable_selinux}
ls -1 $RPM_BUILD_ROOT/%{_selinuxdir} |\
  sed -e 's#^#'%{_selinuxdir}'\/#' > pcp-selinux.list
ls -1 $RPM_BUILD_ROOT/%{_libexecdir}/pcp/bin |\
  grep -E 'selinux-setup' |\
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >> pcp-selinux.list
%endif

ls -1 $RPM_BUILD_ROOT/%{_libexecdir}/pcp/bin |\
%if !%{disable_python2} || !%{disable_python3}
  grep -E -v 'atop|collectl|dmcache|lvmcache|dstat|free|iostat|ipcs|mpstat|numastat' |\
  grep -E -v 'shping|tapestat|uptime|verify|selinux-setup' |\
%endif
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >base_exec.list
ls -1 $RPM_BUILD_ROOT/%{_booksdir} |\
  sed -e 's#^#'%{_booksdir}'\/#' > pcp-doc.list
ls -1 $RPM_BUILD_ROOT/%{_mandir}/man1 |\
  sed -e 's#^#'%{_mandir}'\/man1\/#' >>pcp-doc.list
ls -1 $RPM_BUILD_ROOT/%{_mandir}/man5 |\
  sed -e 's#^#'%{_mandir}'\/man5\/#' >>pcp-doc.list
%if 0%{?suse_version}
mv $RPM_BUILD_ROOT/%{_datadir}/pcp/demos $RPM_BUILD_ROOT/%{_docdir}/pcp
ls -1 $RPM_BUILD_ROOT/%{_docdir}/pcp/demos/tutorials |\
  sed -e 's#^#'%{_docdir}/pcp/demos/tutorials'\/#' >>pcp-doc.list
%else
ls -1 $RPM_BUILD_ROOT/%{_datadir}/pcp/demos/tutorials |\
  sed -e 's#^#'%{_datadir}/pcp/demos/tutorials'\/#' >>pcp-doc.list
%endif
%if !%{disable_qt}
ls -1 $RPM_BUILD_ROOT/%{_pixmapdir} |\
  sed -e 's#^#'%{_pixmapdir}'\/#' > pcp-gui.list
cat base_bin.list base_exec.list |\
  grep -E "$PCP_GUI" >> pcp-gui.list
%endif
ls -1 $RPM_BUILD_ROOT/%{_logconfdir}/ |\
    sed -e 's#^#'%{_logconfdir}'\/#' |\
    grep -E -v 'zeroconf' >pcp-logconf.list
cat base_pmdas.list base_bin.list base_exec.list pcp-logconf.list |\
  grep -E -v 'pmdaib|pmmgr|pmweb|pmsnap|2pcp|pmdas/systemd' |\
  grep -E -v "$PCP_GUI|pixmaps|pcp-doc|tutorials|selinux|pmlogger_daily_report" |\
  grep -E -v %{_confdir} | grep -E -v %{_logsdir} > base.list

# all devel pcp package files except those split out into sub packages
ls -1 $RPM_BUILD_ROOT/%{_mandir}/man3 |\
sed -e 's#^#'%{_mandir}'\/man3\/#' | grep -v '3pm' >>pcp-doc.list
%if 0%{?suse_version}
ls -1 $RPM_BUILD_ROOT/%{_docdir}/pcp/demos |\
sed -e 's#^#'%{_docdir}'\/pcp\/demos\/#' | grep -E -v tutorials >> devel.list
%else
ls -1 $RPM_BUILD_ROOT/%{_datadir}/pcp/demos |\
sed -e 's#^#'%{_datadir}'\/pcp\/demos\/#' | grep -E -v tutorials >> devel.list
%endif
ls -1 $RPM_BUILD_ROOT/%{_bindir} |\
grep -E 'pmdbg|pmclient|pmerr|genpmda' |\
sed -e 's#^#'%{_bindir}'\/#' >>devel.list

%pre testsuite
test -d %{_testsdir} || mkdir -p -m 755 %{_testsdir}
getent group pcpqa >/dev/null || groupadd -r pcpqa
getent passwd pcpqa >/dev/null || \
  useradd -c "PCP Quality Assurance" -g pcpqa -d %{_testsdir} -M -r -s /bin/bash pcpqa 2>/dev/null
chown -R pcpqa:pcpqa %{_testsdir} 2>/dev/null
exit 0

%post testsuite
chown -R pcpqa:pcpqa %{_testsdir} 2>/dev/null
exit 0

%if 0%{?suse_version} && !%{disable_systemd}
%pre zeroconf
%service_add_pre pmlogger_daily_report.timer pmlogger_daily_report-poll.timer
%endif

%pre
%if 0%{?suse_version} && !%{disable_systemd}
%service_add_pre pmcd pmlogger pmie pmproxy pmie_check.timer pmie_daily.timer pmlogger_daily.timer pmlogger_check.timer pmlogger_daily-poll.timer
%endif
getent group pcp >/dev/null || groupadd -r pcp
getent passwd pcp >/dev/null || \
  useradd -c "Performance Co-Pilot" -g pcp -d %{_localstatedir}/lib/pcp -M -r -s /sbin/nologin pcp
%if !0%{?suse_version}
PCP_CONFIG_DIR=%{_localstatedir}/lib/pcp/config
PCP_SYSCONF_DIR=%{_confdir}
PCP_LOG_DIR=%{_logsdir}
PCP_ETC_DIR=%{_sysconfdir}
# rename crontab files to align with current Fedora packaging guidelines
for crontab in pmlogger pmie
do
    test -f "$PCP_ETC_DIR/cron.d/$crontab" || continue
    mv -f "$PCP_ETC_DIR/cron.d/$crontab" "$PCP_ETC_DIR/cron.d/pcp-$crontab"
done
# produce a script to run post-install to move configs to their new homes
save_configs_script()
{
    _new="$1"
    shift
    for _dir
    do
        [ "$_dir" = "$_new" ] && continue
        if [ -d "$_dir" ]
        then
            ( cd "$_dir" ; find . -maxdepth 1 -type f ) | sed -e 's/^\.\///' \
            | while read _file
            do
                [ "$_file" = "control" ] && continue
                _want=true
                if [ -f "$_new/$_file" ]
                then
                    # file exists in both directories, pick the more
                    # recently modified one
                    _try=`find "$_dir/$_file" -newer "$_new/$_file" -print`
                    [ -n "$_try" ] || _want=false
                fi
                $_want && echo cp -p "$_dir/$_file" "$_new/$_file"
            done
        fi
    done
}
# migrate and clean configs if we have had a previous in-use installation
[ -d "$PCP_LOG_DIR" ] || exit 0	# no configuration file upgrades required
rm -f "$PCP_LOG_DIR/configs.sh"
for daemon in pmie pmlogger
do
    save_configs_script >> "$PCP_LOG_DIR/configs.sh" "$PCP_CONFIG_DIR/$daemon" \
        "$PCP_SYSCONF_DIR/$daemon"
done
for daemon in pmcd pmproxy
do
    save_configs_script >> "$PCP_LOG_DIR/configs.sh" "$PCP_SYSCONF_DIR/$daemon"\
        "$PCP_CONFIG_DIR/$daemon" /etc/$daemon
done
%endif
exit 0

%if !%{disable_microhttpd}
%preun webapi
%if 0%{?suse_version}
%if !%{disable_systemd}
%service_del_preun pmwebd
%else
%{stop_on_removal pmwebd}
%endif
%else
if [ "$1" -eq 0 ]
then
%if !%{disable_systemd}
    systemctl --no-reload disable pmwebd.service >/dev/null 2>&1
    systemctl stop pmwebd.service >/dev/null 2>&1
%else
    /sbin/service pmwebd stop >/dev/null 2>&1
    /sbin/chkconfig --del pmwebd >/dev/null 2>&1
%endif
fi
%endif
%endif

%preun manager
%if 0%{?suse_version}
%if !%{disable_systemd}
%service_del_preun pmmgr
%else
%{stop_on_removal pmmgr}
%endif
%else
if [ "$1" -eq 0 ]
then
%if !%{disable_systemd}
    systemctl --no-reload disable pmmgr.service >/dev/null 2>&1
    systemctl stop pmmgr.service >/dev/null 2>&1
%else
    /sbin/service pmmgr stop >/dev/null 2>&1
    /sbin/chkconfig --del pmmgr >/dev/null 2>&1
%endif
fi
%endif

%if 0%{?suse_version} && !%{disable_systemd}
%preun zeroconf
%service_del_preun pmlogger_daily_report.timer pmlogger_daily_report-poll.timer
%endif

%preun
%if 0%{?suse_version}
%if !%{disable_systemd}
%service_del_preun pmlogger pmie pmproxy pmcd
%else
%{?stop_on_removal:%{stop_on_removal pmlogger pmie pmproxy pmcd}}
%endif
%else
if [ "$1" -eq 0 ]
then
    # stop daemons before erasing the package
    %if !%{disable_systemd}
	systemctl --no-reload disable pmlogger pmie pmproxy pmcd >/dev/null 2>&1
	systemctl stop pmlogger pmie pmproxy pmcd >/dev/null 2>&1
    %else
	/sbin/service pmlogger stop >/dev/null 2>&1
	/sbin/service pmie stop >/dev/null 2>&1
	/sbin/service pmproxy stop >/dev/null 2>&1
	/sbin/service pmcd stop >/dev/null 2>&1

	/sbin/chkconfig --del pcp >/dev/null 2>&1
	/sbin/chkconfig --del pmcd >/dev/null 2>&1
	/sbin/chkconfig --del pmlogger >/dev/null 2>&1
	/sbin/chkconfig --del pmie >/dev/null 2>&1
	/sbin/chkconfig --del pmproxy >/dev/null 2>&1
    %endif
    # cleanup namespace state/flag, may still exist
    PCP_PMNS_DIR=%{_pmnsdir}
    rm -f "$PCP_PMNS_DIR/.NeedRebuild" >/dev/null 2>&1
fi
%endif

%if !%{disable_microhttpd}
%post webapi
chown -R pcp:pcp %{_logsdir}/pmwebd 2>/dev/null
%if 0%{?suse_version}
%if !%{disable_systemd}
%service_add_post pmwebd
%else
%{fillup_and_insserv pmwebd}
%endif
%else
%if !%{disable_systemd}
    systemctl condrestart pmwebd.service >/dev/null 2>&1
%else
    /sbin/chkconfig --add pmwebd >/dev/null 2>&1
    /sbin/service pmwebd condrestart
%endif
%endif
%endif

%post manager
chown -R pcp:pcp %{_logsdir}/pmmgr 2>/dev/null
%if 0%{?suse_version}
%if !%{disable_systemd}
%service_add_post pmmgr
%else
%{fillup_and_insserv pmmgr}
%endif
%else
%if !%{disable_systemd}
    systemctl condrestart pmmgr.service >/dev/null 2>&1
%else
    /sbin/chkconfig --add pmmgr >/dev/null 2>&1
    /sbin/service pmmgr condrestart
%endif
%endif

%post zeroconf
%if 0%{?suse_version}
%if !%{disable_systemd}
%service_add_post pmlogger_daily_report.timer pmlogger_daily_report-poll.timer
%endif
%else
%if !%{disable_systemd}
    systemctl restart pmcd >/dev/null 2>&1
    systemctl restart pmlogger >/dev/null 2>&1
    systemctl restart pmie >/dev/null 2>&1
    systemctl enable pmcd >/dev/null 2>&1
    systemctl enable pmlogger >/dev/null 2>&1
    systemctl enable pmlogger_daily_report >/dev/null 2>&1
    systemctl enable pmlogger_daily_report-poll >/dev/null 2>&1
    systemctl enable pmie >/dev/null 2>&1
%else
    /sbin/chkconfig --add pmcd >/dev/null 2>&1
    /sbin/chkconfig --add pmlogger >/dev/null 2>&1
    /sbin/chkconfig --add pmie >/dev/null 2>&1
    /sbin/service pmcd condrestart
    /sbin/service pmlogger condrestart
    /sbin/service pmie condrestart
%endif
%endif #zeroconf

%if !%{disable_selinux}
%post selinux
%if 0%{?fedora} >= 24 || 0%{?rhel} > 6
    semodule -X 400 -i %{_selinuxdir}/pcpupstream.pp
%else
    semodule -i %{_selinuxdir}/pcpupstream.pp
%endif #distro version check
%triggerin selinux -- docker-selinux
if ls %{_selinuxdir} | grep -q docker 2>/dev/null
then
%if 0%{?fedora} >= 24 || 0%{?rhel} > 6
    semodule -X 400 -i %{_selinuxdir}/pcpupstream-docker.pp
%else
    semodule -i %{_selinuxdir}/pcpupstream-docker.pp
%endif #distro version check
fi

%triggerin selinux -- container-selinux
if ls %{_selinuxdir} | grep -q container 2>/dev/null
then
%if 0%{?fedora} >= 24 || 0%{?rhel} > 6
    semodule -X 400 -i %{_selinuxdir}/pcpupstream-container.pp
%else
    semodule -i %{_selinuxdir}/pcpupstream-container.pp
%endif #distro version check
fi
%endif

%post
PCP_LOG_DIR=%{_logsdir}
PCP_PMNS_DIR=%{_pmnsdir}
# restore saved configs, if any
test -s "$PCP_LOG_DIR/configs.sh" && source "$PCP_LOG_DIR/configs.sh"
rm -f $PCP_LOG_DIR/configs.sh

# migrate old to new temp dir locations (within the same filesystem)
migrate_tempdirs()
{
    _sub="$1"
    _new_tmp_dir=%{_tempsdir}
    _old_tmp_dir=%{_localstatedir}/tmp

    for d in "$_old_tmp_dir/$_sub" ; do
        test -d "$d" -a -k "$d" || continue
        cd "$d" || continue
        for f in * ; do
            [ "$f" != "*" ] || continue
            source="$d/$f"
            target="$_new_tmp_dir/$_sub/$f"
            [ "$source" != "$target" ] || continue
	    [ -f "$target" ] || mv -fu "$source" "$target"
        done
        cd && rmdir "$d" 2>/dev/null
    done
}
for daemon in mmv pmdabash pmie pmlogger
do
    migrate_tempdirs $daemon
done
chown -R pcp:pcp %{_logsdir}/pmcd 2>/dev/null
chown -R pcp:pcp %{_logsdir}/pmlogger 2>/dev/null
chown -R pcp:pcp %{_logsdir}/pmie 2>/dev/null
chown -R pcp:pcp %{_logsdir}/pmproxy 2>/dev/null
touch "$PCP_PMNS_DIR/.NeedRebuild"
chmod 644 "$PCP_PMNS_DIR/.NeedRebuild"
%if 0%{?suse_version}
%if !%{disable_systemd}
%{fillup_only -n pmcd}
%{fillup_only -n pmlogger}
%{fillup_only -n pmproxy}
%service_add_post pmcd pmlogger pmie pmproxy pmie_check.timer pmie_daily.timer pmlogger_daily.timer pmlogger_check.timer pmlogger_daily-poll.timer
%else
%{fillup_and_insserv pmcd}
%{fillup_and_insserv pmlogger}
%{fillup_and_insserv pmie}
%{fillup_and_insserv pmproxy}
%{fillup_and_insserv pmie_timers}
%{fillup_and_insserv pmlogger_timers}
%endif
%else
%if !%{disable_systemd}
    systemctl condrestart pmcd pmlogger pmie pmproxy >/dev/null 2>&1
%else
    /sbin/chkconfig --add pmcd >/dev/null 2>&1
    /sbin/service pmcd condrestart
    /sbin/chkconfig --add pmlogger >/dev/null 2>&1
    /sbin/service pmlogger condrestart
    /sbin/chkconfig --add pmie >/dev/null 2>&1
    /sbin/service pmie condrestart
    /sbin/chkconfig --add pmproxy >/dev/null 2>&1
    /sbin/service pmproxy condrestart
%endif
%endif

(cd $PCP_PMNS_DIR && ./Rebuild -s && rm -f .NeedRebuild)

%post -n %{lib_pkg} -p /sbin/ldconfig
%postun -n %{lib_pkg} -p /sbin/ldconfig
%if 0%{?suse_version}
%post -n libpcp_gui%{libpcp_gui_sover} -p /sbin/ldconfig
%postun -n libpcp_gui%{libpcp_gui_sover} -p /sbin/ldconfig

%post -n libpcp_mmv%{libpcp_mmv_sover} -p /sbin/ldconfig
%postun -n libpcp_mmv%{libpcp_mmv_sover} -p /sbin/ldconfig

%post -n libpcp_trace%{libpcp_trace_sover} -p /sbin/ldconfig
%postun -n libpcp_trace%{libpcp_trace_sover} -p /sbin/ldconfig

%post -n libpcp_import%{libpcp_import_sover} -p /sbin/ldconfig
%postun -n libpcp_import%{libpcp_import_sover} -p /sbin/ldconfig

%post -n libpcp_web%{libpcp_web_sover} -p /sbin/ldconfig
%postun -n libpcp_web%{libpcp_web_sover} -p /sbin/ldconfig
%endif

%if !%{disable_selinux}
%preun selinux
if [ `semodule -l | grep pcpupstream` ]
then
%if 0%{?fedora} >= 24 || 0%{?rhel} > 6
    semodule -X 400 -r pcpupstream >/dev/null
%else
    semodule -r pcpupstream >/dev/null
%endif
fi

%triggerun selinux -- docker-selinux
if [ `semodule -l | grep pcpupstream-docker` ]
then
%if 0%{?fedora} >= 24 || 0%{?rhel} > 6
    semodule -X 400 -r pcpupstream-docker
%else
semodule -r pcpupstream-docker
%endif #distro version check
fi

%triggerun selinux -- container-selinux
if [ `semodule -l | grep pcpupstream-container` ]
then
%if 0%{?fedora} >= 24 || 0%{?rhel} > 6
    semodule -X 400 -r pcpupstream-container
%else
    semodule -r pcpupstream-container
%endif #distro version check
fi
%endif

%if 0%{?suse_version} && !%{disable_systemd}
%postun zeroconf
%service_del_postun pmlogger_daily_report.timer pmlogger_daily_report-poll.timer
%endif

%if 0%{?suse_version}
%postun
/sbin/ldconfig
%if !%{disable_systemd}
%service_del_postun pmcd pmlogger pmproxy pmie pmie_check.timer pmie_daily.timer pmlogger_daily.timer pmlogger_check.timer pmlogger_daily-poll.timer
%else
%{?restart_on_update:%{restart_on_update pcp pmproxy pmie}}
%{?insserv_cleanup:%{insserv_cleanup}}
%endif
%endif

%files -f base.list
#
# Note: there are some headers (e.g. domain.h) and in a few cases some
# C source files that rpmlint complains about. These are not devel files,
# but rather they are (slightly obscure) PMDA config files.
#
%defattr(-,root,root)
%doc CHANGELOG INSTALL.md README.md VERSION.pcp pcp.lsm
%license COPYING
%if 0%{?suse_version}
%exclude %{_docdir}/pcp/demos
%exclude %{_testsdir}
%endif

%dir %{_confdir}
%dir %{_pmdasdir}
%dir %{_datadir}/pcp
%dir %{_localstatedir}/lib/pcp
%if 0%{?suse_version}
%dir %{_libdir}/pcp
%dir %{_libdir}/pcp/bin
%endif
%dir %{_localstatedir}/lib/pcp/config
%if 0%{?suse_version}
# part of pcp-gui
%exclude %{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
%{_initddir}/pcp
%{_initddir}/pmcd
%{_initddir}/pmlogger
%{_initddir}/pmie
%{_initddir}/pmproxy
%endif
%dir %attr(0775,pcp,pcp) %{_tempsdir}
%dir %attr(0775,pcp,pcp) %{_tempsdir}/pmie
%dir %attr(0775,pcp,pcp) %{_tempsdir}/pmlogger
%dir %attr(0700,root,root) %{_tempsdir}/pmcd

%dir %{_datadir}/pcp/lib
%{_datadir}/pcp/lib/ReplacePmnsSubtree
%{_datadir}/pcp/lib/bashproc.sh
%{_datadir}/pcp/lib/lockpmns
%{_datadir}/pcp/lib/pmdaproc.sh
%{_datadir}/pcp/lib/utilproc.sh
%{_datadir}/pcp/lib/rc-proc.sh
%{_datadir}/pcp/lib/rc-proc.sh.minimal
%{_datadir}/pcp/lib/unlockpmns

%dir %attr(0775,pcp,pcp) %{_logsdir}
%attr(0775,pcp,pcp) %{_logsdir}/pmcd
%attr(0775,pcp,pcp) %{_logsdir}/pmlogger
%attr(0775,pcp,pcp) %{_logsdir}/pmie
%attr(0775,pcp,pcp) %{_logsdir}/pmproxy
%{_localstatedir}/lib/pcp/pmns
%if %{disable_systemd}
%{_initrddir}/pcp
%{_initrddir}/pmcd
%{_initrddir}/pmlogger
%{_initrddir}/pmie
%{_initrddir}/pmproxy
%else
%{_unitdir}/pmcd.service
%{_unitdir}/pmlogger.service
%{_unitdir}/pmie.service
%{_unitdir}/pmproxy.service
%{_sbindir}/rcpmcd
%{_sbindir}/rcpmie
%{_sbindir}/rcpmlogger
%{_sbindir}/rcpmproxy
%endif
%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/pmcd.conf
%if %{disable_systemd}
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmlogger
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmie
%else
%{_unitdir}/pmie_check.service
%{_unitdir}/pmie_check.timer
%{_unitdir}/pmie_daily.service
%{_unitdir}/pmie_daily.timer
%{_unitdir}/pmlogger_daily.service
%{_unitdir}/pmlogger_daily.timer
%{_unitdir}/pmlogger_check.service
%{_unitdir}/pmlogger_check.timer
%{_unitdir}/pmlogger_daily-poll.service
%{_unitdir}/pmlogger_daily-poll.timer
%endif
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.pmlogger
%{_fillupdir}/sysconfig.pmproxy
%{_fillupdir}/sysconfig.pmcd
%{_fillupdir}/sysconfig.pmie_timers
%{_fillupdir}/sysconfig.pmlogger_timers
%else
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger
%config(noreplace) %{_sysconfdir}/sysconfig/pmproxy
%config(noreplace) %{_sysconfdir}/sysconfig/pmcd
%config(noreplace) %{_sysconfdir}/sysconfig/pmie_timers
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger_timers
%endif
%config %{_sysconfdir}/pcp.env
%dir %{_confdir}/pmcd
%config(noreplace) %{_confdir}/pmcd/pmcd.conf
%config(noreplace) %{_confdir}/pmcd/pmcd.options
%config(noreplace) %{_confdir}/pmcd/rc.local
%dir %{_confdir}/pmproxy
%config(noreplace) %{_confdir}/pmproxy/pmproxy.options
%config(noreplace) %{_confdir}/pmproxy/pmproxy.conf
%dir %{_confdir}/pmie
%dir %{_confdir}/pmie/control.d
%config(noreplace) %{_confdir}/pmie/control
%config(noreplace) %{_confdir}/pmie/control.d/local
%dir %{_confdir}/pmlogger
%dir %{_confdir}/pmlogger/control.d
%config(noreplace) %{_confdir}/pmlogger/control
%config(noreplace) %{_confdir}/pmlogger/control.d/local
%dir %attr(0775,pcp,pcp) %{_confdir}/nssdb
%dir %{_confdir}/discover
%config(noreplace) %{_confdir}/discover/pcp-kube-pods.conf

%{_localstatedir}/lib/pcp/config/pmafm
%dir %attr(0775,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmie
%{_localstatedir}/lib/pcp/config/pmie
%{_localstatedir}/lib/pcp/config/pmieconf
%dir %attr(0775,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmlogger
%{_localstatedir}/lib/pcp/config/pmlogger/*
%dir %{_logconfdir}
%{_localstatedir}/lib/pcp/config/pmlogrewrite
%dir %attr(0775,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmda

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_pcp

%if !%{disable_sdt}
%{tapsetdir}/pmcd.stp
%endif

%files zeroconf
%defattr(-,root,root)
%{_libexecdir}/pcp/bin/pmlogger_daily_report
%if %{disable_systemd}
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmlogger-daily-report
%else
%{_unitdir}/pmlogger_daily_report.service
%{_unitdir}/pmlogger_daily_report.timer
%{_unitdir}/pmlogger_daily_report-poll.service
%{_unitdir}/pmlogger_daily_report-poll.timer
%endif
%{_logconfdir}/zeroconf

%files conf
%defattr(-,root,root)

%dir %{_includedir}/pcp
%{_includedir}/pcp/builddefs
%{_includedir}/pcp/buildrules
%config %{_sysconfdir}/pcp.conf
%dir %{_localstatedir}/lib/pcp/config/derived
%config %{_localstatedir}/lib/pcp/config/derived/*

%files -n %{lib_pkg}
%defattr(-,root,root)
%{_libdir}/libpcp.so.%{libpcp_pmda_sover}
%{_libdir}/libpcp_pmda.so.%{libpcp_pmda_sover}
%if !0%{?suse_version}
%{_libdir}/libpcp_gui.so.%{libpcp_gui_sover}
%{_libdir}/libpcp_mmv.so.%{libpcp_mmv_sover}
%{_libdir}/libpcp_trace.so.%{libpcp_trace_sover}
%{_libdir}/libpcp_import.so.%{libpcp_import_sover}
%{_libdir}/libpcp_web.so.%{libpcp_web_sover}
%else

%files -n libpcp_gui%{libpcp_gui_sover}
%defattr(-,root,root)
%{_libdir}/libpcp_gui.so.%{libpcp_gui_sover}

%files -n libpcp_mmv%{libpcp_mmv_sover}
%defattr(-,root,root)
%{_libdir}/libpcp_mmv.so.%{libpcp_mmv_sover}

%files -n libpcp_trace%{libpcp_trace_sover}
%defattr(-,root,root)
%{_libdir}/libpcp_trace.so.%{libpcp_trace_sover}

%files -n libpcp_import%{libpcp_import_sover}
%defattr(-,root,root)
%{_libdir}/libpcp_import.so.%{libpcp_import_sover}

%files -n libpcp_web%{libpcp_web_sover}
%defattr(-,root,root)
%{_libdir}/libpcp_web.so.%{libpcp_web_sover}
%endif

%files -n %{lib_devel_pkg}
%defattr(-,root,root)
%{_libdir}/libpcp.so
%{_libdir}/libpcp_gui.so
%{_libdir}/libpcp_mmv.so
%{_libdir}/libpcp_pmda.so
%{_libdir}/libpcp_trace.so
%{_libdir}/libpcp_import.so
%{_libdir}/libpcp_web.so
%{_includedir}/pcp/*.h

%files devel -f devel.list
%{_datadir}/pcp/examples
%{_libdir}/pkgconfig/*.pc

# PMDAs that ship src and are not for production use
# straight out-of-the-box, for devel or QA use only.
%{_pmdasdir}/simple
%{_pmdasdir}/sample
%{_pmdasdir}/trivial
%{_pmdasdir}/txmon

%files testsuite
%defattr(-,pcpqa,pcpqa)
%{_testsdir}

%if !%{disable_microhttpd}
%files webapi
%defattr(-,root,root)
%{_initddir}/pmwebd
%if !%{disable_systemd}
%{_unitdir}/pmwebd.service
%{_sbindir}/rcpmwebd
%endif
%{_libexecdir}/pcp/bin/pmwebd
%attr(0775,pcp,pcp) %{_logsdir}/pmwebd
%dir %{_confdir}/pmwebd
%config(noreplace) %{_confdir}/pmwebd/pmwebd.options
# duplicate directories from pcp and pcp-webjs, but rpm copes with that.
%dir %{_datadir}/pcp
%endif

%files manager
%defattr(-,root,root)
%{_initddir}/pmmgr
%if !%{disable_systemd}
%{_unitdir}/pmmgr.service
%{_sbindir}/rcpmmgr
%endif
%{_libexecdir}/pcp/bin/pmmgr
%attr(0775,pcp,pcp) %{_logsdir}/pmmgr
%config(missingok,noreplace) %{_confdir}/pmmgr
%config(noreplace) %{_confdir}/pmmgr/pmmgr.options

%files import-sar2pcp
%defattr(-,root,root)
%{_bindir}/sar2pcp

%files import-iostat2pcp
%defattr(-,root,root)
%{_bindir}/iostat2pcp

%if !%{disable_sheet2pcp}
%files import-sheet2pcp
%defattr(-,root,root)
%{_bindir}/sheet2pcp
%endif

%files import-mrtg2pcp
%defattr(-,root,root)
%{_bindir}/mrtg2pcp

%files import-ganglia2pcp
%defattr(-,root,root)
%{_bindir}/ganglia2pcp

%files import-collectl2pcp
%defattr(-,root,root)
%{_bindir}/collectl2pcp

%if !%{disable_perfevent}
%files pmda-perfevent
%defattr(-,root,root)
%{_pmdasdir}/perfevent
%config(noreplace) %{_pmdasdir}/perfevent/perfevent.conf
%endif

%if !%{disable_infiniband}
%files pmda-infiniband
%defattr(-,root,root)
%{_pmdasdir}/ib
%{_pmdasdir}/infiniband
%endif

%files pmda-activemq
%{_pmdasdir}/activemq

%files pmda-bonding
%{_pmdasdir}/bonding

%files pmda-bind2
%{_pmdasdir}/bind2

%files pmda-dbping
%{_pmdasdir}/dbping

%files pmda-ds389log
%{_pmdasdir}/ds389log

%files pmda-ds389
%{_pmdasdir}/ds389

%files pmda-elasticsearch
%{_pmdasdir}/elasticsearch

%files pmda-gpfs
%{_pmdasdir}/gpfs

%files pmda-gpsd
%{_pmdasdir}/gpsd

%files pmda-docker
%{_pmdasdir}/docker

%if !%{disable_lio}
%files pmda-lio
%{_pmdasdir}/lio
%endif

%files pmda-prometheus
%{_pmdasdir}/prometheus

%files pmda-lustre
%{_pmdasdir}/lustre

%files pmda-lustrecomm
%{_pmdasdir}/lustrecomm

%files pmda-memcache
%{_pmdasdir}/memcache

%files pmda-mysql
%{_pmdasdir}/mysql

%files pmda-named
%{_pmdasdir}/named

%files pmda-netfilter
%{_pmdasdir}/netfilter

%files pmda-news
%{_pmdasdir}/news

%files pmda-nginx
%{_pmdasdir}/nginx

%files pmda-nfsclient
%{_pmdasdir}/nfsclient

%if !%{disable_nutcracker}
%files pmda-nutcracker
%{_pmdasdir}/nutcracker
%endif

%files pmda-oracle
%{_pmdasdir}/oracle

%files pmda-pdns
%{_pmdasdir}/pdns

%files pmda-postfix
%{_pmdasdir}/postfix

%if !%{disable_postgresql}
%files pmda-postgresql
%{_pmdasdir}/postgresql
%config(noreplace) %{_pmdasdir}/postgresql/pmdapostgresql.conf
%endif

%files pmda-redis
%{_pmdasdir}/redis

%files pmda-rsyslog
%{_pmdasdir}/rsyslog

%files pmda-samba 
%{_pmdasdir}/samba 

%if !%{disable_snmp}
%files pmda-snmp
%{_pmdasdir}/snmp
%endif

%files pmda-slurm
%{_pmdasdir}/slurm

%files pmda-vmware
%{_pmdasdir}/vmware

%files pmda-zimbra
%{_pmdasdir}/zimbra

%files pmda-dm
%{_pmdasdir}/dm

%if !%{disable_python2} || !%{disable_python3}
%files pmda-gluster
%{_pmdasdir}/gluster

%files pmda-zswap
%{_pmdasdir}/zswap

%files pmda-unbound
%{_pmdasdir}/unbound

%files pmda-mic
%{_pmdasdir}/mic

%files pmda-haproxy
%{_pmdasdir}/haproxy

%if !%{disable_libvirt}
%files pmda-libvirt
%{_pmdasdir}/libvirt
%endif

%files export-pcp2elasticsearch
%{_bindir}/pcp2elasticsearch

%files export-pcp2graphite
%{_bindir}/pcp2graphite

%files export-pcp2influxdb
%{_bindir}/pcp2influxdb

%files export-pcp2json
%{_bindir}/pcp2json

%files export-pcp2spark
%{_bindir}/pcp2spark

%if !%{disable_xlsx}
%files export-pcp2xlsx
%{_bindir}/pcp2xlsx
%endif

%files export-pcp2xml
%{_bindir}/pcp2xml

%files export-pcp2zabbix
%{_bindir}/pcp2zabbix

%files pmda-lmsensors
%{_pmdasdir}/lmsensors

%endif # !%{disable_python2} || !%{disable_python3}

%files export-zabbix-agent
%{_libdir}/zabbix
%{_sysconfdir}/zabbix

%if !%{disable_json}
%files pmda-json
%{_pmdasdir}/json
%endif

%files pmda-apache
%{_pmdasdir}/apache

%files pmda-bash
%{_pmdasdir}/bash

%files pmda-cifs
%{_pmdasdir}/cifs

%files pmda-cisco
%{_pmdasdir}/cisco

%files pmda-gfs2
%{_pmdasdir}/gfs2

%files pmda-logger
%{_pmdasdir}/logger

%files pmda-mailq
%{_pmdasdir}/mailq

%files pmda-mounts
%{_pmdasdir}/mounts

%files pmda-nvidia-gpu
%{_pmdasdir}/nvidia

%files pmda-roomtemp
%{_pmdasdir}/roomtemp

%if !%{disable_rpm}
%files pmda-rpm
%{_pmdasdir}/rpm
%endif

%files pmda-sendmail
%{_pmdasdir}/sendmail

%files pmda-shping
%{_pmdasdir}/shping

%files pmda-smart
%{_pmdasdir}/smart

%files pmda-summary
%{_pmdasdir}/summary

%if !%{disable_systemd}
%files pmda-systemd
%{_pmdasdir}/systemd
%endif

%files pmda-trace
%{_pmdasdir}/trace

%files pmda-weblog
%{_pmdasdir}/weblog

%files -n perl-PCP-PMDA -f perl-pcp-pmda.list
%defattr(-,root,root)
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP/PMDA
%endif

%files -n perl-PCP-MMV -f perl-pcp-mmv.list
%defattr(-,root,root)
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP/MMV
%endif

%files -n perl-PCP-LogImport -f perl-pcp-logimport.list
%defattr(-,root,root)
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP/LogImport
%endif

%files -n perl-PCP-LogSummary -f perl-pcp-logsummary.list
%defattr(-,root,root)
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/PCP
%endif

%if !%{disable_python2}
%files -n %{__python2}-pcp -f python-pcp.list.rpm
%defattr(-,root,root)
%if 0%{?suse_version}
%{python_sitearch}/*.so
%dir %{python_sitearch}/pcp
%{python_sitearch}/pcp
%endif
%endif

%if !%{disable_python3}
%files -n python3-pcp -f python3-pcp.list.rpm
%defattr(-,root,root)
%endif

%if !%{disable_qt}
%files gui -f pcp-gui.list
%defattr(-,root,root,-)
%{_pixmapdir}/pmchart.png
%{_confdir}/pmsnap
%config(noreplace) %{_confdir}/pmsnap/control
%{_localstatedir}/lib/pcp/config/pmsnap
%{_localstatedir}/lib/pcp/config/pmchart
%{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
%{_datadir}/applications/pmchart.desktop
%endif

%files doc -f pcp-doc.list
%defattr(-,root,root,-)
%if 0%{?suse_version}
%exclude %{_docdir}/pcp/CHANGELOG
%exclude %{_docdir}/pcp/COPYING
%exclude %{_docdir}/pcp/INSTALL.md
%exclude %{_docdir}/pcp/README.md
%exclude %{_docdir}/pcp/VERSION.pcp
%exclude %{_docdir}/pcp/pcp.lsm
%dir %{_docdir}/pcp/demos
%dir %{_docdir}/pcp/demos/tutorials
%dir %{_datadir}/doc/pcp-doc
%{_datadir}/doc/pcp-doc/html
%{_datadir}/doc/pcp-doc/pcp-programmers-guide.pdf
%{_datadir}/doc/pcp-doc/pcp-users-and-administrators-guide.pdf
%endif

%if !%{disable_python2} || !%{disable_python3}
%files system-tools -f pcp-system-tools.list
%dir %{_confdir}/dstat
%dir %{_confdir}/pmrep
%config(noreplace) %{_confdir}/dstat/*
%config(noreplace) %{_confdir}/pmrep/*
%endif

%changelog
