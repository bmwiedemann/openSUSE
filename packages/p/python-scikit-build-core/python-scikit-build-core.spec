#
# spec file for package python-scikit-build-core
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
Name:           python-scikit-build-core
Version:        0.9.5
Release:        0
Summary:        Build backend for CMake based projects
License:        Apache-2.0
URL:            https://github.com/scikit-build/scikit-build-core
Source0:        https://files.pythonhosted.org/packages/source/s/scikit_build_core/scikit_build_core-%{version}.tar.gz
# PATCH-FIX-UPSTREAM scikit-build-core-pr764-printversion.patch gh#scikit-build/scikit-build-core#764
Patch0:         scikit-build-core-pr764-printversion.patch
# PATCH-FEATURE-OPENSUSE scikit-build-core-offline-wheelhouse.patch provide the testing wheels without runtime download code@bnavigator.de
Patch1:         scikit-build-core-offline-wheelhouse.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging >= 21.3}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       cmake >= 3.15
Requires:       python-packaging >= 21.3
Requires:       python-pathspec >= 0.10.1
Requires:       (python-exceptiongroup >= 1 if python-base < 3.11)
Requires:       (python-importlib-metadata >= 4.13 if python-base < 3.8)
Requires:       (python-importlib-resources >= 1.3 if python-base < 3.9)
Requires:       (python-tomli >= 1.2.2 if python-base < 3.11)
Requires:       (python-typing-extensions >= 3.10.0 if python-base < 3.9)
Recommends:     ninja
Recommends:     python-rich
Provides:       python-scikit_build_core = %{version}-%{release}
# SECTION require runtime
BuildRequires:  %{python_module exceptiongroup >= 1 if %python-base < 3.11}
BuildRequires:  %{python_module importlib-metadata >= 4.13 if %python-base < 3.8}
BuildRequires:  %{python_module importlib-resources >= 1.3 if %python-base < 3.9}
BuildRequires:  %{python_module pathspec >= 0.10.1}
BuildRequires:  %{python_module tomli >= 1.2.2 if %python-base < 3.11}
BuildRequires:  %{python_module typing-extensions >= 3.10.0 if %python-base < 3.9}
BuildRequires:  cmake >= 3.15
BuildArch:      noarch
# /SECITON
# SECTION test requirements
BuildRequires:  %{python_module build >= 0.8}
BuildRequires:  %{python_module cattrs >= 22.2.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distlib >= 0.3.5}
BuildRequires:  %{python_module pybind11-devel >= 2.11}
BuildRequires:  %{python_module pytest >= 7.2}
BuildRequires:  %{python_module pytest-subprocess >= 1.5.0}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv >= 20.20}
BuildRequires:  %{python_module wheel}
BuildRequires:  gcc-c++
BuildRequires:  ninja
# /SECTION
%python_subpackages

%description
Python CMake adaptor and Python API for plugins

Features over classic Scikit-build:
  - Better warnings, errors, and logging
  - No warning about unused variables
  - Automatically adds Ninja and/or CMake only as required
  - No dependency on setuptools, distutils, or wheel in build mode.
  - Powerful config system, including config options support in build mode.
  - Automatic inclusion of site-packages in CMAKE_PREFIX_PATH
  - FindPython is backported if running on CMake < 3.24 (included via hatchling in a submodule, configurable)
  - Limited API / Stable ABI and pythonless tags supported via config option
  - No slow generator search, ninja/make or MSVC used by default, respects CMAKE_GENERATOR
  - SDists are reproducible by default (UNIX, Python 3.9+)

%package pyproject
Summary:        The scikit_build_core[pyproject] extra
Requires:       python-scikit-build-core = %{version}
Provides:       python-scikit_build_core-pyproject = %{version}-%{release}

%description pyproject
Python CMake adaptor and Python API for plugins: The extra requirement to build PEP518 wheels and sdists

%prep
%autosetup -p1 -n scikit_build_core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# A writable temp dir is required for some tests
mkdir ./tmp
export PYTEST_DEBUG_TEMPROOT=./tmp
# no wheel dependencies for isolated build provided
donttestmark="isolated"
# different hash due to different build environment:
donttest="test_pep517_sdist_hash or test_pep518_sdist"
%pytest -m "not ($donttestmark)" -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/scikit_build_core
%{python_sitelib}/scikit_build_core-%{version}.dist-info

%files %{python_files pyproject}
%license LICENSE
%doc README.md

%changelog
