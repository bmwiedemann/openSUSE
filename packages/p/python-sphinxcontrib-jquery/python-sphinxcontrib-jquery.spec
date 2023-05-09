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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-jquery%{psuffix}
Version:        4.1
Release:        0
Summary:        Extension to include jQuery on newer Sphinx releases
License:        0BSD
URL:            https://github.com/sphinx-contrib/jquery/
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-jquery/sphinxcontrib-jquery-4.1.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 1.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-jquery = %{version}}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx >= 1.8
BuildArch:      noarch
%python_subpackages

%description
Extension to include jQuery on newer Sphinx releases

%prep
%autosetup -p1 -n sphinxcontrib-jquery-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%dir %{python_sitelib}/sphinxcontrib
%dir %{python_sitelib}/sphinxcontrib/jquery
%{python_sitelib}/sphinxcontrib/jquery/*
%{python_sitelib}/sphinxcontrib_jquery-%{version}*info
%endif

%changelog
