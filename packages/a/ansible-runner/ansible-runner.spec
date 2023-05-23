#
# spec file for package ansible-runner
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

%define module_name ansible-runner

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

Name:           ansible-runner
Version:        2.3.2
Release:        0
Summary:        Run ansible-playbook inside an execution environment
License:        Apache-2.0
URL:            https://github.com/ansible/%{module_name}
Source:         https://files.pythonhosted.org/packages/source/a/%{module_name}/%{module_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-rpm-macros
# https://github.com/ansible/ansible-runner/blob/devel/setup.cfg#L31
BuildRequires:  %{ansible_python}-base >= 3.8
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-pbr
# https://github.com/ansible/ansible-runner/blob/devel/setup.cfg#L32
BuildRequires:  ansible-core
BuildRequires:  %{ansible_python}-packaging
BuildRequires:  %{ansible_python}-pexpect >= 4.5
BuildRequires:  %{ansible_python}-python-daemon
BuildRequires:  %{ansible_python}-PyYAML
BuildRequires:  %{ansible_python}-six
# https://github.com/ansible/ansible-runner/blob/devel/setup.cfg#L38
# importlib-metadata not required, as we are using python3.10 or higher
# SECTION test requirements
# https://github.com/ansible/ansible-runner/blob/devel/test/requirements.txt
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-pytest-mock
BuildRequires:  %{ansible_python}-pytest-timeout
BuildRequires:  %{ansible_python}-pytest-xdist
# /SECTION
BuildRequires:  fdupes
# https://github.com/ansible/ansible-runner/blob/devel/setup.cfg#L32
Requires:       %{ansible_python}-packaging
Requires:       %{ansible_python}-pexpect >= 4.5
Requires:       %{ansible_python}-python-daemon
Requires:       %{ansible_python}-PyYAML
Requires:       %{ansible_python}-six
Requires:       %{ansible_python}-setuptools
# https://github.com/ansible/ansible-runner/blob/devel/setup.cfg#L38
# importlib-metadata not required, as we are using python3.10 or higher

%description
Consistent Ansible Python API and CLI with container and process isolation runtime capabilities

%prep
%setup -q -n %{module_name}-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{ansible_python_sitelib}

sed -i '1s|^#!%{_bindir}/env bash$|#!%{_bindir}/bash|' %{buildroot}/%{_datadir}/%{module_name}/utils/entrypoint.sh

%check
# disable coverage tests
sed -i '/cov/d' pytest.ini

# Ignored tests, upstream bug report:
# https://github.com/ansible/ansible-runner/issues/1237
#
IGNORED_TESTS='test_callback_plugin_task_args_leak[playbook0] or '
IGNORED_TESTS+='test_resolved_actions[playbook0] or '
IGNORED_TESTS+='test_playbook_on_stats_summary_fields or '
IGNORED_TESTS+='test_multiline_blank_write[pexpect]'
export PATH=%{buildroot}%{_bindir}:$PATH
%pytest -k "not ($IGNORED_TESTS)"

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{module_name}
%{ansible_python_sitelib}/ansible_runner
%{ansible_python_sitelib}/ansible_runner-*-info
%dir %{_datadir}/%{module_name}/
%dir %{_datadir}/%{module_name}/utils/
%{_datadir}/%{module_name}/utils/entrypoint.sh

%changelog
