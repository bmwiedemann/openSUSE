#
# spec file for package pcp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%ifarch %{ix86}
%define _binary_payload w1.gzdio
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
%global libpcp_fault_sover 3

Summary:        System-level performance monitoring and performance management
License:        %{license_gplv2plus} AND %{license_lgplv2plus} AND %{license_cc_by}
Group:          %{pcp_gr}
Name:           pcp
Version:        6.3.8
Release:        0
%global buildversion 1

URL:            https://pcp.io
Source0:        https://github.com/performancecopilot/pcp/archive/refs/tags/%{version}.tar.gz#/pcp-%{version}.tar.gz
%if 0%{?suse_version}
Source2:        pcp-rpmlintrc
%endif
# Removes packaged content from /var/lib/pcp in the buildroot and
# generates per-subpackage tmpfiles snippets that recreate the tree at
# boot via systemd-tmpfiles. Required for transactional-update /
# immutable-OS targets (boo#XXXXXXX).
Source50:       pcp-stash-relocate.sh

# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch1:         0001-Install-libraries-without-exec-permission.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch3:         0003-Remove-runlevel-4-from-init-scripts.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch5:         0005-SUSE-fy-pmsnap-control-path.patch
# PATCH-FIX-OPENSUSE, kkaempf@suse.de
Patch6:         0006-pmsnap-control-var-www-srv-www.patch
# PATCH-FIX-UPSTREAM, ddiss@suse.de
Patch7:         0001-selinux-add-permissions-allowing-proc_psi_t-access.patch
# PATCH-FIX-OPENSUSE, jsegitz@suse.de
Patch8:         0008-selinux-additional-labeling-rules.patch

%global disable_selinux 0
%if 0%{?suse_version} < 1600
%global disable_selinux 1
%endif

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

# Perl PMDA bindings need a Y2038-safe Perl (64-bit time_t)
%ifarch %{ix86}
%global disable_perl 1
%global disable_nutcracker 1
%global disable_snmp 1
%global disable_sheet2pcp 1
%global with_perl --with-perl=no
%else
%global disable_perl 0
%global disable_nutcracker 0
%global disable_snmp 0
%global disable_sheet2pcp 0
%global with_perl --with-perl=yes
%endif

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
%global disable_mssql 1
%else
%global disable_mssql 1
%endif
%else
%global disable_mssql 1
%endif

%ifarch x86_64
%global disable_resctrl 0
%else
%global disable_resctrl 1
%endif

# support for pmdarpm
%if 0%{?rhel} == 0 || 0%{?rhel} > 5
%global disable_rpm 0
%else
%global disable_rpm 1
%endif

# Qt development and runtime environment missing components before el6
%if 0%{?rhel} && 0%{?rhel} <= 5
%global disable_qt 1
%else
%if 0%{?suse_version} < 1500
%global disable_qt 1
%else
%global disable_qt 0
%endif
%endif

# We need qt5 for fedora and openSUSE / SLE factory
%if 0%{?fedora} != 0 || 0%{?suse_version} > 1320
%if 0%{suse_version} >= 1600
%global default_qt 6
%else
%global default_qt 5
%endif
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

# declare the user/group we create in the preinstall script
Provides:       user(pcp)
Provides:       group(pcp)

# KVM PMDA moved into pcp (no longer using Perl, default on)
Obsoletes:      pcp-pmda-kvm < %{version}
Provides:       pcp-pmda-kvm = %{version}

# PCP REST APIs are now provided by pmproxy
Obsoletes:      pcp-webapi < 5.0.0
Provides:       pcp-webapi = %{version}
Obsoletes:      pcp-webapi-debuginfo < 5.0.0
Provides:       pcp-webapi-debuginfo = %{version}

# PCP discovery service now provided by pmfind
Obsoletes:      pcp-manager < 5.2.0
Provides:       pcp-manager = %{version}
Obsoletes:      pcp-manager-debuginfo < 5.2.0
Provides:       pcp-manager-debuginfo = %{version}

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
BuildRequires:  man
BuildRequires:  openssl-devel >= 1.0.2p
BuildRequires:  perl-ExtUtils-MakeMaker
%if !%{disable_systemd}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif
%if !%{disable_qt}
BuildRequires:  desktop-file-utils
%if 0%{?default_qt} == 6
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-svg-devel
%else	# default_qt == 5
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
Requires:       (pcp-selinux = %{version}-%{release} if selinux-policy-targeted)
%endif

Requires:       bash
%if %{disable_systemd}
Requires:       cron
%endif
Requires:       /usr/bin/which
Requires:       fileutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       perl
Requires:       sed
%if 0%{?suse_version}
Requires:       /usr/bin/hostname
Requires:       cpp
Requires:       cyrus-sasl
%else
Requires:       initscripts
%endif

Requires:       %{lib_pkg} = %{version}-%{release}
Obsoletes:      pcp-pmda-nvidia < %{version}
Provides:       pcp-pmda-nvidia = %{version}

%global _confdir	%{_sysconfdir}/pcp
%global _logsdir	%{_localstatedir}/log/pcp
%global _pmnsdir	%{_localstatedir}/lib/pcp/pmns
%global _pmnsexecdir	%{_libexecdir}/pcp/pmns
%global _tempsdir	%{_localstatedir}/lib/pcp/tmp
%global _pmdasdir	%{_localstatedir}/lib/pcp/pmdas
%global _pmdasexecdir	%{_libexecdir}/pcp/pmdas
%global _testsdir	%{_localstatedir}/lib/pcp/testsuite
%global _selinuxdir     %{_datadir}/selinux/packages/targeted
%global _logconfdir	%{_localstatedir}/lib/pcp/config/pmlogconf
%global _ieconfdir	%{_localstatedir}/lib/pcp/config/pmieconf
# Stash directory under /usr for content that genuinely cannot remain
# under /var/lib/pcp on transactional-update targets (testsuite real
# files). PMDA symlinks do not need a stash — their targets in
# /usr/libexec/pcp are already snapshot-included.
#
# The stash lives under %{_libexecdir} (not %{_datadir}) because the
# testsuite ships ELF binaries (broken/dynamic test PMDAs and Qt unit
# tests). %{_datadir} (= /usr/share) is reserved by FHS for arch-
# independent content; rpmlint flags ELF files there as
# arch-dependent-file-in-usr-share with very high badness.
%global _stashdir	%{_libexecdir}/pcp/stash
%global _tapsetdir	%{_datadir}/systemtap/tapset
%global _bashcompdir	%{_datadir}/bash-completion/completions
%if 0%{?suse_version}
%global _pixmapdir	%{_datadir}/pixmaps
%global _booksdir	%{_docdir}/pcp-doc
%if 0%{?suse_version} >= 1500
%global _hicolordir	%{_datadir}/icons/hicolor
%endif
%else
%global _pixmapdir	%{_datadir}/pcp-gui/pixmaps
%global _booksdir	%{_datadir}/doc/pcp-doc
%global _hicolordir	%{_datadir}/icons/hicolor
%endif

%if 0%{?fedora} >= 20 || 0%{?rhel} >= 8 || 0%{?suse_version}
# FIXME: PCP defaults to using %%{_datadir}/doc/pcp-doc
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
# we never want Infiniband on versions earlier than SLE-15
%if 0%{?suse_version} != 0 && 0%{?suse_version} < 1500
%global disable_infiniband 1
%else
# we never want Infiniband on RHEL5 or earlier
%if 0%{?rhel} != 0 && 0%{?rhel} < 6
%global disable_infiniband 1
%else
%global disable_infiniband 0
%endif
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

%description
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management.

The PCP open source release provides a unifying abstraction for all of
the interesting performance data in a system, and allows client
applications to easily retrieve and process any subset of that data.

%package conf
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot run-time configuration
License:        %{license_lgplv21plus}
Group:          %{lib_gr}
URL:            https://pcp.io
# http://fedoraproject.org/wiki/Packaging:Conflicts "Splitting Packages"
Conflicts:      pcp-libs < 3.9

%description conf
Performance Co-Pilot (PCP) run-time configuration

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
Requires:       libpcp_gui%{libpcp_gui_sover} = %{version}
Requires:       libpcp_import%{libpcp_import_sover} = %{version}-%{release}
Requires:       libpcp_mmv%{libpcp_mmv_sover} = %{version}-%{release}
Requires:       libpcp_trace%{libpcp_trace_sover} = %{version}-%{release}
Requires:       libpcp_web%{libpcp_web_sover} = %{version}-%{release}
Conflicts:      %{lib_devel_pkg_conflict}
%if (0%{?suse_version} > 0)
Obsoletes:      pcp-devel < %{version}
Provides:       pcp-devel = %{version}
%endif

%description -n %{lib_devel_pkg}
Performance Co-Pilot (PCP) headers for development.

%package devel
Summary:        Performance Co-Pilot (PCP) development tools and documentation
License:        %{license_gplv2plus} AND %{license_lgplv21plus}
Group:          %{lib_devel_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_devel_pkg} = %{version}-%{release}
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       pcp = %{version}-%{release}
Requires:       pcp = %{version}-%{release}
%endif

%description devel
Performance Co-Pilot (PCP) documentation and tools for development.

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
Obsoletes:      pcp-gui-testsuite < %{version}
Provides:       pcp-gui-testsuite = %{version}
# declare the user/group we create in the preinstall script
Provides:       user(pcpqa)
Provides:       group(pcpqa)

%description testsuite
Quality assurance test suite for Performance Co-Pilot (PCP).

%if !%{disable_perl}
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
%endif

%if !%{disable_perl}
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
%endif

%if !%{disable_perl}
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
%endif

%if !%{disable_perl}
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
%endif

%if !%{disable_perl}
%package import-sar2pcp
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
%package import-iostat2pcp
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

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

%if !%{disable_perl}
%package import-mrtg2pcp
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
%package import-ganglia2pcp
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

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
# this package nests files under %%{_sysconfdir}/zabbix, which is provided by:
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
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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

%package export-pcp2graphite
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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

%package export-pcp2influxdb
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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

%package export-pcp2json
%if !%{disable_noarch}
BuildArch:      noarch
%endif
URL:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics in JSON format
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-pcp = %{version}-%{release}

%description export-pcp2json
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in JSON format.

%package export-pcp2spark
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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

%package export-pcp2xml
%if !%{disable_noarch}
BuildArch:      noarch
%endif
URL:            https://pcp.io
Summary:        Performance Co-Pilot tools for exporting PCP metrics in XML format
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
Requires:       %{lib_pkg} >= %{version}-%{release}
Requires:       python3-pcp = %{version}-%{release}

%description export-pcp2xml
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in XML format.

%package export-pcp2zabbix
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
Provides:       pcp-pmda-papi = %{version}
Obsoletes:      pcp-pmda-papi-debuginfo < 5.0.0
Provides:       pcp-pmda-papi-debuginfo = %{version}

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

%if !%{disable_perl}
%package pmda-activemq
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for ActiveMQ
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(LWP::UserAgent)

%description pmda-activemq
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the ActiveMQ message broker.
%endif

%if !%{disable_perl}
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
%endif

%if !%{disable_perl}
%package pmda-redis
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Redis
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-redis
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from Redis servers (redis.io).
%endif

%if !%{disable_nutcracker}
#
# pcp-pmda-nutcracker
#
%package pmda-nutcracker
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for NutCracker (TwemCache)
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Requires:       perl(JSON)
Requires:       perl(YAML::XS)

%description pmda-nutcracker
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from NutCracker (TwemCache).
%endif

%if !%{disable_perl}
%package pmda-bonding
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Bonded network interfaces
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-bonding
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about bonded network interfaces.
%endif

%if !%{disable_perl}
%package pmda-dbping
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Database responsiveness
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-dbping
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Database response times and Availablility.
%endif

%if !%{disable_perl}
%package pmda-ds389
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
%package pmda-ds389log
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for 389 Directory Server Loggers
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-Date-Manip
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-ds389log
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from a 389 Directory Server log.
%endif

%if !%{disable_perl}
%package pmda-gpfs
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for GPFS Filesystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-gpfs
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the GPFS filesystem.
%endif

%if !%{disable_perl}
%package pmda-gpsd
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for a GPS Daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-gpsd
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about a GPS Daemon.
%endif

%package pmda-docker
Summary:        Performance Co-Pilot (PCP) metrics from the Docker daemon
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io

%description pmda-docker
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics using the Docker daemon REST API.

%if !%{disable_perl}
%package pmda-lustre
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for the Lustre Filesytem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-lustre
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Lustre Filesystem.
%endif

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

%if !%{disable_perl}
%package pmda-memcache
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Memcached
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-memcache
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Memcached.
%endif

%if !%{disable_perl}
%package pmda-mysql
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
%package pmda-named
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Named
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-named
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Named nameserver.
%endif

%if !%{disable_perl}
%package pmda-netfilter
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Netfilter framework
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-netfilter
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Netfilter packet filtering framework.
%endif

%if !%{disable_perl}
%package pmda-news
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Usenet News
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-news
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Usenet News.
%endif

%if !%{disable_perl}
%package pmda-nginx
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
%package pmda-oracle
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
%package pmda-pdns
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for PowerDNS
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-pdns
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the PowerDNS.
%endif

%if !%{disable_perl}
%package pmda-postfix
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%if 0%{?suse_version} >= 1500
Supplements:    (pcp and postfix)
%else
Supplements:    pcp
Supplements:    postfix
%endif

%description pmda-postfix
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Postfix (MTA).
%endif

%if !%{disable_perl}
%package pmda-rsyslog
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Rsyslog
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
%if 0%{?suse_version} >= 1500
Supplements:    (pcp and rsyslog)
%else
Supplements:    pcp
Supplements:    rsyslog
%endif

%description pmda-rsyslog
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Rsyslog.
%endif

%if !%{disable_perl}
%package pmda-samba
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Samba
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}
Supplements:    pcp

%description pmda-samba
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Samba.
%endif

%if !%{disable_perl}
%package pmda-slurm
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for NFS Clients
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       perl-PCP-PMDA = %{version}-%{release}

%description pmda-slurm
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from the SLURM Workload Manager.
%endif

%if !%{disable_snmp}
#
# pcp-pmda-snmp
#
%package pmda-snmp
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_perl}
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
%endif

%if !%{disable_perl}
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
%endif

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

%if !%{disable_python3}
#
# pcp-pmda-gluster
#
%package pmda-gluster
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for the Gluster filesystem
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-gluster
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the gluster filesystem.

%package pmda-nfsclient
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for NFS Clients
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-nfsclient
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics for NFS Clients.

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
%endif

%package pmda-zswap
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for compressed swap
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-zswap
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about compressed swap.

%package pmda-unbound
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for the Unbound DNS Resolver
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-unbound
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Unbound DNS Resolver.

%package pmda-mic
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Intel MIC cards
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-mic
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Intel MIC cards.

%package pmda-haproxy
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for HAProxy
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-haproxy
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
extracting performance metrics from HAProxy over the HAProxy stats socket.

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
%endif

%package pmda-elasticsearch
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Elasticsearch
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-elasticsearch
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about Elasticsearch.

%package pmda-openvswitch
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for Open vSwitch
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-openvswitch
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics from Open vSwitch.

%package pmda-rabbitmq
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for RabbitMQ queues
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp

%description pmda-rabbitmq
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about RabbitMQ message queues.

%if !%{disable_lio}
#
# pcp-pmda-lio
#
%package pmda-lio
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif # !%%{disable_lio}

%package pmda-openmetrics
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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

%package pmda-lmsensors
%if !%{disable_noarch}
BuildArch:      noarch
%endif
Summary:        Performance Co-Pilot (PCP) metrics for hardware sensors
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       python3-pcp
# rewritten in python, so there is no longer a debuginfo package
Obsoletes:      pcp-pmda-lmsensors-debuginfo < %{version}
Provides:       pcp-pmda-lmsensors-debuginfo = %{version}

%description pmda-lmsensors
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about the Linux hardware monitoring sensors.

%package pmda-netcheck
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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

%endif # !%%{disable_python3}

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
%endif

%if !%{disable_resctrl}
#
# pcp-pmda-resctrl
#
%package pmda-resctrl
Summary:        Performance Co-Pilot (PCP) metrics for the /sys/fs/resctrl interface
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-resctrl
This package contains the PCP Performance Metrics Domain Agent (PMDA)
which exposes performance metrics values from the /sys/fs/resctrl
interface to provide information on the last level cache.
%endif

%package pmda-uwsgi
Summary:        Performance Co-Pilot (PCP) metrics uWSGI servers
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
%if !0%{?suse_version}
Requires:       %{lib_pkg} = %{version}-%{release}
%endif

%description pmda-uwsgi
This package contains the PCP Performance Metrics Domain Agent (PMDA)
for collecting metrics from uWSGI servers.

%if !%{disable_json}
#
# pcp-pmda-json
#
%package pmda-json
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif # !%%{disable_json}

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

%package pmda-sockets
License:        %{license_gplv2plus}
Summary:        Performance Co-Pilot (PCP) per-socket metrics
URL:            https://pcp.io
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       iproute
Requires:       pcp = %{version}-%{release}

%description pmda-sockets
This package contains the PCP Performance Metric Domain Agent (PMDA) for
collecting per-socket statistics, making use of utilities such as 'ss'.

%package pmda-hacluster
License:        %{license_gplv2plus}
Summary:        Performance Co-Pilot (PCP) metrics for High Availability Clusters
URL:            https://pcp.io
Requires:       %{lib_pkg} = %{version}-%{release}
Requires:       pcp = %{version}-%{release}

%description pmda-hacluster
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
collecting metrics about linux High Availability (HA) Clusters.

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
%endif

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
 end C pmdas

%package pmda-amdgpu
Summary:        Performance Co-Pilot (PCP) metrics from AMD GPU devices
License:        %{license_gplv2plus}
Group:          %{pcp_gr}
URL:            https://pcp.io
Requires:       pcp = %{version}-%{release}
BuildRequires:  libdrm-devel

%description pmda-amdgpu
This package contains the PCP Performance Metrics Domain Agent (PMDA) for
extracting performance metrics from AMDGPU devices.

%package zeroconf
%if !%{disable_noarch}
BuildArch:      noarch
%endif
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
%endif

%if !%{disable_qt}

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

%if !%{disable_selinux}
%package selinux
Summary:        Selinux policy package
License:        %{license_gplv2plus} AND %{license_cc_by}
Group:          Applications/System
URL:            https://pcp.io
BuildRequires:  selinux-policy-devel
%{?selinux_requires}
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
%autosetup -p1

%build
autoconf
%define _lto_cflags %{nil}
%if 0%{?suse_version}
# in case we're building without os-release (bsc#1123311)...
export PACKAGE_DISTRIBUTION="suse"
%endif
# tmpdir used during build https://github.com/performancecopilot/pcp/issues/1140
export PACKAGE_BUILD_DATE=`date -u -r CHANGELOG +%Y-%m-%d`
PCP_CFLAGS="%{optflags}" CFLAGS="%{optflags} -std=c99" CCFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %configure \
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
%make_jobs default_pcp

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

# Make all shared libraries executable
find %{buildroot}/%{_libdir} -name "*.so*" -exec chmod a+x {} \;

# Fix all #!/usr/bin/env shebangs
find %{buildroot}/%{_bindir} -type f -exec sed -i -E 's@#!/usr/bin/env ([a-zA-Z0-9]+)@#!/usr/bin/\1@g' {} \;
find %{buildroot}/%{_usr}/lib -type f -exec sed -i -E 's@#!/usr/bin/env ([a-zA-Z0-9]+)@#!/usr/bin/\1@g' {} \;
find %{buildroot}/%{_libdir} -type f -exec sed -i -E 's@#!/usr/bin/env ([a-zA-Z0-9]+)@#!/usr/bin/\1@g' {} \;
find %{buildroot}/%{_datadir} -type f -exec sed -i -E 's@#!/usr/bin/env ([a-zA-Z0-9]+)@#!/usr/bin/\1@g' {} \;
find %{buildroot}/%{_libexecdir}/pcp -type f -exec sed -i -E 's@#!/usr/bin/env ([a-zA-Z0-9]+)@#!/usr/bin/\1@g' {} \;

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
%fdupes %{buildroot}%{_testsdir}

%if 0%{?suse_version}
mkdir -p %{buildroot}/%{_tempsdir}

install -d -m 0755 %{buildroot}/%{_sbindir}
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmcd
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmie
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmlogger
ln -sf /sbin/service %{buildroot}/%{_sbindir}/rcpmproxy

# SUSE requires use of %%fillup_and_insserv
mkdir -p %{buildroot}/%{_fillupdir}
for f in pmlogger pmproxy pmcd pmie_timers pmlogger_timers pmlogger_farm pmfind; do
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
for pmda in jbd2 kvm linux mmv pipe pmcd proc root xfs zfs; do
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
ls -1 %{buildroot}/%{_libexecdir}/pcp/bin |\
  grep -E 'selinux-setup' |\
  sed -e 's#^#'%{_libexecdir}/pcp/bin'\/#' >> pcp-selinux.list
%endif

ls -1 %{buildroot}/%{_libexecdir}/pcp/bin |\
%if !%{disable_python3}
  grep -E -v 'atop|dmcache|dstat|free|iostat|ipcs|lvmcache|mpstat' |\
  grep -E -v 'numastat|shping|tapestat|uptime|verify|selinux-setup' |\
%endif
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

# pcp-gui ships symlinks under /var/lib/pcp/config/{pmsnap,pmchart}
# pointing into /etc/pcp/{pmsnap,pmchart}, plus a single
# /var/lib/pcp/config/pmafm/pcp-gui symlink. Enumerate those so the
# relocation step ghosts them and emits L+ tmpfiles entries.
for d in pmsnap pmchart; do
    ( cd %{buildroot}%{_localstatedir}/lib/pcp/config/$d && \
      find . -mindepth 1 -printf "/var/lib/pcp/config/$d/%%P\n" ) \
      >> pcp-gui.list
    echo "%%dir /var/lib/pcp/config/$d" >> pcp-gui.list
done
echo '/var/lib/pcp/config/pmafm/pcp-gui' >> pcp-gui.list
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

# Base pcp ships a number of paths under /var/lib/pcp and /var/log/pcp:
#  - 4 built-in PMDA trees (denki, farm, overhead, podman) consisting of
#    symlinks into %{_libexecdir}/pcp/pmdas/<name>
#  - 2 pmlogredact symlinks into /etc/pcp/pmlogredact/
#  - assorted runtime-state and log directories.
# Enumerate them all into base.list so the relocation step ghosts the
# legacy paths and emits a single tmpfiles snippet (pcp-base-stash.conf)
# that recreates the tree at boot.
for pmda in denki farm overhead podman; do
    ( cd %{buildroot}%{_pmdasdir}/$pmda && \
      find . -mindepth 1 -printf "/var/lib/pcp/pmdas/$pmda/%%P\n" ) \
      >> base.list
    echo "%%dir /var/lib/pcp/pmdas/$pmda" >> base.list
done
( cd %{buildroot}%{_localstatedir}/lib/pcp/config/pmlogredact && \
  find . -mindepth 1 -printf '/var/lib/pcp/config/pmlogredact/%%P\n' ) \
  >> base.list
echo '%%dir /var/lib/pcp/config/pmlogredact' >> base.list

# Top-level container directories owned by base pcp.
echo '%%dir /var/lib/pcp'                          >> base.list
echo '%%dir /var/lib/pcp/config'                   >> base.list
echo '%%dir /var/lib/pcp/pmdas'                    >> base.list

# Runtime-state directories (mode 0775 pcp:pcp via PERM_OVERRIDES).
echo '%%dir /var/lib/pcp/tmp'                      >> base.list
for d in bash json mmv pmie pmlogger pmproxy; do
    echo "%%dir /var/lib/pcp/tmp/$d" >> base.list
done

# pmda runtime-state directory (also 0775 pcp:pcp).
echo '%%dir /var/lib/pcp/config/pmda'              >> base.list

# Log directories.
echo '%%dir /var/log/pcp'                          >> base.list
for d in pmcd pmlogger pmie pmproxy pmfind; do
    echo "%%dir /var/log/pcp/$d" >> base.list
done

# all devel pcp package files except those split out into sub packages
ls -1 %{buildroot}/%{_mandir}/man3 |\
sed -e 's#^#'%{_mandir}'\/man3\/#' | grep -v '3pm' >>pcp-doc.list

# populate devel.list
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

# pcp-devel ships sample/simple/trivial/txmon PMDAs whose
# /var/lib/pcp/pmdas/<name> trees consist of symlinks into
# %{_libexecdir}/pcp/pmdas/<name>. Enumerate those trees so the
# relocation step below ghosts the legacy paths and emits L+ tmpfiles
# entries pointing at the original /usr/libexec/... targets.
for pmda in sample simple trivial txmon; do
    ( cd %{buildroot}%{_pmdasdir}/$pmda && \
      find . -mindepth 1 -printf "/var/lib/pcp/pmdas/$pmda/%%P\n" ) \
      >> devel.list
    echo "%%dir /var/lib/pcp/pmdas/$pmda" >> devel.list
done

# Generate a .list file for pmda-activemq so the relocation step below
# picks up its /var/lib/pcp/pmdas/activemq tree (which on disk consists
# entirely of symlinks pointing into %{_pmdasexecdir}/activemq). The
# %files block for pmda-activemq below reads the rewritten list back
# via -f. (%%P and %%dir doubled so RPM passes them to the shell.)
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/activemq && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/activemq/%%P\n' ) \
  >> pmda-activemq.list
echo '%%dir /var/lib/pcp/pmdas/activemq' >> pmda-activemq.list
%endif

# Batch A: generate per-PMDA .list files so the stash relocation
# below picks up each PMDA tree under /var/lib/pcp/pmdas/<name>/
# (which on disk consists entirely of symlinks pointing into
# %{_pmdasexecdir}/<name>). The corresponding %files blocks read
# these rewritten lists back via -f. (%%P and %%dir are doubled
# so RPM passes them through to the shell unchanged.)
( cd %{buildroot}%{_pmdasdir}/amdgpu && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/amdgpu/%%P\n' ) \
  >> pmda-amdgpu.list
echo '%%dir /var/lib/pcp/pmdas/amdgpu' >> pmda-amdgpu.list
( cd %{buildroot}%{_pmdasdir}/apache && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/apache/%%P\n' ) \
  >> pmda-apache.list
echo '%%dir /var/lib/pcp/pmdas/apache' >> pmda-apache.list
( cd %{buildroot}%{_pmdasdir}/bash && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/bash/%%P\n' ) \
  >> pmda-bash.list
echo '%%dir /var/lib/pcp/pmdas/bash' >> pmda-bash.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/bonding && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/bonding/%%P\n' ) \
  >> pmda-bonding.list
echo '%%dir /var/lib/pcp/pmdas/bonding' >> pmda-bonding.list
%endif
( cd %{buildroot}%{_pmdasdir}/cifs && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/cifs/%%P\n' ) \
  >> pmda-cifs.list
echo '%%dir /var/lib/pcp/pmdas/cifs' >> pmda-cifs.list
( cd %{buildroot}%{_pmdasdir}/cisco && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/cisco/%%P\n' ) \
  >> pmda-cisco.list
echo '%%dir /var/lib/pcp/pmdas/cisco' >> pmda-cisco.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/dbping && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/dbping/%%P\n' ) \
  >> pmda-dbping.list
echo '%%dir /var/lib/pcp/pmdas/dbping' >> pmda-dbping.list
%endif
( cd %{buildroot}%{_pmdasdir}/docker && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/docker/%%P\n' ) \
  >> pmda-docker.list
echo '%%dir /var/lib/pcp/pmdas/docker' >> pmda-docker.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/ds389 && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/ds389/%%P\n' ) \
  >> pmda-ds389.list
echo '%%dir /var/lib/pcp/pmdas/ds389' >> pmda-ds389.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/ds389log && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/ds389log/%%P\n' ) \
  >> pmda-ds389log.list
echo '%%dir /var/lib/pcp/pmdas/ds389log' >> pmda-ds389log.list
%endif
( cd %{buildroot}%{_pmdasdir}/gfs2 && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/gfs2/%%P\n' ) \
  >> pmda-gfs2.list
echo '%%dir /var/lib/pcp/pmdas/gfs2' >> pmda-gfs2.list
%if !%{disable_python3}
( cd %{buildroot}%{_pmdasdir}/gluster && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/gluster/%%P\n' ) \
  >> pmda-gluster.list
echo '%%dir /var/lib/pcp/pmdas/gluster' >> pmda-gluster.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/gpfs && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/gpfs/%%P\n' ) \
  >> pmda-gpfs.list
echo '%%dir /var/lib/pcp/pmdas/gpfs' >> pmda-gpfs.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/gpsd && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/gpsd/%%P\n' ) \
  >> pmda-gpsd.list
echo '%%dir /var/lib/pcp/pmdas/gpsd' >> pmda-gpsd.list
%endif
( cd %{buildroot}%{_pmdasdir}/hacluster && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/hacluster/%%P\n' ) \
  >> pmda-hacluster.list
echo '%%dir /var/lib/pcp/pmdas/hacluster' >> pmda-hacluster.list
%if !%{disable_infiniband}
( cd %{buildroot}%{_pmdasdir}/infiniband && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/infiniband/%%P\n' ) \
  >> pmda-infiniband.list
echo '%%dir /var/lib/pcp/pmdas/infiniband' >> pmda-infiniband.list
%endif
%if !%{disable_lio}
( cd %{buildroot}%{_pmdasdir}/lio && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/lio/%%P\n' ) \
  >> pmda-lio.list
echo '%%dir /var/lib/pcp/pmdas/lio' >> pmda-lio.list
%endif
( cd %{buildroot}%{_pmdasdir}/lmsensors && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/lmsensors/%%P\n' ) \
  >> pmda-lmsensors.list
echo '%%dir /var/lib/pcp/pmdas/lmsensors' >> pmda-lmsensors.list
( cd %{buildroot}%{_pmdasdir}/logger && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/logger/%%P\n' ) \
  >> pmda-logger.list
echo '%%dir /var/lib/pcp/pmdas/logger' >> pmda-logger.list
( cd %{buildroot}%{_pmdasdir}/lustrecomm && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/lustrecomm/%%P\n' ) \
  >> pmda-lustrecomm.list
echo '%%dir /var/lib/pcp/pmdas/lustrecomm' >> pmda-lustrecomm.list
( cd %{buildroot}%{_pmdasdir}/mailq && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/mailq/%%P\n' ) \
  >> pmda-mailq.list
echo '%%dir /var/lib/pcp/pmdas/mailq' >> pmda-mailq.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/memcache && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/memcache/%%P\n' ) \
  >> pmda-memcache.list
echo '%%dir /var/lib/pcp/pmdas/memcache' >> pmda-memcache.list
%endif
( cd %{buildroot}%{_pmdasdir}/mic && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/mic/%%P\n' ) \
  >> pmda-mic.list
echo '%%dir /var/lib/pcp/pmdas/mic' >> pmda-mic.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/mysql && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/mysql/%%P\n' ) \
  >> pmda-mysql.list
echo '%%dir /var/lib/pcp/pmdas/mysql' >> pmda-mysql.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/named && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/named/%%P\n' ) \
  >> pmda-named.list
echo '%%dir /var/lib/pcp/pmdas/named' >> pmda-named.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/netfilter && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/netfilter/%%P\n' ) \
  >> pmda-netfilter.list
echo '%%dir /var/lib/pcp/pmdas/netfilter' >> pmda-netfilter.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/news && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/news/%%P\n' ) \
  >> pmda-news.list
echo '%%dir /var/lib/pcp/pmdas/news' >> pmda-news.list
%endif
( cd %{buildroot}%{_pmdasdir}/nfsclient && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/nfsclient/%%P\n' ) \
  >> pmda-nfsclient.list
echo '%%dir /var/lib/pcp/pmdas/nfsclient' >> pmda-nfsclient.list
( cd %{buildroot}%{_pmdasdir}/nvidia && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/nvidia/%%P\n' ) \
  >> pmda-nvidia-gpu.list
echo '%%dir /var/lib/pcp/pmdas/nvidia' >> pmda-nvidia-gpu.list
( cd %{buildroot}%{_pmdasdir}/openvswitch && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/openvswitch/%%P\n' ) \
  >> pmda-openvswitch.list
echo '%%dir /var/lib/pcp/pmdas/openvswitch' >> pmda-openvswitch.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/pdns && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/pdns/%%P\n' ) \
  >> pmda-pdns.list
echo '%%dir /var/lib/pcp/pmdas/pdns' >> pmda-pdns.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/postfix && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/postfix/%%P\n' ) \
  >> pmda-postfix.list
echo '%%dir /var/lib/pcp/pmdas/postfix' >> pmda-postfix.list
%endif
( cd %{buildroot}%{_pmdasdir}/roomtemp && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/roomtemp/%%P\n' ) \
  >> pmda-roomtemp.list
echo '%%dir /var/lib/pcp/pmdas/roomtemp' >> pmda-roomtemp.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/rsyslog && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/rsyslog/%%P\n' ) \
  >> pmda-rsyslog.list
echo '%%dir /var/lib/pcp/pmdas/rsyslog' >> pmda-rsyslog.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/samba && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/samba/%%P\n' ) \
  >> pmda-samba.list
echo '%%dir /var/lib/pcp/pmdas/samba' >> pmda-samba.list
%endif
( cd %{buildroot}%{_pmdasdir}/sendmail && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/sendmail/%%P\n' ) \
  >> pmda-sendmail.list
echo '%%dir /var/lib/pcp/pmdas/sendmail' >> pmda-sendmail.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/slurm && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/slurm/%%P\n' ) \
  >> pmda-slurm.list
echo '%%dir /var/lib/pcp/pmdas/slurm' >> pmda-slurm.list
%endif
( cd %{buildroot}%{_pmdasdir}/smart && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/smart/%%P\n' ) \
  >> pmda-smart.list
echo '%%dir /var/lib/pcp/pmdas/smart' >> pmda-smart.list
( cd %{buildroot}%{_pmdasdir}/sockets && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/sockets/%%P\n' ) \
  >> pmda-sockets.list
echo '%%dir /var/lib/pcp/pmdas/sockets' >> pmda-sockets.list
%if !%{disable_systemd}
( cd %{buildroot}%{_pmdasdir}/systemd && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/systemd/%%P\n' ) \
  >> pmda-systemd.list
echo '%%dir /var/lib/pcp/pmdas/systemd' >> pmda-systemd.list
%endif
( cd %{buildroot}%{_pmdasdir}/trace && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/trace/%%P\n' ) \
  >> pmda-trace.list
echo '%%dir /var/lib/pcp/pmdas/trace' >> pmda-trace.list
( cd %{buildroot}%{_pmdasdir}/unbound && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/unbound/%%P\n' ) \
  >> pmda-unbound.list
echo '%%dir /var/lib/pcp/pmdas/unbound' >> pmda-unbound.list
( cd %{buildroot}%{_pmdasdir}/weblog && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/weblog/%%P\n' ) \
  >> pmda-weblog.list
echo '%%dir /var/lib/pcp/pmdas/weblog' >> pmda-weblog.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/zimbra && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/zimbra/%%P\n' ) \
  >> pmda-zimbra.list
echo '%%dir /var/lib/pcp/pmdas/zimbra' >> pmda-zimbra.list
%endif
%if !%{disable_python3}
( cd %{buildroot}%{_pmdasdir}/zswap && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/zswap/%%P\n' ) \
  >> pmda-zswap.list
echo '%%dir /var/lib/pcp/pmdas/zswap' >> pmda-zswap.list
%endif
( cd %{buildroot}%{_pmdasdir}/elasticsearch && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/elasticsearch/%%P\n' ) \
  >> pmda-elasticsearch.list
echo '%%dir /var/lib/pcp/pmdas/elasticsearch' >> pmda-elasticsearch.list
( cd %{buildroot}%{_pmdasdir}/haproxy && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/haproxy/%%P\n' ) \
  >> pmda-haproxy.list
echo '%%dir /var/lib/pcp/pmdas/haproxy' >> pmda-haproxy.list
( cd %{buildroot}%{_pmdasdir}/netcheck && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/netcheck/%%P\n' ) \
  >> pmda-netcheck.list
echo '%%dir /var/lib/pcp/pmdas/netcheck' >> pmda-netcheck.list
( cd %{buildroot}%{_pmdasdir}/rabbitmq && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/rabbitmq/%%P\n' ) \
  >> pmda-rabbitmq.list
echo '%%dir /var/lib/pcp/pmdas/rabbitmq' >> pmda-rabbitmq.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/redis && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/redis/%%P\n' ) \
  >> pmda-redis.list
echo '%%dir /var/lib/pcp/pmdas/redis' >> pmda-redis.list
%endif
%if !%{disable_snmp}
( cd %{buildroot}%{_pmdasdir}/snmp && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/snmp/%%P\n' ) \
  >> pmda-snmp.list
echo '%%dir /var/lib/pcp/pmdas/snmp' >> pmda-snmp.list
%endif
%if !%{disable_json}
( cd %{buildroot}%{_pmdasdir}/json && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/json/%%P\n' ) \
  >> pmda-json.list
echo '%%dir /var/lib/pcp/pmdas/json' >> pmda-json.list
%endif
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/lustre && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/lustre/%%P\n' ) \
  >> pmda-lustre.list
echo '%%dir /var/lib/pcp/pmdas/lustre' >> pmda-lustre.list
%endif
( cd %{buildroot}%{_pmdasdir}/mounts && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/mounts/%%P\n' ) \
  >> pmda-mounts.list
echo '%%dir /var/lib/pcp/pmdas/mounts' >> pmda-mounts.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/nginx && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/nginx/%%P\n' ) \
  >> pmda-nginx.list
echo '%%dir /var/lib/pcp/pmdas/nginx' >> pmda-nginx.list
%endif
%if !%{disable_nutcracker}
( cd %{buildroot}%{_pmdasdir}/nutcracker && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/nutcracker/%%P\n' ) \
  >> pmda-nutcracker.list
echo '%%dir /var/lib/pcp/pmdas/nutcracker' >> pmda-nutcracker.list
%endif
( cd %{buildroot}%{_pmdasdir}/openmetrics && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/openmetrics/%%P\n' ) \
  >> pmda-openmetrics.list
echo '%%dir /var/lib/pcp/pmdas/openmetrics' >> pmda-openmetrics.list
%if !%{disable_perl}
( cd %{buildroot}%{_pmdasdir}/oracle && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/oracle/%%P\n' ) \
  >> pmda-oracle.list
echo '%%dir /var/lib/pcp/pmdas/oracle' >> pmda-oracle.list
%endif
( cd %{buildroot}%{_pmdasdir}/shping && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/shping/%%P\n' ) \
  >> pmda-shping.list
echo '%%dir /var/lib/pcp/pmdas/shping' >> pmda-shping.list
( cd %{buildroot}%{_pmdasdir}/summary && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/summary/%%P\n' ) \
  >> pmda-summary.list
echo '%%dir /var/lib/pcp/pmdas/summary' >> pmda-summary.list
( cd %{buildroot}%{_pmdasdir}/dm && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/dm/%%P\n' ) \
  >> pmda-dm.list
echo '%%dir /var/lib/pcp/pmdas/dm' >> pmda-dm.list
# pmda-dm additionally ships content under %{_ieconfdir}/dm; enumerate
# that tree as well so the script will ghost it and emit tmpfiles
# entries pointing at the underlying /etc/pcp/pmieconf/dm targets.
( cd %{buildroot}%{_ieconfdir}/dm && \
  find . -mindepth 1 -printf '/var/lib/pcp/config/pmieconf/dm/%%P\n' ) \
  >> pmda-dm.list
echo '%%dir /var/lib/pcp/config/pmieconf/dm' >> pmda-dm.list
%if !%{disable_perfevent}
( cd %{buildroot}%{_pmdasdir}/perfevent && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/perfevent/%%P\n' ) \
  >> pmda-perfevent.list
echo '%%dir /var/lib/pcp/pmdas/perfevent' >> pmda-perfevent.list
%endif

# Pattern 5 PMDAs (resctrl, uwsgi): hand-listed %files blocks above
# include their /var/lib/pcp/pmdas/<name> paths individually. We
# enumerate those subtrees here so the relocation step ghosts them and
# emits L+ tmpfiles entries pointing at the existing %{_libexecdir}
# (and, for uwsgi.conf, %{_confdir}) targets.
%if !%{disable_resctrl}
( cd %{buildroot}%{_pmdasdir}/resctrl && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/resctrl/%%P\n' ) \
  >> pmda-resctrl.list
echo '%%dir /var/lib/pcp/pmdas/resctrl' >> pmda-resctrl.list
%endif
( cd %{buildroot}%{_pmdasdir}/uwsgi && \
  find . -mindepth 1 -printf '/var/lib/pcp/pmdas/uwsgi/%%P\n' ) \
  >> pmda-uwsgi.list
echo '%%dir /var/lib/pcp/pmdas/uwsgi' >> pmda-uwsgi.list

# pcp-conf ships symlinks under /var/lib/pcp/config/derived/ pointing
# into /etc/pcp/derived/.
( cd %{buildroot}%{_localstatedir}/lib/pcp/config/derived && \
  find . -mindepth 1 -printf '/var/lib/pcp/config/derived/%%P\n' ) \
  >> conf.list
echo '%%dir /var/lib/pcp/config/derived' >> conf.list

# pcp-zeroconf ships symlinks under /var/lib/pcp/config/{pmieconf,pmlogconf}/zeroconf/
# pointing into /etc/pcp/{pmieconf,pmlogconf}/zeroconf/.
for d in pmieconf pmlogconf; do
    ( cd %{buildroot}%{_localstatedir}/lib/pcp/config/$d/zeroconf && \
      find . -mindepth 1 -printf "/var/lib/pcp/config/$d/zeroconf/%%P\n" ) \
      >> zeroconf.list
    echo "%%dir /var/lib/pcp/config/$d/zeroconf" >> zeroconf.list
done

# pcp-testsuite is the only subpackage exercising the script's
# real-file relocation path: ~5500 actual files under
# /var/lib/pcp/testsuite/ get cp'd into %{_stashdir}/testsuite/ and
# %ghost'd at their legacy location. The dirs are also enumerated so
# the rewritten list and tmpfiles snippet cover the whole tree.
( cd %{buildroot}%{_testsdir} && \
  find . -mindepth 1 \( -type f -o -type l \) \
        -printf "/var/lib/pcp/testsuite/%%P\n" ) \
  >> testsuite.list
( cd %{buildroot}%{_testsdir} && \
  find . -mindepth 1 -type d \
        -printf "%%%%dir /var/lib/pcp/testsuite/%%P\n" ) \
  >> testsuite.list
echo '%%dir /var/lib/pcp/testsuite' >> testsuite.list
###############################################################################
# Stash relocation (boo#XXXXXXX).
#
# At this point all subpackage .list files have been generated in $BACKDIR.
# For each entry naming a path under /var/lib/pcp:
#   - if the buildroot has a symlink there, delete it and emit an
#     'L+ <path> - - - - <original-target>' tmpfiles entry;
#   - if the buildroot has a real file there (testsuite case), move it
#     to %{_stashdir} and emit an 'L+ <path> - - - - <stash-path>' entry.
# The .list files are rewritten in place to %ghost the legacy paths and
# (for relocated files) name the stash paths.
#
# Required for transactional-update / immutable-OS targets where /var
# is a separate writable subvolume from the read-only /usr snapshot.
###############################################################################
install -m 0755 %{SOURCE50} $BACKDIR/pcp-stash-relocate.sh
$BACKDIR/pcp-stash-relocate.sh \
    --buildroot   %{buildroot} \
    --legacy-root /var/lib/pcp \
    --legacy-root /var/log/pcp \
    --stash-root  %{_stashdir} \
    --listdir     $BACKDIR \
    --tmpfilesdir %{_tmpfilesdir} \
    --skip        base_pmdas \
    --skip        base_conf \
    --skip        base_pmns \
    --skip        base_bin \
    --skip        base_exec \
    --skip        base_bashcomp \
    --skip        pcp-logconf \
    --skip        pcp-ieconf

%pre testsuite
test -d %{_testsdir} || mkdir -p -m 755 %{_testsdir}
getent group pcpqa >/dev/null || groupadd -r pcpqa
getent passwd pcpqa >/dev/null || \
  useradd -c "PCP Quality Assurance" -g pcpqa -d %{_testsdir} -M -r -s /bin/bash pcpqa 2>/dev/null

%post testsuite
%tmpfiles_create pcp-testsuite-stash.conf

%postun testsuite
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-testsuite-stash.conf >/dev/null 2>&1 || :
fi

%pre
%if 0%{?suse_version} && !%{disable_systemd}
%service_add_pre pmcd pmlogger pmie pmproxy pmie_check.timer pmie_daily.timer pmlogger_daily.timer pmlogger_check.timer
%endif
getent group pcp >/dev/null || groupadd -r pcp
getent passwd pcp >/dev/null || \
  useradd -c "Performance Co-Pilot" -g pcp -d %{_localstatedir}/lib/pcp -M -r -s /sbin/nologin pcp

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

# Batch A: %post/%postun for relocated PMDAs. Each invokes
# systemd-tmpfiles to materialise the /var/lib/pcp/pmdas/<name>
# symlink tree at install time and clean it up on uninstall.
%post pmda-amdgpu
%tmpfiles_create pcp-pmda-amdgpu-stash.conf

%postun pmda-amdgpu
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-amdgpu-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-apache
%tmpfiles_create pcp-pmda-apache-stash.conf

%postun pmda-apache
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-apache-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-bash
%tmpfiles_create pcp-pmda-bash-stash.conf

%postun pmda-bash
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-bash-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-bonding
%tmpfiles_create pcp-pmda-bonding-stash.conf

%postun pmda-bonding
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-bonding-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-cifs
%tmpfiles_create pcp-pmda-cifs-stash.conf

%postun pmda-cifs
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-cifs-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-cisco
%tmpfiles_create pcp-pmda-cisco-stash.conf

%postun pmda-cisco
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-cisco-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-dbping
%tmpfiles_create pcp-pmda-dbping-stash.conf

%postun pmda-dbping
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-dbping-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-docker
%tmpfiles_create pcp-pmda-docker-stash.conf

%postun pmda-docker
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-docker-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-ds389
%tmpfiles_create pcp-pmda-ds389-stash.conf

%postun pmda-ds389
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-ds389-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-ds389log
%tmpfiles_create pcp-pmda-ds389log-stash.conf

%postun pmda-ds389log
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-ds389log-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-gfs2
%tmpfiles_create pcp-pmda-gfs2-stash.conf

%postun pmda-gfs2
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-gfs2-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_python3}
%post pmda-gluster
%tmpfiles_create pcp-pmda-gluster-stash.conf

%postun pmda-gluster
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-gluster-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-gpfs
%tmpfiles_create pcp-pmda-gpfs-stash.conf

%postun pmda-gpfs
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-gpfs-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-gpsd
%tmpfiles_create pcp-pmda-gpsd-stash.conf

%postun pmda-gpsd
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-gpsd-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-hacluster
%tmpfiles_create pcp-pmda-hacluster-stash.conf

%postun pmda-hacluster
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-hacluster-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_infiniband}
%post pmda-infiniband
%tmpfiles_create pcp-pmda-infiniband-stash.conf

%postun pmda-infiniband
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-infiniband-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_lio}
%post pmda-lio
%tmpfiles_create pcp-pmda-lio-stash.conf

%postun pmda-lio
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-lio-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-lmsensors
%tmpfiles_create pcp-pmda-lmsensors-stash.conf

%postun pmda-lmsensors
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-lmsensors-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-logger
%tmpfiles_create pcp-pmda-logger-stash.conf

%postun pmda-logger
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-logger-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-lustrecomm
%tmpfiles_create pcp-pmda-lustrecomm-stash.conf

%postun pmda-lustrecomm
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-lustrecomm-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-mailq
%tmpfiles_create pcp-pmda-mailq-stash.conf

%postun pmda-mailq
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-mailq-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-memcache
%tmpfiles_create pcp-pmda-memcache-stash.conf

%postun pmda-memcache
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-memcache-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-mic
%tmpfiles_create pcp-pmda-mic-stash.conf

%postun pmda-mic
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-mic-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-mysql
%tmpfiles_create pcp-pmda-mysql-stash.conf

%postun pmda-mysql
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-mysql-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-named
%tmpfiles_create pcp-pmda-named-stash.conf

%postun pmda-named
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-named-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-netfilter
%tmpfiles_create pcp-pmda-netfilter-stash.conf

%postun pmda-netfilter
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-netfilter-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-news
%tmpfiles_create pcp-pmda-news-stash.conf

%postun pmda-news
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-news-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-nfsclient
%tmpfiles_create pcp-pmda-nfsclient-stash.conf

%postun pmda-nfsclient
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-nfsclient-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-nvidia-gpu
%tmpfiles_create pcp-pmda-nvidia-gpu-stash.conf

%postun pmda-nvidia-gpu
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-nvidia-gpu-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-openvswitch
%tmpfiles_create pcp-pmda-openvswitch-stash.conf

%postun pmda-openvswitch
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-openvswitch-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-pdns
%tmpfiles_create pcp-pmda-pdns-stash.conf

%postun pmda-pdns
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-pdns-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-postfix
%tmpfiles_create pcp-pmda-postfix-stash.conf

%postun pmda-postfix
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-postfix-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-roomtemp
%tmpfiles_create pcp-pmda-roomtemp-stash.conf

%postun pmda-roomtemp
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-roomtemp-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-rsyslog
%tmpfiles_create pcp-pmda-rsyslog-stash.conf

%postun pmda-rsyslog
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-rsyslog-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-samba
%tmpfiles_create pcp-pmda-samba-stash.conf

%postun pmda-samba
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-samba-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-sendmail
%tmpfiles_create pcp-pmda-sendmail-stash.conf

%postun pmda-sendmail
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-sendmail-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-slurm
%tmpfiles_create pcp-pmda-slurm-stash.conf

%postun pmda-slurm
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-slurm-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-smart
%tmpfiles_create pcp-pmda-smart-stash.conf

%postun pmda-smart
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-smart-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-sockets
%tmpfiles_create pcp-pmda-sockets-stash.conf

%postun pmda-sockets
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-sockets-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_systemd}
%post pmda-systemd
%tmpfiles_create pcp-pmda-systemd-stash.conf

%postun pmda-systemd
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-systemd-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-trace
%tmpfiles_create pcp-pmda-trace-stash.conf

%postun pmda-trace
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-trace-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-unbound
%tmpfiles_create pcp-pmda-unbound-stash.conf

%postun pmda-unbound
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-unbound-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-weblog
%tmpfiles_create pcp-pmda-weblog-stash.conf

%postun pmda-weblog
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-weblog-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-zimbra
%tmpfiles_create pcp-pmda-zimbra-stash.conf

%postun pmda-zimbra
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-zimbra-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_python3}
%post pmda-zswap
%tmpfiles_create pcp-pmda-zswap-stash.conf

%postun pmda-zswap
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-zswap-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-elasticsearch
%tmpfiles_create pcp-pmda-elasticsearch-stash.conf

%postun pmda-elasticsearch
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-elasticsearch-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-haproxy
%tmpfiles_create pcp-pmda-haproxy-stash.conf

%postun pmda-haproxy
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-haproxy-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-netcheck
%tmpfiles_create pcp-pmda-netcheck-stash.conf

%postun pmda-netcheck
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-netcheck-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-rabbitmq
%tmpfiles_create pcp-pmda-rabbitmq-stash.conf

%postun pmda-rabbitmq
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-rabbitmq-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-redis
%tmpfiles_create pcp-pmda-redis-stash.conf

%postun pmda-redis
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-redis-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_snmp}
%post pmda-snmp
%tmpfiles_create pcp-pmda-snmp-stash.conf

%postun pmda-snmp
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-snmp-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perfevent}
%post pmda-perfevent
%tmpfiles_create pcp-pmda-perfevent-stash.conf

%postun pmda-perfevent
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-perfevent-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_resctrl}
%post pmda-resctrl
%tmpfiles_create pcp-pmda-resctrl-stash.conf

%postun pmda-resctrl
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-resctrl-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-uwsgi
%tmpfiles_create pcp-pmda-uwsgi-stash.conf

%postun pmda-uwsgi
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-uwsgi-stash.conf >/dev/null 2>&1 || :
fi

%post conf
%tmpfiles_create pcp-conf-stash.conf

%postun conf
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-conf-stash.conf >/dev/null 2>&1 || :
fi

%post devel
%tmpfiles_create pcp-devel-stash.conf

%postun devel
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-devel-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_qt}
%post gui
%tmpfiles_create pcp-pcp-gui-stash.conf

%postun gui
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pcp-gui-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_json}
%post pmda-json
%tmpfiles_create pcp-pmda-json-stash.conf

%postun pmda-json
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-json-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_perl}
%post pmda-lustre
%tmpfiles_create pcp-pmda-lustre-stash.conf

%postun pmda-lustre
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-lustre-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-mounts
%tmpfiles_create pcp-pmda-mounts-stash.conf

%postun pmda-mounts
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-mounts-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-nginx
%tmpfiles_create pcp-pmda-nginx-stash.conf

%postun pmda-nginx
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-nginx-stash.conf >/dev/null 2>&1 || :
fi
%endif

%if !%{disable_nutcracker}
%post pmda-nutcracker
%tmpfiles_create pcp-pmda-nutcracker-stash.conf

%postun pmda-nutcracker
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-nutcracker-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-openmetrics
%tmpfiles_create pcp-pmda-openmetrics-stash.conf

%postun pmda-openmetrics
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-openmetrics-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-oracle
%tmpfiles_create pcp-pmda-oracle-stash.conf

%postun pmda-oracle
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-oracle-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post pmda-shping
%tmpfiles_create pcp-pmda-shping-stash.conf

%postun pmda-shping
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-shping-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-summary
%tmpfiles_create pcp-pmda-summary-stash.conf

%postun pmda-summary
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-summary-stash.conf >/dev/null 2>&1 || :
fi

%post pmda-dm
%tmpfiles_create pcp-pmda-dm-stash.conf

%postun pmda-dm
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-dm-stash.conf >/dev/null 2>&1 || :
fi

%if !%{disable_perl}
%post pmda-activemq
%tmpfiles_create pcp-pmda-activemq-stash.conf

%postun pmda-activemq
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-pmda-activemq-stash.conf >/dev/null 2>&1 || :
fi
%endif

%post zeroconf
%tmpfiles_create pcp-zeroconf-stash.conf
%if 0%{?suse_version}
%else
%if !%{disable_systemd}
    systemctl restart pmcd >/dev/null 2>&1
    systemctl restart pmlogger >/dev/null 2>&1
    systemctl restart pmie >/dev/null 2>&1
    systemctl enable pmcd >/dev/null 2>&1
    systemctl enable pmlogger >/dev/null 2>&1
    systemctl enable pmlogger_daily >/dev/null 2>&1
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

%postun zeroconf
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-zeroconf-stash.conf >/dev/null 2>&1 || :
fi

%post
%tmpfiles_create pcp-base-stash.conf
PCP_PMNS_DIR=%{_pmnsdir}
PCP_LOG_DIR=%{_logsdir}
%{install_file "$PCP_PMNS_DIR" .NeedRebuild}
%{install_file "$PCP_LOG_DIR/pmlogger" .NeedRewrite}
%if 0%{?suse_version}
%if !%{disable_systemd}
%{fillup_only -n pmcd}
%{fillup_only -n pmlogger}
%{fillup_only -n pmproxy}
%service_add_post pmcd pmlogger pmie pmproxy pmie_check.timer pmie_daily.timer pmlogger_daily.timer pmlogger_check.timer
%else
%{fillup_and_insserv pmcd}
%{fillup_and_insserv pmlogger}
%{fillup_and_insserv pmie}
%{fillup_and_insserv pmproxy}
%{fillup_and_insserv pmie_timers}
%{fillup_and_insserv pmlogger_timers}
%{fillup_and_insserv pmlogger_farm}
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

%if 0%{?suse_version}
%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    systemd-tmpfiles --remove pcp-base-stash.conf >/dev/null 2>&1 || :
fi
%if !%{disable_systemd}
%service_del_postun pmcd pmlogger pmproxy pmie pmie_check.timer pmie_daily.timer pmlogger_daily.timer pmlogger_check.timer
%else
%{?restart_on_update:%{restart_on_update pcp pmproxy pmie}}
%{?insserv_cleanup:%{insserv_cleanup}}
%endif
%endif

%if !%{disable_selinux}
%pre selinux
%selinux_relabel_pre -s targeted

%post selinux
PCP_SELINUX_DIR=%{_selinuxdir}
semodule -r pcpupstream-container >/dev/null 2>&1 || true
semodule -r pcpupstream-docker >/dev/null 2>&1 || true
semodule -r pcpupstream >/dev/null 2>&1 || true
%selinux_modules_install -s targeted "$PCP_SELINUX_DIR/pcp.pp.bz2"
%selinux_relabel_post -s targeted

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s targeted pcp
    %selinux_relabel_post -s targeted
fi
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

%config(noreplace) %{_sysconfdir}/pcp/sockets/filter.conf
%config(noreplace) %{_sysconfdir}/pcp/kvm/kvm.conf
%{_prefix}/lib/systemd/system/pmie_farm.service
%{_prefix}/lib/systemd/system/pmie_farm_check.service
%{_prefix}/lib/systemd/system/pmie_farm_check.timer
%{_prefix}/lib/systemd/system/pmlogger_farm.service
%{_prefix}/lib/systemd/system/pmlogger_farm_check.service
%{_prefix}/lib/systemd/system/pmlogger_farm_check.timer
%{_libexecdir}/pcp/pmdas/denki/Install
%{_libexecdir}/pcp/pmdas/denki/README
%{_libexecdir}/pcp/pmdas/denki/Remove
%{_libexecdir}/pcp/pmdas/denki/domain.h
%{_libexecdir}/pcp/pmdas/denki/help
%{_libexecdir}/pcp/pmdas/denki/pmda_denki.so
%{_libexecdir}/pcp/pmdas/denki/pmdadenki
%{_libexecdir}/pcp/pmdas/denki/root
%{_libexecdir}/pcp/pmdas/podman/Install
%{_libexecdir}/pcp/pmdas/podman/Remove
%{_libexecdir}/pcp/pmdas/podman/domain.h
%{_libexecdir}/pcp/pmdas/podman/help
%{_libexecdir}/pcp/pmdas/podman/pmda_podman.so
%{_libexecdir}/pcp/pmdas/podman/pmdapodman
%{_libexecdir}/pcp/pmdas/podman/root
%{_datadir}/pcp/htop/columns/container
%{_datadir}/pcp/htop/columns/delayacct
%{_datadir}/pcp/htop/columns/fdcount
%{_datadir}/pcp/htop/columns/guest
%{_datadir}/pcp/htop/columns/gpu_memory
%{_datadir}/pcp/htop/columns/memory
%{_datadir}/pcp/htop/columns/sched
%{_datadir}/pcp/htop/columns/swap
%{_datadir}/pcp/htop/columns/tcp
%{_datadir}/pcp/htop/columns/udp
%{_datadir}/pcp/htop/columns/wchan
%{_datadir}/pcp/htop/meters/entropy
%{_datadir}/pcp/htop/meters/freespace
%{_datadir}/pcp/htop/meters/gpu
%{_datadir}/pcp/htop/meters/ipc
%{_datadir}/pcp/htop/meters/locks
%{_datadir}/pcp/htop/meters/memcache
%{_datadir}/pcp/htop/meters/mysql
%{_datadir}/pcp/htop/meters/postfix
%{_datadir}/pcp/htop/meters/redis
%{_datadir}/pcp/htop/meters/tcp
%{_datadir}/pcp/zeroconf/pmlogger

%dir %{_sysconfdir}/pcp/sockets
%dir %{_libexecdir}/pcp/pmdas/denki
%dir %{_libexecdir}/pcp/pmdas/podman
%dir %{_datadir}/pcp/htop
%dir %{_datadir}/pcp/htop/columns
%dir %{_datadir}/pcp/htop/meters
%dir %{_datadir}/pcp/zeroconf

%dir %{_confdir}
%dir %{_pmdasexecdir}
%dir %{_datadir}/pcp
%dir %{_libexecdir}/pcp
%dir %{_stashdir}
%dir %{_libexecdir}/pcp/bin
%if %{disable_qt}
# part of pcp-gui
%exclude %{_localstatedir}/lib/pcp/config/pmafm/pcp-gui
%endif

%dir %{_datadir}/pcp/lib
%{_datadir}/pcp/lib/ReplacePmnsSubtree
%{_datadir}/pcp/lib/bashproc.sh
%{_datadir}/pcp/lib/lockpmns
%{_datadir}/pcp/lib/pmdaproc.sh
%{_datadir}/pcp/lib/utilproc.sh
%{_datadir}/pcp/lib/rc-proc.sh
%{_datadir}/pcp/lib/rc-proc.sh.minimal
%{_datadir}/pcp/lib/unlockpmns
%{_datadir}/pcp/lib/checkproc.sh
%{_datadir}/pcp/lib/pmcheck/pmcd
%{_datadir}/pcp/lib/pmcheck/pmda-overhead
%{_datadir}/pcp/lib/pmcheck/pmda-postgresql
%{_datadir}/pcp/lib/pmcheck/pmda-redis
%{_datadir}/pcp/lib/pmcheck/pmda-sample
%{_datadir}/pcp/lib/pmcheck/pmda-uwsgi
%{_datadir}/pcp/lib/pmcheck/pmie
%{_datadir}/pcp/lib/pmcheck/pmlogger
%{_datadir}/pcp/lib/pmcheck/pmproxy
%{_datadir}/pcp/lib/pmcheck/zeroconf
%dir %{_datadir}/pcp/lib/pmcheck

%config %{_sysusersdir}/pcp-testsuite.conf
%config %{_sysusersdir}/pcp.conf
%config %{_tmpfilesdir}/pcp-reboot-init.conf
%config(noreplace) %{_sysconfdir}/pcp/indom.conf
%config(noreplace) %{_sysconfdir}/pcp/overhead/conf.d/default.conf
%config(noreplace) %{_sysconfdir}/pcp/overhead/examples/sample.conf
%config(noreplace) %{_sysconfdir}/pcp/tls.conf
%{_libdir}/libpcp_archive.so
%{_libdir}/libpcp_archive.so.1
%{_libdir}/pkgconfig/libpcp_archive.pc
%{_libexecdir}/pcp/bin/pmlogger_daily_report
%{_libexecdir}/pcp/pmdas/denki/pmns
%{_libexecdir}/pcp/pmdas/farm/Install
%{_libexecdir}/pcp/pmdas/farm/Remove
%{_libexecdir}/pcp/pmdas/farm/domain.h
%{_libexecdir}/pcp/pmdas/farm/help
%{_libexecdir}/pcp/pmdas/farm/pmda_farm.so
%{_libexecdir}/pcp/pmdas/farm/pmdafarm
%{_libexecdir}/pcp/pmdas/farm/pmns
%{_libexecdir}/pcp/pmdas/farm/root
%{_libexecdir}/pcp/pmdas/overhead/Install
%{_libexecdir}/pcp/pmdas/overhead/README
%{_libexecdir}/pcp/pmdas/overhead/Remove
%{_libexecdir}/pcp/pmdas/overhead/domain.h
%{_libexecdir}/pcp/pmdas/overhead/pmdaoverhead
%{_libexecdir}/pcp/pmdas/overhead/pmns
%{_libexecdir}/pcp/pmdas/overhead/root
%{_libexecdir}/pcp/pmdas/podman/pmns
%{_sysconfdir}/pcp/pmlogredact/network
%{_sysconfdir}/pcp/pmlogredact/usernames
%{_unitdir}/pcp-geolocate.service
%{_unitdir}/pcp-reboot-init.service
%{_usr}/share/pcp/htop/screens/biosnoop
%{_usr}/share/pcp/htop/screens/cgroups
%{_usr}/share/pcp/htop/screens/cgroupsio
%{_usr}/share/pcp/htop/screens/cgroupsmem
%{_usr}/share/pcp/htop/screens/devices
%{_usr}/share/pcp/htop/screens/execsnoop
%{_usr}/share/pcp/htop/screens/exitsnoop
%{_usr}/share/pcp/htop/screens/filesystems
%{_usr}/share/pcp/htop/screens/opensnoop
%dir %{_libexecdir}/pcp/pmdas/farm
%dir %{_libexecdir}/pcp/pmdas/overhead
%dir %{_sysconfdir}/pcp/overhead
%dir %{_sysconfdir}/pcp/overhead/conf.d
%dir %{_sysconfdir}/pcp/overhead/examples
%dir %{_sysconfdir}/pcp/pmlogredact
%dir %{_usr}/share/pcp/htop/screens

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
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmlogger-daily-report
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmfind
%config(noreplace) %{_sysconfdir}/cron.d/pcp-pmie
%else
%{_unitdir}/pmlogger_daily.service
%{_unitdir}/pmlogger_daily.timer
%{_unitdir}/pmlogger_check.service
%{_unitdir}/pmlogger_check.timer
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
%{_fillupdir}/sysconfig.pmlogger_farm
%else
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger
%config(noreplace) %{_sysconfdir}/sysconfig/pmproxy
%config(noreplace) %{_sysconfdir}/sysconfig/pmfind
%config(noreplace) %{_sysconfdir}/sysconfig/pmcd
%config(noreplace) %{_sysconfdir}/sysconfig/pmie_timers
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger_timers
%config(noreplace) %{_sysconfdir}/sysconfig/pmlogger_farm
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
%attr(0644,pcp,pcp) %{_localstatedir}/lib/pcp/config/pmlogger/*
%dir %{_logconfdir}
%{_localstatedir}/lib/pcp/config/pmlogrewrite

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_pcp
%if !%{disable_sdt}
%{_tapsetdir}/pmcd.stp
%endif

%files zeroconf -f zeroconf.list
%if !%{disable_systemd}
%else
%endif
%config(noreplace) %{_confdir}/pmieconf/zeroconf
%config(noreplace) %{_confdir}/pmlogconf/zeroconf

#additional pmlogger config files

%files conf -f conf.list
%config %{_confdir}/derived/*
%config %{_sysconfdir}/pcp.conf
%dir %{_confdir}/derived
%dir %{_includedir}/pcp
%{_includedir}/pcp/builddefs
%{_includedir}/pcp/buildrules

%files -n %{lib_pkg}
%{_libdir}/libpcp.so.%{libpcp_pmda_sover}
%{_libdir}/libpcp_pmda.so.%{libpcp_pmda_sover}
%{_libdir}/libpcp_fault.so.%{libpcp_fault_sover}
%if !0%{?suse_version}
%{_libdir}/libpcp_gui.so.%{libpcp_gui_sover}
%{_libdir}/libpcp_import.so.%{libpcp_import_sover}
%{_libdir}/libpcp_mmv.so.%{libpcp_mmv_sover}
%{_libdir}/libpcp_trace.so.%{libpcp_trace_sover}
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
%{_libdir}/libpcp_fault.so
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
%config(noreplace) %{_confdir}/simple

%files testsuite -f testsuite.list

%if !%{disable_perl}
%files import-sar2pcp
%{_bindir}/sar2pcp
%endif

%if !%{disable_perl}
%files import-iostat2pcp
%{_bindir}/iostat2pcp
%endif

%if !%{disable_sheet2pcp}
%files import-sheet2pcp
%{_bindir}/sheet2pcp
%endif

%if !%{disable_perl}
%files import-mrtg2pcp
%{_bindir}/mrtg2pcp
%endif

%if !%{disable_perl}
%files import-ganglia2pcp
%{_bindir}/ganglia2pcp
%endif

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
%files pmda-perfevent -f pmda-perfevent.list
%{_pmdasexecdir}/perfevent
%dir %{_confdir}/perfevent
%config(noreplace) %{_confdir}/perfevent/perfevent.conf
%endif

%if !%{disable_infiniband}
%files pmda-infiniband -f pmda-infiniband.list
%{_pmdasexecdir}/infiniband
%endif

%if !%{disable_perl}
%files pmda-activemq -f pmda-activemq.list
%{_pmdasexecdir}/activemq
%endif

%if !%{disable_perl}
%files pmda-bonding -f pmda-bonding.list
%{_pmdasexecdir}/bonding
%endif

%if !%{disable_perl}
%files pmda-dbping -f pmda-dbping.list
%{_pmdasexecdir}/dbping
%endif

%if !%{disable_perl}
%files pmda-ds389log -f pmda-ds389log.list
%{_pmdasexecdir}/ds389log
%endif

%if !%{disable_perl}
%files pmda-ds389 -f pmda-ds389.list
%{_pmdasexecdir}/ds389
%endif

%files pmda-elasticsearch -f pmda-elasticsearch.list
%dir %{_confdir}/elasticsearch
%config(noreplace) %{_confdir}/elasticsearch/elasticsearch.conf
%{_pmdasexecdir}/elasticsearch

%files pmda-openvswitch -f pmda-openvswitch.list
%{_pmdasexecdir}/openvswitch

%files pmda-rabbitmq -f pmda-rabbitmq.list
%dir %{_confdir}/rabbitmq
%config(noreplace) %{_confdir}/rabbitmq/rabbitmq.conf
%{_pmdasexecdir}/rabbitmq

%if !%{disable_perl}
%files pmda-gpfs -f pmda-gpfs.list
%{_pmdasexecdir}/gpfs
%endif

%if !%{disable_perl}
%files pmda-gpsd -f pmda-gpsd.list
%{_pmdasexecdir}/gpsd
%endif

%files pmda-docker -f pmda-docker.list
%{_pmdasexecdir}/docker

%if !%{disable_lio}
%files pmda-lio -f pmda-lio.list
%{_pmdasexecdir}/lio
%endif

%files pmda-openmetrics -f pmda-openmetrics.list
%{_pmdasexecdir}/openmetrics
%config(noreplace) %{_confdir}/openmetrics

%if !%{disable_perl}
%files pmda-lustre -f pmda-lustre.list
%{_pmdasexecdir}/lustre
%config(noreplace) %{_confdir}/lustre
%endif

%files pmda-lustrecomm -f pmda-lustrecomm.list
%{_pmdasexecdir}/lustrecomm

%if !%{disable_perl}
%files pmda-memcache -f pmda-memcache.list
%{_pmdasexecdir}/memcache
%endif

%if !%{disable_perl}
%files pmda-mysql -f pmda-mysql.list
%{_pmdasexecdir}/mysql
%endif

%if !%{disable_perl}
%files pmda-named -f pmda-named.list
%{_pmdasexecdir}/named
%endif

%if !%{disable_perl}
%files pmda-netfilter -f pmda-netfilter.list
%{_pmdasexecdir}/netfilter
%endif

%if !%{disable_perl}
%files pmda-news -f pmda-news.list
%{_pmdasexecdir}/news
%endif

%if !%{disable_perl}
%files pmda-nginx -f pmda-nginx.list
%{_pmdasexecdir}/nginx
%config(noreplace) %{_confdir}/nginx
%endif

%files pmda-nfsclient -f pmda-nfsclient.list
%{_pmdasexecdir}/nfsclient

%if !%{disable_nutcracker}
%files pmda-nutcracker -f pmda-nutcracker.list
%{_pmdasexecdir}/nutcracker
%config(noreplace) %{_confdir}/nutcracker
%endif

%if !%{disable_perl}
%files pmda-oracle -f pmda-oracle.list
%{_pmdasexecdir}/oracle
%config(noreplace) %{_confdir}/oracle
%endif

%if !%{disable_perl}
%files pmda-pdns -f pmda-pdns.list
%{_pmdasexecdir}/pdns
%endif

%if !%{disable_perl}
%files pmda-postfix -f pmda-postfix.list
%{_pmdasexecdir}/postfix
%endif

%if !%{disable_postgresql}
%files pmda-postgresql
%{_pmdasdir}/postgresql
%{_pmdasexecdir}/postgresql
%dir %{_confdir}/postgresql
%config(noreplace) %{_confdir}/postgresql/pmdapostgresql.conf
%endif

%if !%{disable_perl}
%files pmda-redis -f pmda-redis.list
%dir %{_confdir}/redis
%config(noreplace) %{_confdir}/redis/redis.conf
%{_pmdasexecdir}/redis
%endif

%if !%{disable_perl}
%files pmda-rsyslog -f pmda-rsyslog.list
%{_pmdasexecdir}/rsyslog
%endif

%if !%{disable_perl}
%files pmda-samba -f pmda-samba.list
%{_pmdasexecdir}/samba
%endif

%if !%{disable_snmp}
%files pmda-snmp -f pmda-snmp.list
%dir %{_confdir}/snmp
%config(noreplace) %{_confdir}/snmp/snmp.conf
%{_pmdasexecdir}/snmp
%endif

%if !%{disable_perl}
%files pmda-slurm -f pmda-slurm.list
%{_pmdasexecdir}/slurm
%endif

%if !%{disable_perl}
%files pmda-zimbra -f pmda-zimbra.list
%{_pmdasexecdir}/zimbra
%endif

%files pmda-dm -f pmda-dm.list
%{_pmdasexecdir}/dm
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
%files pmda-gluster -f pmda-gluster.list
%{_pmdasexecdir}/gluster

%files pmda-zswap -f pmda-zswap.list
%{_pmdasexecdir}/zswap

%files pmda-unbound -f pmda-unbound.list
%{_pmdasexecdir}/unbound

%files pmda-mic -f pmda-mic.list
%{_pmdasexecdir}/mic

%files pmda-haproxy -f pmda-haproxy.list
%dir %{_confdir}/haproxy
%config(noreplace) %{_confdir}/haproxy/haproxy.conf
%{_pmdasexecdir}/haproxy

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

%files pmda-lmsensors -f pmda-lmsensors.list
%{_pmdasexecdir}/lmsensors

%files pmda-netcheck -f pmda-netcheck.list
%dir %{_confdir}/netcheck
%config(noreplace) %{_confdir}/netcheck/netcheck.conf
%{_pmdasexecdir}/netcheck

%endif # !%%{disable_python3}

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

%if !%{disable_resctrl}
%files pmda-resctrl -f pmda-resctrl.list
%{_libexecdir}/pcp/pmdas/resctrl/Install
%{_libexecdir}/pcp/pmdas/resctrl/Remove
%{_libexecdir}/pcp/pmdas/resctrl/domain.h
%{_libexecdir}/pcp/pmdas/resctrl/help
%{_libexecdir}/pcp/pmdas/resctrl/pmda_resctrl.so
%{_libexecdir}/pcp/pmdas/resctrl/pmdaresctrl
%{_libexecdir}/pcp/pmdas/resctrl/pmns
%{_libexecdir}/pcp/pmdas/resctrl/root
%{_unitdir}/sys-fs-resctrl.mount
%dir %{_libexecdir}/pcp/pmdas/resctrl
%endif

%files pmda-uwsgi -f pmda-uwsgi.list
%config(noreplace) %{_confdir}/uwsgi/uwsgi.conf
%{_libexecdir}/pcp/pmdas/uwsgi/Install
%{_libexecdir}/pcp/pmdas/uwsgi/Remove
%{_libexecdir}/pcp/pmdas/uwsgi/pmdauwsgi.python
%dir %{_confdir}/uwsgi
%dir %{_libexecdir}/pcp/pmdas/uwsgi

%if !%{disable_json}
%files pmda-json -f pmda-json.list
%{_pmdasexecdir}/json
%config(noreplace) %{_confdir}/json
%endif

%files pmda-apache -f pmda-apache.list
%{_pmdasexecdir}/apache

%files pmda-amdgpu -f pmda-amdgpu.list
%{_pmdasexecdir}/amdgpu

%files pmda-bash -f pmda-bash.list
%{_pmdasexecdir}/bash

%files pmda-cifs -f pmda-cifs.list
%{_pmdasexecdir}/cifs

%files pmda-cisco -f pmda-cisco.list
%{_pmdasexecdir}/cisco

%files pmda-gfs2 -f pmda-gfs2.list
%{_pmdasexecdir}/gfs2

%files pmda-logger -f pmda-logger.list
%{_pmdasexecdir}/logger

%files pmda-mailq -f pmda-mailq.list
%{_pmdasexecdir}/mailq

%files pmda-mounts -f pmda-mounts.list
%{_pmdasexecdir}/mounts
%config(noreplace) %{_confdir}/mounts

%files pmda-nvidia-gpu -f pmda-nvidia-gpu.list
%{_pmdasexecdir}/nvidia

%files pmda-roomtemp -f pmda-roomtemp.list
%{_pmdasexecdir}/roomtemp

%files pmda-sendmail -f pmda-sendmail.list
%{_pmdasexecdir}/sendmail

%files pmda-shping -f pmda-shping.list
%{_pmdasexecdir}/shping
%config(noreplace) %{_confdir}/shping

%files pmda-smart -f pmda-smart.list
%{_pmdasexecdir}/smart

%files pmda-sockets -f pmda-sockets.list
%{_pmdasexecdir}/sockets

%files pmda-hacluster -f pmda-hacluster.list
%{_pmdasexecdir}/hacluster

%files pmda-summary -f pmda-summary.list
%{_pmdasexecdir}/summary
%config(noreplace) %{_confdir}/summary

%if !%{disable_systemd}
%files pmda-systemd -f pmda-systemd.list
%{_pmdasexecdir}/systemd
%endif

%files pmda-trace -f pmda-trace.list
%{_pmdasexecdir}/trace

%files pmda-weblog -f pmda-weblog.list
%{_pmdasexecdir}/weblog

%if !%{disable_perl}
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
%endif

%if !%{disable_python3}
%files -n python3-pcp -f python3-pcp.list.rpm
%endif

%if !%{disable_qt}
%files gui -f pcp-gui.list
%{_pixmapdir}/pmchart.png
%{_confdir}/pmsnap
%config(noreplace) %{_confdir}/pmsnap/control
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
%endif

%if !%{disable_selinux}
%files selinux -f pcp-selinux.list
%dir %{_selinuxdir}
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
