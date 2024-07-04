#
# spec file for package ansible-navigator
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

Name:           ansible-navigator
Version:        24.6.0
Release:        0
Summary:        A text-based user interface (TUI) for Ansible
License:        Apache-2.0
URL:            https://github.com/ansible/ansible-navigator
Source:         ansible-navigator-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{ansible_python}-base >= 3.10
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-setuptools_scm
BuildRequires:  %{ansible_python}-wheel
BuildRequires:  python-rpm-macros
# Use Requires also as BuildRequires
# to make sure we only build, if everything needed is present
# https://github.com/ansible/ansible-navigator/blob/main/.config/requirements.in
BuildRequires:  %{ansible_python}-Jinja2
BuildRequires:  %{ansible_python}-PyYAML
BuildRequires:  %{ansible_python}-jsonschema
BuildRequires:  %{ansible_python}-onigurumacffi >= 1.1.0
BuildRequires:  %{ansible_python}-pytzdata
BuildRequires:  %{ansible_python}-requirements-parser
BuildRequires:  ansible-builder >= 3.0.0
BuildRequires:  ansible-core >= 2.14.3
BuildRequires:  ansible-lint >= 6.19.0
BuildRequires:  ansible-runner >= 2.3.2
# SECTION test requirements
# https://github.com/ansible/ansible-navigator/blob/main/test/requirements.txt
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-libtmux
BuildRequires:  tmux
# /SECTION
BuildRequires:  git-core
BuildRequires:  fdupes
# https://github.com/ansible/ansible-navigator/blob/main/.config/requirements.in
Requires:       %{ansible_python}-Jinja2
Requires:       %{ansible_python}-PyYAML
Requires:       %{ansible_python}-curses
Requires:       %{ansible_python}-jsonschema
Requires:       %{ansible_python}-onigurumacffi >= 1.1.0
Requires:       %{ansible_python}-pytzdata
Requires:       %{ansible_python}-setuptools
Requires:       ansible-builder >= 3.0.0
Requires:       ansible-core >= 2.14.3
Requires:       ansible-lint >= 6.19.0
Requires:       ansible-runner >= 2.3.2
Requires:       (podman or docker)
Suggests:       %{ansible_python}-importlib-metadata
Suggests:       %{ansible_python}-mkdocs-ansible >= 0.1.2
Suggests:       %{ansible_python}-darglint
Suggests:       %{ansible_python}-libtmux
Suggests:       %{ansible_python}-pre-commit

%description
A text-based user interface (TUI) for Ansible.

When running ansible-navigator with no arguments, you will be presented with the welcome page. From this page, you can run playbooks, browse collections, explore inventories, read Ansible documentation, and more.

A full list of key bindings can be viewed by typing :help.

%prep
%setup -q -n ansible-navigator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{ansible_python_sitelib}

%files
%doc README.md
%license LICENSE
%{_bindir}/ansible-navigator
%{ansible_python_sitelib}/ansible_navigator
%{ansible_python_sitelib}/ansible_navigator-%{version}.dist-info/

%changelog
