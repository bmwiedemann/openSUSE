#
# spec file for package python-pre-commit
#
# Copyright (c) 2019 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pre-commit
Version:        1.20.0
Release:        0
Summary:        Multi-language pre-commit hooks
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pre-commit/pre-commit
Source:         https://github.com/pre-commit/pre-commit/archive/v%{version}.tar.gz#/pre_commit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-aspy.yaml
Requires:       python-cfgv >= 1.4.0
Requires:       python-identify >= 1.0.0
Requires:       python-importlib-metadata
Requires:       python-nodeenv >= 0.11.1
Requires:       python-six
Requires:       python-toml
Requires:       python-virtualenv >= 15.2
%ifpython2
Requires:       python-futures
Requires:       python-importlib_resources
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aspy.yaml}
BuildRequires:  %{python_module cfgv >= 1.4.0}
BuildRequires:  %{python_module identify >= 1.0.0}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nodeenv >= 0.11.1}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module virtualenv >= 15.2}
BuildRequires:  git-core
BuildRequires:  python2-futures
BuildRequires:  python2-importlib_resources
BuildRequires:  python3
# /SECTION
%python_subpackages

%description
A framework for managing and maintaining multi-language pre-commit hooks.

%prep
%setup -q -n pre-commit-%{version}
rm pre_commit/color_windows.py
sed -i 's|^#!/usr/bin/env python|#!%{_bindir}/python|' pre_commit/resources/hook-tmpl

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# %%check
# export GIT_AUTHOR_NAME=test GIT_COMMITTER_NAME=test \
#     GIT_AUTHOR_EMAIL=test@example.com GIT_COMMITTER_EMAIL=test@example.com \
#     VIRTUALENV_NO_DOWNLOAD=1 PRE_COMMIT_NO_CONCURRENCY=1
# # gh#pre-commit/pre-commit#1202
# #     test_switch_language_versions_doesnt_clobber - looks like your installation of python2 is broken?
# #     test_run_a_ruby_hook, test_additional_ruby_dependencies_installed: you need to have gem installed
# #     test_golang_hook, test_golang_hook_still_works_when_gobin_is_set, test_additional_golang_dependencies_installed, test_local_golang_additional_dependencies: you need to have go installed
# #     test_rust_hook, test_additional_rust_lib_dependencies_installed, test_local_rust_additional_dependencies: you need to have cargo installed
# #     test_installed_from_venv I suspect you have some PYTHONPATH shenanigans going on? hard to tell
# #     test_healthy_types_py_in_cwd: no idea, probably a problem with your environment
# EXCLUDED_TESTS="test_main or test_run_a_node_hook or test_run_versioned_node_hook or test_additional_node_dependencies_installed"
# EXCLUDED_TESTS="$EXCLUDED_TESTS or test_run_versioned_ruby_hook or test_run_ruby_hook_with_disable_shared_gems or test_additional_dependencies_roll_forward"
# EXCLUDED_TESTS="$EXCLUDED_TESTS or test_golang or test_additional_ruby_ or test_additional_golang_ or test_additional_rust_ or test_rust"
# EXCLUDED_TESTS="$EXCLUDED_TESTS or test_switch_language_versions_doesnt_clobber or test_run_a_ruby_hook or test_local_golang_additional_dependencies"
# EXCLUDED_TESTS="$EXCLUDED_TESTS or test_local_rust_additional_dependencies or test_installed_from_venv or test_healthy_types_py_in_cwd"
# git init .
# %%pytest -k "not ($EXCLUDED_TESTS)"

%files %{python_files}
%python3_only %{_bindir}/pre-commit-validate-manifest
%python3_only %{_bindir}/pre-commit
%python3_only %{_bindir}/pre-commit-validate-config
%{python_sitelib}/*

%changelog
