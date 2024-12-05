#
# spec file for package python-google-api-core
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-google-api-core
Version:        2.23.0
Release:        0
Summary:        Google API client core library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-core
Source:         https://files.pythonhosted.org/packages/source/g/google_api_core/google_api_core-%{version}.tar.gz
BuildRequires:  %{python_module googleapis-common-protos >= 1.56.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.3.0}
BuildRequires:  %{python_module wheel}
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-google-api-core < %{version}
%endif
# START TESTING SECTION
%if %{with test}
BuildRequires:  %{python_module google-api-core = %{version}}
BuildRequires:  %{python_module proto-plus}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
%endif
# END TESTING SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 2.14.1
Requires:       python-googleapis-common-protos >= 1.56.2
Requires:       python-grpcio >= 1.49.1
Requires:       python-grpcio-status >= 1.49.1
Requires:       python-requests >= 2.18.0
Requires:       (python-proto-plus >= 1.25.0 with python-proto-plus < 2.0.0dev0)
Requires:       (python-protobuf >= 3.19.5 with python-protobuf < 6.0.0.dev0)
BuildArch:      noarch
%python_subpackages

%description
Core Library for Google Client Libraries.

%prep
%autosetup -p1 -n google_api_core-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/google/api_core
%{python_sitelib}/google_api_core-%{version}.dist-info
%endif

%changelog
