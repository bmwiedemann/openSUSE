#
# spec file for package python-iminuit
#
# Copyright (c) 2020 SUSE LLC
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
# Python2 support dropped since version 1.4.0
%define skip_python2 1
Name:           python-iminuit
Version:        1.5.2
Release:        0
Summary:        Python bindings for MINUIT2
License:        MIT
URL:            https://github.com/scikit-hep/iminuit
Source:         https://files.pythonhosted.org/packages/source/i/iminuit/iminuit-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.11.3
Recommends:     python-matplotlib
Recommends:     python-scipy
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# Fix unresolved status for Leap 15.x on account of multiple choices for python3-importlib-metadata (python3-importlib-metadata and python3-importlib_metadata)
BuildRequires:  %{python_module importlib-metadata}
# /SECTION
%python_subpackages

%description
iminuit is a Python interface to the MINUIT2 C++ package.

It can be used as a general function minimization method,
but is most commonly used for likelihood fits of models to data,
and to get model parameter error estimates from likelihood profile analysis.

%prep
%setup -q -n iminuit-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch %{buildroot}%{$python_sitearch}/iminuit

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
