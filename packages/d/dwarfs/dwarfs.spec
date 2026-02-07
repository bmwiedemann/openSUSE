#
# spec file for package dwarfs
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


%define sover %(echo %{version} | sed 's/\\./_/g;')
%define __builder ninja
Name:           dwarfs
Version:        0.14.1
Release:        0
Summary:        Deduplicating compressed read-only file system
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/mhx/dwarfs
Source0:        https://github.com/mhx/dwarfs/releases/download/v%{version}/dwarfs-%{version}.tar.xz
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
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
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

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

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

%check
%ctest

%files
%license LICENSE
%doc README.md

%{_mandir}/*/*dwarfs*
%{_bindir}/*dwarfs*
%{_sbindir}/mount.dwarfs
%{_datadir}/mime/packages/dwarfs.xml
%{_datadir}/applications/dwarfs-mount-handler.desktop

%files -n libdwarfs%{sover}
%{_libdir}/*.so.*

%files devel
%{_includedir}/dwarfs
%{_libdir}/cmake/dwarfs
%{_libdir}/libdwarfs*.so

%files zsh-completion
%{_datadir}/zsh/site-functions/*

%files bash-completion
%{_datadir}/bash-completion/completions/*

%changelog
