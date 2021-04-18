#
# spec file for package pcp
#
# Copyright (c) 2021 SUSE LLC
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
Version:        5.2.2
Release:        0
%global buildversion 1

URL:            https://pcp.io
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
# PATCH-FIX-UPSTREAM, ddiss@suse.de
Patch7:         0007-pmns-Make-drop-duplicate-if-else.patch
# PATCH-FIX-UPSTREAM, ddiss@suse.de
Patch8:         0008-fixes-for-GH-1140-PCP_TMPFILE_DIR-used-in-build.patch
# PATCH-FIX-UPSTREAM, ddiss@suse.de
Patch9:         0009-remove-rundir-install.patch

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

# libvarlink and pmdapodman
%if 0%{?fedora} >= 28 || 0%{?rhel} > 7
%global disable_podman 0
%else
%global disable_podman 1
%endif

# libchan, libhdr_histogram and pmdastatsd
%if 0%{?fedora} >= 29 || 0%{?rhel} > 8
%global disable_statsd 0
%else
%global disable_statsd 1
%endif

%global disable_sheet2pcp 1

%global disable_python3 0
# drop python2 packages
%global _with_python2 --with-python=no

%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
%global perl_interpreter perl-interpreter
%else
%global perl_interpreter perl
%endif

# support for pmdabcc
%if 0%{?fedora} >= 25 || 0%{?rhel} > 6
%ifarch s390 s390x armv7hl aarch64 i686
%global disable_bcc 1
%else
%global disable_bcc 0
%endif
%else
%global disable_bcc 1
%endif

# support for pmdabpftrace
%if 0%{?fedora} >= 30 || 0%{?rhel} > 8
%ifarch s390 s390x armv7hl aarch64 i686
%global disable_bpftrace 1
%else
%global disable_bpftrace 0
%endif
%else
%global disable_bpftrace 1
%endif

# support for pmdajson
%if 0%{?rhel} == 0 || 0%{?rhel} > 6
%if !%{disable_python3}
%global disable_json 0
%else
%global disable_json 1
%endif
%else
%global disable_json 1
%endif

# No mssql ODBC driver on non-x86 platforms
%ifarch x86_64
%if !%{disable_python3}
%global disable_mssql 0
%else
%global disable_mssql 1
%endif
%else
%global disable_mssql 1
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

# libuv async event library
%if 0%{?fedora} >= 28 || 0%{?rhel} > 7 || 0%{?suse_version}
%global disable_libuv 0
%else
%global disable_libuv 1
%endif

# libvirt pmda introduces a dependency loop: ffmpeg-4=>gstreamer-plugins-bad
# =>libquicktime=>libvirt=>pcp=>samba=>Wireshark
%global disable_libvirt 1

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

%if 0%{?suse_version} <= 1500 && !%{disable_python3}
%global disable_lio 1
%else
%global disable_lio 0
%endif

%if 0%{?suse_version}
# pcp-export-zabbix-agent installs under a zabbix owned directory
%global disable_zabbix_agent 1
%else
%global disable_zabbix_agent 0
%endif

# KVM PMDA moved into pcp (no longer using Perl, default on)
Obsoletes:      pcp-pmda-kvm < %{version}
Provides:       pcp-pmda-kvm = %{version}

# PCP REST APIs are now provided by pmproxy
Obsoletes:      pcp-webapi < 5.0.0
Obsoletes:      pcp-webapi-debuginfo < 5.0.0
Provides:       pcp-webapi = %{version}

# PCP discovery service now provided by pmfind
Obsoletes:      pcp-manager < 5.2.0
Obsoletes:      pcp-manager-debuginfo < 5.2.0

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
%if !%{disable_podman}
BuildRequires:  libvarlink-devel
%endif
%if !%{disable_statsd}
BuildRequires:  HdrHistogram_c-devel
BuildRequires:  chan-devel
BuildRequires:  ragel
%endif
%if !%{disable_perfevent}
BuildRequires:  libpfm-devel >= 4.4
%endif
%if !%{disable_sdt}
BuildRequires:  systemtap-sdt-devel
%endif
%if !%{disable_libuv}
BuildRequires:  libuv-devel >= 1.0
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
BuildRequires:  pkgconfig(libsystemd) 
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
%else
Requires:       initscripts
%endif

Requires:       %{lib_pkg} = %{version}-%{release}
Obsoletes:      pcp-pmda-nvidia < %{version}

%global _confdir	%{_sysconfdir}/pcp
%global _logsdir	%{_localstatedir}/log/pcp
%global _pmnsdir	%{_localstatedir}/lib/pcp/pmns
%global _pmnsexecdir	%{_libexecdir}/pcp/pmns
%global _tempsdir	%{_localstatedir}/lib/pcp/tmp
%global _pmdasdir	%{_localstatedir}/lib/pcp/pmdas
%global _pmdasexecdir	%{_libexecdir}/pcp/pmdas
%global _testsdir	%{_localstatedir}/lib/pcp/testsuite
%global _selinuxdir	%{_localstatedir}/lib/pcp/selinux
%global _selinuxexecdir	%{_libexecdir}/pcp/selinux
%global _logconfdir	%{_localstatedir}/lib/pcp/config/pmlogconf
%global _ieconfdir	%{_localstatedir}/lib/pcp/config/pmieconf
%global _tapsetdir	%{_datadir}/systemtap/tapset
%global _bashcompdir	%{_datadir}/bash-completion/completions
%if 0%{?suse_version}
%global _pixmapdir	%{_datadir}/pixmaps
%global _booksdir	%{_docdir}/pcp-doc
%else
%global _pixmapdir	%{_datadir}/pcp-gui/pixmaps
%global _booksdir	%{_datadir}/doc/pcp-doc
%endif
%global _hicolordir	%{_datadir}/icons/hicolor

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

%if !%{disable_infiniband}
%global _with_ib --with-infiniband=yes
%endif

%if %{disable_perfevent}
%global _with_perfevent --with-perfevent=no
%else
%global _with_perfevent --with-perfevent=yes
%endif

%if %{disable_podman}
%global _with_podman --with-podman=no
%else
%global _with_podman --with-podman=yes
%endif

%if %{disable_statsd}
%global _with_statsd --with-statsd=no
%else
%global _with_statsd --with-statsd=yes
%endif

%if %{disable_bcc}
%global _with_bcc --with-pmdabcc=no
%else
%global _with_bcc --with-pmdabcc=yes
%endif

%if %{disable_bpftrace}
%global _with_bpftrace --with-pmdabpftrace=no
%else
%global _with_bpftrace --with-pmdabpftrace=yes
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

%global pmda_remove() %{expand:
if [ %1 -eq 0 ]
then
    PCP_PMDAS_DIR=%{_pmdasdir}
    PCP_PMCDCONF_PATH=%{_confdir}/pmcd/pmcd.conf
    if [ -f "$PCP_PMCDCONF_PATH" -a -f "$PCP_PMDAS_DIR/%2/domain.h" ]
    then
        (cd "$PCP_PMDAS_DIR/%2/" && ./Remove >/dev/null 2>&1)
    fi
fi
}

%global install_file() %{expand:
if [ -w "%1" ]
then
    (cd "%1" && touch "%2" && chmod 644 "%2")
else
    echo "WARNING: Cannot write to %1, skipping %2 creation." >&2
fi
}

%global rebuild_pmns() %{expand:
if [ -w "%1" ]
then
    (cd "%1" && ./Rebuild -s && rm -f "%2")
else
    echo "WARNING: Cannot write to %1, skipping namespace rebuild." >&2
fi
}

%global selinux_handle_policy() %{expand:
if [ %1 -ge 1 ]
then
    %{_libexecdir}/pcp/bin/selinux-setup %{_selinuxdir} install %2
elif [ %1 -eq 0 ]
then
    %{_libexecdir}/pcp/bin/selinux-setup %{_selinuxdir} remove %2
fi
}

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
URL:            https://pcp.io
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
URL:            https://pcp.io
Conflicts:      %{lib_pkg_conflict}
Requires:       pcp-conf >= %{version}-%{release}

%description -n %{lib_pkg}
Performance Co-Pilot (PCP) run-time libraries

%if 0%{?suse_version}
%package -n libpcp_gui%{libpcp_gui_sover}
Summary:        Performance Co-Pilot run-time GUI library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
URL:            https://pcp.io

%description -n libpcp_gui%{libpcp_gui_sover}
Performance Co-Pilot (PCP) run-time graphical user interface library

%package -n libpcp_mmv%{libpcp_mmv_sover}
Summary:        Performance Co-Pilot run-time MMV library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
URL:            https://pcp.io

%description -n libpcp_mmv%{libpcp_mmv_sover}
Performance Co-Pilot (PCP) run-time Memory Mapped Values library

%package -n libpcp_trace%{libpcp_trace_sover}
Summary:        Performance Co-Pilot run-time tracing library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
URL:            https://pcp.io

%description -n libpcp_trace%{libpcp_trace_sover}
Performance Co-Pilot (PCP) run-time tracing library

%package -n libpcp_import%{libpcp_import_sover}
Summary:        Performance Co-Pilot run-time import library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
URL:            https://pcp.io

%description -n libpcp_import%{libpcp_import_sover}
Performance Co-Pilot (PCP) run-time import library

%package -n libpcp_web%{libpcp_web_sover}
Summary:        Performance Co-Pilot run-time web library
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
URL:            https://pcp.io

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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
# perl-PCP-PMDA. This is the PCP agent perl binding.
#
%package -n perl-PCP-PMDA
Summary:        Performance Co-Pilot (PCP) Perl bindings and documentation
License:        %{license_gplv2plus}
Group:          %{lib_devel_gr}
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description import-collectl2pcp
Performance Co-Pilot (PCP) front-end tools for importing collectl data
into standard PCP archive logs for replay with any PCP monitoring tool.

%if !%{disable_zabbix_agent}
#
# pcp-export-zabbix-agent
#
%package export-zabbix-agent
Summary:        Module for exporting from PCP into a Zabbix agent daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} >= %{version}-%{release}
%else
# this package nests files under %{_sysconfdir}/zabbix, which is provided by:
Requires:       zabbix-server
%endif

%description export-zabbix-agent
Performance Co-Pilot (PCP) module for exporting metrics from PCP to
Zabbix via the Zabbix agent - see zbxpcp(3) for further details.
%endif

%if !%{disable_python3}
#
# pcp-export-pcp2elasticsearch
#
%package export-pcp2elasticsearch
Summary:        Performance Co-Pilot tools for exporting PCP metrics to ElasticSearch
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-pcp = %{version}-%{release}
Requires:       python3-requests
BuildRequires:  python3-requests

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
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       python3-pcp = %{version}-%{release}

%description export-pcp2graphite
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to graphite (http://graphite.readthedocs.org).

# pcp-export-pcp2influxdb
#
%package export-pcp2influxdb
Summary:        Performance Co-Pilot tools for exporting PCP metrics to InfluxDB
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} >= %{version}-%{release}
%endif
Requires:       python3-pcp = %{version}-%{release}
Requires:       python3-requests
BuildRequires:  python3-requests

%description export-pcp2influxdb
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to InfluxDB (https://influxdata.com/time-series-platform/influxdb).

#
# pcp-export-pcp2json
#
%package export-pcp2json
URL:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics in JSON format
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-pcp = %{version}-%{release}

%description export-pcp2json
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in JSON format.

#
# pcp-export-pcp2spark
#
%package export-pcp2spark
URL:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics to Apache Spark
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-pcp = %{version}-%{release}

%description export-pcp2spark
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in JSON format to Apache Spark. See https://spark.apache.org/ for
further details on Apache Spark.

#
# pcp-export-pcp2xlsx
#
%if !%{disable_xlsx}
%package export-pcp2xlsx
URL:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics to Excel
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-openpyxl
Requires:       python3-pcp = %{version}-%{release}
BuildRequires:  python3-openpyxl

%description export-pcp2xlsx
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in Excel spreadsheet format.
%endif
#
# pcp-export-pcp2xml
#
%package export-pcp2xml
URL:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics in XML format
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-pcp = %{version}-%{release}

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
URL:            https://pcp.io
Requires:       python3-pcp = %{version}-%{release}

%description export-pcp2zabbix
Performance Co-Pilot (PCP) front-end tools for exporting metric values
to the Zabbix (https://www.zabbix.org/) monitoring software.
%endif

%if !%{disable_statsd}
#
# pcp-pmda-statsd
#
%package pmda-statsd
Summary:        Performance Co-Pilot (PCP) metrics from statsd
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       pcp = %{version}-%{release}
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       HdrHistogram_c
Requires:       chan

%description pmda-statsd
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting statistics from the statsd daemon.
%endif

%if !%{disable_perfevent}
#
# pcp-pmda-perfevent
#
%package pmda-perfevent
Summary:        Performance Co-Pilot (PCP) metrics for hardware counters
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       libpfm >= 4.4
%endif
BuildRequires:  libpfm-devel >= 4.4
Obsoletes:      pcp-pmda-papi < 5.0.0
Obsoletes:      pcp-pmda-papi-debuginfo < 5.0.0

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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io

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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-dm
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Device Mapper Cache and Thin Client.
# end pcp-pmda-dm
   

%if !%{disable_python3}
#
# pcp-pmda-gluster
#
%package pmda-gluster
Summary:        Performance Co-Pilot (PCP) metrics for the Gluster filesystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

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
URL:            https://pcp.io
Requires:       python3-pcp

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
URL:            https://pcp.io
Requires:       python3-pcp
Requires:       python3-psycopg2
BuildRequires:  python3-psycopg2

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
URL:            https://pcp.io
Requires:       python3-pcp

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
URL:            https://pcp.io
Requires:       python3-pcp

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
URL:            https://pcp.io
Requires:       python3-pcp

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
Requires:       python3-pcp

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
URL:            https://pcp.io
%if 0%{?suse_version}
Requires:       python3-libvirt-python
BuildRequires:  python3-libvirt-python
%else
Requires:       libvirt-python3
BuildRequires:  libvirt-python3
%endif
Requires:       python3-lxml
BuildRequires:  python3-lxml
Requires:       python3-pcp

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
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-elasticsearch
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Elasticsearch.
#end pcp-pmda-elasticsearch

#
# pcp-pmda-openvswitch
#
%package pmda-openvswitch
Summary:        Performance Co-Pilot (PCP) metrics for Open vSwitch
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-openvswitch
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from Open vSwitch.
#end pcp-pmda-openvswitch

#
# pcp-pmda-rabbitmq
#
%package pmda-rabbitmq
Summary:        Performance Co-Pilot (PCP) metrics for RabbitMQ queues
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-rabbitmq
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about RabbitMQ message queues.
#end pcp-pmda-rabbitmq

%if !%{disable_lio}
#
# pcp-pmda-lio
#
%package pmda-lio
Summary:        Performance Co-Pilot (PCP) metrics for the LIO subsystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp
%if 0%{?suse_version}
Requires:       python3-rtslib-fb
BuildRequires:  python3-rtslib-fb
%else
Requires:       python3-rtslib
BuildRequires:  python3-rtslib
%endif
%description pmda-lio
This package provides a PMDA to gather performance metrics from the kernels
iSCSI target interface (LIO). The metrics are stored by LIO within the Linux
kernels configfs filesystem. The PMDA provides per LUN level stats, and a
summary instance per iSCSI target, which aggregates all LUN metrics within the
target.
#end pcp-pmda-lio
%endif # !%{disable_lio}

#
# pcp-pmda-openmetrics
#
%package pmda-openmetrics
Summary:        Performance Co-Pilot (PCP) metrics from OpenMetrics endpoints
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp
Requires:       python3-requests
BuildRequires:  python3-requests
Obsoletes:      pcp-pmda-prometheus < 5.0.0
Provides:       pcp-pmda-prometheus = %{version}

%description pmda-openmetrics
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
extracting metrics from OpenMetrics (https://openmetrics.io/) endpoints.
#end pcp-pmda-openmetrics

#
# pcp-pmda-lmsensors
#
%package pmda-lmsensors
Summary:        Performance Co-Pilot (PCP) metrics for hardware sensors
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp
# rewritten in python, so there is no longer a debuginfo package
Obsoletes:      pcp-pmda-lmsensors-debuginfo

%description pmda-lmsensors
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Linux hardware monitoring sensors.
# end pcp-pmda-lmsensors

#
# pcp-pmda-netcheck
#
%package pmda-netcheck
Summary:        Performance Co-Pilot (PCP) metrics for simple network checks
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       python3-pcp

%description pmda-netcheck
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from simple network checks.
# end pcp-pmda-netcheck

%endif # !%{disable_python3}

%if !%{disable_mssql}
#
# pcp-pmda-mssql
#
%package pmda-mssql
Summary:        Performance Co-Pilot (PCP) metrics for Microsoft SQL Server
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif
Requires:       python3-pcp

%description pmda-mssql
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from Microsoft SQL Server.
# end pcp-pmda-mssql
%endif

%if !%{disable_json}
#
# pcp-pmda-json
#
%package pmda-json
Summary:        Performance Co-Pilot (PCP) metrics for JSON data
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp
Requires:       python3-six
BuildRequires:  python3-six
Requires:       python3-jsonpointer
BuildRequires:  python3-jsonpointer

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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
URL:            https://pcp.io
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

%if !%{disable_python3}
#
# python3-pcp. This is the PCP library bindings for python3.
#
%package -n python3-pcp
Summary:        Performance Co-Pilot (PCP) Python3 bindings and documentation
License:        %{license_gplv2plus}
Group:          %{lib_gr}
URL:            https://pcp.io
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

%if !%{disable_python3}
#
# pcp-system-tools
#
%package system-tools
Summary:        Performance Co-Pilot (PCP) System and Monitoring Tools
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp = %{version}-%{release}
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
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       liberation-sans-fonts
%else
Requires:       dejavu-fonts
%endif
BuildRequires:  hicolor-icon-theme

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
URL:            https://pcp.io
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
URL:            https://pcp.io
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
%patch7 -p1
%patch8 -p1
%patch9 -p1

autoconf

%build
%define _lto_cflags %{nil}
%if 0%{?suse_version}
# in case we're building without os-release (bsc#1123311)...
export PACKAGE_DISTRIBUTION="suse"
%endif
# tmpdir used during build https://github.com/performancecopilot/pcp/issues/1140
export PACKAGE_BUILD_DATE=`date -u -r CHANGELOG +%Y-%m-%d`
PCP_CFLAGS="%{optflags}" CFLAGS="%{optflags}" CCFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %configure \
   --with-tmpdir=%{_tempsdir} \
   --datarootdir=%{_datadir} \
   --docdir=%{_docdir} \
   --with-dstat-symlink=no \
   %{?_with_initd} \
   %{?_with_doc} \
   %{?_with_dstat} \
   %{?_with_ib} \
   %{?_with_podman} \
   %{?_with_statsd} \
   %{?_with_perfevent} \
   %{?_with_bcc} \
   %{?_with_bpftrace} \
   %{?_with_json} \
   %{?_with_snmp} \
   %{?_with_nutcracker} \
   %{?_with_python2}
PCP_CFLAGS="%{optflags}" CFLAGS="%{optflags}" CCFLAGS="%{optflags}" CXXFLAGS="%{optflags}" make default_pcp

###############################################################################

%install
BACKDIR=`pwd`
NO_CHOWN=true
DIST_ROOT="%{buildroot}"
DIST_TMPFILES=$BACKDIR/install.tmpfiles
export NO_CHOWN DIST_ROOT DIST_TMPFILES
make install_pcp

PCP_GUI='pmchart|pmconfirm|pmdumptext|pmmessage|pmquery|pmsnap|pmtime'

# Fix stuff we do/don't want to ship
rm -f %{buildroot}/%{_libdir}/*.a

%if %{disable_sheet2pcp}
# remove sheet2pcp until BZ 830923 and BZ 754678 are resolved.
rm -f %{buildroot}/%{_bindir}/sheet2pcp %{buildroot}/%{_mandir}/man1/sheet2pcp.1*
%endif

%if %{disable_libvirt}
rm -fr %{buildroot}/%{_pmdasdir}/libvirt
%endif

%if %{disable_postgresql}
rm -fr %{buildroot}/%{_pmdasdir}/postgresql
%endif

# remove {config,platform}sz.h as these are not multilib friendly.
rm -f %{buildroot}/%{_includedir}/pcp/configsz.h
rm -f %{buildroot}/%{_includedir}/pcp/platformsz.h

%if %{disable_infiniband}
# remove pmdainfiniband on platforms lacking IB devel packages.
rm -f %{buildroot}/%{_pmdasdir}/ib
rm -fr %{buildroot}/%{_pmdasdir}/infiniband
%endif

%if %{disable_mssql}
# remove pmdamssql on platforms lacking MSODBC driver packages.
rm -fr %{buildroot}/%{_pmdasdir}/mssql
rm -fr %{buildroot}/%{_pmdasexecdir}/mssql
rm -fr %{buildroot}/%{_confdir}/mssql
%endif

%if %{disable_zabbix_agent}
rm -fr %{buildroot}/%{_libdir}/zabbix
rm -fr %{buildroot}/%{_sysconfdir}/zabbix
%endif

%if %{disable_sdt}
rm -fr %{buildroot}/%{_tapsetdir}
%endif

%if %{disable_selinux}
rm -fr %{buildroot}/%{_selinuxdir}
%endif

%if %{disable_qt}
%if !0%{?suse_version}
rm -fr %{buildroot}/%{_pixmapdir}
%endif
rm -fr %{buildroot}/%{_hicolordir}
rm -fr %{buildroot}/%{_confdir}/pmsnap
rm -fr %{buildroot}/%{_localstatedir}/lib/pcp/config/pmsnap
rm -fr %{buildroot}/%{_localstatedir}/lib/pcp/config/pmchart
rm -f %{buildroot}/%{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
rm -f %{buildroot}/%{_datadir}/applications/pmchart.desktop
rm -f `find %{buildroot}/%{_mandir}/man1 | grep -E "$PCP_GUI"`
%else
rm -rf %{buildroot}/usr/share/doc/pcp-gui
%if 0%{?suse_version}
mkdir -p %{buildroot}/%{_pixmapdir}
mv %{buildroot}/%{_datadir}/pcp-gui/pixmaps/*.png %{buildroot}/%{_pixmapdir}
rm -rf %{buildroot}/%{_datadir}/pcp-gui/pixmaps
%suse_update_desktop_file -r -G 'Performance Copilot Chart' %{buildroot}/%{_datadir}/applications/pmchart.desktop System Monitor
%else
desktop-file-validate %{buildroot}/%{_datadir}/applications/pmchart.desktop
%endif
%endif

%if %{disable_xlsx}
rm -f %{buildroot}/%{_bashcompdir}/pcp2xlsx
%endif

%if %{disable_lio}
rm -fr %{buildroot}/%{_pmdasdir}/lio
%endif

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
# Fedora and RHEL default local only access for pmcd and pmlogger
sed -i -e '/^# .*_LOCAL=1/s/^# //' %{buildroot}/%{_sysconfdir}/sysconfig/{pmcd,pmlogger}
%endif

rm -f %{buildroot}/%{_localstatedir}/lib/pcp/testsuite/perfevent/perfevent_coverage # drop unreproducible file (boo#1040589)

%if 0%{?suse_version}
mkdir -p %{buildroot}/%{_tempsdir}

install -d -m 0755 %{buildroot}/%{_sbindir}
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmcd
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmie
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmlogger
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmproxy

# SUSE requires use of %fillup_and_insserv
mkdir -p %{buildroot}/%{_fillupdir}
for f in pmlogger pmproxy pmcd pmie_timers pmlogger_timers pmfind; do
	mv %{buildroot}/%{_sysconfdir}/sysconfig/${f} \
		%{buildroot}/%{_fillupdir}/sysconfig.${f}
done

%else
# default chkconfig off for Fedora and RHEL
for f in %{buildroot}/%{_initddir}/{pcp,pmcd,pmlogger,pmie,pmwebd,pmmgr,pmproxy}; do
	test -f "$f" || continue
	sed -i -e '/^# chkconfig/s/:.*$/: - 95 05/' -e '/^# Default-Start:/s/:.*$/:/' $f
done
%endif

# list of PMDAs in the base pcp package
for pmda in jbd2 kvm linux mmv pipe pmcd proc root xfs; do
    for alt in %{_pmdasdir} %{_pmdasexecdir} %{_confdir}; do
        [ -d %{buildroot}/$alt/$pmda ] && echo $alt/$pmda >>base_pmdas.list
    done
done

# list of conf directories in base pcp package
for conf in discover labels nssdb pmafm pmcd pmfind pmie pmieconf pmlogconf \
    proc pipe linux pmlogger pmlogrewrite pmproxy pmsearch pmseries; do
    for alt in %{_confdir} %{_localstatedir}/lib/pcp/config; do
        replace=""; [ "$alt" = "%{_confdir}" ] && replace="%config(noreplace)"
        [ -d %{buildroot}/$alt/$conf ] && echo "$replace $alt/$conf" >>base_conf.list
    done
done

# all base binary files except those split out into sub-packages
ls -1 %{buildroot}/%{_bindir} |\
  grep -E -v 'pmiostat|zabbix|zbxpcp|dstat|pmrep|pcp2csv' |\
  grep -E -v 'pcp2spark|pcp2graphite|pcp2influxdb|pcp2zabbix' |\
  grep -E -v 'pcp2elasticsearch|pcp2json|pcp2xlsx|pcp2xml' |\
  grep -E -v 'pmdbg|pmclient|pmerr|genpmda' |\
sed -e 's#^#'%{_bindir}'\/#' >base_bin.list

# all base pmns files
echo %{_pmnsdir} >>base_pmns.list
echo %{_pmnsexecdir} >>base_pmns.list

ls -1 %{buildroot}/%{_bashcompdir} |\
  grep -E -v 'pcp2spark|pcp2graphite|pcp2influxdb|pcp2zabbix' |\
  grep -E -v 'pcp2elasticsearch|pcp2json|pcp2xlsx|pcp2xml' |\
  grep -E -v 'pcp2csv|pmrep|pmdumptext' |\
sed -e 's#^#'%{_bashcompdir}'\/#' >base_bashcomp.list

# Separate the pcp-system-tools package files.
# pmiostat is a back-compat symlink to its pcp(1) sub-command variant
# so its also in pcp-system-tools.
%if !%{disable_python3}
ls -1 %{buildroot}/%{_bindir} |\
  grep -E -e 'pmiostat|pmrep|dstat|pcp2csv' |\
  sed -e 's#^#'%{_bindir}'\/#' >pcp-system-tools.list
ls -1 %{buildroot}/%{_libexecdir}/pcp/bin |\
  grep -E -e 'atop|dmcache|dstat|free|iostat|ipcs|lvmcache|mpstat' \
        -e 'numastat|pidstat|shping|tapestat|uptime|verify' |\
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >>pcp-system-tools.list
%endif
# Separate the pcp-selinux package files.
%if !%{disable_selinux}
ls -1 %{buildroot}/%{_selinuxdir} |\
  sed -e 's#^#'%{_selinuxdir}'\/#' > pcp-selinux.list
ls -1 %{buildroot}/%{_selinuxexecdir} |\
  sed -e 's#^#'%{_selinuxexecdir}'\/#' >> pcp-selinux.list
ls -1 %{buildroot}/%{_libexecdir}/pcp/bin |\
  grep -E 'selinux-setup' |\
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >> pcp-selinux.list
%endif

ls -1 %{buildroot}/%{_libexecdir}/pcp/bin |\
%if !%{disable_python3}
  grep -E -v 'atop|dmcache|dstat|free|iostat|ipcs|lvmcache|mpstat' |\
  grep -E -v 'numastat|shping|tapestat|uptime|verify|selinux-setup' |\
%endif
  grep -E -v 'pmlogger_daily_report' |\
  grep -E -v 'pmsnap' |\
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >base_exec.list
echo %{_libexecdir}/pcp/lib >>base_exec.list

ls -1 %{buildroot}/%{_booksdir} |\
  sed -e 's#^#'%{_booksdir}'\/#' > pcp-doc.list
ls -1 %{buildroot}/%{_mandir}/man1 |\
  sed -e 's#^#'%{_mandir}'\/man1\/#' >>pcp-doc.list
ls -1 %{buildroot}/%{_mandir}/man5 |\
  sed -e 's#^#'%{_mandir}'\/man5\/#' >>pcp-doc.list
%if 0%{?suse_version}
mv %{buildroot}/%{_datadir}/pcp/demos %{buildroot}/%{_docdir}/pcp
ls -1 %{buildroot}/%{_docdir}/pcp/demos/tutorials |\
  sed -e 's#^#'%{_docdir}/pcp/demos/tutorials'\/#' >>pcp-doc.list
%else
ls -1 %{buildroot}/%{_datadir}/pcp/demos/tutorials |\
  sed -e 's#^#'%{_datadir}/pcp/demos/tutorials'\/#' >>pcp-doc.list
%endif

%if !%{disable_qt}
ls -1 %{buildroot}/%{_pixmapdir} |\
  sed -e 's#^#'%{_pixmapdir}'\/#' > pcp-gui.list
ls -1 %{buildroot}/%{_hicolordir} |\
  sed -e 's#^#'%{_hicolordir}'\/#' >> pcp-gui.list
cat base_bin.list base_exec.list base_bashcomp.list |\
  grep -E "$PCP_GUI" >> pcp-gui.list
echo %{_confdir}/pmchart >>pcp-gui.list
echo %{_libexecdir}/pcp/bin/pmsnap >>pcp-gui.list
%endif

ls -1 %{buildroot}/%{_logconfdir}/ |\
    sed -e 's#^#'%{_logconfdir}'\/#' |\
    grep -E -v 'zeroconf' >pcp-logconf.list
ls -1 %{buildroot}/%{_ieconfdir}/ |\
    sed -e 's#^#'%{_ieconfdir}'\/#' |\
    grep -E -v 'zeroconf' >pcp-ieconf.list

# generate full base package file list
cat base_pmdas.list base_conf.list base_bin.list base_exec.list base_bashcomp.list \
    pcp-logconf.list pcp-ieconf.list base_pmns.list |\
  grep -E -v 'pmdaib|pmsnap|2pcp|pmdas/systemd|zeroconf' |\
  grep -E -v "$PCP_GUI|pixmaps|hicolor|pcp-doc|tutorials|selinux" |\
  grep -E -v %{_logsdir} > base.list
%if !%{disable_systemd}
mkdir -p %{buildroot}/%{_tmpfilesdir}
mv $DIST_TMPFILES %{buildroot}/%{_tmpfilesdir}/pcp.conf
echo %{_tmpfilesdir}/pcp.conf >> base.list
%endif

# all devel pcp package files except those split out into sub packages
ls -1 %{buildroot}/%{_mandir}/man3 |\
sed -e 's#^#'%{_mandir}'\/man3\/#' | grep -v '3pm' >>pcp-doc.list
%if 0%{?suse_version}
ls -1 %{buildroot}/%{_docdir}/pcp/demos |\
sed -e 's#^#'%{_docdir}'\/pcp\/demos\/#' | grep -E -v tutorials >> devel.list
%else
ls -1 %{buildroot}/%{_datadir}/pcp/demos |\
sed -e 's#^#'%{_datadir}'\/pcp\/demos\/#' | grep -E -v tutorials >> devel.list
%endif
ls -1 %{buildroot}/%{_bindir} |\
grep -E 'pmdbg|pmclient|pmerr|genpmda' |\
sed -e 's#^#'%{_bindir}'\/#' >>devel.list
for pmda in sample simple trivial txmon; do
    echo %{_libexecdir}/pcp/pmdas/$pmda >>devel.list
done
echo %{_confdir}/simple/simple.conf >>devel.list

%pre testsuite
test -d %{_testsdir} || mkdir -p -m 755 %{_testsdir}
getent group pcpqa >/dev/null || groupadd -r pcpqa
getent passwd pcpqa >/dev/null || \
  useradd -c "PCP Quality Assurance" -g pcpqa -d %{_testsdir} -M -r -s /bin/bash pcpqa 2>/dev/null
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
exit 0

%if !%{disable_rpm}
%preun pmda-rpm
%{pmda_remove "$1" "rpm"}
%endif

%if !%{disable_systemd}
%preun pmda-systemd
%{pmda_remove "$1" "systemd"}
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
%{selinux_handle_policy "$1" "pcpupstream"}

%triggerin selinux -- docker-selinux
%{selinux_handle_policy "$1" "pcpupstream-docker"}

%triggerin selinux -- container-selinux
%{selinux_handle_policy "$1" "pcpupstream-container"}
%endif

%post
PCP_PMNS_DIR=%{_pmnsdir}
PCP_LOG_DIR=%{_logsdir}
%{install_file "$PCP_PMNS_DIR" .NeedRebuild}
%{install_file "$PCP_LOG_DIR/pmlogger" .NeedRewrite}
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
    %systemd_postun_with_restart pmcd.service
    %systemd_post pmcd.service
    %systemd_postun_with_restart pmlogger.service
    %systemd_post pmlogger.service
    %systemd_postun_with_restart pmie.service
    %systemd_post pmie.service
    systemctl condrestart pmproxy.service >/dev/null 2>&1
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
%{rebuild_pmns "$PCP_PMNS_DIR" .NeedRebuild}

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
%{selinux_handle_policy "$1" "pcpupstream"}

%triggerun selinux -- docker-selinux
%{selinux_handle_policy "$1" "pcpupstream-docker"}

%triggerun selinux -- container-selinux
%{selinux_handle_policy "$1" "pcpupstream-container"}
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
%doc CHANGELOG INSTALL.md README.md VERSION.pcp pcp.lsm
%license COPYING
%if 0%{?suse_version}
%exclude %{_docdir}/pcp/demos
%exclude %{_testsdir}
%endif

%dir %{_confdir}
%dir %{_pmdasdir}
%dir %{_pmdasexecdir}
%dir %{_datadir}/pcp
%dir %{_libexecdir}/pcp
%dir %{_libexecdir}/pcp/bin
%dir %{_localstatedir}/lib/pcp
%dir %{_localstatedir}/lib/pcp/config
%if 0%{?suse_version}
# part of pcp-gui
%exclude %{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
%endif
%dir %attr(0775,pcp,pcp) %{_tempsdir}
%dir %attr(0775,pcp,pcp) %{_tempsdir}/bash
%dir %attr(0775,pcp,pcp) %{_tempsdir}/json
%dir %attr(0775,pcp,pcp) %{_tempsdir}/mmv
%dir %attr(0775,pcp,pcp) %{_tempsdir}/pmie
%dir %attr(0775,pcp,pcp) %{_tempsdir}/pmlogger
%dir %attr(0775,pcp,pcp) %{_tempsdir}/pmproxy
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
%attr(0775,pcp,pcp) %{_logsdir}/pmfind
%{_localstatedir}/lib/pcp/pmns
%if %{disable_systemd}
%{_initddir}/pcp
%{_initddir}/pmcd
%{_initddir}/pmlogger
%{_initddir}/pmie
%{_initddir}/pmproxy
%else
%{_unitdir}/pmcd.service
%{_unitdir}/pmproxy.service
%{_unitdir}/pmlogger.service
%{_unitdir}/pmfind.service
%{_unitdir}/pmie.service
%{_sbindir}/rcpmcd
%{_sbindir}/rcpmie
%{_sbindir}/rcpmlogger
%{_sbindir}/rcpmproxy
%endif
%if %{disable_systemd}
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmlogger
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmfind
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmie
%else
%{_unitdir}/pmlogger_check.service
%{_unitdir}/pmlogger_check.timer
%{_unitdir}/pmlogger_daily.service
%{_unitdir}/pmlogger_daily.timer
%{_unitdir}/pmlogger_daily-poll.service
%{_unitdir}/pmlogger_daily-poll.timer
%{_unitdir}/pmie_check.service
%{_unitdir}/pmie_check.timer
%{_unitdir}/pmie_daily.service
%{_unitdir}/pmie_daily.timer
%{_unitdir}/pmfind.timer
%endif
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.pmlogger
%{_fillupdir}/sysconfig.pmproxy
%{_fillupdir}/sysconfig.pmfind
%{_fillupdir}/sysconfig.pmcd
%{_fillupdir}/sysconfig.pmie_timers
%{_fillupdir}/sysconfig.pmlogger_timers
%else
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger
%config(noreplace) %{_sysconfdir}/sysconfig/pmproxy
%config(noreplace) %{_sysconfdir}/sysconfig/pmfind
%config(noreplace) %{_sysconfdir}/sysconfig/pmcd
%config(noreplace) %{_sysconfdir}/sysconfig/pmie_timers
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger_timers
%endif
%dir %{_sysconfdir}/sasl2
%config(noreplace) %{_sysconfdir}/sasl2/pmcd.conf
%config %{_sysconfdir}/pcp.env
%dir %{_confdir}/labels
%dir %{_confdir}/labels/optional
%config(noreplace) %{_confdir}/labels.conf
%dir %{_confdir}/pipe.conf.d
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
%if !%{disable_libuv}
%dir %{_confdir}/pmseries
%config(noreplace) %{_confdir}/pmseries/pmseries.conf
%endif

%{_localstatedir}/lib/pcp/config/pmafm
%dir %attr(0775,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmie
# exclude pmieconf for pmda-dm
%exclude %{_confdir}/pmieconf/dm
%exclude %{_ieconfdir}/dm
# exclude zeroconf
%exclude %{_ieconfdir}/zeroconf
%exclude %{_logconfdir}/zeroconf
%exclude %{_confdir}/pmlogconf/zeroconf
%exclude %{_confdir}/pmieconf/zeroconf
%dir %attr(0775,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmlogger
%{_localstatedir}/lib/pcp/config/pmlogger/*
%dir %{_logconfdir}
%{_localstatedir}/lib/pcp/config/pmlogrewrite
%dir %attr(0775,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmda

%{_datadir}/zsh/site-functions/_pcp
%if !%{disable_sdt}
%{_tapsetdir}/pmcd.stp
%endif

%files zeroconf
%{_libexecdir}/pcp/bin/pmlogger_daily_report
%if !%{disable_systemd}
# systemd services for pmlogger_daily_report to replace the cron script
%{_unitdir}/pmlogger_daily_report.service
%{_unitdir}/pmlogger_daily_report.timer
%{_unitdir}/pmlogger_daily_report-poll.service
%{_unitdir}/pmlogger_daily_report-poll.timer
%else
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmlogger-daily-report
%endif
%config(noreplace) %{_ieconfdir}/zeroconf
%config(noreplace) %{_logconfdir}/zeroconf
%config(noreplace) %{_confdir}/pmlogconf/zeroconf
%config(noreplace) %{_confdir}/pmieconf/zeroconf

#additional pmlogger config files

%files conf
%dir %{_includedir}/pcp
%{_includedir}/pcp/builddefs
%{_includedir}/pcp/buildrules
%config %{_sysconfdir}/pcp.conf
%dir %{_confdir}/derived
%config %{_confdir}/derived/*
%dir %{_localstatedir}/lib/pcp/config/derived
%config %{_localstatedir}/lib/pcp/config/derived/*

%files -n %{lib_pkg}
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
%{_libdir}/libpcp_gui.so.%{libpcp_gui_sover}

%files -n libpcp_mmv%{libpcp_mmv_sover}
%{_libdir}/libpcp_mmv.so.%{libpcp_mmv_sover}

%files -n libpcp_trace%{libpcp_trace_sover}
%{_libdir}/libpcp_trace.so.%{libpcp_trace_sover}

%files -n libpcp_import%{libpcp_import_sover}
%{_libdir}/libpcp_import.so.%{libpcp_import_sover}

%files -n libpcp_web%{libpcp_web_sover}
%{_libdir}/libpcp_web.so.%{libpcp_web_sover}
%endif

%files -n %{lib_devel_pkg}
%{_libdir}/libpcp.so
%{_libdir}/libpcp_gui.so
%{_libdir}/libpcp_mmv.so
%{_libdir}/libpcp_pmda.so
%{_libdir}/libpcp_trace.so
%{_libdir}/libpcp_import.so
%{_libdir}/libpcp_web.so
%{_libdir}/pkgconfig/libpcp.pc
%{_libdir}/pkgconfig/libpcp_pmda.pc
%{_libdir}/pkgconfig/libpcp_import.pc
%{_includedir}/pcp/*.h

%files devel -f devel.list
%{_datadir}/pcp/examples

# PMDAs that ship src and are not for production use
# straight out-of-the-box, for devel or QA use only.
%{_pmdasdir}/simple
%config(noreplace) %{_confdir}/simple
%{_pmdasdir}/sample
%{_pmdasdir}/trivial
%{_pmdasdir}/txmon

%files testsuite
%{_testsdir}

%files import-sar2pcp
%{_bindir}/sar2pcp

%files import-iostat2pcp
%{_bindir}/iostat2pcp

%if !%{disable_sheet2pcp}
%files import-sheet2pcp
%{_bindir}/sheet2pcp
%endif

%files import-mrtg2pcp
%{_bindir}/mrtg2pcp

%files import-ganglia2pcp
%{_bindir}/ganglia2pcp

%files import-collectl2pcp
%{_bindir}/collectl2pcp

%if !%{disable_podman}
%files pmda-podman
%{_pmdasdir}/podman
%{_pmdasexecdir}/podman
%endif

%if !%{disable_statsd}
%files pmda-statsd
%{_pmdasdir}/statsd
%{_pmdasexecdir}/statsd
%{_confdir}/statsd
%config(noreplace) %{_pmdasdir}/statsd/pmdastatsd.ini
%endif

%if !%{disable_perfevent}
%files pmda-perfevent
%{_pmdasdir}/perfevent
%{_pmdasexecdir}/perfevent
%{_confdir}/perfevent
%config(noreplace) %{_pmdasdir}/perfevent/perfevent.conf
%endif

%if !%{disable_infiniband}
%files pmda-infiniband
%{_pmdasdir}/infiniband
%{_pmdasexecdir}/infiniband
%endif

%files pmda-activemq
%{_pmdasdir}/activemq
%{_pmdasexecdir}/activemq

%files pmda-bonding
%{_pmdasdir}/bonding
%{_pmdasexecdir}/bonding

%files pmda-bind2
%{_pmdasdir}/bind2
%{_pmdasexecdir}/bind2
%{_confdir}/bind2

%files pmda-dbping
%{_pmdasdir}/dbping
%{_pmdasexecdir}/dbping

%files pmda-ds389log
%{_pmdasdir}/ds389log
%{_pmdasexecdir}/ds389log

%files pmda-ds389
%{_pmdasdir}/ds389
%{_pmdasexecdir}/ds389

%files pmda-elasticsearch
%{_pmdasdir}/elasticsearch
%{_pmdasexecdir}/elasticsearch
%{_confdir}/elasticsearch

%files pmda-openvswitch
%{_pmdasdir}/openvswitch
%{_pmdasexecdir}/openvswitch

%files pmda-rabbitmq
%{_pmdasdir}/rabbitmq
%{_pmdasexecdir}/rabbitmq
%{_confdir}/rabbitmq

%files pmda-gpfs
%{_pmdasdir}/gpfs
%{_pmdasexecdir}/gpfs

%files pmda-gpsd
%{_pmdasdir}/gpsd
%{_pmdasexecdir}/gpsd

%files pmda-docker
%{_pmdasdir}/docker
%{_pmdasexecdir}/docker

%if !%{disable_lio}
%files pmda-lio
%{_pmdasdir}/lio
%{_pmdasexecdir}/lio
%endif

%files pmda-openmetrics
%{_pmdasdir}/openmetrics
%{_pmdasexecdir}/openmetrics
%config(noreplace) %{_confdir}/openmetrics

%files pmda-lustre
%{_pmdasdir}/lustre
%{_pmdasexecdir}/lustre
%config(noreplace) %{_confdir}/lustre

%files pmda-lustrecomm
%{_pmdasdir}/lustrecomm
%{_pmdasexecdir}/lustrecomm

%files pmda-memcache
%{_pmdasdir}/memcache
%{_pmdasexecdir}/memcache

%files pmda-mysql
%{_pmdasdir}/mysql
%{_pmdasexecdir}/mysql

%files pmda-named
%{_pmdasdir}/named
%{_pmdasexecdir}/named

%files pmda-netfilter
%{_pmdasdir}/netfilter
%{_pmdasexecdir}/netfilter

%files pmda-news
%{_pmdasdir}/news
%{_pmdasexecdir}/news

%files pmda-nginx
%{_pmdasdir}/nginx
%{_pmdasexecdir}/nginx
%config(noreplace) %{_confdir}/nginx

%files pmda-nfsclient
%{_pmdasdir}/nfsclient
%{_pmdasexecdir}/nfsclient

%if !%{disable_nutcracker}
%files pmda-nutcracker
%{_pmdasdir}/nutcracker
%{_pmdasexecdir}/nutcracker
%config(noreplace) %{_confdir}/nutcracker
%endif

%files pmda-oracle
%{_pmdasdir}/oracle
%{_pmdasexecdir}/oracle
%config(noreplace) %{_confdir}/oracle

%files pmda-pdns
%{_pmdasdir}/pdns
%{_pmdasexecdir}/pdns

%files pmda-postfix
%{_pmdasdir}/postfix
%{_pmdasexecdir}/postfix

%if !%{disable_postgresql}
%files pmda-postgresql
%{_pmdasdir}/postgresql
%{_pmdasexecdir}/postgresql
%dir %{_confdir}/postgresql
%config(noreplace) %{_confdir}/postgresql/pmdapostgresql.conf
%endif

%files pmda-redis
%{_pmdasdir}/redis
%{_pmdasexecdir}/redis
%{_confdir}/redis

%files pmda-rsyslog
%{_pmdasdir}/rsyslog
%{_pmdasexecdir}/rsyslog

%files pmda-samba
%{_pmdasdir}/samba
%{_pmdasexecdir}/samba

%if !%{disable_snmp}
%files pmda-snmp
%{_pmdasdir}/snmp
%{_pmdasexecdir}/snmp
%{_confdir}/snmp
%endif

%files pmda-slurm
%{_pmdasdir}/slurm
%{_pmdasexecdir}/slurm

%files pmda-vmware
%{_pmdasdir}/vmware
%{_pmdasexecdir}/vmware

%files pmda-zimbra
%{_pmdasdir}/zimbra
%{_pmdasexecdir}/zimbra

%files pmda-dm
%{_pmdasdir}/dm
%{_pmdasexecdir}/dm
%{_ieconfdir}/dm
%dir %{_confdir}/pmieconf/dm
%config(noreplace) %{_confdir}/pmieconf/dm

%if !%{disable_bcc}
%files pmda-bcc
%{_pmdasdir}/bcc
%{_pmdasexecdir}/bcc
%endif

%if !%{disable_bpftrace}
%files pmda-bpftrace
%{_pmdasdir}/bpftrace
%{_pmdasexecdir}/bpftrace
%config(noreplace) %{_confdir}/bpftrace
%endif

%if !%{disable_python3}
%files pmda-gluster
%{_pmdasdir}/gluster
%{_pmdasexecdir}/gluster

%files pmda-zswap
%{_pmdasdir}/zswap
%{_pmdasexecdir}/zswap

%files pmda-unbound
%{_pmdasdir}/unbound
%{_pmdasexecdir}/unbound

%files pmda-mic
%{_pmdasdir}/mic
%{_pmdasexecdir}/mic

%files pmda-haproxy
%{_pmdasdir}/haproxy
%{_pmdasexecdir}/haproxy
%{_confdir}/haproxy

%if !%{disable_libvirt}
%files pmda-libvirt
%{_pmdasdir}/libvirt
%{_pmdasexecdir}/libvirt
%{_confdir}/libvirt
%endif

%files export-pcp2elasticsearch
%{_bindir}/pcp2elasticsearch
%{_bashcompdir}/pcp2elasticsearch

%files export-pcp2graphite
%{_bindir}/pcp2graphite
%{_bashcompdir}/pcp2graphite

%files export-pcp2influxdb
%{_bindir}/pcp2influxdb
%{_bashcompdir}/pcp2influxdb

%files export-pcp2json
%{_bindir}/pcp2json
%{_bashcompdir}/pcp2json

%files export-pcp2spark
%{_bindir}/pcp2spark
%{_bashcompdir}/pcp2spark

%if !%{disable_xlsx}
%files export-pcp2xlsx
%{_bindir}/pcp2xlsx
%{_bashcompdir}/pcp2xlsx
%endif

%files export-pcp2xml
%{_bindir}/pcp2xml
%{_bashcompdir}/pcp2xml

%files export-pcp2zabbix
%{_bindir}/pcp2zabbix
%{_bashcompdir}/pcp2zabbix

%files pmda-lmsensors
%{_pmdasdir}/lmsensors
%{_pmdasexecdir}/lmsensors

%files pmda-netcheck
%{_pmdasdir}/netcheck
%{_pmdasexecdir}/netcheck
%{_confdir}/netcheck

%endif # !%{disable_python3}

%if !%{disable_zabbix_agent}
%files export-zabbix-agent
%{_libdir}/zabbix
%dir %{_sysconfdir}/zabbix/zabbix_agentd.d
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.d/zbxpcp.conf
%endif

%if !%{disable_mssql}
%files pmda-mssql
%{_pmdasdir}/mssql
%{_pmdasexecdir}/mssql
%config(noreplace) %{_confdir}/mssql
%endif

%if !%{disable_json}
%files pmda-json
%{_pmdasdir}/json
%{_pmdasexecdir}/json
%config(noreplace) %{_confdir}/json
%endif

%files pmda-apache
%{_pmdasdir}/apache
%{_pmdasexecdir}/apache

%files pmda-bash
%{_pmdasdir}/bash
%{_pmdasexecdir}/bash

%files pmda-cifs
%{_pmdasdir}/cifs
%{_pmdasexecdir}/cifs

%files pmda-cisco
%{_pmdasdir}/cisco
%{_pmdasexecdir}/cisco

%files pmda-gfs2
%{_pmdasdir}/gfs2
%{_pmdasexecdir}/gfs2

%files pmda-logger
%{_pmdasdir}/logger
%{_pmdasexecdir}/logger

%files pmda-mailq
%{_pmdasdir}/mailq
%{_pmdasexecdir}/mailq

%files pmda-mounts
%{_pmdasdir}/mounts
%{_pmdasexecdir}/mounts
%config(noreplace) %{_confdir}/mounts

%files pmda-nvidia-gpu
%{_pmdasdir}/nvidia
%{_pmdasexecdir}/nvidia

%files pmda-roomtemp
%{_pmdasdir}/roomtemp
%{_pmdasexecdir}/roomtemp

%if !%{disable_rpm}
%files pmda-rpm
%{_pmdasdir}/rpm
%{_pmdasexecdir}/rpm
%endif

%files pmda-sendmail
%{_pmdasdir}/sendmail
%{_pmdasexecdir}/sendmail

%files pmda-shping
%{_pmdasdir}/shping
%{_pmdasexecdir}/shping
%config(noreplace) %{_confdir}/shping

%files pmda-smart
%{_pmdasdir}/smart
%{_pmdasexecdir}/smart

%files pmda-summary
%{_pmdasdir}/summary
%{_pmdasexecdir}/summary
%config(noreplace) %{_confdir}/summary

%if !%{disable_systemd}
%files pmda-systemd
%{_pmdasdir}/systemd
%{_pmdasexecdir}/systemd
%endif

%files pmda-trace
%{_pmdasdir}/trace
%{_pmdasexecdir}/trace

%files pmda-weblog
%{_pmdasdir}/weblog
%{_pmdasexecdir}/weblog

%files -n perl-PCP-PMDA -f perl-pcp-pmda.list
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP/PMDA
%endif

%files -n perl-PCP-MMV -f perl-pcp-mmv.list
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP/MMV
%endif

%files -n perl-PCP-LogImport -f perl-pcp-logimport.list
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP
%dir %{_prefix}/lib/perl5/vendor_perl/*/*-linux-thread-multi*/auto/PCP/LogImport
%endif

%files -n perl-PCP-LogSummary -f perl-pcp-logsummary.list
%if 0%{?suse_version}
%dir %{_prefix}/lib/perl5/vendor_perl/*/PCP
%endif

%if !%{disable_python3}
%files -n python3-pcp -f python3-pcp.list.rpm
%endif

%if !%{disable_qt}
%files gui -f pcp-gui.list
%{_pixmapdir}/pmchart.png
%{_confdir}/pmsnap
%config(noreplace) %{_confdir}/pmsnap/control
%{_localstatedir}/lib/pcp/config/pmsnap
%{_localstatedir}/lib/pcp/config/pmchart
%{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
%{_datadir}/applications/pmchart.desktop
%{_bashcompdir}/pmdumptext
%endif

%files doc -f pcp-doc.list
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

%if !%{disable_selinux}
%files selinux -f pcp-selinux.list
%dir %{_selinuxdir}
%dir %{_selinuxexecdir}
%endif

%if !%{disable_python3}
%files system-tools -f pcp-system-tools.list
%dir %{_confdir}/dstat
%dir %{_confdir}/pmrep
%config(noreplace) %{_confdir}/dstat/*
%config(noreplace) %{_confdir}/pmrep/*
%{_bashcompdir}/pmrep
%endif

%changelog
