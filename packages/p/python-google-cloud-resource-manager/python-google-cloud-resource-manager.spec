#
# spec file for package python-google-cloud-resource-manager
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
Name:           python-google-cloud-resource-manager
Version:        1.18.0
Release:        0
Summary:        Google Cloud Resource Manager API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-resource-manager
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-resource-manager/google_cloud_resource_manager-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 2.17.1}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.14.0}
BuildRequires:  %{python_module grpcio >= 1.59.0}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 4.25.8}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 2.17.1
Requires:       python-google-auth >= 2.14.1
Requires:       python-grpc-google-iam-v1 >= 0.14.0
Requires:       python-grpcio >= 1.59.0
Requires:       python-proto-plus >= 1.22.3
Requires:       python-protobuf >= 4.25.8
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Resource Manager API client library

%prep
%setup -q -n google_cloud_resource_manager-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/google_cloud_resource_manager-%{version}*
%dir %{python_sitelib}/google
%dir %{python_sitelib}/google/cloud
%{python_sitelib}/google/cloud/resourcemanager
%{python_sitelib}/google/cloud/resourcemanager_v3

%changelog
