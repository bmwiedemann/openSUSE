#
# spec file for package python-sphinxcontrib-jsmath
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%global flavor @BUILD_FLAVOR@%{nil}
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
URL:            http://sphinx-doc.org/
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-jsmath/sphinxcontrib-jsmath-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#sphinx-doc/sphinxcontrib-jsmath#3297b27177ab4862d1b2408a2db66235397fe212 Fix #9361: RemovedInSphinx50Warning on testing
Patch0:         sphinx5.patch
# PATCH-FIX-UPSTREAM Based on gh#sphinx-doc/sphinxcontrib-jsmath#98f7b308148f3670b0c1bd45c0a9a62e781d782b
Patch1:         do-not-use-sphinx-testing.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# test_disabled_when_equations_not_found fails with Sphinx 8.2 - https://github.com/sphinx-doc/sphinx/issues/13442
%pytest -k "not test_disabled_when_equations_not_found"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst CHANGES
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib/jsmath
%{python_sitelib}/sphinxcontrib_jsmath-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_jsmath-%{version}.dist-info
%endif

%changelog
