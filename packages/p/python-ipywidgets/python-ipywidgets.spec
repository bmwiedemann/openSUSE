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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-ipywidgets
Version:        7.6.5
Release:        0
Summary:        IPython HTML widgets for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipywidgets
Source0:        https://files.pythonhosted.org/packages/source/i/ipywidgets/ipywidgets-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ipywidgets-pr2655-collectionsabc.patch -- gh#jupyter-widgets/ipywidgets#2655
Patch0:         https://github.com/jupyter-widgets/ipywidgets/commit/f9a13dbb3b8f1ffefef483bdb4c14f04f7743ff1.patch#/ipywidgets-pr2655-collectionsabc.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-ipykernel >= 4.5.1
Requires:       python-ipython >= 4
Requires:       python-ipython_genutils >= 0.2
Requires:       python-jupyterlab_widgets >= 1
Requires:       python-nbformat >= 4.2
Requires:       python-traitlets >= 4.3.1
Requires:       python-widgetsnbextension >= 3.5.0
Provides:       python-jupyter_ipywidgets = %{version}
Obsoletes:      python-jupyter_ipywidgets < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipykernel >= 4.5.1}
BuildRequires:  %{python_module ipython >= 4}
BuildRequires:  %{python_module ipython_genutils >= 0.2}
BuildRequires:  %{python_module jupyterlab_widgets >= 1}
BuildRequires:  %{python_module nbformat >= 4.2.0}
BuildRequires:  %{python_module pytest >= 3.6.0}
BuildRequires:  %{python_module traitlets >= 4.3.1}
BuildRequires:  %{python_module widgetsnbextension >= 3.5.0}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-ipywidgets = %{version}
%endif
%python_subpackages

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%prep
%autosetup -p1 -n ipywidgets-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipywidgets/
%{python_sitelib}/ipywidgets-%{version}*-info

%changelog
