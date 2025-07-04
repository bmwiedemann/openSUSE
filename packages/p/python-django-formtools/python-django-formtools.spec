#
# spec file for package python-django-formtools
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
Name:           python-django-formtools
Version:        2.4.1
Release:        0
Summary:        A set of high-level abstractions for Django forms
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-formtools
Source:         https://files.pythonhosted.org/packages/source/d/django-formtools/django-formtools-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%prep
%setup -q -n django-formtools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=`pwd`
%python_expand $python -m django test -v 2 tests --pythonpath=`pwd`

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python_sitelib}/formtools
%{python_sitelib}/django_formtools-%{version}.dist-info

%changelog
