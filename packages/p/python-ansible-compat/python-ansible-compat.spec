#
# spec file for package python-ansible-compat
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%if 0%{?suse_version} >= 1600
# Tumbleweed
# only works with the python version which the package 'ansible' uses
%define pythons python3
%endif

Name:           python-ansible-compat
Version:        25.8.2
Release:        0
Summary:        Compatibility shim for Ansible 2.9 and newer
License:        MIT
URL:            https://github.com/ansible-community/ansible-compat
Source:         https://github.com/ansible-community/ansible-compat/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 7.0.5}
BuildRequires:  %{python_module setuptools >= 65.3.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test
# https://github.com/ansible/ansible-compat/blob/main/.config/requirements.in
BuildRequires:  ansible-core >= 2.16
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module jsonschema >= 4.17.3}
BuildRequires:  %{python_module packaging >= 25.0}
BuildRequires:  %{python_module subprocess-tee >= 0.4.1}
# https://github.com/ansible/ansible-compat/blob/main/.config/requirements-test.in
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-instafail}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-plus}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
Requires:       ansible-core >= 2.16
Requires:       python-PyYAML >= 6.0.2
Requires:       python-jsonschema >= 4.17.3
Requires:       python-packaging >= 25.0
Requires:       python-subprocess-tee >= 0.4.1
%{?python_enable_dependency_generator}
BuildArch:      noarch
%python_subpackages

%description
Facilitate working with various versions of Ansible 2.9 and newer.

%prep
%setup -q -n ansible-compat-%{version}

# for some reason 15.x errors out with an invalid duplicate license in pyproject.toml...
%if 0%{?suse_version} < 1600
sed -i '/license/d' pyproject.toml
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# excluding tests requiring internet connection
IGNORED_CHECKS="test_install_collection"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_install_collection_dest"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_prepare_environment_with_collections"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_prerun_reqs_v1"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_prerun_reqs_v2"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_require_collection"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_require_collection_no_cache_dir"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_require_collection_wrong_version"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_runtime_example"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_runtime_require_module"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[isolatedF-scanF-raises_not_foundT]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[isolatedF-scanT-raises_not_foundF]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[isolatedT-scanF-raises_not_foundT]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[isolatedT-scanT-raises_not_foundT]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[scanF-raises_not_foundT]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[scanT-raises_not_foundF]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_upgrade_collection"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_runtime_has_playbook"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_load_plugins[modules]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_cache_dir_relative"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ro_venv"
# tests that need network connectivity
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[0]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[1]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[disabled]"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_scan_sys_path[enabled]"
# Disable checks on test names: https://github.com/pytest-dev/pytest-plus#user-content-avoiding-problematic-test-identifiers https://github.com/ansible/ansible-compat/issues/340
export PYTEST_CHECK_TEST_ID_REGEX=0
%pytest -k "not (${IGNORED_CHECKS})"

%files %{python_files}
%{python_sitelib}/ansible_compat
%{python_sitelib}/ansible_compat-%{version}.dist-info
%doc README.md
%license LICENSE

%changelog
