#
# spec file for package python-django-qsessions
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
Name:           python-django-qsessions
Version:        2.1.0
Release:        0
Summary:        Extended session backends for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/QueraTeam/django-qsessions
Source:         https://files.pythonhosted.org/packages/source/d/django-qsessions/django_qsessions-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-ua-parser >= 1.0.1
Suggests:       python-geoip2 >= 4.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module geoip2 >= 4.1.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ua-parser >= 1.0.1}
# /SECTION
%python_subpackages

%description
Extended session backends for Django.

%prep
%setup -q -n django_qsessions-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=${PWD}
%pytest

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{python_sitelib}/*qsessions*/

%changelog
