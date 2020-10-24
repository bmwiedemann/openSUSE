#
# spec file for package python-PyCBC
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


Name:           python-PyCBC
Version:        1.16.11
Release:        0
Summary:        Core library to analyze gravitational-wave data
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://www.pycbc.org/
Source:         https://files.pythonhosted.org/packages/source/P/PyCBC/PyCBC-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy >= 1.16.0}
BuildRequires:  %{python_module numpy-devel >= 1.16.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-astropy
Requires:       python-beautifulsoup4
Requires:       python-decorator
Requires:       python-h5py
Requires:       python-numpy >= 1.16.0
Requires:       python-requests
Requires:       python-scipy
Requires:       python-tqdm
Recommends:     python-emcee
Recommends:     python-gwdatafind
Recommends:     python-lal
Recommends:     python-lalframe
Recommends:     python-lalsimulation
Recommends:     python-ligo-segments
ExclusiveArch:  %{ix86} x86_64
%python_subpackages

%description
PyCBC is a software package used to explore astrophysical sources of
gravitational waves. It contains algorithms to analyze
gravitational-wave data from the LIGO and Virgo detectors, detect
coalescing compact binaries, and measure the astrophysical parameters
of detected sources.

%prep
%setup -q -n PyCBC-%{version}

# FOR REAL BINARIES SET HASHBANG TO PYTHON3 DIRECTLY
sed -E -i "1{s|^#\!\s*/usr/bin/env python|#\!%{_bindir}/python3|}" \
  bin/pycbc_* \
  bin/*/pycbc_*

# FOR FILES NOT INSTALLED TO BINDIR, REMOVE HASHBANGS
sed -E -i "1{/^#\!\s*\/usr\/bin/d}" \
  pycbc/fft/fft_callback.py \
  pycbc/filter/fotonfilter.py \
  pycbc/psd/*.py \
  pycbc/results/*.py

%build
%python_build

%install
%python_install
sed -E -i "1 s|^#\!\s*/usr/bin/env\s*bash|#\!/bin/bash|" %{buildroot}%{_bindir}/run_pycbc_inference

%python_expand chmod -x %{buildroot}%{$python_sitearch}/pycbc/results/static/js/fancybox/2.1.5/jquery.fancybox.js
%python_expand chmod -x %{buildroot}%{$python_sitearch}/pycbc/results/static/js/fancybox/2.1.5/jquery.fancybox.pack.js

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%python3_only %{_bindir}/*
%{python_sitearch}/pycbc/
%{python_sitearch}/PyCBC-%{version}-py%{python_version}.egg-info/

%changelog
