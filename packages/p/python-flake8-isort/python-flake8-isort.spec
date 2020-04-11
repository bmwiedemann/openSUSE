#
# spec file for package python-flake8-isort
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
Name:           python-flake8-isort
Version:        2.9.1
Release:        0
Summary:        Plugin integrating isort in flake8
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/gforcada/flake8-isort
Source:         https://files.pythonhosted.org/packages/source/f/flake8-isort/flake8-isort-%{version}.tar.gz
BuildRequires:  %{python_module flake8 >= 3.2.1}
BuildRequires:  %{python_module isort >= 4.3.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 3.2.1
Requires:       python-isort >= 4.3.5
Requires:       python-testfixtures
BuildArch:      noarch
%python_subpackages

%description
Use `isort`_ to check if the imports on your python files are sorted the way you expect.

%prep
%setup -q -n flake8-isort-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the three skipped tests need to have the extension registered in the flake8 -> same sitelib
%pytest run_tests.py -k 'not (test_config_file or test_default_option or test_isort_uses_pyproject)'

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE*
%{python_sitelib}/*

%changelog
