#
# spec file for package python-pytest-filter-subpackage
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pytest-filter-subpackage
Version:        0.1.2
Release:        0
Summary:        Pytest plugin for filtering based on sub-packages
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-filter-subpackage
Source:         https://files.pythonhosted.org/packages/source/p/pytest-filter-subpackage/pytest-filter-subpackage-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.0}
# Patch0 is for the change from doctestplus 0.5 to 0.6
BuildRequires:  %{python_module pytest-doctestplus >= 0.6}
BuildRequires:  %{python_module setuptools >= 30.3}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.0
BuildArch:      noarch
%python_subpackages

%description
This package contains a simple plugin for the pytest framework that provides a
shortcut to testing all code and documentation for a given sub-package.

%prep
%autosetup -p1 -n pytest-filter-subpackage-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# don't error on obs resource warnings
sed -i '/^\s*error/ a \    ignore::ResourceWarning' setup.cfg
%pytest

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE.rst
%{python_sitelib}/pytest_filter_subpackage
%{python_sitelib}/pytest_filter_subpackage-%{version}*-info

%changelog
