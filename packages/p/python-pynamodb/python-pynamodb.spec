#
# spec file for package python-pynamodb
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-pynamodb
Version:        6.1.0
Release:        0
Summary:        Python Interface to DynamoDB
License:        MIT
URL:            https://github.com/pynamodb/PynamoDB
Source0:        https://files.pythonhosted.org/packages/source/p/pynamodb/pynamodb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-botocore >= 1.12.54
Requires:       python-python-dateutil >= 2.1
Recommends:     python-blinker >= 1.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module blinker >= 1.3}
BuildRequires:  %{python_module botocore >= 1.12.54}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.1}
# /SECTION
%python_subpackages

%description
A Python interface for Amazon's DynamoDB.

%prep
%setup -q -n pynamodb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export AWS_SECRET_ACCESS_KEY=fake_key
export AWS_ACCESS_KEY_ID=fake_id
# Sadly the tests since 4.x series require local dynamdb running on the local machine instead of mocking
#%%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pynamodb
%{python_sitelib}/pynamodb-%{version}.dist-info

%changelog
