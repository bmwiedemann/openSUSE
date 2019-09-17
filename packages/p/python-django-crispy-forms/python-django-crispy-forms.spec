#
# spec file for package python-django-crispy-forms
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
%define mod_name django-crispy-forms
Name:           python-%{mod_name}
Version:        1.7.2
Release:        0
Summary:        Django DRY Forms
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/maraujop/django-crispy-forms
Source:         https://files.pythonhosted.org/packages/source/d/%{mod_name}/%{mod_name}-%{version}.tar.gz
Patch0:         django-20.patch
Patch1:         django-21.patch
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest < 4.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
A module to build programmatic reusable layouts out of components
with control over the rendered HTML without writing HTML in
templates, and without breaking the standard way of doing things in
Django.

%prep
%setup -q -n %{mod_name}-%{version}
%autopatch -p1

# Remove not needed files
find . -name '*.pyc' -delete

%build
%python_build

%check
%python_expand PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=crispy_forms.tests.test_settings py.test-%{$python_version} crispy_forms/tests

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.txt README.rst
%{python_sitelib}/*

%changelog
