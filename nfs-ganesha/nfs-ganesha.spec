#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%define __arch_install_post /usr/lib/rpm/check-rpaths /usr/lib/rpm/check-buildroot

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%global with_nfsidmap 1
%else
%global with_nfsidmap 0
%endif

%if 0%{?suse_version}
BuildRequires: distribution-release
%global with_nfsidmap 1
%endif

# Conditionally enable some FSALs, disable others.
#
# 1. rpmbuild accepts these options (gpfs as example):
#    --with gpfs
#    --without gpfs

%define on_off_switch() %%{?with_%1:ON}%%{!?with_%1:OFF}

# A few explanation about % bcond_with and % bcond_without
# /!\ be careful: this syntax can be quite messy
# % bcond_with means you add a "--with" option, default = without this feature
# % bcond_without adds a"--without" so the feature is enabled by default

%bcond_without nullfs
%global use_fsal_null %{on_off_switch nullfs}

%bcond_with mem
%global use_fsal_mem %{on_off_switch mem}

%bcond_with gpfs
%global use_fsal_gpfs %{on_off_switch gpfs}

%bcond_without xfs
%global use_fsal_xfs %{on_off_switch xfs}

%bcond_with lustre
%global use_fsal_lustre %{on_off_switch lustre}

%bcond_without ceph
%global use_fsal_ceph %{on_off_switch ceph}

%bcond_without rgw
%global use_fsal_rgw %{on_off_switch rgw}

%bcond_with gluster
%global use_fsal_gluster %{on_off_switch gluster}

%bcond_with panfs
%global use_fsal_panfs %{on_off_switch panfs}

%bcond_with rdma
%global use_rdma %{on_off_switch rdma}

%bcond_with jemalloc

%bcond_with lttng
%global use_lttng %{on_off_switch lttng}

%bcond_with utils
%global use_utils %{on_off_switch utils}

%bcond_with gui_utils
%global use_gui_utils %{on_off_switch gui_utils}

%bcond_with system_ntirpc
%global use_system_ntirpc %{on_off_switch system_ntirpc}

%bcond_without man_page
%global use_man_page %{on_off_switch man_page}

%bcond_without rados_recov
%global use_rados_recov %{on_off_switch rados_recov}

%bcond_without rados_urls
%global use_rados_urls %{on_off_switch rados_urls}

%bcond_without rpcbind
%global use_rpcbind %{on_off_switch rpcbind}

%bcond_with mspac_support
%global use_mspac_support %{on_off_switch mspac_support} 

%bcond_with sanitize_address
%global use_sanitize_address %{on_off_switch sanitize_address}

%global dev_version %{lua: s = string.gsub('@GANESHA_EXTRA_VERSION@', '^%-', ''); s2 = string.gsub(s, '%-', '.'); print((s2 ~= nil and s2 ~= '') and s2 or "0.1") }

%define sourcename @CPACK_SOURCE_PACKAGE_FILE_NAME@

Name:		nfs-ganesha
Version: 2.8.dev.29+git.1557746732.251ace12d
Release:	0
Summary:	An NFS server running in user space
Group:		Productivity/Networking/NFS
License:	LGPL-3.0+ and GPL-3.0+
Url:		https://github.com/nfs-ganesha/nfs-ganesha/wiki

Source:		%{name}-%{version}.tar.bz2

%if 0%{?suse_version}
%if 0%{?is_opensuse}
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le
%else
ExclusiveArch:  x86_64 aarch64
%endif
%endif

BuildRequires:	cmake
BuildRequires:	bison flex
BuildRequires:	flex
BuildRequires:	pkgconfig
BuildRequires:	krb5-devel
BuildRequires:  liburcu-devel
%if ( 0%{?suse_version} >= 1330 )
BuildRequires:  libnsl-devel
%endif
%if ( 0%{?suse_version} )
BuildRequires:	dbus-1-devel
Requires:	dbus-1
%else
BuildRequires:	dbus-devel
Requires:	dbus
%endif

BuildRequires:	libcap-devel
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
%if %{with mspac_support}
BuildRequires:	libwbclient-devel
%endif
BuildRequires:	gcc-c++
%if %{with system_ntirpc}
BuildRequires: libntirpc-devel >= 1.3.1
%endif
%if %{with sanitize_address}
BuildRequires:	libasan
%endif
Requires:	nfs-utils

%if ( 0%{?with_rpcbind} )
%if ( 0%{?fedora} ) || ( 0%{?rhel} && 0%{?rhel} >= 6 ) || ( 0%{?suse_version} )
Requires:	rpcbind
%else
Requires:	portmap
%endif
%endif

%if %{with_nfsidmap}
%if ( 0%{?suse_version} )
BuildRequires:	nfsidmap-devel
%else
BuildRequires:	libnfsidmap-devel
%endif
%else
BuildRequires: nfs-utils-lib-devel
%endif

%if %{with rdma}
BuildRequires:	libmooshika-devel >= 0.6-0
%endif
%if %{with jemalloc}
BuildRequires:	jemalloc-devel
%endif
%if 0%{?suse_version}
BuildRequires:  pkgconfig(systemd)
BuildRequires:	systemd-rpm-macros
%{?systemd_ordering}
PreReq:         %fillup_prereq
Requires(post): procps
%else
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
%endif

%if %{with man_page}
BuildRequires: python3-Sphinx
%endif

# Use CMake variables

%description
NFS-Ganesha is an NFS server running in userspace. It comes with various
back-end modules (called File System Abstraction Layers - FSALs) for different
file systems and name-spaces (notably the Ceph "file" and "object" back-ends -
CephFS and RGW, respectively).

%package -n libntirpc1_7
Summary:        NFS-Ganesha transport-independent RPC (TI-RPC) shared library
Group:          System/Libraries
%description -n libntirpc1_7
This package contains a new implementation of the original libtirpc, 
transport-independent RPC (TI-RPC) library for NFS-Ganesha. It has
the following features not found in libtirpc:
 1. Bi-directional operation
 2. Full-duplex operation on the TCP (vc) transport
 3. Thread-safe operating modes
 3.1 new locking primitives and lock callouts (interface change)
 3.2 stateless send/recv on the TCP transport (interface change)
 4. Flexible server integration support
 5. Event channels (remove static arrays of xprt handles, new EPOLL/KEVENT
    integration)

%post -n libntirpc1_7 -p /sbin/ldconfig

%postun -n libntirpc1_7 -p /sbin/ldconfig

%package -n libntirpc-devel
Summary:        Copy of TIRPC headers from NFS-Ganesha
Group:          Development/Libraries/C and C++
Requires:       libntirpc1_7 = %{version}
Obsoletes:      nfs-ganesha-devel < %{version}
%description -n libntirpc-devel
This package contains the libraries and headers needed to develop programs
using NFS-Ganesha transport-independent RPC (TI-RPC).

%package -n libganesha_nfsd2_8
Summary:        NFS-Ganesha NFSD shared library
Group:          System/Libraries
%description -n libganesha_nfsd2_8
This package contains the NFSD shared library from NFS-Ganesha.

%post -n libganesha_nfsd2_8 -p /sbin/ldconfig

%postun -n libganesha_nfsd2_8 -p /sbin/ldconfig

%package -n libganesha_nfsd-devel
Summary:        NFS-Ganesha NFSD shared library
Group:          Development/Libraries/C and C++
Requires:       libganesha_nfsd2_8 = %{version}
%description -n libganesha_nfsd-devel
This package contains the libraries and headers needed to develop programs
using NFS-Ganesha NFSD.

%package mount-9P
Summary: a 9p mount helper
Group: System/Filesystems
%description mount-9P
This package contains the mount.9P script that clients can use
to simplify mounting to NFS-Ganesha. This is a 9p mount helper.

%package vfs
Summary: VFS backend for NFS-Ganesha
Group: Productivity/Networking/NFS
BuildRequires: libattr-devel
Requires: nfs-ganesha = %{version}-%release
%description vfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support VFS based filesystems

%package proxy
Summary: PROXY-based filesystem backend for NFS-GANESHA
Group: Productivity/Networking/NFS
BuildRequires: libattr-devel
Requires: nfs-ganesha = %{version}-%{release}
%description proxy
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PROXY based filesystems

%if %{with utils}
%package utils
Summary: The NFS-Ganesha utility scripts
Group: Productivity/Networking/NFS
%if ( 0%{?suse_version} )
Requires:	dbus-1-python
Requires:       python-gobject2
Requires:       python-pyparsing
%else
Requires:	dbus-python
Requires:       pygobject2
Requires:       pyparsing
%endif
%if %{with gui_utils}
%if ( 0%{?suse_version} )
BuildRequires:	python-qt4-devel
Requires:	python-qt4
%else
BuildRequires:	PyQt4-devel
Requires:	PyQt4
%endif
%endif
BuildRequires:  python-devel
Requires:       nfs-ganesha = %{version}-%{release}
Requires:       python
%description utils
This package contains utility scripts for managing the NFS-Ganesha server
%endif

%if %{with lttng}
%package lttng
Summary: The NFS-Ganesha library for use with LTTng
Group: Productivity/Networking/NFS
BuildRequires: lttng-ust-devel >= 2.3
BuildRequires: lttng-tools-devel >= 2.3
Requires:      nfs-ganesha = %{version}-%{release}
Requires:      lttng-tools >= 2.3
Requires:      lttng-ust >= 2.3
%description lttng
This package contains the libganesha_trace.so library. When preloaded
to the ganesha.nfsd server, it makes it possible to trace using LTTng.
%endif

%if %{with rados_recov}
%package rados-grace
Summary: The NFS-Ganesha command for managing the RADOS grace database
BuildRequires: librados-devel >= 0.61
Requires: nfs-ganesha = %{version}-%{release}
%description rados-grace
This package contains the ganesha-rados-grace tool for interacting with the
database used by the rados_cluster recovery backend.
%endif

# Option packages start here. use "rpmbuild --with gpfs" (or equivalent)
# for activating this part of the spec file

# NULL
%if %{with nullfs}
%package nullfs
Summary: "null" filesystem backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires: nfs-ganesha = %{version}-%{release}
%description nullfs
This package contains a Stackable FSAL shared object to
be used with NFS-Ganesha. This is mostly a template for future (more sophisticated) stackable FSALs
%endif

# MEM
%if %{with mem}
%package mem
Summary: Memory-backed testing filesystem backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires: nfs-ganesha = %{version}-%{release}
%description mem
This package contains a FSAL shared object to be used with NFS-Ganesha.  This
is used for speed and latency testing.
%endif

# GPFS
%if %{with gpfs}
%package gpfs
Summary: GPFS backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires: nfs-ganesha = %{version}-%{release}
%description gpfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support GPFS backend
%endif

# CEPH
%if %{with ceph}
%package ceph
Summary: CephFS backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires:	nfs-ganesha = %{version}-%{release}
Requires:       ceph-common
BuildRequires:	libcephfs-devel >= 10.2.0
%description ceph
This package contains the Ceph "file" (CephFS) File System Abstraction Layer
(FSAL).
%endif

# RGW
%if %{with rgw}
%package rgw
Summary: Ceph RADOS Gateway backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires:	nfs-ganesha = %{version}-%{release}
Requires:       ceph-common
BuildRequires:	librgw-devel >= 10.2.0
%description rgw
This package contains the Ceph "object" (RGW) File System Abstraction Layer
(FSAL).
%endif

# XFS
%if %{with xfs}
%package xfs
Summary: XFS backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires:	nfs-ganesha = %{version}-%{release}
BuildRequires:	libattr-devel xfsprogs-devel
%description xfs
This package contains the XFS File System Abstraction Layer (FSAL)
for use with NFS-Ganesha, providing correct XFS support.
%endif

#LUSTRE
%if %{with lustre}
%package lustre
Summary: Lustre backend for NFS-Ganesha
Group: Productivity/Networking/NFS
BuildRequires: libattr-devel
BuildRequires: lustre-client
Requires: nfs-ganesha = %{version}-%{release}
Requires: lustre-client
%description lustre
This package contains a FSAL shared object to
be used with NFS-Ganesha to support LUSTRE based filesystems
%endif

# PANFS
%if %{with panfs}
%package panfs
Summary: PANFS backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires:	nfs-ganesha = %{version}-%{release}
%description panfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PANFS
%endif

# GLUSTER
%if %{with gluster}
%package gluster
Summary: Gluster filesystem backend for NFS-Ganesha
Group: Productivity/Networking/NFS
Requires:	nfs-ganesha = %{version}-%{release}
BuildRequires:        glusterfs-api-devel >= 3.8
BuildRequires:        libacl-devel libattr-devel
%description gluster
This package contains a FSAL shared object to
be used with NFS-Ganesha to support Gluster
%endif

%prep
%setup -q

%build
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_TYPE=en_US.UTF-8
cmake .	-DCMAKE_BUILD_TYPE=Release			\
	-DBUILD_CONFIG=rpmbuild				\
	-DUSE_FSAL_NULL=%{use_fsal_null}		\
	-DUSE_FSAL_MEM=%{use_fsal_mem}			\
	-DUSE_FSAL_XFS=%{use_fsal_xfs}			\
	-DUSE_FSAL_LUSTRE=%{use_fsal_lustre}			\
	-DUSE_FSAL_CEPH=%{use_fsal_ceph}		\
	-DUSE_FSAL_RGW=%{use_fsal_rgw}			\
	-DUSE_FSAL_GPFS=%{use_fsal_gpfs}		\
	-DUSE_FSAL_PANFS=%{use_fsal_panfs}		\
	-DUSE_FSAL_GLUSTER=%{use_fsal_gluster}		\
	-DUSE_SYSTEM_NTIRPC=%{use_system_ntirpc}	\
	-DUSE_9P_RDMA=%{use_rdma}			\
	-DUSE_LTTNG=%{use_lttng}			\
	-DUSE_ADMIN_TOOLS=%{use_utils}			\
	-DUSE_GUI_ADMIN_TOOLS=%{use_gui_utils}		\
	-DUSE_RADOS_RECOV=%{use_rados_recov}		\
	-DRADOS_URLS=%{use_rados_urls}			\
	-DUSE_FSAL_VFS=ON				\
	-DUSE_FSAL_PROXY=ON				\
	-DUSE_DBUS=ON					\
	-DUSE_9P=ON					\
	-DDISTNAME_HAS_GIT_DATA=OFF			\
	-DUSE_MAN_PAGE=%{use_man_page}                  \
	-DRPCBIND=%{use_rpcbind}			\
	-D_MSPAC_SUPPORT=%{use_mspac_support}		\
	-DSANITIZE_ADDRESS=%{use_sanitize_address}	\
%if %{with jemalloc}
	-DALLOCATOR=jemalloc
%endif

make %{?_smp_mflags} || make %{?_smp_mflags} || make

%install
mkdir -p %{buildroot}%{_sysconfdir}/ganesha/
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}/ganesha
mkdir -p %{buildroot}%{_localstatedir}/run/ganesha
mkdir -p %{buildroot}%{_libexecdir}/ganesha
mkdir -p %{buildroot}%{_docdir}/ganesha
mkdir -p %{buildroot}/usr/share/doc/ganesha/config_samples
install -m 644 LICENSE.txt %{buildroot}%{_docdir}/ganesha/LICENSE.txt
install -m 644 config_samples/logrotate_ganesha	%{buildroot}%{_sysconfdir}/logrotate.d/ganesha
install -m 644 scripts/ganeshactl/org.ganesha.nfsd.conf	%{buildroot}%{_sysconfdir}/dbus-1/system.d
install -m 755 scripts/nfs-ganesha-config.sh %{buildroot}%{_libexecdir}/ganesha
install -m 755 tools/mount.9P	%{buildroot}%{_sbindir}/mount.9P

install -m 644 config_samples/vfs.conf %{buildroot}%{_sysconfdir}/ganesha

install -D -m 444 scripts/systemd/nfs-ganesha.service.el7 %{buildroot}%{_unitdir}/nfs-ganesha.service
install -D -m 444 scripts/systemd/nfs-ganesha-lock.service.el7 %{buildroot}%{_unitdir}/nfs-ganesha-lock.service
install -D -m 444 scripts/systemd/nfs-ganesha-config.service %{buildroot}%{_unitdir}/nfs-ganesha-config.service
%if 0%{?suse_version}
install -D -m 644 scripts/systemd/sysconfig/nfs-ganesha %{buildroot}%{_fillupdir}/sysconfig.nfs-ganesha
%else
install -D -m 644 scripts/systemd/sysconfig/nfs-ganesha %{buildroot}%{_sysconfdir}/sysconfig/ganesha
%endif
%if 0%{?_tmpfilesdir:1}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 scripts/systemd/tmpfiles.d/ganesha.conf	%{buildroot}%{_tmpfilesdir}
%endif
mkdir -p %{buildroot}%{_localstatedir}/log/ganesha

%if %{with xfs}
install -m 644 config_samples/xfs.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with ceph}
install -m 644 config_samples/ceph.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with rgw}
install -m 644 config_samples/rgw.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/rgw_bucket.conf %{buildroot}%{_sysconfdir}/ganesha
%endif

%if %{with gpfs}
install -m 755 scripts/gpfs-epoch %{buildroot}%{_libexecdir}/ganesha
install -m 644 config_samples/gpfs.conf	%{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.nfsd.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.main.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.log.conf %{buildroot}%{_sysconfdir}/ganesha
install -m 644 config_samples/gpfs.ganesha.exports.conf	%{buildroot}%{_sysconfdir}/ganesha
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 755 scripts/init.d/nfs-ganesha.gpfs		%{buildroot}%{_sysconfdir}/init.d/nfs-ganesha-gpfs
%endif

%make_install

%if ( 0%{?suse_version} )
%pre
%service_add_pre nfs-ganesha.service nfs-ganesha-lock.service nfs-ganesha-config.service
getent group ganesha > /dev/null || groupadd -r ganesha
getent passwd ganesha > /dev/null || useradd -r -g ganesha -d /var/run/ganesha -s /sbin/nologin -c "NFS-Ganesha Daemon" ganesha
exit 0

%endif

%post
%if ( 0%{?suse_version} )
%service_add_post nfs-ganesha.service nfs-ganesha-lock.service nfs-ganesha-config.service
%fillup_only
%else
%systemd_post nfs-ganesha-lock.service
%endif
pgrep dbus-daemon >/dev/null 2>&1 && killall -SIGHUP dbus-daemon >/dev/null 2>&1 || :

%preun
%if ( 0%{?suse_version} )
%service_del_preun nfs-ganesha-lock.service
%else
%systemd_preun nfs-ganesha-lock.service
%endif

%postun
%if ( 0%{?suse_version} )
%service_del_postun nfs-ganesha-lock.service
%else
%systemd_postun_with_restart nfs-ganesha-lock.service
%endif

%files
%docdir %{_docdir}/ganesha
%{_bindir}/ganesha.nfsd
%dir %{_libdir}/ganesha
%config %{_sysconfdir}/dbus-1/system.d/org.ganesha.nfsd.conf
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.*
%else
%config(noreplace) %{_sysconfdir}/sysconfig/ganesha
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/ganesha
%dir %{_sysconfdir}/ganesha
%config(noreplace) %{_sysconfdir}/ganesha/ganesha.conf
%dir %{_docdir}/ganesha
%{_docdir}/ganesha/LICENSE.txt
%dir %{_docdir}/ganesha/config_samples
%{_docdir}/ganesha/config_samples/README
%{_docdir}/ganesha/config_samples/ceph.conf
%{_docdir}/ganesha/config_samples/config.txt
%{_docdir}/ganesha/config_samples/ds.conf
%{_docdir}/ganesha/config_samples/export.txt
%{_docdir}/ganesha/config_samples/ganesha.conf.example
%{_docdir}/ganesha/config_samples/gluster.conf
%{_docdir}/ganesha/config_samples/gpfs.conf
%{_docdir}/ganesha/config_samples/gpfs.ganesha.exports.conf
%{_docdir}/ganesha/config_samples/gpfs.ganesha.log.conf
%{_docdir}/ganesha/config_samples/gpfs.ganesha.main.conf
%{_docdir}/ganesha/config_samples/gpfs.ganesha.nfsd.conf
%{_docdir}/ganesha/config_samples/logging.txt
%{_docdir}/ganesha/config_samples/logrotate_fsal_gluster
%{_docdir}/ganesha/config_samples/logrotate_ganesha
%{_docdir}/ganesha/config_samples/lustre.conf
%{_docdir}/ganesha/config_samples/mem.conf
%{_docdir}/ganesha/config_samples/proxy.conf
%{_docdir}/ganesha/config_samples/rgw.conf
%{_docdir}/ganesha/config_samples/rgw_bucket.conf
%{_docdir}/ganesha/config_samples/vfs.conf
%{_docdir}/ganesha/config_samples/xfs.conf
%dir %{_libexecdir}/ganesha
%{_libexecdir}/ganesha/nfs-ganesha-config.sh
%dir %attr(0755,ganesha,ganesha) %{_localstatedir}/log/ganesha

%if %{with man_page}
%{_mandir}/*/ganesha-config.8.gz
%{_mandir}/*/ganesha-core-config.8.gz
%{_mandir}/*/ganesha-export-config.8.gz
%{_mandir}/*/ganesha-cache-config.8.gz
%{_mandir}/*/ganesha-log-config.8.gz
%endif

%{_unitdir}/nfs-ganesha.service
%{_unitdir}/nfs-ganesha-lock.service
%{_unitdir}/nfs-ganesha-config.service
%if 0%{?_tmpfilesdir:1}
%{_tmpfilesdir}/ganesha.conf
%endif

%if ! %{with system_ntirpc}

%files -n libntirpc1_7
%{_libdir}/libntirpc.so.1.7.999
%{_libdir}/libntirpc.so.1.7

%files -n libntirpc-devel
%{_includedir}/ntirpc/
%{_libdir}/libntirpc.so
%{_libdir}/pkgconfig/libntirpc.pc

%endif

%files -n libganesha_nfsd2_8
%{_libdir}/libganesha_nfsd.so.*

%files -n libganesha_nfsd-devel
%{_libdir}/libganesha_nfsd.so

%files mount-9P
%{_sbindir}/mount.9P
%if %{with man_page}
%{_mandir}/*/ganesha-9p-config.8.gz
%endif

%files vfs
%{_libdir}/ganesha/libfsalvfs*
%config(noreplace) %{_sysconfdir}/ganesha/vfs.conf
%if %{with man_page}
%{_mandir}/*/ganesha-vfs-config.8.gz
%endif

%files proxy
%{_libdir}/ganesha/libfsalproxy*
%if %{with man_page}
%{_mandir}/*/ganesha-proxy-config.8.gz
%endif

# Optional packages
%if %{with lustre}
%files lustre
%{_libdir}/ganesha/libfsallustre*
%config(noreplace) %{_sysconfdir}/ganesha/lustre.conf
%if %{with man_page}
%{_mandir}/*/ganesha-lustre-config.8.gz
%endif
%endif

%if %{with nullfs}
%files nullfs
%{_libdir}/ganesha/libfsalnull*
%endif

%if %{with mem}
%files mem
%{_libdir}/ganesha/libfsalmem*
%endif

%if %{with gpfs}
%files gpfs
%{_libdir}/ganesha/libfsalgpfs*
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.nfsd.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.main.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.log.conf
%config(noreplace) %{_sysconfdir}/ganesha/gpfs.ganesha.exports.conf
%{_libexecdir}/ganesha/gpfs-epoch
%if %{with man_page}
%{_mandir}/*/ganesha-gpfs-config.8.gz
%endif
%endif

%if %{with xfs}
%files xfs
%{_libdir}/ganesha/libfsalxfs*
%config(noreplace) %{_sysconfdir}/ganesha/xfs.conf
%if %{with man_page}
%{_mandir}/*/ganesha-xfs-config.8.gz
%endif
%endif

%if %{with ceph}
%files ceph
%{_libdir}/ganesha/libfsalceph*
%config(noreplace) %{_sysconfdir}/ganesha/ceph.conf
%if %{with man_page}
%{_mandir}/*/ganesha-ceph-config.8.gz
%endif
%endif

%if %{with rgw}
%files rgw
%{_libdir}/ganesha/libfsalrgw*
%config(noreplace) %{_sysconfdir}/ganesha/rgw.conf
%config(noreplace) %{_sysconfdir}/ganesha/rgw_bucket.conf
%if %{with man_page}
%{_mandir}/*/ganesha-rgw-config.8.gz
%endif
%endif

%if %{with gluster}
%files gluster
%{_libdir}/ganesha/libfsalgluster*
%if %{with man_page}
%{_mandir}/*/ganesha-gluster-config.8.gz
%endif
%endif

%if %{with panfs}
%files panfs
%{_libdir}/ganesha/libfsalpanfs*
%endif

%if %{with lttng}
%files lttng
%{_libdir}/ganesha/libganesha_trace*
%endif

%if %{with rados_recov}
%files rados-grace
%{_bindir}/ganesha-rados-grace
%if %{with man_page}
%{_mandir}/*/ganesha-rados-grace.8.gz
%{_mandir}/*/ganesha-rados-cluster-design.8.gz
%endif
%endif

%if %{with utils}
%files utils
%if ( 0%{?suse_version} || 0%{?fedora} )
%{python_sitelib}/Ganesha
%{python_sitelib}/Ganesha/*
%{python_sitelib}/ganeshactl-*-info
%else
%{python2_sitelib}/Ganesha
%{python2_sitelib}/Ganesha/*
%{python2_sitelib}/ganeshactl-*-info
%endif
%if %{with gui_utils}
%{_bindir}/ganesha-admin
%{_bindir}/manage_clients
%{_bindir}/manage_exports
%{_bindir}/manage_logger
%{_bindir}/ganeshactl
%{_bindir}/client_stats_9pOps
%{_bindir}/export_stats_9pOps
%endif
%{_bindir}/fake_recall
%{_bindir}/get_clientids
%{_bindir}/grace_period
%{_bindir}/ganesha_stats
%{_bindir}/sm_notify.ganesha
%{_bindir}/ganesha_mgr
%{_bindir}/ganesha_conf
%{_mandir}/man8/ganesha_conf.8.gz
%endif

%changelog
