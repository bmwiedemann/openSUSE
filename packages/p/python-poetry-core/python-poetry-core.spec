#
# spec file for package python-poetry-core
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-poetry-core
Version:        1.0.0
Release:        0
Summary:        Python poetry core utilities
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-poetry/poetry-core
# Only the github archive provides the tests
Source:         https://github.com/python-poetry/poetry-core/archive/%{version}.tar.gz#/poetry-core-%{version}-gh.tar.gz
BuildRequires:  %{python_module attrs >= 19.3.0}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module lark-parser >= 0.9.0}
BuildRequires:  %{python_module packaging >= 20.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing >= 2.4.7}
BuildRequires:  %{python_module pyrsistent >= 0.16.0}
BuildRequires:  %{python_module six >= 1.15.0}
BuildRequires:  %{python_module tomlkit >= 0.7.0}
BuildRequires:  %{python_module typing >= 3.7.4}
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.3.0
Requires:       python-jsonschema >= 3.2.0
Requires:       python-lark-parser >= 0.9.0
Requires:       python-packaging >= 20.4
Requires:       python-pyparsing >= 2.4.7
Requires:       python-pyrsistent >= 0.16.0
Requires:       python-six >= 1.15.0
Requires:       python-tomlkit >= 0.7.0
Requires:       python-typing >= 3.7.4
BuildArch:      noarch
# SECTION these are all test dependencies, including devel and git
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pep517}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
A PEP 517 build backend implementation developed for Poetry. This project is
intended to be a light weight, fully compliant, self-contained package allowing
PEP 517 compatible build frontends to build Poetry managed projects.

%prep
%setup -q -n poetry-core-%{version}
# python-poetry will provide this file
rm poetry/__init__.py
# unbundle: we provide the vendored packages on our own
rm -r poetry/core/_vendor
# remove executable bits
find poetry/core -name '*.py' -executable -print0 | xargs -0 chmod a-x

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
%license LICENSE
%dir %{python_sitelib}/poetry
%{python_sitelib}/poetry/core
%{python_sitelib}/poetry_core-%{version}.dist-info

%changelog
