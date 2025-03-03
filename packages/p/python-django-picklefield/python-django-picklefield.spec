#
# spec file for package python-django-picklefield
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
%define upstream_version 3.1
Name:           python-django-picklefield
Version:        3.1.0
Release:        0
Summary:        Pickled object field for Django
License:        MIT
URL:            https://github.com/gintas/django-picklefield
Source:         https://github.com/gintas/django-picklefield/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
BuildArch:      noarch
%python_subpackages

%description
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

The implementation is taken and adopted from Django snippet #1694
<http://www.djangosnippets.org/snippets/1694/> by Taavi Taijala, which is in
turn based on Django snippet #513 <http://www.djangosnippets.org/snippets/513/>
by Oliver Beattie.

%prep
%setup -q -n django-picklefield-%{version}
echo 'DEFAULT_AUTO_FIELD="django.db.models.AutoField"' >> tests/settings.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m django test -v2 --settings=tests.settings

%files %{python_files}
%doc README.rst
%{python_sitelib}/picklefield
%{python_sitelib}/django_picklefield-%{upstream_version}.dist-info

%changelog
