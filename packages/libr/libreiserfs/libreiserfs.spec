#
# spec file for package libreiserfs
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


Name:           libreiserfs
%define lname	libreiserfs-0_3-0
Url:            http://reiserfs.linux.kiev.ua
Version:        0.3.0.5
Release:        0
Summary:        ReiserFS File System Access Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Source:         http://ftp.roedu.net/pub/mirrors/ftp.namesys.com/pub/libreiserfs/progsreiserfs-%{version}.tar.bz2
Source1:        series
Source2:        baselibs.conf
Patch1:         reiserfs-strict-aliasing.diff
Patch2:         reiserfs-fix-warn.diff
Patch3:         reiserfs-dal-64bit.diff
Patch4:         libreiserfs-autoconf-fixups
Patch5:         libreiserfs-devel-fix
# PATCH-FIX-UPSTREAM libreiserfs-0.3.0.5-gettext.patch -- Support gettext 0.20
Patch6:         libreiserfs-0.3.0.5-gettext.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %install_info_prereq
BuildRequires:  libtool

%description
This is a library for reiserfs file system access and manipulation. The
primary goal is to develop the nice, full functionality library that
can be linked to any projects that needed reiserfs file system access.
These include GNU Parted, GNU GRUB, Yaboot, Partimage, and EVMS.

libreiserfs has a number of high level APIs for accessing reiserfs
file systems. There are main file system code, journal code, bitmap
code, directories and files access code, and device abstraction
layer.

progsreiserfs supports versions reiserfs versions 3.5 and 3.6 with
standard and relocated journal. It also supports all possible block
sizes supported by the kernel (2.4.18 with patches or 2.4.19).

Authors:
--------
    Yury Umanets <torque@ukrpost.net>
    Andrew Clausen <clausen@gnu.org>

%package -n %lname
Summary:        ReiserFS File System Access Library
# added on 2012-05-24
Group:          System/Libraries
Obsoletes:      libreiserfs < %version-%release
Provides:       libreiserfs = %version-%release

%description -n %lname
This is a library for reiserfs file system access and manipulation. The
primary goal is to develop the nice, full functionality library that
can be linked to any projects that needed reiserfs file system access.
These include GNU Parted, GNU GRUB, Yaboot, Partimage, and EVMS.

libreiserfs has a number of high level APIs for accessing reiserfs
file systems. There are main file system code, journal code, bitmap
code, directories and files access code, and device abstraction
layer.

%package progs
Summary:        ReiserFS Filesystem Access Tools
Group:          System/Filesystems
Conflicts:      reiserfs

%description progs
progsreiserfs supports reiserfs versions 3.5, 3.6 with standard and
relocated journal. Also all possible blocksizes which supported by
kernel (2.4.18 with patches or 2.4.19)

This package contains four programs that are simple frontends to
libreiserfs. There are: mkfs.reiserfs, resizefs.reiserfs,
cpfs.reiserfs, tunefs.reiserfs

Authors:
--------
    Yury Umanets <torque@ukrpost.net>
    Andrew Clausen <clausen@gnu.org>

%package devel
Summary:        ReiserFS Filesystem Access Tools
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel

%description devel
This is a library for reiserfs filesystem access and manipulation. The
primary goal is to develop the nice, full functionality library wich
might be linked against any projects which needed reiserfs filesystem
access. There are GNU Parted, GNU GRUB, Yaboot, Partimage, EVMS, etc.

Authors:
--------
    Yury Umanets <torque@ukrpost.net>
    Andrew Clausen <clausen@gnu.org>

%prep
%setup -n progsreiserfs-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
cp /usr/share/gettext/config.rpath .
mkdir -p m4
autoreconf -fi
%configure --disable-static --enable-shared
make %{?_smp_mflags}

%check
#make check

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libdal-0.3.so.0*
%_libdir/libreiserfs-0.3.so.0*

%files devel
%defattr(-,root,root)
%_includedir/dal
%_includedir/reiserfs
%{_libdir}/libdal.so
%{_libdir}/libreiserfs.so
%_datadir/aclocal/progsreiserfs.m4

%files progs
%defattr(-,root,root)
%_sbindir/*.reiserfs
%_mandir/man8/*.reiserfs.8*
%_mandir/man8/reiserfs.8*

%changelog
