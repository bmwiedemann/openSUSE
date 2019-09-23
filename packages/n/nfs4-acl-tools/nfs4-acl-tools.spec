#
# spec file for package nfs4-acl-tools
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           nfs4-acl-tools
Version:        0.3.3
Release:        0
Summary:        Command line tools for managing ACLs over NFSv4
License:        BSD-3-Clause
Group:          System/Filesystems
Url:            http://www.citi.umich.edu/projects/nfsv4/linux/

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}-git4cb4187e83.tar.bz2
# PATCH-FIX-UPSTREAM allow-spaces-in-principal-names.patch bnc#772896 nfbrown@suse.com
Patch1:         allow-spaces-in-principal-names.patch
Patch2:         nfs-acl-tools-xattr.patch
BuildRequires:  libtool

%description
Command line tools for viewing and setting ACLs (Access Control Lists)
when using NFSv4 to access a remote filesystem. The remote filesystem
must also support ACLs.

%prep
%setup -q -n %{name}-%{version}-git4cb4187e83
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie"
sed -e 's,--acdir=,-I ,' -i Makefile
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc COPYING README TODO VERSION
%{_bindir}/nfs4_editfacl
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
