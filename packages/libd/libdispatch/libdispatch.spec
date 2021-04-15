#
# spec file for package libdispatch
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


%define reltag 5.3.3-RELEASE
Name:           libdispatch
Version:        5.3.3
Release:        0
Summary:        Apple's Grand Central Dispatch library
License:        Apache-2.0
Group:          Development/Languages/C and C++
URL:            https://github.com/apple/swift-corelibs-libdispatch
Source0:        https://github.com/apple/swift-corelibs-libdispatch/archive/swift-%{reltag}.tar.gz#/corelibs-libdispatch.tar.gz
Source1:        libdispatch-rpmlintrc
# Fedora patch
Patch0:         asprintf.patch
# set library versions
Patch1:         soversion.patch
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  libbsd-devel
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-gold
BuildRequires:  ninja

%description
Grand Central Dispatch (GCD or libdispatch) provides
comprehensive support for concurrent code execution on
multicore hardware.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n swift-corelibs-libdispatch-swift-%{reltag}
%patch0 -p2
%patch1 -p1
%build
export CC=clang
export CXX=clang++
# clang doesn't have 'auto'
# aarch64 specific flag
%ifarch aarch64
export CFLAGS="%{optflags} -Wno-unused-command-line-argument"
%else
export CFLAGS="%{optflags}"
%endif
CFLAGS=${CFLAGS/-flto=auto/-flto}

%ifarch aarch64
export CXXFLAGS="%{optflags} -Wno-unused-command-line-argument"
%else
export CXXFLAGS="%{optflags}"
%endif
CXXFLAGS=${CXXFLAGS/-flto=auto/-flto}
export LDFLAGS="-flto -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now"

%define __builder ninja
%cmake \
    -DCMAKE_Fortran_FLAGS="$CXXFLAGS" \
    -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" \
    -DCMAKE_MODULE_LINKER_FLAGS="-flto -Wl, --as-needed" \
    -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
    -DINSTALL_BLOCK_HEADERS_DIR:PATH=include/block .
ninja

%install
%cmake_install
chrpath --delete %{buildroot}%{_libdir}/libdispatch.so.1.3

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/*.so*
%{_mandir}/man3/*

%files devel
%dir %{_includedir}/block
%{_includedir}/block/*
%dir %{_includedir}/dispatch
%{_includedir}/dispatch/*
%dir %{_includedir}/os
%{_includedir}/os/*

%changelog
