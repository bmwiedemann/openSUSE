#
# spec file for package python-django-contrib-comments
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-contrib-comments
Version:        1.9.1
Release:        0
License:        BSD-3-Clause
Summary:        Framework for attaching comments to Django models	
Url:            https://github.com/django/django-contrib-comments
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/django-contrib-comments/django-contrib-comments-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 1.11
BuildArch:      noarch

%python_subpackages

%description
This framework can be used to attach comments to any model, so you can use
it for comments on blog entries, photos, book chapters, or anything else.

This is the same framework that was removed from Django 1.6.

%prep
%setup -q -n django-contrib-comments-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst HISTORY.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
