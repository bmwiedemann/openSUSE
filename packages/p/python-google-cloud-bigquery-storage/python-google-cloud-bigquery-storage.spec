#
# spec file for package python-google-cloud-bigquery-storage
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
Name:           python-google-cloud-bigquery-storage
Version:        2.37.0
Release:        0
Summary:        Google Cloud Bigquery Storage API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-bigquery-storage
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-bigquery-storage/google_cloud_bigquery_storage-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 2.10.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module google-cloud-core >= 1.6.0}
BuildRequires:  %{python_module grpcio >= 1.47.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module protobuf >= 3.19.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 2.10.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-google-cloud-core >= 1.6.0
Requires:       python-grpcio >= 1.47.0
Requires:       python-proto-plus >= 1.22.0
Requires:       python-protobuf >= 3.19.5
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Bigquery Storage API client library.

%prep
%autosetup -n google_cloud_bigquery_storage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/bigquery_storage
%{python_sitelib}/google/cloud/bigquery_storage_v1
%{python_sitelib}/google/cloud/bigquery_storage_v1alpha
%{python_sitelib}/google/cloud/bigquery_storage_v1beta
%{python_sitelib}/google/cloud/bigquery_storage_v1beta2
%{python_sitelib}/google_cloud_bigquery_storage-%{version}.dist-info

%changelog
