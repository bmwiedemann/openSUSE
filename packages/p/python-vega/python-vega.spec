#
# spec file for package python-vega
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
%define         skip_python36 1
Name:           python-vega
Version:        3.6.0
Release:        0
Summary:        An IPython/Jupyter widget for Vega 3 and Vega-Lite 2
License:        BSD-3-Clause
URL:            https://github.com/vega/ipyvega/
Source:         https://files.pythonhosted.org/packages/source/v/vega/vega-%{version}.tar.gz
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module pandas >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry >= 0.12}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       python-altair
Requires:       python-ipython
Requires:       python-jupyter-client >= 4.2
Recommends:     python-ipywidgets
Provides:       python-jupyter_vega = %{version}-%{release}
Obsoletes:      python-jupyter_vega < %{version}-%{release}
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
# notebook >= 5.3 does not need to install a separate nbextension
Provides:       jupyter-vega = %{version}-%{release}
Obsoletes:      jupyter-vega < %{version}-%{release}
%endif
# SECTION test requirements
BuildRequires:  %{python_module altair >= 4.0.1}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
IPython/Jupyter notebook module for Vega and Vega-Lite,
Polestar, and Voyager. Notebooks with embedded visualizations
can be viewed on github and nbviewer.

%prep
%setup -q -n vega-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%exclude %{_bindir}/test
%{python_sitelib}/vega/
%{python_sitelib}/vega-%{version}*-info

%changelog
