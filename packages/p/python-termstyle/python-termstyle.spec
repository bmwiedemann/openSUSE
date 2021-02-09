#
# spec file for package python-termstyle
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-termstyle
Version:        0.1.11
Release:        0
Summary:        Console colouring for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gfxmonk/termstyle
Source:         https://files.pythonhosted.org/packages/source/t/termstyle/termstyle-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-python-termstyle < %{version}
Provides:       %{oldpython}-python-termstyle = %{version}
%endif
Provides:       python-python-termstyle = %{version}
Obsoletes:      python-python-termstyle < %{version}
%python_subpackages

%description
termstyle is a Python library for adding coloured output to
terminal (console) programs.  The definitions come from ECMA-048, the
"Control Functions for Coded Character Sets" standard.

%prep
%setup -q -n termstyle-%{version}
sed -i '1s/^#!.*//' termstyle.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
PYTHONPATH=. %python_exec -c 'from termstyle import *; print(green("unicod\xe9!"))'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
