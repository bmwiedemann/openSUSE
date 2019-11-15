#
# spec file for package python-ipydatawidgets
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
%define mainver 4.0.1
%define labver  6.2.0
Name:           python-ipydatawidgets
Version:        %{mainver}
Release:        0
Summary:        Jupyter widgets to help facilitate reuse of large datasets
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vidartf/ipydatawidgets
Source:         https://files.pythonhosted.org/packages/py2.py3/i/ipydatawidgets/ipydatawidgets-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module traittypes >= 0.2.0}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  zip
# SECTION test requirements
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       jupyter-ipydatawidgets = %{mainver}
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-notebook
Requires:       python-numpy
Requires:       python-six
Requires:       python-traittypes >= 0.2.0
Provides:       python-jupyter_ipydatawidgets = %{mainver}
Obsoletes:      python-jupyter_ipydatawidgets < %{mainver}
Recommends:     python-ipyscales >= 0.1.1
BuildArch:      noarch
%ifpython3
Requires(post): python3-ipywidgets >= 7.0.0
Requires(post): python3-notebook
Requires(post): python3-numpy
Requires(post): python3-six
Requires(post): python3-traittypes >= 0.2.0
Requires(preun): python3-ipywidgets >= 7.0.0
Requires(preun): python3-notebook
Requires(preun): python3-numpy
Requires(preun): python3-six
Requires(preun): python3-traittypes >= 0.2.0
%endif
%python_subpackages

%description
IPydatawidgets is a set of widgets to help facilitate reuse of large
datasets across different widgets, and different packages.

This package provides the python interface.

%package     -n jupyter-ipydatawidgets
Summary:        Jupyter widgets to help facilitate reuse of large datasets
Requires:       jupyter-notebook
Requires:       python3-ipydatawidgets = %{mainver}

%description -n jupyter-ipydatawidgets
IPydatawidgets is a set of widgets to help facilitate reuse of large
datasets across different widgets, and different packages.

This package provides the jupyter notebook extension.

%package     -n jupyter-ipydatawidgets-jupyterlab
Version:        %{labver}
Summary:        JupyterLab Widgets to help facilitate reuse of large datasets
Requires:       jupyter-jupyterlab
Requires:       jupyter-ipydatawidgets = %{mainver}
Provides:       jupyter_ipydatawidgets_jupyterlab = %{labver}
Obsoletes:      jupyter_ipydatawidgets_jupyterlab < %{labver}

%description -n jupyter-ipydatawidgets-jupyterlab
IPydatawidgets is a set of widgets to help facilitate reuse of large
datasets across different widgets, and different packages.

This package provides the JupyterLab extension.

%prep
%setup -q -T -c
unzip %{SOURCE0} 'ipydatawidgets/*'
find ipydatawidgets/ -type f -name "*.py" -exec sed -i 's/\r$//' {} +
find ipydatawidgets/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
zip -r %{SOURCE0} ipydatawidgets
rm -rf ipydatawidgets

%build
# Not Needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
cp %{buildroot}%{python3_sitelib}/ipydatawidgets-%{mainver}.dist-info/LICENSE.txt .

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%pytest %{buildroot}%{$python_sitelib}/ipydatawidgets/

%files %{python_files}
%license %{python_sitelib}/ipydatawidgets-%{mainver}.dist-info/LICENSE.txt
%{python_sitelib}/ipydatawidgets-%{mainver}*.dist-info/
%{python_sitelib}/ipydatawidgets/

%files -n jupyter-ipydatawidgets
%license LICENSE.txt
%{_jupyter_nbextension_dir}/jupyter-datawidgets/
%config %{_jupyter_nb_notebook_confdir}/jupyter-datawidgets.json

%files -n jupyter-ipydatawidgets-jupyterlab
%license LICENSE.txt
%{_jupyter_labextensions_dir}/jupyterlab-datawidgets-%{labver}.tgz

%changelog
