#
# spec file for package python-pip-run
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

Name:           python-pip-run%{psuffix}
Version:        8.8.2
Release:        0
Summary:        Install packages and run Python with them
License:        MIT
URL:            https://github.com/jaraco/pip-run
Source:         https://files.pythonhosted.org/packages/source/p/pip-run/pip-run-%{version}.tar.gz
# Needs the wheels for path and path.py for testing
Source10:       https://files.pythonhosted.org/packages/py3/p/path.py/path.py-12.5.0-py3-none-any.whl
Source11:       https://files.pythonhosted.org/packages/py3/p/path/path-16.4.0-py3-none-any.whl
# PATCH-FEATURE-OPENSUSE pip-run-suse-ring1-no-nbformat.patch code@bnavigator.de -- Don't test with nbformat if not available
Patch1:         pip-run-suse-ring1-no-nbformat.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-autocommand
Requires:       python-packaging
Requires:       python-path >= 15.1
Requires:       python-pip >= 19.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
%if %{with test}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module pip-run = %{version}}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  ca-certificates
%if %{without ringdisabled}
BuildRequires:  %{python_module nbformat}
%endif
%endif
BuildArch:      noarch
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
%autosetup -p1 -n pip-run-%{version}

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
export PIP_FIND_LINKS=$PWD/wheels/
dont_test=""
%pytest -k "$dont_test"
%endif

%post
%python_install_alternative pip-run

%postun
%python_uninstall_alternative pip-run

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.rst
%python_alternative %{_bindir}/pip-run
%{python_sitelib}/pip-run.py*
%pycache_only %{python_sitelib}/__pycache__/pip-run*.pyc
%{python_sitelib}/pip_run
%{python_sitelib}/pip_run-%{version}*-info
%endif

%changelog
