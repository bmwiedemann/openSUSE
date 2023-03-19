#
# spec file for package librsync
#
# Copyright (c) 2023 SUSE LLC
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


%define lname   librsync2
Name:           librsync
Version:        2.3.4
Release:        0
Summary:        A Library for Generating Network Deltas
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/librsync/librsync
Source:         https://github.com/librsync/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(zlib)

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package -n %{lname}
Summary:        A Library for Generating Network Deltas
# O/P added 2011-11-26
Group:          System/Libraries
Obsoletes:      librsync < %{version}-%{release}
Provides:       librsync = %{version}-%{release}

%description -n %{lname}
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package devel
Summary:        Development files for librsync
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package -n rdiff
Summary:        Frontend to rsync's delta algorithm
Group:          Productivity/Archiving/Backup

%description -n rdiff
rdiff computes and applies signature-based file differences.

%prep
%setup -q

%build
%cmake \
  -DENABLE_COMPRESSION=ON
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/librsync.so.*
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS TODO.md

%files devel
%{_libdir}/librsync.so
%{_mandir}/man3/*
%{_includedir}/*.h

%files -n rdiff
%{_bindir}/rdiff
%{_mandir}/man1/*

%changelog
