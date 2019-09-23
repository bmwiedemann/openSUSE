#
# spec file for package xfsdump
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


Name:           xfsdump
Version:        3.1.8
Release:        0
Summary:        Administrative Utilities for the XFS File System
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            http://xfs.org
Source0:        https://www.kernel.org/pub/linux/utils/fs/xfs/xfsdump/xfsdump-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/linux/utils/fs/xfs/xfsdump/xfsdump-%{version}.tar.sign
Source2:        %{name}.keyring
Patch0:         xfsdump-docdir.diff
Patch1:         xfsdump-rename-READ-WRITE-macros-in-rmtlib.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  xfsprogs-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xfsdump package contains xfsdump, xfsrestore, and a number of other
utilities for administering XFS file systems.

xfsdump examines files in a file system, determines which files need to
be backed up, and copies those files to a specified disk, tape, or
other storage medium.  It uses XFS-specific directives for optimizing
the dump of an XFS file system and also knows how to backup XFS
extended attributes.  Backups created with xfsdump are "endian safe"
and can thus be transferred between Linux machines of different
architectures and also between IRIX machines.

xfsrestore performs the inverse function of xfsdump.  It can restore a
full backup of a file system.  Subsequent incremental backups can then
be layered on top of the full backup.  Single files and directory
subtrees may be restored from full or partial backups.

%prep
%setup -q
%patch0
%patch1 -p1

%build
rm -f configure
make configure
export DEBUG=-DNDEBUG
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}

%install
export DIST_ROOT=%{buildroot}
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang xfsdump
# Remove the link created by the make file
rm %{buildroot}/%{_sbindir}/{xfsdump,xfsrestore}
mv %{buildroot}/sbin/{xfsdump,xfsrestore} %{buildroot}/%{_sbindir}
#UsrMerge
ln -s %{_sbindir}/xfsdump %{buildroot}/sbin
ln -s %{_sbindir}/xfsrestore %{buildroot}/sbin
#EndUsrMerge

%files -f xfsdump.lang
%defattr(-,root,root,755)
%{_sbindir}/*
#UsrMerge
/sbin/*
#EndUsrMerge
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man8/*
%if 0%{?suse_version} > 1200
%doc doc/COPYING
%endif

%changelog
