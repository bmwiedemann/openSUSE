#
# spec file for package rocksdb
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lib_name librocksdb9
%bcond_with jemalloc
Name:           rocksdb
Version:        9.3.1
Release:        0
Summary:        Library for embeddable, persistent and fast key-value store
License:        (Apache-2.0 OR GPL-2.0-only) AND BSD-2-Clause
URL:            https://rocksdb.org/
Source:         https://github.com/facebook/rocksdb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         rocksdb-8.0.0-reproducible.patch
Patch1:         rocksdb-8.0.0-shared-liburing.patch
Patch2:         rocksdb-8.0.0-rpath.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(Snappy)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
%if %{with jemalloc}
BuildRequires:  pkgconfig(jemalloc)
%endif
# see SR#1075555 for gflags linking failure
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(gflags)
%else
BuildRequires:  gflags-devel-static
%endif

%description
RocksDB is a high performance embedded database for key-value data.
It is a fork of LevelDB which was then optimized to exploit many
central processing unit (CPU) cores, and make efficient use of fast
storage, such as solid-state drives (SSD), for input/output (I/O)
bound workloads. It is based on a log-structured merge-tree (LSM tree)
data structure.

%package -n %{lib_name}
Summary:        Shared library from rocksdb

%description -n %{lib_name}
RocksDB is a high performance embedded database for key-value data.
It is a fork of LevelDB which was then optimized to exploit many
central processing unit (CPU) cores, and make efficient use of fast
storage, such as solid-state drives (SSD), for input/output (I/O)
bound workloads. It is based on a log-structured merge-tree (LSM tree)
data structure.

This package holds the shared library of rocksdb.

%package tools
Summary:        Utility tools for RocksDB
# MariaDB ships /usr/bin/sst_dump - MDEV-14918
Conflicts:      mariadb

%description tools
RocksDB is a high performance embedded database for key-value data.
This package contains utility tools for RocksDB.

%package devel
Summary:        Development package for RocksDB
Requires:       %{lib_name} = %{version}

%description devel
RocksDB is a high performance embedded database for key-value data.
It is a fork of LevelDB which was then optimized to exploit many
central processing unit (CPU) cores, and make efficient use of fast
storage, such as solid-state drives (SSD), for input/output (I/O)
bound workloads. It is based on a log-structured merge-tree (LSM tree)
data structure.

This package contains the files needed to compile programs that use
the RocksDB library.

%prep
%autosetup -p1

%build
# building tests is disabled, because they require additional instrumentation,
# which is build in library in debug mode and adds some overhead.
# Warnings: https://github.com/facebook/rocksdb/issues/11043
%cmake \
    -DPORTABLE=1 \
    -DFAIL_ON_WARNINGS=OFF \
%if !%{with jemalloc}
    -DWITH_JEMALLOC=0 \
%endif
    -DWITH_SNAPPY=ON \
    -DWITH_LZ4=ON \
    -DWITH_ZLIB=ON \
    -DWITH_ZSTD=ON \
    -DWITH_BZ2=ON \
    -DWITH_TESTS=OFF \
    -DWITH_TOOLS=OFF \
    -DWITH_BENCHMARK_TOOLS=OFF \
    %{nil}

%cmake_build

%install
%cmake_install
find %{buildroot}%{_libdir} -type f -name "*.a" -print -delete
install -dD -m 755 %{buildroot}/%{_bindir}
install -m 755 build/tools/ldb %{buildroot}/%{_bindir}/ldb
install -m 755 build/tools/sst_dump %{buildroot}/%{_bindir}/sst_dump

%ldconfig_scriptlets -n %{lib_name}

%files -n %{lib_name}
%license COPYING LICENSE.Apache LICENSE.leveldb
%{_libdir}/librocksdb.so.*

%files tools
%license COPYING LICENSE.Apache LICENSE.leveldb
%{_bindir}/ldb
%{_bindir}/sst_dump

%files devel
%license COPYING LICENSE.Apache LICENSE.leveldb
%doc README.md HISTORY.md LANGUAGE-BINDINGS.md
%{_includedir}/rocksdb
%{_libdir}/librocksdb.so
%{_libdir}/pkgconfig/rocksdb.pc
%{_libdir}/cmake/rocksdb

%changelog
