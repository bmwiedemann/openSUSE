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


%define lname libgrpc6
%define src_install_dir /usr/src/%{name}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           grpc
Version:        1.21.3
Release:        0
%define rver	1.21.3
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            http://grpc.io/
Source:         https://github.com/grpc/grpc/archive/v%rver.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(protobuf) >= 3.8.0
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package -n %lname
Summary:        HTTP/2-based Remote Procedure Call implementation
Group:          System/Libraries

%description -n %lname
The reference implementation of the gRPC protocol, done on top of
HTTP/2 with support for synchronous and asynchronous calls. gRPC uses
Protocol Buffers as the Interface Definition Language by default.

%package devel
Summary:        Development files for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Tools/Building
Requires:       %lname = %version

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
Requires:       %lname = %version-%release
Requires:       python = %python2_version

%description -n python2-grpcio
This subpackage contains the python2 bindings.

%package -n python3-grpcio
Summary:        Python language bindings for grpc, a HTTP/2 Remote Procedure Call implementation
Group:          Development/Libraries/Python
Requires:       %lname = %version-%release
Requires:       python = %python3_version

%description -n python3-grpcio
This subpackage contains the python3 bindings.

%prep
%setup -qn grpc-%rver

%build
make %{?_smp_mflags} STRIP=/bin/true V=1 VERBOSE=1 \
	CFLAGS="%optflags -Wno-error" CXXFLAGS="%optflags -Wno-error"

# build python module
export GRPC_PYTHON_BUILD_WITH_CYTHON=True
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=True
export GRPC_PYTHON_BUILD_SYSTEM_CARES=True
export CFLAGS="%optflags"
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
mkdir -p %{buildroot}%{src_install_dir}
tar -xzf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix env-script-interpreter rpmlint error
find %{buildroot}%{src_install_dir} -type f -exec sed -i 's|#!/usr/bin/env bash|#!/bin/bash|' "{}" +
find %{buildroot}%{src_install_dir} -type f -exec sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' "{}" +
find %{buildroot}%{src_install_dir} -type f \( -name "*.bzl" -o -name "*.py" \) -exec sed -i 's|#!/usr/bin/env python2.7|#!/usr/bin/python2.7|' "{}" +
find %{buildroot}%{src_install_dir} -type f \( -name "*.bzl" -o -name "*.py" \) -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|' "{}" +

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libaddress_sorting.so.*
%_libdir/libgpr*.so.*
%_libdir/libgrpc*.so.*

%files devel
%defattr(-,root,root)
%license LICENSE
%_bindir/*
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/*.so

%files source
%{src_install_dir}

%files -n python2-grpcio
%python2_sitearch/grpc*

%files -n python3-grpcio
%python3_sitearch/grpc*

%changelog
