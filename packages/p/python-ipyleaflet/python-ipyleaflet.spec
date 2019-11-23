#
# spec file for package python-ipyleaflet
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
Name:           python-ipyleaflet
Version:        0.11.4
Release:        0
Summary:        A Jupyter widget for dynamic Leaflet maps
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipyleaflet
Source:         https://files.pythonhosted.org/packages/py2.py3/i/ipyleaflet/ipyleaflet-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyleaflet = %{version}
Requires:       python-branca >= 0.3.1
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-notebook
Requires:       python-traittypes >= 0.2.1
Requires:       python-xarray >= 0.10
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module branca >= 0.3.1}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module traittypes >= 0.2.1}
BuildRequires:  %{python_module xarray >= 0.10}
# /SECTION
%python_subpackages

%description
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipyleaflet
Summary:        Interactive plotting package for the Jupyter notebook
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-notebook
Requires:       python3-ipyleaflet = %{version}

%description -n jupyter-ipyleaflet
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

This package provides the jupyter notebook extension.

%prep
%setup -q -c -T

%build
# Not Needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}

%{jupyter_move_config}
cp %{buildroot}%{python3_sitelib}/ipyleaflet-%{version}.dist-info/LICENSE .
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%files %{python_files}
%{python_sitelib}/ipyleaflet/
%{python_sitelib}/ipyleaflet-%{version}.dist-info/
%license %{python_sitelib}/ipyleaflet-%{version}.dist-info/LICENSE

%files -n jupyter-ipyleaflet
%license LICENSE
%{_jupyter_nb_notebook_confdir}/jupyter-leaflet.json
%{_jupyter_nbextension_dir}/jupyter-leaflet/

%changelog
