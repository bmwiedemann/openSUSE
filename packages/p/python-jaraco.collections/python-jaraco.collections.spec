#
# spec file for package python-jaraco.collections
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
Name:           python-jaraco.collections
Version:        3.0.0
Release:        0
Summary:        Tools to work with collections
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.collections
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.collections/jaraco.collections-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.base >= 6.1}
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module jaraco.functools}
BuildRequires:  %{python_module jaraco.text}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.base >= 6.1
Requires:       python-jaraco.classes
Requires:       python-jaraco.functools
Requires:       python-jaraco.text
BuildArch:      noarch
%python_subpackages

%description
jaraco.collections Tools for working with collections.
Models and classes to supplement the stdlib ‘collections’ module.

%prep
%setup -q -n jaraco.collections-%{version}
sed -i 's/--flake8 --black --cov//' pytest.ini

%build
%python_build

%install
%python_install

%python_expand rm %{buildroot}%{$python_sitelib}/jaraco/__init__.py

%{?python_compileall}
%{!?python_compileall: # if we haven no python_compileall we are for sure still without multiple python3 flavors.
%py3_compile %{buildroot}%{python3_sitelib}/jaraco/
%py3_compile -O %{buildroot}%{python3_sitelib}/jaraco/
}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.collections-%{version}-py*.egg-info
%{python_sitelib}/jaraco/collections.py*
%pycache_only %{python_sitelib}/jaraco/__pycache__/collections*.py*

%changelog
