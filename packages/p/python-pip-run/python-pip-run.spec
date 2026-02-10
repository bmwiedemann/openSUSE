#
# spec file for package python-pip-run
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
# Disables installing nbformat for tests in Ring1 (see also Patch1)
%bcond_with ringdisabled
# Do not depend on nbformat for SLES or SLFO:Main
%if ( 0%{?suse_version} == 1500 && 0%{?sle_version} >= 150400 ) || 0%{?suse_version} == 1600
%bcond_without ringdisabled
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pip-run%{psuffix}
Version:        16.1.0
Release:        0
Summary:        Install packages and run Python with them
License:        MIT
URL:            https://github.com/jaraco/pip-run
Source:         https://files.pythonhosted.org/packages/source/p/pip-run/pip_run-%{version}.tar.gz
# Needs the wheels for path and path.py for testing
Source10:       https://files.pythonhosted.org/packages/py3/p/path.py/path.py-12.5.0-py3-none-any.whl
Source11:       https://files.pythonhosted.org/packages/py3/p/path/path-16.4.0-py3-none-any.whl
# PATCH-FEATURE-OPENSUSE pip-run-suse-ring1-no-nbformat.patch code@bnavigator.de -- Don't test with nbformat if not available
Patch1:         pip-run-suse-ring1-no-nbformat.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-autocommand
Requires:       python-coherent.deps
Requires:       python-jaraco.context
Requires:       python-jaraco.env
Requires:       python-jaraco.functools >= 3.7
Requires:       python-more-itertools
Requires:       python-packaging
Requires:       python-path >= 15.1
Requires:       python-pip >= 19.3
Requires:       python-platformdirs
Requires:       python-tempora
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module jaraco.path}
BuildRequires:  %{python_module pip-run = %{version}}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  python3-setuptools-wheel
%if %{without ringdisabled}
BuildRequires:  %{python_module nbformat}
%endif
%endif
%python_subpackages

%description
On-demand temporary package installation for a single interpreter run.

pip-run is not intended to solve production dependency management,
but does aim to address the other, one-off scenarios around dependency management
  - trials and experiments
  - build setup
  - test runners
  - just in time script running
  - interactive development
  - bug triage

pip-run is a compliment to Pip and Virtualenv and Setuptools, intended to more
readily address the on-demand needs.

%prep
%autosetup -p1 -n pip_run-%{version}

%if %{without ringdisabled}
sed -i -e '/nbformat/d' setup.cfg
%endif

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pip-run
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
mkdir -p wheels
cp %{SOURCE10} %{SOURCE11} wheels/
export PIP_FIND_LINKS="%{python3_sitelib}/../wheels $PWD/wheels"
# requires DNS resolution
dont_test="DepsReader.infer or test_pkg_loaded_from_url"
dont_test+=" or read-deps.run or persist.clean_if_older"
%pytest -m "not network" -k "not ($dont_test)"
%endif

%pre
%python_libalternatives_reset_alternative pip-run

%post
%python_install_alternative pip-run

%postun
%python_uninstall_alternative pip-run

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst NEWS.rst
%python_alternative %{_bindir}/pip-run
%{python_sitelib}/pip-run.py
%pycache_only %{python_sitelib}/__pycache__/pip-run*.pyc
%{python_sitelib}/pip_run
%{python_sitelib}/pip_run-%{version}.dist-info
%endif

%changelog
