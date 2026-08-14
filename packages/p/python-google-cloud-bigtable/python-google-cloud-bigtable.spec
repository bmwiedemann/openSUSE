#
# spec file for package python-google-cloud-bigtable
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
Name:           python-google-cloud-bigtable
Version:        2.41.0
Release:        0
Summary:        Google Cloud Bigtable API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigtable
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-bigtable/google_cloud_bigtable-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Core dependencies
BuildRequires:  %{python_module grpcio >= 1.59.0 if %python-base < 3.14}
BuildRequires:  %{python_module google-api-core >= 2.24.2}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module google-cloud-core >= 2.0.0}
BuildRequires:  %{python_module google-crc32c >= 1.6.0}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.14.2}
BuildRequires:  %{python_module grpcio >= 1.75.1 if %python-base >= 3.14}
BuildRequires:  %{python_module proto-plus >= 1.26.1}
BuildRequires:  %{python_module protobuf >= 6.33.5}
BuildRequires:  fdupes
BuildArch:      noarch
# Runtime dependencies
%if %python_version_nodots < 314
Requires:       python-grpcio >= 1.59.0
%else
Requires:       python-grpcio >= 1.75.1
%endif
Requires:       python-google-api-core >= 2.24.2
Requires:       python-google-auth >= 2.14.1
Requires:       python-google-cloud-core >= 2.0.0
Requires:       python-google-crc32c >= 1.6.0
Requires:       python-grpc-google-iam-v1 >= 0.14.2
Requires:       python-proto-plus >= 1.26.1
Requires:       python-protobuf >= 6.33.5

%python_subpackages

%description
Google Cloud Bigtable API client library.

%prep
%autosetup -p1 -n google_cloud_bigtable-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%dir %{python_sitelib}/google
%dir %{python_sitelib}/google/cloud
%{python_sitelib}/google/cloud/bigtable
%{python_sitelib}/google/cloud/bigtable_admin
%{python_sitelib}/google/cloud/bigtable_admin_v2
%{python_sitelib}/google/cloud/bigtable_v2
%{python_sitelib}/google_cloud_bigtable-%{version}.dist-info

%changelog
