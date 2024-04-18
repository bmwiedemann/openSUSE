#
# spec file for package python-meson-python
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
Name:           python-meson-python
Version:        0.15.0
Release:        0
Summary:        Meson Python build backend (PEP 517)
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source0:        https://files.pythonhosted.org/packages/source/m/meson_python/meson_python-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE mesonpy-trim-deps.patch code@bnavigator.de
Patch11:        mesonpy-trim-deps.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata >= 0.7.1}
BuildRequires:  %{python_module tomli >= 1.0.0 if %python-base < 3.11}
BuildRequires:  fdupes
BuildRequires:  meson >= 1.2.3
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
%if 0%{python_version_nodots} >= 312
Requires:       meson >= 1.2.3
%else
Requires:       meson >= 0.63.3
%endif
Requires:       python-pyproject-metadata >= 0.7.1
%if 0%{python_version_nodots} < 311
Requires:       python-tomli >= 1.0.0
%endif
# SECTION test
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  patchelf
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
meson-python is a Python build backend built on top of the Meson build system.
It enables using Meson for the configuration and build steps of Python packages.
meson-python is best suited for building Python packages containing extension
modules implemented in languages such as C, C++, Cython, Fortran, Pythran, or Rust.

%prep
%autosetup -p1 -n meson_python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test suite path issues
donttest="test_vendored_meson"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/mesonpy
%{python_sitelib}/meson_python-%{version}*-info

%changelog
