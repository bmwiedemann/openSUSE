#
# spec file for package python-pyparallel
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyparallel
Version:        0.2.2
Release:        0
# For license file
%define tag     b33995136e433839cb5cd139214d02c7c6dd2008
Summary:        Python Parallel Port Extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/pyserial/pyparallel
Source:         https://files.pythonhosted.org/packages/source/p/pyparallel/pyparallel-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/pyserial/pyparallel/%{tag}/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
This module encapsulates the access for the parallel port. It provides
backends for Python running on Windows and Linux.

%prep
%setup -q -n pyparallel-%{version}
sed -i -e '/^#!\//, 1d' parallel/parallelppdev.py
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
