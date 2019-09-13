#
# spec file for package python-django-formtools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-formtools
Version:        2.1
Release:        0
Summary:        A set of high-level abstractions for Django forms
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django/django-formtools
Source:         https://files.pythonhosted.org/packages/source/d/django-formtools/django-formtools-%{version}.tar.gz
Patch0:         django-21.patch
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-pysqlite
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
BuildArch:      noarch
%python_subpackages

%description
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%prep
%setup -q -n django-formtools-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=`pwd`
%python_expand %{_bindir}/django-admin.py-%{$python_bin_suffix} test tests --pythonpath=`pwd` 

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python_sitelib}/*

%changelog
