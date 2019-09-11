#
# spec file for package ganglia
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:        A scalable distributed monitoring system for high-performance computing systems
License:        BSD-3-Clause
Group:          System/Monitoring
Name:           ganglia
Version:        3.7.2
Release:        0
%define lib_version 0
Url:            http://ganglia.info/
# The Release macro value is set in configure.in, please update it there.
Source0:        http://downloads.sourceforge.net/ganglia/%{name}-%{version}.tar.gz
Source1:        btrfs-subvol-test.sh
# PATCH-FIX-OPENSUSE ganglia-3.7.1-no-private-apr.patch
Patch1:         ganglia-3.7.2-no-private-apr.patch
Patch2:         gmetad-service-btrfs-check.patch
Patch3:         detect_aarch.patch
Patch4:         add_unknown_arch.patch
Patch5:         ganglia-0001-avoid-segfault-when-fd-leaked-and-reached-fd-number-.patch
Patch6:         ganglia-0002-Ignore-hostname-line-in-Apache-2.4.16.patch
Patch7:         ganglia-0003-Avoid-KeyError-for-new-metric-groups.patch
Patch8:         ganglia-0004-Metric-currestab-unlike-all-the-other-one-is-an-abso.patch
Patch9:         ganglia-0005-ensure-the-num-DS-is-always-of-type-GAUGE.patch
Patch10:        ganglia-0006-Fix-race-condition-where-new-metrics-are-added-while.patch
Patch11:        ganglia-0007-fix-indent-to-use-whitespace.patch
Patch12:        ganglia-0008-support-fs-size-for-ZFS-on-Linux.patch
Patch13:        ganglia-0009-Fix-server-definition-type-of-cpu_steal-float.patch
Patch14:        ganglia-0010-Fixes-245.patch
Patch15:        ganglia-0011-Fixed-44.patch
Patch16:        ganglia-0012-Fix-disable-setuid-and-disable-setgid.patch
Patch17:        ganglia-0013-downgrade-udp-recv-buffer-length-check.patch
Patch18:        ganglia-0014-Report-mem-as-float-to-avoid-uint32-overflow.patch
Patch19:        ganglia-0015-Fix-for-issue-246-minor-typo-in-conversion-from-sflo.patch
Patch20:        ganglia-0016-The-way-forward-is-sometimes-the-way-back.patch
Patch21:        ganglia-0017-Fix-wrong-steal-values-being-reported-for-multi_cpu.patch
Patch22:        ganglia-0018-PEP8-changed-indentation-resulting-in-wrong-summatio.patch
Patch23:        ganglia-0019-issue-266-requiring-dhcp-and-network-interfaces-to-b.patch
Patch24:        ganglia-0020-Fix-segfault-with-TCP-listener-thread-on-exit.patch
Patch25:        ganglia-0021-fix-net-byte-packet-stats-on-32-bit-linux.patch
Patch26:        ganglia-0022-spaces-may-not-appear-in-some-parts-of-the-rrdtool-d.patch
Patch27:        ganglia-0023-Fix-hash-collisions.patch
Patch28:        ganglia-0024-Add-regular-Slab-memory-to-linux-memory-metrics.patch
Patch29:        ganglia-0025-Report-the-Linux-specific-slab-memory-metric.patch
BuildRequires:  fdupes
BuildRequires:  libapr1-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libexpat-devel
BuildRequires:  libpng-devel
BuildRequires:  libtirpc-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  rrdtool-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define gmond_conf %{_builddir}/%{?buildsubdir}/gmond/gmond.conf
%define generate_gmond_conf %(test -e %gmond_conf && echo 0 || echo 1)

%description
Ganglia is a scalable distributed monitoring system for high-performance
computing systems such as clusters and Grids. It is based on a hierarchical
design targeted at federations of clusters. It leverages widely used
technologies such as XML for data representation, XDR for compact, portable
data transport, and RRDtool for data storage and visualization. It uses
carefully engineered data structures and algorithms to achieve very low
per-node overheads and high concurrency. The implementation is robust,
has been ported to an extensive set of operating systems and processor
architectures, and is currently in use on thousands of clusters around
the world. It has been used to link clusters across university campuses
and around the world and can scale to handle clusters with 2000 nodes.


%package gmetad
Summary:        Ganglia Meta daemon
Group:          System/Monitoring
Obsoletes:      ganglia-monitor-core < %{version}
Obsoletes:      ganglia-monitor-core-gmetad < %{version}
Provides:       ganglia-monitor-core = %{version}
Provides:       ganglia-monitor-core-gmetad = %{version}
%{?systemd_requires}

%description gmetad
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmetad daemon aggregates monitoring data from several clusters
to form a monitoring grid. It also keeps metric history using rrdtool.


%package gmond
Summary:        Ganglia Monitor daemon
Group:          System/Monitoring
Obsoletes:      ganglia-monitor-core < %{version}
Obsoletes:      ganglia-monitor-core-gmond < %{version}
Provides:       ganglia-monitor-core = %{version}
Provides:       ganglia-monitor-core-gmond = %{version}
%{?systemd_requires}
Requires(post): coreutils

%description gmond
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmond daemon provides the ganglia service within a single cluster or
Multicast domain.

%package gmond-modules-python
Summary:        Ganglia Monitor daemon DSO/Python metric modules support
Group:          System/Monitoring
Requires:       ganglia-gmond
Requires:       python

%description gmond-modules-python
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmond modules support package provides the capability of loading
gmetric/python modules via DSO at daemon start time instead of via gmetric.


%package gmetad-skip-bcheck
Summary:        Skips check for btrs root fs before gmond starts
Group:          System/Monitoring
Requires:       ganglia-gmetad

%description gmetad-skip-bcheck
Skips test for btrfs-root before gmond service start by touching a config file. 
No needed if no btrfs-root is used or statedir is on seperare mount.
Avoids potential data loss on rollback

%package devel
Summary:        Ganglia static libraries and header files
Group:          Development/Libraries/C and C++
Requires:       libapr1-devel
Requires:       libconfuse-devel
Requires:       libexpat-devel
Requires:       libganglia%{lib_version} = %{version}

%description devel
The Ganglia Monitoring Core library provides a set of functions that programmers
can use to build scalable cluster or grid applications

%package -n libganglia%{lib_version}
Summary:        Ganglia Shared Libraries http://ganglia.sourceforge.net/
Group:          System/Libraries
Provides:       libganglia-3_7_2 = %{version}
Obsoletes:      libganglia-3_7_2 < %{version}

%description -n libganglia%{lib_version}
The Ganglia Shared Libraries contains common libraries required by both gmond and
gmetad packages


%prep
%setup -q
%patch1 -p1
%patch2
%patch3
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

%build
export LIBS="-ltirpc"
%configure --with-gmetad \
           --enable-status \
           --sysconfdir=%{_sysconfdir}/%{name} \
           --enable-setuid=daemon \
           --enable-setgid=nogroup \
           --disable-static \
           --enable-shared \
           --sysconfdir=%{_sysconfdir}/%{name} \
	   --localstatedir=%{_localstatedir}
make %{?_smp_mflags}

%install
# Create the directory structure
install -d -m 0755 %{buildroot}/var/lib/ganglia/rrds

# Move the files into the structure
install -d -m 0755 %{buildroot}%{_sbindir}

install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -d -m 0755 %{buildroot}%{_libdir}/ganglia/python_modules

# We just output the default gmond.conf from gmond using the '-t' flag
LD_LIBRARY_PATH=lib/.libs  gmond/gmond -t > %{buildroot}%{_sysconfdir}/%{name}/gmond.conf

cp -f gmond/modules/conf.d/* %{buildroot}%{_sysconfdir}/%{name}/conf.d

# Copy the python metric modules and .conf files
cp -f gmond/python_modules/conf.d/*.pyconf* %{buildroot}%{_sysconfdir}/%{name}/conf.d/
install -m 0755 gmond/python_modules/*/*.py %{buildroot}%{_libdir}/ganglia/python_modules/
# Fix env in scripts
%{__sed} -i 's,/usr/bin/env python,/usr/bin/python,' %{buildroot}%{_libdir}/ganglia/python_modules/*.py
# Ugly fix to add right shebang line
for file in %{buildroot}%{_libdir}/ganglia/python_modules/*.py; do grep '#!/usr/bin/python' $file || sed -i '1s,^,#!/usr/bin/python\n,' $file ;done  
pushd  %{buildroot}%{_libdir}/ganglia/python_modules/
%py_compile . 
popd
# Don't install the example modules
rm -f %{buildroot}%{_sysconfdir}/%{name}/conf.d/example.conf
rm -f %{buildroot}%{_sysconfdir}/%{name}/conf.d/example.pyconf
rm -f %{buildroot}%{_sysconfdir}/%{name}/conf.d/spfexample.pyconf

# Clean up the .conf.in files
rm -f %{buildroot}%{_sysconfdir}/%{name}/conf.d/*.conf.in

# Disable the multicpu module until it is configured properly
mv %{buildroot}%{_sysconfdir}/%{name}/conf.d/multicpu.conf %{buildroot}%{_sysconfdir}/%{name}/conf.d/multicpu.conf.disabled

make DESTDIR=%{buildroot} install
make -C gmond gmond.conf.5

# Remove .la files
rm  %{buildroot}%{_libdir}/*.la

%fdupes %{buildroot}
#rc file needed by systemd
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcgmond
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcgmetad
# copy check for btrs-root-fs
cp -f %SOURCE1 %{buildroot}%{_libdir}/ganglia/
cat > %{buildroot}%{_sysconfdir}/ganglia/no_btrfs_check <<EOF
This file belongs to the package %name-gmond-skip-bcheck 
skips the test for a btrfs root
EOF

%pre  gmetad
%service_add_pre gmetad.service

%pre gmond
%service_add_pre gmond.service

%post   -n libganglia%{lib_version} -p /sbin/ldconfig

%postun -n libganglia%{lib_version} -p /sbin/ldconfig

%post gmetad
%service_add_post gmetad.service

if [ -e /etc/gmetad.conf ]; then
  ln -s /etc/gmetad.conf %{_sysconfdir}/%{name}
fi

%post gmond
%service_add_post gmond.service

# Only do on update and when /sys and /proc are mounted.
# This avoids problems with post build scripts.
if [ $1 -gt 1 -a -d /sys/block -a -d /proc/sys ] ; then
  LEGACY_GMOND_CONF=%{_sysconfdir}/%{name}/gmond.conf
  if [ -e /etc/gmond.conf ] ; then
    LEGACY_GMOND_CONF=/etc/gmond.conf
  fi

  METRIC_LIST="`%{_sbindir}/gmond -c ${LEGACY_GMOND_CONF} -m`"
  if [[ $? != 0 ]] ; then
    # They may have an old configuration file format
    echo "-----------------------------------------------------------"
    echo "IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT"
    echo "-----------------------------------------------------------"
    echo "Parsing your gmond.conf file failed"
    echo "It appears that you are upgrading from ganglia gmond version"
    echo "2.5.x.  The configuration file has changed and you need to "
    echo "convert your old 2.5.x configuration file to the new format."
    echo ""   
    echo "To convert your old configuration file to the new format"
    echo "simply run the command:"
    echo ""
    echo "% gmond --convert old.conf > new.conf"
    echo ""
    echo "This conversion was not made automatic to prevent unknowningly"
    echo "altering your configuration without your notice."
  else
    if [ `echo "$METRIC_LIST" | wc -l` -eq 1 ] ; then
      echo "-----------------------------------------------------------"
      echo "IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT"
      echo "-----------------------------------------------------------"
      echo "No metrics detected - perhaps you are using a gmond.conf"
      echo "file from Ganglia 3.0 or earlier."
      echo "Please see the README file for details about how to"
      echo "create a valid configuration."
    else
      if [ -e /etc/gmond.conf ]; then
        mv /etc/gmond.conf %{_sysconfdir}/%{name}
      fi
    fi
  fi
fi

%preun gmetad
%service_del_preun gmetad.service

%preun gmond
%service_del_preun gmond.service

%postun gmetad
%service_del_postun gmetad.service

%postun gmond
%service_del_postun gmond.service

%files gmetad
%defattr(-,root,root)
%attr(0755,nobody,nobody) /var/lib/ganglia/
%{_sbindir}/gmetad
%{_mandir}/man1/gmetad*1*
%{_unitdir}/gmetad.service
%{_sbindir}/rcgmetad
%attr(0755,-,-) %{_libdir}/ganglia/btrfs-subvol-test.sh
%config(noreplace) %{_sysconfdir}/%{name}/gmetad.conf

%files gmond
%defattr(-,root,root)
%{_bindir}/gmetric
%{_bindir}/gstat
%{_sbindir}/gmond
%{_unitdir}/gmond.service
%{_sbindir}/rcgmond
%{_mandir}/man1/gmetric.1*
%{_mandir}/man1/gmond.1*
%{_mandir}/man1/gstat.1*
%{_mandir}/man5/gmond.conf.5*
%config(noreplace) %{_sysconfdir}/%{name}/gmond.conf
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d/
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/modgstatus.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/multicpu.conf.disabled
%dir %{_libdir}/ganglia/
%{_libdir}/ganglia/modmulticpu.so*
%{_sysconfdir}/%{name}/conf.d/multicpu.conf*
%{_libdir}/ganglia/modcpu.so*
%{_libdir}/ganglia/moddisk.so*
%{_libdir}/ganglia/modgstatus.so
%{_libdir}/ganglia/modload.so*
%{_libdir}/ganglia/modmem.so*
%{_libdir}/ganglia/modnet.so*
%{_libdir}/ganglia/modproc.so*
%{_libdir}/ganglia/modsys.so*

%files gmond-modules-python
%defattr(-,root,root,-)
%dir %{_libdir}/ganglia/python_modules/
%{_libdir}/ganglia/python_modules/*.py*
%{_libdir}/ganglia/modpython.so*
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/modpython.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.pyconf*

%files gmetad-skip-bcheck
%config %{_sysconfdir}/ganglia/no_btrfs_check

%files devel
%defattr(-,root,root,-)
%{_includedir}/ganglia.h
%{_includedir}/ganglia_gexec.h
%{_includedir}/gm_file.h
%{_includedir}/gm_metric.h
%{_includedir}/gm_mmn.h
%{_includedir}/gm_msg.h
%{_includedir}/gm_protocol.h
%{_includedir}/gm_value.h
%{_libdir}/libganglia*.so
%{_bindir}/ganglia-config

%files -n libganglia%{lib_version}
%defattr(-,root,root,-)
%{_libdir}/libganglia*.so.*

%changelog
