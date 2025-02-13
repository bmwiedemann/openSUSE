#
# spec file for package grpc
#
# Copyright (c) 2024 SUSE LLC
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


%define lver 45
%define lverp 1_70
%define src_install_dir /usr/src/%name
Name:           grpc
Version:        1.70.1
Release:        0
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://grpc.io/
Source:         https://github.com/grpc/grpc/archive/v%version.tar.gz
Source2:        %name-rpmlintrc
Patch1:         terminate.patch
Patch2:         link-failure.patch
Patch3:         return-values.patch
Patch4:         telemetry.patch
Patch14:        ARM-Unaligned-access-fixes.patch
Patch15:        Fix-compilation-on-RHEL-7-ppc64le-gcc-4.8.patch
BuildRequires:  abseil-cpp-devel >= 20240722
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?suse_version} < 1550
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  opencensus-proto-source
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcares) >= 1.19.1
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(protobuf) >= 22
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)

%description
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n libgrpc%lver
Summary:        HTTP/2-based Remote Procedure Call implementation
Group:          System/Libraries

%description -n libgrpc%lver
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n libgrpc%lverp
Summary:        HTTP/2-based Remote Procedure Call implementation
Group:          System/Libraries

%description -n libgrpc%lverp
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n libgrpc++%lverp
Summary:        HTTP/2-based Remote Procedure Call implementation
Group:          System/Libraries

%description -n libgrpc++%lverp
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n libupb%lver
Summary:        A small protobuf implementation in C
Group:          System/Libraries

%description -n libupb%lver
μpb (often written "upb") is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

%package devel
Summary:        Development files for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Tools/Building
Requires:       libgrpc%lver = %version
Requires:       libgrpc%lverp = %version
Requires:       libgrpc++%lverp = %version
Requires:       libupb%lver = %version
Requires:       pkgconfig(libcares)
Requires:       pkgconfig(re2)

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the gRPC reference implementation.

%package -n upb-devel
Summary:        Developmnt files for upb
Group:          Development/Tools/Building
Requires:       libupb%lver = %version

%description -n upb-devel
μpb (often written "upb") is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

This package provides development files for upb.

%package source
Summary:        Source code of gRPC
Group:          Development/Sources
BuildArch:      noarch

%description -n grpc-source
This subpackage contains source code of the gRPC reference implementation.

%prep
%autosetup -N
%patch -P 1 -P 2 -P 3 -P 4 -p1
find "." -type f -exec grep -l '/usr/bin/python' {} + |
	xargs -r perl -i -lpe \
	's{#! ?/usr/bin/python\S*}{#!/usr/bin/python3}g;'
find "." -type f -exec grep -l '/usr/bin/env ' {} + |
	xargs -r perl -i -lpe \
	's{#! ?/usr/bin/env python\S*}{#!/usr/bin/python3}g;
	 s{#! ?/usr/bin/env sh}{#!/bin/sh}g;
	 s{#! ?/usr/bin/env bash}{#!/bin/bash}g;
	 s{#! ?/usr/bin/env }{#!/usr/bin/}g;'
pushd third_party/xxhash
%patch -P 14 -P 15 -p1
popd
rm -Rf third_party/abseil-cpp/

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%define _lto_cflags %nil

# protoc is invoked strangely; make it happy with this dir or it will assert()
mkdir -p third_party/protobuf/src

cp -a /usr/src/opencensus-proto third_party/
export CFLAGS="%optflags -Wno-error"
export CXXFLAGS="$CFLAGS"
find "." -type f -exec grep '/usr/bin/env ' {} + || :
pushd .
%cmake -DgRPC_INSTALL=ON                  \
       -DgRPC_INSTALL_LIBDIR:PATH="%_lib" \
       -DgRPC_INSTALL_CMAKEDIR:PATH="%_libdir/cmake/grpc" \
       -DgRPC_ABSL_PROVIDER=package       \
       -DgRPC_CARES_PROVIDER=package      \
       -DgRPC_PROTOBUF_PROVIDER=package   \
       -DgRPC_RE2_PROVIDER=package        \
       -DgRPC_SSL_PROVIDER=package        \
       -DZLIB_LIBRARY=%{_libdir}/libz.so  \
       -DgRPC_ZLIB_PROVIDER=package \
       -DCMAKE_CXX_STANDARD=17
%cmake_build
popd
find "." -type f -exec grep '/usr/bin/env ' {} + || :

%install
b="%buildroot"
%cmake_install

pushd "$b/usr"
rm -fv lib/*.a share/grpc/*.pem
popd

# Install sources
pushd %__builddir
rm -fv CMakeFiles/*.log
make clean
find . -type f "(" -name "*.so" -o -name "*.o" -o -name ".git*" -o \
	-name "*.bin" -o -name "*.out" ")" -exec rm -Rfv {} +
popd
# Don't include abseil-cpp in sources
rm -fr third_party/abseil-cpp/*
# Don't include non-deterministic log in sources
rm -f build/CMakeFiles/CMakeConfigureLog.yaml

mkdir -p "%buildroot/%src_install_dir"
cp -r * "%buildroot/%src_install_dir"

%fdupes %buildroot/%_prefix

# Checks cannot be run because of `make clean` above
#%%check

%ldconfig_scriptlets -n libgrpc%lver
%ldconfig_scriptlets -n libgrpc%lverp
%ldconfig_scriptlets -n libgrpc++%lverp
%ldconfig_scriptlets -n libupb%lver

%files -n libgrpc%lver
%_libdir/libaddress_sorting.so.%{lver}*
%_libdir/libgpr*.so.%{lver}*
%_libdir/libgrpc*.so.%{lver}*
%_libdir/libutf8_range_lib.so.%{lver}*

%files -n libgrpc%lverp
%_libdir/libgrpc_authorization_provider.so.1.*
%_libdir/libgrpc_plugin_support.so.1.*

%files -n libgrpc++%lverp
%_libdir/libgrpc++*.so.*
%_libdir/libgrpcpp_channelz.so.*

%files -n libupb%lver
%_libdir/libupb*.so.%{lver}*

%files devel
%license LICENSE
%_bindir/*
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%_libdir/cmake/grpc/

%files -n upb-devel
%_libdir/libupb*.so

%files source
%src_install_dir

%changelog
