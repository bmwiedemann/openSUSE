#
# spec file for package python-django-contrib-comments
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
Name:           python-django-contrib-comments
Version:        2.2.0
Release:        0
Summary:        Framework for attaching comments to Django models
License:        BSD-3-Clause
URL:            https://github.com/django/django-contrib-comments
Source:         https://files.pythonhosted.org/packages/source/d/django-contrib-comments/django-contrib-comments-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django4 >= 2.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django4 >= 2.2}
# /SECTION
%python_subpackages

%description
This framework can be used to attach comments to any model, so you can use
it for comments on blog entries, photos, book chapters, or anything else.

This is the same framework that was removed from Django 1.6.

%prep
%autosetup -p1 -n django-contrib-comments-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec tests/runtests.py

%files %{python_files}
%doc README.rst HISTORY.rst
%license LICENSE.txt
%{python_sitelib}/django_comments
%{python_sitelib}/django_contrib_comments-%{version}.dist-info

%changelog
