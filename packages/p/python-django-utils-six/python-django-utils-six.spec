#
# spec file for package python-django-utils-six
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-django-utils-six
Version:        2.0
Release:        0
Summary:        Forward compatibility django.utils.six for Django 3
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/whtsky/django-utils-six
Source:         https://files.pythonhosted.org/packages/source/d/django-utils-six/django-utils-six-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-Django >= 3
%python_subpackages

%description
Forward compatibility django.utils.six for Django 3.

%prep
%setup -q -n django-utils-six-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
