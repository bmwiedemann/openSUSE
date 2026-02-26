#
# spec file for package python-pytest-ansible
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
#
%define python_for_dependencies python310
%endif
%if %pythons == "python311"
%define ansible_python python311
%define ansible_python_executable python3.11
%define ansible_python_sitelib %python311_sitelib
#
%define python_for_dependencies python311
%endif
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_executable python3
%define ansible_python_sitelib %python3_sitelib
#
%define python_for_dependencies python3
%endif

Name:           python-pytest-ansible
Version:        26.2.0
Release:        0
Summary:        Plugin for pytest to simplify calling ansible modules from tests or fixtures
License:        MIT
URL:            https://github.com/ansible-community/pytest-ansible
Source:         pytest-ansible-%{version}.tar.gz
BuildRequires:  %{python_for_dependencies}-base >= 3.10
BuildRequires:  %{python_for_dependencies}-pip
BuildRequires:  %{python_for_dependencies}-setuptools >= 63.0.0
BuildRequires:  %{python_for_dependencies}-setuptools_scm >= 7.0.5
BuildRequires:  %{python_for_dependencies}-wheel
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
# SECTION runtime requirements
BuildRequires:  %{python_for_dependencies}-cffi >= 1.15.1
BuildRequires:  %{python_for_dependencies}-ansible-compat >= 25.8.2
BuildRequires:  %{python_for_dependencies}-packaging >= 23.2
BuildRequires:  %{python_for_dependencies}-pytest >= 6
BuildRequires:  %{python_for_dependencies}-pytest-xdist >= 3.8.0
BuildRequires:  %{python_for_dependencies}-typing_extensions >= 4.15.0
BuildRequires:  ansible-core > 2.16.14
# /SECTION
# SECTION test requirements
BuildRequires:  ansible-core >= 2.17.4
BuildRequires:  %{python_module bracex}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  ansible-test >= 2.15.0
BuildRequires:  molecule >= 6.0.0
# /SECTION
BuildRequires:  fdupes
Requires:       %{python_for_dependencies}-ansible-compat >= 25.8.2
Requires:       %{python_for_dependencies}-cffi >= 1.15.1
Requires:       %{python_for_dependencies}-packaging >= 23.2
Requires:       %{python_for_dependencies}-pytest >= 6
Requires:       %{python_for_dependencies}-pytest-xdist >= 3.8.0
Requires:       %{python_for_dependencies}-typing_extensions >= 4.15.0
Requires:       ansible-core > 2.16.16
BuildArch:      noarch
%python_subpackages

%description
Plugin for pytest to simplify calling ansible modules from tests or fixtures

%prep
%autosetup -p1 -n pytest-ansible-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
IGNORED_CHECKS="test_connection_failure_extra_inventory_v2"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_connection_failure_v2"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_contacted_with_params"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_contacted_with_params_and_host_pattern_marker"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_contacted_with_params_and_inventory_host_pattern_marker"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_contacted_with_params_and_inventory_marker"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_dark_with_debug_enabled"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_dark_with_params"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_dark_with_params_and_host_pattern_marker"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_dark_with_params_and_inventory_marker"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_molecule_disabled"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_molecule_runtest"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ansible_test"

%pytest -k "not (${IGNORED_CHECKS})" -W ignore:'There is no current event loop'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pytest_ansible
%{python_sitelib}/pytest_ansible-%{version}.dist-info

%changelog
