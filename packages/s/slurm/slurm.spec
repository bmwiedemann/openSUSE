#
# spec file
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


# Check file META in sources: update so_version to (API_CURRENT - API_AGE)
%define so_version 38
%define ver 22.05.5
%define _ver _22_05
%define dl_ver %{ver}
# so-version is 0 and seems to be stable
%define pmi_so 0
%define nss_so 2
%define pmix_so 2
%define ver_major %(ver=%{version}; echo ${ver%.*})

%define pname slurm

%define slurm_testsuite 1

%ifarch i586 %arm s390
ExclusiveArch:  do_not_build
%endif

%if 0%{?suse_version} < 1315
ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version} == 120200
%define base_ver 1702
%define nocheck 1
%endif
%if 0%{?sle_version} == 150000
%define base_ver 1711
%endif
%if 0%{?sle_version} == 150100
%define base_ver 1808
%endif
%if 0%{?sle_version} == 150200
%define base_ver 2002
%endif
%if 0%{?sle_version} == 150300 || 0%{?sle_version} == 150400
%define base_ver 2011
%endif

%if 0%{?suse_version} >= 1500
%define have_sysuser 1
%endif

%if 0%{?base_ver} > 0 && 0%{?base_ver} < %(echo %{_ver} | tr -d _)
%define upgrade 1
%endif

# Build with PMIx only for SLE >= 15.0 and TW
%if 0%{?sle_version} >= 150000 || 0%{suse_version} >= 1550
%{bcond_without pmix}
%else
%{bcond_with pmix}
%endif

%if 0%{?suse_version} >= 1220 || 0%{?sle_version} >= 120000
 %define with_systemd 1
%endif

%if 0%{?suse_version:1} && 0%{?suse_version} <= 1140
 %define comp_at %defattr(-,root,root)
 %undefine python_ver
%else
 %define have_json_c 1
 %define python_ver 3
 %if 0%{?sle_version} >= 150000 || 0%{?is_opensuse}
 %define have_apache_rpm_macros 1
 %endif
%endif

%if 0%{?sle_version} >= 150000 || 0%{?is_opensuse}
%define have_http_parser 1
%endif

# it seems as disabling slurmrestd has no effect on 22.05
%if 0%{?have_http_parser} && 0%{?have_json_c}
%define build_slurmrestd 1
%endif

%if 0
%define have_netloc 1
%endif

%if 0%{?is_opensuse} && 0%{!?sle_version:1}
%define is_factory 1
%endif

%if 0%{?is_factory} || 0%{?sle_version} >= 150000
%define have_hdf5 1
%define have_boolean_deps 1
%define have_lz4 1
%define have_firewalld 1
%endif

%ifarch x86_64
 %define have_libnuma 1
%else
 %ifarch %{ix86}
  %if 0%{?sle_version} >= 120200
   %define have_libnuma 1
  %endif
 %endif
%endif

%if 0%{?with_systemd}
 %define slurm_u %pname
 %define slurm_g %pname
%else
 %define slurm_u daemon
 %define slurm_g root
%endif
%define slurm_uid 120
%define slurmdir %{_rundir}/slurm
%define slurmdescr "SLURM workload manager"

%define libslurm libslurm%{so_version}
%{!?_rundir:%define _rundir /var/run}

%if !0%{?_pam_moduledir:1}
%define _pam_moduledir /%_lib
%endif
%if !0%{?%_pam_secconfdir:1}
%define _pam_secconfdir %_sysconfdir/security
%endif

Name:           %{pname}%{?upgrade:%{_ver}}
Version:        %{ver}
Release:        0
Summary:        Simple Linux Utility for Resource Management
License:        SUSE-GPL-2.0-with-openssl-exception
Group:          Productivity/Clustering/Computing
URL:            https://www.schedmd.com
Source:         https://download.schedmd.com/slurm/%{pname}-%{dl_ver}.tar.bz2
Source1:        slurm-rpmlintrc
Source10:       https://raw.githubusercontent.com/openSUSE/hpc/10c105e/files/slurm/slurmd.xml
Source11:       https://raw.githubusercontent.com/openSUSE/hpc/10c105e/files/slurm/slurmctld.xml
Source12:       https://raw.githubusercontent.com/openSUSE/hpc/10c105e/files/slurm/slurmdbd.xml
# create: tar --owner=nobody --group=nogroup --exclude=*~ -cvzf test_setup.tar.gz test_setup
Source20:       test_setup.tar.gz
Source21:       README_Testsuite.md
Patch0:         Remove-rpath-from-build.patch
Patch2:         pam_slurm-Initialize-arrays-and-pass-sizes.patch
Patch10:        Fix-test-21.41.patch
Patch11:        Fix-test-38.11.patch
Patch12:        Fix-test-32.8.patch
Patch13:        Fix-test-3.13.patch
Patch14:        Keep-logs-of-skipped-test-when-running-test-cases-sequentially.patch
Patch15:        Fix-test7.2-to-find-libpmix-under-lib64-as-well.patch

%{?upgrade:Provides: %{pname} = %{version}}
%{?upgrade:Conflicts: %{pname}}

Requires:       %{name}-config = %{version}
%if 0%{?have_boolean_deps}
Recommends:     (%{name}-munge = %version if munge)
%else
Recommends:     %{name}-munge = %version
%endif
Requires(pre):  %{name}-node = %{version}
Recommends:     %{name}-config-man = %{version}
Recommends:     %{name}-doc = %{version}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  fdupes
%{?have_firewalld:BuildRequires:  firewalld}
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
%if 0%{?have_hdf5}
BuildRequires:  hdf5-devel
%endif
BuildRequires:  libbitmask-devel
BuildRequires:  libcpuset-devel
BuildRequires:  python%{?python_ver}
%if 0%{?have_libnuma}
BuildRequires:  libnuma-devel
%endif
BuildRequires:  mysql-devel >= 5.0.0
BuildRequires:  ncurses-devel
%{?with_pmix:BuildRequires:  pmix-devel}
BuildRequires:  openssl-devel >= 0.9.6
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
%if 0%{?suse_version} > 1310 || 0%{?sle_version}
 %if 0%{?sle_version} >= 120400 && 0%{?sle_version} < 150000
BuildRequires:  infiniband-diags-devel
 %else
BuildRequires:  libibmad-devel
 %endif
BuildRequires:  libibumad-devel
%endif
%if 0%{?suse_version} > 1140
BuildRequires:  libhwloc-devel
%ifarch %{ix86} x86_64
BuildRequires:  freeipmi-devel
%endif
%endif
BuildRequires:  libcurl-devel
%if 0%{?have_json_c}
BuildRequires:  libjson-c-devel
%endif
%if 0%{?have_lz4}
BuildRequires:  liblz4-devel
%endif
BuildRequires:  libssh2-devel
BuildRequires:  libyaml-devel
BuildRequires:  rrdtool-devel
%if 0%{?with_systemd}
%{?have_sysuser:BuildRequires:  sysuser-tools}
%{?systemd_ordering}
BuildRequires:  dejagnu
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)
%else
Requires(post): %insserv_prereq %fillup_prereq
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Obsoletes:      slurm-sched-wiki < %{version}
Obsoletes:      slurmdb-direct < %{version}

%description
SLURM is a fault-tolerant scalable cluster management and job
scheduling system for Linux clusters containing up to 65,536 nodes.
Components include machine status, partition management, job
management, scheduling and accounting modules.

%package doc
Summary:        Documentation for SLURM
Group:          Documentation/HTML
BuildArch:      noarch
%{?upgrade:Provides: %{pname}-doc = %{version}}
%{?upgrade:Conflicts: %{pname}-doc}

%package webdoc
Summary:        Set up SLURM Documentation Server
Group:          Productivity/Clustering/Computing
BuildArch:      noarch
%if 0%{?have_apache_rpm_macros}
BuildRequires:  apache-rpm-macros
%else
%define apache_sysconfdir /etc/apache2
%endif
Requires:       slurm-doc = %{version}
Requires(pre):  apache2

%description webdoc
Set up HTTP server for SLURM configuration.

%description doc
Documentation (HTML) for the SLURM cluster managment software.

%package -n perl-%{name}
Summary:        Perl API to SLURM
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{libperl_requires}
%{perl_requires}
%endif
%{?upgrade:Provides: perl-%{pname} = %{version}}
%{?upgrade:Conflicts: perl-%{pname}}

%description -n perl-%{name}
This package includes the Perl API to provide an interface to SLURM
through Perl.

%package -n %{libslurm}
# the .so number of libslurm is bumped with each major release
# therefore no need for a version string for Leap/SLE upgrade packages
Summary:        Libraries for SLURM
Group:          System/Libraries
Requires:       %{name}-config
Conflicts:      %{name}-config < %{ver_major}
Conflicts:      %{name}-config > %{ver_major}.99
Provides:       libslurm = %{version}
Conflicts:      libslurm

%description -n %{libslurm}
This package contains the library needed to run programs dynamically linked
with SLURM.

%package -n libpmi%{pmi_so}%{?upgrade:%{_ver}}
Summary:        SLURM PMI Library
Group:          System/Libraries
%{?upgrade:Provides: libpmi%{pmi_so} = %{version}}
%{?upgrade:Conflicts: libpmi%{pmi_so}}

%description -n libpmi%{pmi_so}%{?upgrade:%{_ver}}
This package contains the library needed to run programs dynamically linked
with SLURM.

%package -n libnss_%{pname}%{nss_so}%{?upgrade:%{_ver}}
Summary:        NSS Plugin for SLURM
Group:          System/Libraries
%{?upgrade:Provides: libnss_%{pname}%{nss_so} = %{version}}
%{?upgrade:Conflicts: libnss_%{pname}%{nss_so}}

%description -n libnss_%{pname}%{nss_so}%{?upgrade:%{_ver}}
libnss_slurm is an optional NSS plugin that permits password and group
resolution for a job on a compute node to be serviced through the local
slurmstepd process.

%package devel
Summary:        Development package for SLURM
Group:          Development/Libraries/C and C++
Requires:       %{libslurm} = %{version}
Requires:       %{name} = %{version}
Requires:       libpmi%{pmi_so} = %{version}
%{?upgrade:Provides: %{pname}-devel = %{version}}
%{?upgrade:Conflicts: %{pname}-devel}

%description devel
This package includes the header files for the SLURM API.

%package auth-none
Summary:        SLURM auth NULL implementation (no authentication)
Group:          Productivity/Clustering/Computing
Requires:       %{name} = %{version}
%{?upgrade:Provides: %{pname}-auth-none = %{version}}
%{?upgrade:Conflicts: %{pname}-auth-none}

%description auth-none
This package cobtains the SLURM NULL authentication module.

%package munge
Summary:        SLURM authentication and crypto implementation using Munge
Group:          Productivity/Clustering/Computing
Requires:       %{name}-plugins = %{version}
Requires:       munge
BuildRequires:  munge-devel
Obsoletes:      %{name}-auth-munge < %{version}
Provides:       %{name}-auth-munge = %{version}
%{?upgrade:Provides: %{pname}-munge = %{version}}
%{?upgrade:Conflicts: %{pname}-munge}

%description munge
This package contains the SLURM authentication module for Chris Dunlap's Munge.

%package sview
Summary:        SLURM graphical interface
Group:          Productivity/Clustering/Computing
%{?upgrade:Provides: %{pname}-sview = %{version}}
%{?upgrade:Conflicts: %{pname}-sview}

%description sview
sview is a graphical user interface to get and update state information for
jobs, partitions, and nodes managed by SLURM.

%package slurmdbd
Summary:        SLURM database daemon
Group:          Productivity/Clustering/Computing
Requires:       %{name}-config = %{version}
Requires:       %{name}-plugins = %{version}
Requires:       %{name}-sql = %{version}
%if 0%{?suse_version} > 1310
Recommends:     mariadb
%endif
%if 0%{?have_boolean_deps}
Recommends:     (%{name}-munge = %version if munge)
%else
Recommends:     %{name}-munge = %version
%endif
%if 0%{?with_systemd}
%{?systemd_ordering}
%else
Requires(post): %insserv_prereq %fillup_prereq
%endif
Obsoletes:      slurm-sched-wiki < %{version}
Obsoletes:      slurmdb-direct < %{version}
%{?upgrade:Provides: %{pname}-slurmdbd = %{version}}
%{?upgrade:Conflicts: %{pname}-slurmdb}

%description slurmdbd
The SLURM database daemon provides accounting of jobs in a database.

%package sql
Summary:        Slurm SQL support
Group:          Productivity/Clustering/Computing
%{?upgrade:Provides: %{pname}-sql = %{version}}
%{?upgrade:Conflicts: %{pname}-sql}

%description sql
Contains interfaces to MySQL for use by SLURM.

%package plugins
Summary:        SLURM plugins (loadable shared objects)
Group:          Productivity/Clustering/Computing
%{?upgrade:Provides: %{pname}-plugins = %{version}}
%{?upgrade:Conflicts: %{pname}-plugins}
%if %{with pmix}
Requires:       libpmix%{pmix_so}
Requires:       pmix
%endif

%description plugins
This package contains the SLURM plugins (loadable shared objects)

%package plugin-ext-sensors-rrd
Summary:        SLURM ext_sensors/rrd Plugin (loadable shared objects)
Group:          Productivity/Clustering/Computing
%{?upgrade:Provides: %{pname}-plugin-ext-sensors-rrd = %{version}}
%{?upgrade:Conflicts: %{pname}-plugin-ext-sensors-rrd}
Requires:       %{name}-plugins = %{version}

%description plugin-ext-sensors-rrd
This package contains the ext_sensors/rrd plugin used to read data
using RRD, a tool that creates and manages a linear database for
sampling and logging data.

%package torque
Summary:        Wrappers for transitition from Torque/PBS to SLURM
Group:          Productivity/Clustering/Computing
Requires:       perl-%{name} = %{version}
Requires:       perl-Switch
Provides:       torque-client
%{?upgrade:Provides: %{pname}-torque = %{version}}
%{?upgrade:Conflicts: %{pname}-torque}

%description torque
Wrapper scripts for aiding migration from Torque/PBS to SLURM.

%package openlava
Summary:        Wrappers for transitition from OpenLava/LSF to Slurm
Group:          Productivity/Clustering/Computing
Requires:       perl-%{name} = %{version}
%{?upgrade:Provides: %{pname}-openlava = %{version}}
%{?upgrade:Conflicts: %{pname}-openlava}

%description openlava
Wrapper scripts for aiding migration from OpenLava/LSF to Slurm

%package seff
Summary:        Mail tool that includes job statistics in user notification email
Group:          Productivity/Clustering/Computing
Requires:       perl-%{name} = %{version}
%{?upgrade:Provides: %{pname}-seff = %{version}}
%{?upgrade:Conflicts: %{pname}-seff}

%description seff
Mail program used directly by the SLURM daemons. On completion of a job,
it waits for accounting information to be available and includes that
information in the email body.

%package sjstat
Summary:        Perl tool to print SLURM job state information
Group:          Productivity/Clustering/Computing
Requires:       %{name} = %{version}
%{?upgrade:Provides: %{pname}-sjstat = %{version}}
%{?upgrade:Conflicts: %{pname}-sjstat}
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description sjstat
This package contains a Perl tool to print SLURM job state information.

%package pam_slurm
Summary:        PAM module for restricting access to compute nodes via SLURM
Group:          Productivity/Clustering/Computing
Requires:       %{name}-node = %{version}
%{?upgrade:Provides: %{pname}-pam_slurm = %{version}}
%{?upgrade:Conflicts: %{pname}-pam_slurm}
BuildRequires:  pam-devel

%description pam_slurm
This module restricts access to compute nodes in a cluster where the Simple
Linux Utility for Resource Managment (SLURM) is in use. Access is granted
to root, any user with an SLURM-launched job currently running on the node,
or any user who has allocated resources on the node according to the SLURM.

%package lua
Summary:        Lua API for SLURM
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
%{?upgrade:Provides: %{pname}-lua = %{version}}
%{?upgrade:Conflicts: %{pname}-lua}
BuildRequires:  lua-devel

%description lua
This package includes the Lua API to provide an interface to SLURM
through Lua.

%package rest
Summary:        Slurm REST API Interface
Group:          Productivity/Clustering/Computing
Requires:       %{name}-config = %{version}
%if 0%{?have_http_parser}
BuildRequires:  http-parser-devel
%endif
%if 0%{?have_boolean_deps}
Recommends:     (%{name}-munge = %version if munge)
%else
Recommends:     %{name}-munge = %version
%endif
%{?upgrade:Provides: %{pname}-rest = %{version}}
%{?upgrade:Conflicts: %{pname}-rest}

%description rest
This package provides the interface to SLURM via REST API.

%package node
Summary:        Minimal slurm node
Group:          Productivity/Clustering/Computing
Requires:       %{name}-config = %{version}
Requires:       %{name}-plugins = %{version}
%if 0%{?have_boolean_deps}
Recommends:     (%{name}-munge = %version if munge)
%else
Recommends:     %{name}-munge = %version
%endif
%{?with_pmix:Recommends:     pmix-devel}
%if 0%{?with_systemd}
%{?systemd_ordering}
%else
Requires(post): %insserv_prereq %fillup_prereq
%endif
%{?upgrade:Provides: %{pname}-node = %{version}}
%{?upgrade:Conflicts: %{pname}-node}

%description node
This package contains just the minmal code to run a compute node.

%package config
Summary:        Config files and directories for slurm services
Group:          Productivity/Clustering/Computing
Requires:       logrotate
BuildArch:      noarch
%if 0%{?suse_version} <= 1140
Requires(pre):  pwdutils
%else
Requires(pre):  shadow
%endif
%if 0%{?with_systemd}
%{?systemd_ordering}
%endif
%{?upgrade:Provides: %{pname}-config = %{version}}
%{?upgrade:Conflicts: %{pname}-config}

%description config
This package contains the slurm config files necessary direcories
for the slurm daemons.

%package config-man
Summary:        Config files and directories for slurm services
Group:          Documentation/Man
BuildArch:      noarch
%{?upgrade:Provides: %{pname}-config-man = %{version}}
%{?upgrade:Conflicts: %{pname}-config-man}

%description config-man
Man pages for the SLURM cluster managment software config files.

%package hdf5
Summary:        Store accounting data in hdf5
Group:          Productivity/Clustering/Computing

%description hdf5
Plugin to store accounting in the hdf5 file format. This plugin has to be
activated in the slurm configuration. Includes also utility the program
sh5utils to merge this hdf5 files or extract data from them.

%package cray
Summary:        Cray specific plugins
Group:          Productivity/Clustering/Computing

%description cray
Plugins for specific cray hardware, includes power and knl node management.
Contains also cray specific documentation.

# Certain packages are not shipped with SLE.
%define ts_depends %{?sle_version:Recommends}%{!?sle_version:Requires}

%package testsuite
Summary:        Regression tests from Slurm sources
Group:          Productivity/Clustering/Computing
Requires:       %{name} = %version
Requires:       %{name}-auth-none = %version
Requires:       %{name}-cray = %version
Requires:       %{name}-devel = %version
%{?have_hdf5:%ts_depends:     %{name}-hdf5 = %version}
Requires:       %{name}-lua = %version
Requires:       %{name}-munge = %version
Requires:       %{name}-node = %version
Requires:       %{name}-openlava = %version
Requires:       %{name}-rest = %version
Requires:       %{name}-seff = %version
Requires:       %{name}-sjstat = %version
Requires:       %{name}-slurmdbd = %version
Requires:       %{name}-sql = %version
Requires:       %{name}-torque = %version
Requires:       mariadb
%{?with_pmix:Requires:       pmix-devel}
Requires:       bind-utils
Requires:       bzip2
Requires:       expect
Requires:       gcc-c++
Requires:       libnuma-devel
%ts_depends:     openmpi4-gnu-hpc-devel
Requires:       pdsh
Requires:       perl-%{name} = %version
Requires:       sudo
Requires:       tar
Requires:       config(pam)
BuildRequires:  sudo

%description testsuite
NOTE: THIS PACKAGE IS FOR TESTING PURPOSES ONLY. IT REQUIRES A
DEDICATED TESTING ENVIRONMENT.

DO NOT INSTALL ON A PRODUCTION SYSTEM!

Slurm provides a test set implemented as 'expect' scripts.
Not all of the tests are expected to pass, some require a modified
configuration. This test package is meant for internal purposes.
Do not run test suite and file bug reports for each failed test!

%prep
%setup -q -n %{pname}-%{dl_ver}
%patch0 -p1
#%%patch1 -p1
%patch2 -p1
#%%patch3 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%if 0%{?python_ver} < 3
# Workaround for wrongly flagged python3 to keep SLE-11-SP4 building
mkdir -p mybin; ln -s /usr/bin/python2 mybin/python3
%endif

%build
# needed as slurm works that way bsc#1200030
export SUSE_ZNOW=0

# To make stripped object files work which we ship in the
# testsuite package we need to build with -ffat-lto-objects.
# This should not affect anything as we do not ship static
# libraries and object files - except for the testsuite.
%if "%{?_lto_cflags}" != ""
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%endif

autoreconf
[ -e $(pwd)/mybin ] && PATH=$(pwd)/mybin:$PATH
%configure --enable-shared \
           --disable-static \
           --without-rpath \
           --without-datawarp \
           --with-shared-libslurm \
           --with-pam_dir=%_pam_moduledir \
           %{?with_pmix:--with-pmix=%_prefix/} \
%if 0%{!?build_slurmrestd:1}
           --disable-slurmrestd \
%endif
	   --with-yaml \
%{!?have_netloc:--without-netloc} \
           --sysconfdir=%{_sysconfdir}/%{pname} \
%{!?have_hdf5:--without-hdf5} \
%{!?have_lz4:--without-lz4} \
%{!?have_json_c:--without-json}

make %{?_smp_mflags}

%install
[ -e $(pwd)/mybin ] && PATH=$(pwd)/mybin:$PATH
%make_install
make install-contrib DESTDIR=%{buildroot} PERL_MM_PARAMS="INSTALLDIRS=vendor"

%if 0%{?with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 etc/slurmd.service etc/slurmdbd.service etc/slurmctld.service %{buildroot}%{_unitdir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcslurmd
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcslurmdbd
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcslurmctld
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}/
cat <<-EOF > %{buildroot}/%{_tmpfilesdir}/%{pname}.conf
	# Create a directory with permissions 0700 owned by user slurm, group slurm
	d %{_rundir}/slurm 0700 slurm slurm
EOF
chmod 0644 %{buildroot}/%{_tmpfilesdir}/%{pname}.conf
%else
install -D -m755 etc/init.d.slurm    %{buildroot}%{_initrddir}/slurm
install -D -m755 etc/init.d.slurmdbd %{buildroot}%{_initrddir}/slurmdbd
ln -sf %{_initrddir}/slurm %{buildroot}%{_sbindir}/rcslurm
ln -sf %{_initrddir}/slurmdbd %{buildroot}%{_sbindir}/rcslurmdbd
%endif
mkdir -p %{buildroot}%{_localstatedir}/spool/slurm

install -D -m644 etc/cgroup.conf.example %{buildroot}/%{_sysconfdir}/%{pname}/cgroup.conf
install -D -m644 etc/slurm.conf.example %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf.example
install -D -m600 etc/slurmdbd.conf.example %{buildroot}/%{_sysconfdir}/%{pname}/slurmdbd.conf
install -D -m755 contribs/sjstat %{buildroot}%{_bindir}/sjstat
install -D -m755 contribs/sgather/sgather %{buildroot}%{_bindir}/sgather
%if 0%{?have_firewalld}
install -D -m644 %{S:10} %{buildroot}/%{_prefix}/lib/firewalld/services/slurmd.xml
install -D -m644 %{S:11} %{buildroot}/%{_prefix}/lib/firewalld/services/slurmctld.xml
install -D -m644 %{S:12} %{buildroot}/%{_prefix}/lib/firewalld/services/slurmdbd.xml
%endif

cat <<EOF >%{buildroot}%{_sysconfdir}/%{pname}/plugstack.conf
include %{_sysconfdir}/%{pname}/plugstack.conf.d/*.conf
EOF

mkdir -p %{buildroot}%{_sysconfdir}/%{pname}/plugstack.conf.d

cp contribs/pam_slurm_adopt/README ../README.pam_slurm_adopt
cp  contribs/pam/README ../README.pam_slurm
# remove static pam libs
rm -v %{buildroot}%{_pam_moduledir}/*la
# change slurm.conf for our needs
head -n -2 %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf.example | grep -v ReturnToService > %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf
sed -i 's#\(StateSaveLocation=\).*#\1%_localstatedir/lib/slurm#'  %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf
sed -i 's#^\(SlurmdPidFile=\).*$#\1%{_localstatedir}/run/slurm/slurmd.pid#' %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf
sed -i 's#^\(SlurmctldPidFile=\).*$#\1%{_localstatedir}/run/slurm/slurmctld.pid#' %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf
sed -i 's#^\(SlurmdSpoolDir=\)/.*#\1%{_localstatedir}/spool/slurm#' %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf
sed -i -e '/^ControlMachine=/i# Ordered List of Control Nodes' \
    -e 's#ControlMachine=\(.*\)$#SlurmctldHost=\1(10.0.10.20)#' \
    -e 's#BackupController=.*#SlurmctldHost=linux1(10.0.10.21)#' \
    -e '/.*ControlAddr=.*/d' \
    -e '/.*BackupAddr=.*/d'  %{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf
cat >>%{buildroot}/%{_sysconfdir}/%{pname}/slurm.conf <<EOF
# Potential exploit mitigation CVE-2022-29500
# When upgrading from a version without this fix
# enable only after all daemons have been upgraded
CommunicationParameters=block_null_hash
# SUSE default configuration
PropagateResourceLimitsExcept=MEMLOCK
NodeName=linux State=UNKNOWN
PartitionName=normal Nodes=linux Default=YES MaxTime=24:00:00 State=UP
EOF
# change slurmdbd.conf for our needs
sed -i 's@LogFile=/var/log/slurm/slurmdbd.log@LogFile=/var/log/slurmdbd.log@'\
 %{buildroot}/%{_sysconfdir}/%{pname}/slurmdbd.conf
sed -i -e "s@PidFile=.*@PidFile=%{_localstatedir}/run/slurm/slurmdbd.pid@" \
 %{buildroot}/%{_sysconfdir}/%{pname}/slurmdbd.conf
# manage local state dir and a remote states save location
mkdir -p %{buildroot}/%_localstatedir/lib/slurm
%if 0%{?with_systemd}
sed -i -e "s@PIDFile=.*@PIDFile=%{_localstatedir}/run/slurm/slurmctld.pid@" \
 -e "s@After=.*@After=network.target munge.service remote-fs.target@" \
 %{buildroot}/%{_unitdir}/slurmctld.service
sed -i -e "s@PIDFile=.*@PIDFile=%{_localstatedir}/run/slurm/slurmd.pid@" \
 %{buildroot}/%{_unitdir}/slurmd.service
sed -i -e "s@PIDFile=.*@PIDFile=%{_localstatedir}/run/slurm/slurmdbd.pid@" \
       -e 's@After=\(.*\)@After=\1 mariadb.service@' \
 %{buildroot}/%{_unitdir}/slurmdbd.service
%if 0%{?have_sysuser}
[ -e /usr/bin/bash ] && BASH_BIN=/usr/bin/bash || BASH_BIN=/bin/bash
echo "u %slurm_u %{slurm_uid} \"%slurmdescr\" %{slurmdir} ${BASH_BIN}" > system-user-%{pname}.conf
%sysusers_generate_pre system-user-%{pname}.conf %{pname} system-user-%{pname}.conf
install -D -m 644 system-user-%{pname}.conf %{buildroot}%{_sysusersdir}/system-user-%{pname}.conf
%endif
%endif

# Delete static files:
rm -rf %{buildroot}/%{_libdir}/slurm/*.{a,la} \
       %{buildroot}/%{_libdir}/*.la \
       %{buildroot}/%_lib/security/*.la

rm %{buildroot}/%{perl_archlib}/perllocal.pod \
   %{buildroot}/%{perl_vendorarch}/auto/Slurm/.packlist \
   %{buildroot}/%{perl_vendorarch}/auto/Slurmdb/.packlist

# Remove Cray specific binaries
rm -f %{buildroot}/%{_sbindir}/capmc_suspend \
      %{buildroot}/%{_sbindir}/capmc_resume

# Build man pages that are generated directly by the tools
%{buildroot}%{_bindir}/sjobexitmod --roff > %{buildroot}/%{_mandir}/man1/sjobexitmod.1
%{buildroot}%{_bindir}/sjstat --roff > %{buildroot}/%{_mandir}/man1/sjstat.1

# avoid conflicts with other packages, make wrapper unique
mv %{buildroot}/%{_bindir}/mpiexec %{buildroot}/%{_bindir}/mpiexec.slurm

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo '%{_libdir}/slurm' > %{buildroot}/etc/ld.so.conf.d/slurm.conf
chmod 644 %{buildroot}/etc/ld.so.conf.d/slurm.conf

# Make pkg-config file
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat > %{buildroot}/%{_libdir}/pkgconfig/slurm.pc <<EOF
includedir=%{_prefix}/include
libdir=%{_libdir}

Cflags: -I\${includedir}
Libs: -L\${libdir} -lslurm
Description: Slurm API
Name:           %{pname}
Version:        %{version}
EOF

# Enable rotation of log files

mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d/
for service in slurmd slurmctld slurmdbd ; do
cat <<EOF > %{buildroot}/%{_sysconfdir}/logrotate.d/${service}.conf
/var/log/${service}.log {
    compress
    dateext
    missingok
    nocreate
    notifempty
    maxage 365
    rotate 99
    copytruncate
    postrotate
        pgrep ${service} && killall -SIGUSR2 ${service} || exit 0
    endscript
}
EOF
done
mkdir -p %{buildroot}/%{apache_sysconfdir}/conf.d
cat > %{buildroot}/%{apache_sysconfdir}/conf.d/slurm.conf <<EOF
Alias /slurm/ "/usr/share/doc/slurm-%{ver}/html/"
<Directory "/usr/share/doc/slurm-%{ver}/html/">
        AllowOverride None
        DirectoryIndex slurm.html
        # Controls who can get stuff from this server.
        <IfModule !mod_access_compat.c>
                Require all granted
        </IfModule>
        <IfModule mod_access_compat.c>
                Order allow,deny
                Allow from all
        </IfModule>
</Directory>
EOF
cat > %{buildroot}/%{_sysconfdir}/%{pname}/nss_slurm.conf <<EOF
## Optional config for libnss_slurm
## Specify if different from default
# SlurmdSpoolDir /var/spool/slurmd
## Specify if does not match hostname
# NodeName myname
EOF

# Install testsuite
%if 0%{?slurm_testsuite}
# bug in testsuite
ln -sf %{_libdir}/libslurm.so %{buildroot}%{_libdir}/slurm/libslurm.so

mkdir -p %{buildroot}/srv/slurm-testsuite
cd testsuite/expect
filelist="$(grep '#include' *.c | sed -ne 's/.*:#include *\"\([^\"]*\)\".*/\1/p' | sort | uniq)"
while true; do
    oldfilelist=$filelist; tlist=""
    for i in $filelist; do
        nlist=" $(grep '#include' ../../$i | sed -ne 's/#include *\"\([^\"]*\)\".*/\1/p')"
        tlist+=" $(for j in $nlist; do [ -e ../../$j ] && echo $j || true; done)"
    done
    filelist="$(for i in $filelist $tlist; do echo $i; done | sort | uniq)"
    [ "$filelist" = "$oldfilelist" ] && break
done
filelist+=" $(grep -Ehor '\{*build_dir\}*[^ ]*\.[oa]' | sed -e "s@{*build_dir}*/@@" | sort | uniq)"
cd -
newlist=""
for i in $filelist; do
    dir=$(dirname $i)
    [ -d %{buildroot}/srv/slurm-testsuite/$dir ] || mkdir -p %{buildroot}/srv/slurm-testsuite/$dir
    cp -a $i %{buildroot}/srv/slurm-testsuite/$dir/
done
mkdir -p %{buildroot}/srv/slurm-testsuite/testsuite/expect
cp -ax testsuite/expect %{buildroot}/srv/slurm-testsuite/testsuite/
cat > %{buildroot}/srv/slurm-testsuite/testsuite/expect/globals.local <<EOF
set slurm_dir "/usr"
set build_dir "/srv/slurm-testsuite"
set src_dir "/srv/slurm-testsuite"
if {[ catch { set mpicc [ exec which mpicc 2>/dev/null ]}]} {
  set mpicc ""
}
set testsuite_user "auser"
#set testsuite_cleanup_on_failure false
EOF
mkdir -p %{buildroot}/srv/slurm-testsuite/shared
mkdir -p %{buildroot}%_localstatedir/lib/slurm/shared
cd %{buildroot}/srv/slurm-testsuite
find -type f -name "*.[ao]" -print | while read f; do
  # drop non-deterministic lto bits from .o files
  strip -p --discard-locals -R .gnu.lto_* -R .gnu.debuglto_* -N __gnu_lto_v1 $f
done
%if 0%{?suse_version} >= 1500
%define tar_sort --sort=name
%endif
tar --group=%slurm_g --owner=%slurm_u \
  %{?tar_sort} --mtime="@${SOURCE_DATE_EPOCH:-`date +%%s`}" --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
  -cjf /tmp/slurmtest.tar.bz2 *
cd -
rm -rf %{buildroot}/srv/slurm-testsuite
mkdir -p %{buildroot}/srv/slurm-testsuite
mkdir -p %{buildroot}/%{_datadir}/%{name}
mv /tmp/slurmtest.tar.bz2 %{buildroot}/%{_datadir}/%{name}

mkdir -p %{buildroot}/etc/sudoers.d
echo "slurm ALL=(auser) NOPASSWD:ALL" > %{buildroot}/etc/sudoers.d/slurm
chmod 0440 %{buildroot}/etc/sudoers.d/slurm

SLURMD_SERVICE=%{buildroot}%_sysconfdir/systemd/system/slurmd.service
mkdir -p `dirname $SLURMD_SERVICE`
cp %{buildroot}/%_unitdir/slurmd.service  $SLURMD_SERVICE
if grep -qE "^LimitNPROC" $SLURMD_SERVICE; then
    sed -i -e '/LimitNPROC/s@=.*@=infinity@' $SLURMD_SERVICE
else
    sed -i -e '/LimitSTACK/aLimitNPROC=infinity' $SLURMD_SERVICE
fi
if grep -qE "^LimitNOFILE" $SLURMD_SERVICE; then
    sed -i -e '/LimitNOFILE/s@=.*@=131072:infinity@' $SLURMD_SERVICE
else
    sed -i -e '/LimitSTACK/aLimitNOFILE=131072:infinity' $SLURMD_SERVICE
fi
sed -i -e '/ExecStart/aExecStartPre=/bin/bash -c "for i in 0 1 2 3; do test -e /dev/nvidia$i || mknod /dev/nvidia$i c 10 $((i+2)); done"' $SLURMD_SERVICE

tar -xzf %{S:20}
mkdir -p %{buildroot}%{_pam_secconfdir}/limits.d
mv test_setup/slurm.conf.limits %{buildroot}%_pam_secconfdir/limits.d/slurm.conf
%if 0%{?sle_version} < 150200
sed -i -e '/hard[[:space:]]*nofile/s@unlimited@1048576@' %{buildroot}%_pam_secconfdir/limits.d/slurm.conf
%endif

mkdir -p %{buildroot}/root
mv test_setup/setup-testsuite.sh %{buildroot}/root

mkdir -p %{buildroot}/srv/slurm-testsuite/config/plugstack.conf.d
cp %{S:21} .
%endif

%fdupes -s %{buildroot}
# For testsuite - do after fdupes!
[ -d test_setup -a -d %{buildroot}/srv/slurm-testsuite/config ] && \
    mv test_setup/* %{buildroot}/srv/slurm-testsuite/config

# Temporary - remove when build is fixed upstream.
%if !0%{?build_slurmrestd}
rm -f %{buildroot}%{_mandir}/man8/slurmrestd.*
rm -f %{buildroot}%{_libdir}/slurm/openapi_*.so
rm -f %{buildroot}%{_libdir}/slurm/rest_auth_*.so
%endif

%check
%{!?nocheck:make check}

%define fixperm() [ $1 -eq 1 -a -e %2 ] && /bin/chmod %1 %2

%if 0%{!?service_del_postun_without_restart:1}
%define service_del_postun_without_restart() %{expand:%%service_del_postun -n %{**}}
%endif

%pre
%if 0%{?with_systemd}
%service_add_pre slurmctld.service
%endif

%post
%if 0%{?with_systemd}
%service_add_post slurmctld.service
%else
%fillup_and_insserv slurm
%endif

%preun
%if 0%{?with_systemd}
%service_del_preun slurmctld.service
%endif

%postun
%if 0%{?with_systemd}
%service_del_postun_without_restart slurmctld.service
%else
%insserv_cleanup
%endif

%if 0%{?with_systemd}
%pre slurmdbd
%service_add_pre slurmdbd.service
%endif

%post slurmdbd
%{fixperm 0600 %{_sysconfdir}/%{pname}/slurmdbd.conf}
%{fixperm 0600 %{_sysconfdir}/%{pname}/slurmdbd.conf.example}
%if 0%{?with_systemd}
%service_add_post slurmdbd.service
%else
%fillup_and_insserv slurmdbd
%endif

%preun slurmdbd
%if 0%{?with_systemd}
%service_del_preun slurmdbd.service
%else
%stop_on_removal slurmdbd
%endif

%postun slurmdbd
%{fixperm 0600 %{_sysconfdir}/%{pname}/slurmdbd.conf}
%{fixperm 0600 %{_sysconfdir}/%{pname}/slurmdbd.conf.example}
%if 0%{?with_systemd}
%service_del_postun_without_restart slurmdbd.service
%else
%restart_on_update slurmdbd
%insserv_cleanup
%endif

%pre node
%if 0%{?with_systemd}
%service_add_pre slurmd.service
%endif

%post node
%if 0%{?with_systemd}
%service_add_post slurmd.service
%endif

%preun node
%if 0%{?with_systemd}
%service_del_preun slurmd.service
%else
%stop_on_removal slurmd
%endif

%postun node
%if 0%{?with_systemd}
%service_del_postun_without_restart slurmd.service
%else
%restart_on_update slurmd
%insserv_cleanup
%endif

%pre config %{?have_sysuser:-f %{pname}.pre}
%if 0%{!?have_sysuser:1}
getent group %slurm_g >/dev/null || groupadd -r %slurm_g
getent passwd %slurm_u >/dev/null || useradd -r -g %slurm_g -d %slurmdir -s /bin/bash -c %{slurmdescr} %slurm_u
[ -d %{_localstatedir}/spool/slurm ] && /bin/chown -h %slurm_u:%slurm_g %{_localstatedir}/spool/slurm
exit 0
%endif

%post config
%if 0%{?with_systemd}
%if 0%{?tmpfiles_create:1}
  %tmpfiles_create slurm.conf
%else
  systemd-tmpfiles --create slurm.conf
%endif
%endif

%post -n %{libslurm} -p /sbin/ldconfig
%postun -n %{libslurm} -p /sbin/ldconfig

%post -n  libpmi%{pmi_so}%{?upgrade:%{_ver}} -p /sbin/ldconfig
%postun -n  libpmi%{pmi_so}%{?upgrade:%{_ver}} -p /sbin/ldconfig

%post -n libnss_%{pname}%{nss_so}%{?upgrade:%{_ver}} -p /sbin/ldconfig
%postun -n libnss_%{pname}%{nss_so}%{?upgrade:%{_ver}} -p /sbin/ldconfig

%post testsuite
rm -rf /srv/slurm-testsuite/src /srv/slurm-testsuite/testsuite /srv/slurm-testsuite/config.h
runuser -u %slurm_u -- tar --same-owner -C /srv/slurm-testsuite -xjf %{_datadir}/%{name}/slurmtest.tar.bz2

%preun testsuite
rm -rf /srv/slurm-testsuite/src /srv/slurm-testsuite/testsuite \
   /srv/slurm-testsuite/slurm /srv/slurm-testsuite/shared \
   /srv/slurm-testsuite/config.h

%{!?nil:
# On update the %%postun code of the old package restarts the
# service. This breaks in case the ABI between slurm and its
# plugins has changed as updates are not atomic. Since we cannot
# fix the old scripts we need these macros as a workaround.
# They should be removed at some point.
# Do pretrans in lua: https://fedoraproject.org/wiki/Packaging:Scriptlets
}
%define _test_rest() %{?with_systemd: os.remove("/run/%{1}.rst")
 if os.execute() and os.getenv("YAST_IS_RUNNING") ~= "instsys" then
  local handle = io.popen("systemctl is-active %{1} 2>&1")
  local str = handle:read("*a"); handle:close()
  str = string.gsub(str, '^%%s+', '')
  str = string.gsub(str, '%%s+$', '')
  str = string.gsub(str, '[\\n\\r]+', ' ')
  if str == "active" then
    local file = io.open("/run/%{1}.rst","w"); file:close()
  end
 end
}
%define _rest() %{?with_systemd:[ -e /run/%{1}.rst ] && { systemctl status %{1} &>/dev/null || systemctl restart %{1}; }; rm -f /run/%{1}.rst;}
%{!?nil:
# Until a posttrans macro has been added to macros.systemd, we need this
# Do NOT delete the line breaks in the macro definition: they help
# to cope with different versions of the %%_restart_on_update.
}
%define _res_update() %{?with_systemd:
 %{expand:%%_restart_on_update %{?*}}
}

%pretrans -p <lua>
%_test_rest slurmctld

%pretrans node -p <lua>
%_test_rest slurmd

%pretrans slurmdbd -p <lua>
%_test_rest slurmdbd

%posttrans
%_res_update slurmctld
%_rest slurmctld

%posttrans node
%_res_update slurmd
%_rest slurmd

%posttrans slurmdbd
%_res_update slurmdbd.service
%_rest slurmdbd

%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%define my_license %license
%else
%define my_license %doc
%endif

%files
%{?comp_at}
%doc AUTHORS NEWS RELEASE_NOTES DISCLAIMER
%my_license COPYING
%{_bindir}/sacct
%{_bindir}/sacctmgr
%{_bindir}/salloc
%{_bindir}/sattach
%{_bindir}/sbatch
%{_bindir}/sbcast
%{_bindir}/scancel
%{_bindir}/scrontab
%{_bindir}/scontrol
%{_bindir}/sdiag
%{_bindir}/sgather
%{_bindir}/sinfo
%{_bindir}/sjobexitmod
%{_bindir}/sprio
%{_bindir}/squeue
%{_bindir}/sreport
%{_bindir}/sshare
%{_bindir}/sstat
%{_bindir}/strigger
%{?have_netloc:%{_bindir}/netloc_to_topology}
%{_sbindir}/slurmctld
%{_sbindir}/slurmsmwd
%dir %{_libdir}/slurm/src
%if 0%{?with_systemd}
%{_unitdir}/slurmctld.service
%{_sbindir}/rcslurmctld
%endif
%{_mandir}/man1/sacct.1*
%{_mandir}/man1/sacctmgr.1*
%{_mandir}/man1/salloc.1*
%{_mandir}/man1/sattach.1*
%{_mandir}/man1/sbatch.1*
%{_mandir}/man1/sbcast.1*
%{_mandir}/man1/scancel.1*
%{_mandir}/man1/scrontab.1*
%{_mandir}/man1/scontrol.1*
%{_mandir}/man1/sdiag.1.*
%{_mandir}/man1/sgather.1.*
%{_mandir}/man1/sinfo.1*
%{_mandir}/man1/slurm.1*
%{_mandir}/man1/sprio.1*
%{_mandir}/man1/squeue.1*
%{_mandir}/man1/sreport.1*
%{_mandir}/man1/sshare.1*
%{_mandir}/man1/sstat.1*
%{_mandir}/man1/strigger.1*
%{_mandir}/man1/sjobexitmod.1.*
%{_mandir}/man1/sjstat.1.*
%{_mandir}/man8/slurmctld.*
%{_mandir}/man8/spank*

%files openlava
%{?comp_at}
%{_bindir}/bjobs
%{_bindir}/bkill
%{_bindir}/bsub
%{_bindir}/lsid

%files seff
%{?comp_at}
%{_bindir}/seff
%{_bindir}/smail

%files doc
%{?comp_at}
%dir %{_datadir}/doc/%{pname}-%{dl_ver}
%{_datadir}/doc/%{pname}-%{dl_ver}/*

%files webdoc
%{?comp_at}
%config %{apache_sysconfdir}/conf.d/slurm.conf

%files -n %{libslurm}
%{?comp_at}
%{_libdir}/libslurm*.so.%{so_version}*

%files -n libpmi%{pmi_so}%{?upgrade:%{_ver}}
%{?comp_at}
%{_libdir}/libpmi*.so.%{pmi_so}*

%files -n libnss_%{pname}%{nss_so}%{?upgrade:%{_ver}}
%{?comp_at}
%config(noreplace) %{_sysconfdir}/%{pname}/nss_slurm.conf
%{_libdir}/libnss_slurm.so.%{nss_so}

%files devel
%{?comp_at}
%{_prefix}/include/slurm
%{_libdir}/libpmi.so
%{_libdir}/libpmi2.so
%{_libdir}/libslurm.so
%{_libdir}/slurm/src/*
#%{_mandir}/man3/slurm_*
%{_libdir}/pkgconfig/slurm.pc

%files sview
%{?comp_at}
%{_bindir}/sview
%{_mandir}/man1/sview.1*

%files auth-none
%{?comp_at}
%{_libdir}/slurm/auth_none.so

%files munge
%{?comp_at}
%{_libdir}/slurm/auth_munge.so
%{_libdir}/slurm/cred_munge.so

%files -n perl-%{name}
%{?comp_at}
%{perl_vendorarch}/Slurm.pm
%{perl_vendorarch}/Slurm
%{perl_vendorarch}/auto/Slurm
%{perl_vendorarch}/Slurmdb.pm
%{perl_vendorarch}/auto/Slurmdb
%{_mandir}/man3/Slurm*.3pm.*

%files slurmdbd
%{?comp_at}
%{_sbindir}/slurmdbd
%{_mandir}/man5/slurmdbd.*
%{_mandir}/man8/slurmdbd.*
%config(noreplace) %attr(0600,%slurm_u,%slurm_g) %{_sysconfdir}/%{pname}/slurmdbd.conf
%if 0%{?with_systemd}
%{_unitdir}/slurmdbd.service
%else
%{_initrddir}/slurmdbd
%endif
%{_sbindir}/rcslurmdbd

%files sql
%{?comp_at}
%dir %{_libdir}/slurm
%{_libdir}/slurm/accounting_storage_mysql.so
%{_libdir}/slurm/jobcomp_mysql.so

%files plugins
%{?comp_at}
%config %{_sysconfdir}/ld.so.conf.d/slurm.conf
%config(noreplace) %{_sysconfdir}/%{pname}/plugstack.conf
%dir %{_sysconfdir}/%{pname}/plugstack.conf.d
%dir %{_libdir}/slurm
%{_libdir}/slurm/libslurmfull.so
%{_libdir}/slurm/accounting_storage_none.so
%{_libdir}/slurm/accounting_storage_slurmdbd.so
%{_libdir}/slurm/acct_gather_energy_pm_counters.so
%{_libdir}/slurm/acct_gather_energy_gpu.so
%{_libdir}/slurm/acct_gather_energy_ibmaem.so
%{_libdir}/slurm/acct_gather_energy_none.so
%{_libdir}/slurm/acct_gather_energy_rapl.so
%{_libdir}/slurm/acct_gather_interconnect_sysfs.so
%{_libdir}/slurm/acct_gather_filesystem_lustre.so
%{_libdir}/slurm/acct_gather_filesystem_none.so
%{_libdir}/slurm/acct_gather_interconnect_none.so
%{_libdir}/slurm/acct_gather_profile_none.so
%{_libdir}/slurm/burst_buffer_lua.so
%{?have_json_c:%{_libdir}/slurm/burst_buffer_datawarp.so}
%{_libdir}/slurm/cgroup_v1.so
%if 0%{?suse_version} >= 1500
%{_libdir}/slurm/cgroup_v2.so
%endif
%{_libdir}/slurm/core_spec_none.so
%{_libdir}/slurm/cli_filter_none.so
%{_libdir}/slurm/cli_filter_lua.so
%{_libdir}/slurm/cli_filter_syslog.so
%{_libdir}/slurm/cli_filter_user_defaults.so
%{_libdir}/slurm/cred_none.so
%{_libdir}/slurm/ext_sensors_none.so
%{_libdir}/slurm/gpu_generic.so
%{_libdir}/slurm/gres_gpu.so
%{_libdir}/slurm/gres_mps.so
%{_libdir}/slurm/gres_nic.so
%{_libdir}/slurm/gres_shard.so
%{_libdir}/slurm/hash_k12.so
%{_libdir}/slurm/jobacct_gather_cgroup.so
%{_libdir}/slurm/jobacct_gather_linux.so
%{_libdir}/slurm/jobacct_gather_none.so
%{_libdir}/slurm/jobcomp_filetxt.so
%{_libdir}/slurm/jobcomp_none.so
%{_libdir}/slurm/jobcomp_lua.so
%{_libdir}/slurm/jobcomp_script.so
%{_libdir}/slurm/job_container_cncu.so
%{_libdir}/slurm/job_container_none.so
%{_libdir}/slurm/job_container_tmpfs.so
%{_libdir}/slurm/job_submit_all_partitions.so
%{_libdir}/slurm/job_submit_defaults.so
%{_libdir}/slurm/job_submit_logging.so
%{_libdir}/slurm/job_submit_partition.so
%{_libdir}/slurm/job_submit_require_timelimit.so
%{_libdir}/slurm/job_submit_throttle.so
%{_libdir}/slurm/launch_slurm.so
%{_libdir}/slurm/libslurm_pmi.so
%{_libdir}/slurm/mcs_account.so
%{_libdir}/slurm/mcs_group.so
%{_libdir}/slurm/mcs_none.so
%{_libdir}/slurm/mcs_user.so
%{_libdir}/slurm/mpi_none.so
%{_libdir}/slurm/mpi_pmi2.so
%if %{with pmix}
%{_libdir}/slurm/mpi_pmix.so
%{_libdir}/slurm/mpi_pmix_v3.so
%endif
%{_libdir}/slurm/node_features_helpers.so
%{_libdir}/slurm/power_none.so
%{_libdir}/slurm/preempt_none.so
%{_libdir}/slurm/preempt_partition_prio.so
%{_libdir}/slurm/preempt_qos.so
%{_libdir}/slurm/prep_script.so
%{_libdir}/slurm/priority_basic.so
%{_libdir}/slurm/priority_multifactor.so
%{_libdir}/slurm/proctrack_cgroup.so
%{_libdir}/slurm/proctrack_linuxproc.so
%{_libdir}/slurm/proctrack_pgid.so
%{_libdir}/slurm/route_default.so
%{_libdir}/slurm/route_topology.so
%{_libdir}/slurm/sched_backfill.so
%{_libdir}/slurm/sched_builtin.so
%{_libdir}/slurm/select_cons_res.so
%{_libdir}/slurm/select_cons_tres.so
%{_libdir}/slurm/select_linear.so
%{_libdir}/slurm/serializer_json.so
%{_libdir}/slurm/serializer_url_encoded.so
%{_libdir}/slurm/serializer_yaml.so
%{_libdir}/slurm/site_factor_none.so
%{_libdir}/slurm/slurmctld_nonstop.so
%{_libdir}/slurm/switch_none.so
%{_libdir}/slurm/task_affinity.so
%{_libdir}/slurm/task_cgroup.so
%{_libdir}/slurm/task_none.so
%{_libdir}/slurm/topology_3d_torus.so
%{_libdir}/slurm/topology_hypercube.so
%{_libdir}/slurm/topology_none.so
%{_libdir}/slurm/topology_tree.so
%if 0%{?suse_version} > 1310
%{_libdir}/slurm/acct_gather_interconnect_ofed.so
%endif
%if 0%{?suse_version} > 1140
%ifarch %{ix86} x86_64
%{_libdir}/slurm/acct_gather_energy_ipmi.so
%{_libdir}/slurm/acct_gather_energy_xcc.so
%endif
%endif
%{_libdir}/slurm/node_features_knl_generic.so
%{_libdir}/slurm/acct_gather_profile_influxdb.so
%{_libdir}/slurm/jobcomp_elasticsearch.so

%files plugin-ext-sensors-rrd
%{_libdir}/slurm/ext_sensors_rrd.so

%files lua
%{?comp_at}
%{_libdir}/slurm/job_submit_lua.so

%files torque
%{?comp_at}
%{_bindir}/pbsnodes
%{_bindir}/qalter
%{_bindir}/qdel
%{_bindir}/qhold
%{_bindir}/qrls
%{_bindir}/qrerun
%{_bindir}/qstat
%{_bindir}/qsub
%{_bindir}/mpiexec.slurm
%{_bindir}/generate_pbs_nodefile
%{_libdir}/slurm/job_submit_pbs.so
%{_libdir}/slurm/spank_pbs.so

%files sjstat
%{?comp_at}
%{_bindir}/sjstat

%files pam_slurm
%{?comp_at}
%doc ../README.pam_slurm ../README.pam_slurm_adopt
%{_pam_moduledir}/pam_slurm.so
%{_pam_moduledir}/pam_slurm_adopt.so

%if 0%{?build_slurmrestd}
%files rest
%{?comp_at}
%{_sbindir}/slurmrestd
%{_mandir}/man8/slurmrestd.*
%{_libdir}/slurm/openapi_dbv0_0_38.so
%{_libdir}/slurm/openapi_v0_0_38.so
%{_libdir}/slurm/openapi_dbv0_0_37.so
%{_libdir}/slurm/openapi_v0_0_37.so
%{_libdir}/slurm/openapi_dbv0_0_36.so
#%{_libdir}/slurm/openapi_v0_0_35.so
%{_libdir}/slurm/openapi_v0_0_36.so
#%{_libdir}/slurm/rest_auth_jwt.so
%{_libdir}/slurm/rest_auth_local.so
%endif

%files node
%{?comp_at}
%{_sbindir}/slurmd
%{_sbindir}/slurmstepd
# bsc#1153095
%{_bindir}/srun
%{_mandir}/man1/srun.1*
%{_mandir}/man8/slurmd.*
%{_mandir}/man8/slurmstepd*
%if 0%{?with_systemd}
%{_sbindir}/rcslurmd
%{_unitdir}/slurmd.service
%else
%{_initrddir}/slurm
%{_sbindir}/rcslurm
%endif

%files config
%{?comp_at}
%dir %{_sysconfdir}/%{pname}
%config(noreplace) %{_sysconfdir}/%{pname}/slurm.conf
%config %{_sysconfdir}/%{pname}/slurm.conf.example
%config(noreplace) %{_sysconfdir}/%{pname}/cgroup.conf
%attr(0755, %slurm_u, %slurm_g) %_localstatedir/lib/slurm
%{?with_systemd:%{_tmpfilesdir}/%{pname}.conf}
%{?_rundir:%ghost %{_rundir}/slurm}
%dir %attr(0755, %slurm_u, %slurm_g)%{_localstatedir}/spool/slurm
%config(noreplace) %{_sysconfdir}/logrotate.d/slurm*
%if 0%{?have_firewalld}
%{_prefix}/lib/firewalld/services/slurmd.xml
%{_prefix}/lib/firewalld/services/slurmctld.xml
%{_prefix}/lib/firewalld/services/slurmdbd.xml
%endif
%{?have_sysuser:%{_sysusersdir}/system-user-%{pname}.conf}

%files config-man
%{?comp_at}
%{_mandir}/man5/acct_gather.conf.*
%{_mandir}/man5/burst_buffer.conf.*
%{_mandir}/man5/ext_sensors.conf.*
%{_mandir}/man5/slurm.*
%{_mandir}/man5/cgroup.*
%{_mandir}/man5/gres.*
%{_mandir}/man5/helpers.*
%{_mandir}/man5/nonstop.conf.5.*
%{_mandir}/man5/oci.conf.5.gz
%{_mandir}/man5/topology.*
%{_mandir}/man5/knl.conf.5.*
%{_mandir}/man5/job_container.conf.5.*
%{_mandir}/man5/mpi.conf.5.*

%if 0%{?have_hdf5}
%files hdf5
%{_bindir}/sh5util
%{_libdir}/slurm/acct_gather_profile_hdf5.so
%{_mandir}/man1/sh5util.1.gz
%endif

%files cray
%{?comp_at}
# do not remove cray sepcific packages from SLES update
# Only for Cray
%{_libdir}/slurm/core_spec_cray_aries.so
%{_libdir}/slurm/job_submit_cray_aries.so
%{_libdir}/slurm/select_cray_aries.so
%{_libdir}/slurm/switch_cray_aries.so
%{_libdir}/slurm/task_cray_aries.so
%{_libdir}/slurm/mpi_cray_shasta.so
%if 0%{?have_json_c}
%{_libdir}/slurm/node_features_knl_cray.so
%{_libdir}/slurm/power_cray_aries.so
%endif

%if 0%{?slurm_testsuite}
%files testsuite
%defattr(-, %slurm_u, %slurm_u, -)
%dir %attr(-, %slurm_u, %slurm_u) /srv/slurm-testsuite
%attr(-, root, root) %{_datadir}/%{name}
%if 0%{?sle_version} == 120200
%dir %{_pam_secconfdir}/limits.d
%endif
%doc testsuite/expect/README
%doc %{basename: %{S:21}}
%config %attr( -, root, root) %{_sysconfdir}/systemd/system/slurmd.service
%config %attr(0440, root, root) %{_sysconfdir}/sudoers.d/slurm
%config %attr( -, root, root) %{_pam_secconfdir}/limits.d/slurm.conf
%{_libdir}/slurm/libslurm.so
%attr(0600, %slurm_u, %slurm_g) /srv/slurm-testsuite/config/slurmdbd.conf
/srv/slurm-testsuite/*
%dir %attr(-, %slurm_u, %slurm_g) %_localstatedir/lib/slurm/shared
%attr( -, root, root) /root/setup-testsuite.sh
%endif

%changelog
