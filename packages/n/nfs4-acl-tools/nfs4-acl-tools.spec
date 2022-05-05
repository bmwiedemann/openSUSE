#
# spec file for package nfs4-acl-tools
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


Name:           nfs4-acl-tools
Version:        0.3.7
Release:        0
Summary:        Command line tools for managing ACLs over NFSv4
License:        BSD-3-Clause
Group:          System/Filesystems
URL:            http://linux-nfs.org/~bfields/nfs4-acl-tools/
Source0:        http://linux-nfs.org/~bfields/nfs4-acl-tools/nfs4-acl-tools-%{version}.tar.gz
# GitClone:     http://git.linux-nfs.org/?p=bfields/nfs4-acl-tools.git
Patch2:         nfs-acl-tools-xattr.patch
BuildRequires:  libtool

%description
Command line tools for viewing and setting ACLs (Access Control Lists)
when using NFSv4 to access a remote filesystem. The remote filesystem
must also support ACLs.

%prep
%setup -q
%patch2 -p1

%build
autoreconf -fi
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie"
%configure
%make_build

%install
# Don't try to chown/chgrp as we build as non-root
export CHOWNPROG=: CHGRPPROG=:
%make_install

%files
%license COPYING
%doc README TODO VERSION
%{_bindir}/nfs4_editfacl
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
