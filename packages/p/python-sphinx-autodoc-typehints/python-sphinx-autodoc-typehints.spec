#
# spec file for package python-sphinx-autodoc-typehints
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-sphinx-autodoc-typehints
Version:        1.11.0
Release:        0
Summary:        Type hints (PEP 484) support for the Sphinx autodoc extension
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/agronholm/sphinx-autodoc-typehints
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-autodoc-typehints/sphinx-autodoc-typehints-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-sphinx-autodoc-typehints-system-object.inv.patch gh#agronholm/sphinx-autodoc-typehints#174 mcepl@suse.com
# skip network tests
Patch0:         python-sphinx-autodoc-typehints-system-object.inv.patch
BuildRequires:  %{python_module setuptools >= 36.2.7}
BuildRequires:  %{python_module setuptools_scm >= 1.7.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.7
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module Sphinx >= 1.7}
BuildRequires:  %{python_module doc}
BuildRequires:  %{python_module pathlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphobjinv}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
This is a Sphinx extension which allows to use Python 3 annotations for documenting acceptable argument types
and return value types of functions.

%prep
%autosetup -p1 -n sphinx-autodoc-typehints-%{version}

%build
%python_build
%python_expand sed -i -e 's/@PYTHON_VERSION@/%{$python_version}/' tests/conftest.py

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_sphinx_output -- too depenedent on sphinx version available
%pytest -k 'not test_sphinx_output'

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc README.rst CHANGELOG.rst

%changelog
