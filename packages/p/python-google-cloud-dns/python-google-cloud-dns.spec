#
# spec file for package python-google-cloud-dns
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


%define upstream_name google_cloud_dns
%{?sle15_python_module_pythons}
Name:           python-google-cloud-dns
Version:        0.36.0
Release:        0
Summary:        Google Cloud DNS API access
License:        Apache-2.0
URL:            https://github.com/googleapis/python-dns
Source:         https://files.pythonhosted.org/packages/source/g/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildRequires:  %{python_module google-cloud-core >= 1.4.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module google-api-core}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-cloud-core >= 1.4.4
BuildArch:      noarch
%python_subpackages

%description
Cloud DNS API provides methods that you can use to manage DNS for your
applications.

%prep
%autosetup -n %{upstream_name}-%{version}
find tests -name "*.py" | xargs sed -i 's/import mock/import unittest.mock as mock/'
# No integration tests, these require credentials
rm -rf tests/system

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/dns*
%{python_sitelib}/google_cloud_dns-%{version}.dist-info

%changelog
