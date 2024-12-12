#
# spec file for package python-django-bootstrap3
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
Name:           python-django-bootstrap3
Version:        24.3
Release:        0
Summary:        Bootstrap support for Django projects
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/zostera/django-bootstrap3
Source0:        https://files.pythonhosted.org/packages/source/d/django_bootstrap3/django_bootstrap3-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Bootstrap support for Django projects.

%prep
%setup -q -n django_bootstrap3-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.app.settings
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m django test -v1 --noinput

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/bootstrap3
%{python_sitelib}/django_bootstrap3-%{version}*-info

%changelog
