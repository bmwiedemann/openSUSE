#
# spec file for package python-nbindex-jupyter
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
Name:           python-nbindex-jupyter
Version:        0.2.25
Release:        0
License:        BSD-3-Clause
Summary:        Jupyter Notebook additions
Url:            https://github.com/l-althueser/nbindex-jupyter
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/n/nbindex-jupyter/nbindex-jupyter-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-ipython
%ifpython3
Provides:       jupyter-nbindex-jupyter = %{version}
%endif
BuildArch:      noarch

%python_subpackages

%description
Javascript based Jupyter Notebook additions (Table of Content, hide code, Figure numbers, ...)

%prep
%setup -q -n nbindex-jupyter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
