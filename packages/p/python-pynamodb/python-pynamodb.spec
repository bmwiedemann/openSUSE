#
# spec file for package python-pynamodb
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pynamodb
Version:        4.3.3
Release:        0
Summary:        Python Interface to DynamoDB
License:        MIT
URL:            https://github.com/pynamodb/PynamoDB
Source0:        https://files.pythonhosted.org/packages/source/p/pynamodb/pynamodb-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-botocore >= 1.12.54
Requires:       python-python-dateutil >= 2.1
Requires:       python-six
Recommends:     python-blinker >= 1.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module blinker >= 1.3}
BuildRequires:  %{python_module botocore >= 1.12.54}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A Python interface for Amazon's DynamoDB.

%prep
%setup -q -n pynamodb-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export AWS_SECRET_ACCESS_KEY=fake_key
export AWS_ACCESS_KEY_ID=fake_id
# Sadly the tests since 4.x series require local dynamdb running on the local machine instead of mocking
#%%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
