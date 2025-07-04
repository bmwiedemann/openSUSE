#
# spec file for package apfsprogs
#
# Copyright (c) 2025 SUSE LLC
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


Name:           apfsprogs
Version:        0.2.1
Release:        0
Summary:        Experimental APFS tools for Linux
License:        GPL-2.0-only
URL:            https://github.com/linux-apfs/apfsprogs
Source0:        %{url}/archive/v%{version}.tar.gz#/apfsprogs-%{version}.tar.gz

%description
apfsprogs is a suite of userland software to work with the Apple File System
on Linux. It's intended mainly to help test the Linux kernel module that can
be retrieved from <git://github.com/eafer/linux-apfs-rw.git>. The following
are included:

  o mkapfs: an experimental filesystem build tool
  o apfs-snap: a tool to take snapshots of a volume mounted with our module
  o apfsck: a filesystem integrity checker, for now only useful for testers

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags} -C lib
make %{?_smp_mflags} -C apfs-label
make %{?_smp_mflags} -C apfs-snap
make %{?_smp_mflags} -C apfsck
make %{?_smp_mflags} -C mkapfs

%install
%make_install -C apfs-label BINDIR=%{_sbindir} MANDIR=%{_mandir}
%make_install -C apfs-snap BINDIR=%{_sbindir} MANDIR=%{_mandir}
%make_install -C apfsck BINDIR=%{_sbindir} MANDIR=%{_mandir}
%make_install -C mkapfs BINDIR=%{_sbindir} MANDIR=%{_mandir}

%files
%license LICENSE
%doc README
%{_mandir}/apfs-label.8
%{_mandir}/apfs-snap.8
%{_mandir}/apfsck.8
%{_mandir}/fsck.apfs.8
%{_mandir}/mkapfs.8
%{_mandir}/mkfs.apfs.8
%{_sbindir}/apfs-label
%{_sbindir}/apfs-snap
%{_sbindir}/apfsck
%{_sbindir}/fsck.apfs
%{_sbindir}/mkapfs
%{_sbindir}/mkfs.apfs

%changelog
