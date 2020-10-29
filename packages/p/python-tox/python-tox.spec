#
# spec file for package python-tox
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-tox
Version:        3.18.0
Release:        0
Summary:        Virtualenv-based automation of test activities
License:        MIT
URL:            https://github.com/tox-dev/tox
Source:         https://files.pythonhosted.org/packages/source/t/tox/tox-%{version}.tar.gz
BuildRequires:  %{python_module filelock >= 3.0.0}
BuildRequires:  %{python_module flaky >= 3.4.0}
BuildRequires:  %{python_module freezegun >= 0.3.11}
BuildRequires:  %{python_module importlib-metadata >= 0.12}
BuildRequires:  %{python_module pathlib2 >= 2.3.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pluggy >= 0.12.0}
BuildRequires:  %{python_module py >= 1.4.17}
BuildRequires:  %{python_module pytest >= 4.0.0}
BuildRequires:  %{python_module pytest-cov >= 2.5.1}
BuildRequires:  %{python_module pytest-mock >= 1.10.0}
BuildRequires:  %{python_module pytest-xdist >= 1.22.2}
BuildRequires:  %{python_module setuptools >= 41.0.1}
BuildRequires:  %{python_module setuptools_scm >= 2.0.0}
BuildRequires:  %{python_module six >= 1.14.0}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module virtualenv >= 16.0.0}
BuildRequires:  %{python_module wheel >= 0.29.0}
BuildRequires:  fdupes
# we need python2 interpreter in tests for venv calls checks
# even on python3 variant
BuildRequires:  python-base
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-filelock >= 3.0.0
Requires:       python-importlib-metadata >= 0.12
Requires:       python-packaging >= 17.1
Requires:       python-pluggy >= 0.12.0
Requires:       python-py >= 1.4.17
Requires:       python-setuptools >= 30.0.0
Requires:       python-six >= 1.14.0
Requires:       python-toml >= 0.9.4
Requires:       python-virtualenv >= 16.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python-detox
BuildArch:      noarch
%ifpython3
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

%package -n %{name}-doc
Summary:        Documentation for tox, a virtualenv-based test automation
Recommends:     %{python_module tox = %{version}}
Provides:       %{python_module tox-doc = %{version}}

%description -n %{name}-doc
Tox as is a generic virtualenv management and test command line tool you can
use for:

* checking your package installs correctly with different
  Python versions and interpreters

* running your tests in each of the
  environments, configuring your test tool of choice

* acting as a frontend to Continuous Integration
  servers, greatly reducing boilerplate and merging
  CI and shell-based testing.

This is the HTML documentation for tox package.

%prep
%setup -q -n tox-%{version}
# remove cmdline test as they exec tox binary that is alternatived by us
rm -f tests/unit/test_z_cmdline.py

%build
export LANG=en_US.UTF8
%pyproject_wheel

%install
export LANG=en_US.UTF8
%pyproject_install
for B in tox tox-quickstart ; do
    %python_clone -a %{buildroot}%{_bindir}/$B
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PATH=%{buildroot}%{_bindir}:$PATH
# Ignores for gh#tox-dev/tox#1293
# test_dist_exists_version_change test_verbose_isolated_build: need python2* deps even on python3
# test_spinner_stdout_not_unicode breaks with changes in monkeypatch in pytest
rm tests/unit/util/test_spinner.py
%pytest -k 'not (network or parallel or test_provision_missing or test_provision_interrupt_child or test_workdir_gets_resolved or test_provision_cli_args_ignore or test_provision_non_canonical_dep or test_create_KeyboardInterrupt or test_provision_from_pyvenv or test_verbose_isolated_build or test_dist_exists_version_change)'

%post
%python_install_alternative tox tox-quickstart

%postun
%python_uninstall_alternative tox

%files %{python_files}
%license LICENSE
%doc README.md docs/changelog.rst CONTRIBUTORS CONTRIBUTING.rst
%python_alternative %{_bindir}/tox
%python_alternative %{_bindir}/tox-quickstart
%{python_sitelib}/tox-%{version}*
%{python_sitelib}/tox

%changelog
