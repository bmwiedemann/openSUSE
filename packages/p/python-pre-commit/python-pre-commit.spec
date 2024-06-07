#
# spec file for package python-pre-commit
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
Name:           python-pre-commit
Version:        3.7.1
Release:        0
Summary:        Multi-language pre-commit hooks
License:        MIT
URL:            https://github.com/pre-commit/pre-commit
Source:         https://github.com/pre-commit/pre-commit/archive/v%{version}.tar.gz#/pre-commit-%{version}.tar.gz
%if 0%{?sle_version} <= 150600
Group:          Development/Tools/Other
%endif
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-cfgv >= 2.0.0
Requires:       python-identify >= 1.0.0
Requires:       python-nodeenv >= 0.11.1
Requires:       python-virtualenv >= 20.10.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
BuildRequires:  lua53-devel
BuildRequires:  lua53-luarocks
%else
BuildRequires:  lua54-devel
BuildRequires:  lua54-luarocks
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module cfgv >= 2.0.0}
BuildRequires:  %{python_module identify >= 1.0.0}
BuildRequires:  %{python_module nodeenv >= 0.11.1}
BuildRequires:  %{python_module pytest-env}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module re-assert}
BuildRequires:  %{python_module virtualenv >= 20.10.0}
BuildRequires:  %{pythons}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
A framework for managing and maintaining multi-language pre-commit hooks.

%prep
%autosetup -n pre-commit-%{version}
sed -i 's|^#!%{_bindir}/env python|#!%{_bindir}/python|' pre_commit/resources/hook-tmpl
sed -i 's|^#!%{_bindir}/env bash|#!%{_bindir}/bash|' pre_commit/resources/hook-tmpl

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pre-commit

%check
export GIT_AUTHOR_NAME=test GIT_COMMITTER_NAME=test \
    GIT_AUTHOR_EMAIL=test@example.com GIT_COMMITTER_EMAIL=test@example.com \
    VIRTUALENV_NO_DOWNLOAD=1 PRE_COMMIT_NO_CONCURRENCY=1 LANG=en_US.UTF-8
# gh#pre-commit/pre-commit#1202
# test_switch_language_versions_doesnt_clobber - looks like your installation of python is broken?
# test_run_a_ruby_hook, test_additional_ruby_dependencies_installed: you need to have gem installed
# test_golang_hook, test_golang_hook_still_works_when_gobin_is_set, test_additional_golang_dependencies_installed, test_local_golang_additional_deps: you need to have go installed
# test_rust_hook, test_additional_rust_lib_dependencies_installed, test_local_rust_additional_dependencies: you need to have cargo installed
# test_installed_from_venv I suspect you have some PYTHONPATH shenanigans going on? hard to tell
# conda, dart, dotnet, node, r tests: not available
# test_node_hook_with_npm_userconfig_set: need internet
# test_perl_hook, test_local_perl_additional_dependencies: need internet
EXCLUDED_TESTS="test_main or test_run_a_node_hook or test_run_versioned_node_hook or test_additional_node_dependencies_installed or test_node_hook_with_npm_userconfig_set"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_run_versioned_ruby_hook or test_run_ruby_hook_with_disable_shared_gems or test_additional_dependencies_roll_forward"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_golang or test_additional_ruby_ or test_additional_golang_ or test_additional_rust_ or test_rust"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_switch_language_versions_doesnt_clobber or test_run_a_ruby_hook or test_local_golang_additional_deps"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_local_rust_additional_dependencies or test_installed_from_venv"
EXCLUDED_TESTS="$EXCLUDED_TESTS or conda or test_perl_hook or test_local_perl_additional_dependencies"
EXCLUDED_TESTS="$EXCLUDED_TESTS or dart or dotnet or r_ or node or ruby"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_local_lua_additional_dependencies"
# rust_tests use rustup which require network
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_local_python_repo_python2 or rust_test"
# tests that require network access
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_run_example_executable"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_run_dep"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_perl_additional_dependencies"
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_lua_additional_dependencies"
EXCLUDED_TESTS="$EXCLUDED_TESTS or (golang_test and test_during_commit_all)"
# requires swift
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_swift_language"
%if 0%{?sle_version} <= 150600
# requires network on Leap or SUSE Linux Enterprise
EXCLUDED_TESTS="$EXCLUDED_TESTS or test_perl_install"
%endif

# Fix issue with git submodule in OBS
git config --global --add protocol.file.allow always
git init .

# Required for python312 https://virtualenv.pypa.io/en/latest/changelog.html#features-20-23-0
export VIRTUALENV_SETUPTOOLS=bundle
export VIRTUALENV_WHEEL=bundle

%pytest -k "not ($EXCLUDED_TESTS)"

%post
%python_install_alternative pre-commit

%postun
%python_uninstall_alternative pre-commit

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md
%python_alternative %{_bindir}/pre-commit
%{python_sitelib}/pre_commit
%{python_sitelib}/pre_commit-%{version}.dist-info

%changelog
