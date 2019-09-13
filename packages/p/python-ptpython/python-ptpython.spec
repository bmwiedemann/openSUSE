#
# spec file for package python-ptpython
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
Name:           python-ptpython
Version:        2.0.4
Release:        0
Summary:        Python REPL build on top of prompt_toolkit
License:        ISC
Group:          Development/Languages/Python
Url:            https://github.com/jonathanslenders/ptpython
Source:         https://files.pythonhosted.org/packages/source/p/ptpython/ptpython-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module jedi >= 0.9.0}
BuildRequires:  %{python_module prompt_toolkit >= 2.0.6}
# /SECTION
Requires:       python-Pygments
Requires:       python-docopt
Requires:       python-jedi >= 0.9.0
Requires:       python-prompt_toolkit >= 2.0.6
%ifpython3
Recommends:     python3-ptpython-ptipython
%endif
BuildArch:      noarch

%python_subpackages

%description
Ptpython is an advanced Python REPL.

%package     -n python3-ptpython-ptipython
Summary:        Python REPL build on top of prompt_toolkit - IPython support
Group:          Development/Languages/Python
Requires:       python3-ipython
Requires:       python3-ptpython

%description -n python3-ptpython-ptipython
Ptpython is an advanced Python REPL.

This package provides IPython support to Ptpython.

%prep
%setup -q -n ptpython-%{version}
sed -i -e '/^#!\//, 1d' ptpython/entry_points/run_*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

rm %{buildroot}%{_bindir}/ptpython
rm %{buildroot}%{_bindir}/ptipython
rm %{buildroot}%{_bindir}/ptipython2*

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%python2_only %{_bindir}/ptpython2*
%python3_only %{_bindir}/ptpython3*
%{python_sitelib}/*

%files -n python3-ptpython-ptipython
%license LICENSE
%{_bindir}/ptipython3*

%changelog
