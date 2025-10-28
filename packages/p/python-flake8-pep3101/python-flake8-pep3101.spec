#
# spec file for package python-flake8-pep3101
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-flake8-pep3101
Version:        3.0.0
Release:        0
Summary:        Checks for old string formatting
License:        GPL-2.0-only
URL:            https://github.com/gforcada/flake8-pep3101
Source:         https://files.pythonhosted.org/packages/source/f/flake8-pep3101/flake8_pep3101-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testfixtures}
# /SECTION
%python_subpackages

%description
Checks for old string formatting.

%prep
%autosetup -p1 -n flake8_pep3101-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest run_tests.py

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/flake8_pep3101.py
%pycache_only %{python_sitelib}/__pycache__/flake8_pep3101*pyc
%{python_sitelib}/flake8_pep3101-%{version}.dist-info

%changelog
