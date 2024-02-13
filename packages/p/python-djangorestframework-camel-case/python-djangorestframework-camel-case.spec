#
# spec file for package python-djangorestframework-camel-case
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
Name:           python-djangorestframework-camel-case
Version:        1.4.2
Release:        0
Summary:        Camel case JSON support for Django REST framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vbabiy/djangorestframework-camel-case
Source:         https://files.pythonhosted.org/packages/source/d/djangorestframework-camel-case/djangorestframework-camel-case-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/vbabiy/djangorestframework-camel-case/master/tests.py
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Camel case JSON support for Django REST framework.

%prep
%setup -q -n djangorestframework-camel-case-%{version}
cp %{SOURCE1} tests.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/djangorestframework_camel_case
%{python_sitelib}/djangorestframework_camel_case-%{version}*-info

%changelog
