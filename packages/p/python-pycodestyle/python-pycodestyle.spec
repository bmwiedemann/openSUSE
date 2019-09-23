#
# spec file for package python-pycodestyle
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
%define oldpython python
Name:           python-pycodestyle
Version:        2.5.0
Release:        0
Summary:        Python style guide checker
License:        MIT
Group:          Development/Languages/Python
Url:            https://pycodestyle.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/p/pycodestyle/pycodestyle-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-pep8 = %{version}
Obsoletes:      %{oldpython}-pep8 < %{version}
%endif
Provides:       python-pep8 = %{version}
Obsoletes:      python-pep8 < %{version}
%python_subpackages

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in `PEP 8`.

This package used to be called ``pep8`` but was renamed to ``pycodestyle``
to reduce confusion.

%prep
%setup -q -n pycodestyle-%{version}
%autopatch -p1
sed -ri '1s/^#!.*//' pycodestyle.py

%build
%python_build

%install
%python_install
%python_clone %{buildroot}%{_bindir}/pycodestyle
ln -sf pycodestyle-%{python3_bin_suffix} %{buildroot}%{_bindir}/pycodestyle

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/pycodestyle
%{_bindir}/pycodestyle-%{python_bin_suffix}
%{python_sitelib}/*

%changelog
