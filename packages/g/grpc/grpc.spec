#
# spec file for package grpc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lver 7
%define lverp 1
%define src_install_dir /usr/src/%name
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           grpc
Version:        1.23.1
Release:        0
%define rver	1.23.1
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://grpc.io/
Source0:        https://github.com/grpc/grpc/archive/v%rver.tar.gz
Source1:        %{name}-rpmlintrc
Patch1:         gettid.patch
Patch2:         0001-bazel-Replace-boringssl-with-openssl.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  zypper
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(protobuf) >= 3.8.0
BuildRequires:  pkgconfig(zlib)

%description
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n libgrpc%lver
Summary:        HTTP/2-based Remote Procedure Call implementation
Group:          System/Libraries
%if "%lver" == "7"
# prior error in packaging
Conflicts:      libgrpc6
%endif

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

%package devel
Summary:        Development files for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Tools/Building
Requires:       libgrpc%lver = %version
Requires:       libgrpc++%lverp = %version

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the gRPC reference implementation.

%package source
Summary:        Source code of gRPC
Group:          Development/Sources
BuildArch:      noarch

%description -n grpc-source
This subpackage contains source code of the gRPC reference implementation.

%package -n python2-grpcio
Summary:        Python language bindings for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Libraries/Python
Requires:       libgrpc%lver = %version-%release
Requires:       python = %python2_version

%description -n python2-grpcio
This subpackage contains the python2 bindings.

%package -n python3-grpcio
Summary:        Python language bindings for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Libraries/Python
Requires:       libgrpc%lver = %version-%release
Requires:       python = %python3_version

%description -n python3-grpcio
This subpackage contains the python3 bindings.

%prep
%autosetup -n grpc-%rver -p1
sed -i -e "s|%%LIBDIR%%|%{_libdir}|" bazel/grpc_deps.bzl

%build
%define _lto_cflags %nil
# protoc is invoked strangely; make it happy with this dir or it will assert()
mkdir -p third_party/protobuf/src

export CFLAGS="%optflags -Wno-error"
export CXXFLAGS="$CFLAGS"
make %{?_smp_mflags} STRIP=/bin/true V=1 VERBOSE=1

# build python module
export GRPC_PYTHON_BUILD_WITH_CYTHON=True
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=True
export GRPC_PYTHON_BUILD_SYSTEM_CARES=True
%python_build

%install
b="%buildroot"
# work around "Argument list too long"
ln -s "%buildroot" "b"
%make_install DESTDIR="b" prefix="b/%_prefix" STRIP=/bin/true V=1 VERBOSE=1

find "$b/%_includedir" -type f -exec chmod a-x {} +
pushd "$b/usr"
rm -fv lib/*.a share/grpc/*.pem
perl -i -pe 's{^prefix=.*}{prefix=%_prefix}' lib/pkgconfig/*.pc
perl -i -pe 's{^libdir=.*}{libdir=%_libdir}' lib/pkgconfig/*.pc
if test ! -d lib64 && test "%_lib" = lib64; then
	mv lib lib64
fi
popd
%python_install

# Install sources
make clean
rm -f "b" "a.out"
find . -type f "(" -name "*.so" -o -name "*.o" -o -name ".git*" ")" -exec rm -rf {} +
mkdir -p "%buildroot/%src_install_dir"
cp -r * "%buildroot/%src_install_dir"

%fdupes %buildroot/%_prefix

%post   -n libgrpc%lver -p /sbin/ldconfig
%postun -n libgrpc%lver -p /sbin/ldconfig
%post   -n libgrpc++%lverp -p /sbin/ldconfig
%postun -n libgrpc++%lverp -p /sbin/ldconfig

%files -n libgrpc%lver
%_libdir/libaddress_sorting.so.%{lver}*
%_libdir/libgpr*.so.%{lver}*
%_libdir/libgrpc*.so.%{lver}*

%files -n libgrpc++%lverp
%_libdir/libgrpc++*.so.%{lverp}*
%_libdir/libgrpcpp_channelz.so.%{lverp}*

%files devel
%license LICENSE
%_bindir/*
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/*.so

%files source
%src_install_dir

%files -n python2-grpcio
%python2_sitearch/grpc*

%files -n python3-grpcio
%python3_sitearch/grpc*

%changelog
