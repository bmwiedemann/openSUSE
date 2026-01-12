#
# spec file for package python-ipyleaflet
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


%define distversion 0.20
Name:           python-ipyleaflet
Version:        0.20.0
Release:        0
Summary:        A Jupyter widget for dynamic Leaflet maps
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipyleaflet
Source:         https://files.pythonhosted.org/packages/source/i/ipyleaflet/ipyleaflet-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-branca >= 0.5.0
Requires:       python-xyzservices >= 2021.8.1
Requires:       (python-ipywidgets >= 7.6.0 with python-ipywidgets < 9)
Requires:       (python-jupyter_leaflet >= 0.20 with python-jupyter_leaflet < 0.21)
Requires:       (python-traittypes >= 0.2.1 with python-traittypes < 3)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.6.0 with %python-ipywidgets < 9}
BuildRequires:  %{python_module branca >= 0.5.0}
BuildRequires:  %{python_module jupyter_leaflet >= 0.20 with %python-jupyter_leaflet < 0.21}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module nbclassic}
BuildRequires:  %{python_module traittypes >= 0.2.1 with %python-traittypes < 3}
BuildRequires:  %{python_module xyzservices >= 2021.8.1}
# /SECTION
%python_subpackages

%description
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

%prep
%setup -q -n ipyleaflet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # no python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import ipyleaflet'
jupyter-%{$python_bin_suffix} nbclassic-extension list 2>&1 | grep 'jupyter-leaflet.*enabled'
jupyter-%{$python_bin_suffix} labextension list 2>&1 | grep 'jupyter-leaflet.*enabled'
}

%files %{python_files}
%license LICENSE
%{python_sitelib}/ipyleaflet/
%{python_sitelib}/ipyleaflet-%{version}.dist-info/

%changelog
