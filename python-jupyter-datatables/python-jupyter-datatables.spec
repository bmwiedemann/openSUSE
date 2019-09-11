#
# spec file for package python-jupyter-datatables
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter-datatables
Version:        0.3.1
Release:        0
License:        MIT
Summary:        Jupyter Notebook extension to levarage pandas DataFrames
Url:            https://github.com/CermakM/jupyter-datatables
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-datatables/jupyter-datatables-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-require}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scipy}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
Requires:       python-ipython
Requires:       python-ipykernel
Requires:       python-jupyter-require
Requires:       python-pandas
Requires:       python-scipy

%python_subpackages

%description
Jupyter Notebook extension to levarage pandas DataFrames
by integrating DataTables JS.

%prep
%setup -q -n jupyter-datatables-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
