#
# spec file for package python-PyWavelets
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
%define         skip_python2 1
# no python36-numpy in Tumbleweed (NEP 29)
%define         skip_python36 1
%define         skip_python37 1
Name:           python-PyWavelets
Version:        1.4.1
Release:        0
Summary:        PyWavelets is a Python wavelet transforms module
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/PyWavelets/pywt
Source0:        https://files.pythonhosted.org/packages/source/P/PyWavelets/PyWavelets-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.17.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-numpy >= 1.17.3
Provides:       python-PyWavelets-doc = %{version}
Obsoletes:      python-PyWavelets-doc < %{version}
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
%setup -q -n PyWavelets-%{version}
sed -i -e '/^#!\//, 1d' pywt/tests/*.py

# Fix wrong-script-interpreter
find demo -name '*.py' -exec sed -i "s|#!%{_bindir}/env python|#!%__python3|"  {} \;

# Remove unneeded shebangs
sed -i '1{\@^#!%{_bindir}/env python@d}' pywt/data/create_dat.py

# Remove unneeded executable bits
for lib in test_concurrent test_data test_deprecations test_doc test_matlab_compatibility test_matlab_compatibility_cwt test_thresholding data/generate_matlab_data data/generate_matlab_data_cwt ; do
   chmod a-x pywt/tests/$lib.py
done

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
# Fix wrong-script-interpreter
%python_expand sed -i "s|#!%{_bindir}/env python.*$|#!%{_bindir}$python|" %{buildroot}%{$python_sitearch}/pywt/tests/*.py
%{python_compileall}
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
%{python_sitearch}/PyWavelets-%{version}-py*.egg-info

%changelog
