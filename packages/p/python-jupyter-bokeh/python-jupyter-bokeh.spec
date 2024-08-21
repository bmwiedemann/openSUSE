#
# spec file for package python-jupyter-bokeh
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


# .0 s get truncated
%define distver 4.0.5
Name:           python-jupyter-bokeh
Version:        4.0.5
Release:        0
Summary:        A Jupyter extension for rendering Bokeh content
License:        BSD-3-Clause
URL:            https://github.com/bokeh/jupyter_bokeh
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_bokeh/jupyter_bokeh-%{version}.tar.gz
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatch-nodejs-version}
BuildRequires:  %{python_module hatchling >= 1.5.0}
BuildRequires:  %{python_module jupyterlab >= 4.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-bokeh = %{version}-%{release}
Requires:       (python-bokeh >= 3 with python-bokeh < 4)
Requires:       (python-ipywidgets >= 8 with python-ipywidgets < 9)
Provides:       python-jupyter_bokeh = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module bokeh >= 3 with %python-bokeh < 4}
BuildRequires:  %{python_module ipywidgets >= 8 with %python-ipywidgets < 9}
# /SECTION
%python_subpackages

%description
A Jupyter extension for rendering Bokeh content within Jupyter.

%package -n jupyter-bokeh
Summary:        A Jupyter extension for rendering Bokeh content -- jupyter files
Requires:       python3dist(jupyter-bokeh) = %{distver}
Suggests:       python3-jupyter-bokeh

%description -n jupyter-bokeh
A Jupyter extension for rendering Bokeh content within Jupyter.

This package provides the jupyter labextension

%prep
%autosetup -p1 -n jupyter_bokeh-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# no upstream python tests

%files -n jupyter-bokeh
%{_jupyter_labextensions_dir3}/@bokeh

%files %{python_files}
%{python_sitelib}/jupyter_bokeh
%{python_sitelib}/jupyter_bokeh-%{version}.dist-info

%changelog
