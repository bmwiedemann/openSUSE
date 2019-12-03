#
# spec file for package python-django-gravatar2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-django-gravatar2
Version:        1.4.2
Release:        0
Summary:        Gravatar Support for Django
License:        MIT
URL:            https://github.com/twaddington/django-gravatar
Source:         https://github.com/twaddington/django-gravatar/archive/1.4.2.tar.gz
# https://github.com/twaddington/django-gravatar/issues/30
Patch0:         python-django-gravatar2-fix-testsuite.patch
# skip test which wants to read from https://secure.gravatar.com/avatar/
Patch1:         python-django-gravatar2-skip-online-test.patch
BuildRequires:  %{python_module setuptools}
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
%setup -q -n django-gravatar-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd example_project
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python manage.py test --verbosity=2 django_gravatar
popd

%files %{python_files}
%doc README README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
