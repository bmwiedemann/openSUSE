#
# spec file for package rdiff-backup
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rdiff-backup
Version:        1.2.8
Release:        0
Summary:        Convenient and transparent local/remote incremental mirror/backup
License:        GPL-2.0+
Group:          Productivity/Archiving/Backup
Url:            http://www.nongnu.org/rdiff-backup/
Source0:        http://savannah.nongnu.org/download/rdiff-backup/%{name}-%{version}.tar.gz
Source1:        http://savannah.nongnu.org/download/rdiff-backup/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch0:         rdiff-backup-fix-deprecations.diff
# well, upstream is apparently dead, but I found this patch on the upstream mailing list.
# PATCH-FEATURE-UPSTREAM rdiff-backup-1.2.8-sparsefiles.diff -- seife+obs@b1-systems.com
Patch1:         rdiff-backup-1.2.8-sparsefiles.diff
# in order not stumble on handle hardlinks, these two patches are necessary
# http://savannah.nongnu.org/bugs/?26848
# PATCH-FEATURE-UPSTREAM Hardlink.py.revised-patch compare.py.patch -- hpj@urpla.net
Patch2:         Hardlink.py.revised-patch
Patch3:         compare.py.patch
# don't take empty sessions into account, which has the potential of removing valid
# backups with --remove-older-than xB, while keeping empty/useless sessions instead
# patch is not upstream -- hpj@urpla.net
Patch4:         rdiff-backup-dont-pick-empty-sessions.diff
# the above patch is slightly broken, fix it by not using sparse code when writing
# compressed files
# PATCH-FIX-OPENSUSE rdiff-backup-1.2.8-sparse-no-seek-in-gzip.diff --seife+obs@b1-systems.com
Patch11:        rdiff-backup-1.2.8-sparse-no-seek-in-gzip.diff
# PATCH-FIX-UPSTREAM rdiff-backup-librsync-1.0.patch dimstar@opensuse.org -- Fix build with librsync 1.0.0
Patch12:        rdiff-backup-librsync-1.0.patch
BuildRequires:  python-devel
Recommends:     python-pylibacl
Recommends:     python-xattr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%if 0%{?suse_version} > 1210
BuildRequires:  librsync-devel
%else
BuildRequires:  librsync
%endif

%description
rdiff-backup backs up one directory to another, possibly over a
network. The target directory ends up a copy of the source directory,
but extra reverse diffs are stored in a special subdirectory of that
target directory, so you can still recover files lost some time ago.
The idea is to combine the best features of a mirror and an incremental
backup. rdiff-backup also preserves subdirectories, hard links, dev
files, permissions, uid/gid ownership, and modification times. Also,
rdiff-backup can operate in a bandwidth efficient manner over a pipe,
like rsync. Thus you can use rdiff-backup and ssh to securely back a
hard drive up to a remote location, and only the differences will be
transmitted. Finally, rdiff-backup is easy to use and settings have
sensical defaults.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch11 -p1
%patch2
%patch3
%patch4 -p1
%patch12 -p1

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root %{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/rdiff-backup-%{version}

%files
%defattr(-, root, root)
%doc CHANGELOG COPYING FAQ.html examples.html README
%{_mandir}/*/*
%{_bindir}/*
%{py_sitedir}/rdiff_backup
%{py_sitedir}/*.egg-info

%changelog
