#
# spec file for package cluster-glue
#
# Copyright (c) 2024 SUSE LLC
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


%define gid 90
%define uid 90
%define gname haclient
%define uname hacluster
# Directory where we install documentation
%global glue_docdir %{_defaultdocdir}/%{name}
Name:           cluster-glue
Version:        1.0.13+v1.git.1711478146.5cc622b4
Release:        0
Summary:        Reusable cluster components
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/ClusterLabs/cluster-glue.git
Source:         %{name}-%{version}.tar.bz2
Source3:        hb_report.in
# PATCH-FIX-OPENSUSE: load libplumb symbols manually (thanks to lge) (bnc#694243)
Patch1:         bug-694243_cluster-glue_symbol-conflict.patch
# PATCH-FIX-OPENSUSE: drop lrm as it's not used anymore by pacemaker
Patch4:         cluster-glue_droplrm.patch
# PATCH-FIX-UPSTREAM: fix warnings seen by GCC7

BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  e2fsprogs-devel
BuildRequires:  help2man
BuildRequires:  libaio-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(OpenIPMI)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       perl-TimeDate
Requires:       sudo
Requires(pre):  shadow
# The following is necessary since sbd is dropped from
# cluster-glue itself:
Recommends:     sbd
Conflicts:      heartbeat-common < 3.0.2
Conflicts:      pacemaker < 1.1.8
Obsoletes:      heartbeat-common < 3.0.2
%{?systemd_requires}
%if 0%{?suse_version} >= 1330
Requires(pre):  group(nobody)
Requires(pre):  user(nobody)
%endif
Provides:       group(%{gname})
Provides:       user(%{uname})

%description
A collection of common tools that are useful for writing cluster managers
such as Pacemaker.
Provides a local resource manager that understands the OCF and LSB
standards, and an interface to common STONITH devices.

%package libs
Summary:        Reusable cluster libraries
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Provides:       libglue2 = %version-%release
Conflicts:      libheartbeat2 < 3.0.2
Obsoletes:      libglue2 < %version-%release
Obsoletes:      libheartbeat2 < 3.0.2

%description libs
A collection of libraries that are useful for writing cluster managers
such as Pacemaker.

%package devel
Summary:        Headers and libraries for writing cluster managers
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}-%{release}
Provides:       libglue-devel = %version-%release
Conflicts:      libheartbeat-devel < 3.0.2
Obsoletes:      libglue-devel < %version-%release
Obsoletes:      libheartbeat-devel < 3.0.2

%description devel
Headers and shared libraries for a useful for writing cluster managers
such as Pacemaker.

%prep
%autosetup -p1

%build
export CFLAGS="${CFLAGS} %{optflags}"
export PYTHON="%{_bindir}/python3"
./autogen.sh
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!%{_bindir}/env perl][#\!%{_bindir}/perl]' {} \;
%configure \
    --disable-static \
    --enable-ipmilan=no \
    --enable-libnet=no \
    --disable-fatal-warnings \
    --with-package-name=%{name} \
    --with-daemon-group=%{gname} \
    --with-daemon-user=%{uname} \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-rundir=%{_rundir} \
    --docdir=%{glue_docdir}
make %{?_smp_mflags}

%install
%make_install
# Dont package static libs or compiled python
find %{buildroot} -type f "(" -name "*.la" -o -name "*.pyc" -o -name "*.pyo" ")" -delete -print
install -D -m 755 %{SOURCE3} %{buildroot}%{_sbindir}/hb_report
%if %{defined _unitdir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rclogd
%endif

%pre
getent group %{gname} >/dev/null || groupadd -r -g %{gid} %{gname}
getent passwd %{uname} >/dev/null || useradd -r -u %{uid} -g %{gname} -d %{_localstatedir}/lib/heartbeat/cores/%{uname} -s /sbin/nologin -c "heartbeat processes" %{uname}
%service_add_pre logd.service

%post
%service_add_post logd.service
mkdir -p %{_var}/run/heartbeat/rsctmp

%preun
%service_del_preun logd.service

%postun
%service_del_postun logd.service

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%{_defaultdocdir}/%{name}/
%dir %{_libdir}/heartbeat
%dir %{_var}/lib/heartbeat
%dir %{_var}/lib/heartbeat/cores
%dir %attr (0700, root, root) %{_var}/lib/heartbeat/cores/root
%dir %attr (0700, nobody, nobody) %{_var}/lib/heartbeat/cores/nobody
%dir %attr (0700, %{uname}, %{gname}) %{_var}/lib/heartbeat/cores/%{uname}
%dir %{_libdir}/heartbeat/plugins
%dir %{_libdir}/heartbeat/plugins/RAExec
%dir %{_libdir}/heartbeat/plugins/InterfaceMgr
%dir %{_libdir}/heartbeat/plugins/compress
%dir %{_libdir}/stonith
%dir %{_libdir}/stonith/plugins
%dir %{_libdir}/stonith/plugins/stonith2
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ha_cf_support.sh
%{_datadir}/%{name}/openais_conf_support.sh
%{_datadir}/%{name}/utillib.sh
%{_datadir}/%{name}/ha_log.sh
%{_sbindir}/ha_logger
%{_sbindir}/hb_report
%{_sbindir}/meatclient
%{_sbindir}/stonith
%{_unitdir}/logd.service
%{_mandir}/man8/*
%doc AUTHORS
%license COPYING
%doc logd/logd.cf
%{_sbindir}/rclogd
%{_libdir}/heartbeat/ha_logd
%{_libdir}/heartbeat/plugins/RAExec/*.so
%{_libdir}/heartbeat/plugins/InterfaceMgr/*.so
%{_libdir}/heartbeat/plugins/compress/*.so
%{_libdir}/stonith/plugins/external
%{_libdir}/stonith/plugins/stonith2/ribcl.py
%exclude %{_libdir}/stonith/plugins/stonith2/null.so
%exclude %{_libdir}/stonith/plugins/stonith2/ssh.so
%exclude %{_libdir}/stonith/plugins/external/ssh
%{_libdir}/stonith/plugins/stonith2/*.so
%{_libdir}/stonith/plugins/xen0-ha-dom0-stonith-helper

%files libs
%{_libdir}/lib*.so.*
%doc AUTHORS
%license COPYING.LIB

%files devel
%dir %{_libdir}/heartbeat
%dir %{_libdir}/heartbeat/plugins
%dir %{_libdir}/heartbeat/plugins/test
%dir %{_datadir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/heartbeat/ipctest
%{_libdir}/heartbeat/ipctransientclient
%{_libdir}/heartbeat/ipctransientserver
%{_libdir}/heartbeat/transient-test.sh
%{_libdir}/heartbeat/base64_md5_test
%{_libdir}/heartbeat/logtest
%{_includedir}/clplumbing
%{_includedir}/heartbeat
%exclude %{_includedir}/heartbeat/lrm
%{_includedir}/stonith
%{_includedir}/pils
%{_libdir}/heartbeat/plugins/test/test.so
%{_libdir}/stonith/plugins/stonith2/null.so
%{_libdir}/stonith/plugins/stonith2/ssh.so
%{_libdir}/stonith/plugins/external/ssh
%doc AUTHORS
%license COPYING
%license COPYING.LIB

%changelog
