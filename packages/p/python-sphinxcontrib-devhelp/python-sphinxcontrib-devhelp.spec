#
# spec file for package python-sphinxcontrib-devhelp
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
Name:           python-sphinxcontrib-devhelp%{psuffix}
Version:        1.0.6
Release:        0
Summary:        Sphinx extension which outputs Devhelp documents
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-doc/sphinxcontrib-devhelp
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib-devhelp/sphinxcontrib_devhelp-%{version}.tar.gz
Source99:       python-sphinxcontrib-devhelp.rpmlintrc
# PATCH-FIX-UPSTREAM no-store-btime-gzip.patch bsc#1227999 mcepl@suse.com
# don't store build time in gzip headers to make building documentation reproducible
Patch0:         no-store-btime-gzip.patch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-devhelp >= %{version}}
%endif
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%prep
%autosetup -p1 -n sphinxcontrib_devhelp-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if %{without test}
%files %{python_files}
%doc README.rst CHANGES
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib/devhelp
%{python_sitelib}/sphinxcontrib_devhelp-%{version}*-info
%endif

%changelog
