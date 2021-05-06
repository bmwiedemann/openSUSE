#
# spec file for package python-PyCBC
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


%bcond_without tests

%define modname PyCBC
Name:           python-PyCBC
Version:        1.18.0
Release:        0
Summary:        Core library to analyze gravitational-wave data
License:        GPL-3.0-or-later
URL:            http://www.pycbc.org/
Source0:        https://github.com/gwastro/pycbc/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy >= 1.16.0
BuildRequires:  python3-numpy-devel >= 1.16.0
BuildRequires:  python3-setuptools
Requires:       python3-astropy
Requires:       python3-beautifulsoup4
Requires:       python3-decorator
Requires:       python3-h5py
Requires:       python3-lal
Requires:       python3-lalframe
Requires:       python3-lalpulsar
Requires:       python3-lalsimulation
Requires:       python3-ligo-lw
Requires:       python3-ligo-segments
Requires:       python3-lscsoft-glue
Requires:       python3-numpy >= 1.16.0
Requires:       python3-requests
Requires:       python3-scipy
Requires:       python3-tqdm
Recommends:     python3-gwdatafind
Recommends:     python3-ligo-segments
ExclusiveArch:  %{ix86} x86_64
%if %{with tests}
# SECTION Test Requirements
BuildRequires:  python3-Mako
BuildRequires:  python3-astropy
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-decorator
BuildRequires:  python3-gwdatafind
BuildRequires:  python3-h5py
BuildRequires:  python3-lal
BuildRequires:  python3-lalframe
BuildRequires:  python3-lalpulsar
BuildRequires:  python3-lalsimulation
BuildRequires:  python3-ligo-lw
BuildRequires:  python3-ligo-segments
BuildRequires:  python3-lscsoft-glue
BuildRequires:  python3-matplotlib
BuildRequires:  python3-mpld3
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-testsuite
BuildRequires:  python3-tqdm
# /SECTION
%endif

%description
PyCBC is a software package used to explore astrophysical sources of
gravitational waves. It contains algorithms to analyze
gravitational-wave data from the LIGO and Virgo detectors, detect
coalescing compact binaries, and measure the astrophysical parameters
of detected sources.

%package -n python3-%{modname}
Summary:        Core library to analyze gravitational-wave data

%description -n python3-%{modname}
PyCBC is a software package used to explore astrophysical sources of
gravitational waves. It contains algorithms to analyze
gravitational-wave data from the LIGO and Virgo detectors, detect
coalescing compact binaries, and measure the astrophysical parameters
of detected sources.

%prep
%autosetup -p1 -n pycbc-%{version}
sed -i "/emcee==/d" setup.py
sed -i "s/,<1.19//" setup.py

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
%python3_build

%install
%python3_install
sed -E -i "1 s|^#\!\s*/usr/bin/env\s*bash|#\!/bin/bash|" %{buildroot}%{_bindir}/run_pycbc_inference

chmod -x %{buildroot}%{python3_sitearch}/pycbc/results/static/js/fancybox/2.1.5/jquery.fancybox.js
chmod -x %{buildroot}%{python3_sitearch}/pycbc/results/static/js/fancybox/2.1.5/jquery.fancybox.pack.js

%fdupes %{buildroot}%{python3_sitearch}

%if %{with tests}
%check
# Delete tests requiring network
rm test/test_dq.py examples/workflow/data_checker/daily_test.py
# Broken tests
rm test/fft_base.py \
   test/test_array.py \
   test/test_chisq.py \
   test/test_fft_unthreaded.py \
   test/test_fftw_openmp.py \
   test/test_fftw_pthreads.py \
   test/test_frame.py \
   test/test_frequencyseries.py \
   test/test_schemes.py \
   test/test_skymax.py \
   test/test_timeseries.py
pushd test
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYTHONDONTWRITEBYTECODE=1
python3 -m unittest
popd
%endif

%files -n python3-%{modname}
%{_bindir}/*
%{python3_sitearch}/pycbc/
%{python3_sitearch}/%{modname}-%{version}-py%{python3_version}.egg-info/

%changelog
