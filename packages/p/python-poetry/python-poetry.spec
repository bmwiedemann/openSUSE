#
# spec file for package python-poetry
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
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-poetry%{psuffix}
Version:        2.3.2
Release:        0
Summary:        Python dependency management and packaging
License:        MIT
URL:            https://python-poetry.org/
# PyPI sdist doesn't contain tests
Source:         https://github.com/python-poetry/poetry/archive/%{version}.tar.gz#/poetry-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-poetry-core = 2.3.1
Requires:       (python-build >= 1.2.1 with python-build < 2.0.0)
Requires:       (python-cachecontrol >= 0.14.0 with python-cachecontrol < 0.15.0)
# from cachecontrol[filecache]
Requires:       python-filelock >= 3.8.0
# /cachecontrol[filecache]
Requires:       (python-cleo >= 2.1.0 with python-cleo < 3.0.0)
Requires:       python-packaging >= 24
Requires:       python-pbs-installer >= 2025.6.10
Requires:       python-trove-classifiers >= 2022.5.19
Requires:       python-virtualenv >= 20.26.6
Requires:       (python-dulwich >= 0.25.0 with python-dulwich < 2)
Requires:       (python-fastjsonschema >= 2.18.0 with python-fastjsonschema < 3.0.0)
Requires:       (python-findpython >= 0.6.2 with python-findpython < 0.8.0)
Requires:       (python-installer >= 0.7.0 with python-installer < 0.8.0)
Requires:       (python-keyring >= 25.1.0 with python-keyring < 26.0.0)
Requires:       (python-pkginfo >= 1.12 with python-pkginfo < 2.0)
Requires:       (python-platformdirs >= 3.0.0 with python-platformdirs < 5)
Requires:       (python-pyproject-hooks >= 1.0.0 with python-pyproject-hooks < 2.0.0)
Requires:       (python-requests >= 2.26 with python-requests < 3.0)
Requires:       (python-requests-toolbelt >= 1.0.0 with python-requests-toolbelt < 2.0.0)
Requires:       (python-shellingham >= 1.5 with python-shellingham < 2.0)
Requires:       (python-tomlkit >= 0.11.4 with python-tomlkit < 1.0.0)
# python-pbs-installer[download,install]
Requires:       (python-httpx >= 0.27.0 with python-httpx < 1)
Requires:       python-zstandard >= 0.21.0
# /python-pbs-installer[download,install]
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     git-core
Recommends:     python-devel
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module cachy >= 0.3.0}
BuildRequires:  %{python_module deepdiff >= 6.3}
# Required because deepdiff > 6.2.3
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module poetry = %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 7.1}
BuildRequires:  %{python_module pytest-mock >= 3.9}
BuildRequires:  %{python_module pytest-xdist >= 3.1}
BuildRequires:  %{python_module responses >= 0.25}
BuildRequires:  git-core
%endif
%python_subpackages

%description
Python dependency management and packaging made easy.

%prep
%autosetup -p1 -n poetry-%{version}
echo "# empty module" >> src/poetry/console/events/console_events.py

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/poetry
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# can't install setuptools from PyPI (no network)
donttest="test_uninstall_git_package_nspkg_pth_cleanup or test_builder_setup_generation_runs_with_pip_editable"
donttest="$donttest or test_installer_with_pypi_repository"
# does not find the expected packages in venv
donttest="$donttest or test_executor_should_write_pep610_url_references"
donttest="$donttest or test_prepare_directory or test_prepare_sdist"
donttest="$donttest or test_isolated_env_install_success"
# different hashes in our own ecosystem
donttest="$donttest or test_executor_known_hashes"
# no command "exit-code"
donttest="$donttest or test_info_setup_complex_calls_script"
# we have other packages installed
donttest="$donttest or test_system_site_packages"
# does not raise deprecationwarning
donttest="$donttest or test_get_http_auth"
# requires /tmp to be mounted exec
donttest="$donttest or test_list_poetry_managed or test_find_all_with_poetry_managed"
donttest="$donttest or test_find_poetry_managed_pythons"
# flaky
donttest="$donttest or test_threading_atomic_cached_property_different_instances"
%{python_expand # pytest needs to be called from the virtualenv python interpreter gh#python-poetry/poetry#1645
virtualenv-%{$python_bin_suffix} --system-site-packages testenv-%{$python_bin_suffix}
source testenv-%{$python_bin_suffix}/bin/activate
export PYTHONDONTWRITEBYTECODE=1
python -m pytest -v -k "not ($donttest)"
deactivate
}
%endif

%post
%python_install_alternative poetry

%postun
%python_uninstall_alternative poetry

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/poetry
%{python_sitelib}/poetry-%{version}.dist-info
%python_alternative %{_bindir}/poetry
%endif

%changelog
