#
# spec file for package python-grpcio
#
# Copyright (c) 2022 SUSE LLC
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
# PYTHON2 NOT SUPPORTED BY UPSTREAM
%define         skip_python2 1
Name:           python-grpcio
Version:        1.51.1
Release:        0
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://grpc.io
Source:         https://files.pythonhosted.org/packages/source/g/grpcio/grpcio-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-grpcio-disable-boring-ssl.patch gh#grpc/grpc#24498 badshah400@gmail.com -- Make enabling system ssl disable boring ssl; patch taken from upstream PR
Patch0:         python-grpcio-disable-boring-ssl.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
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
Requires:       python-six >= 1.5.2
Suggests:       python-enum34 >= 1.0.4
Suggests:       python-futures >= 2.2.0
%python_subpackages

%description
gRPC is a remote procedure call (RPC) framework. gRPC enables client
and server applications to communicate, and enables the building of
connected systems.

%prep
%autosetup -p1 -n grpcio-%{version}

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags}"
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=true
export GRPC_PYTHON_BUILD_SYSTEM_CARES=true
export GRPC_PYTHON_BUILD_SYSTEM_RE2=true
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# a symlink to the shared system certificates is used
%python_expand ln -sf %{_localstatedir}/lib/ca-certificates/ca-bundle.pem %{buildroot}%{$python_sitearch}/grpc/_cython/_credentials/roots.pem

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/grpc/
%{python_sitearch}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
