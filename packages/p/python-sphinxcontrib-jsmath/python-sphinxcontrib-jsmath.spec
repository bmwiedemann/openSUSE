#
# spec file
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-jsmath%{?psuffix}
Version:        1.0.1
Release:        0
Summary:        Sphinx extension which renders display math in HTML via JavaScript
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://sphinx-doc.org/
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-jsmath/sphinxcontrib-jsmath-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/sphinx-doc/sphinxcontrib-jsmath/commit/3297b27177ab4862d1b2408a2db66235397fe212 Fix #9361: RemovedInSphinx50Warning on testing
Patch0:         sphinx5.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-jsmath >= %{version}}
%endif
%python_subpackages

%description
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.

%prep
%setup -q -n sphinxcontrib-jsmath-%{version}
%autopatch -p1

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst CHANGES
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
