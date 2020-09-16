#
# spec file for package python-grpcio
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


%global modname grpcio
# PYTHON2 NOT SUPPORTED BY UPSTREAM
%define         skip_python2 1
Name:           python-grpcio
Version:        1.31.0
Release:        0
Summary:        HTTP/2-based Remote Procedure Call implementation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://grpc.io
Source:         https://files.pythonhosted.org/packages/source/g/grpcio/grpcio-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
Requires:       python-six >= 1.5.2
Suggests:       python-enum34 >= 1.0.4
Suggests:       python-futures >= 2.2.0
%python_subpackages

%description
gRPC is a remote procedure call (RPC) framework. gRPC enables client
and server applications to communicate, and enables the building of
connected systems.

%prep
%setup -q -n grpcio-%{version}

%build
export CFLAGS="%{optflags}"
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=true
export GRPC_PYTHON_BUILD_SYSTEM_CARES=true
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/grpc/
%{python_sitearch}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
