#
# spec file for package python-flake8-builtins
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
Name:           python-flake8-builtins
Version:        1.4.1
Release:        0
License:        GPL-2.0-only
Summary:        Flake8 Builtins plugin
Url:            https://github.com/gforcada/flake8-builtins
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/flake8-builtins/flake8-builtins-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-flake8
Suggests:       python-coverage
Suggests:       python-coveralls
Suggests:       python-mock
Suggests:       python-pytest
Suggests:       python-pytest-cov
BuildArch:      noarch

%python_subpackages

%description
Check for python builtins being used as variables or parameters

%prep
%setup -q -n flake8-builtins-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest run_tests.py

%files %{python_files}
%license LICENSE LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
