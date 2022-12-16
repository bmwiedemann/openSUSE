#
# spec file for package python-flake8-builtins
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-flake8-builtins
Version:        2.0.1
Release:        0
Summary:        Flake8 Builtins plugin
License:        GPL-2.0-only
URL:            https://github.com/gforcada/flake8-builtins
Source:         https://files.pythonhosted.org/packages/source/f/flake8-builtins/flake8-builtins-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 6.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 6.0.0}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module hypothesmith}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This plugin checks for Python builtins being used as variables or parameters.

%prep
%setup -q -n flake8-builtins-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_builtin_works_on_many_examples - will crash in obs as it is speed related
%pytest run_tests.py -k 'not test_builtin_works_on_many_examples'

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
