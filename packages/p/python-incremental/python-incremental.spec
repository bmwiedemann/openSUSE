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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-incremental%{psuffix}
Version:        22.10.0
Release:        0
Summary:        Library that versions your Python projects
License:        MIT
URL:            https://github.com/twisted/incremental
Source:         https://files.pythonhosted.org/packages/source/i/incremental/incremental-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Twisted >= 16.4.0
Suggests:       python-click >= 6.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Twisted >= 16.4.0}
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Incremental is a small library that versions your Python projects.

%prep
%setup -q -n incremental-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# test_prereleaseAttributeDeprecated - same as bellow
# test_prereleaseDeprecated - uses deprecated pytest behaviour removed with pytest 5.4
%pytest -k 'not test_prereleaseAttributeDeprecated and not test_prereleaseDeprecated'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%{python_sitelib}/*
%endif

%changelog
