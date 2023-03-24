#
# spec file for package python-vispy
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


%bcond_without  ext_deps
Name:           python-vispy
Version:        0.12.2
Release:        0
Summary:        Interactive visualization in Python
License:        BSD-3-Clause
URL:            https://github.com/vispy/vispy
Source:         https://files.pythonhosted.org/packages/source/v/vispy/vispy-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       fontconfig
Requires:       python-numpy
Requires:       python-qt5
Recommends:     python-PySDL2
Recommends:     python-imageio
Recommends:     python-jupyter_ipython
Recommends:     python-networkx
Recommends:     python-opengl
Recommends:     python-opengl-accelerate
Recommends:     python-pyglet
Recommends:     python-pypng
Recommends:     python-scipy
# SECTION test requirements
BuildRequires:  %{python_module PySDL2}
BuildRequires:  %{python_module glfw}
BuildRequires:  %{python_module hsluv}
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pyglet}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module scipy}
BuildRequires:  fontconfig
%if %{with ext_deps}
BuildRequires:  %{python_module cassowary}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module freetype-py}
BuildRequires:  %{python_module husl}
BuildRequires:  %{python_module pypng}
%endif
# /SECTION
%if %{with ext_deps}
Requires:       python-cassowary
Requires:       python-decorator
Requires:       python-freetype-py
Requires:       python-husl
Requires:       python-pypng
%endif
%python_subpackages

%description
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

%package     -n jupyter-vispy
Summary:        Interactive visualization in the Jupyter notebook
Requires:       jupyter-notebook
Requires:       python3-vispy = %{version}

%description -n jupyter-vispy
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

This package provides the jupyter notebook extension.

%prep
%setup -q -n vispy-%{version}
%if %{with ext_deps}
rm -rf vispy/ext/_bundled
%endif

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
# cd because of gh#vispy/vispy#1506 (they are not src-based)
cd vispy/testing
%pytest_arch

%files %{python_files}
%doc *.rst *.md
%license LICENSE.txt
%{python_sitearch}/vispy
%{python_sitearch}/vispy-%{version}*-info

%changelog
