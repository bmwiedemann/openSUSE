#
# spec file for package python-pytest-sphinx
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


Name:           python-pytest-sphinx
Version:        0.6.3
Release:        0
Summary:        Doctest plugin for pytest with support for Sphinx-specific doctest-directives
License:        BSD-3-Clause
URL:            https://github.com/thisch/pytest-sphinx
Source:         https://github.com/thisch/pytest-sphinx/archive/v%{version}.tar.gz#/pytest-sphinx-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 8.1.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest >= 8.1.1}
# /SECTION
%python_subpackages

%description
Doctest plugin for pytest with support for Sphinx-specific doctest-directives.

%prep
%setup -q -n pytest-sphinx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_sphinx.py
%{python_sitelib}/pytest_sphinx-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/pytest_sphinx*pyc

%changelog
