#
# spec file for package nilfs-utils
#
# Copyright (c) 2021 SUSE LLC
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


%define libnilfs    libnilfs0
%define libcleaner  libnilfscleaner0
%define libgc       libnilfsgc0
Name:           nilfs-utils
Version:        2.2.8
Release:        0
Summary:        Utilities for NILFS
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://nilfs.sourceforge.io/en/
Source:         https://nilfs.sourceforge.io/download/%{name}-%{version}.tar.bz2
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
%setup -q

%build
%configure \
  --disable-static \
  --enable-libmount
%make_build

%install
make install DESTDIR=%{buildroot} root_sbindir=/sbin root_libdir=/%{_lib}
# remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print
chrpath -d %{buildroot}/sbin/*

%post -n %{libnilfs}      -p /sbin/ldconfig
%post -n %{libcleaner}    -p /sbin/ldconfig
%post -n %{libgc}         -p /sbin/ldconfig
%postun -n %{libnilfs}    -p /sbin/ldconfig
%postun -n %{libcleaner}  -p /sbin/ldconfig
%postun -n %{libgc}       -p /sbin/ldconfig

%files
%config(noreplace) %{_sysconfdir}/nilfs_cleanerd.conf
/sbin/*
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libnilfs}
%{_libdir}/libnilfs.so.*

%files -n %{libcleaner}
%{_libdir}/libnilfscleaner.so.*

%files -n %{libgc}
%{_libdir}/libnilfsgc.so.*

%files devel
%{_includedir}/nilfs.h
%{_includedir}/nilfs2_fs.h
%{_includedir}/nilfs_cleaner.h
%{_libdir}/libnilfs.so
%{_libdir}/libnilfscleaner.so
%{_libdir}/libnilfsgc.so

%changelog
