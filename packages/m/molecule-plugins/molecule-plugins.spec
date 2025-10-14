#
# spec file for package molecule-plugins
#
# Copyright (c) 2025 SUSE LLC
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

Name:           molecule-plugins
Version:        25.8.12
Release:        0
Summary:        Collection of molecule plugins
License:        MIT
URL:            https://github.com/ansible-community/molecule-plugins
Source:         https://github.com/ansible-community/molecule-plugins/archive/v%{version}.tar.gz#/molecule-plugins-v%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-wheel
# add runtime dependencies as build dependencies
BuildRequires:  %{ansible_python}-selinux
BuildRequires:  %{ansible_python}-docker >= 4.3.1
BuildRequires:  %{ansible_python}-requests >= 2.31.0
BuildRequires:  %{ansible_python}-google-auth >= 2.28.2
#
BuildRequires:  fdupes
BuildRequires:  grep
# Test dependencies
BuildRequires:  molecule >= 6.0.0
BuildRequires:  podman
BuildRequires:  %{ansible_python}-ansi2html
BuildRequires:  %{ansible_python}-bracex
BuildRequires:  %{ansible_python}-coverage
BuildRequires:  %{ansible_python}-filelock
BuildRequires:  %{ansible_python}-pexpect
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-pytest-helpers-namespace >= 2019.1.8
BuildRequires:  %{ansible_python}-pytest-html
BuildRequires:  %{ansible_python}-pytest-mock
BuildRequires:  %{ansible_python}-pytest-plus
BuildRequires:  %{ansible_python}-pytest-testinfra
BuildRequires:  %{ansible_python}-pytest-xdist
Requires:       molecule
Requires:       %{ansible_python}-selinux
Requires:       %{ansible_python}-docker >= 4.3.1
Requires:       %{ansible_python}-requests >= 2.31.0
Requires:       %{ansible_python}-google-auth >= 2.28.2
BuildArch:      noarch

%description
Collection of the molecule plugins azure, docker and gce.

%prep
%autosetup -p 1 -n molecule-plugins-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

sed -i '0,/^#!/ d' \
	%{buildroot}%{ansible_python_sitelib}/molecule_plugins/docker/playbooks/validate-dockerfile.yml \
	%{buildroot}%{ansible_python_sitelib}/molecule_plugins/gce/playbooks/files/windows_auth.py \
	%{buildroot}%{ansible_python_sitelib}/molecule_plugins/podman/playbooks/validate-dockerfile.yml \
	%{buildroot}%{ansible_python_sitelib}/molecule_plugins/vagrant/modules/vagrant.py

%fdupes %{buildroot}%{ansible_python_sitelib}

%check
rm -rvf test/vagrant-plugin

export ANSIBLE_FORCE_COLOR={env:ANSIBLE_FORCE_COLOR:1}
export ANSIBLE_INVENTORY=./tests/hosts.ini
export ANSIBLE_CONFIG=./ansible.cfg
export ANSIBLE_NOCOWS=1
export ANSIBLE_RETRY_FILES_ENABLED=0
export MOLECULE_NO_LOG={env:MOLECULE_NO_LOG:0}
export MOLECULE_OPTS=--destroy always
export PIP_DISABLE_PIP_VERSION_CHECK=1

# tests failing due to missing network connectivity
# to https://galaxy.ansible.com/api/
IGNORED_CHECKS="test_containers_command_init_scenario"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_podman_command_init_scenario"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_dockerfile"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_sample"
%pytest -k "not (${IGNORED_CHECKS})"

%files
%license LICENSE
%doc README.md
%{ansible_python_sitelib}/*

%changelog

