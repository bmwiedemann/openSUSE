#
# spec file for package python-pyFFTW
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
%ifarch %{ix86} x86_64
%bcond_without  test
%else
%bcond_with     test
%endif
Name:           python-pyFFTW
Version:        0.11.1
Release:        0
Summary:        A pythonic wrapper around FFTW, the FFT library
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://hgomersall.github.com/pyFFTW/
Source:         https://files.pythonhosted.org/packages/source/p/pyFFTW/pyFFTW-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.6}
BuildRequires:  %{python_module scipy >= 0.12.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-threads-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.6
Requires:       python-scipy >= 0.12.0

%python_subpackages

%description
pyFFTW is a pythonic wrapper around the FFTW libary.
An interface for all the possible transforms that FFTW can perform is provided.

Both the complex DFT and the real DFT are supported, as well as arbitrary
axes of abitrary shaped and strided arrays, which makes it almost
feature equivalent to standard and real FFT functions of ``numpy.fft`` 
(indeed, it supports the ``clongdouble`` dtype which ``numpy.fft`` does not).

Operating FFTW in multithreaded mode is supported.

A comprehensive unittest suite can be found with the source on the github 
repository.

%prep
%setup -q -n pyFFTW-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand find %{buildroot}%{$python_sitearch}/pyfftw/ -name "*.py" -exec sed -i "s|^#!/usr/bin/env python$|#!%__$python|" {} \; -exec grep -q "^#!%__$python$" {} \; -exec chmod a+x {} \;
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/pyfftw/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/pyfftw/
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with test}
%check
%{python_expand $python setup.py build_ext --inplace
$python setup.py test
$python setup.py clean
}
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
