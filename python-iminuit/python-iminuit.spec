#
# spec file for package python-iminuit
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
Name:           python-iminuit
Version:        1.3.7
Release:        0
Summary:        Python bindings for MINUIT2
License:        MIT
Group:          Development/Languages/Python
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
Suggests:       python-cython
Suggests:       python-matplotlib
Suggests:       python-scipy
# SECTION test requirements
BuildRequires:  %{python_module pytest-runner}
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
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
