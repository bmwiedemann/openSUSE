#
# spec file for package ansible-creator
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           ansible-creator
Version:        26.3.3
Release:        0
Summary:        A CLI tool for scaffolding Ansible Content
License:        Apache-2.0
URL:            https://github.com/ansible/ansible-creator
Source:         ansible-creator-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  git-core
# https://github.com/ansible/ansible-creator/blob/main/pyproject.toml
BuildRequires:  %{ansible_python}-base >= 3.10
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools >= 65.3.0
BuildRequires:  %{ansible_python}-setuptools_scm >= 7.0.5
BuildRequires:  %{ansible_python}-wheel
BuildRequires:  python-rpm-macros
# Runtime deps as BuildRequires to ensure buildability
# https://github.com/ansible/ansible-creator/blob/main/pyproject.toml#L29
BuildRequires:  %{ansible_python}-Jinja2 >= 3.1.2
BuildRequires:  %{ansible_python}-PyYAML >= 6.0.1
# SECTION test requirements
# https://github.com/ansible/ansible-creator/blob/main/pyproject.toml (dependency-groups)
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-pytest-xdist
# /SECTION
BuildRequires:  fdupes
# https://github.com/ansible/ansible-creator/blob/main/pyproject.toml#L29
Requires:       %{ansible_python}-Jinja2 >= 3.1.2
Requires:       %{ansible_python}-PyYAML >= 6.0.1

%description
Ansible Creator is a CLI tool for scaffolding Ansible content.
It provides commands to initialize new Ansible projects and add
resources to existing ones, including collections, playbook
projects, and execution environments.

See the documentation at:
https://ansible.readthedocs.io/projects/creator/

%prep
%setup -q -n ansible-creator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{ansible_python_sitelib}

%check
export PATH=%{buildroot}%{_bindir}:$PATH
# Integration tests require the installed binary and external tools (npm, ansible-lint)
# Run only unit tests; skip test_devcontainer_usability which requires npm
%pytest tests/units -k "not test_devcontainer_usability"

%files
%doc README.md
%license LICENSE
%{_bindir}/ansible-creator
%{ansible_python_sitelib}/ansible_creator
%{ansible_python_sitelib}/ansible_creator-%{version}.dist-info

%changelog
