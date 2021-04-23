#
# spec file for package python-django-mathfilters
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-django-mathfilters
Version:        1.0.0
Release:        0
Summary:        Django math filters
License:        MIT
URL:            https://github.com/dbrgn/django-mathfilters
Source:         https://files.pythonhosted.org/packages/source/d/django-mathfilters/django-mathfilters-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
A set of math filters for Django.

%prep
%setup -q -n django-mathfilters-%{version}
mv mathfilters/tests.py .
sed -i 's/from .templatetags/from mathfilters.templatetags/' tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
