#
# spec file for package glusterfs
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


Name:           glusterfs
Version:        5.5
Release:        0
Summary:        Aggregating distributed file system
License:        GPL-2.0-only OR LGPL-3.0-or-later
Group:          System/Filesystems
Url:            http://www.gluster.org/

#Git-Clone:	git://github.com/gluster/glusterfs
#Git-Clone:	git://github.com/fvzwieten/lsgvt
Source:         https://download.gluster.org/pub/gluster/glusterfs/5/5.5/glusterfs-5.5.tar.gz
BuildRequires:  acl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libaio-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python2
BuildRequires:  readline-devel
BuildRequires:  rpcgen
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(fuse) >= 2.6.5
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
%{?systemd_requires}

%description
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file system.
GlusterFS is one of the most sophisticated file systems in terms of
features and extensibility. It borrows a powerful concept called
Translators from GNU Hurd kernel. Much of the code in GlusterFS is in
user space and easily manageable.

%package -n libgfapi0
Summary:        GlusterFS API library
Group:          System/Libraries

%description -n libgfapi0
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package -n libgfchangelog0
Summary:        GlusterFS volume changelog translator library
Group:          System/Libraries

%description -n libgfchangelog0
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

The goal of this volume translator is to capture changes performed on
a GlusterFS volume. The translator needs to be loaded on the server
(bricks) and captures changes in a plain text file inside a
configured directory path (controlled by the "changelog-dir"
directive).

%package -n libgfrpc0
Summary:        GlusterFS Remote Procedure Call library
Group:          System/Libraries

%description -n libgfrpc0
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package -n libgfxdr0
Summary:        GlusterFS's External Data Representation library
Group:          System/Libraries

%description -n libgfxdr0
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package -n libglusterfs0
Summary:        GlusterFS's core library
Group:          System/Libraries

%description -n libglusterfs0
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package -n libgfdb0
Summary:        GlusterFS's database library
Group:          System/Libraries

%description -n libgfdb0
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package -n python-gluster
Summary:        Python bindings for GlusterFS
Group:          Development/Languages/Python

%description -n python-gluster
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package devel
Summary:        Development files for glusterfs
Group:          Development/Libraries/C and C++
Requires:       %name = %version
Requires:       libacl-devel
Requires:       libgfapi0 = %version
Requires:       libgfchangelog0 = %version
Requires:       libgfrpc0 = %version
Requires:       libgfxdr0 = %version
Requires:       libglusterfs0 = %version

%description devel
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

This package provides development files such as headers and library
links.

%prep
%setup -q
#%patch -P 2 -p1
>contrib/sunrpc/xdr_sizeof.c

%build
%define _lto_cflags %{nil}
./autogen.sh
%configure \
    --disable-static \
    --disable-silent-rules
make %{?_smp_mflags} V=0
find . -name 'xdr_sizeof*' -type f -exec ls -lgo {} + || :

%install
b="%buildroot"
%make_install docdir="%_docdir/%name"
find "$b" -type f -name "*.la" -delete -print
mkdir -p "$b/%_localstatedir/log"/{glusterd,glusterfs,glusterfsd}

# The things seemingly forgotten by make install.
# - Manually populate devel dirs
mkdir -p "$b/%_includedir/%name"
install -pm0644 libglusterfs/src/*.h "$b/%_includedir/%name/"
# - hekafs wants this:
mkdir -p "$b/%_includedir/%name"/{rpc,server}
install -pm0644 rpc/rpc-lib/src/*.h rpc/xdr/src/*.h \
	"$b/%_includedir/%name/rpc/"
install -pm0644 xlators/protocol/server/src/*.h \
	"$b/%_includedir/%name/server/"
# - wrapper umount script?
# - logrotate entry
mkdir -p "$b/%_localstatedir/log/%name"
# - vim syntax

# - state
mkdir -p "$b/%_localstatedir/lib/glusterd"
perl -i -pe \
	's{^(\s*option working-directory )\S+}{$1 %_localstatedir/lib/glusterd}g' \
	"$b/%_sysconfdir/%name/glusterd.vol"

# W: wrong-file-end-of-line-encoding
perl -i -pe 's{\x0d\x0a}{\x0a}gs' %_docdir/%name/glusterfs-mode.el

# E: env-script-interpreter
perl -i -pe 's{#!/usr/bin/env python}{#!/usr/bin/python}' \
	"$b/%_bindir/glusterfind" \
	"$b/%_sbindirusr/gcron.py" "$b/%_sbindir/snap_scheduler.py" \
	"$b/%_libexecdir/glusterfs"/*.py "$b/%_libexecdir/glusterfs"/*/*.py \
	"$b/%_libexecdir/glusterfs/peer_mountbroker" \
	"$b/%_datadir/glusterfs/scripts"/*.py
perl -i -pe 's{#!/usr/bin/env bash}{#!/bin/bash}' \
	"$b/%_datadir/glusterfs/scripts"/*.sh

mkdir -p "%buildroot/%_unitdir"
ln -s service "%buildroot/%_sbindir/rcglusterd"
chmod u-s "%buildroot/%_bindir/fusermount-glusterfs"
rm -f "%buildroot/%_sbindir/conf.py"
%fdupes %buildroot/%_prefix

%pre
%service_add_pre glusterd.service glustereventsd.service glusterfssharedstorage.service

%post
%service_add_post glusterd.service glustereventsd.service glusterfssharedstorage.service

%preun
%service_del_preun glusterd.service glustereventsd.service glusterfssharedstorage.service

%postun
%service_del_postun glusterd.service glustereventsd.service glusterfssharedstorage.service

%post   -n libgfapi0 -p /sbin/ldconfig
%postun -n libgfapi0 -p /sbin/ldconfig
%post   -n libgfchangelog0 -p /sbin/ldconfig
%postun -n libgfchangelog0 -p /sbin/ldconfig
%post   -n libgfrpc0 -p /sbin/ldconfig
%postun -n libgfrpc0 -p /sbin/ldconfig
%post   -n libgfxdr0 -p /sbin/ldconfig
%postun -n libgfxdr0 -p /sbin/ldconfig
%post   -n libglusterfs0 -p /sbin/ldconfig
%postun -n libglusterfs0 -p /sbin/ldconfig
%post   -n libgfdb0 -p /sbin/ldconfig
%postun -n libgfdb0 -p /sbin/ldconfig

%files
%doc COPYING-GPLV2 COPYING-LGPLV3 ChangeLog NEWS README.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/eventsconfig.json
%config(noreplace) %_sysconfdir/%name/g*lusterd.vol
%config(noreplace) %_sysconfdir/%name/glusterfs-logrotate
%config %_sysconfdir/%name/gluster-rsyslog*.conf
%config %_sysconfdir/%name/*.example
%config %_sysconfdir/%name/*-logrotate
%config %_sysconfdir/%name/group-*
%config %_sysconfdir/%name/gsyncd.conf
%_bindir/fusermount-glusterfs
%_bindir/glusterfind
/sbin/mount.%name
%_libexecdir/%name/
%_libdir/%name/
%_sbindir/gluster*
%_sbindir/glfsheal
%_sbindir/rcglusterd
%_sbindir/gcron.py
%_sbindir/gf_attach
%_sbindir/gfind_missing_files
%_sbindir/snap_scheduler.py
%_datadir/glusterfs/
%_mandir/man*/*
%_docdir/%name
%_localstatedir/lib/glusterd
%_localstatedir/log/%name
%_unitdir/glusterd.service
%_unitdir/glustereventsd.service
%_unitdir/glusterfssharedstorage.service
%_libexecdir/ocf

%files -n libgfapi0
%_libdir/libgfapi.so.0*

%files -n libgfchangelog0
%_libdir/libgfchangelog.so.0*

%files -n libgfrpc0
%_libdir/libgfrpc.so.0*

%files -n libgfxdr0
%_libdir/libgfxdr.so.0*

%files -n libglusterfs0
%_libdir/libglusterfs.so.0*

%files -n libgfdb0
%_libdir/libgfdb.so.0*

%files -n python-gluster
%dir %python_sitelib/gluster
%dir %python_sitelib/gluster/glupy
%python_sitelib/gluster/__init__.*
%python_sitelib/gluster/cliutils/
%python_sitelib/gluster/glupy/__init__.*

%files devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
