#
# spec file for package xfsdump
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


Name:           xfsdump
Version:        3.1.12
Release:        0
Summary:        Administrative Utilities for the XFS File System
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://xfs.wiki.kernel.org/
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
mv %{buildroot}/sbin/{xfsdump,xfsrestore} %{buildroot}/%{_sbindir}
%if 0%{?suse_version} < 1550
ln -s %{_sbindir}/xfsdump %{buildroot}/sbin
ln -s %{_sbindir}/xfsrestore %{buildroot}/sbin
%endif

%files -f xfsdump.lang
%defattr(-,root,root,755)
%{_sbindir}/*
%if 0%{?suse_version} < 1550
/sbin/*
%endif
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man8/*
%if 0%{?suse_version} > 1200
%doc doc/COPYING
%endif

%changelog
