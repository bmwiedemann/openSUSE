#
# spec file for package python-django-bootstrap3
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
%define skip_python2 1
Name:           python-django-bootstrap3
Version:        14.1.0
Release:        0
Summary:        Bootstrap support for Django projects
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/dyve/django-bootstrap3
Source:         https://github.com/zostera/django-bootstrap3/archive/v%{version}.tar.gz#/django-bootstrap3-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-dephell-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Bootstrap support for Django projects.

%prep
%setup -q -n django-bootstrap3-%{version}

# Remove django dependency specification which breaks dephell
sed -i '/django.*||/d' pyproject.toml
# Prevent PyPI fetches of doc deps during dephell conversion
sed -i '/sphinx/d;/m2r/d' pyproject.toml

%dephell_gensetup

mv example/ src/
touch src/example/__init__.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/example/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export DJANGO_SETTINGS_MODULE=tests.app.settings
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m django test -v1 --noinput

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
