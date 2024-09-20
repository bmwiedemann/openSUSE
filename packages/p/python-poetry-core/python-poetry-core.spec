#
# spec file for package python-poetry-core
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


%{?sle15_python_module_pythons}
Name:           python-poetry-core
Version:        1.9.0
Release:        0
Summary:        Poetry PEP 517 Build Backend
License:        Apache-2.0 AND BSD-2-Clause AND MIT AND Python-2.0
URL:            https://github.com/python-poetry/poetry-core
# Only the github archive provides the tests
Source:         %{url}/archive/%{version}.tar.gz#/poetry-core-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM gh#python-poetry/poetry-core#758
Patch0:         support-newer-pythons.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION these are all test dependencies, including python-devel and git-core
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli-w}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
A PEP 517 build backend implementation developed for Poetry. This project is
intended to be a light weight, fully compliant, self-contained package allowing
PEP 517 compatible build frontends to build Poetry managed projects.

%prep
%autosetup -p1 -n poetry-core-%{version}
mkdir vendoredlicenses
cp -p src/poetry/core/_vendor/lark/LICENSE              vendoredlicenses/lark.LICENSE
cp -p src/poetry/core/_vendor/fastjsonschema/LICENSE    vendoredlicenses/fastjsonschema.LICENSE
cp -p src/poetry/core/_vendor/packaging/LICENSE         vendoredlicenses/packaging.LICENSE
cp -p src/poetry/core/_vendor/packaging/LICENSE.APACHE  vendoredlicenses/packaging.LICENSE.APACHE
cp -p src/poetry/core/_vendor/packaging/LICENSE.BSD     vendoredlicenses/packaging.LICENSE.BSD
cp -p src/poetry/core/_vendor/tomli/LICENSE             vendoredlicenses/tomli.LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#python-poetry/poetry#1645
git init
#https://github.com/python-poetry/poetry/issues/9678
donttest="obsdummyprefix"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE vendoredlicenses/*
%dir %{python_sitelib}/poetry
%{python_sitelib}/poetry/core
%{python_sitelib}/poetry_core-%{version}.dist-info

%changelog
