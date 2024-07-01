#
# spec file for package python-poetry
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
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-poetry%{psuffix}
Version:        1.8.3
Release:        0
Summary:        Python dependency management and packaging
License:        MIT
Group:          Development/Languages/Python
URL:            https://python-poetry.org/
# PyPI sdist doesn't contain tests
Source:         https://github.com/python-poetry/poetry/archive/%{version}.tar.gz#/poetry-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.7.0 with %python-poetry-core < 2.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-build >= 1.0.3
Requires:       python-poetry-core = 1.9.0
Requires:       python-poetry-plugin-export >= 1.6.0
# SECTION cachecontrol[filecache]
Requires:       python-CacheControl >= 0.13
Requires:       python-filelock >= 3.8.0
# /SECTION
Requires:       python-cleo >= 2.0.0
Requires:       python-crashtest >= 0.4.1
Requires:       python-dulwich >= 0.21.2
Requires:       python-fastjsonschema >= 2.18.0
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 4.4
%endif
Requires:       python-installer >= 0.7.0
Requires:       python-keyring >= 24.0
Requires:       python-packaging >= 23.1
Requires:       python-pexpect >= 4.7.0
Requires:       python-pkginfo >= 1.10.0
Requires:       python-pyproject-hooks >= 1.0.0
Requires:       python-requests >= 2.26
Requires:       python-shellingham >= 1.5
Requires:       (python-platformdirs >= 3.0.0 with python-platformdirs < 5)
Requires:       (python-requests-toolbelt >= 1.0.0 with python-requests-toolbelt < 2)
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 2.0.1
%endif
Requires:       python-trove-classifiers >= 2022.5.19
Requires:       python-virtualenv >= 20.22
Requires:       (python-tomlkit >= 0.11.4 with python-tomlkit < 1.0)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     git-core
Recommends:     python-devel
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module cachy >= 0.3.0}
BuildRequires:  %{python_module deepdiff >= 6.3}
BuildRequires:  %{python_module httpretty >= 1.0}
# Required because deepdiff > 6.2.3
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module poetry = %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 7.1}
BuildRequires:  %{python_module pytest-mock >= 3.9}
BuildRequires:  %{python_module pytest-xdist >= 3.1}
BuildRequires:  git-core
%endif
%python_subpackages

%description
Python dependency management and packaging made easy.

%prep
%autosetup -p1 -n poetry-%{version}
for f in console/events/console_events.py \
         layouts/standard.py; do
  [ -e src/poetry/$f ] || exit 1 # file does not exist
  [ ! -s src/poetry/$f ] && echo "# empty module" >> src/poetry/$f || exit 2 # file is not empty
done

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
