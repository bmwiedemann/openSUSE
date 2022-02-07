#
# spec file for package python-PyCBC
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


%bcond_without tests

# Python2 no longer supported by PyCBC
%define skip_python2 1

%define modname PyCBC
Name:           python-PyCBC
Version:        2.0.1
Release:        0
Summary:        Core library to analyze gravitational-wave data
License:        GPL-3.0-or-later
URL:            http://www.pycbc.org/
Source0:        https://github.com/gwastro/pycbc/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-astropy
Requires:       python-beautifulsoup4
Requires:       python-decorator
Requires:       python-h5py
Requires:       python-lal
Requires:       python-lalframe
Requires:       python-lalpulsar
Requires:       python-lalsimulation
Requires:       python-ligo-lw
Requires:       python-ligo-segments
Requires:       python-lscsoft-glue
Requires:       python-numpy
Requires:       python-requests
Requires:       python-scipy
Requires:       python-tqdm
Recommends:     python-gwdatafind
Recommends:     python-ligo-segments
ExclusiveArch:  x86_64
%if %{with tests}
# SECTION Test Requirements
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module gwdatafind}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module lalframe}
BuildRequires:  %{python_module lalpulsar}
BuildRequires:  %{python_module lalsimulation}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module ligo-lw}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module lscsoft-glue}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mpld3}
BuildRequires:  %{python_module pyFFTW}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module tqdm}
# /SECTION
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
%python_build

%install
%python_install
sed -E -i "1 s|^#\!\s*/usr/bin/env\s*bash|#\!/bin/bash|" %{buildroot}%{_bindir}/run_pycbc_inference

%python_expand chmod -x %{buildroot}%{$python_sitearch}/pycbc/results/static/js/fancybox/2.1.5/jquery.fancybox*.js

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
# Tests that either require network or don't work due to unpackaged modules
rm -fr \
   examples/workflow/data_checker/daily_test.py \
   test/test_calibration.py \
   test/test_chisq.py \
   test/test_distributions.py \
   test/test_dq.py \
   test/test_fft*.py \
   test/test_frame.py \
   test/test_frequencyseries.py \
   test/test_infmodel.py

%{python_expand pushd test # for tests
export PYTHONPATH=%{buildroot}%{$python_sitearch}
export PYTHONDONTWRITEBYTECODE=1
pytest-%{$python_version}
popd
}
%endif

%files -n %{modname}-utils
%{_bindir}/*

%files %{python_files}
%{python_sitearch}/pycbc/
%{python_sitearch}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
