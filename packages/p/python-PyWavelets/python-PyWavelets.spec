#
# spec file for package python-PyWavelets
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-PyWavelets
Version:        1.6.0
Release:        0
Summary:        PyWavelets is a Python wavelet transforms module
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/PyWavelets/pywt
Source0:        https://files.pythonhosted.org/packages/source/P/PyWavelets/pywavelets-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.0.4}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module meson-python >= 0.15}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       (python-numpy >= 1.22.4 with python-numpy < 3)
Provides:       python-PyWavelets-doc = %{version}
Obsoletes:      python-PyWavelets-doc < %{version}
Provides:       python-pywavelets = %{version}-%{release}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyWavelets is a Python wavelet transforms module that can do:

  * 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
  * 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
  * 1D and 2D Wavelet Packet decomposition and reconstruction
  * Computing Approximations of wavelet and scaling functions
  * Over seventy built-in wavelet filters and support for custom wavelets
  * Single and double precision calculations
  * Results compatibility with Matlab Wavelet Toolbox

%prep
%autosetup -p1 -n pywavelets-%{version}
sed -i '1{/env python/d}' pywt/tests/*.py pywt/data/create_dat.py
chmod -x pywt/data/create_dat.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir temp
mv pywt temp/pywt
# Accuracy is platform-dependent
%pytest_arch --ignore=temp -k 'not test_accuracy_precomputed_cwt' %{buildroot}%{$python_sitearch}/pywt/
mv temp/pywt pywt

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pywt/
%{python_sitearch}/pywavelets-%{version}.dist-info

%changelog
