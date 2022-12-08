#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-ttp%{psuffix}
Version:        0.9.2
Release:        0
Summary:        Template Text Parser
License:        MIT
URL:            https://github.com/dmulyalin/ttp
Source:         https://github.com/dmulyalin/ttp/archive/refs/tags/%{version}.tar.gz#/ttp-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-tests.patch gh#dmulyalin/ttp#90
Patch0:         fix-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module deepdiff}
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module ttp = %{version}}
BuildRequires:  %{python_module ttp-templates}
%endif
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
TTP is a Python library for semi-structured text parsing using templates.

%prep
%autosetup -p1 -n ttp-%{version}
rm ttp/utils/load_python_exec_py2.py

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ttp
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
pushd test/pytest
# No python-yangson
donttest="yangson"
%pytest . -k "not ($donttest)"
popd
%endif

%post
%python_install_alternative ttp

%postun
%python_uninstall_alternative ttp

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/ttp
%{python_sitelib}/*
%endif

%changelog
