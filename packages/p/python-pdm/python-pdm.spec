#
# spec file for package python-pdm
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-pdm%{psuffix}
Version:        2.16.1
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://github.com/pdm-project/pdm/
Source0:        https://files.pythonhosted.org/packages/source/p/pdm/pdm-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module importlib-metadata if %python-base <= 3.9}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blinker
Requires:       python-cachecontrol >= 0.12.11
Requires:       python-certifi
Requires:       python-dep-logic
Requires:       python-findpython >= 0.4
Requires:       python-hishel
Requires:       python-installer
Requires:       python-packaging >= 20.9
Requires:       python-pbs-installer
Requires:       python-pdm-backend
Requires:       python-platformdirs
Requires:       python-pyproject-hooks
Requires:       python-python-dotenv >= 0.15
Requires:       python-requests-toolbelt
Requires:       python-resolvelib >= 1.0.1
Requires:       python-rich >= 12.3.0
Requires:       python-shellingham >= 1.3.2
Requires:       python-unearth >= 0.12.1
Requires:       python-virtualenv >= 20
Requires:       (python-tomlkit >= 0.11.1 with python-tomlkit < 1)
# from python-cachecontrol[filecache]
Requires:       python-lockfile >= 0.9
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
%if 0%{?python_version_nodots} <= 39
Requires:       python-importlib-metadata
Requires:       python-typing-extensions
%endif
%if 0%{?python_version_nodots} >= 310
Requires:       python-truststore
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module hishel}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pbs-installer}
BuildRequires:  %{python_module pdm = %{version}}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module unearth}
%endif
# /SECTION
%python_subpackages

%description
PDM is a modern Python package manager with PEP 582 support. It
installs and manages packages in a similar way to npm that
doesn't need to create a virtualenv at all!

%prep
%autosetup -p1 -n pdm-%{version}
#  we don't care about certifi version, the distro package replaces the certificates with system ones anyway
sed -i 's/"certifi>=[0-9.]*"/"certifi"/' pyproject.toml

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pdm
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# no network
donttest="network"
# mock testing finds the wrong python versions in our multiflavor setup
donttest="$donttest or test_project_packages_path or test_conda_backend_create"
donttest="$donttest or test_init_non_interactive"

# Broken test trying to find a resolution to a git repository
donttest="$donttest or test_add_editable_package or test_non_editable_override_editable"
# Broken test unable to find a resolution for wheel
donttest="$donttest or test_list_dependency_graph_include_exclude or test_list_csv_include_exclude_valid"
# Unable to find a resolution for setuptools
donttest="$donttest or test_list_csv_include_exclude or test_remove_editable_packages_while_keeping_normal or test_project_backend"
# Requires network
donttest="$donttest or test_build_with_no_isolation"
# Requires network
donttest="$donttest or test_find_candidates_from_find_links"
donttest="$donttest or test_build_single_module"
donttest="$donttest or test_build_single_module_with_readme"
donttest="$donttest or test_build_package"
donttest="$donttest or test_build_src_package"
donttest="$donttest or test_build_package_include"
donttest="$donttest or test_build_src_package_by_include"
donttest="$donttest or test_build_with_config_settings"
donttest="$donttest or test_cli_build_with_config_settings"
donttest="$donttest or test_build_ignoring_pip_environment"
donttest="$donttest or test_find_interpreters_with_PDM_IGNORE_ACTIVE_VENV"
donttest="$donttest or test_hooks[build] or test_hooks[publish]"
donttest="$donttest or test_skip_option_from_signal"
donttest="$donttest or test_skip_all_option_from_signal"
donttest="$donttest or test_skip_pre_post_option_from_signal"
donttest="$donttest or test_build_distributions"
donttest="$donttest or test_show_self_package"
donttest="$donttest or test_publish_and_build_in_one_run"
donttest="$donttest or test_expand_project_root_in_url"

%pytest -v -k "not ($donttest)"
%endif

%post
%python_install_alternative pdm

%postun
%python_uninstall_alternative pdm

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pdm
%{python_sitelib}/pdm
%{python_sitelib}/pdm-%{version}*-info
%endif

%changelog
