#
# spec file for package python-google-cloud-bigquery
#
# Copyright (c) 2026 SUSE LLC
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
Name:           python-google-cloud-bigquery
Version:        3.41.0
Release:        0
Summary:        Google BigQuery API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-bigquery
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-bigquery/google_cloud_bigquery-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module google-api-core >= 2.10.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module google-cloud-core >= 1.6.0}
BuildRequires:  %{python_module google-cloud-testutils}
BuildRequires:  %{python_module google-resumable-media >= 0.6.0}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module protobuf >= 3.19.5}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module python-dateutil >= 2.7.2}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module google-cloud-bigquery-storage >= 2.0.0}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module grpcio >= 1.47.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-freezegun}
BuildRequires:  fdupes
Requires:       python-google-api-core >= 2.10.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-google-cloud-core >= 1.6.0
Requires:       python-google-resumable-media >= 0.6.0
Requires:       python-requests >= 2.18.0
Requires:       python-python-dateutil >= 2.7.2
Requires:       python-packaging >= 20.0
BuildArch:      noarch
%python_subpackages

%description
Querying massive datasets can be time consuming and expensive without the right
hardware and infrastructure. Google BigQuery solves this problem by enabling
super-fast, SQL queries against append-mostly tables, using the processing
power of Google's infrastructure.

%prep
%autosetup -n google_cloud_bigquery-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip system tests that require cloud infrastructure and additional dependencies
%pytest tests/unit

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/bigquery*
%{python_sitelib}/google_cloud_bigquery-%{version}.dist-info

%changelog
