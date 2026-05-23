#
# spec file for package python-gwpy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-gwpy
Version:        4.0.1
Release:        0
Summary:        A python package for gravitational-wave astrophysics
License:        GPL-3.0-only
URL:            https://gwpy.github.io/
Source0:        https://files.pythonhosted.org/packages/source/g/gwpy/gwpy-%{version}.tar.gz
Source1:        python-gwpy.rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 4.3.0
Requires:       python-dateparser
Requires:       python-dqsegdb2
Requires:       python-gwdatafind >= 1.1.0
Requires:       python-gwosc >= 0.5.3
Requires:       python-h5py >= 3
Requires:       python-igwn-ligolw
Requires:       python-igwn-segments
Requires:       python-ligotimegps >= 1.2.1
Requires:       python-matplotlib >= 3.3.0
Requires:       python-numpy >= 1.17
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       python-scipy >= 1.2.0
Requires:       python-tqdm >= 4.10.0
Recommends:     python-PyCBC
Recommends:     python-PyMySQL
Recommends:     python-lalsimulation
Recommends:     python-lscsoft-glue
Suggests:       python-inspiral-range
BuildArch:      noarch
# SECTION test requirements
# BuildRequires:  %%{python_module PyCBC} -- optional, not available on aarch64
BuildRequires:  %{python_module PyMySQL}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module astropy >= 4.3.0}
BuildRequires:  %{python_module awkward}
BuildRequires:  %{python_module dateparser}
BuildRequires:  %{python_module dqsegdb2}
BuildRequires:  %{python_module gwdatafind >= 1.1.0}
BuildRequires:  %{python_module gwosc >= 0.5.3}
BuildRequires:  %{python_module h5py >= 3}
BuildRequires:  %{python_module igwn-ligolw}
BuildRequires:  %{python_module igwn-segments}
BuildRequires:  %{python_module lalframe}
BuildRequires:  %{python_module ldas-tools-al-swig}
BuildRequires:  %{python_module ligotimegps >= 1.2.1}
BuildRequires:  %{python_module lscsoft-glue}
BuildRequires:  %{python_module matplotlib >= 3.3.0}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module pytest-freezegun}
BuildRequires:  %{python_module pytest-socket}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy >= 1.2.0}
BuildRequires:  %{python_module tqdm >= 4.10.0}
BuildRequires:  %{python_module uproot}
BuildRequires:  %{python_module xxhash}
# extra not defined upstream but needed for tests
BuildRequires:  %{python_module ligo-lw}
# /SECTION
# Unsupported archs by upstream
ExcludeArch:    %{ix86}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
GWpy is a collaboration-driven Python package providing tools for
studying data from ground-based gravitational-wave detectors.

GWpy provides a user-friendly, intuitive interface to the common
time-domain and frequency-domain data produced by the LIGO and Virgo
observatories and their analyses, with easy-to-follow tutorials at each
step.

%prep
%autosetup -p1 -n gwpy-%{version}
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" gwpy/cli/*.py
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" gwpy/utils/sphinx/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gwpy-plot
%python_clone -a %{buildroot}%{_bindir}/gwpy-rds
%python_clone -a %{buildroot}%{_bindir}/gwpy-tconvert
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Set TMPDIR to a dir in working dir so that tests can write to it
mkdir ./tmp
export TMPDIR=./tmp

# List of tests to disable
# - automatic skips by python-gwpy-connectionerror-test.patch
# - test_fetch_open_data in multiple modules try to connect to
#   gw-openscience.org
# - test_{range,time}.py: required pkgs unavailable for oS
# - all other disabled tests require network conn via nds2
# - test_query_director, test_kerberos: kerberos server needs to be configured
# - test_open_remote*, test_pelican: requests_pelican not packaged
# - test_io_gwf: ldastools-framecpp python module not packaged
# - test_io_hacr: requires pandas (aka kitchen sink)
# - test_from_arrakis: no package for arrakis module
export DISABLE_TESTS="fetch_open_data or nds2 or test_channel \
or test_coherence or test_get_data or test_gravityspy \
or test_gwf or test_gwpy_plot_timeseries or test_io_losc \
or test_qtransform or test_range or test_run or test_spectrogram \
or test_spectrum or test_table or test_time \
or test_to_from_pycbc or test_find_urls \
or test_query_director or test_kerberos \
or test_pelican or test_open_remote or test_scitokens \
or test_io_gwf \
or test_io_hacr \
or test_from_arrakis"

# examples are not installed into buildroot: test via pyargs
%pytest --pyargs gwpy -k "not ($DISABLE_TESTS)"

%post
%python_install_alternative gwpy-plot gwpy-rds gwpy-tconvert

%postun
%python_uninstall_alternative gwpy-plot gwpy-rds gwpy-tconvert

%files %{python_files}
%license LICENSE
%doc README.md examples
%python_alternative %{_bindir}/gwpy-plot
%python_alternative %{_bindir}/gwpy-rds
%python_alternative %{_bindir}/gwpy-tconvert
%{python_sitelib}/gwpy/
%{python_sitelib}/gwpy-%{version}*-info/

%changelog
