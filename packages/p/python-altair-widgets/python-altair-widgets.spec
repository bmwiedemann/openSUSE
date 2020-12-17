#
# spec file for package python-altair-widgets
#
# Copyright (c) 2020 SUSE LLC
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
# The test suite is not packaged in the PyPI package. The tests available on
# GitHub require pytest-ipynb which is not available on openSUSE and was
# abandoned upstream
%bcond_with     test
Name:           python-altair-widgets
Version:        0.2.2
Release:        0
Summary:        Interactive visualization package for statistical data for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://altair-viz.github.io
Source:         https://files.pythonhosted.org/packages/source/a/altair_widgets/altair_widgets-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-altair >= 2.0.0
Requires:       python-ipython
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-pandas
Requires:       python-vega >= 0.4.4
Provides:       python-jupyter_altair-widgets = %{version}
Obsoletes:      python-jupyter_altair-widgets <= %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module altair >= 2.0.0}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-ipynb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module vega >= 0.4.4}
%endif
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-altair-widgets = %{version}
%endif
%python_subpackages

%description
This package provides interactive data visualization tools in the Jupyter
Notebook.

The interactive visualization tool that is provided allows data selection
through HTML widgets and outputs a Vega-lite plot through Altair. In the HTML
widget it is possible to select columns to plot in various encodings. This
widget also supports some basic configuration (i.e., log vs linear scales).

%prep
%setup -q -n altair_widgets-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest altair_widgets
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/altair_widgets/
%{python_sitelib}/altair_widgets-%{version}-py*.egg-info

%changelog
