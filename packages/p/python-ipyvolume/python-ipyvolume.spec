#
# spec file for package python-ipyvolume
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


%define anypython3dist python3dist
%define python3dist_version 0.6
Name:           python-ipyvolume
Version:        0.6.0
Release:        0
Summary:        IPython widget for rendering 3d volumes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/widgetti/ipyvolume
Source:         https://files.pythonhosted.org/packages/source/i/ipyvolume/ipyvolume-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module jupyter_packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyvolume = %{version}
Requires:       python-Pillow
Requires:       python-bqplot
Requires:       python-ipyvue >= 1.7.0
Requires:       python-ipyvuetify
Requires:       python-ipywebrtc
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-pythreejs >= 2.4.0
Requires:       python-requests
Requires:       python-traitlets
Requires:       python-traittypes
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module bqplot}
BuildRequires:  %{python_module ipyvue >= 1.7.0}
BuildRequires:  %{python_module ipyvuetify}
BuildRequires:  %{python_module ipywebrtc}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pythreejs >= 2.4.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module traitlets}
BuildRequires:  %{python_module traittypes}
# /SECTION
%python_subpackages

%description
3d plotting for Python in the Jupyter notebook based on IPython widgets using WebGL.

Ipyvolume currently can
- Do (multi) volume rendering.
- Create scatter plots (up to ~1 million glyphs).
- Create quiver plots (like scatter, but with an arrow pointing in a particular direction).
- Render isosurfaces.
- Do lasso mouse selections.
- Render in the Jupyter notebook, or create a standalone html page (or snippet to embed in your page).
- Render in stereo, for virtual reality with Google Cardboard.
- Animate in d3 style, for instance if the x coordinates or color of a scatter plots changes.
- Animations / sequences, all scatter/quiver plot properties can be a list of arrays, which can represent time snapshots.
- Stylable (although still basic)
- Integrates with
  + ipywidgets for adding gui controls (sliders, button etc), see an example at the documentation homepage
  + bokeh by linking the selection
  + bqplot by linking the selection

This package provides the python interface.

%package     -n jupyter-ipyvolume
Summary:        IPython widget for rendering 3d volumes
Requires:       jupyter-ipywebrtc
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-notebook
Requires:       jupyter-pythreejs >= 2.0.0
Requires:       %{anypython3dist}(ipyvolume) = %{python3dist_version}

%description -n jupyter-ipyvolume
3d plotting for Python in the Jupyter notebook based on IPython widgets using WebGL.

This package provides the jupyter notebook extension.

%package     -n jupyter-jupyterlab-ipyvolume
Summary:        IPython widget for rendering 3d volumes
Requires:       jupyter-ipywebrtc
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-jupyterlab
Requires:       jupyter-pythreejs >= 2.0.0
Requires:       %{anypython3dist}(ipyvolume) = %{python3dist_version}

%description -n jupyter-jupyterlab-ipyvolume
3d plotting for Python in the Jupyter notebook based on IPython widgets using WebGL.

This package provides the jupyterlab extension.

%prep
%setup -q -n ipyvolume-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# no python tests, only typescript which needs network

%files %{python_files}
%doc README.md README.rst
%license LICENSE
%{python_sitelib}/ipyvolume/
%{python_sitelib}/ipyvolume-%{version}.dist-info

%files -n jupyter-ipyvolume
%license LICENSE
%_jupyter_config %{_jupyter_nb_notebook_confdir}/ipyvolume.json
%{_jupyter_nbextension_dir}/ipyvolume/

%files -n jupyter-jupyterlab-ipyvolume
%license LICENSE
%{_jupyter_labextensions_dir3}/ipyvolume

%changelog
