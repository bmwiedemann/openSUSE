#
# spec file for package python-sphinxcontrib-applehelp
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-applehelp%{psuffix}
Version:        2.0.0
Release:        0
Summary:        Sphinx extension which outputs Apple help books
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-doc/sphinxcontrib-applehelp
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib_applehelp/sphinxcontrib_applehelp-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-applehelp >= %{version}}
%endif
%python_subpackages

%description
sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books

%prep
%setup -q -n sphinxcontrib_applehelp-%{version}

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
%{python_sitelib}/sphinxcontrib/applehelp
%{python_sitelib}/sphinxcontrib_applehelp-%{version}*-info
%endif

%changelog
