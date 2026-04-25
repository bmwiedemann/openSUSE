#
# spec file for package python-sphinxcontrib-htmlhelp
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
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-htmlhelp%{psuffix}
Version:        2.1.0
Release:        0
Summary:        Sphinx extension to generate HTML help files
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-htmlhelp
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_htmlhelp/sphinxcontrib_htmlhelp-%{version}.tar.gz
Source99:       python-sphinxcontrib-htmlhelp.rpmlintrc
# PATCH-FIX-UPSTREAM gh#sphinx-doc/sphinxcontrib-htmlhelp#44
Patch0:         support-sphinx-9.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 5.0}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-htmlhelp >= %{version}}
%endif
%python_subpackages

%description
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.

%prep
%autosetup -p1 -n sphinxcontrib_htmlhelp-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENCE.rst
%dir %{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib/htmlhelp
%{python_sitelib}/sphinxcontrib_htmlhelp-%{version}.dist-info
%endif

%changelog
