#
# spec file for package python-PyCBC
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

# Python2 no longer supported by PyCBC
%define skip_python2 1

%define modname PyCBC
Name:           python-PyCBC%{psuffix}
Version:        2.2.0
Release:        0
Summary:        Core library to analyze gravitational-wave data
License:        GPL-3.0-or-later
URL:            http://www.pycbc.org/
Source0:        https://github.com/gwastro/pycbc/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= 1.16.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# Note: The definitive specification is setup.py, not requirements.txt!
Requires:       python-Cython >= 0.29
Requires:       python-Jinja2
Requires:       python-Mako >= 1.0.1
Requires:       python-Pillow
Requires:       python-astropy >= 2.0.3
Requires:       python-beautifulsoup4 >= 4.6.0
Requires:       python-gwdatafind
Requires:       python-h5py >= 3.0
# SECTION lalsuite, see below
Requires:       python-lal
Requires:       python-lalframe
Requires:       python-lalpulsar
Requires:       python-lalsimulation
# /SECTION
Requires:       python-ligo-lw >= 1.7.0
Requires:       python-ligo-segments
Requires:       python-lscsoft-glue
Requires:       python-matplotlib >= 1.5.1
Requires:       python-mpld3 >= 0.3
Requires:       python-numpy >= 1.16.0
Requires:       python-pegasus-wms.api >= 5.0.1
Requires:       python-scipy >= 0.16
Requires:       python-tqdm
Conflicts:      python-astropy = 4.0.5
Conflicts:      python-astropy = 4.2.1
Conflicts:      python-lal = 7.2
Conflicts:      python-numpy = 1.19.0
ExclusiveArch:  x86_64
%if %{with test}
BuildRequires:  %{python_module PyCBC = %{version}}
BuildRequires:  %{python_module pyFFTW}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
PyCBC is a software package used to explore astrophysical sources of
gravitational waves. It contains algorithms to analyze
gravitational-wave data from the LIGO and Virgo detectors, detect
coalescing compact binaries, and measure the astrophysical parameters
of detected sources.

%package -n %{modname}-utils
Summary:        PyCBC utilities to analyze gravitational-wave data
Requires:       python3-PyCBC = %{version}
Obsoletes:      python3-%{modname} <= 1.18.0
BuildArch:      noarch

%description -n %{modname}-utils
PyCBC is a software package used to explore astrophysical sources of
gravitational waves. It contains algorithms to analyze
gravitational-wave data from the LIGO and Virgo detectors, detect
coalescing compact binaries, and measure the astrophysical parameters
of detected sources.

This package provides PyCBC utility programs that are built against
the default python3 flavour.

%prep
%autosetup -p1 -n pycbc-%{version}
# there is no python metadata in the distribution to provide "lalsuite"
sed -i '/lalsuite/d' setup.py

# FOR REAL EXECUTABLES SET HASHBANG TO PYTHON3 DIRECTLY
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
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
sed -E -i "1 s|^#\!\s*/usr/bin/env\s*bash|#\!/bin/bash|" %{buildroot}%{_bindir}/run_pycbc_inference

%python_expand chmod -x %{buildroot}%{$python_sitearch}/pycbc/results/static/js/fancybox/2.1.5/jquery.fancybox*.js

%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# Tests that either require network or require special setups
# can't use pytest --ignore because of a special arg parser in test/utils.py
rm -r \
   test/test_chisq.py \
   test/test_dq.py \
   test/test_fft_mkl_threaded.py \
   test/test_fftw_openmp.py \
   test/test_frame.py \
   test/test_live_coinc_compare.py \
   test/test_infmodel.py \
   test/test_skymax.py \
   test/test_tmpltbank.py \
   %{nil}

pushd test
%{python_expand # can't use the macro because of a special arg parser in test/utils.py
export PYTHONDONTWRITEBYTECODE=1
pytest-%{$python_bin_suffix}
}
popd
%endif

%if !%{with test}
%files -n %{modname}-utils
%{_bindir}/pycbc_*
%{_bindir}/run_pycbc_inference

%files %{python_files}
%{python_sitearch}/pycbc
%{python_sitearch}/%{modname}-%{version}*-info
%endif

%changelog
