#
# spec file for package python-djangorestframework-csv
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


Name:           python-djangorestframework-csv
Version:        3.0.2
Release:        0
Summary:        CSV Tools for Django REST Framework
License:        BSD-1-Clause
URL:            https://github.com/mjumbewu/django-rest-framework-csv
Source:         https://files.pythonhosted.org/packages/source/d/djangorestframework-csv/djangorestframework-csv-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/mjumbewu/django-rest-framework-csv/refs/heads/master/testsettings.py
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module djangorestframework}
# /SECTION
BuildRequires:  fdupes
Requires:       python-djangorestframework
BuildArch:      noarch
%python_subpackages

%description
CSV Tools for Django REST Framework

%prep
%autosetup -p1 -n djangorestframework-csv-%{version}
cp %{SOURCE1} rest_framework_csv

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=rest_framework_csv.testsettings
%pyunittest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/rest_framework_csv
%{python_sitelib}/djangorestframework_csv-%{version}.dist-info

%changelog
