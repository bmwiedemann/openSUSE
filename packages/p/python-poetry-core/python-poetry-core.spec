#
# spec file for package python-poetry-core
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


Name:           python-poetry-core
Version:        1.4.0
Release:        0
Summary:        Python poetry core utilities
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-poetry/poetry-core
# Only the github archive provides the tests
Source:         %{url}/archive/%{version}.tar.gz#/poetry-core-%{version}-gh.tar.gz
BuildRequires:  %{python_module attrs >= 22.1.0}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jsonschema >= 4.1.0}
BuildRequires:  %{python_module lark >= 1.1.2}
BuildRequires:  %{python_module packaging >= 21.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing >= 3.0.9}
BuildRequires:  %{python_module pyrsistent >= 0.18.1}
BuildRequires:  %{python_module tomlkit >= 0.11.3}
BuildRequires:  %{python_module typing-extensions >= 4.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 22.1.0
Requires:       python-jsonschema >= 4.1.0
Requires:       python-lark >= 1.1.2
Requires:       python-packaging >= 21.3
Requires:       python-pyparsing >= 3.0.9
Requires:       python-pyrsistent >= 0.18.1
Requires:       python-tomlkit >= 0.11.3
Requires:       python-typing-extensions >= 4.3.0
BuildArch:      noarch
# SECTION these are all test dependencies, including devel and git
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
# unbundle: we provide the vendored packages on our own
rm -r src/poetry/core/_vendor

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
