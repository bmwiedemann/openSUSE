#
# spec file for package openafs
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
# needssslcertforbuild


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
%define _fillupdir /var/adm/fillup-templates
%endif
%define _lto_cflags %{nil}

#
#	TUNABLES
#

# package-wide definitions here

# build authlibs
%define build_authlibs 1

# build kernel modules
%define build_kernel_modules 1

# flag for firewalld, only required for SLE-12
%if 0%{?sle_version} <= 120500 && !0%{?is_opensuse}
%define have_firewalld 0
%else
%define have_firewalld 1
%endif

#
# package internal directories
#
%define afslogsdir        /var/log/openafs
%define afsconfdir        /etc/openafs/server
%define viceetcdir        /etc/openafs
%define vicecachedir	  /var/cache/openafs
%define afslocaldir       /var/lib/openafs

%ifarch ppc64le ppc64 %{arm}
%define build_kernel_modules 0
%endif

# used for %setup only
# leave upstream tar-balls untouched for integrity checks.
%define upstream_version 1.8.9pre2

Name:           openafs

Version:        1.8.9~pre2
Release:        0
Summary:        OpenAFS Distributed File System
License:        IPL-1.0
Group:          System/Filesystems
URL:            http://www.openafs.org/

Source0:        openafs-%{upstream_version}-src.tar.bz2
Source1:        openafs-%{upstream_version}-doc.tar.bz2
Source2:        openafs-%{upstream_version}-src.tar.bz2.md5
Source3:        openafs-%{upstream_version}-doc.tar.bz2.md5
Source4:        openafs-%{upstream_version}-src.tar.bz2.sha256
Source5:        openafs-%{upstream_version}-doc.tar.bz2.sha256

Source10:       README.SUSE.openafs
Source15:       logrotate.openafs-server
Source18:       RELNOTES-%{upstream_version}
Source19:       ChangeLog
Source20:       kernel-source.build-modules.sh
Source23:       openafs-client.service
Source24:       openafs-client.service.allow_unsupported
Source25:       openafs-server.service
Source26:       openafs-fuse-client.service
Source27:       sysconfig.openafs-client
Source28:       sysconfig.openafs-server
Source29:       sysconfig.openafs-fuse-client
Source30:       preamble
Source40:       afs3-bos.xml
Source41:       afs3-callback.xml
Source42:       afs3-fileserver.xml
Source43:       afs3-prserver.xml
Source44:       afs3-rmtsys.xml
Source45:       afs3-update.xml
Source46:       afs3-vlserver.xml
Source47:       afs3-volser.xml
Source55:       openafs.SuidCells
Source56:       openafs.CellAlias
Source57:       openafs.ThisCell
Source58:       openafs.cacheinfo
Source98:       kmp_only.files
Source99:       openafs.changes

# PATCH-FIX-UPSTREAM make configure detect ncurses 6 correctly
Patch4:         4cf7a9a.diff

#	GENERAL BuildRequires and Requires
#

BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  fdupes
%if %{have_firewalld}
BuildRequires:  firewall-macros
%endif
BuildRequires:  flex
BuildRequires:  fuse-devel
BuildRequires:  git
BuildRequires:  krb5-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  swig

Requires(post): %fillup_prereq

%if %{build_kernel_modules}
BuildRequires:  %{kernel_module_package_buildreqs}
%endif

%description
AFS is a cross-platform distributed file system product pioneered at
Carnegie Mellon University and supported and developed as a product by
Transarc Corporation (now IBM Pittsburgh Labs). It offers a
client-server architecture for file sharing, providing location
independence, scalability, and transparent migration capabilities for
data.

In addition, among its features are authentication, encryption,
caching, disconnected operations, replication for higher availability
and load balancing, and ACLs.

%package server
Summary:        OpenAFS File System Server
Group:          System/Filesystems
Requires:       %{name} = %{version}

%description server
AFS is a cross-platform distributed file system product pioneered at
Carnegie Mellon University and supported and developed as a product by
Transarc Corporation (now IBM Pittsburgh Labs). It offers a
client-server architecture for file sharing, providing location
independence, scalability, and transparent migration capabilities for
data.

In addition, among its features are authentication, encryption,
caching, disconnected operations, replication for higher availability
and load balancing, and ACLs. This package contains the static
libraries and header files needed to develop applications for OpenAFS.

%if %{build_authlibs}
%package authlibs
Summary:        OpenAFS authentication shared libraries
Group:          Development/Libraries/C and C++

%description authlibs
The AFS distributed filesystem.  AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides a shared version of libafsrpc and libafsauthent.
None of the programs included with OpenAFS currently use these shared
libraries; however, third-party software that wishes to perform AFS
authentication may link against them.

%package authlibs-devel
Summary:        OpenAFS shared library development
Group:          Development/Libraries/C and C++
Requires:       %{name}-authlibs = %{version}
Requires:       %{name}-devel = %{version}

%description authlibs-devel
The AFS distributed filesystem.  AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package includes the static versions of libafsrpc and
libafsauthent, and symlinks required for building against the dynamic
libraries.

%endif

%package devel
Summary:        OpenAFS Static Libraries and Header Files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
AFS is a cross-platform distributed file system product pioneered at
Carnegie Mellon University and supported and developed as a product by
Transarc Corporation (now IBM Pittsburgh Labs). It offers a
client-server architecture for file sharing, providing location
independence, scalability, and transparent migration capabilities for
data.

In addition, among its features are authentication, encryption,
caching, disconnected operations, replication for higher availability
and load balancing, and ACLs. This package contains the OpenAFS server.

%package kernel-source
Summary:        OpenAFS Kernel Module source tree
Group:          System/Filesystems
Requires:       bison
Requires:       flex
Requires:       gcc
Requires:       kernel-devel
Provides:       openafs-kernel = %{version}

%description kernel-source
The AFS distributed filesystem.  AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides the source code to build your own AFS kernel
module.

%if %{build_kernel_modules}
%package KMP
Summary:        OpenAFS Distributed File System - kernel module
Group:          System/Kernel

%kernel_module_package -x lockdep um pae -p %{S:30}

%description KMP
This package contains the kernel module for OpenAFS. For details see
the openafs package.

%endif

%package fuse_client
Summary:        OpenAFS FUSE File System Client
Group:          System/Filesystems
Conflicts:      %{name}-client
Requires:       %{name} = %{version}

%description fuse_client
AFS is a cross-platform distributed file system product pioneered at
Carnegie Mellon University and supported and developed as a product by
Transarc Corporation (now IBM Pittsburgh Labs). It offers a
client-server architecture for file sharing, providing location
independence, scalability, and transparent migration capabilities for
data.

This client is using the EXPERIMENTAL FUSE interface on LINUX.
It does not offer authentication etc.

%if %{build_kernel_modules}
%package client
Summary:        OpenAFS File System Client
Group:          System/Filesystems
Requires:       %{name} = %{version}
Requires:       %{name}-kmp
Requires:       krb5-client

%description client
AFS is a cross-platform distributed file system product pioneered at
Carnegie Mellon University and supported and developed as a product by
Transarc Corporation (now IBM Pittsburgh Labs). It offers a
client-server architecture for file sharing, providing location
independence, scalability, and transparent migration capabilities for
data.

In addition, among its features are authentication, encryption,
caching, disconnected operations, replication for higher availability
and load balancing, and ACLs. This package contains the OpenAFS client.
%endif

%prep

: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
: @@@
: @@@ package-name:       %{name}
: @@@ file-layout:	  fsh
: @@@ lib dir:    	  %{_libdir}
: @@@ libexec dir:    	  %{libexecdir}
: @@@ bin dir:    	  %{_bindir}
: @@@ sbin dir:    	  %{_sbindir}
: @@@ include dir:    	  %{includedir}
: @@@ sysconf dir:    	  %{_sysconfdir}
: @@@ man dir:    	  %{_mandir}
: @@@ build modules:      %{build_kernel_modules}
: @@@ architecture:       %{_arch}
: @@@ target cpu:         %{_target_cpu}
: @@@
: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

for src_file in %{S:0}  %{S:1}; do
    if [ "`md5sum $src_file | awk '{print $1}'`" != "`cat $src_file.md5 | awk '{print $1}'`" ]; then
        echo "ERROR: MD5-Integrity check for $src_file failed.";
        exit 1
    fi
    if [ "`sha256sum $src_file | awk '{print $1}'`" != "`cat $src_file.sha256 | awk '{print $1}'`" ]; then
        echo "ERROR: SHA256-Integrity check for $src_file failed.";
        exit 1
    fi
done

%setup -q -n openafs-%{upstream_version} -T -b 0 -b 1
%patch4 -p1

./regen.sh

%build
# architecture specific settings
sysbase=%{_arch}

%ifarch ppc
perl -pi -e 's,^(XCFLAGS.*),\1 -fPIC,' src/config/Makefile.ppc_linux24.in
%endif
%ifarch ppc64 ppc64le
sysbase=ppc64
export LDFLAGS="$LDFLAGS -m64"
%endif
%ifarch %{arm}
sysbase=arm
%endif
%ifarch aarch64
sysbase=arm64
%define _arch arm64
%endif
%ifarch s390x
sysbase=s390
%endif
%ifarch x86_64
sysbase=amd64
perl -pi -e 's,^(XCFLAGS.*),\1 -fPIC,' src/config/Makefile.amd64_linux24.in
perl -pi -e 's,^(XLIBS.*),\1 -lresolv,' src/config/Makefile.amd64_linux24.in
%endif

afs_sysname=${sysbase}_linux26

RPM_OPT_FLAGS=`echo ${RPM_OPT_FLAGS} | sed s/-D_FORTIFY_SOURCE=2//`
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC -fcommon"

export KRB5LIBS='-lcom_err -lkrb5'
export PATH_KRB5_CONFIG=%{krb5_config}
export afsdbdir='/var/lib/openafs/db'
export afslocaldir='/var/lib/openafs'
export afslogsdir='/var/log/openafs'
export afsdbdir='/var/lib/openafs/db'
%configure \
    --disable-transarc-paths \
    --disable-pam \
    --disable-strip-binaries \
    --includedir=%{_includedir}/openafs \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --with-afs-sysname=$afs_sysname \
    --disable-kernel-module \
    --with-swig

make CCFLAGS="$CFLAGS" XCFLAGS="$CFLAGS" PAM_CFLAGS="$CFLAGS" KOPTS="$CFLAGS" all_nolibafs
make CCFLAGS="$CFLAGS" XCFLAGS="$CFLAGS" PAM_CFLAGS="$CFLAGS" KOPTS="$CFLAGS" only_libafs_tree

# the test suite need a configured KDC
#make -C src/tests all

# Kernel-module

%if %{build_kernel_modules}
mkdir obj

for flavor in %flavors_to_build; do
    rm -rf obj/$flavor
    cp -a libafs_tree obj/$flavor
    pushd obj/$flavor
    find . -name "*.c" -exec sed -i '/MODULE_LICENSE(/a MODULE_INFO(retpoline, "Y");' "{}" "+"
    ./configure  --with-linux-kernel-build=/usr/src/linux-obj/%{_target_cpu}/$flavor --with-linux-kernel-headers=/usr/src/linux \
        --disable-transarc-paths --without-swig
    export EXTRA_CFLAGS='-DVERSION=\"%version\"'
    export LINUX_MAKE_ARCH="ARCH=%{_arch}"
    make
    popd
done
%endif
# build_kernel_modules

%install

#
# install build binaries using  make

make DESTDIR=%{buildroot} install_nolibafs

#
# man-pages

OLD_PWD=`pwd`
cd doc/man-pages
%make_install
cd $OLD_PWD

#
# create directories
mkdir -p %{buildroot}/%_unitdir
mkdir -p %{buildroot}/%{afslogsdir}/old
mkdir -p %{buildroot}/%{_fillupdir}
mkdir -p %{buildroot}/%{vicecachedir}
mkdir -p %{buildroot}/%{viceetcdir}
mkdir -p %{buildroot}%{_datadir}/openafs/C
mkdir -p %{buildroot}/%{afsconfdir}
mkdir -p %{buildroot}/%{afslocaldir}
mkdir -p %{buildroot}/%{_sbindir}

#
# client
# also used by others
cp -a %{S:56} %{buildroot}/%{viceetcdir}/CellAlias
cp -a %{S:57} %{buildroot}/%{viceetcdir}/ThisCell
cp -a src/afsd/CellServDB %{buildroot}/%{viceetcdir}/CellServDB
cp -a %{S:55} %{buildroot}/%{viceetcdir}/SuidCells
cp -a %{S:58} %{buildroot}/%{viceetcdir}/cacheinfo

# kmp-only
%if %{build_kernel_modules}
cp -a src/afs/afszcm.cat %{buildroot}%{_datadir}/openafs/C
install -m 644 %{S:27} %{buildroot}/%{_fillupdir}/sysconfig.openafs-client
%if 0%{?sle_version} > 150000
install -m 644 %{S:24} %{buildroot}/%_unitdir/openafs-client.service
%else
install -m 644 %{S:23} %{buildroot}/%_unitdir
%endif
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcopenafs-client
%endif

#
# fuse client package

install -m 644 %{S:29} %{buildroot}/%{_fillupdir}/sysconfig.openafs-fuse-client
install -m 644 %{S:26} %{buildroot}/%_unitdir
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcopenafs-fuse-client

#
# server
install -m 644 %{S:28} %{buildroot}/%{_fillupdir}/sysconfig.openafs-server
install -m 644 %{S:25} %{buildroot}/%_unitdir
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcopenafs-server

#
# kernel-source
mkdir -p %{buildroot}/usr/src/kernel-modules/openafs
chmod -R o-w src/libafs
chmod -R o-w libafs_tree
cp -a libafs_tree %{buildroot}/usr/src/kernel-modules/openafs
install -m 755 %{S:20} %{buildroot}/usr/src/kernel-modules/openafs/build-modules.sh
install -m 644 LICENSE %{buildroot}/usr/src/kernel-modules/openafs/LICENSE

# KMP
%if %{build_kernel_modules}
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates

for flavor in %flavors_to_build; do
    make -C /usr/src/linux-obj/%{_arch}/$flavor %{?linux_make_arch} modules_install \
        M=$PWD/`find obj/$flavor/ -name MODLOAD-\* -type d`
done
%endif

#
# main package
cp -a %{S:10} README.SUSE
cp -a %{S:18} RELNOTES
cp -a %{S:19} ChangeLog

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo %{_libdir}/openafs > %{buildroot}/etc/ld.so.conf.d/openafs.conf

# move some bin to sbin
mv %{buildroot}/%{_bindir}/asetkey %{buildroot}/%{_sbindir}/asetkey
mv %{buildroot}/%{_bindir}/bos %{buildroot}/%{_sbindir}/bos
mv %{buildroot}/%{_bindir}/akeyconvert %{buildroot}/%{_sbindir}/akeyconvert
mv %{buildroot}/%{_bindir}/udebug %{buildroot}/%{_sbindir}/udebug

# avoid conflicts with other packages by adding the prefix afs_ to filenames
mv %{buildroot}%{_bindir}/scout %{buildroot}%{_bindir}/afs_scout
cat %{buildroot}/%{_mandir}/man1/scout.1 | sed 's/\<scout\>/afs_scout/g' > %{buildroot}/%{_mandir}/man1/afs_scout.1
rm %{buildroot}/%{_mandir}/man1/scout.1
mv %{buildroot}%{_sbindir}/backup %{buildroot}%{_sbindir}/afs_backup
OLD_PWD=`pwd`
cd %{buildroot}/%{_mandir}/man8/
for f in $(ls backup*); do
    cat $f | sed 's/\<backup\>/afs_backup/g' > afs_"$f"
    rm $f
done
cd $OLD_PWD

# create manpage for afsd.fuse as a real file
rm %{buildroot}/%{_mandir}/man8/afsd.fuse.8
cp -p %{buildroot}/%{_mandir}/man8/afsd.8 %{buildroot}/%{_mandir}/man8/afsd.fuse.8

# move  %%{_libdir}/afs-stuff to %%{_libdir}/openafs
mv %{buildroot}/%{_libdir}/afs/* %{buildroot}/%{_libdir}/openafs
mv %{buildroot}/%{_libdir}/*.* %{buildroot}/%{_libdir}/openafs
rm -rf %{buildroot}/%{_libdir}/afs

# move perl module to perl vendor library path
mkdir -p %{buildroot}/%{perl_vendorlib}/AFS
mv %{buildroot}/%{_libdir}/perl/AFS/ukernel.pm %{buildroot}/%{perl_vendorlib}/AFS/ukernel.pm
mkdir -p %{buildroot}%{perl_vendorarch}
mv %{buildroot}/%{_libdir}/perl/ukernel.so %{buildroot}/%{perl_vendorarch}/ukernel.so

# firewalld

%if %{have_firewalld}
mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:40} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:41} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:42} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:43} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:44} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:45} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:46} %{buildroot}%{_prefix}/lib/firewalld/services/
install -D -m 644 %{S:47} %{buildroot}%{_prefix}/lib/firewalld/services/
%endif

#
# general cleanup
#

# we supposedly don't need this on linux
rm %{buildroot}/%{_sbindir}/rmtsysd

%if ! %{build_authlibs}
rm %{buildroot}/%{_libdir}/libafsauthent.so.*
rm %{buildroot}/%{_libdir}/libafsrpc.so.*
rm %{buildroot}/%{_libdir}/libkopenafs.so.*
rm %{buildroot}/%{_libdir}/libafsauthent.so
rm %{buildroot}/%{_libdir}/libafsrpc.so
rm %{buildroot}/%{_libdir}/libkopenafs.so
%endif
%if ! %{build_kernel_modules}
for f in $(cat %{S:98}); do
    rm -f %{buildroot}/$f
done
%endif

# remove all static libraries
find %{buildroot} -type f -name "*.a" -delete

# remove unused man pages
for x in dlog symlink symlink_list symlink_make symlink_remove; do
    rm %{buildroot}/%{_mandir}/man1/${x}.1
done
for x in rmtsysd xfs_size_check aklog_dynamic_auth; do
    rm %{buildroot}/%{_mandir}/man8/${x}.8
done

# compress man pages
OLD_PWD=`pwd`
for d in %{buildroot}%{_mandir}/man*; do
    cd $d
    for f in *; do
        if [ -h $f ]; then
            mv $f $f.gz
        elif [ -f $f ];then
            gzip -9 $f
        else
            echo "Unknown thing to compress : $f"
        fi
    done
done
cd $OLD_PWD

# replace duplicates by symlinks
%fdupes -s %{buildroot}/usr

#
# main

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post kernel-source
echo To install the kernel-module, do:
echo cd /usr/src/kernel-modules/openafs
echo sh ./build-modules.sh build
echo sh ./build-modules.sh install

#
# fuse client

%pre fuse_client
%service_add_pre openafs-fuse-client.service

%preun fuse_client
%service_del_preun openafs-fuse-client.service
%{stop_on_removal}

%post fuse_client
if [ ! -d /afs ]; then
    mkdir /afs
fi
%{fillup_only -n openafs-fuse-client}
%service_add_post openafs-fuse-client.service
/sbin/ldconfig

if [ "x$1" = "x" ]; then
    my_operation=0
else
    my_operation=$1
fi

if [ $my_operation -gt 1 ]; then
    echo Not stopping the possibly running client.
    echo You must restart the client to put the upgrade into effect.
else
    echo This is the experimental FUSE implementation of the openafs-client
    echo Please configure your cell like with the in-kernel openafs-client
    echo authentication etc. is not implemented yet in this version.
fi

%postun fuse_client
%service_del_postun openafs-fuse-client.service
if [ -d /afs ]; then
     echo make sure to remove directory /afs if unwanted.
fi
/sbin/ldconfig

#
# client

%if %{build_kernel_modules}
%pre client
%service_add_pre openafs-client.service

%post client
if [ ! -d /afs ]; then
    mkdir /afs
fi
/sbin/ldconfig
%{fillup_only -n openafs-client}
%service_add_post openafs-client.service
%if %{have_firewalld}
%firewalld_reload
%endif

if [ "x$1" = "x" ]; then
    my_operation=0
else
    my_operation=$1
fi
if [ $my_operation -gt 1 ]; then
    echo Not stopping the possibly running client.
    echo You must restart the client to put the upgrade into effect.
else
    echo For configuring the client, please check /etc/sysconfig/openafs-client
    echo and/or follow the instructions found on http://www.openafs.org  how to install an openafs-client.
fi

%preun client
%{stop_on_removal}
%service_del_preun openafs-client.service

%postun client
if [ -d /afs ]; then
     echo make sure to remove directory /afs if unwanted.
fi
/sbin/ldconfig
%service_del_postun openafs-client.service
%endif

#
# server

%pre server
%service_add_pre openafs-server.service

%post server
/sbin/ldconfig
%{fillup_only -n openafs-server}
%service_add_post openafs-server.service

if [ "$FIRST_ARG" -gt 1 ]; then
    # update no new install
    echo Not stopping the possibly running services.
    echo You must restart the service to put the upgrade into effect.
    if [ -d /var/openafs ]; then
         echo To upgrade, stop the server, copy the contents of /var/openafs to /var/lib/openafs,
         echo remove the empty directory /var/openafs and then start the server again.
    fi
else
    echo For configuring the server, please check /etc/sysconfig/openafs-server
    echo and/or follow the instructions found on http://www.openafs.org to install an openafs-client.
fi

%preun server
%service_del_preun openafs-server.service
%{stop_on_removal}

%postun server
/sbin/ldconfig
%service_del_postun openafs-server.service

#
# devel

%post devel

%postun devel

#
# authlibs

%if %{build_authlibs}
%post authlibs

%postun authlibs
%endif

#
#	FILES
#

%files
%defattr(-,root,root)
%config /etc/ld.so.conf.d/openafs.conf
%config(noreplace) %{viceetcdir}/CellAlias
%config(noreplace) %{viceetcdir}/CellServDB
%config(noreplace) %{viceetcdir}/ThisCell
%dir %{viceetcdir}
%doc %{_mandir}/man5/afsmonitor.5.gz
%doc %{_mandir}/man1/afs.1.gz
%doc %{_mandir}/man1/afs_compile_et.1.gz
%doc %{_mandir}/man1/afs_scout.1.gz
%doc %{_mandir}/man1/afsmonitor.1.gz
%doc %{_mandir}/man1/cmdebug.1.gz
%doc %{_mandir}/man1/pts.1.gz
%doc %{_mandir}/man1/pts_*.gz
%doc %{_mandir}/man1/restorevol.1.gz
%doc %{_mandir}/man1/rxdebug.1.gz
%doc %{_mandir}/man1/sys.1.gz
%doc %{_mandir}/man1/translate_et.1.gz
%doc %{_mandir}/man1/udebug.1.gz
%doc %{_mandir}/man1/vos.1.gz
%doc %{_mandir}/man1/vos_*gz
%doc %{_mandir}/man1/xstat_cm_test.1.gz
%doc %{_mandir}/man1/xstat_fs_test.1.gz
%doc %{_mandir}/man5/CellAlias.5.gz
%doc %{_mandir}/man5/CellServDB.5.gz
%doc %{_mandir}/man5/NetInfo.5.gz
%doc %{_mandir}/man5/NetRestrict.5.gz
%doc %{_mandir}/man5/ThisCell.5.gz
%doc %{_mandir}/man5/afs.5.gz
%doc %{_mandir}/man5/butc.5.gz
%doc %{_mandir}/man5/butc_logs.5.gz
%doc %{_mandir}/man5/fms.log.5.gz
%doc %{_mandir}/man5/sysid.5.gz
%doc %{_mandir}/man5/uss.5.gz
%doc %{_mandir}/man5/uss_*.5.gz
%doc %{_mandir}/man8/afs_backup.8.gz
%doc %{_mandir}/man8/afs_backup_*.8.gz
%doc %{_mandir}/man8/bos.8.gz
%doc %{_mandir}/man8/bos_[a-t]*.8.gz
%doc %{_mandir}/man8/bos_uninstall.8.gz
%doc %{_mandir}/man8/butc.8.gz
%doc %{_mandir}/man8/fms.8.gz
%doc %{_mandir}/man8/read_tape.8.gz
%doc %{_mandir}/man8/uss.8.gz
%doc %{_mandir}/man8/uss_*.8.gz
%doc %{_mandir}/man8/vsys.8.gz
%doc NEWS README* RELNOTES ChangeLog
%{_bindir}/afs_compile_et
%{_bindir}/afs_scout
%{_bindir}/afsio
%{_bindir}/afsmonitor
%{_bindir}/cmdebug
%{_bindir}/pts
%{_bindir}/restorevol
%{_bindir}/sys
%{_bindir}/translate_et
%{_bindir}/xstat_cm_test
%{_bindir}/xstat_fs_test
%{_libdir}/openafs/libafshcrypto.so.*
%{_libdir}/openafs/librokenafs.so.*
%{_sbindir}/afs_backup
%{_sbindir}/bos
%{_sbindir}/butc
%{_sbindir}/fms
%{_sbindir}/read_tape
%{_sbindir}/rxdebug
%{_sbindir}/udebug
%{_sbindir}/uss
%{_sbindir}/vos
%{_sbindir}/vsys

%files fuse_client
%defattr(-,root,root)
%{_sbindir}/afsd.fuse
%{_sbindir}/rcopenafs-fuse-client
%config(noreplace) %{viceetcdir}/SuidCells
%config(noreplace) %{viceetcdir}/cacheinfo
%doc %{_mandir}/man8/afsd.fuse.8.gz
%_unitdir/openafs-fuse-client.service
%{_fillupdir}/sysconfig.openafs-fuse-client
%{vicecachedir}

%if %{build_kernel_modules}
%files client
%defattr(-,root,root)
 %{_bindir}/fs
 %{_bindir}/aklog
 %{_bindir}/klog.krb5
 %{_bindir}/pagsh
 %{_bindir}/pagsh.krb
 %{_bindir}/tokens
 %{_bindir}/tokens.krb
 %{_bindir}/unlog
 %{_bindir}/up
 %{_sbindir}/afsd
 %{_sbindir}/fstrace
%doc %{_mandir}/man1/fs.1.gz
%doc %{_mandir}/man1/fs_*.1.gz
%doc %{_mandir}/man1/aklog.1.gz
%doc %{_mandir}/man1/klog.krb5.1.gz
%doc %{_mandir}/man1/pagsh.1.gz
%doc %{_mandir}/man1/pagsh.krb.1.gz
%doc %{_mandir}/man1/tokens.1.gz
%doc %{_mandir}/man1/tokens.krb.1.gz
%doc %{_mandir}/man1/unlog.1.gz
%doc %{_mandir}/man1/up.1.gz
%doc %{_mandir}/man8/afsd.8.gz
%doc %{_mandir}/man8/fstrace.8.gz
%doc %{_mandir}/man8/fstrace_*.8.gz
%_unitdir/openafs-client.service
%doc %{_mandir}/man1/copyauth.1.gz
%doc %{_mandir}/man5/cacheinfo.5.gz
%doc %{_mandir}/man5/afs_cache.5.gz
%dir %{_datadir}/openafs
%dir %{_datadir}/openafs/C
%{_datadir}/openafs/C/afszcm.cat
%doc %{_mandir}/man5/afszcm.cat.5.gz
%config(noreplace) %{viceetcdir}/SuidCells
%config(noreplace) %{viceetcdir}/cacheinfo
%{_sbindir}/rcopenafs-client
%{_fillupdir}/sysconfig.openafs-client
%{vicecachedir}
%if %{have_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/afs3-callback.xml
%{_prefix}/lib/firewalld/services/afs3-rmtsys.xml
%endif
%endif

%files server
%defattr(-,root,root)
%attr(770,root,root) %dir %{afslocaldir}
%attr(775,root,root) %dir %{afslogsdir}
%config %{viceetcdir}/server
%doc %{_mandir}/man5/AuthLog.5.gz
%doc %{_mandir}/man5/AuthLog.dir.5.gz
%doc %{_mandir}/man5/BackupLog.5.gz
%doc %{_mandir}/man5/BosConfig.5.gz
%doc %{_mandir}/man5/BosLog.5.gz
%doc %{_mandir}/man5/FORCESALVAGE.5.gz
%doc %{_mandir}/man5/FileLog.5.gz
%doc %{_mandir}/man5/KeyFile.5.gz
%doc %{_mandir}/man5/KeyFileExt.5.gz
%doc %{_mandir}/man5/NoAuth.5.gz
%doc %{_mandir}/man5/PtLog.5.gz
%doc %{_mandir}/man5/SALVAGE.fs.5.gz
%doc %{_mandir}/man5/SalvageLog.5.gz
%doc %{_mandir}/man5/UserList.5.gz
%doc %{_mandir}/man5/VLLog.5.gz
%doc %{_mandir}/man5/VolserLog.5.gz
%doc %{_mandir}/man5/afs_volume_header.5.gz
%doc %{_mandir}/man5/bdb.DB0.5.gz
%doc %{_mandir}/man5/krb.conf.5.gz
%doc %{_mandir}/man5/krb.excl.5.gz
%doc %{_mandir}/man5/prdb.DB0.5.gz
%doc %{_mandir}/man5/salvage.lock.5.gz
%doc %{_mandir}/man5/tapeconfig.5.gz
%doc %{_mandir}/man5/vldb.DB0.5.gz
%doc %{_mandir}/man8/akeyconvert.8.gz
%doc %{_mandir}/man8/asetkey.8.gz
%doc %{_mandir}/man8/bos_util.8.gz
%doc %{_mandir}/man8/bosserver.8.gz
%doc %{_mandir}/man8/buserver.8.gz
%doc %{_mandir}/man8/dafileserver.8.gz
%doc %{_mandir}/man8/dafssync-debug.8.gz
%doc %{_mandir}/man8/dafssync-debug_*.8.gz
%doc %{_mandir}/man8/dasalvager.8.gz
%doc %{_mandir}/man8/davolserver.8.gz
%doc %{_mandir}/man8/fileserver.8.gz
%doc %{_mandir}/man8/fssync-debug.8.gz
%doc %{_mandir}/man8/fssync-debug_*.8.gz
%doc %{_mandir}/man8/prdb_check.8.gz
%doc %{_mandir}/man8/pt_util.8.gz
%doc %{_mandir}/man8/ptserver.8.gz
%doc %{_mandir}/man8/salvager.8.gz
%doc %{_mandir}/man8/salvageserver.8.gz
%doc %{_mandir}/man8/state_analyzer.8.gz
%doc %{_mandir}/man8/upclient.8.gz
%doc %{_mandir}/man8/upserver.8.gz
%doc %{_mandir}/man8/vldb_check.8.gz
%doc %{_mandir}/man8/vldb_convert.8.gz
%doc %{_mandir}/man8/vlserver.8.gz
%doc %{_mandir}/man8/voldump.8.gz
%doc %{_mandir}/man8/volinfo.8.gz
%doc %{_mandir}/man8/volscan.8.gz
%doc %{_mandir}/man8/volserver.8.gz
%dir %{_libexecdir}/openafs
%{_libexecdir}/openafs/buserver
%{_libexecdir}/openafs/dafileserver
%{_libexecdir}/openafs/dasalvager
%{_libexecdir}/openafs/davolserver
%{_libexecdir}/openafs/fileserver
%{_libexecdir}/openafs/ptserver
%{_libexecdir}/openafs/salvager
%{_libexecdir}/openafs/salvageserver
%{_libexecdir}/openafs/upclient
%{_libexecdir}/openafs/upserver
%{_libexecdir}/openafs/vlserver
%{_libexecdir}/openafs/volserver
%{_sbindir}/asetkey
%{_sbindir}/akeyconvert
%{_sbindir}/bos_util
%{_sbindir}/bosserver
%{_sbindir}/dafssync-debug
%{_sbindir}/fssync-debug
%{_sbindir}/prdb_check
%{_sbindir}/pt_util
%{_sbindir}/salvsync-debug
%{_sbindir}/state_analyzer
%{_sbindir}/vldb_check
%{_sbindir}/vldb_convert
%{_sbindir}/voldump
%{_sbindir}/volinfo
%{_sbindir}/volscan
%_unitdir/openafs-server.service
%{_sbindir}/rcopenafs-server
/%{_fillupdir}/sysconfig.openafs-server
%if %{have_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/afs3-bos.xml
%{_prefix}/lib/firewalld/services/afs3-fileserver.xml
%{_prefix}/lib/firewalld/services/afs3-prserver.xml
%{_prefix}/lib/firewalld/services/afs3-update.xml
%{_prefix}/lib/firewalld/services/afs3-vlserver.xml
%{_prefix}/lib/firewalld/services/afs3-volser.xml
%endif

%files devel
%defattr(-,root,root)
%dir %{_libdir}/openafs
%doc %{_mandir}/man1/livesys.1.gz
%doc %{_mandir}/man1/rxgen.1.gz
%doc %{_mandir}/man3/AFS::ukernel.3.gz
%{_bindir}/livesys
%{_bindir}/rxgen
%{_includedir}/openafs/
%{_libdir}/openafs/libafshcrypto.so
%{_libdir}/openafs/librokenafs.so
%{perl_vendorarch}/ukernel.so
%dir %{perl_vendorlib}/AFS
%{perl_vendorlib}/AFS/ukernel.pm

%files  kernel-source
%defattr(-,root,root)
%dir /usr/src/kernel-modules
%dir /usr/src/kernel-modules/openafs
/usr/src/kernel-modules/openafs/*

%if %{build_authlibs}
%files authlibs
%defattr(-,root,root)
%{_libdir}/openafs/libafsauthent.so.*
%{_libdir}/openafs/libafsrpc.so.*
%{_libdir}/openafs/libkopenafs.so.*

%files authlibs-devel
%defattr(-,root,root)
%{_libdir}/openafs/libafsauthent.so
%{_libdir}/openafs/libafsrpc.so
%{_libdir}/openafs/libkopenafs.so
%endif

#
#	CHANGELOG
#

%changelog
