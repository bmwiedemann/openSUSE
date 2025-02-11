#
# spec file for package python-py-build-cmake
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-py-build-cmake
Version:        0.4.1
Release:        0
Summary:        Modern, PEP 517 compliant build backend for creating Python packages with
License:        MIT
URL:            https://github.com/tttapa/py-build-cmake
Source:         https://github.com/tttapa/py-build-cmake/archive/refs/tags/%{version}.tar.gz#/py-build-cmake-%{version}-gh.tar.gz
BuildRequires:  %{python_module click >= 8.1.3   with %python-click < 8.2}
BuildRequires:  %{python_module distlib >= 0.3.5 with %python-distlib < 0.4}
BuildRequires:  %{python_module flit-core >= 3.7 with %python-flit-core < 4}
BuildRequires:  %{python_module lark}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       cmake
Requires:       (python-click >= 8.1.3 with python-click < 8.2)
Requires:       (python-distlib >= 0.3.5 with python-distlib < 0.4)
Requires:       (python-flit-core >= 3.7 with python-flit-core < 4)
%if 0%{?python_version_nodots} < 311
Requires:       (python-tomli >= 1.2.3 with python-tomli < 3)
%endif
Requires:       python-lark
Requires:       python-pyproject-metadata
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PEP 517 compliant build backend for creating Python packages with extensions built using CMake.

## Features

 - Building and packaging C, C++ or Fortran extension modules for Python using CMake
 - Declarative configuration using `pyproject.toml` (PEP 621), compatible with flit
 - Editable/development installations for Python modules (PEP 660)
 - Compatible with pybind11 and nanobind
 - Stub generation for type checking and autocompletion
 - Customizable CMake configuration, build and installation options
 - Support for multiple installation configurations and components
 - Cross-compilation support
 - No dependency on setuptools
 - Compatible with cibuildwheel for building Wheels

%prep
%autosetup -p1 -n py-build-cmake-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/py-build-cmake
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative py-build-cmake

%postun
%python_uninstall_alternative py-build-cmake

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/py-build-cmake
%{python_sitelib}/py_build_cmake
%{python_sitelib}/py_build_cmake-%{version}.dist-info

%changelog
