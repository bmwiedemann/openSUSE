#
# spec file for package python-pytest-bdd
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
%bcond_without python2
Name:           python-pytest-bdd
Version:        4.0.1
Release:        0
Summary:        BDD for pytest
License:        MIT
URL:            https://github.com/pytest-dev/pytest-bdd
Source:         https://github.com/pytest-dev/pytest-bdd/archive/%{version}.tar.gz#/pytest-bdd-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Mako
Requires:       python-glob2
Requires:       python-parse
Requires:       python-parse_type
Requires:       python-py
Requires:       python-pytest >= 4.3.0
Requires:       python-six >= 1.9.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module execnet}
BuildRequires:  %{python_module glob2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module parse_type}
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module pytest >= 4.3.0}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module six >= 1.9.0}
%python_subpackages

%description
BDD library for the py.test runner

pytest-bdd implements a subset of Gherkin language for the automation of the project
requirements testing and easier behavioral driven development.

Unlike many other BDD tools it doesn't require a separate runner and benefits from
the power and flexibility of the pytest. It allows to unify your unit and functional
tests, easier continuous integration server configuration and maximal reuse of the
tests setup.

Pytest fixtures written for the unit tests can be reused for the setup and actions
mentioned in the feature steps with dependency injection, which allows a true BDD
just-enough specification of the requirements without maintaining any context object
containing the side effects of the Gherkin imperative declarations.

%prep
%setup -q -n pytest-bdd-%{version}
sed -i '/tox/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pytest-bdd

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
# test_generate_with_quotes and test_unicode_characters require ptyest-bdd binary which we handle with u-a
%pytest -k 'not test_generate_with_quotes and not test_unicode_characters'

%post
%python_install_alternative pytest-bdd

%postun
%python_uninstall_alternative pytest-bdd

%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/pytest-bdd
%{python_sitelib}/*

%changelog
