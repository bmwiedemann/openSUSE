#
# spec file for package python-qcs-api-client-common
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


Name:           python-qcs-api-client-common
Version:        0.19.1
Release:        0
Summary:        Contains core QCS client functionality and middleware implementations
License:        Apache-2.0
URL:            https://github.com/rigetti/qcs-api-client-rust
Source0:        https://files.pythonhosted.org/packages/source/q/qcs-api-client-common/qcs_api_client_common-%{version}.tar.gz
Source1:        vendor.tar.zst
# Not shipped in the sdist
Source2:        https://raw.githubusercontent.com/rigetti/qcs-api-client-rust/refs/heads/main/LICENSE
BuildRequires:  %{python_module maturin >= 1.9.4}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module grpc-interceptor >= 0.15.0}
BuildRequires:  %{python_module grpcio >= 1.63.0}
BuildRequires:  %{python_module httpx >= 0.27.0}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module syrupy >= 4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-grpc-interceptor >= 0.15.0
Requires:       python-grpcio >= 1.63.0
Requires:       python-httpx >= 0.27.0
%python_subpackages

%description
The `qcs-api-client-common` package provides a suite of common functionalities for
QCS client applications. It offers reusable middleware implementations that can be
integrated into various client libraries. This allows for consistent behavior
across different projects and facilitates easier maintenance and scalability
of client-side logic.

%prep
%autosetup -p1 -n qcs_api_client_common-%{version} -a1
cp %{SOURCE2} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Requires network
donttest="(TestClientConfiguration and (test_default or test_load_profile))"
# Requires configuration files
donttest+=" or test_sync_method_from_async_context"
donttest+=" or test_refresh_interceptor"
%pytest_arch -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README-py.md
%{python_sitearch}/qcs_api_client_common
%{python_sitearch}/qcs_api_client_common-%{version}.dist-info

%changelog
