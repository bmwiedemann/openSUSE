#
# spec file for package htcondor
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


%define _vers 9_0_16

Name:           htcondor
Version:        9.0.16
Release:        0
Summary:        HTCondor is a Distributed High Throughput Computing system
License:        Apache-2.0
URL:            https://htcondor.org
Source0:        https://github.com/htcondor/htcondor/archive/V%{_vers}.tar.gz#/htcondor-%{_vers}.tar.gz
Source1:        condor_config
Source2:        osg-env.conf

#Patch0:         added-suse-as-SYSTEM_NAME.patch
Patch0:         added-suse-as-SYSTEM_NAME-again.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel
BuildRequires:  munge-devel
BuildRequires:  ninja
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  scitokens-cpp-devel
BuildRequires:  sqlite3-devel
BuildRequires:  sysuser-tools
BuildRequires:  voms-devel
BuildRequires:  zlib-devel

Recommends:     %{name}-doc

%description
HTCondor is a Distributed High Throughput Computing system developed at the
Center for High Throughput Computing at the University of Wisconsin - Madison.
With it, users can divide large computing workloads into jobs and submit them
to an HTCondor scheduler, which will run them on worker nodes managed by
HTCondor.





#######################
%package doc
Summary:        Man pages and exmamples for htcondor
Group:          Applications/System

%description doc
This package contains the man pages and addional exmples for htcondor





#######################
%package devel
Summary:        Development files for HTCondor
Group:          Applications/System

%description devel
Development files for HTCondor





#######################
%package procd
Summary:        HTCondor Process tracking Daemon
Group:          Applications/System

%description procd
A daemon for tracking child processes started by a parent.
Part of HTCondor, but able to be stand-alone





#######################
%package kbdd
Summary:        HTCondor Keyboard Daemon
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       %name-classads = %{version}-%{release}

%description kbdd
The condor_kbdd monitors logged in X users for activity. It is only
useful on systems where no device (e.g. /dev/*) can be used to
determine console idle time.





#######################
%package vm-gahp
Summary:        HTCondor's VM Gahp
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       %name-classads = %{version}-%{release}
Requires:       libvirt

%description vm-gahp
The condor_vm-gahp enables the Virtual Machine Universe feature of
HTCondor. The VM Universe uses libvirt to start and control VMs under
HTCondor's Startd.





#######################
%package classads
Summary:        HTCondor's classified advertisement language
Group:          Development/Libraries
Provides:       classads = %version-%release

%description classads
Classified Advertisements (classads) are the lingua franca of
HTCondor. They are used for describing jobs, workstations, and other
resources. They are exchanged by HTCondor processes to schedule
jobs. They are logged to files for statistical and debugging
purposes. They are used to enquire about current state of the system.

A classad is a mapping from attribute names to expressions. In the
simplest cases, the expressions are simple constants (integer,
floating point, or string). A classad is thus a form of property
list. Attribute expressions can also be more complicated. There is a
protocol for evaluating an attribute expression of a classad vis a vis
another ad. For example, the expression "other.size > 3" in one ad
evaluates to true if the other ad has an attribute named size and the
value of that attribute is (or evaluates to) an integer greater than
three. Two classads match if each ad has an attribute requirements
that evaluates to true in the context of the other ad. Classad
matching is used by the HTCondor central manager to determine the
compatibility of jobs and workstations where they may be run.





#######################
%package classads-devel
Summary:        Headers for HTCondor's classified advertisement language
Group:          Development/System
Requires:       %name-classads = %version-%release
Requires:       pcre-devel
Provides:       classads-devel = %version-%release

%description classads-devel
Header files for HTCondor's ClassAd Library, a powerful and flexible,
semi-structured representation of data.





#######################
%package test
Summary:        HTCondor Self Tests
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       %name-classads = %{version}-%{release}

%description test
A collection of tests to verify that HTCondor is operating properly.





#######################
#%%if %parallel_setup
%package parallel-setup
Summary:        Configure HTCondor for Parallel Universe jobs
Group:          Applications/System
Requires:       %name = %version-%release

%description parallel-setup
Running Parallel Universe jobs in HTCondor requires some configuration;
in particular, a dedicated scheduler is required.  In order to support
running parallel universe jobs out of the box, this sub-package provides
a condor_config.local.dedicated.resource file that sets up the current
host as the DedicatedScheduler.





#######################
%package -n python3-condor
Summary:        Python bindings for HTCondor.
Group:          Applications/System
Requires:       python3

%description -n python3-condor
The python bindings allow one to directly invoke the C++ implementations of
the ClassAd library and HTCondor from python





#######################
%package credmon-vault
Summary:        Vault credmon for HTCondor.
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       python3-condor
Requires:       python3-six
Conflicts:      %name-credmon-oauth

%description credmon-vault
The Vault credmon allows users to obtain credentials from Vault using
htgettoken and to use those credentials securely inside running jobs.





#######################
%package bosco
Summary:        BOSCO, a HTCondor overlay system for managing jobs at remote clusters
URL:            https://osg-bosco.github.io/docs/
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       python3
Requires:       rsync

%description bosco
BOSCO allows a locally-installed HTCondor to submit jobs to remote clusters,
using SSH as a transit mechanism.  It is designed for cases where the remote
cluster is using a different batch system such as PBS, SGE, LSF, or another
HTCondor system.

BOSCO provides an overlay system so the remote clusters appear to be a HTCondor
cluster.  This allows the user to run their workflows using HTCondor tools across
multiple clusters.





#######################
%package -n minicondor
Summary:        Configuration for a single-node HTCondor
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       %{name}-procd
Requires:       python3-condor = %version-%release

%description -n minicondor
This example configuration is good for trying out HTCondor for the first time.
It only configures the IPv4 loopback address, turns on basic security, and
shortens many timers to be more responsive.





#######################
%package all
Summary:        All condor packages in a typical installation
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       %name-bosco = %version-%release
Requires:       %name-classads = %version-%release
Requires:       %name-kbdd = %version-%release
Requires:       %name-procd = %version-%release
Requires:       %name-vm-gahp = %version-%release
Requires:       python3-condor = %version-%release

%description all
Include dependencies for all condor packages in a typical installation





#######################
%package credmon-oauth
Summary:        OAuth2 credmon for HTCondor.
Group:          Applications/System
Requires:       %name = %version-%release
Requires:       httpd
Requires:       mod_wsgi
Requires:       python3-Flask
Requires:       python3-condor
Requires:       python3-cryptography
Requires:       python3-requests-oauthlib
Requires:       python3-scitokens
Requires:       python3-six

%description credmon-oauth
The OAuth2 credmon allows users to obtain credentials from configured
OAuth2 endpoints and to use those credentials securely inside running jobs.

%prep
%autosetup -n %{name}-%{_vers} -p1

%build
%define __builder ninja
cd build
# Unfortunately the %%cmake macro can't be used as it will fail with unedefined references
# due linking magic from htcondor due to compaltiblity for windows and other *nix systems
cmake \
   -GNinja \
   -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
   -DINCLUDE_INSTALL_DIR:PATH=/usr/include \
   -DSYSCONF_INSTALL_DIR:PATH=/etc \
   -DSHARE_INSTALL_PREFIX:PATH=/usr/share \
   -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib64 \
   -DLIB_INSTALL_DIR:PATH=/usr/lib64 \
   -DLIB_SUFFIX=64 \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%ifarch x86_64
   -DCMAKE_C_FLAGS="${CFLAGS:--O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables} -DNDEBUG" \
        -DCMAKE_CXX_FLAGS="${CXXFLAGS:--O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables} -DNDEBUG" \
%else
   -DCMAKE_C_FLAGS="${CFLAGS:--O2 -g -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables} -DNDEBUG" \
        -DCMAKE_CXX_FLAGS="${CXXFLAGS:--O2 -g -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables} -DNDEBUG" \
%endif
   -DCMAKE_EXE_LINKER_FLAGS=" -Wl,--as-needed -Wl,-z,now" \
   -DCMAKE_MODULE_LINKER_FLAGS=" -Wl,--as-needed" \
   -DCMAKE_SHARED_LINKER_FLAGS=" -Wl,--as-needed -Wl,-z,now" \
   -DLIB_SUFFIX=64 \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DBUILD_STATIC_LIBS:BOOL=OFF \
   -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
   -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
   -DCMAKE_MODULES_INSTALL_DIR=/usr/share/cmake/Modules \
   -DSYSTEM_NAME:STRING=suse \
   -DBUILDID:STRING="suse%{?sle_version}"\
   -DCONDOR_PACKAGE_BUILD:BOOL=ON \
   -DCONDOR_RPMBUILD:BOOL=TRUE \
   -DPROPER:BOOL=ON \
   -DCMAKE_SKIP_RPATH:BOOL=ON \
   -DWITH_GLOBUS:BOOL=FALSE \
   -DWITH_PYTHON_BINDINGS:BOOL=ON \
   -DHAVE_EXT_BOOST:BOOL=ON \
   -DWITH_SCITOKENS:BOOL=ON \
   -DBUILD_TESTING:BOOL=OFF \
   -DHAVE_EXT_KRB5:BOOL=ON \
   -DHAVE_EXT_PCRE:BOOL=ON \
   -DHAVE_EXT_LIBVIRT:BOOL=ON \
   -DHAVE_EXT_LIBXML2:BOOL=ON \
   -DHAVE_EXT_OPENSSL:BOOL=ON \
   -DWITH_CAMPUSFACTORY:BOOL=OFF \
   -DWANT_MAN_PAGES:BOOL=TRUE \
   -DHAVE_HIBERNATION:BOOL=TRUE \
   ../

%cmake_build

%install
%cmake_install

# somewhat most stuff ended up in /usr/usr so fixing this
cp -r %{buildroot}/usr/usr/* %{buildroot}/usr/
rm -rf %{buildroot}/usr/usr/
# condor stuff was installed direcly in /usr/libexec, so moving the stuff
# to /usr/libexsec/condor
mv %{buildroot}/usr/libexec %{buildroot}/usr/libexec_condor/
mkdir -p %{buildroot}/usr/libexec
mv %{buildroot}/usr/libexec_condor %{buildroot}/usr/libexec/condor
mv %{buildroot}/usr%{_sysconfdir}/ %{buildroot}%{_sysconfdir}
%ifnarch %{ix86} %arm
# mv libraries to /usr/lib64
mv %{buildroot}/usr/lib/lib* %{buildroot}%{_libdir}
%endif
# remove static stuff
rm -f %{buildroot}%{_libdir}/*a

# more stuff to move
mkdir -p %{buildroot}/usr/share/condor
mv %{buildroot}/usr/lib/Chirp.jar %{buildroot}/usr/share/condor
mv %{buildroot}/usr/lib/CondorJava*.class %{buildroot}/usr/share/condor

# installing components
# Move oauth credmon config files out of examples and into config.d
mkdir -p %{buildroot}/srv/www/wsgi-scripts/condor_credmon_oauth
mv %{buildroot}/%{_libexecdir}/condor/condor_credmon_oauth.wsgi %{buildroot}/srv/www/wsgi-scripts/condor_credmon_oauth/condor_credmon_oauth.wsgi
mv %{buildroot}%{_sysconfdir}/examples/condor_credmon_oauth/config/condor/40-oauth-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-credmon.conf
mv %{buildroot}%{_sysconfdir}/examples/condor_credmon_oauth/config/condor/40-oauth-tokens.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-tokens.conf
mkdir -p %{buildroot}/%{_var}/lib/condor/oauth_credentials/
mv %{buildroot}%{_sysconfdir}/examples/condor_credmon_oauth/README.credentials %{buildroot}/%{_var}/lib/condor/oauth_credentials/README.credentials
mkdir -p %{buildroot}%{_includedir}/condor
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/user_log.README %{buildroot}%{_includedir}/condor

# install tmpfiles.d/condor.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{buildroot}/%{_sysconfdir}/examples/condor-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
# Drop in a symbolic link for backward compatibility
mkdir -p %{buildroot}/usr/lib/condor %{buildroot}/%_sysconfdir/condor
#cp %{S:1} %{buildroot}/%_sysconfdir/condor
mv %{buildroot}/usr/lib/condor_ssh_to_job_sshd_config_template %{buildroot}/usr/lib/condor
#ln -s ../../lib/condor/condor_ssh_to_job_sshd_config_template %{buildroot}/%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template
mkdir -p %{buildroot}%{_sharedstatedir}/condor/oauth_credentials
mkdir -p %{buildroot}/%{_sysconfdir}/condor/config.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/passwords.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/tokens.d
mkdir -p -m0755 %{buildroot}%{_prefix}/share/condor/config.d
# configs
mv %{buildroot}/etc/examples/00-htcondor-9.0.config %{buildroot}/%{_sysconfdir}/condor/config.d
mv %{buildroot}/etc/examples/00-minicondor %{buildroot}/%{_sysconfdir}/condor/config.d
mv %{buildroot}/etc/examples/condor_config.local.dedicated.resource %{buildroot}/%{_sysconfdir}/condor/config.d/20dedicated_scheduler_condor.config
LIB=$(echo %{?_libdir} | sed -e 's:/usr/\(.*\):\1:')
if [ "$LIB" = "%_libdir" ]; then
  echo "_libdir does not contain /usr, sed expression needs attention"
  exit 1
fi
cp %{S:1} %{buildroot}%{_sysconfdir}/condor

mkdir -p -m0755 %{buildroot}/%{_var}/log/condor
# Note we use %{_var}/lib instead of %{_sharedstatedir} for RHEL5 compatibility
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/spool
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/execute
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/krb_credentials
mkdir -p -m2770 %{buildroot}/%{_var}/lib/condor/oauth_credentials

# service files
mkdir -p %{buildroot}%{_unitdir}
#install -m 0644 src/condor_examples/condor-annex-ec2.service %{buildroot}%{_unitdir}/condor-annex-ec2.service
install -m 0644 src/condor_examples/condor.service %{buildroot}%{_unitdir}/condor.service

# Set condor service enviroment variables for LCMAPS on OSG systems
mkdir -p %{buildroot}%{_unitdir}/condor.service.d
install -Dp -m 0644 %{S:2} %{buildroot}%{_unitdir}/condor.service.d/osg-env.conf

# move examples to root build dir so that the %%doc macro can be used
mv %{buildroot}/usr/examples .
mv %{buildroot}/etc/examples examples/etc
sed -i 's@#!.*/usr/bin/env bash@#!/usr/bin/bash@' examples/etc/openmpiscript
rm -rf %{buildroot}/%{_sysconfdir}/init.d
# move man pages to right location
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_prefix}/man/*.1 %{buildroot}%{_mandir}/man1
for file in %{buildroot}%{_mandir}/man1/*.1; do gzip $file; done

# remove tar ball stuff
rm %{buildroot}/%{_sbindir}/condor_configure \
   %{buildroot}/%{_sbindir}/condor_install \
   %{buildroot}/%{_mandir}/man1/condor_configure.1.gz \
   %{buildroot}/%{_mandir}/man1/condor_install.1.gz \
   %{buildroot}/%{_bindir}/make-personal-from-tarball

rm %{buildroot}/usr/LICENSE-2.0.txt \
   %{buildroot}/usr/NOTICE.txt \
   %{buildroot}/usr/README

# create condor user
echo "u condor -" > system-user-%{name}.conf
echo "g condor -" >> system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf %{name} system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf

# fixing up some env things
sed -i 's@#!/usr/bin/env python[23]@#!/usr/bin/python3@' %{buildroot}%{_sbindir}/condor_* %{buildroot}%{_bindir}/condor_* %{buildroot}%{_libexecdir}/condor/*py %{buildroot}%{_sbindir}/AzureGAHPServer
sed -i 's@#!.*/usr/bin/env perl@#!/usr/bin/perl@' %{buildroot}%{_sbindir}/condor_* %{buildroot}%{_bindir}/condor_* %{buildroot}%{_sbindir}/condor_*  %{buildroot}%{_sbindir}/bosco_install
sed -i 's@#!.*/usr/bin/env bash@#!/usr/bin/bash@' %{buildroot}%{_libexecdir}/condor/*.sh

%pre -f %{name}.pre
%service_add_pre condor.service

%post
%service_add_post condor.service

%preun
%service_del_preun condor.service

%postun
%service_del_postun condor.service

%files
%license LICENSE-2.0.txt NOTICE.txt
%_sysconfdir/bash_completion.d/condor
%_libdir/libchirp_client.so
%_libdir/libcondor_utils_%{_vers}.so
%_libdir/libcondorapi.so
%_libdir/libgetpwnam.so
%dir %_libexecdir/condor/
%_libexecdir/condor/linux_kernel_tuning
%_libexecdir/condor/accountant_log_fixer
%_libexecdir/condor/condor_chirp
%_libexecdir/condor/condor_ssh
%_libexecdir/condor/sshd.sh
%_libexecdir/condor/get_orted_cmd.sh
%_libexecdir/condor/orted_launcher.sh
%_libexecdir/condor/set_batchtok_cmd
%_libexecdir/condor/cred_producer_krb
%_libexecdir/condor/condor_job_router
%_libexecdir/condor/condor_pid_ns_init
%_libexecdir/condor/condor_urlfetch
%_libexecdir/condor/condor_limits_wrapper.sh
%_libexecdir/condor/condor_rooster
%_libexecdir/condor/condor_schedd.init
%_libexecdir/condor/condor_ssh_to_job_shell_setup
%_libexecdir/condor/condor_ssh_to_job_sshd_setup
%_libexecdir/condor/condor_power_state
%_libexecdir/condor/condor_kflops
%_libexecdir/condor/condor_mips
%_libexecdir/condor/data_plugin
%_libexecdir/condor/box_plugin.py
%_libexecdir/condor/gdrive_plugin.py
%_libexecdir/condor/onedrive_plugin.py
# TODO: get rid of these
# Not sure where these are getting built
%_libexecdir/condor/curl_plugin
%_libexecdir/condor/legacy_curl_plugin
%_libexecdir/condor/condor_shared_port
%_libexecdir/condor/condor_defrag
%_libexecdir/condor/interactive.sub
%_libexecdir/condor/condor_gangliad
%_libexecdir/condor/panda-plugin.so
%_libexecdir/condor/pandad
%_libexecdir/condor/ce-audit.so
%_libexecdir/condor/adstash/__init__.py
%_libexecdir/condor/adstash/config.py
%_libexecdir/condor/adstash/convert.py
%_libexecdir/condor/adstash/elastic.py
%_libexecdir/condor/adstash/history.py
%_libexecdir/condor/adstash/utils.py
%_bindir/condor_submit_dag
%_bindir/condor_who
%_bindir/condor_now
%_bindir/condor_prio
%_bindir/condor_transfer_data
%_bindir/condor_check_userlogs
%_bindir/condor_q
%_libexecdir/condor/condor_transferer
%_bindir/condor_docker_enter
%_bindir/condor_qedit
%_bindir/condor_userlog
%_bindir/condor_release
%_bindir/condor_remote_cluster
%_bindir/condor_userlog_job_counter
%_bindir/condor_config_val
%_bindir/condor_reschedule
%_bindir/condor_userprio
%_bindir/condor_check_password
%_bindir/condor_check_config
%_bindir/condor_dagman
%_bindir/condor_rm
%_bindir/condor_vacate
%_bindir/condor_run
%_bindir/condor_router_history
%_bindir/condor_router_q
%_bindir/condor_router_rm
%_bindir/condor_vacate_job
%_bindir/condor_findhost
%_bindir/condor_stats
%_bindir/condor_version
%_bindir/condor_history
%_bindir/condor_status
%_bindir/condor_wait
%_bindir/condor_hold
%_bindir/condor_submit
%_bindir/condor_ssh_to_job
%_bindir/condor_power
%_bindir/condor_gather_info
%_bindir/condor_continue
%_bindir/condor_suspend
%_bindir/condor_test_match
%_bindir/condor_token_create
%_bindir/condor_token_fetch
%_bindir/condor_token_request
%_bindir/condor_token_request_approve
%_bindir/condor_token_request_auto_approve
%_bindir/condor_token_request_list
%_bindir/condor_token_list
%_bindir/condor_scitoken_exchange
%_bindir/condor_drain
%_bindir/condor_ping
%_bindir/condor_tail
%_bindir/condor_qsub
%_bindir/condor_pool_job_report
%_bindir/condor_job_router_info
%_bindir/condor_transform_ads
%_bindir/condor_update_machine_ad
%_bindir/condor_annex
%_bindir/condor_nsenter
%_bindir/condor_evicted_files
%_bindir/condor_adstash
# sbin/condor is a link for master_off, off, on, reconfig,
# reconfig_schedd, restart
%_sbindir/condor_advertise
%_sbindir/condor_aklog
%_sbindir/condor_credmon_krb
%_sbindir/condor_c-gahp
%_sbindir/condor_c-gahp_worker_thread
%_sbindir/condor_collector
%_sbindir/condor_convert_history
%_sbindir/condor_credd
%_sbindir/condor_fetchlog
%_sbindir/condor_had
%_sbindir/condor_master
%_sbindir/condor_negotiator
%_sbindir/condor_off
%_sbindir/condor_on
%_sbindir/condor_preen
%_sbindir/condor_reconfig
%_sbindir/condor_replication
%_sbindir/condor_restart
%_sbindir/condor_schedd
%_sbindir/condor_set_shutdown
%_sbindir/condor_shadow
%_sbindir/condor_sos
%_sbindir/condor_startd
%_sbindir/condor_starter
%_sbindir/condor_store_cred
%_sbindir/condor_testwritelog
%_sbindir/condor_transferd
%_sbindir/condor_updates_stats
%_sbindir/ec2_gahp
%_sbindir/condor_gridmanager
%_sbindir/remote_gahp
%_sbindir/AzureGAHPServer
%_sbindir/gce_gahp
%_sbindir/openstack_gahp
%_libexecdir/condor/condor_gpu_discovery
%_libexecdir/condor/condor_gpu_utilization
%_sbindir/condor_vm-gahp-vmware
%_sbindir/condor_vm_vmware
%{_sysusersdir}/system-user-%{name}.conf
%dir %_sysconfdir/condor/
%config %_sysconfdir/condor/condor_config
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/condor.service
%dir %{_unitdir}/condor.service.d
%{_unitdir}/condor.service.d/osg-env.conf
# Disabled until HTCondor security fixed.
# % {_unitdir}/condor.socket
%dir %_datadir/condor/
%_datadir/condor/Chirp.jar
%_datadir/condor/CondorJavaInfo.class
%_datadir/condor/CondorJavaWrapper.class
#%%_datadir/condor/htcondor.pp
%dir %_sysconfdir/condor/passwords.d/
%dir %_sysconfdir/condor/tokens.d/
%dir %_sysconfdir/condor/config.d/
%config(noreplace) %{_sysconfdir}/condor/config.d/00-htcondor-9.0.config
%dir /usr/share/condor/config.d/
%{_prefix}/lib/condor/condor_ssh_to_job_sshd_config_template
%config(noreplace) %_sysconfdir/condor/ganglia.d/00_default_metrics
%dir %{_sysconfdir}/condor
%dir %{_sysconfdir}/condor/ganglia.d
%dir %{_prefix}/lib/condor
%dir %{_prefix}/libexec/condor/adstash
%defattr(-,condor,condor,-)
%dir %{_sharedstatedir}/condor/
%dir %{_sharedstatedir}/condor/execute/
%dir %{_sharedstatedir}/condor/spool/
%dir %{_var}/log/condor/

#################
%files doc
%doc README.md CITATION.cff examples
%_mandir/man1/condor_advertise.1.gz
%_mandir/man1/condor_annex.1.gz
%_mandir/man1/condor_check_password.1.gz
%_mandir/man1/condor_check_userlogs.1.gz
%_mandir/man1/condor_chirp.1.gz
%_mandir/man1/condor_config_val.1.gz
%_mandir/man1/condor_convert_history.1.gz
%_mandir/man1/condor_dagman.1.gz
%_mandir/man1/condor_fetchlog.1.gz
%_mandir/man1/condor_findhost.1.gz
%_mandir/man1/condor_gpu_discovery.1.gz
%_mandir/man1/condor_history.1.gz
%_mandir/man1/condor_hold.1.gz
%_mandir/man1/condor_job_router_info.1.gz
%_mandir/man1/condor_master.1.gz
%_mandir/man1/condor_off.1.gz
%_mandir/man1/condor_on.1.gz
%_mandir/man1/condor_pool_job_report.1.gz
%_mandir/man1/condor_preen.1.gz
%_mandir/man1/condor_prio.1.gz
%_mandir/man1/condor_q.1.gz
%_mandir/man1/condor_qsub.1.gz
%_mandir/man1/condor_qedit.1.gz
%_mandir/man1/condor_reconfig.1.gz
%_mandir/man1/condor_release.1.gz
%_mandir/man1/condor_reschedule.1.gz
%_mandir/man1/condor_restart.1.gz
%_mandir/man1/condor_rm.1.gz
%_mandir/man1/condor_run.1.gz
%_mandir/man1/condor_set_shutdown.1.gz
%_mandir/man1/condor_sos.1.gz
%_mandir/man1/condor_stats.1.gz
%_mandir/man1/condor_status.1.gz
%_mandir/man1/condor_store_cred.1.gz
%_mandir/man1/condor_submit.1.gz
%_mandir/man1/condor_submit_dag.1.gz
%_mandir/man1/condor_token_create.1.gz
%_mandir/man1/condor_token_fetch.1.gz
%_mandir/man1/condor_token_list.1.gz
%_mandir/man1/condor_token_request.1.gz
%_mandir/man1/condor_token_request_approve.1.gz
%_mandir/man1/condor_token_request_auto_approve.1.gz
%_mandir/man1/condor_token_request_list.1.gz
%_mandir/man1/condor_top.1.gz
%_mandir/man1/condor_transfer_data.1.gz
%_mandir/man1/condor_transform_ads.1.gz
%_mandir/man1/condor_update_machine_ad.1.gz
%_mandir/man1/condor_updates_stats.1.gz
%_mandir/man1/condor_urlfetch.1.gz
%_mandir/man1/condor_userlog.1.gz
%_mandir/man1/condor_userprio.1.gz
%_mandir/man1/condor_vacate.1.gz
%_mandir/man1/condor_vacate_job.1.gz
%_mandir/man1/condor_version.1.gz
%_mandir/man1/condor_wait.1.gz
%_mandir/man1/condor_router_history.1.gz
%_mandir/man1/condor_continue.1.gz
%_mandir/man1/condor_suspend.1.gz
%_mandir/man1/condor_router_q.1.gz
%_mandir/man1/condor_ssh_to_job.1.gz
%_mandir/man1/condor_power.1.gz
%_mandir/man1/condor_gather_info.1.gz
%_mandir/man1/condor_router_rm.1.gz
%_mandir/man1/condor_drain.1.gz
%_mandir/man1/condor_ping.1.gz
%_mandir/man1/condor_rmdir.1.gz
%_mandir/man1/condor_tail.1.gz
%_mandir/man1/condor_who.1.gz
%_mandir/man1/condor_now.1.gz
%_mandir/man1/classad_eval.1.gz
%_mandir/man1/classads.1.gz
%_mandir/man1/condor_adstash.1.gz
%_mandir/man1/condor_evicted_files.1.gz
%_mandir/man1/condor_watch_q.1.gz
%_mandir/man1/get_htcondor.1.gz

#################
%files devel
%dir %{_includedir}/condor
%{_includedir}/condor/MyString.h
%{_includedir}/condor/chirp_client.h
%{_includedir}/condor/compat_classad.h
%{_includedir}/condor/compat_classad_list.h
%{_includedir}/condor/compat_classad_util.h
%{_includedir}/condor/condor_classad.h
%{_includedir}/condor/condor_constants.h
%{_includedir}/condor/condor_event.h
%{_includedir}/condor/condor_header_features.h
%{_includedir}/condor/condor_holdcodes.h
%{_includedir}/condor/file_lock.h
%{_includedir}/condor/iso_dates.h
%{_includedir}/condor/read_user_log.h
%{_includedir}/condor/stl_string_utils.h
%{_includedir}/condor/user_log.README
%{_includedir}/condor/user_log.c++.h
%{_includedir}/condor/write_user_log.h

#################
%files procd
%_sbindir/condor_procd
%_sbindir/gidd_alloc
%_sbindir/procd_ctl
%_mandir/man1/procd_ctl.1.gz
%_mandir/man1/gidd_alloc.1.gz
%_mandir/man1/condor_procd.1.gz

#################
%files kbdd
%defattr(-,root,root,-)
%license LICENSE-2.0.txt NOTICE.txt
#%%_sbindir/condor_kbdd

#################
%files vm-gahp
%defattr(-,root,root,-)
%license LICENSE-2.0.txt NOTICE.txt
%_sbindir/condor_vm-gahp
%_libexecdir/condor/libvirt_simple_script.awk

#################
%files classads
%defattr(-,root,root,-)
%license LICENSE-2.0.txt NOTICE.txt
%_libdir/libclassad.so.*

#################
%files classads-devel
%defattr(-,root,root,-)
%license LICENSE-2.0.txt NOTICE.txt
%_bindir/classad_functional_tester
%_bindir/classad_version
%_libdir/libclassad.so
%dir %_includedir/classad/
%_includedir/classad/attrrefs.h
%_includedir/classad/cclassad.h
%_includedir/classad/classad_distribution.h
%_includedir/classad/classadErrno.h
%_includedir/classad/classad.h
%_includedir/classad/classadItor.h
%_includedir/classad/classadCache.h
%_includedir/classad/classad_containers.h
%_includedir/classad/collectionBase.h
%_includedir/classad/collection.h
%_includedir/classad/common.h
%_includedir/classad/debug.h
%_includedir/classad/exprList.h
%_includedir/classad/exprTree.h
%_includedir/classad/fnCall.h
%_includedir/classad/indexfile.h
%_includedir/classad/jsonSink.h
%_includedir/classad/jsonSource.h
%_includedir/classad/lexer.h
%_includedir/classad/lexerSource.h
%_includedir/classad/literals.h
%_includedir/classad/matchClassad.h
%_includedir/classad/natural_cmp.h
%_includedir/classad/operators.h
%_includedir/classad/query.h
%_includedir/classad/sink.h
%_includedir/classad/source.h
%_includedir/classad/transaction.h
%_includedir/classad/util.h
%_includedir/classad/value.h
%_includedir/classad/view.h
%_includedir/classad/xmlLexer.h
%_includedir/classad/xmlSink.h
%_includedir/classad/xmlSource.h

#################
#%%files test
#%%defattr(-,root,root,-)
%_libexecdir/condor/condor_sinful
%_libexecdir/condor/condor_testingd
%_libexecdir/condor/test_user_mapping

#################
#%%files parallel-setup
%defattr(-,root,root,-)
%config(noreplace) %_sysconfdir/condor/config.d/20dedicated_scheduler_condor.config

#################
%files -n python3-condor
%defattr(-,root,root,-)
%_bindir/condor_top
%_bindir/classad_eval
%_bindir/condor_watch_q
%_libdir/libpyclassad3.*.so
%_libexecdir/condor/libclassad_python_user.cpython-3*.so
%_libexecdir/condor/libclassad_python3_user.so
%_libexecdir/condor/libcollector_python_plugin.cpython-3*.so
%_libexecdir/condor/libcollector_python3_plugin.so
%{python3_sitearch}/htcondor-%{version}-py%{py3_ver}.egg-info

%{python3_sitearch}/htcondor
%{python3_sitearch}/classad

#################
%files credmon-oauth
#%doc examples/condor_credmon_oauth
%_sbindir/condor_credmon_oauth
%_sbindir/scitokens_credential_producer
%dir /srv/www/wsgi-scripts/
/srv/www/wsgi-scripts/condor_credmon_oauth
%_libexecdir/condor/credmon
%config(noreplace) %_sysconfdir/condor/config.d/40-oauth-credmon.conf
%config(noreplace) %_sysconfdir/condor/config.d/40-oauth-tokens.conf
%defattr(-,condor,condor,-)
%{_sharedstatedir}/condor/oauth_credentials/README.credentials
%ghost %{_sharedstatedir}/condor/oauth_credentials/wsgi_session_key
%ghost %{_sharedstatedir}/condor/oauth_credentials/CREDMON_COMPLETE
%ghost %{_sharedstatedir}/condor/oauth_credentials/pid
%dir %{_sharedstatedir}/condor/oauth_credentials
%dir %{_sharedstatedir}/condor

#################
%files credmon-vault
#%%doc examples/condor_credmon_oauth
%_sbindir/condor_credmon_vault
%_bindir/condor_vault_storer
%_libexecdir/condor/credmon
#%%config(noreplace) %_sysconfdir/condor/config.d/40-vault-credmon.conf
%defattr(-,condor,condor,-)
%ghost %{_sharedstatedir}/condor/oauth_credentials/CREDMON_COMPLETE
%ghost %{_sharedstatedir}/condor/oauth_credentials/pid
%dir %{_sharedstatedir}/condor
%dir %{_sharedstatedir}/condor/oauth_credentials

%files bosco
%defattr(-,root,root,-)
%_libexecdir/condor/shellselector
%_sbindir/bosco_install
%_sbindir/condor_ft-gahp
%_bindir/bosco_cluster
%_bindir/bosco_ssh_start
%_bindir/bosco_start
%_bindir/bosco_stop
%_bindir/bosco_findplatform
%_bindir/bosco_uninstall
%_bindir/bosco_quickstart
%_bindir/htsub
%_mandir/man1/bosco_cluster.1.gz
%_mandir/man1/bosco_findplatform.1.gz
%_mandir/man1/bosco_install.1.gz
%_mandir/man1/bosco_ssh_start.1.gz
%_mandir/man1/bosco_start.1.gz
%_mandir/man1/bosco_stop.1.gz
%_mandir/man1/bosco_uninstall.1.gz

%files -n minicondor
%config(noreplace) %_sysconfdir/condor/config.d/00-minicondor

%changelog
