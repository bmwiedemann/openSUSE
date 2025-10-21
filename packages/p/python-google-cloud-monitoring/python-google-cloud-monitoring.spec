#
# spec file for package python-google-cloud-monitoring
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-google-cloud-monitoring
Version:        2.28.0
Release:        0
Summary:        Google Cloud Monitoring API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-monitoring
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-monitoring/google_cloud_monitoring-%{version}.tar.gz
BuildRequires:  %{python_module grpcio}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module google-api-core >= 1.34.1}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module proto-plus >= 1.25.0}
BuildRequires:  %{python_module protobuf >= 3.20.2}
BuildRequires:  %{python_module pytest-asyncio}
# /SECTION
BuildRequires:  fdupes
%if %python_version_nodots < 314
Requires:       python-grpcio >= 1.33.2
%else
Requires:       python-grpcio >= 1.75.1
%endif
Requires:       python-google-api-core >= 1.34.1
Requires:       python-google-auth >= 2.14.1
Requires:       python-proto-plus >= 1.22.3
Requires:       python-proto-plus >= 1.25.0
Requires:       python-protobuf >= 3.20.2
Suggests:       python-pandas >= 0.23.2
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Monitoring API client library

%prep
%autosetup -p1 -n google_cloud_monitoring-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pytest --ignore=tests/system

%files %{python_files}
%{python_sitelib}/google/cloud/monitoring
%{python_sitelib}/google/cloud/monitoring_v3
%{python_sitelib}/google_cloud_monitoring-%{version}.dist-info

%changelog
