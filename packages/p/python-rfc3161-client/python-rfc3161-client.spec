#
# spec file for package python-rfc3161-client
#
# Copyright (c) 2025 SUSE LLC
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-rfc3161-client
Version:        1.0.0
Release:        0
Summary:        Python library implementing the Time-Stamp Protocol (TSP) described in RFC 3161
License:        Apache-2.0
URL:            https://github.com/trailofbits/rfc3161-client
Source:         https://files.pythonhosted.org/packages/source/r/rfc3161-client/rfc3161_client-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module maturin >= 1.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module devel}

BuildRequires:  cargo >= 1.56.0
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.56.0

%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module rfc3161-client == %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module cryptography >= 43}
BuildRequires:  %{python_module pretend}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography >= 43
%python_subpackages

%description
rfc3161-client is a Python library implementing the Time-Stamp
Protocol (TSP) described in RFC 3161.

%prep
%autosetup -p1 -a1 -n rfc3161_client-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%pytest_arch -k "not test_verify_leaf_certs_no_eku"
%endif

%if !%{with test}
%files %{python_files}
%{python_sitearch}/rfc3161_client
%{python_sitearch}/rfc3161_client-%{version}.dist-info
%endif

%changelog
