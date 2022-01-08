#
# spec file for package python-django-debreach
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python36 1
Name:           python-django-debreach
Version:        2.1.0
Release:        0
Summary:        Middleware to protect against the BREACH attack in Django
License:        BSD-2-Clause
URL:            https://github.com/lpomfrey/django-debreach
Source:         https://files.pythonhosted.org/packages/source/d/django-debreach/django-debreach-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Adds middleware and context processors to give some protection against the BREACH attack in Django.

%prep
%setup -q -n django-debreach-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=`pwd`
export DJANGO_SETTINGS_MODULE='test_project.settings'
%python_expand $python -m django test debreach -v2 --pythonpath=`pwd`

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
