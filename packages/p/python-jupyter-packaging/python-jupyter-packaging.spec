#
# spec file for package python-jupyter-packaging
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
Name:           python-jupyter-packaging
Version:        0.4.0
Release:        0
License:        BSD-3-Clause
Summary:        Jupyter Packaging Utilities
Url:            https://github.com/jupyter/jupyter-packaging
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-packaging/jupyter-packaging-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
This package contains utilities for making Python packages
with and without accompanying JavaScript packages

%prep
%setup -q -n jupyter-packaging-%{version}
sed -i 's/\r$//' README.md
sed -i -e '/^#!\//, 1d' jupyter_packaging/*.py

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
%{python_sitelib}/*

%changelog
