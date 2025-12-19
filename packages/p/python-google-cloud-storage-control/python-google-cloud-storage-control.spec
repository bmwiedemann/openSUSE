#
# spec file for package python-google-cloud-storage-control
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


Name:           python-google-cloud-storage-control
Version:        1.8.0
Release:        0
Summary:        Google Cloud Storage Control API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage-control
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-storage-control/google_cloud_storage_control-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 1.34.1}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.14.0}
BuildRequires:  %{python_module grpcio >= 1.33.2}
BuildRequires:  %{python_module proto-plus >= 1.25.0}
BuildRequires:  %{python_module protobuf >= 3.20.2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.34.1
Requires:       python-google-auth >= 2.14.1
Requires:       python-grpc-google-iam-v1 >= 0.14.0
Requires:       python-grpcio >= 1.33.2
Requires:       python-proto-plus >= 1.25.0
Requires:       python-protobuf >= 3.20.2
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Storage Control API client library

%prep
%autosetup -p1 -n google_cloud_storage_control-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/google
%dir %{python_sitelib}/google/cloud
%{python_sitelib}/google/cloud/storage_control
%{python_sitelib}/google/cloud/storage_control_v2
%{python_sitelib}/google_cloud_storage_control-%{version}.dist-info

%changelog
