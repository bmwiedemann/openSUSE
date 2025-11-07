#
# spec file for package python-pybgcode
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define pyversion 0.2.0
Name:           python-pybgcode
# Use the set_version source service for adjusting the field below
Version:        0.2.0+git20240829.b5c57c4
Release:        0
Summary:        Python bindings for libbgcode
License:        AGPL-3.0-only
URL:            https://github.com/prusa3d/libbgcode
Source0:        libbgcode-%{version}.tar.xz
Source1:        pyproject.opensuse.toml
Source99:       python-pybgcode.rpmlintrc
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py-build-cmake >= 0.1.8}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  boost-devel >= 1.78
BuildRequires:  c++_compiler
BuildRequires:  git-core
BuildRequires:  libboost_nowide-devel >= 1.78
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(LibBGCode) = %{pyversion}
%python_subpackages

%description
A new G-code file format featuring the following improvements over the legacy G-code:
1) Block structure with distinct blocks for metadata vs. G-code
2) Faster navigation
3) Coding & compression for smaller file size
4) Checksum for data validity
5) Extensivity through new (custom) blocks. For example, a file signature block may be welcome by corporate customers.

This package provides the Python language bindings for LibBGCode

%prep
%setup -q -n libbgcode-%{version}
cp %{SOURCE1} ./
sed -i 's/@optflags@/%{optflags}/' pyproject.opensuse.toml

%build
export PIP_CONFIG_SETTINGS=--local=pyproject.opensuse.toml
%pyproject_wheel

%install
%pyproject_install

%check
mv pybgcode/pybgcode pybgcode/pybgcode.movedaway
cp tests/data/mini_cube_b_ref.gcode test.gcode
%pytest_arch

%files %{python_files}
%license LICENSE
%{python_sitearch}/pybgcode
%{python_sitearch}/pybgcode-%{pyversion}.dist-info

%changelog
