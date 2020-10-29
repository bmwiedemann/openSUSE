#
# spec file for package python-jaraco.functools
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
Name:           python-jaraco.functools
Version:        3.0.1
Release:        0
Summary:        Tools to work with functools
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.functools
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.functools/jaraco.functools-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.base >= 6.1}
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.base >= 6.1
Requires:       python-more-itertools
BuildArch:      noarch
%python_subpackages

%description
jaraco.functools Tools for working with functools.
Additional functools in the spirit of stdlib’s functools.

%prep
%setup -q -n jaraco.functools-%{version}
sed -i 's/--flake8//' pytest.ini
sed -i 's/--black --cov//' pytest.ini
rm -rf jaraco.functools.egg-info

%build
%python_build

%install
%python_install

%python_expand rm %{buildroot}%{$python_sitelib}/jaraco/__init__.py

%py3_compile %{buildroot}%{python3_sitelib}/jaraco/
%py3_compile -O %{buildroot}%{python3_sitelib}/jaraco/

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_function_throttled - can randomly fail
%pytest -k 'not test_function_throttled'

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.functools-%{version}-py*.egg-info
%{python_sitelib}/jaraco/functools.py*
%pycache_only %{python_sitelib}/jaraco/__pycache__/functools*.py*

%changelog
