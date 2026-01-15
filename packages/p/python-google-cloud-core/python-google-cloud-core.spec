#
# spec file for package python-google-cloud-core
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


%{?sle15_python_module_pythons}
Name:           python-google-cloud-core
Version:        2.5.0
Release:        0
Summary:        Google Cloud API client core library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-cloud-core
Source:         https://files.pythonhosted.org/packages/source/g/google_cloud_core/google_cloud_core-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module google-api-core >= 1.31.6}
BuildRequires:  %{python_module google-auth >= 1.25.0}
BuildRequires:  %{python_module grpcio >= 1.38.0 if %python-base < 3.14}
BuildRequires:  %{python_module grpcio >= 1.75.1 if %python-base >= 3.14}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.31.6
Requires:       python-google-auth >= 1.25.0
Recommends:     python-grpcio >= 1.38.0
BuildArch:      noarch
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-google-cloud-core < %{version}
%endif
%python_subpackages

%description
Core Helpers for Google Cloud Python Client Library
This library is not meant to stand-alone. Instead it defines
common helpers (e.g. base ``Client`` classes) used by all of the
``google-cloud-*`` packages.

%prep
%setup -q -n google_cloud_core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="--import-mode=importlib"
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/google/cloud
%{python_sitelib}/google_cloud_core-%{version}.dist-info

%changelog
