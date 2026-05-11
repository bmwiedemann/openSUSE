#
# spec file for package python-google-cloud-dataplex
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
Name:           python-google-cloud-dataplex
Version:        2.18.0
Release:        0
Summary:        Google Cloud Dataplex API client library
License:        Apache-2.0
URL:            https://pypi.org/project/google-cloud-dataplex/
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-dataplex/google_cloud_dataplex-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Core dependencies
BuildRequires:  %{python_module google-api-core >= 2.11.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.14.0}
BuildRequires:  %{python_module grpcio >= 1.33.2}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 4.25.8}
BuildRequires:  fdupes
BuildArch:      noarch
# Runtime dependencies
Requires:       python-google-api-core >= 2.11.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-grpc-google-iam-v1 >= 0.14.0
Requires:       python-grpcio >= 1.33.2
Requires:       python-proto-plus >= 1.22.3
Requires:       python-protobuf >= 4.25.8

%python_subpackages

%description
Google Cloud Dataplex API client library.
Dataplex is an intelligent data fabric that helps organizations centrally
manage, monitor, and govern their data across data lakes, data warehouses, and
data marts. It provides a unified governance solution for data and AI assets.

%prep
%autosetup -p1 -n google_cloud_dataplex-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%dir %{python_sitelib}/google
%dir %{python_sitelib}/google/cloud
%{python_sitelib}/google/cloud/dataplex
%{python_sitelib}/google/cloud/dataplex_v1
%{python_sitelib}/google_cloud_dataplex-%{version}.dist-info

%changelog
