#
# spec file for package python-PyWavelets
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
Name:           python-PyWavelets
Version:        1.0.3
Release:        0
Summary:        PyWavelets is a Python wavelet transforms module
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/PyWavelets/pywt
Source0:        https://files.pythonhosted.org/packages/source/P/PyWavelets/PyWavelets-%{version}.tar.gz
Source10:       https://media.readthedocs.org/pdf/pywavelets/v%{version}/pywavelets.pdf
Source11:       https://media.readthedocs.org/htmlzip/pywavelets/v%{version}/pywavelets.zip
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.9.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
Requires:       python-numpy >= 1.9.1
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

%package     -n %{name}-doc
Summary:        This package contains the HMTL documentation of %{name}
Group:          Documentation/Other
Provides:       %{python_module PyWavelets-doc = %{version}}

%description -n %{name}-doc
PyWavelets is a Python wavelet transforms module that can do:

  * 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
  * 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
  * 1D and 2D Wavelet Packet decomposition and reconstruction
  * Computing Approximations of wavelet and scaling functions
  * Over seventy built-in wavelet filters and support for custom wavelets
  * Single and double precision calculations
  * Results compatibility with Matlab Wavelet Toolbox

This Package contains the documentation of %{name} in HTML and PDF formats.

%prep
%setup -q -n PyWavelets-%{version}
sed -i -e '/^#!\//, 1d' pywt/tests/*.py

cp %{SOURCE10} .
unzip %{SOURCE11} -d docs
mv docs/pywavelets-* docs/html
rm docs/html/.buildinfo

# Make docs non-executable
chmod a-x *.rst
chmod a-x PyWavelets.egg-info/*

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

%{python_expand pushd %{buildroot}%{$python_sitearch}
# Fix wrong-script-interpreter
sed -i "s|#!%{_bindir}/env python|#!%__$python|" pywt/tests/*.py
# Deduplicating files can generate a RPMLINT warning for pyc mtime
$python -m compileall -d %{$python_sitearch} pywt/tests/
$python -O -m compileall -d %{$python_sitearch} pywt/tests/
%fdupes .
popd
}

%check
mkdir test
pushd test
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B -c 'import pywt;pywt.test()'
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pywt/
%{python_sitearch}/PyWavelets-%{version}-py*.egg-info

%files -n %{name}-doc
%license LICENSE
%doc pywavelets.pdf
%doc docs/html

%changelog
