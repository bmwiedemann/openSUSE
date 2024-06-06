#
# spec file for package python-jaraco.functools
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
Name:           python-jaraco.functools
Version:        4.0.1
Release:        0
Summary:        Tools to work with functools
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.functools
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.functools/jaraco_functools-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-more-itertools
BuildArch:      noarch
# SECTION test and docs
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rst.linker >= 1.9}
# /SECTION
%python_subpackages

%description
jaraco.functools Tools for working with functools.
Additional functools in the spirit of stdlib’s functools.

%prep
%setup -q -n jaraco_functools-%{version}
sed -i 's/--flake8//' pytest.ini
sed -i 's/--black --cov//' pytest.ini
rm -rf jaraco.functools.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_function_throttled - can randomly fail
%pytest -k 'not test_function_throttled'

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst NEWS.rst
%{python_sitelib}/jaraco/functools
%{python_sitelib}/jaraco.functools-%{version}.dist-info

%changelog
