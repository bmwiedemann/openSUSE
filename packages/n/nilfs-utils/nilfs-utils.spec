#
# spec file for package nilfs-utils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define libnilfs    libnilfs3
%define libcleaner  libnilfscleaner0
%define libgc       libnilfsgc3
%if 0%{?suse_version} < 1550
%define root_sbindir	/sbin
%else
%define root_sbindir	%{_sbindir}
%endif
Name:           nilfs-utils
Version:        2.3.1
Release:        0
Summary:        Utilities for NILFS
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://nilfs.sourceforge.io/
Source:         https://nilfs.sourceforge.io/download/nilfs-utils-%{version}.tar.bz2
BuildRequires:  chrpath
BuildRequires:  libmount-devel
BuildRequires:  libuuid-devel

%description
This package contains utility programs for NILFS v2.

%package -n %{libnilfs}
Summary:        Library for interacting with nilfs
Group:          System/Libraries

%description -n %{libnilfs}
This package contains shared library needed for some applications to
interface with nilfs

%package -n %{libcleaner}
Summary:        Cleaner library for interacting with nilfs
Group:          System/Libraries

%description -n %{libcleaner}
This package contains shared cleaner library needed for some applications
to interface with nilfs

%package -n %{libgc}
Summary:        Garbage collection library for interacting with nilfs
Group:          System/Libraries

%description -n %{libgc}
This package contains shared garbage collection library needed for some
applications to interface with nilfs

%package devel
Summary:        Development package for the libnilfs library
Group:          Development/Libraries/C and C++
Requires:       %{libnilfs} = %{version}

%description devel
This package contains the development files for NILFS v2.

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-libmount
%make_build

%install
make install DESTDIR=%{buildroot} root_sbindir=%{root_sbindir}
# remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print
chrpath -d %{buildroot}%{root_sbindir}/*

%ldconfig_scriptlets -n %{libnilfs}
%ldconfig_scriptlets -n %{libcleaner}
%ldconfig_scriptlets -n %{libgc}

%files
%license COPYING
%doc README
%config(noreplace) %{_sysconfdir}/nilfs_cleanerd.conf
%if 0%{?suse_version} < 1550
%{root_sbindir}/*
%endif
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/lscp.1.gz
%{_mandir}/man1/lssu.1.gz
%{_mandir}/man5/nilfs*.5.gz
%{_mandir}/man8/chcp.8.gz
%{_mandir}/man8/dumpseg.8.gz
%{_mandir}/man8/mkcp.8.gz
%{_mandir}/man8/mkfs.nilfs2.8.gz
%{_mandir}/man8/mount.nilfs2.8.gz
%{_mandir}/man8/nilfs.8.gz
%{_mandir}/man8/nilfs*.8.gz
%{_mandir}/man8/rmcp.8.gz
%{_mandir}/man8/umount.nilfs2.8.gz

%files -n %{libnilfs}
%{_libdir}/libnilfs.so.3*

%files -n %{libgc}
%{_libdir}/libnilfsgc.so.3*

%files devel
%{_includedir}/nilfs.h
%{_includedir}/nilfs_gc.h
%{_libdir}/libnilfs.so
%{_libdir}/libnilfsgc.so
%{_libdir}/pkgconfig/nil*.pc

%changelog
