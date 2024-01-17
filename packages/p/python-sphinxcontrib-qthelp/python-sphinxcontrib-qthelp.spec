#
# spec file
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
Name:           python-sphinxcontrib-qthelp%{psuffix}
Version:        1.0.7
Release:        0
Summary:        Sphinx extension which outputs QtHelp
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-doc/sphinxcontrib-qthelp
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib_qthelp/sphinxcontrib_qthelp-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-qthelp >= %{version}}
%endif
%python_subpackages

%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.

%prep
%setup -q -n sphinxcontrib_qthelp-%{version}
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
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst CHANGES
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib/qthelp
%{python_sitelib}/sphinxcontrib_qthelp-%{version}*-info
%endif

%changelog
