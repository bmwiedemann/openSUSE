#
# spec file for package python-vispy
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


%define demodatacommit 5a3db84
%define test_data_tag test-data-10
Name:           python-vispy
Version:        0.14.3
Release:        0
Summary:        Interactive visualization in Python
License:        BSD-3-Clause
URL:            https://github.com/vispy/vispy
Source0:        https://files.pythonhosted.org/packages/source/v/vispy/vispy-%{version}.tar.gz
Source1:        https://github.com/vispy/demo-data/archive/%{demodatacommit}.tar.gz#/vispy-demo-data-%{demodatacommit}.tar.gz
# `git clone https://github.com/vispy/test-data test-data; pushd test-data; git bundle create ../vispy-test-data-10.bundle test-data-10; popd`
Source2:        vispy-%{test_data_tag}.bundle
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 7.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       fontconfig
Requires:       python-freetype-py
Requires:       python-hsluv
Requires:       python-kiwisolver
Requires:       python-numpy
Requires:       python-packaging
Recommends:     python-Pillow
Recommends:     python-PySDL2
Recommends:     python-ipython
Recommends:     python-meshio
Recommends:     python-pyglet
Suggests:       python-qt5
Suggests:       python-PyQt6
Suggests:       python-wxPython
# SECTION test requirements
BuildRequires:  %{python_module hsluv}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module PySDL2}
BuildRequires:  %{python_module freetype-py}
BuildRequires:  %{python_module ipython if %python-base >= 3.10}
BuildRequires:  %{python_module kiwisolver}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pyglet}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  fontconfig
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

%prep
%autosetup -p1 -n vispy-%{version}
sed -i '1{/^#!\/usr\/bin\/env /d;}' \
    vispy/glsl/build_spatial_filters.py \
    vispy/util/transforms.py \
    vispy/visuals/collections/util.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export HOME=$PWD/vispytesthome
mkdir $HOME
pushd $HOME
# The demo data for tests
mkdir -p .vispy/data
tar -x --strip-components=1 -f %{SOURCE1} -C .vispy/data
git clone %{SOURCE2} .vispy/test_data
pushd .vispy/test_data
git checkout -b main %{test_data_tag}
popd
# we can't test file downloading from online resources
donttest="test_config"
# avoid vtk: not multiflavor
donttest="$donttest or (test_io and test_meshio)"
# segfault in xvfb test environment
donttest="$donttest or test_run"
%pytest_arch -rsfE --pyargs vispy -k "not ($donttest)"
popd

%files %{python_files}
%doc *.rst *.md
%license LICENSE.txt
%{python_sitearch}/vispy
%{python_sitearch}/vispy-%{version}.dist-info

%changelog
