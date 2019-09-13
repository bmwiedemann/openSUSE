#
# spec file for package python-ipywidgets
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
Name:           python-ipywidgets
Version:        7.5.1
Release:        0
Summary:        IPython HTML widgets for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipywidgets
Source0:        https://files.pythonhosted.org/packages/source/i/ipywidgets/ipywidgets-%{version}.tar.gz
# Please make sure you update the documentation files at every release
Source1:        https://media.readthedocs.org/pdf/ipywidgets/stable/ipywidgets.pdf
Source2:        https://media.readthedocs.org/htmlzip/ipywidgets/stable/ipywidgets.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-ipykernel >= 4.5.1
Requires:       python-ipython >= 4
Requires:       python-jsonschema
Requires:       python-traitlets >= 4.3.1
Provides:       python-jupyter_ipywidgets = %{version}
Obsoletes:      python-jupyter_ipywidgets <= %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipykernel >= 4.5.1}
BuildRequires:  %{python_module ipython >= 4}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module nbformat >= 4.2.0}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pickleshare}
BuildRequires:  %{python_module pytest >= 3.6.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module recommonmark}
BuildRequires:  %{python_module traitlets >= 4.3.1}
BuildRequires:  python-mock
# /SECTION
Recommends:     jupyter-widgetsnbextension >= 3.5.0
%ifpython3
Provides:       jupyter-ipywidgets = %{version}
%endif
%python_subpackages

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package     -n python-ipywidgets-doc
Summary:        Documentation for python-jupyter_ipywidgets
Group:          Documentation/Other
Provides:       %{python_module ipywidgets-doc = %{version}}

%description -n python-ipywidgets-doc
Documentation and help files for python-jupyter_ipywidgets.

%prep
%setup -q -n ipywidgets-%{version}
cp %{SOURCE1} .
unzip %{SOURCE2} -d docs
mv docs/ipywidgets-* docs/html
rm docs/html/.buildinfo

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
%{python_sitelib}/ipywidgets-%{version}-py*.egg-info

%files -n python-ipywidgets-doc
%license LICENSE
%doc ipywidgets.pdf
%doc docs/html

%changelog
