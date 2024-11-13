#
# spec file for package python-grpcio
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


%global modname grpcio
%{?sle15_python_module_pythons}
Name:           python-grpcio
Version:        1.67.1
Release:        0
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://grpc.io
Source:         https://files.pythonhosted.org/packages/source/g/grpcio/grpcio-%{version}.tar.gz
# PATCH-FIX-SLE xxhash-avoid-armv6-unaligned-access.patch alarrosa@suse.com -- do not expect unaligned accesses to work on armv6
Patch1:         xxhash-avoid-armv6-unaligned-access.patch
# PATCH-FIX-SLE xxhash-ppc64le-gcc7.patch boo#1208794 alarrosa@suse.com -- fix build failure on ppc64le when using gcc 7
Patch2:         xxhash-ppc64le-gcc7.patch
Patch3:         fix-return-values.patch
BuildRequires:  %{python_module Cython >= 0.29.8}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel >= 0.29}
BuildRequires:  abseil-cpp-devel >= 20220623.0
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)
Requires:       ca-certificates
Recommends:     python-enum34 >= 1.0.4
Recommends:     python-futures >= 2.2.0
%python_subpackages

%description
gRPC is a remote procedure call (RPC) framework. gRPC enables client
and server applications to communicate, and enables the building of
connected systems.

%prep
%autosetup -p1 -n grpcio-%{version}

%build
export GRPC_BUILD_WITH_BORING_SSL_ASM=false
export GRPC_PYTHON_BUILD_SYSTEM_ABSL=true
export GRPC_PYTHON_BUILD_SYSTEM_CARES=true
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=true
export GRPC_PYTHON_BUILD_SYSTEM_RE2=true
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true
export GRPC_PYTHON_BUILD_WITH_CYTHON=true
export GRPC_PYTHON_CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# a symlink to the shared system certificates is used
%python_expand ln -sf %{_localstatedir}/lib/ca-certificates/ca-bundle.pem %{buildroot}%{$python_sitearch}/grpc/_cython/_credentials/roots.pem

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/grpc/
%{python_sitearch}/%{modname}-%{version}.dist-info

%changelog
