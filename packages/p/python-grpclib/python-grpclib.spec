#
# spec file for package python-grpclib
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


Name:           python-grpclib
Version:        0.4.7
Release:        0
Summary:        Pure-Python gRPC implementation for asyncio
License:        BSD-3-Clause
URL:            https://github.com/vmagamedov/grpclib
Source:         https://github.com/vmagamedov/grpclib/archive/v%{version}.tar.gz#/grpclib-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.6.0}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module h2 >= 3.1.0}
BuildRequires:  %{python_module multidict}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module async-timeout}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module protobuf}
# /SECTION
BuildRequires:  fdupes
Requires:       python-h2 >= 3.1.0
Requires:       python-multidict
Suggests:       python-protobuf >= 3.20.0
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pure-Python gRPC implementation for asyncio

%prep
%autosetup -p1 -n grpclib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/protoc-gen-python_grpc
%python_clone -a %{buildroot}%{_bindir}/protoc-gen-grpclib_python
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_bindir}

%check
# no google.rpc python module
%pytest --ignore tests/test_status_details_codec.py --ignore tests/test_server_events.py --ignore tests/test_client_events.py

%post
%python_install_alternative protoc-gen-python_grpc protoc-gen-grpclib_python

%postun
%python_uninstall_alternative protoc-gen-python_grpc

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/protoc-gen-python_grpc
%python_alternative %{_bindir}/protoc-gen-grpclib_python
%{python_sitelib}/grpclib
%{python_sitelib}/grpclib-%{version}.dist-info

%changelog
