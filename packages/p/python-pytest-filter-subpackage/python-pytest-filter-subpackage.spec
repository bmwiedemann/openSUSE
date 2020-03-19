#
# spec file for package python-pytest-filter-subpackage
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
Name:           python-pytest-filter-subpackage
Version:        0.1.1
Release:        0
Summary:        Pytest plugin for filtering based on sub-packages
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-filter-subpackage
Source:         https://files.pythonhosted.org/packages/source/p/pytest-filter-subpackage/pytest-filter-subpackage-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module setuptools >= 30.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.0
BuildArch:      noarch
%python_subpackages

%description
This package contains a simple plugin for the `pytest`_ framework that provides a
shortcut to testing all code and documentation for a given sub-package.

%prep
%setup -q -n pytest-filter-subpackage-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
