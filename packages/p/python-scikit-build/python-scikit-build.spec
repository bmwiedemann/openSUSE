#
# spec file for package python-scikit-build
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
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%{?sle15_python_module_pythons}
Name:           python-scikit-build%{psuffix}
Version:        0.18.1
Release:        0
Summary:        Improved build system generator for Python C/C++/Fortran/Cython extensions
License:        MIT
URL:            https://github.com/scikit-build/scikit-build
Source:         https://files.pythonhosted.org/packages/source/s/scikit-build/scikit_build-%{version}.tar.gz
Source99:       sample-setup.cfg
# PATCH-FIX-UPSTREAM scikit-build-pr1120-upddistutils.patch gh#scikit-build/scikit-build#1120
Patch0:         scikit-build-pr1120-upddistutils.patch
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       cmake >= 3.5
Requires:       python-distro
Requires:       python-packaging
Requires:       python-setuptools >= 42.0.0
Requires:       python-wheel >= 0.32.0
%if %{python_version_nodots} < 38
Requires:       python-typing-extensions >= 3.7
%endif
%if %{python_version_nodots} < 311
Requires:       python-tomli
%endif
%if %{with test}
# Note: When tests fail try `osc build ---clean` in order to get rid of remnant numpy typing stubs in $HOME
BuildRequires:  %{python_module Cython >= 0.25.1}
BuildRequires:  %{python_module build >= 0.7}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.21}
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module pytest-mock >= 1.10.4}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-build = %{version}}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  git-core
BuildRequires:  ninja
%endif
BuildArch:      noarch
%python_subpackages

%description
Improved build system generator for Python C/C++/Fortran/Cython extensions

%prep
%autosetup -p1 -n scikit_build-%{version}
%if %{with test}
# some tests call setup.py develop|install|test, which by default write to /usr
# This is not allowed in OBS
# gh#scikit-build/scikit-build#469
%python_expand mkdir -p /tmp/fakepythonroot%{$python_sitelib}
cp %{S:99} tests/samples/hello-cpp/setup.cfg
cp %{S:99} tests/samples/cython-flags/setup.cfg
cp %{S:99} tests/samples/issue-274-support-default-package-dir/setup.cfg
cp %{S:99} tests/samples/issue-274-support-one-package-without-package-dir/setup.cfg
cp %{S:99} tests/samples/issue-334-configure-cmakelist-non-cp1252-encoding/setup.cfg
%endif

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# these tests need a wheelhouse with downloaded wheels including platform dependent cmake
donttestmarker="isolated"
# setuptools_scm is a dependency of hatch_vcs
donttestmarker+=" or nosetuptoolsscm"
%pytest -m "not ($donttestmarker)"
%endif

%if !%{with test}
%files %{python_files}
%doc AUTHORS.rst README.rst CONTRIBUTING.rst docs/
%license LICENSE
%{python_sitelib}/skbuild
%{python_sitelib}/scikit_build-%{version}.dist-info
%endif

%changelog
