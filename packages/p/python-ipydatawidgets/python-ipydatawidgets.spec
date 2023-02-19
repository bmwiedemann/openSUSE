#
# spec file for package python-ipydatawidgets
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


%define mainver 4.3.2
%define labver  7.1.2
%define jupver  5.5.2
Name:           python-ipydatawidgets
Version:        %{mainver}
Release:        0
Summary:        Jupyter widgets to help facilitate reuse of large datasets
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vidartf/ipydatawidgets
Source0:        https://files.pythonhosted.org/packages/py2.py3/i/ipydatawidgets/ipydatawidgets-%{mainver}-py2.py3-none-any.whl
# PATCH-FIX-UPSTREAM ipydatawidgets-pr56-traitlets-fix.patch gh#ipydatawidgets/pull#56
Patch0:         ipydatawidgets-pr56-traitlets-fix.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module traittypes >= 0.2.0}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       jupyter-ipydatawidgets = %{jupver}
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-numpy
Requires:       python-traittypes >= 0.2.0
Provides:       python-jupyter_ipydatawidgets = %{mainver}
Obsoletes:      python-jupyter_ipydatawidgets < %{mainver}
BuildArch:      noarch
%python_subpackages

%description
IPydatawidgets is a set of widgets to help facilitate reuse of large
datasets across different widgets, and different packages.

This package provides the python interface.

%package     -n jupyter-ipydatawidgets
Version:        %{jupver}
Release:        0
Summary:        Jupyter widgets to help facilitate reuse of large datasets
Group:          Development/Languages/Python
Requires:       jupyter-notebook
Provides:       jupyter-datawidgets = %{jupver}
Requires:       python3-ipydatawidgets = %{mainver}

%description -n jupyter-ipydatawidgets
IPydatawidgets is a set of widgets to help facilitate reuse of large
datasets across different widgets, and different packages.

This package provides the jupyter notebook extension.

%package     -n jupyter-ipydatawidgets-jupyterlab
Version:        %{labver}
Release:        0
Summary:        JupyterLab Widgets to help facilitate reuse of large datasets
Group:          Development/Languages/Python
Requires:       jupyter-ipydatawidgets = %{jupver}
Requires:       jupyter-jupyterlab
Provides:       jupyter-datawidgets-jupyterlab = %{labver}
Provides:       jupyter_ipydatawidgets_jupyterlab = %{labver}
Obsoletes:      jupyter_ipydatawidgets_jupyterlab < %{labver}

%description -n jupyter-ipydatawidgets-jupyterlab
IPydatawidgets is a set of widgets to help facilitate reuse of large
datasets across different widgets, and different packages.

This package provides the JupyterLab extension.

%prep
%setup -q -T -c

%build
# Not needed: we must use the prebundled jsfiles from the published wheel

%install
%pyproject_install %{SOURCE0}
%{jupyter_move_config}
%{python_expand pushd %{buildroot}%{$python_sitelib}
find ipydatawidgets/ -type f -name "*.py" -exec sed -i 's/\r$//' {} +
find ipydatawidgets/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
patch --no-backup-if-mismatch -p1 < %{PATCH0}
%{$python_compile}
%fdupes %{buildroot}%{$python_sitelib}
popd
}
%fdupes %{buildroot}%{_jupyter_prefix}
cp %{buildroot}%{python3_sitelib}/ipydatawidgets-%{mainver}.dist-info/LICENSE.txt .

%check
export LANG=en_US.UTF-8
%pytest --pyargs ipydatawidgets

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/ipydatawidgets-%{mainver}*.dist-info/
%{python_sitelib}/ipydatawidgets/

%files -n jupyter-ipydatawidgets
%license LICENSE.txt
%{_jupyter_nbextension_dir}/jupyter-datawidgets/
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyter-datawidgets.json

%files -n jupyter-ipydatawidgets-jupyterlab
%license LICENSE.txt
%{_jupyter_labextensions_dir}/jupyterlab-datawidgets-%{labver}.tgz
%dir %{_jupyter_prefix}/labextensions
%{_jupyter_prefix}/labextensions/jupyterlab-datawidgets

%changelog
