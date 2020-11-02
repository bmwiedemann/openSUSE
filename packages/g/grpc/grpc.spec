#
# spec file for package grpc
#
# Copyright (c) 2020 SUSE LLC
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


%define lver 13
%define lverp 1
%define lverplugin 1
%define src_install_dir /usr/src/%name
Name:           grpc
Version:        1.33.2
Release:        0
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://grpc.io/
Source:         https://github.com/grpc/grpc/archive/v%version.tar.gz
Source2:        %name-rpmlintrc
# PATCH-FIX-UPSTREAM grpc-correct-pkgconfig-path.patch badshah400@gmail.com -- Make path for pkgconfig file installation consistent with gRPC_INSTALL_LIBDIR specification
Patch1:         grpc-correct-pkgconfig-path.patch
BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  zypper
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(protobuf) >= 3.8.0
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

%package -n libgrpc++%lverp
Summary:        HTTP/2-based Remote Procedure Call implementation
Group:          System/Libraries
%if "%lverp" == "1"
# prior error in packaging
Conflicts:      libgrpc6
%endif

%description -n libgrpc++%lverp
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n libgrpc_plugin_support%lverplugin
Summary:        HTTP/2-based Remote Procedure Call implementation - plugin support
Group:          System/Libraries

%description -n libgrpc_plugin_support%lverplugin
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

This package provides the shared library to support plugins for grpc.

%package -n libupb%lver
Summary:        A small protobuf implementation in C
Group:          System/Libraries

%description -n libupb%lver
μpb (often written 'upb') is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

%package devel
Summary:        Development files for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Tools/Building
Requires:       libgrpc%lver = %version
Requires:       libgrpc++%lverp = %version
Requires:       libgrpc_plugin_support%lverplugin = %version
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
μpb (often written 'upb') is a small protobuf implementation written in C.

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
%autosetup -p1
rm -Rf third_party/abseil-cpp/

%build
%define _lto_cflags %nil
# protoc is invoked strangely; make it happy with this dir or it will assert()
mkdir -p third_party/protobuf/src

export CFLAGS="%optflags -Wno-error"
export CXXFLAGS="$CFLAGS"
%cmake -DgRPC_INSTALL=ON                  \
       -DgRPC_INSTALL_LIBDIR:PATH="%_lib" \
       -DgRPC_INSTALL_CMAKEDIR:PATH="%_libdir/cmake/grpc" \
       -DgRPC_ABSL_PROVIDER=package \
       -DgRPC_CARES_PROVIDER=package      \
       -DgRPC_PROTOBUF_PROVIDER=package   \
       -DgRPC_RE2_PROVIDER=package        \
       -DgRPC_SSL_PROVIDER=package        \
       -DgRPC_ZLIB_PROVIDER=package
%cmake_build

%install
b="%buildroot"
# work around "Argument list too long"
ln -s "%buildroot" "b"
%cmake_install

pushd "$b/usr"
rm -fv lib/*.a share/grpc/*.pem
popd

# Install sources
pushd %__builddir
make clean
rm -f "b"
find . -type f "(" -name "*.so" -o -name "*.o" -o -name ".git*" -o -name "*.bin" -o -name "*.out" ")" -exec rm -rf {} +
popd
# Don't include abseil-cpp in sources
rm -fr third_party/abseil-cpp/*

mkdir -p "%buildroot/%src_install_dir"
cp -r * "%buildroot/%src_install_dir"

%fdupes %buildroot/%_prefix

%post   -n libgrpc%lver -p /sbin/ldconfig
%postun -n libgrpc%lver -p /sbin/ldconfig
%post   -n libgrpc++%lverp -p /sbin/ldconfig
%postun -n libgrpc++%lverp -p /sbin/ldconfig
%post   -n libgrpc_plugin_support%lverplugin -p /sbin/ldconfig
%postun -n libgrpc_plugin_support%lverplugin -p /sbin/ldconfig

%files -n libgrpc%lver
%_libdir/libaddress_sorting.so.%{lver}*
%_libdir/libgpr*.so.%{lver}*
%_libdir/libgrpc*.so.%{lver}*

%files -n libgrpc++%lverp
%_libdir/libgrpc++*.so.%{lverp}*
%_libdir/libgrpcpp_channelz.so.%{lverp}*

%files -n libgrpc_plugin_support%lverplugin
%_libdir/libgrpc_plugin_support.so.%{lverplugin}*

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
