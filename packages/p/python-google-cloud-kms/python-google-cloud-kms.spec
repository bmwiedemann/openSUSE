#
# spec file for package python-google-cloud-kms
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


%{?sle15_python_module_pythons}
Name:           python-google-cloud-kms
Version:        2.21.4
Release:        0
Summary:        Cloud Key Management Service (KMS) API API client library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-kms/google-cloud-kms-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 1.34.1}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.12.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 3.19}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.34.1
Requires:       python-google-auth
Requires:       python-grpc-google-iam-v1 >= 0.12.4
Requires:       python-proto-plus >= 1.22.3
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Cloud Key Management Service (KMS) API API client library

%prep
%setup -q -n google-cloud-kms-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/kms
%{python_sitelib}/google/cloud/kms_v1
%{python_sitelib}/google_cloud_kms-%{version}.dist-info

%changelog
