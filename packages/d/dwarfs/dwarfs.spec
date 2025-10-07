#
# spec file for package dwarfs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define sover %(echo %{version} | sed 's/\\./_/g;')
%define __builder ninja
Name:           dwarfs
Version:        0.13.0
Release:        0
Summary:        Deduplicating compressed read-only file system
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/mhx/dwarfs
Source0:        https://github.com/mhx/dwarfs/releases/download/v%{version}/dwarfs-%{version}.tar.xz
# PATCH-FIX-UPSTREAM folly-remove-boost_system-dependency.patch gh#mhx/dwarfs#288 gh#facebook/folly#2489
Patch0:         folly-remove-boost_system-dependency.patch
# PATCH-FIX-UPSTREAM remove_hhdate_dependency.patch https://github.com/mhx/dwarfs/pull/289 TODO: Remove this patch once a new upstream version containing the PR has been released
Patch1:         https://github.com/mhx/dwarfs/pull/289.patch#/remove_hhdate_dependency.patch
BuildRequires:  bison
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_process-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  ninja
BuildRequires:  parallel-hashmap-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(double-conversion)
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(utf8cpp)
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libdwarf)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libglog)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nlohmann_json)
# SECTION test requirements
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gmock)
# /SECTION

%description
The Deduplicating Warp-speed Advanced Read-only File System.

DwarFS is a deduplicating compressed read-only file system
particularly suited for very redundant data.
Compared to SquashFS, it is typically more efficient.

%package -n libdwarfs%{sover}
Summary:        DwarFS dynamic library

%description -n libdwarfs%{sover}
The Deduplicating Warp-speed Advanced Read-only File System.

DwarFS is a deduplicating compressed read-only file system
particularly suited for very redundant data.
Compared to SquashFS, it is typically more efficient.

This package contains the dynamic library for DwarFS.

%package devel
Summary:        DwarFS development files
Requires:       libdwarfs%{sover} = %{version}

%description devel
The Deduplicating Warp-speed Advanced Read-only File System.

DwarFS is a deduplicating compressed read-only file system
particularly suited for very redundant data.
Compared to SquashFS, it is typically more efficient.

This package contains the development files for DwarFS.

%ldconfig_scriptlets -n libdwarfs%{sover}

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_EXE_LINKER_FLAGS="-lboost_filesystem -lboost_process" \
    -DWITH_TESTS=ON -DPREFER_SYSTEM_GTEST=ON
%cmake_build

%install
%cmake_install

# only mount helper should be in sbin
mv %{buildroot}%{_sbindir}/dwarfs %{buildroot}%{_bindir}/dwarfs
ln -sf %{_bindir}/dwarfs %{buildroot}%{_sbindir}/mount.dwarfs

%check
%ctest

%files
%license LICENSE
%doc README.md

%{_mandir}/*/*dwarfs*
%{_bindir}/*dwarfs*
%{_sbindir}/mount.dwarfs

%files -n libdwarfs%{sover}
%{_libdir}/*.so.*

%files devel
%{_includedir}/dwarfs
%{_libdir}/cmake/dwarfs
%{_libdir}/libdwarfs*.so

%changelog
