#
# spec file for package python-plotly
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
Name:           python-plotly
Version:        4.12.0
Release:        0
Summary:        Library for collaborative, interactive, publication-quality graphs
License:        MIT
URL:            https://github.com/plotly/plotly.py
Source:         https://files.pythonhosted.org/packages/source/p/plotly/plotly-%{version}.tar.gz
Source100:      python-plotly-rpmlintrc
BuildRequires:  %{python_module decorator >= 4.0.6}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module nbformat >= 4.2}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module retrying >= 1.3.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4.0.6
Requires:       python-pytz
Requires:       python-requests
Requires:       python-retrying >= 1.3.3
Requires:       python-six
Recommends:     python-matplotlib >= 1.3.1
Recommends:     python-numpy
Recommends:     python-pandas
BuildArch:      noarch
%python_subpackages

%description
Use this package to make collaborative, interactive,
publication-quality graphs from Python on https://plot.ly.

Plotly is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

%package        jupyter
Summary:        Jupyter notebook integration for %{name}
Requires:       %{name} = %{version}
Requires:       jupyter-plotly = %{version}
Requires:       python-ipython
Requires:       python-ipywidgets
Requires:       python-nbformat >= 4.2
Requires:       python-notebook

%description    jupyter
Use this package to make collaborative, interactive,
publication-quality graphs from Python on https://plot.ly.

Plotly is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

This package provides Jupyter Notebook integration and widgets.

%package     -n jupyter-plotly
Summary:        Jupyter notebook integration for %{name}
Requires:       jupyter-ipython
Requires:       jupyter-ipywidgets
Requires:       jupyter-nbformat >= 4.2
Requires:       jupyter-notebook
Requires:       python3-plotly-jupyter = %{version}

%description -n jupyter-plotly
Use this package to make collaborative, interactive,
publication-quality graphs from Python on https://plot.ly.

Plotly is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

This package provides Jupyter Notebook integration and widgets.

%prep
%setup -q -n plotly-%{version}

%build
%python_build

%install
%python_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{jupyter_prefix}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/_plotly_future_/
%{python_sitelib}/_plotly_utils/
%{python_sitelib}/plotly/
%{python_sitelib}/plotly-%{version}-py*.egg-info

%files %{python_files jupyter}
%license LICENSE.txt
%{python_sitelib}/plotlywidget/

%files -n jupyter-plotly
%license LICENSE.txt
%{_jupyter_nbextension_dir}/plotlywidget/
%config %{_jupyter_nb_notebook_confdir}/plotlywidget.json

%changelog
