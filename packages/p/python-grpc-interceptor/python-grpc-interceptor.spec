#
# spec file for package python-grpc-interceptor
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


Name:           python-grpc-interceptor
Version:        0.15.4
Release:        0
Summary:        Simplifies gRPC interceptors
License:        MIT
URL:            https://github.com/d5h-foss/grpc-interceptor
Source:         https://github.com/d5h-foss/grpc-interceptor/archive/refs/tags/v%{version}.tar.gz#/grpc-interceptor-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module grpcio >= 1.49.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module protobuf >= 4.21.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires:       python-grpcio >= 1.49.1
Recommends:     python-protobuf >= 4.21.9
BuildArch:      noarch
%python_subpackages

%description
Simplified Python gRPC interceptors.

The Python `grpc` package provides service interceptors, but they're a bit hard to
use because of their flexibility. The `grpc` interceptors don't have direct access
to the request and response objects, or the service context. Access to these are often
desired, to be able to log data in the request or response, or set status codes on the
context.

%prep
%autosetup -p1 -n grpc-interceptor-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/grpc_interceptor
%{python_sitelib}/grpc_interceptor-%{version}.dist-info

%changelog
