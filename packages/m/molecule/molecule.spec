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


%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1550
# Leap15, SLES15
%if %pythons == "python310"
%define ansible_python python310
%define ansible_python_executable python3.10
%define ansible_python_sitelib %python310_sitelib
%endif
%if %pythons == "python311"
%define ansible_python python311
%define ansible_python_executable python3.11
%define ansible_python_sitelib %python311_sitelib
%endif
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_executable python3
%define ansible_python_sitelib %python3_sitelib
%endif

%bcond_without test
Name:           molecule
Version:        24.6.0
Release:        0
Summary:        Aids in the development and testing of Ansible roles
License:        MIT
URL:            https://github.com/ansible-community/molecule
Source:         https://files.pythonhosted.org/packages/source/m/molecule/molecule-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{ansible_python}-base >= 3.10
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-wheel
%if %{with test}
BuildRequires:  ansible-lint >= 6.12.1
BuildRequires:  %{ansible_python}-ansi2html >= 1.8.0
BuildRequires:  %{ansible_python}-coverage >= 7.0.3
BuildRequires:  %{ansible_python}-filelock >= 3.9.0
BuildRequires:  %{ansible_python}-pexpect >= 4.8.0
BuildRequires:  %{ansible_python}-pytest >= 7.2.0
BuildRequires:  %{ansible_python}-pytest-mock >= 3.10.0
BuildRequires:  %{ansible_python}-pytest-plus >= 0.4.0
BuildRequires:  %{ansible_python}-pytest-xdist >= 3.1.0
BuildRequires:  %{ansible_python}-yamllint
%endif
# add runtime dependencies of molecule as BuildRequires
# https://github.com/ansible/molecule/blob/main/.config/requirements.in
BuildRequires:  %{ansible_python}-base >= 3.9
BuildRequires:  ansible-core >= 2.12.10
BuildRequires:  %{ansible_python}-ansible-compat >= 24.6.1
BuildRequires:  %{ansible_python}-click >= 8.0
BuildRequires:  %{ansible_python}-click-help-colors >= 0.9
BuildRequires:  %{ansible_python}-enrich >= 1.2.7
BuildRequires:  %{ansible_python}-jsonschema >= 4.9.1
BuildRequires:  %{ansible_python}-Jinja2 >= 2.11.3
BuildRequires:  %{ansible_python}-packaging
BuildRequires:  %{ansible_python}-pluggy >= 0.7.1
BuildRequires:  %{ansible_python}-PyYAML >= 5.1
BuildRequires:  %{ansible_python}-rich >= 9.5.1
BuildRequires:  %{ansible_python}-wcmatch >= 8.1.2
BuildRequires:  fdupes
# https://github.com/ansible/molecule/blob/main/.config/requirements.in
Requires:       %{ansible_python}-base >= 3.9
Requires:       %{ansible_python}-ansible-compat >= 24.6.1
Requires:       ansible-core >= 2.12.10
Requires:       %{ansible_python}-click >= 8.0
Requires:       %{ansible_python}-click-help-colors >= 0.9
Requires:       %{ansible_python}-enrich >= 1.2.7
Requires:       %{ansible_python}-jsonschema >= 4.9.1
Requires:       %{ansible_python}-Jinja2 >= 2.11.3
Requires:       %{ansible_python}-packaging
Requires:       %{ansible_python}-pluggy >= 0.7.1
Requires:       %{ansible_python}-PyYAML >= 5.1
Requires:       %{ansible_python}-rich >= 9.5.1
Requires:       %{ansible_python}-wcmatch >= 8.1.2
BuildArch:      noarch

%description
Molecule project is designed to aid in the development and testing of
Ansible roles.

Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios.

%prep
%autosetup -p 1 -n molecule-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{ansible_python_sitelib}

%check
%if %{with test}
export PATH="%{buildroot}%{_bindir}:$PATH"
sed -i '/^addopts/s/ --color=yes//' pyproject.toml

IGNORED_CHECKS="test_podman"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_command_dependency"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_command_init_role[delegated]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_command_init_scenario[delegated]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_docker"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_molecule_schema"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_sample_collection"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_with_and_without_gitignore[test_w_gitignore]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_execute_cmdline_scenarios"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_execute_cmdline_scenarios_prune"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_execute_cmdline_scenarios_no_prune"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_execute_cmdline_scenarios_exit_destroy"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_execute_cmdline_scenarios_exit_nodestroy"

%pytest -k "not (${IGNORED_CHECKS})" -W ignore:'There is no current event loop'
%endif

%files
%license LICENSE
%{ansible_python_sitelib}/*
%{_bindir}/molecule

%changelog
