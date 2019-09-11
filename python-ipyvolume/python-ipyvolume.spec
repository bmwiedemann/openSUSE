#
# spec file for package python-ipyvolume
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
%define         skip_python2 1
Name:           python-ipyvolume
Version:        0.5.2
Release:        0
Summary:        IPython widget for rendering 3d volumes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/maartenbreddels/ipyvolume
Source:         https://files.pythonhosted.org/packages/source/i/ipyvolume/ipyvolume-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyvolume = %{version}
Requires:       python-Pillow
Requires:       python-ipywebrtc
Requires:       python-ipywidgets >= 7.5.0
Requires:       python-notebook
Requires:       python-numpy
Requires:       python-pythreejs >= 2.0.0
Requires:       python-requests
Requires:       python-traittypes
Requires:       python-traitlets
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module ipywebrtc}
BuildRequires:  %{python_module ipywidgets >= 7.5.0}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pythreejs >= 2.0.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module traittypes}
BuildRequires:  %{python_module traitlets}
# /SECTION
%python_subpackages

%description
IPython widget for rendering 3d volumes and glyphs (e.g. scatter and quiver)
in the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipyvolume
Summary:        IPython widget for rendering 3d volumes
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-ipywebrtc
Requires:       jupyter-notebook
Requires:       jupyter-pythreejs >= 2.0.0
Requires:       python3-ipyvolume = %{version}

%description -n jupyter-ipyvolume
IPython widget for rendering 3d volumes and glyphs (e.g. scatter and quiver)
in the Jupyter notebook.

This package provides the jupyter notebook extension.

%prep
%setup -q -n ipyvolume-%{version}

%build
%python_build

%install
%python_install
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md README.rst
%license LICENSE
%{python_sitelib}/ipyvolume/
%{python_sitelib}/ipyvolume-%{version}-py*.egg-info

%files -n jupyter-ipyvolume
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/ipyvolume.json
%{_jupyter_nbextension_dir}/ipyvolume/

%changelog
