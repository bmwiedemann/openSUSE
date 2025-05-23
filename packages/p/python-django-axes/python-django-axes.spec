#
# spec file for package python-django-axes
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
Name:           python-django-axes
Version:        7.0.2
Release:        0
License:        MIT
Summary:        Keep track of failed login attempts in Django-powered sites
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-axes
Source:         https://files.pythonhosted.org/packages/source/d/django-axes/django_axes-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module asgiref >= 3.6.0}
BuildRequires:  %{python_module django-ipware >= 3}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module tzdata}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 4.2
Requires:       python-asgiref >= 3.6.0
Suggests:       python-django-ipware >= 3
BuildArch:      noarch

%python_subpackages

%description
Keep track of failed login attempts in Django-powered sites.

%prep
%setup -q -n django_axes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
rm pyproject.toml
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/axes/
%{python_sitelib}/django[_-]axes*/

%changelog
