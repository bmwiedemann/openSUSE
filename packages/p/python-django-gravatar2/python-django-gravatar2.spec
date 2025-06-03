#
# spec file for package python-django-gravatar2
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
Name:           python-django-gravatar2
Version:        1.4.4
Release:        0
Summary:        Gravatar Support for Django
License:        MIT
URL:            https://github.com/twaddington/django-gravatar
Source:         https://files.pythonhosted.org/packages/source/d/django-gravatar2/django-gravatar2-%{version}.tar.gz
# skip test which wants to read from https://secure.gravatar.com/avatar/
Patch1:         python-django-gravatar2-skip-online-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
# needs sqlite3 module
BuildRequires:  %{pythons}
# /SECTION
%python_subpackages

%description
Essential Gravatar support for Django. Features helper methods, templatetags and a full test suite!

%prep
%autosetup -p1 -n django-gravatar2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd example_project
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python manage.py test --verbosity=2 django_gravatar
popd

%files %{python_files}
%doc README README.rst
%license LICENSE
%{python_sitelib}/django_gravatar
%{python_sitelib}/django_gravatar2-%{version}.dist-info

%changelog
