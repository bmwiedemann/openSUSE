#
# spec file for package ansible-builder
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

Name:           ansible-builder
Version:        3.1.0
Release:        0
Summary:        An Ansible execution environment builder
License:        Apache-2.0
URL:            https://github.com/ansible/ansible-builder
Source:         ansible-builder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  git-core
# https://github.com/ansible/ansible-builder/blob/devel/setup.cfg#L41
BuildRequires:  %{ansible_python}-base >= 3.9
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-setuptools_scm
BuildRequires:  %{ansible_python}-wheel
BuildRequires:  ansible-core
BuildRequires:  python-rpm-macros
# https://github.com/ansible/ansible-builder/blob/devel/requirements.txt
BuildRequires:  %{ansible_python}-PyYAML
BuildRequires:  %{ansible_python}-bindep
BuildRequires:  %{ansible_python}-filelock
BuildRequires:  %{ansible_python}-jsonschema
BuildRequires:  %{ansible_python}-packaging
BuildRequires:  %{ansible_python}-pbr
#
# Tests require podman, but also require connectivity to pull container images
# hence we do not enable this dependency
# BuildRequires:  podman
#
# SECTION test requirements
# https://github.com/ansible/ansible-builder/blob/devel/test/requirements.txt
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-pytest-mock
BuildRequires:  %{ansible_python}-pytest-xdist
# /SECTION
BuildRequires:  fdupes
Requires:       %{ansible_python}-PyYAML
Requires:       %{ansible_python}-bindep
Requires:       %{ansible_python}-jsonschema
Requires:       %{ansible_python}-packaging
Requires:       (podman or docker)

%description
Ansible Builder is a tool that automates the process of
building execution environments using the schemas and
tooling defined in various Ansible Collections and by
the user.

See the readthedocs page for ansible-builder at:
https://ansible-builder.readthedocs.io/en/latest/

%prep
%setup -q -n ansible-builder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand sed -i "1{s/env bash/bash/;}" %{buildroot}%{ansible_python_sitelib}/ansible_builder/_target_scripts/entrypoint
%python_expand head -n 1 %{buildroot}%{ansible_python_sitelib}/ansible_builder/_target_scripts/entrypoint
%fdupes %{buildroot}%{ansible_python_sitelib}

%check
# disable coverage tests
sed -i '/cov/d' pytest.ini
# disable color output
sed -i '/color/d' pytest.ini
# add %{buildroot}%{_bindir} to PATH, so the executable is found
export PATH=%{buildroot}%{_bindir}:$PATH
# checks ignored, as they require podman
# https://github.com/ansible/ansible-builder/issues/534
IGNORED_CHECKS="test_v3_pre_post_commands"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_v3_complete"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ansible_check_is_skipped"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_missing_ansible"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_missing_runner"
%pytest -k "not (${IGNORED_CHECKS})"

%files
%doc README.md
%license LICENSE.md
%{_bindir}/ansible-builder
%{ansible_python_sitelib}/ansible_builder
%{ansible_python_sitelib}/ansible_builder-%{version}.dist-info

%changelog
