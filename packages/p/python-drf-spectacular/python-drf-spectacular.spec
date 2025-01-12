#
# spec file for package python-drf-spectacular
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


# python 3.13 not supported yet
%define skip_python313 1
Name:           python-drf-spectacular
Version:        0.28.0
Release:        0
Summary:        Sane and flexible OpenAPI 3 schema generation for Django REST framework
License:        BSD-3-Clause
URL:            https://github.com/tfranzel/drf-spectacular
Source:         https://files.pythonhosted.org/packages/source/d/drf-spectacular/drf_spectacular-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module djangorestframework >= 3.10.3}
BuildRequires:  %{python_module django-oauth-toolkit}
BuildRequires:  %{python_module inflection >= 0.3.1}
BuildRequires:  %{python_module jsonschema >= 2.6.0}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module psycopg}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module uritemplate >= 2.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 2.2
Requires:       python-djangorestframework >= 3.10.3
Requires:       python-inflection >= 0.3.1
Requires:       python-jsonschema >= 2.6.0
Requires:       python-PyYAML >= 5.1
Requires:       python-uritemplate >= 2.0.0
Suggests:       python-drf-spectacular-sidecar
BuildArch:      noarch
%python_subpackages

%description
Sane and flexible OpenAPI 3 schema generation for Django REST framework

%prep
%autosetup -p1 -n drf_spectacular-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# contrib tests are largely broken or need some modules which are not packaged yet
rm -r tests/contrib
%pytest

%files %{python_files}
%{python_sitelib}/drf_spectacular
%{python_sitelib}/drf_spectacular-%{version}.*info

%changelog
