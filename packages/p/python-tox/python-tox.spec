#
# spec file for package python-tox
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


Name:           python-tox
Version:        3.26.0
Release:        0
Summary:        Virtualenv-based automation of test activities
License:        MIT
URL:            https://github.com/tox-dev/tox
Source:         https://files.pythonhosted.org/packages/source/t/tox/tox-%{version}.tar.gz
BuildRequires:  %{python_module backports.entry_points_selectable >= 1.0.4}
BuildRequires:  %{python_module filelock >= 3.0.0}
BuildRequires:  %{python_module packaging >= 14}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pluggy >= 0.12.0}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module py >= 1.4.17}
BuildRequires:  %{python_module pytoml >= 0.1}
BuildRequires:  %{python_module setuptools >= 41.0.1}
BuildRequires:  %{python_module setuptools_scm >= 2.0.0}
BuildRequires:  %{python_module six >= 1.14.0}
BuildRequires:  %{python_module toml >= 0.9.4}
BuildRequires:  %{python_module tomli >= 2.0.1}
BuildRequires:  %{python_module virtualenv >= 20.0.8}
BuildRequires:  %{python_module wheel >= 0.29.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  (python3-importlib-metadata >= 0.12 if python3-base < 3.8)
BuildRequires:  (python36-importlib-metadata >= 0.12 if python36-base)
Requires:       python-backports.entry_points_selectable >= 1.0.4
Requires:       python-filelock >= 3.0.0
Requires:       python-packaging >= 14
Requires:       python-pip
Requires:       python-pluggy >= 0.12.0
Requires:       python-py >= 1.4.17
Requires:       python-six >= 1.14.0
Requires:       python-toml >= 0.9.4
Requires:       python-tomli >= 2.0.1
Requires:       python-virtualenv >= 20.0.8
Requires:       (python-importlib-metadata >= 0.12 if python3-base < 3.8)
Requires(post): update-alternatives
Requires(postun):update-alternatives
# last detox version is 0.19
Obsoletes:      python-detox <= 0.19
BuildArch:      noarch
# SECTION setup.cfg [options.extras_requires] testing=
# (except for pytest-cov and -randomly)
BuildRequires:  %{python_module flaky >= 3.4.0}
BuildRequires:  %{python_module freezegun >= 0.3.11}
BuildRequires:  %{python_module psutil >= 5.6.1}
BuildRequires:  %{python_module pytest >= 4.0.0}
BuildRequires:  %{python_module pytest-mock >= 1.10.0}
BuildRequires:  %{python_module pytest-randomly >= 1.0.0}
BuildRequires:  %{python_module pytest-xdist >= 1.22.2}
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

%build
export LANG=en_US.UTF8
%pyproject_wheel

%install
export LANG=en_US.UTF8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tox
%python_clone -a %{buildroot}%{_bindir}/tox-quickstart
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

%{python_expand # tests expect an active virtualenv with a clean python name as sys.executable
virtualenv-%{$python_bin_suffix} --system-site-packages testenv-%{$python_bin_suffix}
source testenv-%{$python_bin_suffix}/bin/activate
pip install --no-deps ./build/tox*.whl
python -B -m pytest -v -m "not network" -k "not (${donttest:4})" -n auto
deactivate
}

%post
%python_install_alternative tox tox-quickstart

%postun
%python_uninstall_alternative tox

%files %{python_files}
%license LICENSE
%doc README.md docs/changelog.rst CONTRIBUTORS CONTRIBUTING.rst
%python_alternative %{_bindir}/tox
%python_alternative %{_bindir}/tox-quickstart
%{python_sitelib}/tox-%{version}*-info
%{python_sitelib}/tox

%changelog
