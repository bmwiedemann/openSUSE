#
# spec file for package python-google-cloud-trace
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
Name:           python-google-cloud-trace
Version:        1.19.0
Release:        0
License:        Apache-2.0
Summary:        Google Cloud Trace API client library
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-trace
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-trace/google_cloud_trace-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 2.11.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module grpcio >= 1.33.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 4.25.8}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 2.11.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-grpcio >= 1.33.2
Requires:       python-proto-plus >= 1.22.3
Requires:       python-protobuf >= 4.25.8
BuildArch:      noarch

%python_subpackages

%description
Google Cloud Trace API client library

%prep
%setup -q -n google_cloud_trace-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/trace*
%{python_sitelib}/google_cloud_trace-%{version}*-info

%changelog
