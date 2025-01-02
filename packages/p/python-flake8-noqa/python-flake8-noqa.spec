#
# spec file for package python-flake8-noqa
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
Name:           python-flake8-noqa
Version:        1.4.0
Release:        0
Summary:        Flake8 noqa comment validation
License:        LGPL-3.0-only
URL:            https://github.com/plinss/flake8-noqa
Source:         https://files.pythonhosted.org/packages/source/f/flake8-noqa/flake8-noqa-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 3.8.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4.2}
BuildRequires:  %{python_module flake8-docstrings}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-flake8 >= 3.8.0
Requires:       python-typing_extensions >= 3.7.4.2
Suggests:       python-mypy
Suggests:       python-flake8 >= 3.8.0
Suggests:       python-flake8-annotations
Suggests:       python-flake8-bandit
Suggests:       python-flake8-bugbear
Suggests:       python-flake8-commas
Suggests:       python-flake8-comprehensions
Suggests:       python-flake8-continuation
Suggests:       python-flake8-datetimez
Suggests:       python-flake8-docstrings
Suggests:       python-flake8-import-order
Suggests:       python-flake8-literal
Suggests:       python-flake8-noqa
Suggests:       python-flake8-polyfill
Suggests:       python-flake8-pyproject
Suggests:       python-flake8-modern-annotations
Suggests:       python-flake8-requirements
Suggests:       python-flake8-typechecking-import
Suggests:       python-flake8-use-fstring
Suggests:       python-pep8-naming
BuildArch:      noarch
%python_subpackages

%description
Flake8 noqa comment validation

%prep
%autosetup -p1 -n flake8-noqa-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v test.py

%files %{python_files}
%doc README.md
%license COPYING.LESSER LICENSE
%{python_sitelib}/flake8_noqa
%{python_sitelib}/flake8_noqa-%{version}.dist-info

%changelog
