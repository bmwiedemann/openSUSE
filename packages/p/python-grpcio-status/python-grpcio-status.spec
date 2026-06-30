#
# spec file for package python-grpcio-status
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


%global modname grpcio_status
%{?sle15_python_module_pythons}
Name:           python-grpcio-status
Version:        1.81.1
Release:        0
Summary:        Status proto mapping for gRPC
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://grpc.io
Source:         https://files.pythonhosted.org/packages/source/g/grpcio-status/grpcio_status-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-googleapis-common-protos >= 1.5.5
Requires:       python-grpcio >= %{version}
Requires:       python-protobuf >= 6.33.5
BuildArch:      noarch
%python_subpackages

%description
gRPC is a remote procedure call (RPC) framework. gRPC enables client
and server applications to communicate, and enables the building of
connected systems.

This package implements the GRPC Python status proto mapping.

%prep
%autosetup -p1 -n grpcio_status-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/grpc_status
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
