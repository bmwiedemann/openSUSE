#
# spec file for package python-poetry-core
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


%{?sle15_python_module_pythons}
Name:           python-poetry-core
Version:        1.5.2
Release:        0
Summary:        Python poetry core utilities
License:        Apache-2.0 AND BSD-2-Clause AND MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python-poetry/poetry-core
# Only the github archive provides the tests
Source:         %{url}/archive/%{version}.tar.gz#/poetry-core-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{python_version_nodots} < 38
Requires:       python-importlib-metadata >= 1.7.0
%endif
BuildArch:      noarch
# SECTION these are all test dependencies, including python-devel and git-core
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
A PEP 517 build backend implementation developed for Poetry. This project is
intended to be a light weight, fully compliant, self-contained package allowing
PEP 517 compatible build frontends to build Poetry managed projects.

%prep
%setup -q -n poetry-core-%{version}
mkdir vendoredlicenses
cp src/poetry/core/_vendor/attrs/LICENSE             vendoredlicenses/attrs.LICENSE
cp src/poetry/core/_vendor/jsonschema/COPYING        vendoredlicenses/jsonschema.COPYING
cp src/poetry/core/_vendor/lark/LICENSE              vendoredlicenses/lark.LICENSE
cp src/poetry/core/_vendor/packaging/LICENSE         vendoredlicenses/packaging.LICENSE
cp src/poetry/core/_vendor/packaging/LICENSE.APACHE  vendoredlicenses/packaging.LICENSE.APACHE
cp src/poetry/core/_vendor/packaging/LICENSE.BSD     vendoredlicenses/packaging.LICENSE.BSD
cp src/poetry/core/_vendor/pyrsistent/LICENSE.mit    vendoredlicenses/pyrsistent.LICENSE.mit
cp src/poetry/core/_vendor/tomlkit/LICENSE           vendoredlicenses/tomlkit.LICENSE
cp src/poetry/core/_vendor/typing_extensions.LICENSE vendoredlicenses/typing_extensions.LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#python-poetry/poetry#1645
git init
%pytest

%files %{python_files}
%doc README.md
%license LICENSE vendoredlicenses/*
%dir %{python_sitelib}/poetry
%{python_sitelib}/poetry/core
%{python_sitelib}/poetry_core-%{version}.dist-info

%changelog
