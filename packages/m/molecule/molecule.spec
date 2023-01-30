#
# spec file for package molecule
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


# Disable tests on Leap due to missing build dependencies.
%if 0%{?suse_version} > 1500
%bcond_without test
%else
%bcond_with test
%endif

%define pythons python3
Name:           molecule
Version:        4.0.4
Release:        0
Summary:        Aids in the development and testing of Ansible roles
License:        MIT
URL:            https://github.com/ansible-community/molecule
Source:         https://files.pythonhosted.org/packages/source/m/molecule/molecule-%{version}.tar.gz
Patch0:         skip-broken-test.patch
BuildRequires:  python3-pip
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
%if %{with test}
BuildRequires:  ansible-lint
BuildRequires:  python3-ansi2html
BuildRequires:  python3-coverage
BuildRequires:  python3-filelock
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-html
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-plus
BuildRequires:  python3-pytest-testinfra
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-yamllint
# Runtime dependencies of molecule
BuildRequires:  ansible
BuildRequires:  python3
BuildRequires:  python3-Jinja2 >= 2.11.3
BuildRequires:  python3-PyYAML >= 5.1
BuildRequires:  python3-ansible-compat >= 2.2.0
BuildRequires:  python3-click >= 8.0
BuildRequires:  python3-click-help-colors >= 0.9
BuildRequires:  python3-cookiecutter >= 1.7.3
BuildRequires:  python3-enrich >= 1.2.7
BuildRequires:  python3-jsonschema >= 4.9.1
BuildRequires:  python3-packaging
BuildRequires:  python3-pluggy >= 0.7.1
BuildRequires:  python3-rich >= 9.5.1
%endif
BuildRequires:  fdupes
Requires:       ansible
Requires:       python3
Requires:       python3-Jinja2 >= 2.11.3
Requires:       python3-PyYAML >= 5.1
Requires:       python3-ansible-compat >= 2.2.0
Requires:       python3-click >= 8.0
Requires:       python3-click-help-colors >= 0.9
Requires:       python3-cookiecutter >= 1.7.3
Requires:       python3-enrich >= 1.2.7
Requires:       python3-jsonschema >= 4.9.1
Requires:       python3-packaging
Requires:       python3-pluggy >= 0.7.1
Requires:       python3-rich >= 9.5.1
BuildArch:      noarch

%description
Molecule project is designed to aid in the development and testing of
Ansible roles.

Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios.

%prep
%setup -q -n molecule-%{version}

%patch0 -p1

%build
# On Leap < 15.4, setuptools is too old to support omitting setup.py.
%if 0%{?sle_version} < 150400
echo 'from setuptools import setup; setup()' > setup.py
%endif
%pyproject_wheel

%install
%pyproject_install

sed -i '1{\@^#!/usr/bin/env ansible-playbook@d}' %{buildroot}%{python3_sitelib}/molecule/data/validate-dockerfile.yml
sed -i '1{\@^#!/usr/bin/python@d}' %{buildroot}%{python3_sitelib}/molecule/test/scenarios/verifier/molecule/testinfra-pre-commit/tests/test_testinfra_pre_commit.py

%fdupes %{buildroot}%{python3_sitelib}

%check
%if %{with test}
export PATH="%{buildroot}%{_bindir}:$PATH"
%pytest -k 'not (test_command_dependency or test_sample_collection)' -W ignore:'There is no current event loop'
%endif

%files
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/molecule

%changelog
