#
# spec file for package python-google-cloud-spanner
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
Name:           python-google-cloud-spanner
Version:        3.40.1
Release:        0
Summary:        Google Cloud Spanner API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-spanner
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-spanner/google-cloud-spanner-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 1.34.0}
BuildRequires:  %{python_module google-cloud-core >= 1.4.1}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.12.4}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module protobuf >= 3.19.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sqlparse >= 0.4.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.34.0
Requires:       python-google-cloud-core >= 1.4.1
Requires:       python-grpc-google-iam-v1 >= 0.12.4
Requires:       python-proto-plus >= 1.22.0
Requires:       python-protobuf >= 3.19.5
Requires:       python-sqlparse >= 0.4.4
Suggests:       python-libcst >= 0.2.5
Suggests:       python-opentelemetry-api >= 1.1.0
Suggests:       python-opentelemetry-sdk >= 1.1.0
Suggests:       python-opentelemetry-instrumentation >= 0.20b0
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Spanner API client library

%prep
%autosetup -p1 -n google-cloud-spanner-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
echo 0
# TODO: enable tests. I need to find a way to fix the python path
# because it loads the /usr/lib/$python/site-packages/google for
# dependencies and there it can't find the new package.
#%%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%pycache_only %{python_sitelib}/google/cloud/__pycache__
%{python_sitelib}/google_cloud_spanner-%{version}-*-nspkg.pth
%{python_sitelib}/google/cloud/spanner*
%{python_sitelib}/google_cloud_spanner-%{version}.dist-info

%changelog
