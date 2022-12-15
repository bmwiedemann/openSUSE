#
# spec file for package python-ptpython
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
%define skip_python2 1
Name:           python-ptpython
Version:        3.0.22
Release:        0
Summary:        Python REPL build on top of prompt_toolkit
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/jonathanslenders/ptpython
Source:         https://files.pythonhosted.org/packages/source/p/ptpython/ptpython-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-appdirs
Requires:       python-docopt
Requires:       python-jedi >= 0.9.0
Requires:       python-prompt_toolkit >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jedi >= 0.9.0}
BuildRequires:  %{python_module prompt_toolkit >= 3.0.0}
# /SECTION
Recommends:     python-ptpython-ptipython
%python_subpackages

%description
Ptpython is an advanced Python REPL.

%package ptipython
Summary:        Python REPL build on top of prompt_toolkit - IPython support
Group:          Development/Languages/Python
Requires:       python-ipython
Requires:       python-ptpython

%description ptipython
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
rm %{buildroot}%{_bindir}/pt{,i}python?*
%python_clone -a %{buildroot}%{_bindir}/ptpython
%python_clone -a %{buildroot}%{_bindir}/ptipython

%post
%python_install_alternative ptpython

%post ptipython
%python_install_alternative ptipython

%postun
%python_uninstall_alternative ptpython

%postun ptipython
%python_uninstall_alternative ptipython

%check
# no upstream tests under tests/

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/ptpython

%files %{python_files ptipython}
%license LICENSE
%python_alternative %{_bindir}/ptipython

%changelog
