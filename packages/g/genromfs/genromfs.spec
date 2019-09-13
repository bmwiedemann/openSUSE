#
# spec file for package genromfs
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


Name:           genromfs
Version:        0.5.2
Release:        0
Summary:        Utility for Creating romfs File Systems
License:        GPL-2.0+
Group:          System/Boot
Url:            http://romfs.sourceforge.net
Source:         http://downloads.sf.net/romfs/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Genromfs is a tool for creating romfs file systems, which are
lightweight, read-only file systems supported by the Linux kernel.
Romfs file systems were traditionally used for the initial RAM disks
used during installation.

%prep
%setup -q

%build
make %{?_smp_mflags} CC="gcc" CFLAGS="%{optflags} -DVERSION=\\\"%{version}\\\"" LDFLAGS=

%install
make PREFIX=%{buildroot} mandir=%{_mandir} install

%files
%defattr(-,root,root)
%doc COPYING NEWS ChangeLog genromfs.lsm romfs.txt
%doc %{_mandir}/man8/genromfs.8.gz
%{_bindir}/genromfs

%changelog
