#
# spec file for package python-pdm
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
Version:        2.26.7
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://github.com/pdm-project/pdm/
Source0:        https://files.pythonhosted.org/packages/source/p/pdm/pdm-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pdm-project/pdm#3764
Patch0:         support-installer-1.0.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module importlib-metadata if %python-base <= 3.9}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blinker
Requires:       python-certifi >= 2024.8.30
Requires:       python-dep-logic >= 0.5
Requires:       python-filelock >= 3.13
Requires:       python-findpython >= 0.7
Requires:       python-hishel >= 1.0.0
Requires:       python-httpcore >= 1.0.6
Requires:       python-httpx >= 0.20
Requires:       python-id >= 1.5.0
Requires:       python-installer >= 0.7
Requires:       python-packaging >= 22.0
Requires:       python-pbs-installer >= 2025.10.7
Requires:       python-platformdirs
Requires:       python-pyproject-hooks
Requires:       python-python-dotenv >= 0.15
Requires:       python-resolvelib >= 1.1
Requires:       python-rich >= 12.3.0
Requires:       python-shellingham >= 1.3.2
Requires:       python-unearth >= 0.17.5
Requires:       python-virtualenv >= 20
Requires:       (python-tomlkit >= 0.11.1 with python-tomlkit < 1)
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 3.6
%endif
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
%if 0%{?python_version_nodots} >= 310
Requires:       python-truststore >= 0.10.4
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pdm = %{version}}
BuildRequires:  %{python_module pytest-httpserver >= 1.0.6}
BuildRequires:  %{python_module pytest-httpx >= 0.34}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-rerunfailures >= 10.2}
BuildRequires:  %{python_module pytest-xdist >= 1.31}
BuildRequires:  %{python_module pytest}
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
find . -name ".gitignore" -print -delete

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
donttest="$donttest or test_init_auto_create_venv"
donttest="$donttest or test_expand_project_root_in_url"
donttest="$donttest or test_use_python_write_file_with_use_python_version"
donttest="$donttest or test_use_python_write_file_without_use_python_version"
# Different requires python
donttest="$donttest or test_new_command"
# Broken with installer v1
donttest="$donttest or test_uninstall_with_console_scripts"
donttest="$donttest or test_install_wheel_with_cache"
donttest="$donttest or test_can_install_wheel_with_cache_in_multiple_projects"
donttest="$donttest or test_url_requirement_is_not_cached"
donttest="$donttest or test_install_wheel_with_data_scripts"

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
