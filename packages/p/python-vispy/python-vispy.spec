#
# spec file for package python-vispy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  ext_deps
Name:           python-vispy
Version:        0.6.2
Release:        0
Summary:        Interactive visualization in Python
License:        BSD-3-Clause
URL:            https://github.com/vispy/vispy
Source:         https://files.pythonhosted.org/packages/source/v/vispy/vispy-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm_git_archive}
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
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pyglet}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module scipy}
BuildRequires:  fontconfig
%if %{with ext_deps}
BuildRequires:  %{python_module cassowary}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module freetype-py}
BuildRequires:  %{python_module husl}
BuildRequires:  %{python_module pypng}
BuildRequires:  %{python_module six}
%endif
# /SECTION
%if %{with ext_deps}
Requires:       python-cassowary
Requires:       python-decorator
Requires:       python-freetype-py
Requires:       python-husl
Requires:       python-pypng
Requires:       python-six
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
sed -i -e '/^#!\//, 1d' vispy/glsl/build-spatial-filters.py vispy/util/transforms.py vispy/visuals/collections/util.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/*

%files -n jupyter-vispy
%license LICENSE.txt
%config %{_jupyter_nb_notebook_confdir}/vispy.json
%{_jupyter_nbextension_dir}/vispy/

%changelog
