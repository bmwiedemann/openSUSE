#
# spec file for package python-tox
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
%if %{defined sle15_python_module_pythons}
%bcond_without devpi_process
%else
%bcond_with devpi_process
%endif
Name:           python-tox
Version:        4.23.2
Release:        0
Summary:        Virtualenv-based automation of test activities
License:        MIT
URL:            https://github.com/tox-dev/tox
Source:         https://files.pythonhosted.org/packages/source/t/tox/tox-%{version}.tar.gz
# PATCH-FIX-OPENSUSE optional_devpi_process.patch mcepl@suse.com
# Make use devpi_process optional
Patch0:         optional_devpi_process.patch
# PATCH-FEATURE-UPSTREAM mark-network-tests.patch mcepl@suse.com
# to skip test which require network access
Patch1:         mark-network-tests.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module build >= 0.10.0}
BuildRequires:  %{python_module cachetools >= 5.3.2}
BuildRequires:  %{python_module chardet >= 5.2}
BuildRequires:  %{python_module colorama >= 0.4.6}
BuildRequires:  %{python_module filelock >= 3.13.1}
BuildRequires:  %{python_module hatch >= 0.3}
BuildRequires:  %{python_module hatch_vcs >= 0.4}
BuildRequires:  %{python_module hatchling >= 1.21}
BuildRequires:  %{python_module packaging >= 23.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 4.1}
BuildRequires:  %{python_module pluggy >= 1.3}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pyproject-api >= 1.6.1}
BuildRequires:  %{python_module pytoml >= 0.1}
BuildRequires:  %{python_module re-assert}
BuildRequires:  %{python_module setuptools >= 41.0.1}
BuildRequires:  %{python_module setuptools_scm >= 2.0.0}
BuildRequires:  %{python_module time-machine >= 2.13}
BuildRequires:  %{python_module tomli >= 2.0.1}
BuildRequires:  %{python_module virtualenv >= 20.24.3}
BuildRequires:  %{python_module wheel >= 0.42}
%if %{with devpi_process}
BuildRequires:  %{python_module devpi-process > 1}
%endif
BuildRequires:  %{python_module importlib-metadata >= 6.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-cachetools >= 5.3.2
Requires:       python-chardet >= 5.2
Requires:       python-colorama >= 0.4.6
Requires:       python-filelock >= 3.13.1
Requires:       python-packaging >= 23.2
Requires:       python-platformdirs >= 4.1
Requires:       python-pluggy >= 1.3
Requires:       python-pyproject-api >= 1.6.1
Requires:       python-virtualenv >= 20.24.3
Requires:       (python-importlib-metadata >= 0.12 if python-base < 3.8)
Requires:       (python-tomli >= 2.0.1 if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun):update-alternatives
# last detox version is 0.19
Obsoletes:      python-detox <= 0.19
Provides:       python-detox > 0.19
BuildArch:      noarch
# SECTION setup.cfg [options.extras_requires] testing=
# (except for pytest-cov and -randomly)
BuildRequires:  %{python_module flaky >= 3.7.0}
BuildRequires:  %{python_module freezegun >= 0.3.11}
BuildRequires:  %{python_module numpy >= 1.25}
BuildRequires:  %{python_module psutil >= 5.9.5}
BuildRequires:  %{python_module pytest >= 7.4.4}
BuildRequires:  %{python_module pytest-cov >= 4.1}
BuildRequires:  %{python_module pytest-mock >= 3.12}
BuildRequires:  %{python_module pytest-xdist >= 3.3.1}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       tox = %{version}
%endif
%python_subpackages

%description
Tox as is a generic virtualenv management and test command line tool you can
use for:

* checking your package installs correctly with different
  Python versions and interpreters

* running your tests in each of the
  environments, configuring your test tool of choice

* acting as a frontend to Continuous Integration
  servers, greatly reducing boilerplate and merging
  CI and shell-based testing.

%prep
%setup -q -n tox-%{version}
%if %{without devpi_process}
%patch -P 0 -p1
%endif
%patch -P 1 -p1

%build
export LANG=en_US.UTF8
%pyproject_wheel

%install
export LANG=en_US.UTF8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tox
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignores for gh#tox-dev/tox#1293 -- these tests want to install specific wheels (including pytest) into tox envs
# Upstream suggests to  provide them manually to avoid downloading, but with indirect dependencies the number of
# wheels is too large. Plus, defining PIP_NO_INDEX PIP_FIND_LINKS as suggested will be deprecated in a future
# pip and it does not propagate  to the test calling pip themselves without patching.
# enscons are not packaged
donttest+=" or test_provision_missing or test_provision_interrupt_child or test_provision_from_pyvenv"
donttest+=" or test_provision_cli_args_ignore or test_provision_non_canonical_dep"
donttest+=" or test_test_usedevelop"
donttest+=" or test_different_config_cwd"
donttest+=" or test_toxuone_env"
donttest+=" or test_isolated_build_backend_missing_hook"
donttest+=" or test_parallel_live or (test_parallel and not test_parallel_)"
# gh#tox-dev/tox#3011
donttest+=" or test_replace_env_var_circular_flip_flop"
#
donttest+=" or test_call_as_exe or test_skip_pkg_install"
donttest+=" or test_python_generate_hash_seed"
# this test doesn't work on aarch64
donttest+=" or test_bad_env_var"
# this test doesn't work on Leap
donttest+=" or test_package_cmd_builder"
# this test doesn't work on Tumbleweed
donttest+=" or test_package_pyproject or test_package_only"
# gh#tox-dev/tox#3399
donttest+=" or test_skip_develop_mode"

%{python_expand # tests expect an active virtualenv with a clean python name as sys.executable
virtualenv-%{$python_bin_suffix} --system-site-packages testenv-%{$python_bin_suffix}
source testenv-%{$python_bin_suffix}/bin/activate
pip install --no-deps ./build/tox*.whl
python -B -m pytest -v -m "not network" -k "not (${donttest:4})" -n auto
deactivate
}

%post
%python_install_alternative tox

%postun
%python_uninstall_alternative tox

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/tox
%{python_sitelib}/tox-%{version}*-info
%{python_sitelib}/tox

%changelog
