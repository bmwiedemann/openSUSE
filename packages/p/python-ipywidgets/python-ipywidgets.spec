#
# spec file for package python-ipywidgets
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-ipywidgets
Version:        8.0.4
Release:        0
Summary:        IPython HTML widgets for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipywidgets
Source0:        https://files.pythonhosted.org/packages/source/i/ipywidgets/ipywidgets-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-ipykernel >= 4.5.1
Requires:       python-ipython >= 6.1.0
Requires:       python-ipython_genutils >= 0.2
Requires:       python-traitlets >= 4.3.1
Requires:       (python-jupyterlab_widgets >= 3.0 with python-jupyterlab_widgets < 4)
Requires:       (python-widgetsnbextension >= 4.0 with python-widgetsnbextension < 5)
Provides:       python-jupyter_ipywidgets = %{version}
Obsoletes:      python-jupyter_ipywidgets < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipykernel >= 4.5.1}
BuildRequires:  %{python_module ipython >= 6.1.0}
BuildRequires:  %{python_module ipython_genutils >= 0.2}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module jupyterlab_widgets >= 3 with %python-jupyterlab_widgets < 4}
BuildRequires:  %{python_module pytest >= 3.6.0}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module traitlets >= 4.3.1}
BuildRequires:  %{python_module widgetsnbextension >= 4.0 with %python-widgetsnbextension < 5}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-ipywidgets = %{version}
%endif
%python_subpackages

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%prep
%autosetup -p1 -n ipywidgets-%{version}
# remove shebangs from test modules. Those are not standalone scripts.
sed -i '1{/env python/d}' ipywidgets/widgets/tests/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipywidgets/
%{python_sitelib}/ipywidgets-%{version}*-info

%changelog
