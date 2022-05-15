#
# spec file for package python-django-tagulous
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-django-tagulous
Version:        1.3.3
Release:        0
License:        BSD-3-Clause
Summary:        Fabulous Tagging for Django
Url:            http://radiac.net/projects/django-tagulous/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/django-tagulous/django-tagulous-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  fdupes
Requires:       python-Django
Suggests:       python-jasmine
Suggests:       python-psycopg2
Suggests:       python-mysqlclient
Suggests:       python-unidecode
BuildArch:      noarch

%python_subpackages

%description
Fabulous Tagging for Django.

%prep
%setup -q -n django-tagulous-%{version}
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*tagulous*/

%changelog
