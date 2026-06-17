#
# spec file for package libdispatch
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


%define reltag 6.3.2-RELEASE
Name:           libdispatch
Version:        6.3.2
Release:        0
Summary:        Apple's Grand Central Dispatch library
License:        Apache-2.0
URL:            https://github.com/swiftlang/swift-corelibs-libdispatch
Source0:        https://github.com/swiftlang/swift-corelibs-libdispatch/archive/swift-%{reltag}.tar.gz#/corelibs-libdispatch.tar.gz
Source1:        libdispatch-rpmlintrc
# PATCH-FIX-OPENSUSE set library versions
Patch0:         soversion.patch
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbsd)

%description
Grand Central Dispatch (GCD or libdispatch) provides support for
concurrent code execution on multicore hardware.

%package -n libdispatch1_3
Summary:        Apple's Grand Central Dispatch library
Obsoletes:      libdispatch < %{version}-%{release}
Provides:       libdispatch = %{version}-%{release}

%description -n libdispatch1_3
Grand Central Dispatch (GCD or libdispatch) provides support for
concurrent code execution on multicore hardware.

%package        devel
Summary:        Development files for %{name}
Requires:       libdispatch1_3 = %{version}-%{release}
# Wrong location for manpages in older version
Conflicts:      libdispatch < %{version}-%{release}
BuildArch:      noarch

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n swift-corelibs-libdispatch-swift-%{reltag}

%build
export CC=clang
export CXX=clang++
# clang doesn't have 'auto'
# aarch64 specific flag
%ifarch aarch64 riscv64
export CFLAGS="%{optflags} -Wno-unused-command-line-argument"
%else
export CFLAGS="%{optflags}"
%endif
CFLAGS=${CFLAGS/-flto=auto/-flto}

%ifarch aarch64 riscv64
export CXXFLAGS="%{optflags} -Wno-unused-command-line-argument"
%else
export CXXFLAGS="%{optflags}"
%endif
CXXFLAGS=${CXXFLAGS/-flto=auto/-flto}
export LDFLAGS="-flto -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now"

%define __builder ninja
%cmake \
    -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" \
    -DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS" \
    -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
    -DINSTALL_BLOCK_HEADERS_DIR:PATH=include/block .
%cmake_build

%install
%cmake_install
chrpath --delete %{buildroot}%{_libdir}/libdispatch.so.1.3

%ldconfig_scriptlets -n libdispatch1_3

%files -n libdispatch1_3
%license LICENSE
%{_libdir}/*.so*

%files devel
%dir %{_includedir}/block
%{_includedir}/block/*
%dir %{_includedir}/dispatch
%{_includedir}/dispatch/*
%dir %{_includedir}/os
%{_includedir}/os/*
%{_mandir}/man3/*

%changelog
